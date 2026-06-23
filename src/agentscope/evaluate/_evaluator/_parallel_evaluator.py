# -*- coding: utf-8 -*-
"""A simple parallel evaluator that runs solutions concurrently using
asyncio, without requiring Ray."""
import asyncio
from typing import Callable, Coroutine, Any

from ._evaluator_base import EvaluatorBase
from ._general_evaluator import _ProgressBar
from ._in_memory_exporter import _InMemoryExporter
from .._evaluator_storage import EvaluatorStorageBase
from .._task import Task
from .._solution import SolutionOutput
from .._benchmark_base import BenchmarkBase


class ParallelEvaluator(EvaluatorBase):
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
                    from ... import _config

                    _config.trace_enabled = True

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
