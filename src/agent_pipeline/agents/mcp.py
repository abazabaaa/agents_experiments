"""Helpers for constructing MCP server instances."""

from __future__ import annotations

from typing import Any, Mapping, Sequence


def build_mcp_servers(_config: Mapping[str, Any] | None) -> Sequence[Any]:
    """Return instantiated MCP servers for the pipeline.

    The implementation will be expanded to parse configuration payloads and
    create the appropriate ``MCPServer`` objects.
    """

    return []
