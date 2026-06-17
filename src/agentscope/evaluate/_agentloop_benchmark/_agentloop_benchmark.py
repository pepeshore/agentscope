# -*- coding: utf-8 -*-
"""The AgentLoop benchmark class for loading evaluation datasets."""

import json
import uuid
from typing import Any, Generator

from ..._logging import logger
from .._benchmark_base import BenchmarkBase
from .._task import Task
from .._agentloop_config import AgentLoopConfig


class AgentLoopBenchmark(BenchmarkBase):
    """The AgentLoop benchmark for loading evaluation datasets from
    Alibaba Cloud AgentLoop platform.

    This benchmark allows users to load evaluation datasets directly from
    AgentLoop by specifying the agent space and dataset names. The data is
    queried using the AgentLoop SDK and converted to Task objects.

    Install the required SDK:
        pip install alibabacloud-agentloop20260520
    """

    def __init__(
        self,
        config: AgentLoopConfig,
        name: str = "",
        description: str = "Benchmark loaded from AgentLoop.",
    ) -> None:
        """Initialize the AgentLoopBenchmark.

        Args:
            config (`AgentLoopConfig`):
                The AgentLoop configuration containing agent_space, dataset,
                region_id, query, and credentials.
            name (`str`):
                The name of this benchmark. When empty, defaults to
                ``config.effective_experiment_name`` so the benchmark and
                storage advertise the same identity.
            description (`str`):
                A brief description of this benchmark.
                Defaults to "Benchmark loaded from AgentLoop.".
        """
        super().__init__(
            name=name or config.effective_experiment_name,
            description=description,
        )

        self.config = config
        self.config.validate_credentials()

        # Define task_converter
        def task_converter(log_record: dict) -> Task:
            # Generate a random ID for each task
            task_id = str(uuid.uuid4())
            # Get ground_truth from configured field,
            # empty string if not configured
            ground_truth = ""
            if config.ground_truth_field:
                ground_truth = log_record.get(config.ground_truth_field, "")

            return Task(
                id=task_id,
                input=log_record,
                ground_truth=ground_truth,
                metrics=[],
                metadata={},
            )

        # Load dataset and convert to Task objects
        # Convert once and cache to ensure stable task IDs
        raw_dataset = self._load_data()
        self._tasks: list[Task] = [
            task_converter(item) for item in raw_dataset
        ]

    def _get_client(self) -> Any:
        """Get the AgentLoop client instance.

        Returns:
            `Client`:
                The AgentLoop client instance.

        Raises:
            `ImportError`:
                If the alibabacloud-agentloop20260520 package is not installed.
        """
        try:
            from alibabacloud_agentloop20260520.client import Client
            from alibabacloud_tea_openapi import (
                utils_models as open_api_util_models,
            )
        except ImportError as e:
            raise ImportError(
                "The alibabacloud-agentloop20260520 package is required for "
                "AgentLoopBenchmark. Install it with: "
                "pip install alibabacloud-agentloop20260520",
            ) from e

        client_config = open_api_util_models.Config(
            access_key_id=self.config.access_key_id,
            access_key_secret=self.config.access_key_secret,
        )
        client_config.endpoint = self.config.agentloop_endpoint

        return Client(client_config)

    def _parse_response_data(
        self,
        columns: list[str] | None,
        rows: list[list[Any]] | None,
    ) -> list[dict]:
        """Parse columns and rows from an ExecuteQuery response into dicts.

        Args:
            columns:
                The column names from the response.
            rows:
                The row data from the response, where each row is a list
                of values corresponding to the columns.

        Returns:
            `list[dict]`:
                A list of parsed data records.
        """
        if not columns or not rows:
            return []
        return [dict(zip(columns, row)) for row in rows]

    # Number of records fetched per paginated request
    _PAGE_SIZE: int = 100

    def _execute_query_request(
        self,
        client: Any,
        agentloop_models: Any,
        agent_space: str,
        query: str,
    ) -> list[dict]:
        """Execute a single ExecuteQuery request and return parsed records.

        Args:
            client:
                The AgentLoop client instance.
            agentloop_models:
                The AgentLoop models module.
            agent_space (`str`):
                The agent space name.
            query (`str`):
                The SQL query string to execute.

        Returns:
            `list[dict]`:
                Parsed records from the response, or an empty list if the
                response contains no data.

        Raises:
            `RuntimeError`:
                If the API call fails.
        """
        req = agentloop_models.ExecuteQueryRequest(
            type="SQL",
            query=query,
        )
        try:
            resp = client.execute_query(
                agent_space,
                self.config.dataset,
                req,
            )
        except Exception as e:
            raise RuntimeError(
                f"Failed to query dataset '{self.config.dataset}' "
                f"in agent space '{agent_space}': {e}",
            ) from e

        logger.debug(json.dumps(resp.to_map(), default=str, indent=2))

        if resp.body:
            return self._parse_response_data(
                resp.body.columns,
                resp.body.rows,
            )
        return []

    def _load_data(self) -> list[dict]:
        """Load the dataset from AgentLoop.

        - If ``config.query`` is set, executes it as-is in a single call.
        - Otherwise, uses LIMIT/OFFSET pagination to load up to
          ``config.max_rows`` records, stopping early when a page returns
          no data or the API raises an error.

        Returns:
            `list[dict]`:
                A list of data records loaded from AgentLoop.

        Raises:
            `ImportError`:
                If the alibabacloud-agentloop20260520 package is not installed.
            `RuntimeError`:
                If the API call fails (single-query mode only).
        """
        try:
            from alibabacloud_agentloop20260520 import (
                models as agentloop_models,
            )
        except ImportError as e:
            raise ImportError(
                "The alibabacloud-agentloop20260520 package is required for "
                "AgentLoopBenchmark. Install it with: "
                "pip install alibabacloud-agentloop20260520",
            ) from e

        client = self._get_client()
        agent_space = self.config.agent_space

        logger.info(
            f"AgentLoop agent_space: {agent_space}, "
            f"dataset: {self.config.dataset}",
        )

        if self.config.query:
            logger.info(f"Custom query: {self.config.query}")
            return self._execute_query_request(
                client,
                agentloop_models,
                agent_space,
                self.config.query,
            )

        # No custom query: paginate with LIMIT/OFFSET up to max_rows
        escaped_dataset = self.config.dataset.replace("`", "``")
        dataset: list[dict] = []

        while len(dataset) < self.config.max_rows:
            remaining = self.config.max_rows - len(dataset)
            page_size = min(self._PAGE_SIZE, remaining)
            offset = len(dataset)
            page_query = (
                f"* | select * from `{escaped_dataset}` "
                f"ORDER BY id LIMIT {offset}, {page_size}"
            )
            logger.info(
                f"Paginated query "
                f"(offset={offset}, limit={page_size}): {page_query}",
            )
            try:
                page = self._execute_query_request(
                    client,
                    agentloop_models,
                    agent_space,
                    page_query,
                )
            except RuntimeError as e:
                logger.warning(
                    f"Paginated query failed at offset {offset}, "
                    f"stopping early: {e}",
                )
                break

            if not page:
                logger.info(
                    f"Empty response at offset {offset}, stopping pagination.",
                )
                break

            dataset.extend(page)
            if len(dataset) >= self.config.max_rows:
                dataset = dataset[: self.config.max_rows]
                break

        logger.info(f"Loaded {len(dataset)} records from AgentLoop.")

        ids = [r.get("id", "") for r in dataset]
        unique_ids = set(ids)
        if len(ids) != len(unique_ids):
            from collections import Counter
            dups = {
                k: v for k, v in Counter(ids).items() if v > 1
            }
            logger.warning(
                f"Duplicate records detected! Total: {len(ids)}, "
                f"Unique: {len(unique_ids)}, "
                f"Duplicates: {dups}",
            )
        else:
            logger.info(
                f"No duplicate records. {len(unique_ids)} unique IDs.",
            )

        return dataset

    def __iter__(self) -> Generator[Task, None, None]:
        """Iterate over the benchmark, yielding Task objects.

        Yields:
            `Task`:
                Task objects converted from data records.
        """
        for task in self._tasks:
            yield task

    def __getitem__(self, index: int) -> Task:
        """Get a task by index.

        Args:
            index (`int`):
                The index of the task.

        Returns:
            `Task`:
                The Task object at the given index.
        """
        return self._tasks[index]

    def __len__(self) -> int:
        """Get the number of tasks in the benchmark.

        Returns:
            `int`:
                The number of tasks.
        """
        return len(self._tasks)
