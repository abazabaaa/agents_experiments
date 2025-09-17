"""Azure OpenAI Responses adapter with thread-safe offloading."""

from __future__ import annotations

import os
from typing import Any, Dict, List, Optional
import sys

import trio
from openai import AzureOpenAI
from trio import CapacityLimiter


class AzureResponses:
    """Thin wrapper around AzureOpenAI Responses that makes blocking calls
    Trio-friendly by offloading them to worker threads.
    """

    def __init__(self, model: str, *, thread_limiter: Optional[CapacityLimiter] = None) -> None:
        azure_endpoint = os.getenv("OPENAI_BASE_URL") or os.getenv("AZURE_OPENAI_ENDPOINT")
        api_key = (
            os.getenv("OPENAI_API_KEY")
            or os.getenv("AZURE_OPENAI_API_KEY")
            or os.getenv("AZURE_OPENAI_KEY")
        )
        if not azure_endpoint or not api_key:
            raise SystemExit(
                "Missing Azure OpenAI credentials. Set OPENAI_BASE_URL and OPENAI_API_KEY, "
                "or AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_API_KEY."
            )
        self._model = model
        self._limiter = thread_limiter
        self._client = AzureOpenAI(
            azure_endpoint=azure_endpoint,
            api_key=api_key,
            api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2025-03-01-preview"),
        )
        # Warn only once per instance if GPT-5 control kwargs are rejected by SDK/API
        self._controls_warning_emitted = False

    async def create(
        self,
        *,
        instructions: str,
        input_obj: Any,
        tools: Optional[List[Dict[str, Any]]] = None,
        previous_response_id: Optional[str] = None,
        max_output_tokens: int = 4000,
        # Optional GPT-5 controls
        text_verbosity: Optional[str] = None,  # low|medium|high
        reasoning_effort: Optional[str] = None,  # minimal|low|medium|high
        temperature: Optional[float] = None,
        top_p: Optional[float] = None,
    ) -> Any:
        """Offload a blocking `responses.create` to a worker thread.

        Parameters
        ----------
        instructions : str
        input_obj : Any
            Either a user prompt (str) or a list of `function_call_output` payloads.
        tools : Optional[List[Dict[str, Any]]]
        previous_response_id : Optional[str]
        max_output_tokens : int

        Returns
        -------
        Any
            The Responses API object.
        """

        def _do_call() -> Any:
            base_kwargs = dict(
                model=self._model,
                instructions=instructions,
                max_output_tokens=max_output_tokens,
                input=input_obj,
            )
            if tools is not None:
                base_kwargs["tools"] = tools
            if previous_response_id is not None:
                base_kwargs["previous_response_id"] = previous_response_id

            # Optional GPT-5 controls (best-effort; fallback if SDK doesn't support)
            control_kwargs: Dict[str, Any] = {}
            if text_verbosity in {"low", "medium", "high"}:
                control_kwargs["text"] = {"verbosity": text_verbosity}
            if reasoning_effort in {"minimal", "low", "medium", "high"}:
                control_kwargs["reasoning"] = {"effort": reasoning_effort}

            # For GPT-5 reasoning models, omit unsupported sampling params
            if not self._model.lower().startswith("gpt-5"):
                if temperature is not None:
                    control_kwargs["temperature"] = float(temperature)
                if top_p is not None:
                    control_kwargs["top_p"] = float(top_p)

            def try_call(kwargs: Dict[str, Any]) -> Any:
                return self._client.responses.create(**kwargs)

            # First attempt with controls (if any)
            kwargs = {**base_kwargs, **control_kwargs}
            try:
                return try_call(kwargs)
            except TypeError:
                # Retry without controls if SDK rejects unknown params
                if not self._controls_warning_emitted:
                    ctrl_names = [
                        k
                        for k in ("text", "reasoning", "temperature", "top_p")
                        if k in control_kwargs
                    ]
                    print(
                        "[warn] Responses.create rejected control parameters ("
                        + ", ".join(ctrl_names)
                        + ") — falling back without them."
                        + " This likely indicates an SDK or API version mismatch.",
                        file=sys.stderr,
                    )
                    self._controls_warning_emitted = True
                return try_call(base_kwargs)

        return await trio.to_thread.run_sync(_do_call, limiter=self._limiter)
