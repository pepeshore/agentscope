# -*- coding: utf-8 -*-
"""Unit tests for agentloop_sdk._solutions._http_solution."""
import unittest
from unittest.mock import AsyncMock, MagicMock, patch

import sys
import os

_SDK_SRC_DIR = os.path.join(os.path.dirname(__file__), "..", "src")
if _SDK_SRC_DIR not in sys.path:
    sys.path.insert(0, os.path.abspath(_SDK_SRC_DIR))
_AGENTSCOPE_SRC_DIR = os.path.join(
    os.path.dirname(__file__), "..", "..", "..", "src"
)
if _AGENTSCOPE_SRC_DIR not in sys.path:
    sys.path.insert(0, os.path.abspath(_AGENTSCOPE_SRC_DIR))

from agentloop_sdk._solutions._http_solution import (
    HttpRequestSpec,
    http_solution,
    http_solution_with,
)
from agentscope.evaluate._task import Task


def _make_task(input_data=None) -> Task:
    return Task(
        id="t1",
        input=input_data if input_data is not None else {"input": "hello"},
        ground_truth="",
        metrics=[],
    )


def _patch_async_client(fake_client):
    return patch("httpx.AsyncClient", return_value=fake_client)


def _make_fake_client(resp=None, exc=None):
    client = MagicMock()
    client.request = AsyncMock(
        return_value=resp if exc is None else None,
        side_effect=exc if exc is not None else None,
    )
    client.__aenter__ = AsyncMock(return_value=client)
    client.__aexit__ = AsyncMock(return_value=None)
    return client


def _make_fake_resp(*, status_code=200, json_body=None, text="", headers=None):
    resp = MagicMock()
    resp.status_code = status_code
    resp.headers = headers if headers is not None else {}
    if json_body is not None:
        resp.json.return_value = json_body
    else:
        resp.json.side_effect = ValueError("not json")
    resp.text = text
    resp.raise_for_status = MagicMock()
    return resp


# ============================================================
# HttpRequestSpec validation
# ============================================================

class HttpRequestSpecTest(unittest.TestCase):
    def test_minimal_valid(self) -> None:
        spec = HttpRequestSpec(url="https://example.com")
        self.assertEqual(spec.method, "POST")
        self.assertIsNone(spec.headers)
        self.assertIsNone(spec.timeout)

    def test_method_uppercased(self) -> None:
        spec = HttpRequestSpec(url="https://x", method="get")
        self.assertEqual(spec.method, "GET")

    def test_url_required(self) -> None:
        with self.assertRaises(ValueError):
            HttpRequestSpec(url="")

    def test_url_must_be_http(self) -> None:
        with self.assertRaises(ValueError):
            HttpRequestSpec(url="ftp://x")
        with self.assertRaises(ValueError):
            HttpRequestSpec(url="example.com")

    def test_url_must_be_str(self) -> None:
        with self.assertRaises(ValueError):
            HttpRequestSpec(url=None)  # type: ignore[arg-type]

    def test_unsupported_method(self) -> None:
        with self.assertRaises(ValueError):
            HttpRequestSpec(url="https://x", method="CONNECT")

    def test_json_data_mutually_exclusive(self) -> None:
        with self.assertRaises(ValueError):
            HttpRequestSpec(
                url="https://x",
                json={"a": 1},
                data="raw",
            )

    def test_headers_must_be_dict(self) -> None:
        with self.assertRaises(TypeError):
            HttpRequestSpec(url="https://x", headers="nope")  # type: ignore[arg-type]

    def test_params_must_be_dict(self) -> None:
        with self.assertRaises(TypeError):
            HttpRequestSpec(url="https://x", params="nope")  # type: ignore[arg-type]

    def test_timeout_must_be_positive(self) -> None:
        with self.assertRaises(ValueError):
            HttpRequestSpec(url="https://x", timeout=0)
        with self.assertRaises(ValueError):
            HttpRequestSpec(url="https://x", timeout=-1)


