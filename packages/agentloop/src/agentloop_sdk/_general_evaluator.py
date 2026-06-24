# -*- coding: utf-8 -*-
"""A thin subclass of GeneralEvaluator that adds a progress bar."""
import time
from typing import Callable, Coroutine, Awaitable, Any

from agentscope.evaluate import GeneralEvaluator, Task, SolutionOutput

from ._aggregate_mixin import AggregateMixin
from ._parallel_evaluator import _ProgressBar, _InMemoryExporter


class AgentLoopGeneralEvaluator(AggregateMixin, GeneralEvaluator):
    """GeneralEvaluator with a progress bar overlay.

    Inherits all logic from the PyPI version of ``GeneralEvaluator`` and
    only overrides ``run()`` to wrap the execution loop in a progress bar,
    and ``run_solution()`` to inject per-task latency into
    ``SolutionOutput.meta``.
    """

    async def run_solution(
        self,
        repeat_id: str,
        task: Task,
        solution: Callable[[Task, Callable], Awaitable[SolutionOutput]],
    ) -> None:
        """Override to measure solution latency before delegating."""
        if self.storage.solution_result_exists(task.id, repeat_id):
            return await super().run_solution(repeat_id, task, solution)

        original_solution = solution

        async def _timed_solution(
            t: Task,
            pre_hook: Callable,
        ) -> SolutionOutput:
            t0 = time.time()
            result = await original_solution(t, pre_hook)
            latency_ms = int((time.time() - t0) * 1000)
            if result.meta is None:
                result.meta = {}
            result.meta["latency_ms"] = latency_ms
            return result

        await super().run_solution(repeat_id, task, _timed_solution)

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
