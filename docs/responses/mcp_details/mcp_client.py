"""MCP client adapter for asyncio-based MCP SDK integration."""

from __future__ import annotations

from typing import Any, Dict, Optional

from mcp.client.session import ClientSession
from mcp.client.streamable_http import streamablehttp_client
from mcp.types import CallToolResult


class MCPClient:
    """Owns the MCP session lifecycle and exposes a `call_tool` coroutine.

    This class is asyncio-native internally, but can be safely used from Trio
    because we run it under `trio_asyncio.open_loop()`.
    """

    def __init__(
        self, url: str, headers: Dict[str, str], timeout: float, sse_read_timeout: float
    ) -> None:
        self._url = url.rstrip("/") + "/"
        self._headers = headers
        self._timeout = timeout
        self._sse_read_timeout = sse_read_timeout

        self._stream_ctx = None
        self._session_ctx = None
        self.session: Optional[ClientSession] = None

    async def __aenter__(self) -> "MCPClient":
        self._stream_ctx = streamablehttp_client(
            url=self._url,
            headers=self._headers,
            timeout=self._timeout,
            sse_read_timeout=self._sse_read_timeout,
        )
        read_stream, write_stream, _get_session_id = await self._stream_ctx.__aenter__()
        self._session_ctx = ClientSession(read_stream, write_stream)
        self.session = await self._session_ctx.__aenter__()
        await self.session.initialize()  # fetch server info/instructions
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        try:
            if self._session_ctx is not None:
                await self._session_ctx.__aexit__(exc_type, exc, tb)
        finally:
            if self._stream_ctx is not None:
                await self._stream_ctx.__aexit__(exc_type, exc, tb)

    async def call_tool(self, name: str, arguments: Dict[str, Any]) -> CallToolResult:
        """Call an MCP tool and return its `CallToolResult`.

        Parameters
        ----------
        name : str
        arguments : Dict[str, Any]

        Returns
        -------
        CallToolResult
        """
        if not self.session:
            raise RuntimeError("MCP session not initialized")
        return await self.session.call_tool(name, arguments)