# ============================================================
# http_solution behavior
# ============================================================

class HttpSolutionTest(unittest.IsolatedAsyncioTestCase):
    async def test_success_json_response(self) -> None:
        resp = _make_fake_resp(json_body={"answer": "ok"}, text='{"answer":"ok"}')
        client = _make_fake_client(resp=resp)

        def build_request(task: Task) -> HttpRequestSpec:
            return HttpRequestSpec(
                url="https://example.com/api",
                headers={"key": "secret"},
                json={"input": task.input["input"]},
            )

        with _patch_async_client(client):
            solution = http_solution(build_request)
            out = await solution(_make_task(), pre_hook=lambda *_: None)

        self.assertTrue(out.success)
        self.assertEqual(out.output, {"answer": "ok"})
        self.assertEqual(out.meta["status_code"], 200)
        self.assertIn("key", out.meta["request"]["headers"])
        self.assertEqual(out.meta["request"]["headers"]["key"], "secret")
        args, kwargs = client.request.call_args
        self.assertEqual(args[0], "POST")
        self.assertEqual(args[1], "https://example.com/api")
        self.assertEqual(kwargs["headers"]["key"], "secret")
        self.assertIn("traceparent", kwargs["headers"])
        self.assertEqual(kwargs["json"], {"input": "hello"})

    async def test_success_text_fallback(self) -> None:
        resp = _make_fake_resp(text="plain response")
        client = _make_fake_client(resp=resp)

        with _patch_async_client(client):
            solution = http_solution(
                lambda task: HttpRequestSpec(url="https://x"),
            )
            out = await solution(_make_task(), pre_hook=lambda *_: None)

        self.assertTrue(out.success)
        self.assertEqual(out.output, "plain response")

    async def test_http_status_error(self) -> None:
        import httpx

        fake_resp = MagicMock()
        fake_resp.status_code = 500
        fake_resp.text = "boom"

        err = httpx.HTTPStatusError(
            "Server error",
            request=MagicMock(),
            response=fake_resp,
        )
        client = _make_fake_client(exc=err)

        with _patch_async_client(client):
            solution = http_solution(
                lambda task: HttpRequestSpec(url="https://x"),
            )
            out = await solution(_make_task(), pre_hook=lambda *_: None)

        self.assertFalse(out.success)
        self.assertEqual(out.meta["error_type"], "HTTPStatusError")
        self.assertEqual(out.meta["status_code"], 500)
        self.assertIn("HTTP 500", out.meta["error_message"])
        self.assertEqual(out.meta["request"]["url"], "https://x")

    async def test_transport_error(self) -> None:
        client = _make_fake_client(exc=ConnectionError("dns fail"))

        with _patch_async_client(client):
            solution = http_solution(
                lambda task: HttpRequestSpec(url="https://x"),
            )
            out = await solution(_make_task(), pre_hook=lambda *_: None)

        self.assertFalse(out.success)
        self.assertEqual(out.meta["error_type"], "ConnectionError")
        self.assertEqual(out.meta["error_message"], "dns fail")

    async def test_default_content_type_header(self) -> None:
        resp = _make_fake_resp(json_body={})
        client = _make_fake_client(resp=resp)

        with _patch_async_client(client):
            solution = http_solution(
                lambda task: HttpRequestSpec(
                    url="https://x",
                    json={"a": 1},
                ),
            )
            out = await solution(_make_task(), pre_hook=lambda *_: None)

        self.assertTrue(out.success)
        _, kwargs = client.request.call_args
        self.assertEqual(
            kwargs["headers"]["Content-Type"],
            "application/json",
        )
        self.assertIn("traceparent", kwargs["headers"])

    async def test_build_request_returns_dict_rejected(self) -> None:
        # No http call should be made; the helper must fail with a clear error.
        client = _make_fake_client(resp=_make_fake_resp())

        with _patch_async_client(client):
            solution = http_solution(
                lambda task: {"url": "https://x"},  # type: ignore[arg-type]
            )
            out = await solution(_make_task(), pre_hook=lambda *_: None)

        self.assertFalse(out.success)
        self.assertEqual(out.meta["error_type"], "TypeError")
        self.assertIn("HttpRequestSpec", out.meta["error_message"])
        client.request.assert_not_called()

    async def test_build_request_exception_surfaced(self) -> None:
        client = _make_fake_client(resp=_make_fake_resp())

        def bad_build(task):
            raise RuntimeError("task malformed")

        with _patch_async_client(client):
            solution = http_solution(bad_build)
            out = await solution(_make_task(), pre_hook=lambda *_: None)

        self.assertFalse(out.success)
        self.assertEqual(out.meta["error_type"], "RuntimeError")
        self.assertEqual(out.meta["error_message"], "task malformed")

    async def test_spec_validation_failure_surfaced(self) -> None:
        client = _make_fake_client(resp=_make_fake_resp())

        def build_bad(task: Task) -> HttpRequestSpec:
            # Triggers ValueError in __post_init__
            return HttpRequestSpec(url="ftp://x")  # type: ignore[arg-type]

        with _patch_async_client(client):
            solution = http_solution(build_bad)
            out = await solution(_make_task(), pre_hook=lambda *_: None)

        self.assertFalse(out.success)
        self.assertEqual(out.meta["error_type"], "ValueError")
        client.request.assert_not_called()


