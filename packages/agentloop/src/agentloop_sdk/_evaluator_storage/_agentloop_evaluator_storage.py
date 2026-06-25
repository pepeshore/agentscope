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

from agentscope._logging import logger
from agentscope.evaluate import FileEvaluatorStorage, SolutionOutput
from agentscope.types import JSONSerializableObject
from .._agentloop_config import AgentLoopConfig

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
        from datetime import datetime
        _ts = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        self._base_experiment_name = (
            experiment_name or self.config.effective_experiment_name
        )
        self.experiment_name = f"{self.config.plan_name} {_ts}"
        self.experiment_type = experiment_type
        self.experiment_start_time = int(time.time() * 1000)
        self.experiment_metadata = {
            "run_env": "local_run",
            "record_id": self.experiment_id,
            "record_name": self.experiment_name,
            "experiment_group_name": self._base_experiment_name,
            "planId": self.config.experiment_plan_id,
            "planName": self.config.plan_name,
        }
        if experiment_metadata:
            self.experiment_metadata.update(experiment_metadata)
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

        from .._vendor.alibabacloud_agentloop20260520.client import Client
        from alibabacloud_tea_openapi import (
            utils_models as open_api_util_models,
        )

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
        from .._vendor.alibabacloud_agentloop20260520 import (
            models as agentloop_models,
        )

        from .._agentloop_config import _format_api_error

        client = self._get_agentloop_client()
        req = agentloop_models.GetAgentSpaceRequest()

        try:
            resp = client.get_agent_space(
                self.config.agent_space,
                req,
            )
        except Exception as e:
            raise ValueError(
                f"Failed to get agent space "
                f"'{self.config.agent_space}': "
                f"{_format_api_error(e)}",
            ) from e
        logger.debug(
            f"AgentLoop get_agent_space response: "
            f"{json.dumps(resp.to_map(), default=str, indent=2)}",
        )

        body = resp.body
        if not body or not body.sls_project:
            raise ValueError(
                f"Agent space '{self.config.agent_space}' has no SLS "
                f"project configured. Provide 'project' directly in "
                f"the config.",
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
            ("experiment_name", self._base_experiment_name),
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
        - data_config: dataset configuration
        - experiment_input: rendered input as a top-level string
        - experiment_output: model/agent returned content as a top-level
          string (or ``"ERROR: <type> - <message>"`` for failed tasks)
        - dataset.<col>: dataset item columns flattened as top-level fields

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
            # Cached task meta carries the dataset row under "input".
            task_meta = self._task_meta_cache.get(task_id, {})
            input_data = task_meta.get("input", {}) if isinstance(task_meta, dict) else {}

            # Add data_config field
            data_config = {
                "data_type": "dataset",
                "project": self.config.project,
                "dataset_id": self.config.dataset,
                "dataset_item_id": (
                    input_data.get("id", task_id)
                    if isinstance(input_data, dict)
                    else task_id
                ),
            }
            contents.append(
                (
                    "data_config",
                    json.dumps(data_config, ensure_ascii=False),
                ),
            )

            # experiment_input: if the solution provides an explicit value
            # via meta["experiment_input"] (e.g. the HTTP request body),
            # use that; otherwise fall back to the raw dataset row.
            output_meta = output.meta if isinstance(output.meta, dict) else {}
            raw_input = output_meta.get("experiment_input")
            if raw_input is None:
                raw_input = input_data

            if isinstance(raw_input, (dict, list)):
                experiment_input = json.dumps(
                    raw_input,
                    ensure_ascii=False,
                    default=str,
                )
            elif raw_input == "" or raw_input is None:
                experiment_input = ""
            else:
                experiment_input = str(raw_input)
            contents.append(("experiment_input", experiment_input))

            # experiment_output: top-level string with the returned content,
            # or "ERROR: <type> - <message>" for failed tasks.
            if output.success:
                output_value = output.output
                if isinstance(output_value, str):
                    experiment_output = output_value
                else:
                    experiment_output = json.dumps(
                        output_value,
                        ensure_ascii=False,
                        default=str,
                    )
            else:
                error_meta = output.meta
                error_type = (
                    error_meta.get("error_type") or "UnknownError"
                    if isinstance(error_meta, dict)
                    else "UnknownError"
                )
                error_message = (
                    error_meta.get("error_message")
                    if isinstance(error_meta, dict)
                    else None
                )
                if not error_message:
                    # Fall back to the cause / repr captured by the solution
                    # so we don't lose diagnostics when httpx exceptions
                    # carry an empty str().
                    error_message = (
                        error_meta.get("error_repr")
                        if isinstance(error_meta, dict)
                        else None
                    ) or error_type
                    logger.warning(
                        "Empty error_message for failed task "
                        f"(error_type={error_type}, "
                        f"record_id={self.experiment_id}). "
                        "Falling back to error_repr/type. meta=%s",
                        error_meta,
                    )
                experiment_output = f"ERROR: {error_type} - {error_message}"
            contents.append(("experiment_output", experiment_output))

            contents.append(
                ("status", "success" if output.success else "failed"),
            )

            # Add traceId from solution meta if available.
            trace_id = output_meta.get("traceId")
            if trace_id:
                contents.append(("traceId", str(trace_id)))

            # Add experiment_metrics with latency (ms).
            latency_ms = output_meta.get("latency_ms", 0)
            contents.append(
                (
                    "experiment_metrics",
                    json.dumps({"latency": latency_ms}),
                ),
            )

            # Flatten dataset columns to top-level dataset.<col> fields.
            # List / dict values are JSON-serialized; scalars are stringified.
            if isinstance(input_data, dict):
                for col, value in input_data.items():
                    field_name = f"dataset.{col}"
                    if isinstance(value, (list, dict)):
                        contents.append(
                            (
                                field_name,
                                json.dumps(
                                    value,
                                    ensure_ascii=False,
                                    default=str,
                                ),
                            ),
                        )
                    else:
                        contents.append((field_name, str(value)))

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

    def _merge_evaluators(self, agentloop_models: Any) -> list | None:
        """Merge plan evaluators with local evaluators.

        Plan evaluators take priority. When a local evaluator has the same
        ``evaluator_ref`` as a plan evaluator, the plan version is kept and
        a warning is logged. Local-only evaluators (not in the plan) are
        appended to the result.

        Returns:
            A list of ``agentloop_models.Evaluator`` or ``None`` if both
            sources are empty.
        """
        # Build a dict keyed by evaluator_ref from plan evaluators.
        plan_keys: set[str] = set()
        merged: dict[str, Any] = {}
        for ev in self.config.plan_evaluators:
            key = ev.evaluator_ref or ev.name or ""
            if key:
                merged[key] = ev
                plan_keys.add(key)

        # Local evaluators are added only if not already in the plan.
        if self.config.evaluators:
            for e in self.config.evaluators:
                key = e.evaluator_ref or e.name or ""
                if not key:
                    continue
                if key in plan_keys:
                    continue
                merged[key] = agentloop_models.Evaluator(
                    evaluator_ref=e.evaluator_ref or None,
                    name=e.name or None,
                    type=e.type or None,
                    result_name=e.result_name or None,
                    result_type=e.result_type or None,
                    filters=e.filters,
                    config=e.config,
                    variable_mapping=e.variable_mapping,
                )

        if not merged:
            return None
        return list(merged.values())

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
        from .._vendor.alibabacloud_agentloop20260520 import (
            models as agentloop_models,
        )

        # Delay before uploading to give SLS time to flush all task logs,
        # so the platform can aggregate them when the record is processed.
        time.sleep(10)

        client = self._get_agentloop_client()

        if self.config.query:
            data_source = agentloop_models.UploadExperimentRequestDataSource(
                type="DATASET_PARTIAL",
                dataset_id=self.config.dataset,
                query_sql=self.config.query,
            )
        else:
            data_source = agentloop_models.UploadExperimentRequestDataSource(
                type="DATASET_FULL",
                dataset_id=self.config.dataset,
            )

        evaluator_models = self._merge_evaluators(agentloop_models)

        req = agentloop_models.UploadExperimentRequest(
            record_id=self.experiment_id,
            record_name=self.experiment_name,
            total_tasks=self._total_tasks,
            completed_tasks=self._completed_tasks,
            failed_tasks=self._failed_tasks,
            executed_at=self.experiment_start_time,
            completed_at=int(time.time() * 1000),
            data_source=data_source,
            experiment_plan_id=self.config.experiment_plan_id,
            experiments=[
                agentloop_models.ExperimentConfig(
                    name=self._base_experiment_name,
                ),
            ],
            evaluators=evaluator_models,
        )

        try:
            resp = client.upload_experiment(
                self.config.agent_space,
                req,
            )
            logger.debug(
                f"Uploaded experiment record '{self.experiment_id}' to "
                f"AgentLoop. Response: "
                f"{json.dumps(resp.to_map(), default=str, indent=2)}",
            )
        except Exception as e:
            from .._agentloop_config import _format_api_error

            logger.warning(
                f"Failed to upload experiment record "
                f"'{self.experiment_id}': {_format_api_error(e)}",
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
