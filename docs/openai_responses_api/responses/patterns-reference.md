# Responses API Patterns: Tools, Structured Outputs, Streaming, and Chaining

This guide distills common patterns for using the Responses API effectively. It contrasts background resume vs. multi‑turn chaining, explains when to prefer `text_format` (structured outputs) vs. function tools, and shows how to combine both in a single agent loop.

## Background Resume vs. Multi‑Turn Chaining

- Background + Resume
  - Start in background and optionally stream partial results.
  - Capture `response.id` from the `response.created` event.
  - Later, resume with `response_id` and `starting_after` to continue event streaming.
  - Best for: long‑running generations, interactive viewers, pausing and resuming work without losing server state.
  - Example: `docs/responses/examples/background*.py`

- Multi‑Turn Chaining
  - Pass `previous_response_id` on each follow‑up `responses.create(...)` call.
  - The server keeps the conversation context; you only send new inputs (messages, `function_call_output`s).
  - Best for: agentic tool use across multiple turns, conversation state reuse without resending prior content.
  - Reference: `docs/responses/azure-responses.md` (chaining section)

Guidance: Use background resume to pause and reattach to a single long generation; use chaining for actual multi‑turn conversations with tool calls and evolving inputs.

## Structured Outputs (`text_format`) vs. Tools

- Structured Outputs (text_format)
  - Specify a Pydantic model via `text_format=MySchema`.
  - The SDK parses assistant message text into `MySchema` (available as `item.parsed`).
  - Best for: extracting a predictable structure (tables, summaries, configs) from the model’s text output.
  - Examples: `structured-output.py`, `streaming.py`.

- Function Tools (tools)
  - Define argument schemas (often via `openai.pydantic_function_tool(MyArgs)`), passed as `tools=[...]`.
  - The model emits `function_call` items with typed `parsed_arguments` that you can execute in your runtime.
  - Best for: connecting the model to external capabilities (APIs, DBs, code), ensuring strict argument validation.
  - Examples: `structured-outputs-tools.py`, `streaming-tools.py`.

Guidance: Prefer `text_format` when you want the model to emit structured text for you to parse; prefer `tools` when the model should invoke external actions with validated arguments. You can use both in the same workflow.

## Combining Tools + Structured Outputs in One Agent Loop

A robust agent loop often needs both: tool calling for data acquisition and structured parsing for final reporting.

1) Initial turn (tool discovery enabled):
- Call `responses.create(...)` with `tools=[...]` and your developer `instructions`.
- Input is a user prompt describing the task.
- The model may return `function_call` items.

2) Execute tool calls concurrently:
- Parse `function_call` items; for each, run the external tool with typed `parsed_arguments`.
- Build a list of `{"type": "function_call_output", "call_id": ..., "output": ...}` preserving order.

3) Follow‑up turn (continue conversation):
- Call `responses.create(...)` again with `previous_response_id=<prior.id>`, same `instructions` + `tools`, and `input=function_call_output[]`.
- Repeat until no more `function_call` items are produced.

4) Final turn with structured output:
- Optionally request a final summary or report and parse it using `responses.parse(..., text_format=MyReportSchema)` or stream with `text_format`.

Notes:
- Preserving `call_id` on each `function_call_output` lets the model correlate results to the original tool calls.
- Use a per‑turn timeout and fixed concurrency to guard against slow tools, and prefer batch tools when available to reduce latency and token use.

## Streaming Patterns (Sync and Async)

- Streaming
  - Use `client.responses.stream(..., text_format=OptionalSchema)`.
  - Iterate events; handle those containing `"output_text"` for partial text.
  - At the end, call `stream.get_final_response()` for the consolidated response.
  - Examples: `streaming.py`, `background-streaming*.py`.

- Background + Streaming
  - Start with `background=True`; record `event.response.id` when `event.type == "response.created"`.
  - Resume later with `response_id` and `starting_after` to continue the event sequence.

## Parameterization Tips

- Core request fields:
  - `model`, `instructions` (developer/system guidance), `input` (prompt or `function_call_output[]`), `tools`, `previous_response_id`, `max_output_tokens`.
- Useful GPT‑5 controls (see `gpt5-new-params.md`):
  - `reasoning_effort` for depth vs. latency.
  - `text={"verbosity": "low|medium|high"}` for output length/style without prompt churn.
- Optional (not shown in every example): `temperature`, `top_p`, `tool_choice`, and other sampling/behavior knobs.

## Anti‑Patterns and Practical Advice

- Don’t resend prior messages when using `previous_response_id`—let the server keep state.
- Don’t conflate structured outputs with tool arguments: use `text_format` for parsing message text; use `tools` for validated call arguments.
- When many similar tool calls arise, prefer a batch tool (one call) and split results after (lower latency, fewer tokens).
- Keep the developer `instructions` stable and specific; include a short tool index and any batching guidance.

## See Also

- Examples in `docs/responses/examples/`
- Azure Responses chaining and lifecycle in `docs/responses/azure-responses.md`
- GPT‑5 prompting and parameters in `docs/responses/gpt5-prompting.md` and `docs/responses/gpt5-new-params.md`
