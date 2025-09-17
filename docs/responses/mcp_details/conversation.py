"""Core conversation orchestration logic."""

from __future__ import annotations

import json
from typing import Any, Awaitable, Callable, Dict, List, Optional

import trio
from trio import TooSlowError

from ..adapters.azure_responses import AzureResponses
from ..adapters.mcp_client import MCPClient
from ..concurrency.mux import TrioMultiplexer
from ..domain import FunctionCallReq, MoleculeRunResult, ToolCallOutput
from ..utils.parsing import collect_function_calls, extract_final_text, stringify_call_tool_result
from ..utils.prompts import build_per_molecule_prompt, build_document_prompt
from ..config import ResolvedSettings


class ConversationRunner:
    """Runs one or more model conversations with MCP tools, using Trio for concurrency.

    - Each "loop" follows the model's lead: it issues function calls, we call MCP,
      and we return the outputs in the same order.
    - Per-turn tool calls are executed in parallel using TrioMultiplexer.

    This class is stateless across loops, so it can be reused concurrently.
    """

    def __init__(
        self,
        azure: AzureResponses,
        mcp: MCPClient,
        tools_spec: List[Dict[str, Any]],
        base_instructions: str,
        per_turn_concurrency: int,
        *,
        tool_timeout_s: float,
        turn_timeout_s: float,
        max_turns: int,
        empty_turns_to_proceed: int = 0,
    ) -> None:
        """Parameters
        ----------
        azure : AzureResponses
        mcp : MCPClient
        tools_spec : List[Dict[str, Any]]
            The MCP tool schemas to expose to the model.
        base_instructions : str
            Pre-amble including server instructions and tool listing.
        per_turn_concurrency : int
            Max concurrent MCP tool calls per turn.
        """
        self._azure = azure
        self._mcp = mcp
        self._tools = tools_spec
        self._instructions = base_instructions
        self._turn_mux = TrioMultiplexer(concurrency_cap=per_turn_concurrency, name="tools-turn")
        self._tool_timeout_s = tool_timeout_s
        self._turn_timeout_s = turn_timeout_s
        self._max_turns = max_turns
        self._empty_turns_to_proceed = max(0, int(empty_turns_to_proceed))

        # Verbosity now driven by config via pipeline (default False)
        self._verbose = False
        # Optional settings attached by pipeline
        self._settings: Optional[ResolvedSettings] = None

    async def _answer_with_tools(self, response: Any, *, tag: Optional[str] = None) -> Any:
        """Handle a single Responses turn:
        - collect function calls,
        - invoke MCP tools in parallel,
        - return a follow-up Responses call with outputs,
        - or return the original `response` if there were no calls.
        """
        calls = collect_function_calls(response)
        if self._verbose:
            if calls:
                names = ", ".join(f"{i}:{c.name}" for i, c in enumerate(calls))
                print(f"[{tag or ''} turn] collected {len(calls)} function_calls: {names}")
            else:
                print(f"[{tag or ''} turn] no function_calls; returning response")
        if not calls:
            return response

        # Build parallel callables; preserve order.
        def make_coro_fn(call: FunctionCallReq) -> Callable[[], Awaitable[ToolCallOutput]]:
            async def _do() -> ToolCallOutput:
                try:
                    if self._verbose:
                        print(
                            f"[tools] calling {call.name} with timeout {self._tool_timeout_s:.0f}s"
                        )
                    with trio.fail_after(self._tool_timeout_s):
                        result = await self._mcp.call_tool(call.name, call.arguments or {})
                    output = stringify_call_tool_result(result)
                except TooSlowError:
                    output = json.dumps(
                        {"error": f"tool '{call.name}' timed out", "timeout": True},
                        ensure_ascii=False,
                    )
                except Exception as e:
                    output = json.dumps({"error": str(e)}, ensure_ascii=False)
                return ToolCallOutput(call_id=call.call_id, output=output)

            return _do

        # Special-case: if multiple examine_molecule_tool calls exist and batch_examine_molecules is available,
        # perform a single batch call and split the results back to individual outputs.
        outputs: List[Optional[ToolCallOutput]] = [None] * len(calls)
        tool_names = {t.get("name") for t in self._tools}
        examine_indices = [i for i, c in enumerate(calls) if c.name == "examine_molecule_tool"]
        if len(examine_indices) >= 2 and "batch_examine_molecules" in tool_names:
            # Collect SMILES for batch
            smiles_list: List[str] = []
            ok = True
            for i in examine_indices:
                args = calls[i].arguments or {}
                smi = args.get("smiles")
                if not isinstance(smi, str):
                    ok = False
                    break
                smiles_list.append(smi)
            if ok:
                if self._verbose:
                    print(
                        f"[{tag or ''} turn] using batch_examine_molecules for {len(examine_indices)} fragments"
                    )
                try:
                    with trio.fail_after(self._tool_timeout_s):
                        batch_res = await self._mcp.call_tool(
                            "batch_examine_molecules", {"smiles_list": smiles_list}
                        )
                    # Try to split structured content
                    split_ok = False
                    try:
                        sc = batch_res.structuredContent
                        items = None
                        if isinstance(sc, list) and len(sc) == len(examine_indices):
                            items = sc
                        elif isinstance(sc, dict):
                            for key in ("results", "reports", "items"):
                                if isinstance(sc.get(key), list) and len(sc[key]) == len(
                                    examine_indices
                                ):
                                    items = sc[key]
                                    break
                        if items is not None:
                            for idx, item in zip(examine_indices, items):
                                outputs[idx] = ToolCallOutput(
                                    call_id=calls[idx].call_id,
                                    output=json.dumps(item, ensure_ascii=False),
                                )
                            split_ok = True
                    except Exception:
                        split_ok = False

                    if not split_ok:
                        # Fallback: stringify whole batch once for each; not ideal, but avoids failure.
                        out = stringify_call_tool_result(batch_res)
                        for idx in examine_indices:
                            outputs[idx] = ToolCallOutput(call_id=calls[idx].call_id, output=out)
                except TooSlowError:
                    out = json.dumps(
                        {"error": "batch_examine_molecules timed out", "timeout": True},
                        ensure_ascii=False,
                    )
                    for idx in examine_indices:
                        outputs[idx] = ToolCallOutput(call_id=calls[idx].call_id, output=out)
                except Exception as e:
                    # On failure, we'll just fall back to per-call for those indices
                    if self._verbose:
                        print(f"[{tag or ''} turn] batch_examine_molecules failed: {e}")

        # Build coroutine list for remaining calls
        remaining_fns: List[Callable[[], Awaitable[ToolCallOutput]]] = []
        remaining_positions: List[int] = []
        for i, c in enumerate(calls):
            if outputs[i] is None:
                remaining_fns.append(make_coro_fn(c))
                remaining_positions.append(i)

        if remaining_fns:
            rem_results = await self._turn_mux.run_ordered(remaining_fns)
            for pos, res in zip(remaining_positions, rem_results):
                outputs[pos] = res

        # No Nones expected now
        final_outputs: List[ToolCallOutput] = [o for o in outputs if o is not None]

        # Prepare `function_call_output` payloads in the same order as `calls`.
        fc_outputs = [
            {"type": "function_call_output", "call_id": out.call_id, "output": out.output}
            for out in final_outputs
        ]

        # Continue the conversation turn.
        if self._verbose:
            print(
                f"[{tag or ''} turn] sending {len(fc_outputs)} function_call_outputs; turn timeout {self._turn_timeout_s:.0f}s"
            )
        with trio.fail_after(self._turn_timeout_s):
            t0 = trio.current_time()
            s = self._settings
            next_resp = await self._azure.create(
                instructions=self._instructions,
                input_obj=fc_outputs,
                tools=self._tools,
                previous_response_id=response.id,
                max_output_tokens=(
                    s.max_output_tokens
                    if s and getattr(s, "max_output_tokens", None) is not None
                    else None
                ),
                text_verbosity=(s.text_verbosity if s and s.text_verbosity else None),
                reasoning_effort=(s.reasoning_effort if s and s.reasoning_effort else None),
                temperature=(s.temperature if s and s.temperature is not None else None),
                top_p=(s.top_p if s and s.top_p is not None else None),
            )
        if self._verbose:
            print(f"[{tag or ''} turn] model replied in {trio.current_time() - t0:.2f}s")
        return next_resp

    async def run_single_smiles_loop(
        self, smiles: str, *, tag: Optional[str] = None
    ) -> MoleculeRunResult:
        """Run the multi-turn conversation for a single SMILES:
          - Ask the model to examine, fragment a reasonable bond, then examine fragments.
          - Execute model-requested tools in parallel per turn.
          - Return the final model text.

        Parameters
        ----------
        smiles : str

        Returns
        -------
        MoleculeRunResult
        """
        # Build prompt exclusively from config template
        s = self._settings
        if not s:
            raise SystemExit("Effective settings missing on ConversationRunner")
        prompt = build_per_molecule_prompt(smiles, s)
        # Initial turn
        if self._verbose:
            print(f"[{tag or ''} init] requesting initial response")
        try:
            with trio.fail_after(self._turn_timeout_s):
                t0 = trio.current_time()
                s = self._settings
                response = await self._azure.create(
                    instructions=self._instructions,
                    input_obj=prompt,
                    tools=self._tools,
                    max_output_tokens=(
                        s.max_output_tokens
                        if s and getattr(s, "max_output_tokens", None) is not None
                        else None
                    ),
                    text_verbosity=(s.text_verbosity if s and s.text_verbosity else None),
                    reasoning_effort=(s.reasoning_effort if s and s.reasoning_effort else None),
                    temperature=(s.temperature if s and s.temperature is not None else None),
                    top_p=(s.top_p if s and s.top_p is not None else None),
                )
            if self._verbose:
                print(f"[{tag or ''} init] model replied in {trio.current_time() - t0:.2f}s")
        except TooSlowError:
            final = (
                "Initial model turn timed out before any tool calls. "
                f"Turn timeout={self._turn_timeout_s:.0f}s"
            )
            return MoleculeRunResult(smiles=smiles, final_text=final)

        # Keep answering turns while the model keeps asking for tool calls.
        turn_idx = 0
        empty_turns_seen = 0
        timed_out = False
        while True:
            if turn_idx >= self._max_turns:
                if self._verbose:
                    print(f"[{tag or ''} turn] max turns {self._max_turns} reached; stopping")
                break
            turn_idx += 1
            if self._verbose:
                print(f"[{tag or ''} turn] processing turn {turn_idx}")
            try:
                next_response = await self._answer_with_tools(response, tag=tag)
            except TooSlowError:
                timed_out = True
                if self._verbose:
                    print(f"[{tag or ''} turn] turn {turn_idx} timed out; stopping")
                break
            if next_response is response:
                # No function calls this turn. Optionally proceed for the first N empty turns
                if empty_turns_seen < self._empty_turns_to_proceed:
                    empty_turns_seen += 1
                    if self._verbose:
                        print(
                            f"[{tag or ''} turn] no function_calls; continuing (empty turn {empty_turns_seen}/{self._empty_turns_to_proceed})"
                        )
                    try:
                        with trio.fail_after(self._turn_timeout_s):
                            t1 = trio.current_time()
                            s = self._settings
                            # Continue the conversation with an empty output list
                            next_response = await self._azure.create(
                                instructions=self._instructions,
                                input_obj=[],
                                tools=self._tools,
                                previous_response_id=response.id,
                                max_output_tokens=(
                                    s.max_output_tokens
                                    if s and getattr(s, "max_output_tokens", None) is not None
                                    else None
                                ),
                                text_verbosity=(
                                    s.text_verbosity if s and s.text_verbosity else None
                                ),
                                reasoning_effort=(
                                    s.reasoning_effort if s and s.reasoning_effort else None
                                ),
                                temperature=(
                                    s.temperature if s and s.temperature is not None else None
                                ),
                                top_p=(s.top_p if s and s.top_p is not None else None),
                            )
                        if self._verbose:
                            print(
                                f"[{tag or ''} turn] continued after empty turn in {trio.current_time() - t1:.2f}s"
                            )
                    except TooSlowError:
                        timed_out = True
                        if self._verbose:
                            print(f"[{tag or ''} turn] empty-turn continuation timed out; stopping")
                        break
                else:
                    # Stop as usual if we've exhausted allowed empty turns
                    break
            response = next_response

        final_text = extract_final_text(response)
        notes: List[str] = []
        if turn_idx >= self._max_turns:
            notes.append(
                f"[Note] Stopped after {self._max_turns} turns to prevent infinite tool loop."
            )
        if timed_out:
            notes.append(f"[Note] Stopped due to turn timeout of {self._turn_timeout_s:.0f}s.")
        if notes:
            final_text = (final_text + "\n\n" + "\n".join(notes)).strip()

        return MoleculeRunResult(smiles=smiles, final_text=final_text)

    async def run_single_document_loop(
        self, content: str, *, label: str, tag: Optional[str] = None
    ) -> MoleculeRunResult:
        """Run the multi-turn conversation for a single document content.

        Parameters
        ----------
        content : str
            The markdown/plaintext content of the document.
        label : str
            A short label for display (e.g., filename).
        """
        s = self._settings
        if not s:
            raise SystemExit("Effective settings missing on ConversationRunner")
        prompt = build_document_prompt(content, s)
        if self._verbose:
            print(f"[{tag or ''} init] requesting initial response")
        try:
            with trio.fail_after(self._turn_timeout_s):
                t0 = trio.current_time()
                s = self._settings
                response = await self._azure.create(
                    instructions=self._instructions,
                    input_obj=prompt,
                    tools=self._tools,
                    max_output_tokens=(
                        s.max_output_tokens
                        if s and getattr(s, "max_output_tokens", None) is not None
                        else None
                    ),
                    text_verbosity=(s.text_verbosity if s and s.text_verbosity else None),
                    reasoning_effort=(s.reasoning_effort if s and s.reasoning_effort else None),
                    temperature=(s.temperature if s and s.temperature is not None else None),
                    top_p=(s.top_p if s and s.top_p is not None else None),
                )
            if self._verbose:
                print(f"[{tag or ''} init] model replied in {trio.current_time() - t0:.2f}s")
        except TooSlowError:
            final = (
                "Initial model turn timed out before any tool calls. "
                f"Turn timeout={self._turn_timeout_s:.0f}s"
            )
            return MoleculeRunResult(smiles=label, final_text=final)

        turn_idx = 0
        empty_turns_seen = 0
        timed_out = False
        while True:
            if turn_idx >= self._max_turns:
                if self._verbose:
                    print(f"[{tag or ''} turn] max turns {self._max_turns} reached; stopping")
                break
            turn_idx += 1
            if self._verbose:
                print(f"[{tag or ''} turn] processing turn {turn_idx}")
            try:
                next_response = await self._answer_with_tools(response, tag=tag)
            except TooSlowError:
                timed_out = True
                if self._verbose:
                    print(f"[{tag or ''} turn] turn {turn_idx} timed out; stopping")
                break
            if next_response is response:
                # No function calls this turn. Optionally proceed for the first N empty turns
                if empty_turns_seen < self._empty_turns_to_proceed:
                    empty_turns_seen += 1
                    if self._verbose:
                        print(
                            f"[{tag or ''} turn] no function_calls; continuing (empty turn {empty_turns_seen}/{self._empty_turns_to_proceed})"
                        )
                    try:
                        with trio.fail_after(self._turn_timeout_s):
                            t1 = trio.current_time()
                            s = self._settings
                            next_response = await self._azure.create(
                                instructions=self._instructions,
                                input_obj=[],
                                tools=self._tools,
                                previous_response_id=response.id,
                                max_output_tokens=(
                                    s.max_output_tokens
                                    if s and getattr(s, "max_output_tokens", None) is not None
                                    else None
                                ),
                                text_verbosity=(
                                    s.text_verbosity if s and s.text_verbosity else None
                                ),
                                reasoning_effort=(
                                    s.reasoning_effort if s and s.reasoning_effort else None
                                ),
                                temperature=(
                                    s.temperature if s and s.temperature is not None else None
                                ),
                                top_p=(s.top_p if s and s.top_p is not None else None),
                            )
                        if self._verbose:
                            print(
                                f"[{tag or ''} turn] continued after empty turn in {trio.current_time() - t1:.2f}s"
                            )
                    except TooSlowError:
                        timed_out = True
                        if self._verbose:
                            print(f"[{tag or ''} turn] empty-turn continuation timed out; stopping")
                        break
                else:
                    break
            response = next_response

        final_text = extract_final_text(response)
        notes: List[str] = []
        if turn_idx >= self._max_turns:
            notes.append(
                f"[Note] Stopped after {self._max_turns} turns to prevent infinite tool loop."
            )
        if timed_out:
            notes.append(f"[Note] Stopped due to turn timeout of {self._turn_timeout_s:.0f}s.")
        if notes:
            final_text = (final_text + "\n\n" + "\n".join(notes)).strip()

        return MoleculeRunResult(smiles=label, final_text=final_text)
