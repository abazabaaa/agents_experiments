# Workflow Architecture

The document pipeline now runs each file as a single Agents SDK workflow:

```
DocTask → WorkflowRunner.process_document → (Orchestrator agent ↔ specialists) → NamedDoc
```

## Orchestrated path

If the configuration defines an `orchestrator` agent, the workflow delegates the
entire conversation to that agent. The orchestrator keeps control of the
conversation and invokes specialist tools to:

1. `route_document` (router) – classify the document as markdown or notebook.
2. `clean_markdown` / `refactor_notebook` – transform the content.
3. `review_output` – approve or reject with feedback.
4. `name_output` – produce the final slug and extension.

The orchestrator returns a `WorkflowOutput` payload summarising route, processed
text, review result, naming decision, and rework cycles. The pipeline writes the
resulting `NamedDoc` directly to disk.

### Handling review failures

- When `review.approved` is `false`, the writer now stores the transformed
  artifact under `output/failures/doc-<id>/` instead of the main output root.
- Each failure directory contains the generated content plus a
  `run_details.json` sidecar capturing the orchestrator's final output and a
  serialized trajectory of tool calls/messages to aid debugging.

## Manual fallback

If no orchestrator is configured, the `WorkflowRunner` reuses the previous flow:

- run router → transformation agent → reviewer loop → namer
- append reviewer feedback as developer messages during rework cycles
- respect the `rework_max_cycles` and `rework_target_on_reject` settings

## Concurrency & observability

- Trio launches one task per document with a semaphore bounded by
  `concurrency.agent_thread_limit`.
- `LimiterPool` continues to guard global/model-level token usage during agent
  calls.
- Structured logs (prefixed with `WORKFLOW_RESULT`) capture the route, slug,
  review status, and rework cycle count for every processed document.

## Running the smoke test

Use the bundled script to exercise the end-to-end workflow with the
`configs/smoke_gpt5_nano.json` configuration:

```
uv run python scripts/gpt5_nano_smoke.py --clean --quiet
```

- `--clean` wipes the output directory before running.
- `--quiet` reduces console logging; omit it if you want verbose traces.
- `--config` and `--expect` flags allow pointing at alternate configs or
  adjusting the expected document count.
