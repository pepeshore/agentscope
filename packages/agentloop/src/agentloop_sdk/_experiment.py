# -*- coding: utf-8 -*-
"""High-level experiment runner functions for the AgentLoop SDK."""
import asyncio
from typing import Callable, Coroutine, Any

from agentscope._logging import logger
from agentscope.evaluate import SolutionOutput
from ._general_evaluator import AgentLoopGeneralEvaluator
from ._agentloop_config import AgentLoopConfig
from ._agentloop_benchmark._agentloop_benchmark import AgentLoopBenchmark
from ._evaluator_storage._agentloop_evaluator_storage import (
    AgentLoopEvaluatorStorage,
)


async def _run(
    config: AgentLoopConfig,
    solution_fn: Callable,
    result_dir: str,
    n_repeat: int,
    n_workers: int,
    parallel: bool,
) -> None:
    config.resolve_experiment_plan()
    config.validate_evaluators()

    benchmark = AgentLoopBenchmark(
        config=config,
        description=(
            f"Benchmark from AgentLoop: "
            f"{config.agent_space}/{config.dataset}"
        ),
    )

    storage = AgentLoopEvaluatorStorage(
        save_dir=result_dir,
        config=config,
        experiment_type="agent",
        experiment_metadata={"run_env": "local_run"},
    )

    if parallel:
        from ._parallel_evaluator import ParallelEvaluator

        evaluator = ParallelEvaluator(
            name="AgentLoop Evaluation",
            benchmark=benchmark,
            n_repeat=n_repeat,
            storage=storage,
            n_workers=n_workers,
        )
    else:
        evaluator = AgentLoopGeneralEvaluator(
            name="AgentLoop Evaluation",
            benchmark=benchmark,
            n_repeat=n_repeat,
            storage=storage,
            n_workers=n_workers,
        )

    mode = "parallel" if parallel else "serial"
    logger.info(
        "Experiment %s | %s | %d tasks | %s, n_workers=%d",
        storage.experiment_id,
        config.dataset,
        len(benchmark),
        mode,
        n_workers,
    )
    await evaluator.run(solution_fn)
    logger.info("Experiment %s completed", storage.experiment_id)


async def run_experiment(
    config: AgentLoopConfig,
    solution_fn: Callable[..., Coroutine[Any, Any, SolutionOutput]],
    result_dir: str = "./results",
    n_repeat: int = 1,
    n_workers: int = 1,
) -> None:
    """Run an experiment serially using ``GeneralEvaluator``.

    Args:
        config (`AgentLoopConfig`):
            AgentLoop configuration (credentials, dataset, evaluators, etc.).
        solution_fn (`Callable`):
            An async solution function compatible with evaluator.run().
        result_dir (`str`):
            Local directory for saving results. Defaults to ``"./results"``.
        n_repeat (`int`):
            How many times to repeat each task. Defaults to 1.
        n_workers (`int`):
            Number of workers (for GeneralEvaluator this controls internal
            concurrency). Defaults to 1.
    """
    await _run(
        config=config,
        solution_fn=solution_fn,
        result_dir=result_dir,
        n_repeat=n_repeat,
        n_workers=n_workers,
        parallel=False,
    )


async def run_experiment_parallel(
    config: AgentLoopConfig,
    solution_fn: Callable[..., Coroutine[Any, Any, SolutionOutput]],
    result_dir: str = "./results",
    n_repeat: int = 1,
    n_workers: int = 4,
) -> None:
    """Run an experiment in parallel using ``ParallelEvaluator``.

    Args:
        config (`AgentLoopConfig`):
            AgentLoop configuration (credentials, dataset, evaluators, etc.).
        solution_fn (`Callable`):
            An async solution function compatible with evaluator.run().
        result_dir (`str`):
            Local directory for saving results. Defaults to ``"./results"``.
        n_repeat (`int`):
            How many times to repeat each task. Defaults to 1.
        n_workers (`int`):
            Maximum number of concurrent tasks. Defaults to 4.
    """
    await _run(
        config=config,
        solution_fn=solution_fn,
        result_dir=result_dir,
        n_repeat=n_repeat,
        n_workers=n_workers,
        parallel=True,
    )
