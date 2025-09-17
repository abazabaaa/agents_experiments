"""Utilities for parsing Azure Responses and MCP tool results."""

from __future__ import annotations

import json
from typing import Any, List

from mcp.types import CallToolResult, TextContent

from ..domain import FunctionCallReq


def collect_function_calls(resp: Any) -> List[FunctionCallReq]:
    """Extract model-issued function calls from an Azure Responses `resp` object.

    Parameters
    ----------
    resp : Any
        Azure Responses response object.

    Returns
    -------
    List[FunctionCallReq]
        Ordered by appearance – this order must be preserved in outputs.
    """
    calls: List[FunctionCallReq] = []
    output = getattr(resp, "output", []) or []
    for item in output:
        if getattr(item, "type", None) == "function_call":
            name = getattr(item, "name", None)
            call_id = getattr(item, "call_id", None) or getattr(item, "id", None)
            args = getattr(item, "arguments", None)
            if isinstance(args, str):
                try:
                    arguments = json.loads(args) if args else {}
                except Exception:
                    arguments = {}
            else:
                arguments = args or {}
            if name and call_id:
                calls.append(FunctionCallReq(name=name, call_id=call_id, arguments=arguments))
    return calls


def extract_final_text(resp: Any) -> str:
    """Extract final text from an Azure Responses response object.

    Parameters
    ----------
    resp : Any

    Returns
    -------
    str
    """
    text = getattr(resp, "output_text", None)
    if text:
        return text
    # Fallback: scan output parts
    chunks: List[str] = []
    for item in getattr(resp, "output", []) or []:
        for part in getattr(item, "content", []) or []:
            if getattr(part, "type", None) == "output_text" and getattr(part, "text", None):
                chunks.append(part.text)
    return "".join(chunks).strip()


def stringify_call_tool_result(result: CallToolResult) -> str:
    """Convert MCP CallToolResult into a string payload suitable for function_call_output.

    Preference order:
      - structuredContent (JSON)
      - textual content concatenation
      - full model dump as JSON
    """
    try:
        if result.structuredContent is not None:
            return json.dumps(result.structuredContent, ensure_ascii=False)

        texts: List[str] = []
        for item in result.content or []:
            if isinstance(item, TextContent) and item.text:
                texts.append(item.text)
        if texts:
            return "\n".join(texts)

        return json.dumps(result.model_dump(mode="json"), ensure_ascii=False)
    except Exception:
        return json.dumps(result.model_dump(mode="json"), ensure_ascii=False)
