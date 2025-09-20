"""Helpers for building Agents SDK run configuration."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

from agents.run import RunConfig

from ..config import PipelineConfig
from ..logging import AgentCallContext


def _merge_session_history(
    history: Sequence[dict[str, Any]],
    new_items: Sequence[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Merge session ``history`` with ``new_items`` preserving order."""

    merged: list[dict[str, Any]] = []
    merged.extend(history)
    merged.extend(new_items)
    return merged


def build_run_config(config: PipelineConfig, context: AgentCallContext) -> RunConfig:
    trace_metadata = dict(config.trace_metadata)
    trace_metadata.update(
        {"stage": context.stage, "doc_url": context.doc_url, "run_id": context.run_id}
    )
    return RunConfig(
        workflow_name=config.workflow_name,
        trace_id=context.trace_id,
        trace_metadata=trace_metadata,
        session_input_callback=_merge_session_history,
    )
