"""Tool schema discovery and instruction building for MCP servers."""

from __future__ import annotations

from typing import Any, Dict, List, Optional, Tuple

from mcp.client.session import ClientSession


async def build_tools_and_instructions(
    session: ClientSession, *, extra_instructions: Optional[str] = None
) -> Tuple[List[Dict[str, Any]], str]:
    """Query the MCP server for tools and server instructions; build a neat
    preamble/instructions string and a list of `tools` suitable for Responses API.

    Parameters
    ----------
    session : ClientSession

    Returns
    -------
    (tools_spec, instructions): (List[Dict[str, Any]], str)
    """
    # Tools
    tools_result = await session.list_tools()
    tools = list(tools_result.tools)

    fn_tools: List[Dict[str, Any]] = []
    for t in tools:
        name = t.name
        desc = t.description or ""
        title = getattr(t, "title", None)
        params = t.inputSchema or {"type": "object", "properties": {}}
        if not isinstance(params, dict):
            params = {"type": "object", "properties": {}, "additionalProperties": True}

        parts: List[str] = []
        if title and (not desc or title.strip() != desc.strip()):
            parts.append(str(title))
        if desc:
            parts.append(str(desc))
        description_text = " — ".join([p for p in parts if p])

        fn_tools.append(
            {
                "type": "function",
                "name": name,
                "description": description_text or desc,
                "parameters": params,
            }
        )

    # Instructions
    init = await session.initialize()
    server_info = init.serverInfo
    server_instructions = getattr(init, "instructions", "") or ""

    lines: List[str] = []
    sname = getattr(server_info, "name", None) or "MCP Server"
    sver = getattr(server_info, "version", None) or ""
    lines.append(f"You are connected to {sname}{(' v' + sver) if sver else ''}.")

    if server_instructions:
        lines.append(server_instructions)

    lines.append("You have access to the following MCP tools:")
    for t in fn_tools:
        # One-line descriptions are plenty
        desc = (t.get("description", "") or "").splitlines()[0]
        lines.append(f"- {t['name']}: {desc}")

    # Note: Any further guidance should come from config's base_instructions.

    instructions = "\n\n".join(lines)

    # Append any caller-provided developer instructions
    if extra_instructions:
        extra = extra_instructions.strip()
        if extra:
            instructions = instructions + "\n\n" + extra

    # Verbose listing for debugging
    # Verbose print removed; use caller-controlled logging if needed

    return fn_tools, instructions