# ============================================================
# http_solution_with
# ============================================================

class HttpSolutionWithTest(unittest.IsolatedAsyncioTestCase):
    async def test_static_json(self) -> None:
        resp = _make_fake_resp(json_body={"answer": "ok"})
        client = _make_fake_client(resp=resp)

        with _patch_async_client(client):
            solution = http_solution_with(
                url="https://example.com/api",
                headers={"key": "secret"},
                json={"a": 1},
                timeout=30,
            )
            out = await solution(_make_task(), pre_hook=lambda *_: None)

        self.assertTrue(out.success)
        args, kwargs = client.request.call_args
        self.assertEqual(kwargs["json"], {"a": 1})
        self.assertEqual(kwargs["headers"]["key"], "secret")
        self.assertIn("traceparent", kwargs["headers"])

    async def test_body_builder_overrides_json(self) -> None:
        resp = _make_fake_resp(json_body={})
        client = _make_fake_client(resp=resp)

        with _patch_async_client(client):
            solution = http_solution_with(
                url="https://example.com",
                json={"static": "ignored"},
                body_builder=lambda task: {"input": task.input["input"]},
            )
            out = await solution(_make_task(), pre_hook=lambda *_: None)

        self.assertTrue(out.success)
        _, kwargs = client.request.call_args
        self.assertEqual(kwargs["json"], {"input": "hello"})

    async def test_static_config_validated_at_construction(self) -> None:
        with self.assertRaises(ValueError):
            http_solution_with(url="ftp://x")
        with self.assertRaises(ValueError):
            http_solution_with(url="", json={"a": 1})
        with self.assertRaises(ValueError):
            http_solution_with(
                url="https://x",
                json={"a": 1},
                data="raw",
            )


# ============================================================
# Trace context injection
# ============================================================

