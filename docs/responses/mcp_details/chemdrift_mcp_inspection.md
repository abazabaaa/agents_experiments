# MCP Streamable HTTP Inspection and Fixtures (Chemdrift)

- Identify authoritative sources and confirm their roles.
- Document MCP session/transport lifecycle and discovery calls.
- Record observed server details (exact values, where from).
- Capture tool schema shape and notable annotations.
- Explain the inspector script and how to run it with `uv`.
- Inventory fixtures created, filepaths, and regeneration steps.

## Purpose

- Provide a precise, source‑linked reference for implementing MCP client behavior in a Responses API chat context.
- Record observed Chemdrift server details and the exact fixtures we generated so they are reproducible and easy to reference during backend cleanup and test design.
- Avoid integration speculation; focus on what to do and where the facts originate.

## Primary Sources (in repo)

- Client/session patterns
  - `docs/responses/mcp_details/mcp_client.py` — persistent Streamable HTTP session and `ClientSession` lifecycle.
  - `docs/responses/mcp_details/tool_schema.py` — tool discovery + instruction synthesis from server init.
  - `docs/responses/mcp_details/azure_responses.py` — Trio/threaded wrapper around Azure Responses API.
  - `docs/responses/mcp_details/conversation.py` — turn loop scaffolding, function_call in → tool outputs out.
  - `docs/responses/mcp_details/parsing.py` — function call extraction and MCP result stringification.
  - `docs/responses/mcp_details/pipeline.py` — end-to-end orchestration for molecules/documents using the above.
  - `docs/responses/mcp_details/anythingmcp.md` — reference implementation of full‑feature MCP server behavior.
  - `docs/responses/mcp_details/.env.example` and `docs/responses/mcp_details/e3_ligase_extraction_config.json` — concrete settings model.

- Inspector script we added
  - `examples/mcp_inspect_chemdrift.py` — connects via Streamable HTTP, runs discovery, prints/dumps results.

## MCP Transport and Session Lifecycle

- Transport: Streamable HTTP (per MCP spec 2025-03-26). We maintain a single, long‑lived bidirectional stream for the entire conversation (not per‑call).
- Implementation pattern (see `mcp_client.py`):
  - Establish context with `streamablehttp_client(url=..., headers=..., timeout=..., sse_read_timeout=...)` which yields `(read_stream, write_stream, get_session_id)`.
  - Wrap with `ClientSession(read_stream, write_stream)` and call `await session.initialize()` exactly once at session start.
  - Reuse the `session` for listings (`list_tools`, `list_prompts`, `list_resources`) and tool calls.
  - Clean teardown: close `ClientSession`, then the stream client context.

## Discovery Calls and Data Flow

- `initialize()` returns server metadata and instructions:
  - `serverInfo`: `{ name, version, title? }`
  - `capabilities`: supported subsystems (`tools`, `prompts`, `resources`, `logging`, `experimental`, possibly `roots`).
  - `instructions`: server-provided guidance text.
- `list_tools()` returns tool descriptors:
  - `name`, `title?`, `description`, `inputSchema`, optional `outputSchema`, optional `annotations`, optional `meta`.
- Optional listings (SDK/server dependent):
  - `list_prompts()` and `list_resources()`; present if supported. Roots are advertised via `capabilities.roots`.

## Tool Schema + Instruction Synthesis (from sources)

- `tool_schema.py` maps MCP tools to Responses function tool specs:
  - `{"type": "function", "name", "description", "parameters"}` where `parameters` is a JSON Schema object.
  - Description derived from `title` + `description`.
- Base instructions assembled from `initialize()`:
  - Include server name/version, server `instructions` body, and a concise list of tool names plus first-line descriptions.
  - Developer/system instructions can be appended from config.

## Observed Server Details (Chemdrift)

Source: inspector run of `examples/mcp_inspect_chemdrift.py` via `uv` on local/default URL (`http://localhost:7998/mcp/`).

- Connection
  - URL: `http://localhost:7998/mcp/`
  - Session ID: present (from `get_session_id()`)
  - Server: `ChemServer v1.13.0` (from `initialize().serverInfo`)

- Instructions (verbatim from `initialize().instructions`)
  - “This server accepts SMILES strings and can (i) analyse structure with drug-likeness properties and IUPAC names, (ii) visualise atom numbering, (iii) fragment molecules, and (iv) stitch molecules. All atom indices are 0‑based. Use examine_molecule before edits.”

- Capabilities (from `initialize().capabilities`)
  - `tools: { listChanged: true }`
  - `prompts: { listChanged: true }`
  - `resources: { subscribe: false, listChanged: true }`
  - `experimental: {}`, `logging: null`
  - No explicit `roots` entry in this snapshot.

