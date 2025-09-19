"""Agent factory utilities backed by :class:`PipelineConfig`."""

from __future__ import annotations

from collections.abc import MutableMapping
from typing import Any

from agents import Agent
from agents.model_settings import ModelSettings
from openai.types.shared import Reasoning

from ..config import AgentSpec, PipelineConfig


class AgentRegistry:
    """Instantiate and cache :class:`Agent` objects from configuration specs."""

    def __init__(self, config: PipelineConfig) -> None:
        self._config = config
        self._cache: MutableMapping[str, Agent[Any]] = {}

    def get_agent(
        self,
        key: str,
        *,
        output_type: Any,
        tools: list[Any] | None = None,
        mcp_servers: list[Any] | None = None,
    ) -> Agent[Any]:
        """Return an Agent instance keyed by ``key`` with optional overrides."""

        if key in self._cache:
            return self._cache[key]
        spec = self._lookup_spec(key)
        model_settings = self._build_model_settings(spec)

        handoff_agents: list[Agent[Any]] = []
        if spec.handoffs:
            missing = [name for name in spec.handoffs if name not in self._cache]
            if missing:
                missing_str = ", ".join(missing)
                raise ValueError(
                    f"Agent '{key}' requires handoffs to {missing_str}, but they are not initialised."
                )
            handoff_agents = [self._cache[name] for name in spec.handoffs]

        agent = Agent(
            name=spec.name,
            instructions=spec.instructions,
            model=spec.model,
            model_settings=model_settings,
            output_type=output_type,
            tools=tools or [],
            mcp_servers=mcp_servers or [],
            tool_use_behavior=(spec.tool_use_behavior or "run_llm_again"),
            reset_tool_choice=(
                spec.reset_tool_choice if spec.reset_tool_choice is not None else True
            ),
            handoffs=handoff_agents,
        )
        self._cache[key] = agent
        return agent

    def _lookup_spec(self, key: str) -> AgentSpec:
        try:
            return self._config.agent_specs[key]
        except KeyError as exc:  # pragma: no cover - defensive guard
            raise KeyError(
                f"Agent spec {key!r} is not defined in config {self._config.path}"
            ) from exc

    @staticmethod
    def _build_model_settings(spec: AgentSpec) -> ModelSettings:
        # Start from config-provided mapping to avoid type-literal friction with static checkers.
        kwargs: dict[str, Any] = dict(spec.model_settings)
        if spec.reasoning_effort and "reasoning" not in kwargs:
            kwargs["reasoning"] = Reasoning(effort=str(spec.reasoning_effort))
        if spec.verbosity and "verbosity" not in kwargs:
            kwargs["verbosity"] = spec.verbosity
        if spec.max_tokens is not None and "max_tokens" not in kwargs:
            kwargs["max_tokens"] = spec.max_tokens
        return ModelSettings(**kwargs)
