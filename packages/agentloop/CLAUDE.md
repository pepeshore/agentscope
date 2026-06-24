# AgentLoop SDK Development Rules

## Critical Constraint

**NEVER modify files under `/Users/wu.cc/Code/python/agentscope/src/agentscope/`.**

The `agentloop_sdk` package must be fully independent of unreleased agentscope changes. All enhancements (progress bars, logging improvements, new evaluators, etc.) must be implemented within `packages/agentloop/src/agentloop_sdk/` using:

- **Subclass override**: Inherit from PyPI-published agentscope classes and override methods.
- **Mixin pattern**: Use mixins (e.g., `AggregateMixin`) to inject improved behavior via MRO.
- **Bundling**: For classes that don't exist in PyPI agentscope (e.g., `ParallelEvaluator`), bundle them entirely within the SDK.

The agentscope dependency is pinned to `>=1.0.15,<2.0.0` in `pyproject.toml`. Any feature that relies on unreleased agentscope code will break PyPI users.
