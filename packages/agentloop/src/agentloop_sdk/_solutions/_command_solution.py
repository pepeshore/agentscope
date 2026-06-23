# -*- coding: utf-8 -*-
"""Solution wrapper that turns a command builder into an evaluator solution.

Usage:
    from agentloop_sdk import command_solution

    def build_command(task):
        return ["python", "-c", task.input["code"]]

    solution = command_solution(build_command)
    await evaluator.run(solution)
"""

import asyncio
from typing import Any, Awaitable, Callable, Mapping

from agentscope.evaluate import SolutionOutput, Task


def command_solution(
    build_command: Callable[[Task], "str | list[str]"],
    *,
    default_timeout: float = 60.0,
    cwd: str | None = None,
    env: Mapping[str, str] | None = None,
    shell: bool = False,
) -> Callable[[Task, Callable], Awaitable[SolutionOutput]]:
    """Wrap a command builder into an evaluator solution function.

    Args:
        build_command (`Callable[[Task], str | list[str]]`):
            A synchronous function that takes a `Task` and returns either a
            command argument list (used with ``create_subprocess_exec``) or
            a single command string (used with ``create_subprocess_shell``
            when ``shell=True``).
        default_timeout (`float`):
            Per-command timeout in seconds.
        cwd (`str | None`):
            Working directory for the subprocess.
        env (`Mapping[str, str] | None`):
            Environment variable overrides merged onto ``os.environ``.
        shell (`bool`):
            When ``True``, run the command string via the shell. Ignored
            when ``build_command`` returns a list.

    Returns:
        `Callable[[Task, Callable], Awaitable[SolutionOutput]]`:
            An async solution function compatible with
            `GeneralEvaluator.run`.
    """

    async def _solution(
        task: Task,
        pre_hook: Callable,
    ) -> SolutionOutput:
        import os

        try:
            cmd = build_command(task)
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

        is_shell = shell or isinstance(cmd, str)
        full_env = None
        if env is not None:
            full_env = dict(os.environ)
            full_env.update(env)

        command_repr = cmd if is_shell else list(cmd)

        try:
            if is_shell:
                proc = await asyncio.create_subprocess_shell(
                    cmd if isinstance(cmd, str) else " ".join(cmd),
                    stdout=asyncio.subprocess.PIPE,
                    stderr=asyncio.subprocess.PIPE,
                    cwd=cwd,
                    env=full_env,
                )
            else:
                proc = await asyncio.create_subprocess_exec(
                    *cmd,
                    stdout=asyncio.subprocess.PIPE,
                    stderr=asyncio.subprocess.PIPE,
                    cwd=cwd,
                    env=full_env,
                )
        except Exception as e:  # noqa: BLE001 - spawn failure
            return SolutionOutput(
                success=False,
                output="",
                trajectory=[],
                meta={
                    "error_type": type(e).__name__,
                    "error_message": str(e),
                    "command": command_repr,
                },
            )

        try:
            stdout_b, stderr_b = await asyncio.wait_for(
                proc.communicate(),
                timeout=default_timeout,
            )
        except asyncio.TimeoutError:
            try:
                proc.kill()
            except ProcessLookupError:
                pass
            return SolutionOutput(
                success=False,
                output="",
                trajectory=[],
                meta={
                    "error_type": "TimeoutExpired",
                    "error_message": (
                        f"Command timed out after {default_timeout}s"
                    ),
                    "command": command_repr,
                },
            )
        except Exception as e:  # noqa: BLE001 - runtime error
            return SolutionOutput(
                success=False,
                output="",
                trajectory=[],
                meta={
                    "error_type": type(e).__name__,
                    "error_message": str(e),
                    "command": command_repr,
                },
            )

        stdout = (stdout_b or b"").decode("utf-8", errors="replace")
        stderr = (stderr_b or b"").decode("utf-8", errors="replace")
        returncode = proc.returncode if proc.returncode is not None else -1

        body = {
            "stdout": stdout.rstrip("\n"),
            "stderr": stderr.rstrip("\n"),
            "returncode": returncode,
        }

        if returncode == 0:
            return SolutionOutput(
                success=True,
                output=body,
                trajectory=[],
                meta={"command": command_repr},
            )

        return SolutionOutput(
            success=False,
            output=body,
            trajectory=[],
            meta={
                "error_type": "NonZeroExit",
                "error_message": f"exit {returncode}: {stderr.strip()}",
                "command": command_repr,
            },
        )

    return _solution


def command_solution_with(
    cmd: "str | list[str] | Callable[[Task], str | list[str]]",
    *,
    default_timeout: float = 60.0,
    cwd: str | None = None,
    env: Mapping[str, str] | None = None,
    shell: bool = False,
) -> Callable[[Task, Callable], Awaitable[SolutionOutput]]:
    """Build a solution from a static or per-task command.

    Args:
        cmd (`str | list[str] | Callable[[Task], str | list[str]]`):
            A static command (``str`` or ``list[str]``) or a callable that
            takes a `Task` and returns the command for that task.
        default_timeout (`float`):
            Per-command timeout in seconds.
        cwd (`str | None`):
            Working directory for the subprocess.
        env (`Mapping[str, str] | None`):
            Environment variable overrides merged onto ``os.environ``.
        shell (`bool`):
            When ``True``, run the command string via the shell. Ignored
            when ``cmd`` resolves to a list.

    Returns:
        `Callable[[Task, Callable], Awaitable[SolutionOutput]]`:
            An async solution function compatible with
            `GeneralEvaluator.run`.
    """
    if callable(cmd):
        build_command: Callable[[Task], "str | list[str]"] = cmd
    else:
        static_cmd = cmd

        def build_command(task: Task):  # noqa: ANN202 - trivial passthrough
            return static_cmd

    return command_solution(
        build_command,
        default_timeout=default_timeout,
        cwd=cwd,
        env=env,
        shell=shell,
    )
