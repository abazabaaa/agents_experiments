"""Configuration models and loaders for the agent pipeline."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Mapping, MutableMapping, Optional

Number = float | int


def _coerce_int(value: Any, *, name: str, default: int) -> int:
    """Return ``value`` coerced to ``int`` with defensive error messages."""
    if value is None:
        return default
    if isinstance(value, bool):  # guard against bool being a subclass of int
        raise TypeError(f"{name} must be an integer, not boolean")
    if isinstance(value, (int, float)):
        coerced = int(value)
        if coerced < 0:
            raise ValueError(f"{name} must be non-negative (received {value!r})")
        return coerced
    raise TypeError(f"{name} must be an integer (received {type(value)!r})")


def _coerce_float(value: Any, *, name: str, allow_none: bool) -> Optional[float]:
    """Return ``value`` coerced to ``float`` (or ``None`` when allowed)."""
    if value is None:
        if allow_none:
            return None
        raise TypeError(f"{name} must be a float, not None")
    if isinstance(value, bool):
        raise TypeError(f"{name} must be a float, not boolean")
    if isinstance(value, (int, float)):
        return float(value)
    raise TypeError(f"{name} must be a float (received {type(value)!r})")


def _coerce_mapping(value: Any, *, name: str) -> Mapping[str, Any]:
    if value is None:
        return {}
    if isinstance(value, Mapping):
        return value
    raise TypeError(f"{name} must be a mapping (received {type(value)!r})")


@dataclass(slots=True)
class HTTPTimeoutConfig:
    """Timeout configuration passed to ``httpx.AsyncClient``."""

    connect: Optional[float] = 5.0
    read: Optional[float] = 120.0
    write: Optional[float] = 30.0
    pool: Optional[float] = 5.0

    @classmethod
    def from_payload(cls, payload: Mapping[str, Any] | None) -> "HTTPTimeoutConfig":
        payload = payload or {}
        return cls(
            connect=_coerce_float(payload.get("connect"), name="httpx.connect", allow_none=True),
            read=_coerce_float(payload.get("read"), name="httpx.read", allow_none=True),
            write=_coerce_float(payload.get("write"), name="httpx.write", allow_none=True),
            pool=_coerce_float(payload.get("pool"), name="httpx.pool", allow_none=True),
        )


@dataclass(slots=True)
class RetryPolicy:
    """Retry configuration for API calls with exponential backoff."""

    max_attempts: int = 3
    initial_delay: float = 0.5
    backoff_multiplier: float = 2.0
    max_delay: float = 60.0
    jitter_ratio: float = 0.25

    @classmethod
    def from_payload(cls, payload: Mapping[str, Any] | None) -> "RetryPolicy":
        payload = payload or {}
        defaults = cls()
        max_attempts = _coerce_int(
            payload.get("max_attempts"), name="retry.max_attempts", default=defaults.max_attempts
        )
        if max_attempts < 1:
            raise ValueError("retry.max_attempts must be at least 1")
        initial_delay = _coerce_float(
            payload.get("initial_delay"), name="retry.initial_delay", allow_none=True
        )
        if initial_delay is None:
            initial_delay = defaults.initial_delay
        backoff_multiplier = _coerce_float(
            payload.get("backoff_multiplier"), name="retry.backoff_multiplier", allow_none=True
        )
        if backoff_multiplier is None:
            backoff_multiplier = defaults.backoff_multiplier
        max_delay = _coerce_float(
            payload.get("max_delay"), name="retry.max_delay", allow_none=True
        )
        if max_delay is None:
            max_delay = defaults.max_delay
        jitter_ratio_value = _coerce_float(
            payload.get("jitter_ratio"), name="retry.jitter_ratio", allow_none=True
        )
        if jitter_ratio_value is None:
            jitter_ratio_value = defaults.jitter_ratio
        assert initial_delay is not None and backoff_multiplier is not None and max_delay is not None
        assert jitter_ratio_value is not None
        if initial_delay <= 0:
            raise ValueError("retry.initial_delay must be positive")
        if backoff_multiplier < 1:
            raise ValueError("retry.backoff_multiplier must be >= 1")
        if max_delay <= 0:
            raise ValueError("retry.max_delay must be positive")
        if jitter_ratio_value < 0:
            raise ValueError("retry.jitter_ratio must be non-negative")
        return cls(
            max_attempts=max_attempts,
            initial_delay=initial_delay,
            backoff_multiplier=backoff_multiplier,
            max_delay=max_delay,
            jitter_ratio=jitter_ratio_value,
        )


@dataclass(slots=True)
class ConcurrencyConfig:
    """Concurrency knobs for the pipeline."""

    router_pool: int = 2
    markdown_pool: int = 4
    notebook_pool: int = 2
    review_pool: int = 1
    naming_pool: int = 1
    channel_buffer: int = 10
    stage_buffers: Mapping[str, int] = field(default_factory=dict)
    model_limits: Mapping[str, int] = field(default_factory=dict)
    agent_thread_limit: int = 10

    @classmethod
    def from_payload(cls, payload: Mapping[str, Any] | None) -> "ConcurrencyConfig":
        payload = payload or {}
        defaults = cls()
        buffers = _coerce_mapping(payload.get("buffers"), name="concurrency.buffers")
        model_limits = _coerce_mapping(
            payload.get("model_limits"), name="concurrency.model_limits"
        )
        def stage_buffer(name: str, default: int) -> int:
            return _coerce_int(buffers.get(name), name=f"concurrency.buffers.{name}", default=default)

        base = cls(
            router_pool=_coerce_int(payload.get("router_pool"), name="concurrency.router_pool", default=defaults.router_pool),
            markdown_pool=_coerce_int(payload.get("markdown_pool"), name="concurrency.markdown_pool", default=defaults.markdown_pool),
            notebook_pool=_coerce_int(payload.get("notebook_pool"), name="concurrency.notebook_pool", default=defaults.notebook_pool),
            review_pool=_coerce_int(payload.get("review_pool"), name="concurrency.review_pool", default=defaults.review_pool),
            naming_pool=_coerce_int(payload.get("naming_pool"), name="concurrency.naming_pool", default=defaults.naming_pool),
            channel_buffer=_coerce_int(payload.get("channel_buffer"), name="concurrency.channel_buffer", default=defaults.channel_buffer),
            agent_thread_limit=_coerce_int(
                payload.get("agent_thread_limit"), name="concurrency.agent_thread_limit", default=defaults.agent_thread_limit
            ),
        )
        # Stage-specific buffers inherit from channel_buffer when not provided
        base.stage_buffers = {
            stage: stage_buffer(stage, base.channel_buffer)
            for stage in ("router", "markdown", "notebook", "review", "naming", "write")
        }
        # Validate model limiter capacities
        model_limit_map: dict[str, int] = {}
        for model_name, limit in model_limits.items():
            limit_value = _coerce_int(limit, name=f"concurrency.model_limits.{model_name}", default=1)
            if limit_value < 1:
                raise ValueError(f"model limit for {model_name!r} must be >= 1 (received {limit_value})")
            model_limit_map[str(model_name)] = limit_value
        base.model_limits = model_limit_map
        return base


@dataclass(slots=True)
class PipelineConfig:
    """Top-level configuration for the document processing pipeline."""

    path: Path
    log_file: Path
    workflow_name: str
    trace_metadata: Mapping[str, Any]
    input_artifact: Path
    output_directory: Path
    concurrency: ConcurrencyConfig
    retry_policy: RetryPolicy
    httpx_timeout: HTTPTimeoutConfig
    agent_specs: Mapping[str, "AgentSpec"]

    @classmethod
    def from_json(cls, path: Path) -> "PipelineConfig":
        payload = json.loads(path.read_text(encoding="utf-8"))
        logging_cfg = _coerce_mapping(payload.get("logging"), name="logging")
        io_cfg = _coerce_mapping(payload.get("io"), name="io")
        concurrency_cfg = _coerce_mapping(payload.get("concurrency"), name="concurrency")
        retry_cfg = _coerce_mapping(payload.get("retry"), name="retry")
        httpx_cfg = _coerce_mapping(payload.get("httpx"), name="httpx")
        agents_cfg = _coerce_mapping(payload.get("agents"), name="agents")

        log_file = Path(logging_cfg.get("log_file", "logs/agent_pipeline.log"))
        workflow_name = str(logging_cfg.get("trace_workflow_name", "doc-cleaning"))
        trace_metadata = logging_cfg.get("trace_metadata") or {}
        input_artifact = Path(io_cfg.get("input_artifact", "artifacts/lark_docs.json"))
        output_directory = Path(io_cfg.get("output_directory", "artifacts/cleaned_docs"))

        concurrency = ConcurrencyConfig.from_payload(concurrency_cfg)
        retry_policy = RetryPolicy.from_payload(retry_cfg)
        httpx_timeout = HTTPTimeoutConfig.from_payload(httpx_cfg)

        agent_specs: dict[str, AgentSpec] = {}
        for key, spec in agents_cfg.items():
            if not isinstance(spec, Mapping):
                raise TypeError(f"agents.{key} must be a mapping, received {type(spec)!r}")
            agent_specs[str(key)] = AgentSpec.from_payload(str(key), spec)

        return cls(
            path=path,
            log_file=log_file,
            workflow_name=workflow_name,
            trace_metadata=trace_metadata,
            input_artifact=input_artifact,
            output_directory=output_directory,
            concurrency=concurrency,
            retry_policy=retry_policy,
            httpx_timeout=httpx_timeout,
            agent_specs=agent_specs,
        )


@dataclass(slots=True)
class AgentSpec:
    """Configuration for a single agent stage."""

    key: str
    name: str
    instructions: str
    model: str
    reasoning_effort: Optional[str]
    verbosity: Optional[str]
    timeout: Optional[float]
    max_tokens: Optional[int]

    @classmethod
    def from_payload(cls, key: str, payload: Mapping[str, Any]) -> "AgentSpec":
        def str_or_default(value: Any, default: str = "") -> str:
            return default if value is None else str(value)

        timeout_value = payload.get("timeout")
        timeout_float = (
            float(timeout_value)
            if isinstance(timeout_value, (int, float)) and not isinstance(timeout_value, bool)
            else None
        )
        max_tokens_value = payload.get("max_tokens")
        max_tokens_int = (
            int(max_tokens_value)
            if isinstance(max_tokens_value, (int, float)) and not isinstance(max_tokens_value, bool)
            else None
        )
        return cls(
            key=key,
            name=str_or_default(payload.get("name"), key),
            instructions=str_or_default(payload.get("instructions"), ""),
            model=str_or_default(payload.get("model"), "gpt-5-nano"),
            reasoning_effort=(
                str(payload.get("reasoning_effort"))
                if payload.get("reasoning_effort") is not None
                else None
            ),
            verbosity=(str(payload.get("verbosity")) if payload.get("verbosity") is not None else None),
            timeout=timeout_float,
            max_tokens=max_tokens_int,
        )


def load_config(path: str | Path) -> PipelineConfig:
    """Load a :class:`PipelineConfig` from ``path``."""

    config_path = Path(path)
    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path!s}")
    return PipelineConfig.from_json(config_path)
