# -*- coding: utf-8 -*-
"""Solution wrapper that turns a request builder into an evaluator solution.

Usage (low-level):

    from agentloop_sdk import http_solution, HttpRequestSpec

    def build_request(task):
        return HttpRequestSpec(
            url=AGENT_ENDPOINT,
            headers={"key": AGENT_KEY},
            json={"input": task.input["input"]},
        )

    solution = http_solution(build_request)
    await evaluator.run(solution)

Usage (high-level, when only the body depends on the dataset row):

    from agentloop_sdk import http_solution_with

    solution = http_solution_with(
        url=AGENT_ENDPOINT,
        headers={"key": AGENT_KEY},
        body_builder=lambda task: {"input": task.input["input"]},
    )
    await evaluator.run(solution)
"""

import logging
from dataclasses import dataclass
from typing import Any, Awaitable, Callable

from opentelemetry import propagate, trace

from agentscope.evaluate import SolutionOutput, Task

_tracer = trace.get_tracer("agentloop_sdk")
_logger = logging.getLogger(__name__)


_ALLOWED_METHODS = frozenset(
    {"GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS"},
)


@dataclass
class HttpRequestSpec:
    """Validated specification of an HTTP request.

    Required:
        url (`str`): absolute URL starting with ``http://`` or ``https://``.

    Optional:
        method (`str`): HTTP method. Defaults to ``"POST"``. Case-insensitive.
        headers (`dict[str, str] | None`): request headers. When ``None``,
            the helper injects ``{"Content-Type": "application/json"}``
            for backward compatibility.
        json (`Any | None`): JSON body. Mutually exclusive with ``data``.
        data (`Any | None`): raw body. Mutually exclusive with ``json``.
        params (`dict[str, str] | None`): query string parameters.
        timeout (`float | None`): per-request timeout in seconds. When
            ``None``, falls back to the helper's ``default_timeout``.
    """

    url: str
    method: str = "POST"
    headers: dict[str, str] | None = None
    json: Any = None
    data: Any = None
    params: dict[str, str] | None = None
    timeout: float | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.url, str) or not self.url:
            raise ValueError(
                "HttpRequestSpec.url is required and must be a non-empty str"
            )
        if not self.url.startswith(("http://", "https://")):
            raise ValueError(
                "HttpRequestSpec.url must start with http:// or https://: "
                f"{self.url!r}"
            )

        if not isinstance(self.method, str):
            raise TypeError(
                f"HttpRequestSpec.method must be a str, got "
                f"{type(self.method).__name__}"
            )
        self.method = self.method.upper()
        if self.method not in _ALLOWED_METHODS:
            raise ValueError(
                f"unsupported HTTP method: {self.method!r}"
            )

        if self.headers is not None and not isinstance(self.headers, dict):
            raise TypeError(
                "HttpRequestSpec.headers must be a dict or None"
            )
        if self.params is not None and not isinstance(self.params, dict):
            raise TypeError(
                "HttpRequestSpec.params must be a dict or None"
            )

        if self.json is not None and self.data is not None:
            raise ValueError(
                "HttpRequestSpec.json and .data are mutually exclusive"
            )

        if self.timeout is not None and self.timeout <= 0:
            raise ValueError(
                f"HttpRequestSpec.timeout must be > 0, got {self.timeout}"
            )


def _parse_sse(
    raw: str,
    chunk_extractor: Callable[[Any], str] | None = None,
) -> str:
    """Parse SSE text and return concatenated payload.

    For each ``data:`` line (skipping ``[DONE]``), if *chunk_extractor* is
    provided the line is JSON-decoded and passed through the extractor;
    otherwise the raw data string is used directly.
    """
    import json as _json

    parts: list[str] = []
    for line in raw.splitlines():
        stripped = line.strip()
        if not stripped or not stripped.startswith("data:"):
            continue
        payload = stripped[5:].strip()
        if not payload or payload == "[DONE]":
            continue

        if chunk_extractor is not None:
            try:
                parsed = _json.loads(payload)
            except (ValueError, TypeError):
                parts.append(payload)
                continue
            try:
                extracted = chunk_extractor(parsed)
            except Exception:  # noqa: BLE001
                parts.append(payload)
                continue
            if extracted:
                parts.append(str(extracted))
        else:
            parts.append(payload)

    return "".join(parts)


