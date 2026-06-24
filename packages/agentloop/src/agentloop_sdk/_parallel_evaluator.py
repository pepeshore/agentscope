# -*- coding: utf-8 -*-
"""A simple parallel evaluator that runs solutions concurrently using
asyncio, without requiring Ray.

This module is bundled inside agentloop_sdk so that the SDK can be
installed from PyPI without requiring an unreleased version of agentscope.
"""
import asyncio
import logging
import sys
import time
from typing import Callable, Coroutine, Any

from agentscope.evaluate import (
    EvaluatorBase,
    BenchmarkBase,
    EvaluatorStorageBase,
    SolutionOutput,
    Task,
)

from ._aggregate_mixin import AggregateMixin


class _ProgressBar:
    """Single-line progress bar that coexists with logging output."""

    def __init__(self, total: int, desc: str = "Evaluation") -> None:
        self._total = total
        self._completed = 0
        self._desc = desc
        self._start = time.time()
        self._last_line_len = 0
        self._patched: list[tuple[logging.Handler, type]] = []

    def __enter__(self) -> "_ProgressBar":
        self._patch_stream_handlers()
        return self

    def __exit__(self, *_: object) -> None:
        self.finish()

    def update(self, n: int = 1) -> None:
        self._completed += n
        self._render()

    def finish(self) -> None:
        self._unpatch_stream_handlers()
        self._render()
        sys.stderr.write("\n")
        sys.stderr.flush()

    def _clear_line(self) -> None:
        sys.stderr.write("\r" + " " * self._last_line_len + "\r")
        sys.stderr.flush()

    def _render(self) -> None:
        elapsed = time.time() - self._start
        if self._completed > 0:
            eta = elapsed / self._completed * (self._total - self._completed)
        else:
            eta = 0.0
        pct = self._completed * 100 // self._total
        bar_len = 30
        filled = bar_len * self._completed // self._total
        bar = "█" * filled + "░" * (bar_len - filled)
        line = (
            f"\r{self._desc}: {bar} {pct}% "
            f"({self._completed}/{self._total}) "
            f"[{elapsed:.0f}s, ETA {eta:.0f}s]"
        )
        self._last_line_len = len(line) - 1
        sys.stderr.write(line)
        sys.stderr.flush()

    def _patch_stream_handlers(self) -> None:
        for handler in self._iter_stream_handlers():
            original_cls = type(handler)
            original_emit = original_cls.emit
            pbar = self

            def _make_emit(orig: type) -> type:
                def _emit(self_h: logging.Handler, record: logging.LogRecord) -> None:
                    pbar._clear_line()
                    orig(self_h, record)
                    pbar._render()
                return _emit

            handler.emit = _make_emit(original_emit).__get__(
                handler, original_cls,
            )
            self._patched.append((handler, original_cls))

    def _unpatch_stream_handlers(self) -> None:
        for handler, original_cls in self._patched:
            if hasattr(handler.emit, "__func__"):
                del handler.emit
            else:
                handler.emit = original_cls.emit.__get__(
                    handler, original_cls,
                )
        self._patched.clear()

    @staticmethod
    def _iter_stream_handlers() -> list[logging.Handler]:
        seen: set[int] = set()
        result: list[logging.Handler] = []
        manager = logging.Logger.manager

        loggers: list[logging.Logger] = [logging.getLogger()]
        for ref in manager.loggerDict.values():
            if isinstance(ref, logging.Logger):
                loggers.append(ref)

        for lg in loggers:
            for h in lg.handlers:
                if isinstance(h, logging.StreamHandler) and id(h) not in seen:
                    seen.add(id(h))
                    result.append(h)
        return result


class _InMemoryExporter:
    """Lightweight span exporter that records token usage per task/repeat."""

    def __init__(self) -> None:
        from collections import defaultdict
        self.cnt: dict = {}
        self._defaultdict = defaultdict
        self._stopped = False

    def export(self, spans: Any) -> Any:
        from collections import defaultdict
        from opentelemetry import baggage
        from opentelemetry.sdk.trace.export import SpanExportResult

        try:
            from agentscope.tracing._attributes import (
                SpanAttributes,
                OperationNameValues,
            )
        except ImportError:
            return SpanExportResult.SUCCESS

        for span in spans:
            task_id = baggage.get_baggage("task_id")
            repeat_id = baggage.get_baggage("repeat_id")

            if task_id is None or repeat_id is None:
                continue

            if task_id not in self.cnt:
                self.cnt[task_id] = {}

            if repeat_id not in self.cnt[task_id]:
                self.cnt[task_id][repeat_id] = {
                    "llm": defaultdict(int),
                    "agent": 0,
                    "tool": defaultdict(int),
                    "embedding": defaultdict(int),
                    "chat_usage": {},
                }

            span_kind = span.attributes.get(
                SpanAttributes.GEN_AI_OPERATION_NAME,
            )
            if span_kind == OperationNameValues.CHAT:
                model_name = span.attributes.get(
                    SpanAttributes.GEN_AI_REQUEST_MODEL,
                    "unknown",
                )
                self.cnt[task_id][repeat_id]["llm"][model_name] += 1
                if (
                    model_name
                    not in self.cnt[task_id][repeat_id]["chat_usage"]
                ):
                    self.cnt[task_id][repeat_id]["chat_usage"][
                        model_name
                    ] = defaultdict(int)

                self.cnt[task_id][repeat_id]["chat_usage"][model_name][
                    "input_tokens"
                ] += span.attributes.get(
                    SpanAttributes.GEN_AI_USAGE_INPUT_TOKENS,
                    0,
                )
                self.cnt[task_id][repeat_id]["chat_usage"][model_name][
                    "output_tokens"
                ] += span.attributes.get(
                    SpanAttributes.GEN_AI_USAGE_OUTPUT_TOKENS,
                    0,
                )

            elif span_kind == OperationNameValues.INVOKE_AGENT:
                self.cnt[task_id][repeat_id]["agent"] += 1

            elif span_kind == OperationNameValues.EXECUTE_TOOL:
                tool_name = span.attributes.get(
                    SpanAttributes.GEN_AI_TOOL_NAME,
                    "unknown",
                )
                self.cnt[task_id][repeat_id]["tool"][tool_name] += 1

            elif span_kind == OperationNameValues.EMBEDDINGS:
                embedding_model = span.attributes.get(
                    SpanAttributes.GEN_AI_REQUEST_MODEL,
                    "unknown",
                )
                self.cnt[task_id][repeat_id]["embedding"][
                    embedding_model
                ] += 1

        return SpanExportResult.SUCCESS

    def shutdown(self) -> None:
        self._stopped = True


