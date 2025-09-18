"""Main pipeline orchestration for concurrent SMILES processing."""

from __future__ import annotations

import os
from collections.abc import Awaitable, Callable
from typing import Any

import trio
import trio_asyncio
from trio import CapacityLimiter

from ..adapters.azure_responses import AzureResponses
from ..adapters.mcp_client import MCPClient
from ..adapters.tool_schema import build_tools_and_instructions
from ..concurrency.mux import TrioMultiplexer
from ..config import DEFAULTS, EffectiveSettings
from ..domain import MoleculeRunResult
from ..utils.parsing import extract_final_text
from ..utils.prompts import build_final_instructions, build_final_summary_prompt
from .conversation import ConversationRunner

# Expose the active Azure client instance for tests that monkeypatch this module.
# This is assigned inside run_pipeline when the client is constructed.
azure: Any = None


def _noop() -> None:
    return None


async def run_pipeline(
    model: str,
    mcp_url: str,
    smiles_list: list[str] | None = None,
    *,
    settings: EffectiveSettings | None = None,
) -> None:
    """Entry point run under Trio. Establishes an asyncio-backed MCP loop via trio-asyncio,
    sets up Azure Responses, and fans out 5 SMILES loops concurrently.

    At the end, sends a final 'summary-of-summaries' query to the model.

    Parameters
    ----------
    model : str
        Azure OpenAI model name
    mcp_url : str
        MCP server URL
    smiles_list : Optional[List[str]]
        List of SMILES strings to process (required)
    """
    # Fail fast if no SMILES were provided
    if not smiles_list:
        raise SystemExit("No SMILES provided. Pass one or more via --smiles.")

    # Effective settings are required for prompt construction and behavior.
    if settings is None:
        raise SystemExit(
            "Effective settings are required. Call resolve_settings(...) and pass 'settings'."
        )

    # Azure client (sync → threads); optional thread limiter
    thread_limiter: CapacityLimiter | None = None
    if getattr(settings, "thread_limit", None):
        try:
            tokens = int(settings.thread_limit)  # type: ignore[arg-type]
            if tokens > 0:
                thread_limiter = CapacityLimiter(tokens)
        except Exception:
            thread_limiter = None
    # Allow behavior override for model via settings
    effective_model = settings.model if settings.model else model
    client = AzureResponses(model=effective_model, thread_limiter=thread_limiter)
    # Make the client accessible via module attribute for tests
    global azure
    azure = client

    # MCP connection (asyncio under trio-asyncio)
    # Headers come only from config settings now
    headers: dict[str, str] = settings.mcp_headers

    url = settings.mcp_url.rstrip("/") + "/"
    timeout = settings.mcp_timeout_s if settings else DEFAULTS.mcp_timeout_s
    sse_read_timeout = (
        settings.mcp_sse_read_timeout_s if settings else DEFAULTS.mcp_sse_read_timeout_s
    )

    async with trio_asyncio.open_loop():
        async with MCPClient(
            url=url, headers=headers, timeout=timeout, sse_read_timeout=sse_read_timeout
        ) as mcp:
            if not mcp.session:
                raise RuntimeError("MCP session not available")

            tools_spec, instructions = await build_tools_and_instructions(
                mcp.session,
                extra_instructions=(
                    settings.developer_base_instructions if settings else None
                ),
            )

            # Timeouts and caps from env
            tool_timeout_s = (
                settings.tool_timeout_s if settings else DEFAULTS.tool_timeout_s
            )
            turn_timeout_s = (
                settings.turn_timeout_s if settings else DEFAULTS.turn_timeout_s
            )
            max_turns = settings.max_turns if settings else DEFAULTS.max_turns

            eff_ptc = (
                settings.per_turn_concurrency
                if settings
                else DEFAULTS.per_turn_concurrency
            )
            runner = ConversationRunner(
                azure=client,
                mcp=mcp,
                tools_spec=tools_spec,
                base_instructions=instructions,
                per_turn_concurrency=eff_ptc,
                tool_timeout_s=tool_timeout_s,
                turn_timeout_s=turn_timeout_s,
                max_turns=max_turns,
                empty_turns_to_proceed=(
                    settings.empty_turns_to_proceed
                    if settings
                    else DEFAULTS.empty_turns_to_proceed
                ),
            )
            # Propagate verbosity to runner and mux
            runner._verbose = bool(getattr(settings, "verbose", False))
            # Attach settings to runner for downstream calls
            runner._settings = settings  # type: ignore[attr-defined]

            # Fan out 5 loops concurrently
            eff_fanout = (
                settings.fanout_concurrency if settings else DEFAULTS.fanout_concurrency
            )
            mux = TrioMultiplexer(
                concurrency_cap=eff_fanout,
                name="smiles-fanout",
                verbose=bool(getattr(settings, "verbose", False)),
            )
            fanout_t0 = trio.current_time()
            coro_fns: list[Callable[[], Awaitable[MoleculeRunResult]]] = []
            for i, sm in enumerate(smiles_list):
                tag = f"mol-{i + 1}"

                async def make_fn(smiles=sm, tag=tag) -> MoleculeRunResult:  # capture
                    return await runner.run_single_smiles_loop(smiles, tag=tag)

                coro_fns.append(lambda fn=make_fn: fn())
            results: list[MoleculeRunResult] = await mux.run_ordered(coro_fns)
            fanout_total = trio.current_time() - fanout_t0
            if bool(getattr(settings, "verbose", False)):
                print(f"[fanout] completed {len(results)} loops in {fanout_total:.2f}s")

            # Prepare a final summary query to the model
            # Build final prompt from config template with {{count}}
            final_prompt = build_final_summary_prompt(results, settings)

            # Choose developer/system instructions for final summary (supports {{count}})
            final_instructions = build_final_instructions(
                len(results), settings, default_instructions=instructions
            )

            # Final summary must never call tools: enforce tools=None
            final_tools = None

            # Prefer final-summary-specific max tokens if provided
            eff_max_tokens = (
                settings.final_summary_max_output_tokens
                if settings and settings.final_summary_max_output_tokens
                else (
                    settings.max_output_tokens
                    if settings
                    else DEFAULTS.max_output_tokens
                )
            )
            final_resp = await client.create(
                instructions=final_instructions,
                input_obj=final_prompt,
                tools=final_tools,
                max_output_tokens=eff_max_tokens,
                text_verbosity=(settings.text_verbosity if settings else None),
                reasoning_effort=(
                    settings.final_summary_reasoning_effort
                    if settings and settings.final_summary_reasoning_effort
                    else (settings.reasoning_effort if settings else None)
                ),
                temperature=(settings.temperature if settings else None),
                top_p=(settings.top_p if settings else None),
            )

            # Render output
            print("\n" + "=" * 80)
            print("PER-MOLECULE REPORTS")
            print("=" * 80)
            for res in results:
                print(f"\n# {res.smiles}\n")
                print(res.final_text.strip())
                print("\n" + "-" * 80)

            print("\n" + "=" * 80)
            print("FINAL SUMMARY OF ALL MOLECULES")
            print("=" * 80)
            print(extract_final_text(final_resp).strip())
            print()


