# -*- coding: utf-8 -*-
"""AgentLoop SDK: Evaluation tools for the AgentLoop platform."""

from ._agentloop_config import AgentLoopConfig, EvaluatorConfig
from ._agentloop_benchmark import AgentLoopBenchmark
from ._evaluator_storage import AgentLoopEvaluatorStorage
from ._solutions import (
    HttpRequestSpec,
    http_solution,
    http_solution_with,
    command_solution,
    command_solution_with,
)
from ._experiment import run_experiment, run_experiment_parallel
from ._parallel_evaluator import ParallelEvaluator
from ._general_evaluator import AgentLoopGeneralEvaluator

from agentscope.evaluate import (
    Task,
    SolutionOutput,
    BenchmarkBase,
    EvaluatorStorageBase,
    FileEvaluatorStorage,
    GeneralEvaluator,
    RayEvaluator,
    MetricBase,
    MetricResult,
    MetricType,
)

__all__ = [
    "AgentLoopConfig",
    "EvaluatorConfig",
    "AgentLoopBenchmark",
    "AgentLoopEvaluatorStorage",
    "HttpRequestSpec",
    "http_solution",
    "http_solution_with",
    "command_solution",
    "command_solution_with",
    "run_experiment",
    "run_experiment_parallel",
    "Task",
    "SolutionOutput",
    "BenchmarkBase",
    "EvaluatorStorageBase",
    "FileEvaluatorStorage",
    "GeneralEvaluator",
    "AgentLoopGeneralEvaluator",
    "ParallelEvaluator",
    "RayEvaluator",
    "MetricBase",
    "MetricResult",
    "MetricType",
]
