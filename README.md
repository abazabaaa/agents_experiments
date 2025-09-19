# Agent Pipeline Experiments

This repository contains a lightweight automation pipeline that drives a
collection of OpenAI Agents through a staged workflow. It ingests a batch of
documents, routes them to the appropriate agent, records reviewer feedback, and
writes the transformed artifacts to `artifacts/smoke_output/`.

The project uses `uv` for dependency management, Trio/Trio-asyncio for
concurrency, and an instrumented `AsyncOpenAI` client that captures detailed
HTTP, tracing, and logging telemetry for every request.

## Prerequisites

1. Install [`uv`](https://github.com/astral-sh/uv) and ensure it is available on
   your `PATH`.
2. Create a `.env` file in the repo root with at least:

   ```env
   OPENAI_API_KEY=sk-...
   ```

   The pipeline reads environment variables as soon as `agent_pipeline` is
   imported, so the `.env` file keeps CLIs and tests consistent.

3. Restore dependencies and pre-commit hooks:

   ```bash
   uv lock && uv sync --group dev && uv run pre-commit install
   ```

## Running the Smoke Test

The fastest way to exercise the pipeline end-to-end is the smoke script. It
loads the default configuration in `configs/smoke_gpt5_nano.json`, limits the
document batch, and writes artifacts into `artifacts/smoke_output/`.

```bash
uv run python scripts/gpt5_nano_smoke.py --clean --quiet --limit 5
```

Key flags:

- `--clean` removes any previous `artifacts/smoke_output/*` files.
- `--quiet` keeps console noise to a minimum while logs capture details.
- `--limit N` restricts the number of documents pulled from the source JSON.

### Expected Results

*Artifacts*: Five files appear in `artifacts/smoke_output/`, for example:

```
artifacts/smoke_output/
├── grammar-composition-example.py
├── py3-to-py2-converter.py
├── reconstruct-json-example.py
├── standalone-example.md
└── turtle-dsl.md
```

*Logs*: Each run creates a timestamped directory under `logs/`, such as
`logs/smoke_pipeline-YYYY-MM-DD_HHmmSs-<suffix>/smoke_pipeline.log`, containing
structured lifecycle messages for every agent call.

*Tracing & HTTP diagnostics*: The package automatically configures additional
telemetry when imported:

- `logs/openai_sdk/traces/trace_dump-*.jsonl` — raw trace/span payloads emitted
  by the OpenAI Agents SDK.
- `logs/openai_sdk/logs/openai_agents-*.log` — DEBUG-level SDK logs, including
  tokenizer usage and agent lifecycle events.
- `openai.agents.http` logger entries annotate each HTTP request, indicating
  retry behaviour, latency, and error stacks when they occur.

These files are invaluable when diagnosing intermittent connection errors or
unexpected agent behaviour.

## Troubleshooting

- **Connection errors / timeouts**: The instrumented client retries failed
  requests (default `max_retries=5`) and logs the root exception. Consult the
  latest `openai_agents-*.log` for the exact error chain.
- **No outputs written**: Check `logs/smoke_pipeline-*/smoke_pipeline.log` for
  `PIPELINE_FAILURE` entries. Failures are recorded with document ID, stage, and
  exception summary.
- **Missing key**: If the SDK logs `OPENAI_CLIENT skip reason=no_api_key`, make
  sure your `.env` file includes `OPENAI_API_KEY` and rerun the command in the
  same shell.

## Development Notes

- Formatting and linting: `uv run ruff format src tests` and
  `uv run ruff check src tests`.
- Unit tests: `uv run pytest` will exercise the pipeline helpers and the smoke
  regression suite.
- Type checking: `just typecheck` or `uv run ty check` (when available) ensures
  new code conforms to the project’s typing standards.

Contributions should follow the existing patterns—small, well-tested changes
with clear logs make it easier to analyze complex agent interactions.
