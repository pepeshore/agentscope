# -*- coding: utf-8 -*-
"""Configuration class for AgentLoop components."""
import os
from dataclasses import dataclass, field
from typing import Any


def _format_api_error(e: Exception) -> str:
    """Extract a concise error description from a Tea SDK exception."""
    code = getattr(e, "code", None)
    message = getattr(e, "message", None)
    if code and message:
        return f"[{code}] {message}"
    return str(e)


@dataclass
class EvaluatorConfig:
    """Configuration for a single evaluator.

    Maps to the AgentLoop SDK ``Evaluator`` model used in the
    ``upload_experiment`` API.

    Attributes:
        evaluator_ref (`str`):
            Reference to an existing evaluator definition on the platform
            (e.g. ``"Builtin.correctness"``). Mutually exclusive with
            ``name`` for inline evaluators.
        name (`str`):
            Evaluator name for inline (ondemand) evaluators.
        type (`str`):
            Evaluator type. Defaults to ``"LLM"``.
        result_name (`str`):
            Name of the evaluation metric / score.
        result_type (`str`):
            Result type: ``"score"``, ``"binary"``, or ``"text"``.
        filters (`dict | None`):
            Data filtering conditions.
        config (`dict | None`):
            Additional evaluator configuration.
        variable_mapping (`dict[str, str] | None`):
            Mapping from template variable names to data field paths.
            Must cover every variable declared in the evaluator's prompt
            template.
    """

    evaluator_ref: str = ""
    name: str = ""
    type: str = "LLM"
    result_name: str = ""
    result_type: str = ""
    filters: dict | None = None
    config: dict | None = None
    variable_mapping: dict[str, str] | None = None


