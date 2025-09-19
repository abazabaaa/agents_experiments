"""Configuration models and loaders for the agent pipeline."""

from __future__ import annotations

import json
from collections.abc import Mapping
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from agents.model_settings import ModelSettings

from ..prompts.loader import load_markdown
from .models import PipelineConfigModel, PromptsConfigModel

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


def _coerce_float(value: Any, *, name: str, allow_none: bool) -> float | None:
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

    connect: float | None = 5.0
    read: float | None = 120.0
    write: float | None = 30.0
    pool: float | None = 5.0

    @classmethod
    def from_payload(cls, payload: Mapping[str, Any] | None) -> HTTPTimeoutConfig:
        payload = payload or {}
        return cls(
            connect=_coerce_float(
                payload.get("connect"), name="httpx.connect", allow_none=True
            ),
            read=_coerce_float(payload.get("read"), name="httpx.read", allow_none=True),
            write=_coerce_float(
                payload.get("write"), name="httpx.write", allow_none=True
            ),
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
    def from_payload(cls, payload: Mapping[str, Any] | None) -> RetryPolicy:
        payload = payload or {}
        defaults = cls()
        max_attempts = _coerce_int(
            payload.get("max_attempts"),
            name="retry.max_attempts",
            default=defaults.max_attempts,
        )
        if max_attempts < 1:
            raise ValueError("retry.max_attempts must be at least 1")
        initial_delay = _coerce_float(
            payload.get("initial_delay"), name="retry.initial_delay", allow_none=True
        )
        if initial_delay is None:
            initial_delay = defaults.initial_delay
        backoff_multiplier = _coerce_float(
            payload.get("backoff_multiplier"),
            name="retry.backoff_multiplier",
            allow_none=True,
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
        assert (
            initial_delay is not None
            and backoff_multiplier is not None
            and max_delay is not None
        )
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
    def from_payload(cls, payload: Mapping[str, Any] | None) -> ConcurrencyConfig:
        payload = payload or {}
        defaults = cls()
        buffers = _coerce_mapping(payload.get("buffers"), name="concurrency.buffers")
        model_limits = _coerce_mapping(
            payload.get("model_limits"), name="concurrency.model_limits"
        )

        def stage_buffer(name: str, default: int) -> int:
            return _coerce_int(
                buffers.get(name), name=f"concurrency.buffers.{name}", default=default
            )

        base = cls(
            router_pool=_coerce_int(
                payload.get("router_pool"),
                name="concurrency.router_pool",
                default=defaults.router_pool,
            ),
            markdown_pool=_coerce_int(
                payload.get("markdown_pool"),
                name="concurrency.markdown_pool",
                default=defaults.markdown_pool,
            ),
            notebook_pool=_coerce_int(
                payload.get("notebook_pool"),
                name="concurrency.notebook_pool",
                default=defaults.notebook_pool,
            ),
            review_pool=_coerce_int(
                payload.get("review_pool"),
                name="concurrency.review_pool",
                default=defaults.review_pool,
            ),
            naming_pool=_coerce_int(
                payload.get("naming_pool"),
                name="concurrency.naming_pool",
                default=defaults.naming_pool,
            ),
            channel_buffer=_coerce_int(
                payload.get("channel_buffer"),
                name="concurrency.channel_buffer",
                default=defaults.channel_buffer,
            ),
            agent_thread_limit=_coerce_int(
                payload.get("agent_thread_limit"),
                name="concurrency.agent_thread_limit",
                default=defaults.agent_thread_limit,
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
            limit_value = _coerce_int(
                limit, name=f"concurrency.model_limits.{model_name}", default=1
            )
            if limit_value < 1:
                raise ValueError(
                    f"model limit for {model_name!r} must be >= 1 (received {limit_value})"
                )
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
    agent_specs: Mapping[str, AgentSpec]
    stage_prompts: Mapping[str, str]
    # Rework policy for inter-stage review feedback loops
    rework_enabled: bool = False
    rework_max_cycles: int = 0
    rework_target_on_reject: str = "same"  # one of: same, markdown, notebook

    @classmethod
    def from_json(cls, path: Path) -> PipelineConfig:
        payload = json.loads(path.read_text(encoding="utf-8"))
        base_dir = path.parent
        model = PipelineConfigModel.model_validate(payload)

        def _resolve_path(candidate: Path | None, default: str) -> Path:
            value = candidate or Path(default)
            return Path(value)

        logging_cfg = model.logging
        io_cfg = model.io
        concurrency_cfg = model.concurrency.model_dump(exclude_none=True)
        retry_cfg = model.retry.model_dump(exclude_none=True)
        httpx_cfg = model.httpx.model_dump(exclude_none=True)
        rework_cfg = model.rework.model_dump(exclude_none=True)

        log_file = _resolve_path(logging_cfg.log_file, "logs/agent_pipeline.log")
        workflow_name = logging_cfg.trace_workflow_name or "doc-cleaning"
        trace_metadata = dict(logging_cfg.trace_metadata)

        input_artifact = _resolve_path(
            io_cfg.input_artifact, "artifacts/lark_docs.json"
        )
        output_directory = _resolve_path(
            io_cfg.output_directory, "artifacts/cleaned_docs"
        )

        concurrency = ConcurrencyConfig.from_payload(concurrency_cfg)
        retry_policy = RetryPolicy.from_payload(retry_cfg)
        httpx_timeout = HTTPTimeoutConfig.from_payload(httpx_cfg)

        agents_cfg: Mapping[str, Any] = model.agents.root
        agent_specs: dict[str, AgentSpec] = {}
        for key, spec in agents_cfg.items():
            spec_payload = spec.model_dump(exclude_defaults=True, exclude_none=True)
            agent_specs[str(key)] = AgentSpec.from_payload(
                str(key), spec_payload, base_dir
            )

        # Prompts: inline templates and optional directory
        prompts_model: PromptsConfigModel = model.build_prompts_model()
        stage_prompts: dict[str, str] = dict(prompts_model.templates)
        prompts_dir_value = prompts_model.dir
        if prompts_dir_value is not None:
            prompts_dir = prompts_dir_value
            if not prompts_dir.is_absolute():
                prompts_dir = base_dir / prompts_dir
            if not prompts_dir.exists() or not prompts_dir.is_dir():
                raise FileNotFoundError(
                    f"prompts.dir path not found or not a directory: {prompts_dir}"
                )
            for file_path in prompts_dir.iterdir():
                if file_path.is_file() and file_path.suffix.lower() in {".md", ".txt"}:
                    content = load_markdown(
                        file_path, description=f"stage prompt '{file_path.stem}'"
                    )
                    stage_prompts[file_path.stem] = content

        rework_enabled = bool(rework_cfg.get("enabled", False))
        rework_max_cycles = _coerce_int(
            rework_cfg.get("max_cycles"), name="rework.max_cycles", default=0
        )
        if rework_max_cycles < 0:
            raise ValueError("rework.max_cycles must be >= 0")
        target = str(rework_cfg.get("target_on_reject", "same"))
        if target not in {"same", "markdown", "notebook", "router"}:
            raise ValueError(
                "rework.target_on_reject must be one of 'same','markdown','notebook','router'"
            )

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
            stage_prompts=stage_prompts,
            rework_enabled=rework_enabled,
            rework_max_cycles=rework_max_cycles,
            rework_target_on_reject=target,
        )


@dataclass(slots=True)
class AgentSpec:
    """Configuration for a single agent stage."""

    key: str
    name: str
    instructions: str
    model: str
    reasoning_effort: str | None
    verbosity: str | None
    timeout: float | None
    max_tokens: int | None
    run_max_turns: int | None = None
    # Base model settings mapping (validated against ModelSettings). Optional.
    model_settings: Mapping[str, Any] = field(default_factory=dict)
    # Optional Agent-level knobs
    tool_use_behavior: str | None = None
    reset_tool_choice: bool | None = None
    # Optional per-attempt overrides (e.g., a "repair" attempt for JSON failures)
    attempt_overrides: Mapping[str, AttemptOverride] = field(default_factory=dict)

    @classmethod
    def from_payload(
        cls, key: str, payload: Mapping[str, Any], base_dir: Path
    ) -> AgentSpec:
        def str_or_default(value: Any, default: str = "") -> str:
            return default if value is None else str(value)

        instructions_text = ""
        instructions_path_val = payload.get("instructions_path")
        if instructions_path_val is not None:
            instructions_path = Path(str(instructions_path_val))
            if not instructions_path.is_absolute():
                instructions_path = base_dir / instructions_path
            instructions_text = load_markdown(
                instructions_path,
                description=f"agents.{key}.instructions_path",
            )
        else:
            instructions_val = payload.get("instructions")
            if isinstance(instructions_val, (str, bytes)):
                candidate = Path(str(instructions_val))
                resolved = None
                if candidate.is_absolute() and candidate.exists():
                    resolved = candidate
                else:
                    candidate_rel = base_dir / candidate
                    if candidate_rel.exists():
                        resolved = candidate_rel
                if resolved is not None and resolved.is_file():
                    instructions_text = load_markdown(
                        resolved,
                        description=f"agents.{key}.instructions",
                    )
                else:
                    instructions_text = str(instructions_val)

        timeout_value = payload.get("timeout")
        timeout_float = (
            float(timeout_value)
            if isinstance(timeout_value, (int, float))
            and not isinstance(timeout_value, bool)
            else None
        )
        max_tokens_value = payload.get("max_tokens")
        max_tokens_int = (
            int(max_tokens_value)
            if isinstance(max_tokens_value, (int, float))
            and not isinstance(max_tokens_value, bool)
            else None
        )
        run_max_turns_val = payload.get("run_max_turns")
        run_max_turns_int = (
            int(run_max_turns_val)
            if isinstance(run_max_turns_val, (int, float))
            and not isinstance(run_max_turns_val, bool)
            else None
        )
        if run_max_turns_int is not None and run_max_turns_int < 1:
            raise ValueError(f"agents.{key}.run_max_turns must be >= 1")

        # Attempt override parsing (optional)
        def _parse_attempt_overrides(raw: Any) -> Mapping[str, AttemptOverride]:
            if raw is None:
                return {}
            if not isinstance(raw, Mapping):
                raise TypeError(
                    f"agents.{key}.attempt_overrides must be a mapping, received {type(raw)!r}"
                )
            overrides: dict[str, AttemptOverride] = {}
            for name, entry in raw.items():
                if not isinstance(entry, Mapping):
                    raise TypeError(
                        f"agents.{key}.attempt_overrides.{name} must be a mapping"
                    )
                prompt_suffix_val = entry.get("prompt_suffix")
                prompt_suffix: str | None = None
                if isinstance(prompt_suffix_val, (str, bytes)):
                    text = str(prompt_suffix_val)
                    suffix_path = Path(text)
                    if not suffix_path.is_absolute():
                        suffix_path = base_dir / suffix_path
                    if suffix_path.exists() and suffix_path.is_file():
                        prompt_suffix = load_markdown(
                            suffix_path,
                            description=(
                                f"agents.{key}.attempt_overrides.{name}.prompt_suffix"
                            ),
                        )
                    else:
                        prompt_suffix = text
                model_settings_raw = entry.get("model_settings")
                if model_settings_raw is None:
                    ms: Mapping[str, Any] = {}
                elif isinstance(model_settings_raw, Mapping):
                    ms = dict(model_settings_raw)
                else:
                    raise TypeError(
                        f"agents.{key}.attempt_overrides.{name}.model_settings must be a mapping"
                    )
                _validate_model_settings_keys(key, ms)
                overrides[str(name)] = AttemptOverride(
                    prompt_suffix=prompt_suffix, model_settings=ms
                )
            return overrides

        attempt_overrides = _parse_attempt_overrides(payload.get("attempt_overrides"))

        # Validate verbosity and reasoning_effort against documented values
        verbosity_value = (
            str(payload.get("verbosity"))
            if payload.get("verbosity") is not None
            else None
        )
        if verbosity_value is not None and verbosity_value not in {
            "low",
            "medium",
            "high",
        }:
            raise ValueError(
                f"agents.{key}.verbosity must be one of 'low','medium','high' (got {verbosity_value!r})"
            )
        reasoning_effort_value = (
            str(payload.get("reasoning_effort"))
            if payload.get("reasoning_effort") is not None
            else None
        )
        if reasoning_effort_value is not None and reasoning_effort_value not in {
            "minimal",
            "low",
            "medium",
            "high",
        }:
            raise ValueError(
                "agents.{key}.reasoning_effort must be one of 'minimal','low','medium','high' "
                f"(got {reasoning_effort_value!r})"
            )

        # Optional Agent-level knobs
        tool_use_behavior_val = payload.get("tool_use_behavior")
        if tool_use_behavior_val is not None:
            if tool_use_behavior_val not in {"run_llm_again", "stop_on_first_tool"}:
                raise ValueError(
                    f"agents.{key}.tool_use_behavior must be 'run_llm_again' or 'stop_on_first_tool'"
                )
            tool_use_behavior_out: str | None = str(tool_use_behavior_val)
        else:
            tool_use_behavior_out = None

        reset_tool_choice_val = payload.get("reset_tool_choice")
        if reset_tool_choice_val is None:
            reset_tool_choice_out: bool | None = None
        elif isinstance(reset_tool_choice_val, bool):
            reset_tool_choice_out = reset_tool_choice_val
        else:
            raise TypeError(
                f"agents.{key}.reset_tool_choice must be a boolean if provided"
            )

        # Optional model_settings mapping
        model_settings_raw = payload.get("model_settings")
        if model_settings_raw is None:
            model_settings_out: Mapping[str, Any] = {}
        elif isinstance(model_settings_raw, Mapping):
            model_settings_out = dict(model_settings_raw)
            _validate_model_settings_keys(key, model_settings_out)
        else:
            raise TypeError(
                f"agents.{key}.model_settings must be a mapping if provided"
            )

        if not instructions_text:
            raise ValueError(
                f"agents.{key}.instructions must be provided via instructions_path or literal"
            )

        return cls(
            key=key,
            name=str_or_default(payload.get("name"), key),
            instructions=instructions_text,
            model=str_or_default(payload.get("model"), "gpt-5-nano"),
            reasoning_effort=reasoning_effort_value,
            verbosity=verbosity_value,
            timeout=timeout_float,
            max_tokens=max_tokens_int,
            run_max_turns=run_max_turns_int,
            model_settings=model_settings_out,
            tool_use_behavior=tool_use_behavior_out,
            reset_tool_choice=reset_tool_choice_out,
            attempt_overrides=attempt_overrides,
        )


@dataclass(slots=True)
class AttemptOverride:
    """Attempt-specific overrides used for clearly named events.

    Naming convention:
    - Use descriptive keys under ``attempt_overrides`` like ``on_invalid_json``
      to indicate when this override applies.

    Fields:
    - prompt_suffix: Optional string appended to the base prompt for this attempt.
      You can specify a literal string, or a path to a .md/.txt file via
      agents.<stage>.attempt_overrides.<name>.prompt_suffix, which will be loaded
      relative to the config file.
    - model_settings: Mapping of documented fields passed into ModelSettings for
      this attempt. Unknown keys are rejected during config load.
    """

    prompt_suffix: str | None = None
    model_settings: Mapping[str, Any] = field(default_factory=dict)


def _validate_model_settings_keys(stage: str, mapping: Mapping[str, Any]) -> None:
    """Fail fast if the config provides unknown ModelSettings keys.

    This prevents silently passing made-up parameters to the SDK.
    """
    if not mapping:
        return
    allowed = set(ModelSettings.__dataclass_fields__.keys())
    unknown = [k for k in mapping.keys() if k not in allowed]
    if unknown:
        allowed_str = ", ".join(sorted(allowed))
        raise ValueError(
            "Invalid model_settings keys for stage '"
            + stage
            + "': "
            + ", ".join(sorted(unknown))
            + ". Allowed keys: "
            + allowed_str
        )


def load_config(path: str | Path) -> PipelineConfig:
    """Load a :class:`PipelineConfig` from ``path``."""

    config_path = Path(path)
    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path!s}")
    return PipelineConfig.from_json(config_path)