class HttpSolutionTraceTest(unittest.IsolatedAsyncioTestCase):
    async def test_traceparent_injected(self) -> None:
        resp = _make_fake_resp(json_body={"ok": True})
        client = _make_fake_client(resp=resp)

        with _patch_async_client(client):
            solution = http_solution(
                lambda task: HttpRequestSpec(url="https://x"),
            )
            out = await solution(_make_task(), pre_hook=lambda *_: None)

        self.assertTrue(out.success)
        _, kwargs = client.request.call_args
        self.assertIn("traceparent", kwargs["headers"])
        self.assertTrue(
            kwargs["headers"]["traceparent"].startswith("00-"),
        )

    async def test_trace_id_in_meta(self) -> None:
        resp = _make_fake_resp(json_body={})
        client = _make_fake_client(resp=resp)

        with _patch_async_client(client):
            solution = http_solution(
                lambda task: HttpRequestSpec(url="https://x"),
            )
            out = await solution(_make_task(), pre_hook=lambda *_: None)

        self.assertTrue(out.success)
        self.assertIn("traceId", out.meta)
        self.assertEqual(len(out.meta["traceId"]), 32)

    async def test_eagleeye_trace_id_priority(self) -> None:
        resp = _make_fake_resp(json_body={})
        resp.headers = {
            "eagleeye-traceId": "eagle-123",
            "traceId": "generic-456",
        }
        client = _make_fake_client(resp=resp)

        with _patch_async_client(client):
            solution = http_solution(
                lambda task: HttpRequestSpec(url="https://x"),
            )
            out = await solution(_make_task(), pre_hook=lambda *_: None)

        self.assertTrue(out.success)
        self.assertEqual(out.meta["traceId"], "eagle-123")

    async def test_response_trace_id_header_priority(self) -> None:
        resp = _make_fake_resp(json_body={})
        resp.headers = {"traceId": "resp-trace-789"}
        client = _make_fake_client(resp=resp)

        with _patch_async_client(client):
            solution = http_solution(
                lambda task: HttpRequestSpec(url="https://x"),
            )
            out = await solution(_make_task(), pre_hook=lambda *_: None)

        self.assertTrue(out.success)
        self.assertEqual(out.meta["traceId"], "resp-trace-789")

    async def test_otel_trace_id_fallback(self) -> None:
        resp = _make_fake_resp(json_body={})
        resp.headers = {}
        client = _make_fake_client(resp=resp)

        with _patch_async_client(client):
            solution = http_solution(
                lambda task: HttpRequestSpec(url="https://x"),
            )
            out = await solution(_make_task(), pre_hook=lambda *_: None)

        self.assertTrue(out.success)
        self.assertIn("traceId", out.meta)
        self.assertEqual(len(out.meta["traceId"]), 32)

    async def test_trace_id_on_http_error(self) -> None:
        import httpx

        fake_resp = MagicMock()
        fake_resp.status_code = 502
        fake_resp.text = "bad gateway"
        fake_resp.headers = {"eagleeye-traceId": "err-trace-abc"}

        err = httpx.HTTPStatusError(
            "Bad Gateway",
            request=MagicMock(),
            response=fake_resp,
        )
        client = _make_fake_client(exc=err)

        with _patch_async_client(client):
            solution = http_solution(
                lambda task: HttpRequestSpec(url="https://x"),
            )
            out = await solution(_make_task(), pre_hook=lambda *_: None)

        self.assertFalse(out.success)
        self.assertEqual(out.meta["traceId"], "err-trace-abc")

    async def test_trace_id_on_transport_error(self) -> None:
        client = _make_fake_client(exc=ConnectionError("timeout"))

        with _patch_async_client(client):
            solution = http_solution(
                lambda task: HttpRequestSpec(url="https://x"),
            )
            out = await solution(_make_task(), pre_hook=lambda *_: None)

        self.assertFalse(out.success)
        self.assertIn("traceId", out.meta)
        self.assertEqual(len(out.meta["traceId"]), 32)

    async def test_original_headers_not_mutated(self) -> None:
        resp = _make_fake_resp(json_body={})
        client = _make_fake_client(resp=resp)
        original_headers = {"Authorization": "Bearer token"}

        with _patch_async_client(client):
            solution = http_solution(
                lambda task: HttpRequestSpec(
                    url="https://x",
                    headers=original_headers,
                ),
            )
            await solution(_make_task(), pre_hook=lambda *_: None)

        self.assertNotIn("traceparent", original_headers)


if __name__ == "__main__":
    unittest.main()
