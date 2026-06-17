# -*- coding: utf-8 -*-
"""
AgentLoop Integration Example - Load dataset from Agentloop dataset and write results to SLS

Credentials are read from environment variables (AGENTLOOP_AK / AGENTLOOP_SK)
or a .env file in the project root.
"""

import asyncio
import logging
from typing import Callable

from agentscope.evaluate import (
    AgentLoopConfig,
    EvaluatorConfig,
    GeneralEvaluator,
    SolutionOutput,
    Task,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def run_agentloop_experiment(
    config: AgentLoopConfig,
    solution_fn: Callable,
    result_dir: str = "./results",
) -> None:
    """Run evaluation using AgentLoop.

    Args:
        config: AgentLoop configuration. Includes experiment_name and
            experiment_config; both benchmark and storage read from it.
        solution_fn: The solution function to evaluate.
        result_dir: Local result storage directory.
    """
    logger.info("=" * 60)
    logger.info("Running AgentLoop Evaluation")
    logger.info("=" * 60)

    try:
        from agentscope.evaluate import (
            AgentLoopBenchmark,
            AgentLoopEvaluatorStorage,
        )
    except ImportError as e:
        logger.error("Import error: %s", e)
        logger.error(
            "Please install the required Agentloop SDKs:\n"
            "  pip install aliyun-log-python-sdk alibabacloud-agentloop20260520")
        return

    # Validate evaluators before loading dataset (fast-fail)
    config.validate_evaluators()

    # Load dataset from AgentLoop
    logger.info("Loading dataset from AgentLoop:")
    logger.info("  Agent Space: %s", config.agent_space)
    logger.info("  Dataset:     %s", config.dataset)
    logger.info("  Region ID:   %s", config.region_id)
    benchmark = AgentLoopBenchmark(
        config=config,
        description=f"Benchmark from AgentLoop: "
                    f"{config.agent_space}/{config.dataset}",
    )
    logger.info("Loaded %d tasks", len(benchmark))

    # Configure storage
    logger.info("Using SLS to store results:")
    logger.info("  Agent Space: %s", config.agent_space)
    logger.info("  Region ID:   %s", config.region_id)
    logger.info("Also saving locally to: %s", result_dir)
    storage = AgentLoopEvaluatorStorage(
        save_dir=result_dir,
        config=config,
        experiment_type="agent",
        experiment_metadata={"run_env": "local_run"},
    )
    logger.info("  Project:      %s", storage.config.project)
    logger.info("  SLS Endpoint: %s", storage.config.sls_endpoint)
    logger.info("  Logstore:     %s", storage.logstore)
    logger.info("Experiment ID: %s", storage.experiment_id)

    # Run experiment
    evaluator = GeneralEvaluator(
        name="AgentLoop Evaluation",
        benchmark=benchmark,
        n_repeat=1,
        storage=storage,
        n_workers=4,
    )

    logger.info("Starting experiment...")
    await evaluator.run(solution_fn)
    logger.info("Experiment completed!")


async def main() -> None:
    """Main function"""
    # Load .env file if python-dotenv is available
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        pass

    # AK/SK are read from env vars: AGENTLOOP_AK / AGENTLOOP_SK
    # (or ALIBABA_CLOUD_ACCESS_KEY_ID / ALIBABA_CLOUD_ACCESS_KEY_SECRET)
    config = AgentLoopConfig(
        agent_space="default-cn-hangzhou",
        dataset="cc_dataset",
        region_id="cn-hangzhou",
        experiment_name="Offline—Experiment-Baseline",
        experiment_config={"agent_name": "LocalAgent"},
        evaluators=[
            EvaluatorConfig(
                evaluator_ref="Builtin.agent_correctness",
                result_type="score",
                variable_mapping={
                    "input": "experiment_input",
                    "output": "experiment_output.output",
                    "expected_output": "experiment_data.expected_output",
                },
            ),
        ],
        custom_agentloop_endpoint="agentloop-pre.cn-hangzhou.aliyuncs.com",
    )

    await run_agentloop_experiment(
        config=config,
        solution_fn=http_agent_solution,
        result_dir="./results",
    )

# ============ HTTP Agent Solution ============
async def http_agent_solution(
    task: Task,
    pre_hook: Callable,
) -> SolutionOutput:
    output = task.input.get("expected_output")  # call your agent and get the output

    return SolutionOutput(
        success=True,
        output=output,
        trajectory=[],
        meta={
            "task": task.input,
        },
    )

if __name__ == "__main__":
    asyncio.run(main())
