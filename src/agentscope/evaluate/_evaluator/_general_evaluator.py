# -*- coding: utf-8 -*-
"""General evaluator implementation in AgentScope, which is easy to debug
compared to the RayEvaluator."""
import logging
import sys
import time
from typing import Callable, Awaitable, Coroutine, Any

from ._evaluator_base import EvaluatorBase
from ._in_memory_exporter import _InMemoryExporter
from .._evaluator_storage import EvaluatorStorageBase
from .._task import Task
from .._solution import SolutionOutput
from .._benchmark_base import BenchmarkBase


class _ProgressBar:
    """Single-line progress bar that coexists with logging output.

    Intercepts all ``StreamHandler`` instances attached to any active logger
    so that log lines are printed *above* the progress bar instead of
    overwriting it.  Non-stream handlers (file, socket, …) are left untouched.
    On ``finish()`` / context-manager exit every handler is restored.
    """

    def __init__(self, total: int, desc: str = "Evaluation") -> None:
        self._total = total
        self._completed = 0
        self._desc = desc
        self._start = time.time()
        self._last_line_len = 0
        self._patched: list[
            tuple[logging.Handler, type]
        ] = []

    # -- context manager --------------------------------------------------

    def __enter__(self) -> "_ProgressBar":
        self._patch_stream_handlers()
        return self

    def __exit__(self, *_: object) -> None:
        self.finish()

    # -- public API -------------------------------------------------------

    def update(self, n: int = 1) -> None:
        self._completed += n
        self._render()

    def finish(self) -> None:
        self._unpatch_stream_handlers()
        self._render()
        sys.stderr.write("\n")
        sys.stderr.flush()

    # -- rendering --------------------------------------------------------

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

    # -- handler patching -------------------------------------------------

    def _patch_stream_handlers(self) -> None:
        """Replace the ``emit`` of every ``StreamHandler`` in the logger tree
        with a wrapper that clears / redraws the progress line."""
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

            handler.emit = _make_emit(original_emit).__get__(  # type: ignore[assignment]
                handler, original_cls,
            )
            self._patched.append((handler, original_cls))

    def _unpatch_stream_handlers(self) -> None:
        for handler, original_cls in self._patched:
            if hasattr(handler.emit, "__func__"):
                del handler.emit  # type: ignore[misc]
            else:
                handler.emit = original_cls.emit.__get__(  # type: ignore[assignment]
                    handler, original_cls,
                )
        self._patched.clear()

    @staticmethod
    def _iter_stream_handlers() -> list[logging.Handler]:
        """Collect all ``StreamHandler`` instances in the logger manager."""
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


class GeneralEvaluator(EvaluatorBase):
    """The general evaluator that support users to debug their evaluation"""

    def __init__(
        self,
        name: str,
        benchmark: BenchmarkBase,
        n_repeat: int,
        storage: EvaluatorStorageBase,
        n_workers: int,
    ) -> None:
        """Initialize the evaluator."""
        super().__init__(
            name=name,
            benchmark=benchmark,
            n_repeat=n_repeat,
            storage=storage,
        )

        assert isinstance(benchmark, BenchmarkBase)

        assert n_repeat >= 1, "n_repeat must be at least 1"

        assert n_workers >= 1, "n_workers must be at least 1"

        self.benchmark = benchmark
        self.n_repeat = n_repeat
        self.n_workers = n_workers

    async def run_evaluation(
        self,
        task: Task,
        repeat_id: str,
        solution_output: SolutionOutput,
    ) -> None:
        """Run the evaluation for a task and solution result."""
        evaluation_results = await task.evaluate(solution_output)
        # store the evaluation result
        for result in evaluation_results:
            self.storage.save_evaluation_result(
                task_id=task.id,
                repeat_id=repeat_id,
                evaluation=result,
            )

    async def run_solution(
        self,
        repeat_id: str,
        task: Task,
        solution: Callable[[Task, Callable], Awaitable[SolutionOutput]],
    ) -> None:
        """Generate a solution to a task and evaluate."""
        if self.storage.solution_result_exists(task.id, repeat_id):
            # Obtain from storage
            solution_result = self.storage.get_solution_result(
                task.id,
                repeat_id,
            )

        else:
            from opentelemetry import trace
            from opentelemetry.context import attach, detach
            from opentelemetry import baggage

            tracer = trace.get_tracer(__name__)

            # Set baggage
            ctx = baggage.set_baggage("task_id", task.id)
            ctx = baggage.set_baggage("repeat_id", repeat_id, context=ctx)

            # Activate the context
            token = attach(ctx)

            try:
                with tracer.start_as_current_span(
                    name=f"Solution_{task.id}_{repeat_id}",
                ):
                    from ... import _config

                    _config.trace_enabled = True

                    # Run the solution
                    solution_result = await solution(
                        task,
                        self.storage.get_agent_pre_print_hook(
                            task.id,
                            repeat_id,
                        ),
                    )
                    self.storage.save_solution_result(
                        task.id,
                        repeat_id,
                        solution_result,
                    )
            finally:
                detach(token)

        # Evaluate the solution with the
        for metric in task.metrics:
            if not self.storage.evaluation_result_exists(
                task.id,
                repeat_id,
                metric.name,
            ):
                await self.run_evaluation(
                    task,
                    repeat_id,
                    solution_result,
                )

    async def run(
        self,
        solution: Callable[
            [Task, Callable],
            Coroutine[Any, Any, SolutionOutput],
        ],
    ) -> None:
        """Run the ray-based distributed and parallel evaluation, and get the
        results.

        Args:
            solution (`Callable[[Task, Callable], Coroutine[Any, Any, \
            SolutionOutput]]`):
                A async function that takes a `Task` instance and a pre-print
                hook function as input, returns a `SolutionOutput` instance.
        """

        from opentelemetry import trace
        from opentelemetry.sdk.trace import TracerProvider
        from opentelemetry.sdk.trace.export import SimpleSpanProcessor

        exporter = _InMemoryExporter()
        span_processor = SimpleSpanProcessor(exporter)

        tracer_provider: TracerProvider = trace.get_tracer_provider()
        if not isinstance(tracer_provider, TracerProvider):
            # Create a new tracer provider if not exists
            tracer_provider = TracerProvider()
        tracer_provider.add_span_processor(span_processor)
        trace.set_tracer_provider(tracer_provider)

        await self._save_evaluation_meta()

        total = len(self.benchmark) * self.n_repeat

        with _ProgressBar(total=total) as pbar:
            for task in self.benchmark:
                await self._save_task_meta(task)

                for repeat_id in range(self.n_repeat):
                    await self.run_solution(
                        str(repeat_id),
                        task,
                        solution,
                    )

                    # Save the exporter data
                    if (
                        task.id in exporter.cnt
                        and str(repeat_id) in exporter.cnt[task.id]
                    ):
                        self.storage.save_solution_stats(
                            task.id,
                            str(repeat_id),
                            exporter.cnt[task.id][str(repeat_id)],
                        )

                    pbar.update(1)

        await self.aggregate()