class ParallelEvaluator(AggregateMixin, EvaluatorBase):
    """A parallel evaluator that runs solutions concurrently with asyncio.

    Uses ``asyncio.Semaphore`` to limit the number of concurrent tasks
    to ``n_workers``, and ``asyncio.gather`` to execute them in parallel.
    No external dependencies (e.g. Ray) are required.
    """

    def __init__(
        self,
        name: str,
        benchmark: BenchmarkBase,
        n_repeat: int,
        storage: EvaluatorStorageBase,
        n_workers: int,
    ) -> None:
        super().__init__(
            name=name,
            benchmark=benchmark,
            n_repeat=n_repeat,
            storage=storage,
        )
        assert n_repeat >= 1, "n_repeat must be at least 1"
        assert n_workers >= 1, "n_workers must be at least 1"

        self.n_workers = n_workers

    async def run(
        self,
        solution: Callable[
            [Task, Callable],
            Coroutine[Any, Any, SolutionOutput],
        ],
    ) -> None:
        from opentelemetry import trace
        from opentelemetry.sdk.trace import TracerProvider
        from opentelemetry.sdk.trace.export import SimpleSpanProcessor

        exporter = _InMemoryExporter()
        span_processor = SimpleSpanProcessor(exporter)

        tracer_provider: TracerProvider = trace.get_tracer_provider()
        if not isinstance(tracer_provider, TracerProvider):
            tracer_provider = TracerProvider()
        tracer_provider.add_span_processor(span_processor)
        trace.set_tracer_provider(tracer_provider)

        await self._save_evaluation_meta()

        semaphore = asyncio.Semaphore(self.n_workers)
        total = len(self.benchmark) * self.n_repeat

        with _ProgressBar(total=total) as pbar:

            async def _run_one(task: Task, repeat_id: str) -> None:
                async with semaphore:
                    await self._run_solution(
                        task,
                        repeat_id,
                        solution,
                        exporter,
                    )
                    pbar.update(1)

            tasks = []
            for task in self.benchmark:
                await self._save_task_meta(task)
                for repeat_id in range(self.n_repeat):
                    tasks.append(_run_one(task, str(repeat_id)))

            await asyncio.gather(*tasks)

        await self.aggregate()

    async def _run_solution(
        self,
        task: Task,
        repeat_id: str,
        solution: Callable[
            [Task, Callable],
            Coroutine[Any, Any, SolutionOutput],
        ],
        exporter: _InMemoryExporter,
    ) -> None:
        if self.storage.solution_result_exists(task.id, repeat_id):
            solution_result = self.storage.get_solution_result(
                task.id,
                repeat_id,
            )
        else:
            from opentelemetry import trace, baggage
            from opentelemetry.context import attach, detach

            tracer = trace.get_tracer(__name__)

            ctx = baggage.set_baggage("task_id", task.id)
            ctx = baggage.set_baggage("repeat_id", repeat_id, context=ctx)
            token = attach(ctx)

            try:
                with tracer.start_as_current_span(
                    name=f"Solution_{task.id}_{repeat_id}",
                ):
                    import agentscope
                    agentscope._config.trace_enabled = True

                    _t0 = time.time()
                    solution_result = await solution(
                        task,
                        self.storage.get_agent_pre_print_hook(
                            task.id,
                            repeat_id,
                        ),
                    )
                    _latency_ms = int((time.time() - _t0) * 1000)
                    if solution_result.meta is None:
                        solution_result.meta = {}
                    solution_result.meta["latency_ms"] = _latency_ms

                    self.storage.save_solution_result(
                        task.id,
                        repeat_id,
                        solution_result,
                    )
            finally:
                detach(token)

        if (
            task.id in exporter.cnt
            and repeat_id in exporter.cnt[task.id]
        ):
            self.storage.save_solution_stats(
                task.id,
                repeat_id,
                exporter.cnt[task.id][repeat_id],
            )

        for metric in task.metrics:
            if not self.storage.evaluation_result_exists(
                task.id,
                repeat_id,
                metric.name,
            ):
                evaluation_results = await task.evaluate(solution_result)
                for result in evaluation_results:
                    self.storage.save_evaluation_result(
                        task_id=task.id,
                        repeat_id=repeat_id,
                        evaluation=result,
                    )
                break
