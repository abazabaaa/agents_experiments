# Changelog

All notable changes to this project will be documented in this file.

## Unreleased

### Added
- Guardrail support: agent specs can now declare `input_guardrails`/`output_guardrails`, and the router stage uses the `reject_empty_document` guardrail. See `src/agent_pipeline/agents/guardrails.py` and `configs/smoke_gpt5_nano.json`.
- Session-backed conversations: each pipeline stage now uses `SQLiteSession` memory with a `session_input_callback` that treats list inputs as the authoritative conversation state. Trio bridges (`trio_asyncio.aio_as_trio`) keep session I/O compatible with our existing concurrency model.
- Document-level tracing: every document run executes within a top-level `trace(...)` context; generated trace IDs propagate through stage contexts for consistent telemetry.

### Changed
- Agent call wrappers now propagate `MaxTurnsExceeded` directly instead of translating it to `TimeoutError`, preserving SDK semantics while still logging the event.

### Notes
- Smoke suite executed via `uv run python scripts/gpt5_nano_smoke.py --clean --quiet --limit 5` to validate the refactor across guardrails, sessions, and tracing changes.
