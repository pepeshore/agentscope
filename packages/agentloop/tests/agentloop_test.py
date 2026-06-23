# -*- coding: utf-8 -*-
"""Unit tests for AgentLoop benchmark and evaluator storage."""
import json
import os
import sys
import shutil
import tempfile
import unittest
from unittest.mock import MagicMock, patch, call

# Ensure local source is preferred over any installed version so that
# newly added modules (not yet published) are importable.
_SDK_SRC_DIR = os.path.join(os.path.dirname(__file__), "..", "src")
if _SDK_SRC_DIR not in sys.path:
    sys.path.insert(0, os.path.abspath(_SDK_SRC_DIR))
_AGENTSCOPE_SRC_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "..", "src")
if _AGENTSCOPE_SRC_DIR not in sys.path:
    sys.path.insert(0, os.path.abspath(_AGENTSCOPE_SRC_DIR))

from agentloop_sdk._agentloop_config import AgentLoopConfig, EvaluatorConfig
from agentloop_sdk._agentloop_benchmark._agentloop_benchmark import (
    AgentLoopBenchmark,
)
from agentloop_sdk._evaluator_storage._agentloop_evaluator_storage import (
    AgentLoopEvaluatorStorage,
    EXPERIMENT_LOGSTORE,
)
from agentscope.evaluate._task import Task
from agentscope.evaluate._solution import SolutionOutput
from agentloop_sdk._vendor.alibabacloud_agentloop20260520 import (
    models as _vendor_models,
)


# ============================================================
# Helper factories
# ============================================================

def _make_config(
    region_id: str = "cn-hangzhou",
    project: str = "test_project",
    agent_space: str = "test_agent_space",
    ground_truth_field: str = "",
    query: str = "",
) -> AgentLoopConfig:
    return AgentLoopConfig(
        agent_space=agent_space,
        dataset="test_dataset",
        region_id=region_id,
        project=project,
        query=query,
        ground_truth_field=ground_truth_field,
        access_key_id="test_key_id",
        access_key_secret="test_key_secret",
    )


# ============================================================
# AgentLoopConfig tests
# ============================================================

class TestAgentLoopConfig(unittest.TestCase):
    """Tests for AgentLoopConfig dataclass."""

    def test_basic_initialization(self) -> None:
        config = _make_config()
        self.assertEqual(config.agent_space, "test_agent_space")
        self.assertEqual(config.dataset, "test_dataset")
        self.assertEqual(config.region_id, "cn-hangzhou")
        self.assertEqual(config.project, "test_project")
        self.assertEqual(config.access_key_id, "test_key_id")
        self.assertEqual(config.access_key_secret, "test_key_secret")

    def test_default_query_is_empty(self) -> None:
        config = _make_config(query="")
        self.assertEqual(config.query, "")

    def test_default_max_rows(self) -> None:
        config = _make_config()
        self.assertEqual(config.max_rows, 1000)

    def test_custom_max_rows(self) -> None:
        config = AgentLoopConfig(
            agent_space="as",
            dataset="ds",
            region_id="cn-hangzhou",
            max_rows=500,
            access_key_id="k",
            access_key_secret="s",
        )
        self.assertEqual(config.max_rows, 500)

    def test_invalid_max_rows_raises(self) -> None:
        with self.assertRaises(ValueError):
            AgentLoopConfig(
                agent_space="as",
                dataset="ds",
                region_id="cn-hangzhou",
                max_rows=0,
                access_key_id="k",
                access_key_secret="s",
            )

    def test_negative_max_rows_raises(self) -> None:
        with self.assertRaises(ValueError):
            AgentLoopConfig(
                agent_space="as",
                dataset="ds",
                region_id="cn-hangzhou",
                max_rows=-1,
                access_key_id="k",
                access_key_secret="s",
            )

    def test_custom_query_preserved(self) -> None:
        custom_query = "* | select col1 from test_dataset limit 10"
        config = _make_config(query=custom_query)
        self.assertEqual(config.query, custom_query)

    def test_credentials_loaded_from_env(self) -> None:
        with patch.dict(
            os.environ,
            {
                "ALIBABA_CLOUD_ACCESS_KEY_ID": "env_key",
                "ALIBABA_CLOUD_ACCESS_KEY_SECRET": "env_secret",
            },
        ):
            config = AgentLoopConfig(
                agent_space="as",
                dataset="ds",
                region_id="cn-hangzhou",
            )
        self.assertEqual(config.access_key_id, "env_key")
        self.assertEqual(config.access_key_secret, "env_secret")

    def test_credentials_loaded_from_agentloop_env(self) -> None:
        with patch.dict(
            os.environ,
            {
                "AGENTLOOP_AK": "al_key",
                "AGENTLOOP_SK": "al_secret",
            },
        ):
            config = AgentLoopConfig(
                agent_space="as",
                dataset="ds",
                region_id="cn-hangzhou",
            )
        self.assertEqual(config.access_key_id, "al_key")
        self.assertEqual(config.access_key_secret, "al_secret")

    def test_agentloop_env_takes_priority_over_alibaba_env(self) -> None:
        with patch.dict(
            os.environ,
            {
                "AGENTLOOP_AK": "al_key",
                "AGENTLOOP_SK": "al_secret",
                "ALIBABA_CLOUD_ACCESS_KEY_ID": "env_key",
                "ALIBABA_CLOUD_ACCESS_KEY_SECRET": "env_secret",
            },
        ):
            config = AgentLoopConfig(
                agent_space="as",
                dataset="ds",
                region_id="cn-hangzhou",
            )
        self.assertEqual(config.access_key_id, "al_key")
        self.assertEqual(config.access_key_secret, "al_secret")

    def test_explicit_credentials_override_env(self) -> None:
        with patch.dict(
            os.environ,
            {
                "AGENTLOOP_AK": "al_key",
                "AGENTLOOP_SK": "al_secret",
                "ALIBABA_CLOUD_ACCESS_KEY_ID": "env_key",
                "ALIBABA_CLOUD_ACCESS_KEY_SECRET": "env_secret",
            },
        ):
            config = AgentLoopConfig(
                agent_space="as",
                dataset="ds",
                region_id="cn-hangzhou",
                access_key_id="explicit_key",
                access_key_secret="explicit_secret",
            )
        self.assertEqual(config.access_key_id, "explicit_key")
        self.assertEqual(config.access_key_secret, "explicit_secret")

    def test_validate_credentials_success(self) -> None:
        config = _make_config()
        config.validate_credentials()  # should not raise

    def test_validate_credentials_missing_key_id(self) -> None:
        config = _make_config()
        config.access_key_id = ""
        with self.assertRaises(ValueError) as ctx:
            config.validate_credentials()
        self.assertIn("AccessKey", str(ctx.exception))

    def test_validate_credentials_missing_key_secret(self) -> None:
        config = _make_config()
        config.access_key_secret = ""
        with self.assertRaises(ValueError):
            config.validate_credentials()

    def test_validate_credentials_both_missing(self) -> None:
        config = AgentLoopConfig(
            agent_space="as",
            dataset="ds",
            region_id="cn-hangzhou",
        )
        # Ensure env vars are absent
        with patch.dict(os.environ, {}, clear=True):
            config.access_key_id = ""
            config.access_key_secret = ""
            with self.assertRaises(ValueError):
                config.validate_credentials()

    def test_agentloop_endpoint(self) -> None:
        config = _make_config(region_id="cn-hangzhou")
        self.assertEqual(
            config.agentloop_endpoint,
            "agentloop.cn-hangzhou.aliyuncs.com",
        )

    def test_sls_endpoint(self) -> None:
        config = _make_config(region_id="cn-hangzhou")
        self.assertEqual(config.sls_endpoint, "cn-hangzhou.log.aliyuncs.com")

    def test_endpoints_with_different_region(self) -> None:
        config = _make_config(region_id="cn-shanghai")
        self.assertEqual(
            config.agentloop_endpoint,
            "agentloop.cn-shanghai.aliyuncs.com",
        )
        self.assertEqual(config.sls_endpoint, "cn-shanghai.log.aliyuncs.com")

    def test_default_project_is_empty_string(self) -> None:
        config = AgentLoopConfig(
            agent_space="as",
            dataset="ds",
            region_id="cn-hangzhou",
            access_key_id="k",
            access_key_secret="s",
        )
        self.assertEqual(config.project, "")

    def test_default_ground_truth_field_is_empty(self) -> None:
        config = _make_config()
        self.assertEqual(config.ground_truth_field, "")