async def run_pipeline_documents(
    model: str,
    mcp_url: str,
    documents: list[tuple[str, str]] | None = None,
    *,
    settings: EffectiveSettings | None = None,
) -> None:
    """Pipeline variant for analyzing document contents.

    Parameters
    ----------
    model : str
        Azure OpenAI model name
    mcp_url : str
        MCP server URL
    documents : Optional[List[Tuple[str, str]]]
        List of (path, content) tuples to process (required)
    """
    if not documents:
        raise SystemExit(
            "No documents provided. Pass one or more via --docs/--docs-dir."
        )
    if settings is None:
        raise SystemExit(
            "Effective settings are required. Call resolve_settings(...) and pass 'settings'."
        )

    thread_limiter: CapacityLimiter | None = None
    if getattr(settings, "thread_limit", None):
        try:
            tokens = int(settings.thread_limit)  # type: ignore[arg-type]
            if tokens > 0:
                thread_limiter = CapacityLimiter(tokens)
        except Exception:
            thread_limiter = None
    effective_model = settings.model if settings.model else model
    client = AzureResponses(model=effective_model, thread_limiter=thread_limiter)
    global azure
    azure = client

    headers: dict[str, str] = settings.mcp_headers
    url = settings.mcp_url.rstrip("/") + "/"
    timeout = settings.mcp_timeout_s if settings else DEFAULTS.mcp_timeout_s
    sse_read_timeout = (
        settings.mcp_sse_read_timeout_s if settings else DEFAULTS.mcp_sse_read_timeout_s
    )

    async with trio_asyncio.open_loop():
        async with MCPClient(
            url=url, headers=headers, timeout=timeout, sse_read_timeout=sse_read_timeout
        ) as mcp:
            if not mcp.session:
                raise RuntimeError("MCP session not available")

            tools_spec, instructions = await build_tools_and_instructions(
                mcp.session,
                extra_instructions=(
                    settings.developer_base_instructions if settings else None
                ),
            )

            tool_timeout_s = (
                settings.tool_timeout_s if settings else DEFAULTS.tool_timeout_s
            )
            turn_timeout_s = (
                settings.turn_timeout_s if settings else DEFAULTS.turn_timeout_s
            )
            max_turns = settings.max_turns if settings else DEFAULTS.max_turns

            eff_ptc = (
                settings.per_turn_concurrency
                if settings
                else DEFAULTS.per_turn_concurrency
            )
            runner = ConversationRunner(
                azure=client,
                mcp=mcp,
                tools_spec=tools_spec,
                base_instructions=instructions,
                per_turn_concurrency=eff_ptc,
                tool_timeout_s=tool_timeout_s,
                turn_timeout_s=turn_timeout_s,
                max_turns=max_turns,
                empty_turns_to_proceed=(
                    settings.empty_turns_to_proceed
                    if settings
                    else DEFAULTS.empty_turns_to_proceed
                ),
            )
            runner._verbose = bool(getattr(settings, "verbose", False))
            runner._settings = settings  # type: ignore[attr-defined]

            eff_fanout = (
                settings.fanout_concurrency if settings else DEFAULTS.fanout_concurrency
            )
            mux = TrioMultiplexer(
                concurrency_cap=eff_fanout,
                name="docs-fanout",
                verbose=bool(getattr(settings, "verbose", False)),
            )
            fanout_t0 = trio.current_time()
            coro_fns: list[Callable[[], Awaitable[MoleculeRunResult]]] = []
            for i, (path, content) in enumerate(documents):
                label = path.split("/")[-1] if "/" in path else path.split(os.sep)[-1]
                tag = f"doc-{i + 1}"

                async def make_fn(
                    content=content, label=label, tag=tag
                ) -> MoleculeRunResult:  # capture
                    return await runner.run_single_document_loop(
                        content, label=label, tag=tag
                    )

                coro_fns.append(lambda fn=make_fn: fn())
            results: list[MoleculeRunResult] = await mux.run_ordered(coro_fns)
            fanout_total = trio.current_time() - fanout_t0
            if bool(getattr(settings, "verbose", False)):
                print(f"[fanout] completed {len(results)} loops in {fanout_total:.2f}s")

            final_prompt = build_final_summary_prompt(results, settings)
            final_instructions = build_final_instructions(
                len(results), settings, default_instructions=instructions
            )
            # Final summary must never call tools: enforce tools=None
            final_tools = None
            eff_max_tokens = (
                settings.final_summary_max_output_tokens
                if settings and settings.final_summary_max_output_tokens
                else (
                    settings.max_output_tokens
                    if settings
                    else DEFAULTS.max_output_tokens
                )
            )
            final_resp = await client.create(
                instructions=final_instructions,
                input_obj=final_prompt,
                tools=final_tools,
                max_output_tokens=eff_max_tokens,
                text_verbosity=(settings.text_verbosity if settings else None),
                reasoning_effort=(
                    settings.final_summary_reasoning_effort
                    if settings and settings.final_summary_reasoning_effort
                    else (settings.reasoning_effort if settings else None)
                ),
                temperature=(settings.temperature if settings else None),
                top_p=(settings.top_p if settings else None),
            )

            print("\n" + "=" * 80)
            print("PER-DOCUMENT REPORTS")
            print("=" * 80)
            for res in results:
                print(f"\n# {res.smiles}\n")
                print(res.final_text.strip())
                print("\n" + "-" * 80)

            print("\n" + "=" * 80)
            print("FINAL SUMMARY OF ALL DOCUMENTS")
            print("=" * 80)
            print(extract_final_text(final_resp).strip())
            print()
