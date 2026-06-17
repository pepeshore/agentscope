# -*- coding: utf-8 -*-
"""An AgentLoop (SLS) based evaluator storage that extends FileEvaluatorStorage
to additionally write evaluation results to Alibaba Cloud SLS and upload
experiment records via the AgentLoop API.

Refer to:
https://help.aliyun.com/zh/sls/developer-reference/write-log
"""

import json
import time
import uuid
from typing import Any

from ..._logging import logger
from ._file_evaluator_storage import FileEvaluatorStorage
from .._solution import SolutionOutput
from .._agentloop_config import AgentLoopConfig
from ...types import JSONSerializableObject

# Fixed logstore name for experiment results
EXPERIMENT_LOGSTORE = "experiment_detail"


class AgentLoopEvaluatorStorage(FileEvaluatorStorage):
    """AgentLoop (SLS) based evaluator storage that extends
    FileEvaluatorStorage.

    This storage implementation inherits all functionality from
    FileEvaluatorStorage for local file operations, and additionally writes
    evaluation results to SLS using the PutLogs API.

    The logs written to SLS follow the AgentLoop experiment schema with fields
    like experiment_id, experiment_type, experiment_data, experiment_result,
    experiment_metrics, etc.
    """

    def __init__(
        self,
        save_dir: str,
        config: AgentLoopConfig,
        experiment_id: str | None = None,
        experiment_name: str | None = None,
        experiment_type: str = "agent",
        experiment_metadata: dict | None = None,
        experiment_config: dict | None = None,
    ) -> None:
        """Initialize the AgentLoop evaluator storage.

        Args:
            save_dir (`str`):
                The directory to save evaluation results locally.
            config (`AgentLoopConfig`):
                The AgentLoop configuration containing agent_space, dataset,
                region_id, project, and credentials.
            experiment_id (`str | None`):
                The unique experiment ID. If not provided, a UUID will be
                generated automatically.
            experiment_name (`str | None`):
                A human-readable name for the experiment. When None,
                falls back to ``config.effective_experiment_name`` so the
                benchmark and storage share the same identity.
            experiment_type (`str`):
                The experiment type. Either "model" or "agent".
                Defaults to "agent".
            experiment_metadata (`dict | None`):
                Additional experiment metadata, e.g. {"run_env": "local_run"}.
                Defaults to None.
            experiment_config (`dict | None`):
                The experiment configuration, e.g. model settings or agent
                configuration. When None, falls back to
                ``config.experiment_config``.
        """
        # Initialize parent class
        super().__init__(save_dir=save_dir)

        # Store config reference
        self.config = config
        self.config.validate_credentials()

        self.logstore = EXPERIMENT_LOGSTORE

        # Lazily-initialized cached clients (created on first use)
        self._agentloop_client: Any = None
        self._sls_client: Any = None

        # Resolve SLS project from agent_space if not provided
        if not self.config.project:
            self._resolve_project()

        # Validate evaluators against the platform (skips if already done)
        self.config.validate_evaluators()

        # Experiment identification
        self.experiment_id = experiment_id or str(uuid.uuid4())
        self.experiment_name = (
            experiment_name
            or self.config.effective_experiment_name
        )
        self.experiment_type = experiment_type
        self.experiment_start_time = int(time.time() * 1000)
        self.experiment_metadata = experiment_metadata or {
            "run_env": "local_run",
        }
        self.experiment_config = (
            experiment_config
            if experiment_config is not None
            else self.config.experiment_config
        )

        # Cache for task meta (experiment_data), keyed by task_id
        self._task_meta_cache: dict[str, dict] = {}

        # Tracking counters for upload_experiment
        self._completed_tasks: int = 0
        self._failed_tasks: int = 0
        self._total_tasks: int = 0

    def _get_agentloop_client(self) -> Any:
        """Get the AgentLoop client instance, creating and caching it on
        first call.

        Returns:
            `Client`:
                The AgentLoop client instance.
        """
        if self._agentloop_client is not None:
            return self._agentloop_client

        try:
            from alibabacloud_agentloop20260520.client import Client
            from alibabacloud_tea_openapi import (
                utils_models as open_api_util_models,
            )
        except ImportError as e:
            raise ImportError(
                "The alibabacloud-agentloop20260520 package is required for "
                "AgentLoopEvaluatorStorage. Install it with: "
                "pip install alibabacloud-agentloop20260520",
            ) from e

        client_config = open_api_util_models.Config(
            access_key_id=self.config.access_key_id,
            access_key_secret=self.config.access_key_secret,
        )
        client_config.endpoint = self.config.agentloop_endpoint

        self._agentloop_client = Client(client_config)
        return self._agentloop_client

    def _resolve_project(self) -> None:
        """Resolve SLS project from the agent space.

        Uses the AgentLoop API ``get_agent_space`` to look up the SLS
        project associated with the configured agent space.

        Raises:
            `ValueError`:
                If the SLS project cannot be resolved.
        """
        try:
            from alibabacloud_agentloop20260520 import (
                models as agentloop_models,
            )
        except ImportError as e:
            raise ImportError(
                "The alibabacloud-agentloop20260520 package is required for "
                "AgentLoopEvaluatorStorage. Install it with: "
                "pip install alibabacloud-agentloop20260520",
            ) from e

        client = self._get_agentloop_client()
        req = agentloop_models.GetAgentSpaceRequest()

        resp = client.get_agent_space(
            self.config.agent_space,
            req,
        )
        logger.debug(
            f"AgentLoop get_agent_space response: "
            f"{json.dumps(resp.to_map(), default=str, indent=2)}",
        )

        body = resp.body
        if not body or not body.sls_project:
            raise ValueError(
                f"Failed to get SLS project for agent space "
                f"'{self.config.agent_space}'. "
                "Please ensure the agent space exists and has SLS "
                "configured, or provide 'project' directly in the config.",
            )

        self.config.project = body.sls_project

    def _get_sls_client(self) -> Any:
        """Get the SLS LogClient instance, creating and caching it on first
        call.

        Returns:
            `LogClient`:
                The SLS LogClient instance.
        """
        if self._sls_client is not None:
            return self._sls_client

        try:
            from aliyun.log import LogClient
        except ImportError as e:
            raise ImportError(
                "The aliyun-log-python-sdk package is required for "
                "AgentLoopEvaluatorStorage. Install it with: "
                "pip install aliyun-log-python-sdk",
            ) from e

        self._sls_client = LogClient(
            self.config.sls_endpoint,
            self.config.access_key_id,
            self.config.access_key_secret,
        )
        return self._sls_client

    def _put_log(self, contents: list[tuple[str, str]]) -> None:
        """Write a log entry to SLS.

        Args:
            contents (`list[tuple[str, str]]`):
                The log contents as key-value pairs.
        """
        try:
            from aliyun.log import LogItem, PutLogsRequest
        except ImportError as e:
            raise ImportError(
                "The aliyun-log-python-sdk package is required for "
                "AgentLoopEvaluatorStorage. Install it with: "
                "pip install aliyun-log-python-sdk",
            ) from e

        client = self._get_sls_client()

        log_item = LogItem()
        log_item.set_time(int(time.time()))
        log_item.set_contents(contents)

        request = PutLogsRequest(
            self.config.project,
            self.logstore,
            "",  # topic
            "",  # source
            [log_item],
        )
        client.put_logs(request)

    def _build_base_log_contents(
        self,
        task_id: str | None = None,
        repeat_id: str | None = None,
    ) -> list[tuple[str, str]]:
        """Build the base log contents with common fields.

        Args:
            task_id (`str | None`):
                The task ID if applicable.
            repeat_id (`str | None`):
                The repeat ID if applicable.

        Returns:
            `list[tuple[str, str]]`:
                A list of key-value tuples for log contents.
        """
        contents = [
            ("experiment_id", self.experiment_id),
            ("experiment_name", self.experiment_name),
            ("experiment_start_time", str(self.experiment_start_time)),
            ("experiment_type", self.experiment_type),
            (
                "experiment_metadata",
                json.dumps(self.experiment_metadata, ensure_ascii=False),
            ),
            (
                "experiment_config",
                json.dumps(self.experiment_config, ensure_ascii=False),
            ),
        ]

        if task_id is not None:
            contents.append(("task_id", task_id))
        if repeat_id is not None:
            contents.append(("repeat_id", repeat_id))

        return contents

    def save_solution_result(
        self,
        task_id: str,
        repeat_id: str,
        output: SolutionOutput,
        **kwargs: Any,
    ) -> None:
        """Save the solution result to both local file and SLS.

        This method writes the complete experiment record to SLS, including:
        - experiment_data: from cached task meta
        - data_config: dataset configuration
        - experiment_result: the solution output

        Args:
            task_id (`str`):
                The task ID.
            repeat_id (`str`):
                The repeat ID for the task.
            output (`SolutionOutput`):
                The solution output to be saved.
        """
        # First, save to local file using parent class.
        # This must succeed before attempting the SLS write.
        super().save_solution_result(
            task_id=task_id,
            repeat_id=repeat_id,
            output=output,
            **kwargs,
        )

        # Track task completion for upload_experiment
        if output.success:
            self._completed_tasks += 1
        else:
            self._failed_tasks += 1

        # Then, write to SLS. Failures are logged as warnings so that a
        # transient network / permission issue does not abort the evaluation.
        try:
            contents = self._build_base_log_contents(
                task_id=task_id,
                repeat_id=repeat_id,
            )
            # Get cached experiment_data
            experiment_data = self._task_meta_cache.get(task_id, {})

            # Add data_config field
            data_config = {
                "data_type": "dataset",
                "project": self.config.project,
                "dataset_id": self.config.dataset,
                "dataset_item_id": experiment_data.get("input", {}).get(
                    "id",
                    task_id,
                ),
            }
            contents.append(
                (
                    "data_config",
                    json.dumps(data_config, ensure_ascii=False),
                ),
            )

            # Add experiment_data field
            contents.append(
                (
                    "experiment_data",
                    json.dumps(
                        experiment_data.get("input", {}),
                        ensure_ascii=False,
                        default=str,
                    ),
                ),
            )

            # Add experiment_result field with output data
            result_data = {
                "success": output.success,
                "output": output.output,
                "trajectory": output.trajectory,
                "meta": output.meta,
            }
            contents.append(
                (
                    "experiment_output",
                    json.dumps(result_data, ensure_ascii=False, default=str),
                ),
            )
            self._put_log(contents)
        except Exception as e:
            logger.warning(
                f"Failed to write task '{task_id}' result to SLS "
                f"(local file already saved): {e}",
            )
        finally:
            # Release cached task meta to avoid unbounded memory growth
            self._task_meta_cache.pop(task_id, None)

    def save_task_meta(
        self,
        task_id: str,
        meta_info: dict[str, JSONSerializableObject],
    ) -> None:
        """Save the task meta information to local file and cache for
        later use.

        The task meta (experiment_data) is cached and will be written to SLS
        together with the solution result in save_solution_result().

        Args:
            task_id (`str`):
                The task ID.
            meta_info (`dict[str, JSONSerializableObject]`):
                The task meta information to be saved.
        """
        # Save to local file using parent class
        super().save_task_meta(
            task_id=task_id,
            meta_info=meta_info,
        )

        # Cache the meta_info for later use in save_solution_result
        self._task_meta_cache[task_id] = meta_info

        # Track total tasks
        self._total_tasks += 1

    def upload_experiment_record(
        self,
        aggregation_result: dict,
    ) -> None:
        """Upload the experiment record to AgentLoop via the
        ``upload_experiment`` API.

        Args:
            aggregation_result (`dict`):
                The aggregated evaluation results.
        """
        try:
            from alibabacloud_agentloop20260520 import (
                models as agentloop_models,
            )
        except ImportError as e:
            raise ImportError(
                "The alibabacloud-agentloop20260520 package is required for "
                "AgentLoopEvaluatorStorage. Install it with: "
                "pip install alibabacloud-agentloop20260520",
            ) from e

        client = self._get_agentloop_client()

        data_source = {
            "type": "DATASET_FULL",
            "datasetId": self.config.dataset,
        }

        evaluator_models = None
        if self.config.evaluators:
            evaluator_models = [
                agentloop_models.Evaluator(
                    evaluator_ref=e.evaluator_ref or None,
                    name=e.name or None,
                    type=e.type or None,
                    result_name=e.result_name or None,
                    result_type=e.result_type or None,
                    filters=e.filters,
                    config=e.config,
                    variable_mapping=e.variable_mapping,
                )
                for e in self.config.evaluators
            ]

        req = agentloop_models.UploadExperimentRequest(
            record_id=self.experiment_id,
            total_tasks=self._total_tasks,
            completed_tasks=self._completed_tasks,
            failed_tasks=self._failed_tasks,
            data_source=data_source,
            experiment_config=agentloop_models.ExperimentConfig(
                name=self.experiment_name,
            ),
            evaluators=evaluator_models,
        )

        try:
            resp = client.upload_experiment(
                self.config.agent_space,
                req,
            )
            logger.info(
                f"Uploaded experiment record '{self.experiment_id}' to "
                f"AgentLoop. Response: "
                f"{json.dumps(resp.to_map(), default=str, indent=2)}",
            )
        except Exception as e:
            logger.warning(
                f"Failed to upload experiment record "
                f"'{self.experiment_id}' to AgentLoop: {e}",
            )

    def save_aggregation_result(
        self,
        aggregation_result: dict,
        **kwargs: Any,
    ) -> None:
        """Save the aggregation result to local file and upload the
        experiment record to AgentLoop.

        Args:
            aggregation_result (`dict`):
                A dictionary containing the aggregation result.
        """
        super().save_aggregation_result(
            aggregation_result=aggregation_result,
            **kwargs,
        )

        self.upload_experiment_record(aggregation_result)