@dataclass
class AgentLoopConfig:
    """Configuration for AgentLoop benchmark and evaluator storage.

    This class encapsulates all the configuration needed to connect to
    Alibaba Cloud AgentLoop and SLS (Simple Log Service)
    for the AgentLoop evaluation framework.

    Attributes:
        agent_space (`str`):
            The AgentLoop agent space name.
        dataset (`str`):
            The dataset name.
        region_id (`str`):
            The Alibaba Cloud region ID (e.g., "cn-hangzhou", "cn-shanghai").
            Used to construct endpoints.
        project (`str`):
            The SLS project name. If not provided, will be resolved from
            the agent space at runtime via ``get_agent_space``.
        query (`str`):
            Custom SQL query for loading data. When provided, the query is
            executed as-is in a single call. When empty (the default),
            automatic LIMIT/OFFSET pagination is used to load up to
            ``max_rows`` records.
        max_rows (`int`):
            Maximum number of records to load when using automatic pagination
            (i.e., when ``query`` is empty). Defaults to 1000. Ignored when
            a custom ``query`` is provided.
        evaluators (`list[EvaluatorConfig] | None`):
            A list of evaluator configurations. If provided, the evaluators
            will be validated against the AgentLoop platform (each evaluator
            is fetched via ``get_evaluator`` and its required variables are
            checked against ``variable_mapping``) and passed to the
            ``upload_experiment`` API to trigger automatic evaluation.
            Defaults to None (no evaluators).
        ground_truth_field (`str`):
            The field name in the dataset that contains the ground truth.
            If not provided, ground_truth will be empty string.
        custom_agentloop_endpoint (`str`):
            Custom AgentLoop API endpoint URL. When set, takes priority
            over the auto-generated endpoint from ``region_id``.
        custom_sls_endpoint (`str`):
            Custom SLS endpoint URL. When set, takes priority over the
            auto-generated endpoint from ``region_id``.
        experiment_name (`str`):
            Name for the experiment. Shared by the benchmark and storage,
            so they advertise the same identity on the platform and in
            local metadata. Defaults to ``"{dataset}_{timestamp}"`` if not
            provided.
        experiment_config (`dict`):
            User-defined experiment configuration metadata uploaded to the
            AgentLoop platform (e.g. ``{"agent_name": "..."}``).
            Defaults to an empty dict.
        access_key_id (`str`):
            The Alibaba Cloud AccessKey ID. If not provided, will try to
            get from environment variables `AGENTLOOP_AK` or
            `ALIBABA_CLOUD_ACCESS_KEY_ID` (in that order).
        access_key_secret (`str`):
            The Alibaba Cloud AccessKey Secret. If not provided, will try
            to get from environment variables `AGENTLOOP_SK` or
            `ALIBABA_CLOUD_ACCESS_KEY_SECRET` (in that order).
    """

    agent_space: str
    dataset: str
    region_id: str
    project: str = ""
    query: str = ""
    max_rows: int = 1000
    evaluators: list[EvaluatorConfig] | None = None
    ground_truth_field: str = ""
    custom_agentloop_endpoint: str = ""
    custom_sls_endpoint: str = ""
    experiment_name: str = ""
    experiment_config: dict = field(default_factory=dict)
    access_key_id: str = field(default="", repr=False)
    access_key_secret: str = field(default="", repr=False)

    def __post_init__(self) -> None:
        """Post-initialization to load credentials and set defaults."""
        missing = [
            name
            for name in ("agent_space", "dataset", "region_id")
            if not getattr(self, name)
        ]
        if missing:
            raise ValueError(
                f"{', '.join(missing)} must not be empty.",
            )
        if not self.access_key_id:
            self.access_key_id = (
                os.environ.get("AGENTLOOP_AK")
                or os.environ.get("ALIBABA_CLOUD_ACCESS_KEY_ID")
                or ""
            )
        if not self.access_key_secret:
            self.access_key_secret = (
                os.environ.get("AGENTLOOP_SK")
                or os.environ.get("ALIBABA_CLOUD_ACCESS_KEY_SECRET")
                or ""
            )
        if self.max_rows <= 0:
            raise ValueError(
                f"`max_rows` must be a positive integer, got {self.max_rows}.",
            )

    @property
    def effective_experiment_name(self) -> str:
        """Return the experiment name, generating a default if unset."""
        if self.experiment_name:
            return self.experiment_name
        import time
        return f"{self.dataset}_{time.strftime('%Y%m%d_%H%M%S')}"

    def validate_credentials(self) -> None:
        """Validate that required credentials are present.

        Raises:
            ValueError: If AccessKey credentials are missing.
        """
        if not self.access_key_id or not self.access_key_secret:
            raise ValueError(
                "AccessKey credentials are required. Provide them via "
                "`access_key_id` and `access_key_secret` parameters, or set "
                "environment variables: AGENTLOOP_AK / AGENTLOOP_SK "
                "(or ALIBABA_CLOUD_ACCESS_KEY_ID / "
                "ALIBABA_CLOUD_ACCESS_KEY_SECRET).",
            )

    def _create_agentloop_client(self) -> "Any":
        """Create an AgentLoop API client from this config's credentials."""
        from ._vendor.alibabacloud_agentloop20260520.client import Client
        from alibabacloud_tea_openapi import (
            utils_models as open_api_util_models,
        )

        client_config = open_api_util_models.Config(
            access_key_id=self.access_key_id,
            access_key_secret=self.access_key_secret,
        )
        client_config.endpoint = self.agentloop_endpoint
        return Client(client_config)

    @staticmethod
    def _validate_mapping_value(
        value: str,
        dataset_columns: set[str],
    ) -> str | None:
        """Check whether a single variable_mapping value is valid.

        Returns ``None`` if valid, or an error description string.
        """
        if value == "experiment_output":
            return None
        if value == "experiment_input":
            return None
        if value.startswith("dataset."):
            col = value[len("dataset."):]
            if not col:
                return (
                    f"'{value}' is missing a column name after 'dataset.'"
                )
            if col not in dataset_columns:
                return (
                    f"column '{col}' does not exist in dataset "
                    f"'{sorted(dataset_columns)}'"
                )
            return None
        return (
            f"'{value}' is invalid. Must be 'experiment_output', "
            f"'experiment_input', or 'dataset.<column>'"
        )

    def validate_evaluators(self) -> None:
        """Validate evaluators against the AgentLoop platform.

        Call this before creating benchmark or storage for early failure.
        Validates that each evaluator exists, that ``variable_mapping``
        covers all required variables, and that mapping values reference
        valid data paths.

        Raises:
            `ValueError`: If validation fails.
            `ImportError`: If the AgentLoop SDK is not installed.
        """
        if not self.evaluators:
            return
        if getattr(self, "_evaluators_validated", False):
            return

        from ._vendor.alibabacloud_agentloop20260520 import (
            models as agentloop_models,
        )

        for ev_cfg in self.evaluators:
            if not ev_cfg.evaluator_ref and not ev_cfg.name:
                raise ValueError(
                    "Each evaluator must have 'evaluator_ref' or "
                    "'name' set.",
                )

        self.validate_credentials()
        client = self._create_agentloop_client()
        dataset_columns: set[str] | None = None

        for ev_cfg in self.evaluators:
            ev_name = ev_cfg.evaluator_ref or ev_cfg.name

            req = agentloop_models.GetEvaluatorRequest()
            try:
                resp = client.get_evaluator(
                    self.agent_space, ev_name, req,
                )
            except Exception as e:
                raise ValueError(
                    f"Failed to fetch evaluator '{ev_name}' from "
                    f"agent space '{self.agent_space}': "
                    f"{_format_api_error(e)}",
                ) from e

            evaluator = resp.body.evaluator if resp.body else None
            if not evaluator or not evaluator.config:
                continue

            variables = evaluator.config.get("variables", [])
            if not variables:
                continue

            required_vars = {
                v["name"]
                for v in variables
                if isinstance(v, dict) and "name" in v
            }
            if not required_vars:
                continue

            user_mapping = ev_cfg.variable_mapping or {}

            missing = required_vars - set(user_mapping.keys())
            if missing:
                raise ValueError(
                    f"Evaluator '{ev_name}': variable_mapping is missing "
                    f"keys {sorted(missing)}. The evaluator requires: "
                    f"{sorted(required_vars)}. Provided: "
                    f"{sorted(user_mapping.keys())}.",
                )

            if dataset_columns is None:
                try:
                    req = agentloop_models.GetDatasetRequest()
                    resp = client.get_dataset(
                        self.agent_space, self.dataset, req,
                    )
                    dataset_columns = set()
                    if resp.body and resp.body.schema:
                        dataset_columns = set(resp.body.schema.keys())
                except Exception as e:
                    raise ValueError(
                        f"Failed to fetch dataset '{self.dataset}' "
                        f"from agent space '{self.agent_space}': "
                        f"{_format_api_error(e)}",
                    ) from e

            for var_name, var_value in user_mapping.items():
                error = self._validate_mapping_value(
                    var_value, dataset_columns,
                )
                if error:
                    raise ValueError(
                        f"Evaluator '{ev_name}', variable_mapping "
                        f"'{var_name}' -> '{var_value}': {error}.",
                    )

        self._evaluators_validated = True

    @property
    def agentloop_endpoint(self) -> str:
        """Get the AgentLoop API endpoint URL.

        Returns:
            `str`: The AgentLoop endpoint URL.
        """
        if self.custom_agentloop_endpoint:
            return self.custom_agentloop_endpoint
        return f"agentloop.{self.region_id}.aliyuncs.com"

    @property
    def sls_endpoint(self) -> str:
        """Get the SLS endpoint URL.

        Returns:
            `str`: The SLS endpoint URL.
        """
        if self.custom_sls_endpoint:
            return self.custom_sls_endpoint
        return f"{self.region_id}.log.aliyuncs.com"