# -*- coding: utf-8 -*-
"""
AgentLoop Integration Example

Credentials are read from environment variables (AGENTLOOP_AK / AGENTLOOP_SK)
or a .env file in the project root.
"""

import asyncio
import logging

from agentloop_sdk import (
    AgentLoopConfig,
    EvaluatorConfig,
    http_solution_with,
    run_experiment,
    run_experiment_parallel,
)

logging.basicConfig(level=logging.INFO)

# ============ HTTP Agent Solution ============
AGENT_ENDPOINT = (
    "https://1108555361245511.agentrun-data.cn-hangzhou.aliyuncs.com"
    "/agent-runtimes/agent-code-iwukV/endpoints/Default/invocations"
    "/compatible-mode/v1/responses"
)
AGENT_KEY = "ahsudhaofhaohfauihfiau"


async def main() -> None:
    # Load .env file if python-dotenv is available
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        pass

    config = AgentLoopConfig(
        agent_space="default-cn-hangzhou",
        dataset="cc_dataset",
        region_id="cn-hangzhou",
        experiment_name="Offline—Experiment-LocalAgent",
        experiment_config={"agent_name": "LocalAgent"},
        evaluators=[
            EvaluatorConfig(
                evaluator_ref="Builtin.agent_correctness",
                result_type="score",
                variable_mapping={
                    "input": "experiment_input",
                    "output": "experiment_output",
                    "expected_output": "dataset.expected_output",
                },
            ),
        ],
        custom_agentloop_endpoint="agentloop-pre.cn-hangzhou.aliyuncs.com",
    )

    solution_fn = http_solution_with(
        url=AGENT_ENDPOINT,
        headers={"key": AGENT_KEY},
        body_builder=lambda task: {
            "input": task.input.get("input", ""),
            "stream": False,
        },
        timeout=60,
    )

    # Serial execution
    # await run_experiment(config=config, solution_fn=solution_fn)

    # Parallel execution (4 concurrent tasks)
    await run_experiment_parallel(
        config=config,
        solution_fn=solution_fn,
        n_workers=4,
    )


if __name__ == "__main__":
    asyncio.run(main())