- Tools (from `list_tools()`)
  - Count: 13 tools.
  - Representative tools:
    - `examine_molecule_tool`: detailed analysis; some servers wrap `outputSchema` with `x-fastmcp-wrap-result: true`.
    - `visualize_molecule_tool`: generates images; no `outputSchema`.
    - `fragment_molecule_tool`: requires `smiles` and `bonds_to_break` with defaults for boolean switches.
    - Batch tools (`batch_visualization`, `batch_examine_molecules`) include annotations/tags like `batch`, `images`, `public`, `analysis`.
  - Tool annotations often indicate read-only/idempotency hints.

- Prompts/Resources (optional listings)
  - `list_prompts()` → 0
  - `list_resources()` → 0

## Inspector Script

- Path: `examples/mcp_inspect_chemdrift.py`
- Behavior:
  - Uses Streamable HTTP, initializes session, prints URL/session ID/server.
  - Prints server instructions and capabilities JSON.
  - Prints `list_tools()` result; best-effort `list_prompts()` and `list_resources()`.
  - Supports multiple `--header` values and `MCP_AUTH_HEADER` for auth (e.g., `Authorization: Bearer …`).
  - `--dump-dir` writes fixtures (see below).

## How To Run (with uv)

- Minimal (localhost defaults):
```bash
uv run python examples/mcp_inspect_chemdrift.py \
  --timeout 5 --sse-read-timeout 5
```

- Explicit URL + auth header (inside firewall):
```bash
uv run python examples/mcp_inspect_chemdrift.py \
  --url "http://hopi36.pri.bms.com:7998/mcp/" \
  --header "Authorization: Bearer <token>" \
  --timeout 30 --sse-read-timeout 300
```

- Environment variables:
```bash
export MCP_URL="http://hopi36.pri.bms.com:7998/mcp/"
export MCP_AUTH_HEADER="Authorization: Bearer <token>"
export MCP_TIMEOUT=30
export MCP_SSE_READ_TIMEOUT=300
uv run python examples/mcp_inspect_chemdrift.py
```

- Generate fixtures:
```bash
uv run python examples/mcp_inspect_chemdrift.py \
  --timeout 5 --sse-read-timeout 5 \
  --dump-dir tests/fixtures/mcp
```

## Fixture Inventory (Generated)

Directory: `tests/fixtures/mcp`

- `initialize.server_info.json`
  - Source: `initialize().serverInfo`
  - Example content: `{ "name": "ChemServer", "title": null, "version": "1.13.0" }`

- `initialize.instructions.txt`
  - Source: `initialize().instructions`
  - Verbatim server instructions, plain text.

- `initialize.capabilities.json`
  - Source: `initialize().capabilities`
  - JSON: `tools`, `prompts`, `resources`, `experimental`, `logging`.

- `tools.json`
  - Source: `list_tools()`
  - Full tool descriptors (13 tools in this snapshot), including `inputSchema`, optional `outputSchema`, `annotations`, `meta`.

- `prompts.json`
  - Source: `list_prompts()`
  - Empty array on this server; still present for completeness.

- `resources.json`
  - Source: `list_resources()`
  - Empty array on this server; still present for completeness.

## Fixture Creation Notes

- Script: `examples/mcp_inspect_chemdrift.py`
- Command used to produce current fixtures:
```bash
uv run python examples/mcp_inspect_chemdrift.py \
  --timeout 5 --sse-read-timeout 5 \
  --dump-dir tests/fixtures/mcp
```
- Writes JSON with `ensure_ascii=False`, `indent=2`; instructions saved as `.txt` for readability.

## Constraints and Practical Notes

- Streamable HTTP is the chosen transport; SSE read timeout remains configurable and used by the SDK’s streaming reader.
- Firewall: provide internal base URL and headers via `--header` or `MCP_AUTH_HEADER`.
- Roots capability is server‑advertised; not present in this chemdrift snapshot.
- Some tools use an `outputSchema` wrapper (`x-fastmcp-wrap-result: true`); captured as‑is in `tools.json`.
- Prompts/Resources empty here; recorded to keep discovery parity and deterministic tests.

## Verification Checklist

- MCP SDK available (verified via `uv run`).
- Session lifecycle: `initialize()` once, then listings.
- Server info and capabilities recorded from `initialize`.
- Tool schemas recorded from `list_tools`.
- Optional subsystems recorded (prompts/resources), even if empty.
- Artifacts saved under `tests/fixtures/mcp` with stable filenames.