def _is_sse_response(resp: Any, resp_text: str) -> bool:
    """Detect whether a response is SSE based on Content-Type or content."""
    content_type = ""
    if resp is not None and hasattr(resp, "headers"):
        content_type = resp.headers.get("content-type", "").lower()
    return (
        "text/event-stream" in content_type
        or resp_text.lstrip().startswith("data:")
    )


def _extract_trace_id(resp: Any, otel_trace_id: str) -> str:
    """Extract trace ID from response headers, falling back to OTel trace ID.

    Priority: eagleeye-traceId > traceId header > OTel span trace ID.
    """
    if resp is not None and hasattr(resp, "headers"):
        for header_name in ("eagleeye-traceId", "traceId"):
            value = resp.headers.get(header_name)
            if value and len(value) == 32:
                _logger.debug(
                    "traceId from response header %s=%s", header_name, value,
                )
                return value
    _logger.debug("traceId fallback to otel span traceId=%s", otel_trace_id)
    return otel_trace_id


def http_solution(
    build_request: Callable[[Task], HttpRequestSpec],
    *,
    default_timeout: float = 60.0,
    chunk_extractor: Callable[[Any], str] | None = None,
) -> Callable[[Task, Callable], Awaitable[SolutionOutput]]:
    """Wrap an HTTP request builder into an evaluator solution function.

    Args:
        build_request (`Callable[[Task], HttpRequestSpec]`):
            A synchronous function that takes a `Task` and returns a
            validated `HttpRequestSpec`. Returning a plain dict raises
            ``TypeError``; spec-level validation failures are surfaced
            through ``SolutionOutput.meta["error_type"] / ["error_message"]``.
        default_timeout (`float`):
            Per-request timeout in seconds when ``spec.timeout`` is None.
        chunk_extractor (`Callable[[Any], str] | None`):
            Optional extractor for SSE responses. When the response is
            detected as SSE, each ``data:`` payload is JSON-decoded and
            passed to this callable; the return values are concatenated
            as the final output. When ``None``, SSE payloads are
            concatenated as-is.

    Returns:
        `Callable[[Task, Callable], Awaitable[SolutionOutput]]`:
            An async solution function compatible with
            `GeneralEvaluator.run`.
    """

    async def _solution(
        task: Task,
        pre_hook: Callable,
    ) -> SolutionOutput:
        import httpx

        try:
            spec = build_request(task)
        except Exception as e:  # noqa: BLE001 - surface as solution failure
            return SolutionOutput(
                success=False,
                output="",
                trajectory=[],
                meta={
                    "error_type": type(e).__name__,
                    "error_message": str(e),
                },
            )

        if not isinstance(spec, HttpRequestSpec):
            return SolutionOutput(
                success=False,
                output="",
                trajectory=[],
                meta={
                    "error_type": "TypeError",
                    "error_message": (
                        "build_request must return an HttpRequestSpec, got "
                        f"{type(spec).__name__}"
                    ),
                },
            )

        timeout = (
            spec.timeout if spec.timeout is not None else default_timeout
        )
        headers = dict(spec.headers) if spec.headers else {
            "Content-Type": "application/json",
        }

        with _tracer.start_as_current_span(
            f"http_solution {spec.method} {spec.url}",
        ) as span:
            span_ctx = span.get_span_context()
            otel_trace_id = format(span_ctx.trace_id, "032x")

            propagate.inject(carrier=headers)

            request_summary: dict[str, Any] = {
                "method": spec.method,
                "url": spec.url,
                "headers": dict(headers),
            }
            if spec.json is not None:
                request_summary["json"] = spec.json
            if spec.data is not None:
                request_summary["data"] = spec.data
            if spec.params is not None:
                request_summary["params"] = spec.params

            resp = None
            resp_text = ""
            status_code = None
            try:
                async with httpx.AsyncClient(timeout=timeout) as client:
                    async with client.stream(
                        spec.method,
                        spec.url,
                        headers=headers,
                        json=spec.json,
                        data=spec.data,
                        params=spec.params,
                    ) as resp:
                        status_code = resp.status_code
                        resp.raise_for_status()
                        chunks: list[str] = []
                        async for chunk in resp.aiter_text():
                            chunks.append(chunk)
                        resp_text = "".join(chunks)
            except httpx.HTTPStatusError as e:
                span.set_status(
                    trace.StatusCode.ERROR,
                    str(e),
                )
                trace_id = _extract_trace_id(
                    e.response, otel_trace_id,
                )
                error_body = resp_text or (
                    e.response.text
                    if e.response is not None
                    else ""
                )
                return SolutionOutput(
                    success=False,
                    output=error_body,
                    trajectory=[],
                    meta={
                        "experiment_input": spec.json if spec.json is not None else spec.data,
                        "error_type": "HTTPStatusError",
                        "error_message": (
                            f"HTTP {status_code}: "
                            f"{error_body[:500]}"
                            if status_code is not None
                            else str(e)
                        ),
                        "status_code": status_code,
                        "request": request_summary,
                        "traceId": trace_id,
                    },
                )
            except Exception as e:  # noqa: BLE001 - network / transport errors
                span.set_status(
                    trace.StatusCode.ERROR,
                    str(e),
                )
                return SolutionOutput(
                    success=False,
                    output="",
                    trajectory=[],
                    meta={
                        "experiment_input": spec.json if spec.json is not None else spec.data,
                        "error_type": type(e).__name__,
                        "error_message": str(e),
                        "request": request_summary,
                        "traceId": otel_trace_id,
                    },
                )

            span.set_status(trace.StatusCode.OK)
            trace_id = _extract_trace_id(resp, otel_trace_id)
            _logger.info("%s %s traceId=%s", spec.method, spec.url, trace_id)

        if _is_sse_response(resp, resp_text):
            body: Any = _parse_sse(resp_text, chunk_extractor)
        else:
            try:
                import json as _json
                body = _json.loads(resp_text)
            except Exception:  # noqa: BLE001 - fall back to text
                body = resp_text

        return SolutionOutput(
            success=True,
            output=body,
            trajectory=[],
            meta={
                "experiment_input": spec.json if spec.json is not None else spec.data,
                "request": request_summary,
                "status_code": status_code,
                "traceId": trace_id,
            },
        )

    return _solution