# ============================================================
# AgentLoopBenchmark tests
# ============================================================

class TestAgentLoopBenchmark(unittest.TestCase):
    """Tests for AgentLoopBenchmark class."""

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    def _make_benchmark(
        self,
        raw_data: list[dict],
        ground_truth_field: str = "",
        name: str = "",
        description: str = "Benchmark loaded from AgentLoop.",
    ) -> AgentLoopBenchmark:
        """Create a benchmark with _load_data patched."""
        with patch.object(
            AgentLoopBenchmark,
            "_load_data",
            return_value=raw_data,
        ):
            return AgentLoopBenchmark(
                config=_make_config(ground_truth_field=ground_truth_field),
                name=name,
                description=description,
            )

    # ------------------------------------------------------------------
    # Initialization
    # ------------------------------------------------------------------

    def test_default_name_and_description(self) -> None:
        benchmark = self._make_benchmark([])
        # Default name falls back to config.effective_experiment_name
        self.assertEqual(
            benchmark.name,
            benchmark.config.effective_experiment_name,
        )
        self.assertEqual(benchmark.description, "Benchmark loaded from AgentLoop.")

    def test_custom_name_and_description(self) -> None:
        benchmark = self._make_benchmark(
            [],
            name="MyBench",
            description="Custom desc",
        )
        self.assertEqual(benchmark.name, "MyBench")
        self.assertEqual(benchmark.description, "Custom desc")

    def test_config_stored(self) -> None:
        config = _make_config()
        with patch.object(AgentLoopBenchmark, "_load_data", return_value=[]):
            benchmark = AgentLoopBenchmark(config=config)
        self.assertIs(benchmark.config, config)

    # ------------------------------------------------------------------
    # Task conversion
    # ------------------------------------------------------------------

    def test_task_input_equals_log_record(self) -> None:
        record = {"question": "What is 1+1?", "category": "math"}
        benchmark = self._make_benchmark([record])
        self.assertEqual(benchmark[0].input, record)

    def test_task_ground_truth_empty_when_no_field_configured(self) -> None:
        record = {"question": "Q", "answer": "A"}
        benchmark = self._make_benchmark([record], ground_truth_field="")
        self.assertEqual(benchmark[0].ground_truth, "")

    def test_task_ground_truth_from_configured_field(self) -> None:
        record = {"question": "Q", "answer": "42"}
        benchmark = self._make_benchmark([record], ground_truth_field="answer")
        self.assertEqual(benchmark[0].ground_truth, "42")

    def test_task_ground_truth_missing_field_falls_back_to_empty(self) -> None:
        record = {"question": "Q"}
        benchmark = self._make_benchmark([record], ground_truth_field="answer")
        self.assertEqual(benchmark[0].ground_truth, "")

    def test_task_ids_are_unique(self) -> None:
        records = [{"q": str(i)} for i in range(10)]
        benchmark = self._make_benchmark(records)
        ids = [task.id for task in benchmark]
        self.assertEqual(len(ids), len(set(ids)), "Task IDs are not unique")

    def test_task_ids_are_stable_across_iterations(self) -> None:
        records = [{"q": "1"}, {"q": "2"}]
        benchmark = self._make_benchmark(records)
        first_pass = [task.id for task in benchmark]
        second_pass = [task.id for task in benchmark]
        self.assertEqual(first_pass, second_pass)

    def test_task_has_empty_metrics(self) -> None:
        benchmark = self._make_benchmark([{"q": "Q"}])
        self.assertEqual(benchmark[0].metrics, [])

    def test_task_has_empty_metadata(self) -> None:
        benchmark = self._make_benchmark([{"q": "Q"}])
        self.assertEqual(benchmark[0].metadata, {})

    # ------------------------------------------------------------------
    # __len__ / __iter__ / __getitem__
    # ------------------------------------------------------------------

    def test_len_empty(self) -> None:
        benchmark = self._make_benchmark([])
        self.assertEqual(len(benchmark), 0)

    def test_len_non_empty(self) -> None:
        benchmark = self._make_benchmark([{"q": str(i)} for i in range(5)])
        self.assertEqual(len(benchmark), 5)

    def test_iter_yields_task_objects(self) -> None:
        benchmark = self._make_benchmark([{"q": "1"}, {"q": "2"}])
        for task in benchmark:
            self.assertIsInstance(task, Task)

    def test_iter_yields_all_tasks(self) -> None:
        records = [{"q": str(i)} for i in range(3)]
        benchmark = self._make_benchmark(records)
        tasks = list(benchmark)
        self.assertEqual(len(tasks), 3)
        for task, record in zip(tasks, records):
            self.assertEqual(task.input, record)

    def test_getitem_first(self) -> None:
        records = [{"q": "first"}, {"q": "second"}]
        benchmark = self._make_benchmark(records)
        self.assertEqual(benchmark[0].input, {"q": "first"})

    def test_getitem_last(self) -> None:
        records = [{"q": "a"}, {"q": "b"}, {"q": "c"}]
        benchmark = self._make_benchmark(records)
        self.assertEqual(benchmark[2].input, {"q": "c"})

    def test_getitem_out_of_range(self) -> None:
        benchmark = self._make_benchmark([{"q": "only"}])
        with self.assertRaises(IndexError):
            _ = benchmark[5]

    # ------------------------------------------------------------------
    # _parse_response_data (columns + rows format)
    # ------------------------------------------------------------------

    def test_parse_response_data_basic(self) -> None:
        benchmark = self._make_benchmark([])
        columns = ["col1", "col2"]
        rows = [["a", 1], ["b", 2]]
        result = benchmark._parse_response_data(columns, rows)
        self.assertEqual(result, [{"col1": "a", "col2": 1}, {"col1": "b", "col2": 2}])

    def test_parse_response_data_empty_rows(self) -> None:
        benchmark = self._make_benchmark([])
        result = benchmark._parse_response_data(["col1"], [])
        self.assertEqual(result, [])

    def test_parse_response_data_none_columns(self) -> None:
        benchmark = self._make_benchmark([])
        result = benchmark._parse_response_data(None, [["a"]])
        self.assertEqual(result, [])

    def test_parse_response_data_none_rows(self) -> None:
        benchmark = self._make_benchmark([])
        result = benchmark._parse_response_data(["col1"], None)
        self.assertEqual(result, [])

    def test_parse_response_data_both_none(self) -> None:
        benchmark = self._make_benchmark([])
        result = benchmark._parse_response_data(None, None)
        self.assertEqual(result, [])

    # ------------------------------------------------------------------
    # _load_data with mocked SDK
    # ------------------------------------------------------------------

    def _make_mock_execute_query(
        self,
        columns: list[str] | None,
        rows: list[list] | None,
    ) -> MagicMock:
        """Build a fake execute_query callable returning columns + rows."""
        mock_resp = MagicMock()
        mock_resp.body.columns = columns
        mock_resp.body.rows = rows
        mock_client = MagicMock()
        mock_client.execute_query.return_value = mock_resp
        return mock_client

    def _make_paginated_benchmark(self) -> AgentLoopBenchmark:
        """Create a benchmark with no custom query (paginated mode)."""
        with patch.object(AgentLoopBenchmark, "_load_data", return_value=[]):
            return AgentLoopBenchmark(config=_make_config())

    def test_load_data_columns_rows_response(self) -> None:
        """New format: columns + rows are combined into list of dicts."""
        benchmark = self._make_paginated_benchmark()
        benchmark.config.query = "* | select * from test_dataset"

        mock_client = self._make_mock_execute_query(
            columns=["a", "b"],
            rows=[[1, 2], [3, 4]],
        )

        mock_agentloop_pkg = MagicMock()
        with patch.dict("sys.modules", {"alibabacloud_agentloop20260520": mock_agentloop_pkg}):
            with patch.object(benchmark, "_get_client", return_value=mock_client):
                result = AgentLoopBenchmark._load_data(benchmark)

        self.assertEqual(result, [{"a": 1, "b": 2}, {"a": 3, "b": 4}])

    def test_load_data_none_body(self) -> None:
        mock_resp = MagicMock()
        mock_resp.body = None
        mock_client = MagicMock()
        mock_client.execute_query.return_value = mock_resp

        mock_agentloop_pkg = MagicMock()
        with patch.dict("sys.modules", {"alibabacloud_agentloop20260520": mock_agentloop_pkg}):
            with patch.object(AgentLoopBenchmark, "_load_data", return_value=[]):
                benchmark = AgentLoopBenchmark(config=_make_config())
            benchmark.config.query = "* | select * from test_dataset"
            with patch.object(benchmark, "_get_client", return_value=mock_client):
                result = AgentLoopBenchmark._load_data(benchmark)
        self.assertEqual(result, [])

    # ------------------------------------------------------------------
    # Paginated loading (_load_data with no custom query)
    # ------------------------------------------------------------------

    def test_paginated_stops_on_empty_response(self) -> None:
        benchmark = self._make_paginated_benchmark()
        mock_agentloop_pkg = MagicMock()
        with patch.dict("sys.modules", {"alibabacloud_agentloop20260520": mock_agentloop_pkg}):
            with patch.object(benchmark, "_get_client", return_value=MagicMock()):
                with patch.object(benchmark, "_execute_query_request", return_value=[]):
                    result = AgentLoopBenchmark._load_data(benchmark)
        self.assertEqual(result, [])

    def test_paginated_stops_on_error(self) -> None:
        benchmark = self._make_paginated_benchmark()
        first_page = [{"q": "1"}, {"q": "2"}]
        call_count = 0

        def side_effect(*_args: object, **_kwargs: object) -> list[dict]:
            nonlocal call_count
            call_count += 1
            if call_count == 1:
                return first_page
            raise RuntimeError("simulated API error")

        mock_agentloop_pkg = MagicMock()
        with patch.dict("sys.modules", {"alibabacloud_agentloop20260520": mock_agentloop_pkg}):
            with patch.object(benchmark, "_get_client", return_value=MagicMock()):
                with patch.object(
                    benchmark,
                    "_execute_query_request",
                    side_effect=side_effect,
                ):
                    result = AgentLoopBenchmark._load_data(benchmark)

        self.assertEqual(result, first_page)
        self.assertEqual(call_count, 2)

    def test_paginated_respects_max_rows(self) -> None:
        benchmark = self._make_paginated_benchmark()
        benchmark.config.max_rows = 5
        page = [{"i": i} for i in range(3)]

        call_count = 0

        def side_effect(*_args: object, **_kwargs: object) -> list[dict]:
            nonlocal call_count
            call_count += 1
            return page

        mock_agentloop_pkg = MagicMock()
        with patch.dict("sys.modules", {"alibabacloud_agentloop20260520": mock_agentloop_pkg}):
            with patch.object(benchmark, "_get_client", return_value=MagicMock()):
                with patch.object(
                    benchmark,
                    "_execute_query_request",
                    side_effect=side_effect,
                ):
                    result = AgentLoopBenchmark._load_data(benchmark)

        self.assertEqual(len(result), 5)
        self.assertEqual(call_count, 2)

    def test_paginated_multiple_pages_collected(self) -> None:
        benchmark = self._make_paginated_benchmark()
        benchmark.config.max_rows = 10
        pages = [
            [{"n": 0}, {"n": 1}, {"n": 2}],
            [{"n": 3}, {"n": 4}, {"n": 5}],
            [],
        ]
        call_count = 0

        def side_effect(*_args: object, **_kwargs: object) -> list[dict]:
            nonlocal call_count
            result_page = pages[call_count]
            call_count += 1
            return result_page

        mock_agentloop_pkg = MagicMock()
        with patch.dict("sys.modules", {"alibabacloud_agentloop20260520": mock_agentloop_pkg}):
            with patch.object(benchmark, "_get_client", return_value=MagicMock()):
                with patch.object(
                    benchmark,
                    "_execute_query_request",
                    side_effect=side_effect,
                ):
                    result = AgentLoopBenchmark._load_data(benchmark)

        self.assertEqual(len(result), 6)
        self.assertEqual(result, pages[0] + pages[1])
        self.assertEqual(call_count, 3)

    def test_custom_query_uses_single_call(self) -> None:
        benchmark = self._make_paginated_benchmark()
        benchmark.config.query = "* | select * from test_dataset"
        records = [{"a": 1}]

        mock_agentloop_pkg = MagicMock()
        with patch.dict("sys.modules", {"alibabacloud_agentloop20260520": mock_agentloop_pkg}):
            with patch.object(benchmark, "_get_client", return_value=MagicMock()):
                with patch.object(
                    benchmark,
                    "_execute_query_request",
                    return_value=records,
                ) as mock_exec:
                    result = AgentLoopBenchmark._load_data(benchmark)

        mock_exec.assert_called_once()
        self.assertEqual(result, records)

    # ------------------------------------------------------------------
    # ImportError handling
    # ------------------------------------------------------------------

    def test_get_client_import_error(self) -> None:
        with patch.object(AgentLoopBenchmark, "_load_data", return_value=[]):
            benchmark = AgentLoopBenchmark(config=_make_config())

        with patch.dict(
            "sys.modules",
            {
                "alibabacloud_agentloop20260520": None,
                "alibabacloud_agentloop20260520.client": None,
                "alibabacloud_tea_openapi": None,
                "alibabacloud_tea_openapi.utils_models": None,
            },
        ):
            with self.assertRaises((ImportError, AttributeError)):
                benchmark._get_client()

    # ------------------------------------------------------------------
    # validate_credentials propagation
    # ------------------------------------------------------------------

    def test_invalid_credentials_raise_on_init(self) -> None:
        bad_config = AgentLoopConfig(
            agent_space="as",
            dataset="ds",
            region_id="cn-hangzhou",
        )
        bad_config.access_key_id = ""
        bad_config.access_key_secret = ""

        with patch.object(AgentLoopBenchmark, "_load_data", return_value=[]):
            with self.assertRaises(ValueError):
                AgentLoopBenchmark(config=bad_config)


