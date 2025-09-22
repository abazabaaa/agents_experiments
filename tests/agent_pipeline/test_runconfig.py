from __future__ import annotations

from types import SimpleNamespace

from agent_pipeline.agents.runconfig import build_run_config, _prefer_new_items


def test_prefer_new_items_overrides_history() -> None:
    history = [{"role": "user", "content": "old"}]
    new_items = [{"role": "user", "content": "new"}]
    result = _prefer_new_items(history, new_items)
    assert result is new_items


def test_prefer_new_items_retains_history_when_empty() -> None:
    history = [{"role": "user", "content": "old"}]
    new_items: list[dict[str, str]] = []
    result = _prefer_new_items(history, new_items)
    assert result is history


def test_build_run_config_assigns_callback_and_metadata() -> None:
    config = SimpleNamespace(trace_metadata={"existing": "meta"}, workflow_name="workflow")
    context = SimpleNamespace(
        stage="routing",
        doc_url="http://example.com",
        run_id="router-1",
        trace_id="trace_abc",
    )

    run_config = build_run_config(config, context)

    assert run_config.workflow_name == "workflow"
    assert run_config.trace_id == "trace_abc"
    assert run_config.trace_metadata["stage"] == "routing"
    assert run_config.trace_metadata["doc_url"] == "http://example.com"
    assert run_config.trace_metadata["run_id"] == "router-1"
    assert run_config.session_input_callback is _prefer_new_items