def http_solution_with(
    url: str,
    *,
    method: str = "POST",
    headers: dict[str, str] | None = None,
    json: Any = None,
    data: Any = None,
    params: dict[str, str] | None = None,
    body_builder: Callable[[Task], Any] | None = None,
    timeout: float = 60.0,
    chunk_extractor: Callable[[Any], str] | None = None,
) -> Callable[[Task, Callable], Awaitable[SolutionOutput]]:
    """Build a solution from a static request template.

    Args:
        url (`str`): request URL. Required.
        method (`str`): HTTP method. Defaults to ``"POST"``.
        headers (`dict[str, str] | None`): request headers. ``None`` →
            helper injects ``{"Content-Type": "application/json"}``.
        json (`Any | None`): static JSON body. Ignored when ``body_builder``
            is provided.
        data (`Any | None`): static raw body. Mutually exclusive with
            ``json`` / ``body_builder``.
        params (`dict[str, str] | None`): query string parameters.
        body_builder (`Callable[[Task], Any] | None`): per-task JSON body
            extractor. When provided, overrides ``json``.
        timeout (`float`): per-request timeout in seconds.
        chunk_extractor (`Callable[[Any], str] | None`):
            Optional extractor for SSE responses. Each ``data:`` payload
            is JSON-decoded and passed to this callable; return values
            are concatenated as the final output. When ``None``, SSE
            payloads are concatenated as-is.

    Returns:
        `Callable[[Task, Callable], Awaitable[SolutionOutput]]`:
            An async solution function compatible with
            `GeneralEvaluator.run`.
    """

    # Eager validation of the static parts so misconfiguration fails fast at
    # construction time, not on the first task.
    HttpRequestSpec(
        url=url,
        method=method,
        headers=headers,
        json=json,
        data=data,
        params=params,
        timeout=timeout,
    )

    def build_request(task: Task) -> HttpRequestSpec:
        body = body_builder(task) if body_builder is not None else json
        return HttpRequestSpec(
            url=url,
            method=method,
            headers=headers,
            json=body,
            data=data,
            params=params,
            timeout=timeout,
        )

    return http_solution(
        build_request,
        default_timeout=timeout,
        chunk_extractor=chunk_extractor,
    )
