# -*- coding: utf-8 -*-
"""Unit tests for agentloop_sdk._solutions._command_solution."""
import sys
import os
import unittest

_SDK_SRC_DIR = os.path.join(os.path.dirname(__file__), "..", "src")
if _SDK_SRC_DIR not in sys.path:
    sys.path.insert(0, os.path.abspath(_SDK_SRC_DIR))
_AGENTSCOPE_SRC_DIR = os.path.join(
    os.path.dirname(__file__), "..", "..", "..", "src"
)
if _AGENTSCOPE_SRC_DIR not in sys.path:
    sys.path.insert(0, os.path.abspath(_AGENTSCOPE_SRC_DIR))

from agentloop_sdk._solutions._command_solution import (
    command_solution,
    command_solution_with,
)
from agentscope.evaluate._task import Task


def _make_task(code: str = 'print("hi")') -> Task:
    return Task(
        id="t1",
        input={"code": code},
        ground_truth="",
        metrics=[],
    )


class CommandSolutionTest(unittest.IsolatedAsyncioTestCase):
    async def test_success_stdout(self) -> None:
        def build_command(task: Task):
            return [sys.executable, "-c", task.input["code"]]

        solution = command_solution(build_command, default_timeout=10)
        out = await solution(_make_task(), pre_hook=lambda *_: None)

        self.assertTrue(out.success)
        self.assertIsInstance(out.output, dict)
        self.assertEqual(out.output["stdout"].strip(), "hi")
        self.assertEqual(out.output["returncode"], 0)

    async def test_nonzero_exit(self) -> None:
        def build_command(task: Task):
            return [sys.executable, "-c", "import sys; sys.exit(2)"]

        solution = command_solution(build_command, default_timeout=10)
        out = await solution(_make_task(), pre_hook=lambda *_: None)

        self.assertFalse(out.success)
        self.assertEqual(out.output["returncode"], 2)
        self.assertEqual(out.meta["error_type"], "NonZeroExit")
        self.assertIn("exit 2", out.meta["error_message"])

    async def test_spawn_failure(self) -> None:
        def build_command(task: Task):
            return ["this-binary-does-not-exist-xyz123"]

        solution = command_solution(build_command, default_timeout=10)
        out = await solution(_make_task(), pre_hook=lambda *_: None)

        self.assertFalse(out.success)
        # FileNotFoundError on POSIX
        self.assertEqual(out.meta["error_type"], "FileNotFoundError")

    async def test_shell_mode_string(self) -> None:
        def build_command(task: Task):
            return f"echo {task.input['code']!s}"

        solution = command_solution(build_command, shell=True, default_timeout=10)
        out = await solution(_make_task("hello"), pre_hook=lambda *_: None)

        self.assertTrue(out.success)
        self.assertIn("hello", out.output["stdout"])

    async def test_timeout(self) -> None:
        def build_command(task: Task):
            return [sys.executable, "-c", "import time; time.sleep(5)"]

        solution = command_solution(build_command, default_timeout=0.2)
        out = await solution(_make_task(), pre_hook=lambda *_: None)

        self.assertFalse(out.success)
        self.assertEqual(out.meta["error_type"], "TimeoutExpired")
        self.assertIn("0.2s", out.meta["error_message"])

    async def test_builder_exception(self) -> None:
        def build_command(task: Task):
            raise RuntimeError("bad task")

        solution = command_solution(build_command)
        out = await solution(_make_task(), pre_hook=lambda *_: None)

        self.assertFalse(out.success)
        self.assertEqual(out.meta["error_type"], "RuntimeError")
        self.assertEqual(out.meta["error_message"], "bad task")


class CommandSolutionWithTest(unittest.IsolatedAsyncioTestCase):
    async def test_static_list(self) -> None:
        solution = command_solution_with(
            [sys.executable, "-c", "print('hi')"],
            default_timeout=10,
        )
        out = await solution(_make_task(), pre_hook=lambda *_: None)
        self.assertTrue(out.success)
        self.assertEqual(out.output["stdout"].strip(), "hi")

    async def test_static_string_shell(self) -> None:
        solution = command_solution_with(
            f"{sys.executable} -c \"print('hi')\"",
            shell=True,
            default_timeout=10,
        )
        out = await solution(_make_task(), pre_hook=lambda *_: None)
        self.assertTrue(out.success)
        self.assertIn("hi", out.output["stdout"])

    async def test_callable_cmd(self) -> None:
        def cmd_builder(task: Task):
            return [sys.executable, "-c", task.input["code"]]

        solution = command_solution_with(cmd_builder, default_timeout=10)
        out = await solution(_make_task("print('dynamic')"), pre_hook=lambda *_: None)
        self.assertTrue(out.success)
        self.assertEqual(out.output["stdout"].strip(), "dynamic")


if __name__ == "__main__":
    unittest.main()
