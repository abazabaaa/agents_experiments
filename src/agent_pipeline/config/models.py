"""Pydantic configuration models for pipeline validation."""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path
from typing import Any

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    ValidationInfo,
    field_validator,
)


class LoggingConfigModel(BaseModel):
    """Subset of logging-related configuration."""

    model_config = ConfigDict(extra="ignore")

    log_file: Path | None = None
    trace_workflow_name: str | None = Field(default=None, alias="trace_workflow_name")
    trace_metadata: dict[str, Any] = Field(default_factory=dict)


class IOConfigModel(BaseModel):
    """Input/output artifact configuration."""

    model_config = ConfigDict(extra="ignore")

    input_artifact: Path | None = None
    output_directory: Path | None = None


class ConcurrencyConfigModel(BaseModel):
    """Concurrency knobs for Trio orchestration and API limits."""

    model_config = ConfigDict(extra="ignore")

    router_pool: int | None = None
    markdown_pool: int | None = None
    notebook_pool: int | None = None
    review_pool: int | None = None
    naming_pool: int | None = None
    channel_buffer: int | None = None
    buffers: dict[str, int] = Field(default_factory=dict)
    model_limits: dict[str, int] = Field(default_factory=dict)
    agent_thread_limit: int | None = None


class RetryConfigModel(BaseModel):
    """Retry policy for transient API failures."""

    model_config = ConfigDict(extra="ignore")

    max_attempts: int | None = None
    initial_delay: float | None = None
    backoff_multiplier: float | None = None
    max_delay: float | None = None
    jitter_ratio: float | None = None


class HTTPConfigModel(BaseModel):
    """httpx.AsyncClient timeout settings."""

    model_config = ConfigDict(extra="ignore")

    connect: float | None = None
    read: float | None = None
    write: float | None = None
    pool: float | None = None


class AttemptOverrideModel(BaseModel):
    """Per-attempt overrides for an agent."""

    model_config = ConfigDict(extra="ignore")

    prompt_suffix: str | None = None
    model_settings: dict[str, Any] = Field(default_factory=dict)


class AgentSpecModel(BaseModel):
    """Normalization for a single agent specification."""

    model_config = ConfigDict(extra="ignore")

    name: str | None = None
    instructions: str | None = None
    instructions_path: Path | None = None
    model: str | None = None
    reasoning_effort: str | None = None
    verbosity: str | None = None
    timeout: float | int | None = None
    max_tokens: int | None = None
    run_max_turns: int | None = None
    model_settings: dict[str, Any] = Field(default_factory=dict)
    tool_use_behavior: str | None = None
    reset_tool_choice: bool | None = None
    attempt_overrides: dict[str, AttemptOverrideModel] = Field(default_factory=dict)
    handoffs: list[str] = Field(default_factory=list)
    tools: list[Any] = Field(default_factory=list)

    @field_validator("model_settings")
    @classmethod
    def ensure_dict(cls, value: Mapping[str, Any] | None) -> dict[str, Any]:
        if value is None:
            return {}
        return dict(value)

    @field_validator("instructions_path", mode="before")
    @classmethod
    def coerce_instructions_path(cls, value: Any) -> Path | None:
        if value is None:
            return None
        if isinstance(value, Path):
            return value
        return Path(str(value))


class AgentsConfigModel(RootModel[dict[str, AgentSpecModel]]):
    """Dynamic mapping of agent keys to their configuration."""


class PromptsConfigModel(BaseModel):
    """Prompt sources and inline overrides."""

    model_config = ConfigDict(extra="ignore")

    dir: Path | None = None
    templates: dict[str, str] = Field(default_factory=dict)

    @field_validator("templates", mode="before")
    @classmethod
    def gather_templates(cls, value: Any, info: ValidationInfo) -> dict[str, str]:
        if isinstance(value, dict):
            return {str(k): str(v) for k, v in value.items()}
        return {}

    @field_validator("dir", mode="before")
    @classmethod
    def coerce_dir(cls, value: Any) -> Path | None:
        if value is None:
            return None
        if isinstance(value, Path):
            return value
        return Path(str(value))

    @classmethod
    def from_raw(cls, raw: Mapping[str, Any]) -> PromptsConfigModel:
        raw = dict(raw)
        dir_value = raw.pop("dir", None)
        inline: dict[str, str] = {}
        for key, val in raw.items():
            if isinstance(val, (str, bytes)):
                inline[str(key)] = str(val)
            else:
                raise TypeError(f"prompts.{key} must be string-like")
        return cls(dir=dir_value, templates=inline)


class ReworkConfigModel(BaseModel):
    """Configuration for review-driven rework loops."""

    model_config = ConfigDict(extra="ignore")

    enabled: bool | None = None
    max_cycles: int | None = None
    target_on_reject: str | None = None


class PipelineConfigModel(BaseModel):
    """Root configuration model for the pipeline JSON file."""

    model_config = ConfigDict(extra="ignore")

    logging: LoggingConfigModel = Field(default_factory=LoggingConfigModel)
    io: IOConfigModel = Field(default_factory=IOConfigModel)
    concurrency: ConcurrencyConfigModel = Field(default_factory=ConcurrencyConfigModel)
    retry: RetryConfigModel = Field(default_factory=RetryConfigModel)
    httpx: HTTPConfigModel = Field(default_factory=HTTPConfigModel)
    agents: AgentsConfigModel
    prompts: dict[str, Any] = Field(default_factory=dict)
    rework: ReworkConfigModel = Field(default_factory=ReworkConfigModel)

    def build_prompts_model(self) -> PromptsConfigModel:
        return PromptsConfigModel.from_raw(self.prompts)
