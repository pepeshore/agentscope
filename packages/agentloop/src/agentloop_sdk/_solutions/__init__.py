# -*- coding: utf-8 -*-
"""Ready-to-use solution wrappers for common experiment scenarios."""

from ._http_solution import (
    HttpRequestSpec,
    http_solution,
    http_solution_with,
)
from ._command_solution import (
    command_solution,
    command_solution_with,
)

__all__ = [
    "HttpRequestSpec",
    "http_solution",
    "http_solution_with",
    "command_solution",
    "command_solution_with",
]
