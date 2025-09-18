from __future__ import annotations

import json
from pathlib import Path

from agent_pipeline.config import load_config
from agent_pipeline.pipeline import Pipeline


def test_pipeline_creates_run_directory(tmp_path: Path) -> None:
    config_path = tmp_path / "config.json"
    log_file = tmp_path / "logs" / "test.log"
    payload = {
        "logging": {
            "log_file": str(log_file),
            "trace_workflow_name": "test-workflow",
        },
        "io": {
            "input_artifact": str(tmp_path / "input.json"),
            "output_directory": str(tmp_path / "output"),
        },
        "concurrency": {},
        "retry": {},
        "agents": {
            "router": {
                "name": "Router",
                "instructions": "Route",
                "model": "gpt-5-nano",
            },
            "markdown_cleaner": {
                "name": "Markdown",
                "instructions": "Clean",
                "model": "gpt-5-nano",
            },
            "notebook_refactor": {
                "name": "Notebook",
                "instructions": "Refactor",
                "model": "gpt-5-nano",
            },
            "reviewer": {
                "name": "Reviewer",
                "instructions": "Review",
                "model": "gpt-5-nano",
            },
            "namer": {
                "name": "Namer",
                "instructions": "Name",
                "model": "gpt-5-nano",
            },
        },
    }
    config_path.write_text(json.dumps(payload), encoding="utf-8")
    (tmp_path / "input.json").write_text("{}", encoding="utf-8")

    config = load_config(config_path)
    pipeline = Pipeline(config, quiet=True)

    assert pipeline.run_dir.exists()
    copied_config = pipeline.run_dir / config_path.name
    assert copied_config.exists()
    assert pipeline.logger.verbose_path.parent == pipeline.run_dir
    assert pipeline.config.log_file.parent == pipeline.run_dir