# ============================================================
# AgentLoopEvaluatorStorage tests
# ============================================================

class TestAgentLoopEvaluatorStorage(unittest.TestCase):
    """Tests for AgentLoopEvaluatorStorage class."""

    def setUp(self) -> None:
        self.save_dir = tempfile.mkdtemp()
        self.config = _make_config(project="my_sls_project")

    def tearDown(self) -> None:
        shutil.rmtree(self.save_dir, ignore_errors=True)

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    def _make_storage(
        self,
        experiment_id: str = "exp-001",
        experiment_name: str = "test_exp",
        experiment_type: str = "agent",
        experiment_metadata: dict | None = None,
        experiment_config: dict | None = None,
    ) -> AgentLoopEvaluatorStorage:
        return AgentLoopEvaluatorStorage(
            save_dir=self.save_dir,
            config=self.config,
            experiment_id=experiment_id,
            experiment_name=experiment_name,
            experiment_type=experiment_type,
            experiment_metadata=experiment_metadata,
            experiment_config=experiment_config,
        )

    def _make_solution_output(
        self,
        success: bool = True,
        output: object = "42",
    ) -> SolutionOutput:
        return SolutionOutput(
            success=success,
            output=output,
            trajectory=[],
            meta={"note": "test"},
        )

    # ------------------------------------------------------------------
    # Initialization
    # ------------------------------------------------------------------

    def test_experiment_id_stored(self) -> None:
        storage = self._make_storage(experiment_id="my-exp-id")
        self.assertEqual(storage.experiment_id, "my-exp-id")

    def test_experiment_name_stored(self) -> None:
        storage = self._make_storage(experiment_name="MyExperiment")
        self.assertEqual(storage.experiment_name, "MyExperiment")

    def test_experiment_type_stored(self) -> None:
        storage = self._make_storage(experiment_type="model")
        self.assertEqual(storage.experiment_type, "model")

    def test_logstore_is_experiment_detail(self) -> None:
        storage = self._make_storage()
        self.assertEqual(storage.logstore, EXPERIMENT_LOGSTORE)

    def test_default_experiment_id_generated_when_none(self) -> None:
        storage = AgentLoopEvaluatorStorage(
            save_dir=self.save_dir,
            config=self.config,
        )
        self.assertIsNotNone(storage.experiment_id)
        self.assertGreater(len(storage.experiment_id), 0)

    def test_default_experiment_name_generated_when_none(self) -> None:
        storage = AgentLoopEvaluatorStorage(
            save_dir=self.save_dir,
            config=self.config,
        )
        # Default name falls back to config.effective_experiment_name
        self.assertEqual(
            storage.experiment_name,
            self.config.effective_experiment_name,
        )

    def test_default_metadata_is_local_run(self) -> None:
        storage = AgentLoopEvaluatorStorage(
            save_dir=self.save_dir,
            config=self.config,
        )
        self.assertEqual(storage.experiment_metadata, {"run_env": "local_run"})

    def test_custom_metadata_stored(self) -> None:
        storage = self._make_storage(experiment_metadata={"run_env": "ci"})
        self.assertEqual(storage.experiment_metadata, {"run_env": "ci"})

    def test_default_experiment_config_is_empty_dict(self) -> None:
        storage = AgentLoopEvaluatorStorage(
            save_dir=self.save_dir,
            config=self.config,
        )
        self.assertEqual(storage.experiment_config, {})

    def test_custom_experiment_config_stored(self) -> None:
        cfg = {"model": "gpt-4", "temperature": 0.7}
        storage = self._make_storage(experiment_config=cfg)
        self.assertEqual(storage.experiment_config, cfg)

    def test_task_meta_cache_initialized_empty(self) -> None:
        storage = self._make_storage()
        self.assertEqual(storage._task_meta_cache, {})

    def test_project_from_config(self) -> None:
        storage = self._make_storage()
        self.assertEqual(storage.config.project, "my_sls_project")

    def test_project_resolved_when_not_provided(self) -> None:
        config = AgentLoopConfig(
            agent_space="as",
            dataset="ds",
            region_id="cn-hangzhou",
            project="",
            access_key_id="k",
            access_key_secret="s",
        )
        with patch.object(
            AgentLoopEvaluatorStorage,
            "_resolve_project",
        ) as mock_resolve:
            def set_project() -> None:
                config.project = "queried_project"
            mock_resolve.side_effect = lambda: set_project()
            storage = AgentLoopEvaluatorStorage(
                save_dir=self.save_dir,
                config=config,
            )
            mock_resolve.assert_called_once()
        self.assertEqual(storage.config.project, "queried_project")

    def test_invalid_credentials_raise_on_init(self) -> None:
        bad_config = AgentLoopConfig(
            agent_space="as",
            dataset="ds",
            region_id="cn-hangzhou",
        )
        bad_config.access_key_id = ""
        bad_config.access_key_secret = ""
        with self.assertRaises(ValueError):
            AgentLoopEvaluatorStorage(save_dir=self.save_dir, config=bad_config)

    def test_tracking_counters_initialized(self) -> None:
        storage = self._make_storage()
        self.assertEqual(storage._completed_tasks, 0)
        self.assertEqual(storage._failed_tasks, 0)
        self.assertEqual(storage._total_tasks, 0)

    # ------------------------------------------------------------------
    # _build_base_log_contents
    # ------------------------------------------------------------------

    def test_build_base_log_contents_core_fields(self) -> None:
        storage = self._make_storage(
            experiment_id="eid",
            experiment_name="ename",
            experiment_type="agent",
        )
        contents = storage._build_base_log_contents()
        content_dict = dict(contents)

        self.assertEqual(content_dict["experiment_id"], "eid")
        self.assertEqual(content_dict["experiment_name"], "ename")
        self.assertEqual(content_dict["experiment_type"], "agent")
        self.assertIn("experiment_start_time", content_dict)
        self.assertIn("experiment_metadata", content_dict)
        self.assertIn("experiment_config", content_dict)

    def test_build_base_log_contents_without_task_and_repeat(self) -> None:
        storage = self._make_storage()
        contents = storage._build_base_log_contents()
        keys = [k for k, _ in contents]
        self.assertNotIn("task_id", keys)
        self.assertNotIn("repeat_id", keys)

    def test_build_base_log_contents_with_task_id(self) -> None:
        storage = self._make_storage()
        contents = storage._build_base_log_contents(task_id="task-123")
        content_dict = dict(contents)
        self.assertEqual(content_dict["task_id"], "task-123")
        self.assertNotIn("repeat_id", content_dict)

    def test_build_base_log_contents_with_both_ids(self) -> None:
        storage = self._make_storage()
        contents = storage._build_base_log_contents(
            task_id="task-123",
            repeat_id="repeat-0",
        )
        content_dict = dict(contents)
        self.assertEqual(content_dict["task_id"], "task-123")
        self.assertEqual(content_dict["repeat_id"], "repeat-0")

    def test_build_base_log_contents_metadata_is_json_string(self) -> None:
        metadata = {"run_env": "test", "version": "1.0"}
        storage = self._make_storage(experiment_metadata=metadata)
        contents = storage._build_base_log_contents()
        content_dict = dict(contents)
        self.assertEqual(
            json.loads(content_dict["experiment_metadata"]),
            metadata,
        )

    def test_build_base_log_contents_config_is_json_string(self) -> None:
        exp_config = {"model": "claude", "temp": 0.5}
        storage = self._make_storage(experiment_config=exp_config)
        contents = storage._build_base_log_contents()
        content_dict = dict(contents)
        self.assertEqual(
            json.loads(content_dict["experiment_config"]),
            exp_config,
        )

    def test_build_base_log_contents_start_time_is_string(self) -> None:
        storage = self._make_storage()
        contents = storage._build_base_log_contents()
        content_dict = dict(contents)
        # All SLS values must be strings
        self.assertIsInstance(content_dict["experiment_start_time"], str)

    # ------------------------------------------------------------------
    # save_task_meta
    # ------------------------------------------------------------------

    def test_save_task_meta_writes_file(self) -> None:
        storage = self._make_storage()
        task_id = "task-001"
        meta = {"input": {"question": "Q1"}, "label": "label1"}
        storage.save_task_meta(task_id=task_id, meta_info=meta)

        expected_file = os.path.join(
            self.save_dir,
            task_id,
            "task_meta.json",
        )
        self.assertTrue(os.path.exists(expected_file))
        with open(expected_file, encoding="utf-8") as f:
            loaded = json.load(f)
        self.assertEqual(loaded, meta)

    def test_save_task_meta_caches_in_memory(self) -> None:
        storage = self._make_storage()
        task_id = "task-002"
        meta = {"input": {"question": "Q2"}}
        storage.save_task_meta(task_id=task_id, meta_info=meta)

        self.assertIn(task_id, storage._task_meta_cache)
        self.assertEqual(storage._task_meta_cache[task_id], meta)

    def test_save_task_meta_cache_isolated_per_task(self) -> None:
        storage = self._make_storage()
        storage.save_task_meta("task-a", {"x": 1})
        storage.save_task_meta("task-b", {"x": 2})
        self.assertEqual(storage._task_meta_cache["task-a"], {"x": 1})
        self.assertEqual(storage._task_meta_cache["task-b"], {"x": 2})

    def test_save_task_meta_increments_total_tasks(self) -> None:
        storage = self._make_storage()
        storage.save_task_meta("task-a", {"x": 1})
        storage.save_task_meta("task-b", {"x": 2})
        self.assertEqual(storage._total_tasks, 2)

    # ------------------------------------------------------------------
    # save_solution_result
    # ------------------------------------------------------------------

    def test_save_solution_result_writes_local_file(self) -> None:
        storage = self._make_storage()
        task_id = "task-sol-001"
        repeat_id = "0"
        output = self._make_solution_output()

        with patch.object(storage, "_put_log"):
            storage.save_solution_result(
                task_id=task_id,
                repeat_id=repeat_id,
                output=output,
            )

        solution_file = os.path.join(
            self.save_dir,
            task_id,
            repeat_id,
            "solution.json",
        )
        self.assertTrue(os.path.exists(solution_file))

    def test_save_solution_result_calls_put_log(self) -> None:
        storage = self._make_storage()
        task_id = "task-sol-002"
        repeat_id = "0"
        output = self._make_solution_output()

        with patch.object(storage, "_put_log") as mock_put:
            storage.save_solution_result(
                task_id=task_id,
                repeat_id=repeat_id,
                output=output,
            )
            mock_put.assert_called_once()

    def test_save_solution_result_put_log_contains_correct_fields(self) -> None:
        storage = self._make_storage(experiment_id="exp-xyz")
        task_id = "task-sol-003"
        repeat_id = "1"
        output = self._make_solution_output(success=True, output="hello")

        captured: list[list[tuple[str, str]]] = []

        def capture_put_log(contents: list[tuple[str, str]]) -> None:
            captured.append(contents)

        with patch.object(storage, "_put_log", side_effect=capture_put_log):
            storage.save_solution_result(
                task_id=task_id,
                repeat_id=repeat_id,
                output=output,
            )

        self.assertEqual(len(captured), 1)
        content_dict = dict(captured[0])

        self.assertEqual(content_dict["experiment_id"], "exp-xyz")
        self.assertEqual(content_dict["task_id"], task_id)
        self.assertEqual(content_dict["repeat_id"], repeat_id)
        self.assertIn("experiment_output", content_dict)
        self.assertIn("experiment_input", content_dict)
        self.assertIn("data_config", content_dict)
        self.assertNotIn("experiment_data", content_dict)

    def test_save_solution_result_experiment_output_content(self) -> None:
        storage = self._make_storage()
        task_id = "task-sol-004"
        repeat_id = "0"
        output = self._make_solution_output(success=False, output="error_output")

        captured: list[list[tuple[str, str]]] = []
        with patch.object(storage, "_put_log", side_effect=captured.append):
            storage.save_solution_result(
                task_id=task_id,
                repeat_id=repeat_id,
                output=output,
            )

        content_dict = dict(captured[0])
        # experiment_output is now a top-level string. For failed tasks with
        # no structured error meta, it should be prefixed with "ERROR:".
        self.assertEqual(
            content_dict["experiment_output"],
            "ERROR: UnknownError - Unknown error",
        )

    def test_save_solution_result_experiment_output_success_is_raw_string(self) -> None:
        storage = self._make_storage()
        task_id = "task-sol-004b"
        repeat_id = "0"
        output = self._make_solution_output(success=True, output="hello world")

        captured: list[list[tuple[str, str]]] = []
        with patch.object(storage, "_put_log", side_effect=captured.append):
            storage.save_solution_result(
                task_id=task_id,
                repeat_id=repeat_id,
                output=output,
            )

        content_dict = dict(captured[0])
        # For successful tasks with str output, experiment_output is the raw
        # string, not a JSON wrapper.
        self.assertEqual(content_dict["experiment_output"], "hello world")

    def test_save_solution_result_uses_cached_task_meta(self) -> None:
        storage = self._make_storage()
        task_id = "task-sol-005"
        repeat_id = "0"
        meta = {"input": {"question": "What is AI?", "id": "q-999"}}
        output = self._make_solution_output()

        storage.save_task_meta(task_id=task_id, meta_info=meta)

        captured: list[list[tuple[str, str]]] = []
        with patch.object(storage, "_put_log", side_effect=captured.append):
            storage.save_solution_result(
                task_id=task_id,
                repeat_id=repeat_id,
                output=output,
            )

        content_dict = dict(captured[0])
        # experiment_input is the rendered input as a JSON string.
        self.assertEqual(
            json.loads(content_dict["experiment_input"]),
            meta["input"],
        )
        # Dataset columns are flattened as top-level dataset.<col> fields.
        self.assertEqual(content_dict["dataset.question"], "What is AI?")
        self.assertEqual(content_dict["dataset.id"], "q-999")

        data_config = json.loads(content_dict["data_config"])
        self.assertEqual(data_config["dataset_item_id"], "q-999")

    def test_save_solution_result_data_config_structure(self) -> None:
        storage = self._make_storage()
        task_id = "task-sol-006"
        repeat_id = "0"
        output = self._make_solution_output()

        captured: list[list[tuple[str, str]]] = []
        with patch.object(storage, "_put_log", side_effect=captured.append):
            storage.save_solution_result(
                task_id=task_id,
                repeat_id=repeat_id,
                output=output,
            )

        content_dict = dict(captured[0])
        data_config = json.loads(content_dict["data_config"])
        self.assertEqual(data_config["data_type"], "dataset")
        self.assertEqual(data_config["project"], self.config.project)
        self.assertEqual(data_config["dataset_id"], self.config.dataset)

    def test_save_solution_result_dataset_item_id_falls_back_to_task_id(self) -> None:
        storage = self._make_storage()
        task_id = "task-fallback"
        repeat_id = "0"
        output = self._make_solution_output()
        # no task meta cached → dataset_item_id should fall back to task_id

        captured: list[list[tuple[str, str]]] = []
        with patch.object(storage, "_put_log", side_effect=captured.append):
            storage.save_solution_result(
                task_id=task_id,
                repeat_id=repeat_id,
                output=output,
            )

        content_dict = dict(captured[0])
        data_config = json.loads(content_dict["data_config"])
        self.assertEqual(data_config["dataset_item_id"], task_id)

    def test_save_solution_result_tracks_success(self) -> None:
        storage = self._make_storage()
        with patch.object(storage, "_put_log"):
            storage.save_solution_result("t1", "0", self._make_solution_output(success=True))
            storage.save_solution_result("t2", "0", self._make_solution_output(success=False))
            storage.save_solution_result("t3", "0", self._make_solution_output(success=True))
        self.assertEqual(storage._completed_tasks, 2)
        self.assertEqual(storage._failed_tasks, 1)

    # ------------------------------------------------------------------
    # _put_log ImportError
    # ------------------------------------------------------------------

    def test_put_log_raises_import_error_when_sdk_missing(self) -> None:
        storage = self._make_storage()
        with patch.dict("sys.modules", {"aliyun": None, "aliyun.log": None}):
            with self.assertRaises((ImportError, AttributeError)):
                storage._put_log([("key", "value")])

    # ------------------------------------------------------------------
    # _get_sls_client ImportError
    # ------------------------------------------------------------------

    def test_get_sls_client_raises_import_error_when_sdk_missing(self) -> None:
        storage = self._make_storage()
        with patch.dict("sys.modules", {"aliyun": None, "aliyun.log": None}):
            with self.assertRaises((ImportError, AttributeError)):
                storage._get_sls_client()

    # ------------------------------------------------------------------
    # _get_agentloop_client ImportError
    # ------------------------------------------------------------------

    def test_get_agentloop_client_raises_import_error_when_sdk_missing(self) -> None:
        storage = self._make_storage()
        with patch.dict(
            "sys.modules",
            {
                "alibabacloud_agentloop20260520": None,
                "alibabacloud_agentloop20260520.client": None,
                "alibabacloud_tea_openapi": None,
                "alibabacloud_tea_openapi.utils_models": None,
            },
        ):
            with self.assertRaises((ImportError, AttributeError)):
                storage._get_agentloop_client()

    # ------------------------------------------------------------------
    # _resolve_project
    # ------------------------------------------------------------------

    def test_resolve_project_success(self) -> None:
        storage = self._make_storage()
        storage.config.project = ""

        mock_resp = MagicMock()
        mock_resp.body.sls_project = "found_project"

        mock_client = MagicMock()
        mock_client.get_agent_space.return_value = mock_resp

        mock_agentloop_pkg = MagicMock()
        with patch.dict("sys.modules", {"alibabacloud_agentloop20260520": mock_agentloop_pkg}):
            with patch.object(storage, "_get_agentloop_client", return_value=mock_client):
                storage._resolve_project()

        self.assertEqual(storage.config.project, "found_project")

    def test_resolve_project_no_sls_project_raises(self) -> None:
        storage = self._make_storage()
        storage.config.project = ""

        mock_resp = MagicMock()
        mock_resp.body.sls_project = None

        mock_client = MagicMock()
        mock_client.get_agent_space.return_value = mock_resp

        mock_agentloop_pkg = MagicMock()
        with patch.dict("sys.modules", {"alibabacloud_agentloop20260520": mock_agentloop_pkg}):
            with patch.object(storage, "_get_agentloop_client", return_value=mock_client):
                with self.assertRaises(ValueError) as ctx:
                    storage._resolve_project()
        self.assertIn("SLS project", str(ctx.exception))

    # ------------------------------------------------------------------
    # upload_experiment_record
    # ------------------------------------------------------------------

    def test_upload_experiment_record_calls_api(self) -> None:
        storage = self._make_storage(experiment_id="exp-upload-001")
        storage._total_tasks = 10
        storage._completed_tasks = 8
        storage._failed_tasks = 2

        mock_resp = MagicMock()
        mock_client = MagicMock()
        mock_client.upload_experiment.return_value = mock_resp

        with patch.object(storage, "_get_agentloop_client", return_value=mock_client):
            storage.upload_experiment_record({})

        mock_client.upload_experiment.assert_called_once()

    def test_upload_experiment_data_source_format(self) -> None:
        storage = self._make_storage()

        mock_client = MagicMock()

        with patch.object(
            _vendor_models,
            "UploadExperimentRequest",
            side_effect=lambda **kw: MagicMock(**kw),
        ) as mock_req_cls, \
            patch.object(
            _vendor_models,
            "ExperimentConfig",
            side_effect=lambda **kw: MagicMock(**kw),
        ), \
            patch.object(storage, "_get_agentloop_client", return_value=mock_client):
            storage.upload_experiment_record({})

        kwargs = mock_req_cls.call_args[1]
        ds = kwargs["data_source"]
        self.assertEqual(ds["type"], "DATASET_FULL")
        self.assertEqual(ds["datasetId"], "test_dataset")
        self.assertNotIn("project", ds)
        self.assertNotIn("data_type", ds)
        self.assertNotIn("dataset_id", ds)

    def test_upload_experiment_with_evaluators(self) -> None:
        storage = self._make_storage_with_evaluators([
            EvaluatorConfig(
                evaluator_ref="Builtin.accuracy",
                result_type="score",
                variable_mapping={"output": "output"},
            ),
        ])

        mock_client = MagicMock()

        with patch.object(
            _vendor_models,
            "UploadExperimentRequest",
            side_effect=lambda **kw: MagicMock(**kw),
        ) as mock_req_cls, \
            patch.object(
            _vendor_models,
            "Evaluator",
            side_effect=lambda **kw: MagicMock(**kw),
        ) as mock_eval_cls, \
            patch.object(
            _vendor_models,
            "ExperimentConfig",
            side_effect=lambda **kw: MagicMock(**kw),
        ), \
            patch.object(storage, "_get_agentloop_client", return_value=mock_client):
            storage.upload_experiment_record({})

        kwargs = mock_req_cls.call_args[1]
        evaluators = kwargs["evaluators"]
        self.assertIsNotNone(evaluators)
        self.assertEqual(len(evaluators), 1)

        eval_kwargs = mock_eval_cls.call_args[1]
        self.assertEqual(eval_kwargs["evaluator_ref"], "Builtin.accuracy")
        self.assertEqual(eval_kwargs["result_type"], "score")

    def test_upload_experiment_no_evaluators_when_none(self) -> None:
        storage = self._make_storage()

        mock_client = MagicMock()

        with patch.object(
            _vendor_models,
            "UploadExperimentRequest",
            side_effect=lambda **kw: MagicMock(**kw),
        ) as mock_req_cls, \
            patch.object(
            _vendor_models,
            "ExperimentConfig",
            side_effect=lambda **kw: MagicMock(**kw),
        ), \
            patch.object(storage, "_get_agentloop_client", return_value=mock_client):
            storage.upload_experiment_record({})

        kwargs = mock_req_cls.call_args[1]
        self.assertIsNone(kwargs["evaluators"])

    # ------------------------------------------------------------------
    # validate_evaluators (on AgentLoopConfig)
    # ------------------------------------------------------------------

    def _make_storage_with_evaluators(
        self,
        evaluators: list[EvaluatorConfig],
        **kwargs: object,
    ) -> AgentLoopEvaluatorStorage:
        """Create storage with evaluators, bypassing init-time validation."""
        self.config.evaluators = evaluators
        with patch.object(AgentLoopConfig, "validate_evaluators"):
            return self._make_storage(**kwargs)

    def _mock_get_evaluator_response(
        self,
        variables: list[dict] | None = None,
        config: dict | None = None,
    ) -> MagicMock:
        """Build a mock GetEvaluator response."""
        mock_resp = MagicMock()
        if config is not None:
            mock_resp.body.evaluator.config = config
        elif variables is not None:
            mock_resp.body.evaluator.config = {"variables": variables}
        else:
            mock_resp.body.evaluator.config = {}
        return mock_resp

    def _validate_config_with_mock(
        self,
        evaluators: list[EvaluatorConfig],
        mock_client: MagicMock,
    ) -> None:
        """Run validate_evaluators on a config with a mocked client."""
        self.config.evaluators = evaluators
        self.config._evaluators_validated = False
        mock_agentloop_pkg = MagicMock()
        with patch.dict("sys.modules", {"alibabacloud_agentloop20260520": mock_agentloop_pkg}):
            with patch.object(self.config, "_create_agentloop_client", return_value=mock_client):
                self.config.validate_evaluators()

    def test_validate_evaluators_success(self) -> None:
        mock_resp = self._mock_get_evaluator_response(variables=[
            {"name": "input", "description": "Question"},
            {"name": "output", "description": "Answer"},
        ])
        mock_dataset_resp = MagicMock()
        mock_dataset_resp.body.schema = {"question": MagicMock(), "answer": MagicMock()}

        mock_client = MagicMock()
        mock_client.get_evaluator.return_value = mock_resp
        mock_client.get_dataset.return_value = mock_dataset_resp

        self._validate_config_with_mock([
            EvaluatorConfig(
                evaluator_ref="Builtin.completeness",
                variable_mapping={
                    "input": "experiment_input",
                    "output": "experiment_output",
                },
            ),
        ], mock_client)

        mock_client.get_evaluator.assert_called_once()

    def test_validate_evaluators_not_found_raises(self) -> None:
        mock_client = MagicMock()
        mock_client.get_evaluator.side_effect = RuntimeError("404 Not Found")

        self.config.evaluators = [EvaluatorConfig(evaluator_ref="NonExistent")]
        self.config._evaluators_validated = False
        mock_agentloop_pkg = MagicMock()
        with patch.dict("sys.modules", {"alibabacloud_agentloop20260520": mock_agentloop_pkg}):
            with patch.object(self.config, "_create_agentloop_client", return_value=mock_client):
                with self.assertRaises(ValueError) as ctx:
                    self.config.validate_evaluators()
        self.assertIn("NonExistent", str(ctx.exception))
        self.assertIn("Failed to fetch evaluator", str(ctx.exception))

    def test_validate_evaluators_missing_variables_raises(self) -> None:
        mock_resp = self._mock_get_evaluator_response(variables=[
            {"name": "input", "description": "Question"},
            {"name": "output", "description": "Answer"},
            {"name": "expected_output", "description": "Ground truth"},
        ])
        mock_client = MagicMock()
        mock_client.get_evaluator.return_value = mock_resp

        self.config.evaluators = [
            EvaluatorConfig(
                evaluator_ref="Builtin.correctness",
                variable_mapping={
                    "input": "experiment_input",
                    "output": "experiment_output",
                },
            ),
        ]
        self.config._evaluators_validated = False
        mock_agentloop_pkg = MagicMock()
        with patch.dict("sys.modules", {"alibabacloud_agentloop20260520": mock_agentloop_pkg}):
            with patch.object(self.config, "_create_agentloop_client", return_value=mock_client):
                with self.assertRaises(ValueError) as ctx:
                    self.config.validate_evaluators()
        self.assertIn("expected_output", str(ctx.exception))

    def test_validate_evaluators_skipped_when_none(self) -> None:
        self.config.evaluators = None
        self.config.validate_evaluators()  # should not raise

    def test_validate_evaluators_no_config_skips_variable_check(self) -> None:
        mock_resp = MagicMock()
        mock_resp.body.evaluator.config = None
        mock_client = MagicMock()
        mock_client.get_evaluator.return_value = mock_resp

        self._validate_config_with_mock([
            EvaluatorConfig(evaluator_ref="Builtin.coherence"),
        ], mock_client)

    def test_validate_evaluators_no_name_raises(self) -> None:
        self.config.evaluators = [EvaluatorConfig()]
        self.config._evaluators_validated = False
        with self.assertRaises(ValueError) as ctx:
            self.config.validate_evaluators()
        self.assertIn("evaluator_ref", str(ctx.exception))


    def test_validate_evaluators_skips_when_already_validated(self) -> None:
        self.config.evaluators = [EvaluatorConfig(evaluator_ref="X")]
        self.config._evaluators_validated = True
        self.config.validate_evaluators()  # should not raise or call API

    # ------------------------------------------------------------------
    # _validate_mapping_value (on AgentLoopConfig)
    # ------------------------------------------------------------------

    def test_validate_mapping_value_experiment_output(self) -> None:
        result = AgentLoopConfig._validate_mapping_value(
            "experiment_output", {"col1"},
        )
        self.assertIsNone(result)

    def test_validate_mapping_value_experiment_input(self) -> None:
        result = AgentLoopConfig._validate_mapping_value(
            "experiment_input", {"col1"},
        )
        self.assertIsNone(result)

    def test_validate_mapping_value_dataset_valid_column(self) -> None:
        result = AgentLoopConfig._validate_mapping_value(
            "dataset.question", {"question", "answer"},
        )
        self.assertIsNone(result)

    def test_validate_mapping_value_dataset_invalid_column(self) -> None:
        result = AgentLoopConfig._validate_mapping_value(
            "dataset.nonexistent", {"question", "answer"},
        )
        self.assertIsNotNone(result)
        self.assertIn("nonexistent", result)
        self.assertIn("does not exist", result)

    def test_validate_mapping_value_dataset_missing_column_name(self) -> None:
        result = AgentLoopConfig._validate_mapping_value(
            "dataset.", {"question"},
        )
        self.assertIsNotNone(result)
        self.assertIn("missing a column name", result)

    def test_validate_mapping_value_invalid_format(self) -> None:
        result = AgentLoopConfig._validate_mapping_value(
            "some_random_value", {"col1"},
        )
        self.assertIsNotNone(result)
        self.assertIn("invalid", result)

    # ------------------------------------------------------------------
    # validate_evaluators — value validation integration
    # ------------------------------------------------------------------

    def test_validate_evaluators_invalid_mapping_value_raises(self) -> None:
        mock_resp = self._mock_get_evaluator_response(variables=[
            {"name": "input", "description": "Question"},
            {"name": "output", "description": "Answer"},
        ])
        mock_dataset_resp = MagicMock()
        mock_dataset_resp.body.schema = {"question": MagicMock(), "answer": MagicMock()}
        mock_client = MagicMock()
        mock_client.get_evaluator.return_value = mock_resp
        mock_client.get_dataset.return_value = mock_dataset_resp

        self.config.evaluators = [
            EvaluatorConfig(
                evaluator_ref="Builtin.correctness",
                variable_mapping={"input": "experiment_input", "output": "bad_value"},
            ),
        ]
        self.config._evaluators_validated = False
        mock_agentloop_pkg = MagicMock()
        with patch.dict("sys.modules", {"alibabacloud_agentloop20260520": mock_agentloop_pkg}):
            with patch.object(self.config, "_create_agentloop_client", return_value=mock_client):
                with self.assertRaises(ValueError) as ctx:
                    self.config.validate_evaluators()
        self.assertIn("bad_value", str(ctx.exception))
        self.assertIn("invalid", str(ctx.exception))

    def test_validate_evaluators_invalid_column_raises(self) -> None:
        mock_resp = self._mock_get_evaluator_response(variables=[
            {"name": "input", "description": "Question"},
            {"name": "output", "description": "Answer"},
        ])
        mock_dataset_resp = MagicMock()
        mock_dataset_resp.body.schema = {"question": MagicMock(), "answer": MagicMock()}
        mock_client = MagicMock()
        mock_client.get_evaluator.return_value = mock_resp
        mock_client.get_dataset.return_value = mock_dataset_resp

        self.config.evaluators = [
            EvaluatorConfig(
                evaluator_ref="Builtin.correctness",
                variable_mapping={"input": "experiment_input", "output": "dataset.nonexistent"},
            ),
        ]
        self.config._evaluators_validated = False
        mock_agentloop_pkg = MagicMock()
        with patch.dict("sys.modules", {"alibabacloud_agentloop20260520": mock_agentloop_pkg}):
            with patch.object(self.config, "_create_agentloop_client", return_value=mock_client):
                with self.assertRaises(ValueError) as ctx:
                    self.config.validate_evaluators()
        self.assertIn("nonexistent", str(ctx.exception))
        self.assertIn("does not exist", str(ctx.exception))

    def test_validate_evaluators_experiment_data_column_valid(self) -> None:
        mock_resp = self._mock_get_evaluator_response(variables=[
            {"name": "input", "description": "Question"},
            {"name": "output", "description": "Answer"},
            {"name": "expected_output", "description": "Ground truth"},
        ])
        mock_dataset_resp = MagicMock()
        mock_dataset_resp.body.schema = {"question": MagicMock(), "answer": MagicMock()}
        mock_client = MagicMock()
        mock_client.get_evaluator.return_value = mock_resp
        mock_client.get_dataset.return_value = mock_dataset_resp

        self._validate_config_with_mock([
            EvaluatorConfig(
                evaluator_ref="Builtin.correctness",
                variable_mapping={
                    "input": "experiment_input",
                    "output": "experiment_output",
                    "expected_output": "dataset.answer",
                },
            ),
        ], mock_client)

    def test_validate_evaluators_dataset_columns_lazy_loaded(self) -> None:
        """get_dataset is not called when evaluator has no variables."""
        mock_resp = MagicMock()
        mock_resp.body.evaluator.config = None
        mock_client = MagicMock()
        mock_client.get_evaluator.return_value = mock_resp

        self._validate_config_with_mock([
            EvaluatorConfig(evaluator_ref="Builtin.coherence"),
        ], mock_client)

        mock_client.get_dataset.assert_not_called()

    # ------------------------------------------------------------------
    # upload_experiment_record (continued)
    # ------------------------------------------------------------------

    def test_upload_experiment_record_does_not_raise_on_failure(self) -> None:
        storage = self._make_storage()

        mock_client = MagicMock()
        mock_client.upload_experiment.side_effect = RuntimeError("API error")

        mock_agentloop_pkg = MagicMock()
        with patch.dict("sys.modules", {"alibabacloud_agentloop20260520": mock_agentloop_pkg}):
            with patch.object(storage, "_get_agentloop_client", return_value=mock_client):
                # Should not raise
                storage.upload_experiment_record({})

    # ------------------------------------------------------------------
    # save_aggregation_result
    # ------------------------------------------------------------------

    def test_save_aggregation_result_calls_upload(self) -> None:
        storage = self._make_storage()
        aggregation = {"total_tasks": 5}

        with patch.object(storage, "upload_experiment_record") as mock_upload:
            storage.save_aggregation_result(aggregation)

        mock_upload.assert_called_once_with(aggregation)

        # Also verify local file was saved
        result_file = os.path.join(self.save_dir, "evaluation_result.json")
        self.assertTrue(os.path.exists(result_file))


if __name__ == "__main__":
    unittest.main()
