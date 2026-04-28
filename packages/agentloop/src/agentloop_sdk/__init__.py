# -*- coding: utf-8 -*-
"""AgentLoop SDK: Evaluation tools for the AgentLoop platform."""

from ._agentloop_config import AgentLoopConfig
from ._agentloop_benchmark import AgentLoopBenchmark
from ._evaluator_storage import AgentLoopEvaluatorStorage

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
    "AgentLoopBenchmark",
    "AgentLoopEvaluatorStorage",
    "Task",
    "SolutionOutput",
    "BenchmarkBase",
    "EvaluatorStorageBase",
    "FileEvaluatorStorage",
    "GeneralEvaluator",
    "RayEvaluator",
    "MetricBase",
    "MetricResult",
    "MetricType",
]
