"""Protocol interfaces for external system adapters."""

from __future__ import annotations

from typing import Any, Dict, List, Optional, Protocol, Tuple


class LLMClient(Protocol):
    """Protocol for language model clients."""

    async def create(
        self,
        *,
        instructions: str,
        input_obj: Any,
        tools: Optional[List[Dict[str, Any]]] = None,
        previous_response_id: Optional[str] = None,
        max_output_tokens: int = 4000,
    ) -> Any:
        """Create a new model response."""
        ...


class ToolExecutor(Protocol):
    """Protocol for tool execution systems."""

    async def call_tool(self, name: str, arguments: Dict[str, Any]) -> Any:
        """Execute a tool with given name and arguments."""
        ...


class ToolSchemaProvider(Protocol):
    """Protocol for providing tool schemas and instructions."""

    async def get_tools_and_instructions(self) -> Tuple[List[Dict[str, Any]], str]:
        """Get available tools and server instructions."""
        ...
