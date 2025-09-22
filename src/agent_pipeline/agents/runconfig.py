"""Helpers for building Agents SDK run configuration."""

from __future__ import annotations

from agents.run import RunConfig

from ..config import PipelineConfig
from ..logging import AgentCallContext


def _prefer_new_items(history: list, new_items: list) -> list:
    """Replace session history with explicitly provided input when present."""

    return new_items or history


def build_run_config(config: PipelineConfig, context: AgentCallContext) -> RunConfig:
    trace_metadata = dict(config.trace_metadata)
    trace_metadata.update(
        {"stage": context.stage, "doc_url": context.doc_url, "run_id": context.run_id}
    )
    return RunConfig(
        workflow_name=config.workflow_name,
        trace_id=context.trace_id,
        trace_metadata=trace_metadata,
        session_input_callback=_prefer_new_items,
    )
