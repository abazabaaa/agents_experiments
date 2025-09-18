from __future__ import annotations

import json
from pathlib import Path

from agent_pipeline.config import load_config


def test_load_config_with_stage_buffers(tmp_path: Path) -> None:
    payload = {
        "logging": {
            "log_file": "logs/test.log",
            "trace_workflow_name": "workflow",
            "trace_metadata": {"env": "test"},
        },
        "io": {
            "input_artifact": "artifacts/input.json",
            "output_directory": "artifacts/output",
        },
        "concurrency": {
            "router_pool": 4,
            "markdown_pool": 5,
            "notebook_pool": 2,
            "review_pool": 3,
            "naming_pool": 1,
            "channel_buffer": 20,
            "agent_thread_limit": 8,
            "buffers": {"router": 5, "write": 1},
            "model_limits": {"gpt-5": 4, "gpt-5-mini": 6},
        },
        "retry": {
            "max_attempts": 4,
            "initial_delay": 0.5,
            "backoff_multiplier": 2.0,
            "max_delay": 60.0,
            "jitter_ratio": 0.1,
        },
        "httpx": {
            "connect": 2.0,
            "read": None,
            "write": 15.0,
            "pool": 3.0,
        },
        "agents": {
            "router": {
                "name": "Router",
                "instructions": "Route documents",
                "model": "gpt-5-nano",
                "verbosity": "low",
            }
        },
    }
    config_path = tmp_path / "config.json"
    config_path.write_text(json.dumps(payload), encoding="utf-8")

    config = load_config(config_path)

    assert config.log_file == Path("logs/test.log")
    assert config.input_artifact == Path("artifacts/input.json")
    assert config.concurrency.router_pool == 4
    assert config.concurrency.stage_buffers["router"] == 5
    # Stage without explicit override inherits channel buffer
    assert config.concurrency.stage_buffers["markdown"] == 20
    # Model limits preserved
    assert config.concurrency.model_limits["gpt-5"] == 4
    assert config.retry_policy.max_attempts == 4
    assert config.retry_policy.initial_delay == 0.5
    assert config.httpx_timeout.read is None
    assert "router" in config.agent_specs
    router_spec = config.agent_specs["router"]
    assert router_spec.model == "gpt-5-nano"
    assert router_spec.timeout is None
