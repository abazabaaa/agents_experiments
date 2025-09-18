diff --git a/configs/agent_pipeline_optimized.json b/configs/agent_pipeline_optimized.json
index 99c7dfeb2241e2817048d2acf3caa7312ffcb830..5ed831a36a8a5fcef4ead72061291b167b68af6f 100644
--- a/configs/agent_pipeline_optimized.json
+++ b/configs/agent_pipeline_optimized.json
@@ -1,45 +1,53 @@
 {
   "logging": {
     "log_file": "logs/agent_pipeline.log",
     "trace_workflow_name": "lark-doc-cleaning-pipeline",
     "trace_metadata": {
       "project": "firecrawl-lark-doc-cleaning",
       "version": "2.0-optimized"
     }
   },
   "io": {
     "input_artifact": "artifacts/lark_docs.json",
     "output_directory": "artifacts/cleaned_docs"
   },
   "concurrency": {
     "router_pool": 4,
     "markdown_pool": 6,
     "notebook_pool": 3,
     "review_pool": 2,
     "naming_pool": 2,
-    "channel_buffer": 20
+    "channel_buffer": 20,
+    "buffers": {
+      "router": 5,
+      "markdown": 10,
+      "notebook": 5,
+      "review": 2,
+      "naming": 1,
+      "write": 0
+    }
   },
   "retry": {
     "max_attempts": 3,
     "initial_delay": 2.0,
     "backoff_multiplier": 2.0,
     "max_delay": 30.0,
     "jitter_ratio": 0.5
   },
   "agents": {
     "router": {
       "name": "DocumentRouter",
       "instructions": "TASK: Classify document as markdown OR notebook.\n\nDECISION TREE:\nCheck content structure:\n├── Contains ```python cells or {\"cells\": [ → route=notebook\n├── Contains .ipynb JSON structure → route=notebook\n├── Contains Jupyter magic commands (%%, !) → route=notebook\n├── Contains EBNF grammar rules (lowercase: pattern) → route=markdown\n├── Contains TERMINALS (UPPERCASE: /regex/) → route=markdown\n├── Contains Lark directives (%import, %ignore) → route=markdown\n└── Default markdown prose → route=markdown\n\nOUTPUT: route=markdown OR route=notebook\nKEEP EXPLANATION UNDER 10 WORDS.",
       "model": "gpt-5-nano",
       "reasoning_effort": "minimal",
       "verbosity": "low",
       "timeout": 180.0,
       "max_tokens": 4096
     },
     "markdown_cleaner": {
       "name": "MarkdownPolisher",
       "instructions": "You are cleaning Lark parser documentation. Lark is a parsing library that uses EBNF grammar syntax.\n\nKEY LARK SYNTAX TO PRESERVE:\n- Grammar rules (lowercase): rule_name: expression | alternative\n- Terminals (UPPERCASE): TERM_NAME: \"literal\" | /regex/flags\n- Comments: // or # style\n- Operators: | + * ? ~ (preserve exactly)\n- Directives: %import, %ignore, %extend, %override\n- Templates: name{params}: expression\n- String literals and regex patterns must remain exact\n\nCLEANING TASKS:\n1. Format markdown with consistent heading levels (# ## ###)\n2. Preserve ALL code blocks with correct ```language tags\n3. Keep EBNF grammar blocks as ```ebnf or ```lark\n4. Maintain Python code blocks as ```python\n5. Fix broken tables while preserving technical content\n6. Add descriptive front-matter (title, description, source_url)\n7. Remove duplicate navigation but keep technical cross-references\n8. Ensure special characters in grammar (|, ?, *, +, ~) are properly escaped outside code blocks\n\nIMPORTANT: Lark grammars are precision syntax - even minor changes break parsers. Preserve ALL grammar examples exactly as written.\n\nIf review_feedback provided, address it specifically.",
       "model": "gpt-5",
       "reasoning_effort": "medium",
       "verbosity": "medium",
       "timeout": 180.0,
diff --git a/examples/agent_clean_pipeline.py b/examples/agent_clean_pipeline.py
index 44155526c3206f96c288efd7ac5d3c9a27ca5b2a..5a8a8ad024d6b73b1b154861d84110092d9ecfe4 100644
--- a/examples/agent_clean_pipeline.py
+++ b/examples/agent_clean_pipeline.py
@@ -1,116 +1,134 @@
 #!/usr/bin/env python3
 """Concurrent document cleaning pipeline using OpenAI Agents and Trio."""
 
 from __future__ import annotations
 
 import argparse
+import contextvars
 import json
 import logging
 import os
 import random
 import re
 import sys
 import threading
 import traceback
 import unicodedata
-from collections.abc import Awaitable, Callable, Iterable
+from collections.abc import Awaitable, Callable, Iterable, Sequence
 from dataclasses import dataclass, field
 from pathlib import Path
-from typing import Any, Literal
+from typing import Any, Literal, cast
 
 import httpx
 import trio_asyncio
 from agents import Agent, Runner, set_default_openai_client
 from agents.items import ItemHelpers
 from agents.lifecycle import RunHooks
 from agents.model_settings import ModelSettings
 from agents.run import RunConfig
 from agents.run_context import RunContextWrapper
 from openai import AsyncOpenAI
 from openai.types.shared import Reasoning
 from pydantic import BaseModel, Field
 
 import trio
 from trio.lowlevel import current_task
 
 AGENT_THREAD_LIMIT = 10
 DEFAULT_AGENT_TIMEOUT = 300.0
 LARGE_DOCUMENT_THRESHOLD = 1_000_000
 CHANNEL_PRESSURE_FRACTION = 0.8
 CHANNEL_MONITOR_INTERVAL = 10.0
 
 AGENT_THREAD_LIMITER = trio.CapacityLimiter(AGENT_THREAD_LIMIT)
+MODEL_LIMITER_DEFAULTS: dict[str, int] = {
+    "gpt-5": 4,
+    "gpt-5-mini": 8,
+    "gpt-5-nano": 12,
+}
+MODEL_LIMITERS: dict[str, trio.CapacityLimiter] = {
+    name: trio.CapacityLimiter(limit)
+    for name, limit in MODEL_LIMITER_DEFAULTS.items()
+}
+TRACE_ID_VAR = cast(
+    contextvars.ContextVar[str | None],
+    contextvars.ContextVar("trace_id", default=None),
+)
 
 
 # ---------------------------------------------------------------------------
 # Structured logging + lifecycle hooks (adapted from trio_agents_firecrawl)
 
 
 class StructuredLogger:
     """Thread-safe logger that mirrors console output to a verbose log file."""
 
     def __init__(self, *, quiet: bool, verbose_path: Path) -> None:
         self.quiet = quiet
         self.verbose_path = verbose_path
         self._lock = threading.Lock()
         self._attached_logger_names: set[str] = set()
         verbose_path.parent.mkdir(parents=True, exist_ok=True)
         verbose_path.write_text("", encoding="utf-8")
 
     def info(self, message: str, *, spacer: bool = False) -> None:
         formatted = message.rstrip()
         if not self.quiet:
             if spacer:
                 print()
             print(formatted)
         self._write_verbose(formatted)
 
     def blank_line(self) -> None:
         if not self.quiet:
             print()
         self._write_verbose("")
 
     def verbose(self, message: str) -> None:
         self._write_verbose(message.rstrip())
 
     def attach_python_logger(self, name: str, level: int = logging.INFO) -> None:
         if name in self._attached_logger_names:
             return
         handler = _StructuredLoggingHandler(self)
         handler.setLevel(level)
         handler.setFormatter(logging.Formatter("%(levelname)s %(name)s: %(message)s"))
         py_logger = logging.getLogger(name)
         py_logger.addHandler(handler)
         py_logger.setLevel(level)
         py_logger.propagate = False
         self._attached_logger_names.add(name)
 
     def _write_verbose(self, message: str) -> None:
+        trace_id = TRACE_ID_VAR.get()
+        formatted = message.rstrip("\n")
+        if trace_id and not formatted.startswith("trace="):
+            formatted = f"trace={trace_id} {formatted}"
         with self._lock:
             with self.verbose_path.open("a", encoding="utf-8") as stream:
-                stream.write(message.rstrip("\n") + "\n")
+                stream.write(formatted + "\n")
 
 
 class _StructuredLoggingHandler(logging.Handler):
     def __init__(self, structured_logger: StructuredLogger) -> None:
         super().__init__()
         self._structured_logger = structured_logger
 
     def emit(
         self, record: logging.LogRecord
     ) -> None:  # pragma: no cover - logging bridge
         try:
             message = self.format(record)
         except Exception:  # noqa: BLE001
             message = record.getMessage()
         self._structured_logger.verbose(
             f"SDK_LOG level={record.levelname} logger={record.name} message={message}"
         )
 
 
 class AgentCallContext:
     """Context passed through Agents SDK runs to enrich telemetry."""
 
     def __init__(
         self,
         logger: StructuredLogger,
@@ -309,91 +327,112 @@ class AgentSpec:
     max_tokens: int | None
 
 
 @dataclass
 class RetryPolicy:
     max_attempts: int
     initial_delay: float
     backoff_multiplier: float
     max_delay: float
     jitter_ratio: float
 
 
 @dataclass
 class PipelineConfig:
     log_file: Path
     workflow_name: str
     trace_metadata: dict[str, Any]
     input_artifact: Path
     output_directory: Path
     router_pool: int
     markdown_pool: int
     notebook_pool: int
     review_pool: int
     naming_pool: int
     channel_buffer: int
+    router_buffer: int
+    markdown_buffer: int
+    notebook_buffer: int
+    review_buffer: int
+    naming_buffer: int
+    write_buffer: int
     max_attempts: int
     retry_policy: RetryPolicy
     agent_specs: dict[str, AgentSpec]
 
     @classmethod
     def from_json(cls, path: Path) -> PipelineConfig:
         payload = json.loads(path.read_text(encoding="utf-8"))
         logging_cfg = payload.get("logging", {})
         concurrency_cfg = payload.get("concurrency", {})
         retry_cfg = payload.get("retry", {})
         io_cfg = payload.get("io", {})
+        buffers_cfg = concurrency_cfg.get("buffers") or {}
 
         agents_cfg = payload.get("agents", {})
         agent_specs: dict[str, AgentSpec] = {}
         for key, spec in agents_cfg.items():
             agent_specs[key] = AgentSpec(
                 name=spec["name"],
                 instructions=spec["instructions"],
                 model=spec["model"],
                 reasoning_effort=spec.get("reasoning_effort"),
                 verbosity=spec.get("verbosity"),
                 timeout=spec.get("timeout"),
                 max_tokens=spec.get("max_tokens"),
             )
 
+        default_buffer = int(concurrency_cfg.get("channel_buffer", 10))
+        router_buffer = int(buffers_cfg.get("router", default_buffer))
+        markdown_buffer = int(buffers_cfg.get("markdown", default_buffer))
+        notebook_buffer = int(buffers_cfg.get("notebook", default_buffer))
+        review_buffer = int(buffers_cfg.get("review", default_buffer))
+        naming_buffer = int(buffers_cfg.get("naming", default_buffer))
+        write_buffer = int(buffers_cfg.get("write", default_buffer))
+
         return cls(
             log_file=Path(logging_cfg.get("log_file", "logs/agent_pipeline.log")),
             workflow_name=logging_cfg.get("trace_workflow_name", "doc-cleaning"),
             trace_metadata=logging_cfg.get("trace_metadata", {}),
             input_artifact=Path(
                 io_cfg.get("input_artifact", "artifacts/lark_docs.json")
             ),
             output_directory=Path(
                 io_cfg.get("output_directory", "artifacts/cleaned_docs")
             ),
             router_pool=int(concurrency_cfg.get("router_pool", 2)),
             markdown_pool=int(concurrency_cfg.get("markdown_pool", 4)),
             notebook_pool=int(concurrency_cfg.get("notebook_pool", 2)),
             review_pool=int(concurrency_cfg.get("review_pool", 1)),
             naming_pool=int(concurrency_cfg.get("naming_pool", 1)),
             channel_buffer=int(concurrency_cfg.get("channel_buffer", 10)),
+            router_buffer=router_buffer,
+            markdown_buffer=markdown_buffer,
+            notebook_buffer=notebook_buffer,
+            review_buffer=review_buffer,
+            naming_buffer=naming_buffer,
+            write_buffer=write_buffer,
             max_attempts=int(retry_cfg.get("max_attempts", 2)),
             retry_policy=RetryPolicy(
                 max_attempts=int(retry_cfg.get("max_attempts", 2)),
                 initial_delay=float(retry_cfg.get("initial_delay", 1.0)),
                 backoff_multiplier=float(retry_cfg.get("backoff_multiplier", 2.0)),
                 max_delay=float(retry_cfg.get("max_delay", 30.0)),
                 jitter_ratio=float(retry_cfg.get("jitter_ratio", 0.25)),
             ),
             agent_specs=agent_specs,
         )
 
 
 # ---------------------------------------------------------------------------
 # Utility helpers
 
 
 def _truncate(value: str | None, limit: int = 160) -> str:
     if not value:
         return ""
     collapsed = " ".join(value.split())
     if len(collapsed) <= limit:
         return collapsed
     return collapsed[:limit] + "..."
 
 
@@ -512,206 +551,250 @@ class AgentFactory:
         agent = Agent[Any](
             name=spec.name,
             instructions=spec.instructions,
             model=spec.model,
             model_settings=model_settings,
             output_type=output_type,
         )
         self._agents[key] = agent
         return agent
 
     def get_timeout(self, key: str) -> float:
         spec = self.config.agent_specs[key]
         return spec.timeout if spec.timeout is not None else DEFAULT_AGENT_TIMEOUT
 
 
 async def run_agent(
     agent: Agent[Any],
     message: str,
     context: AgentCallContext,
     *,
     run_config: RunConfig,
     timeout: float | None = None,
 ) -> Any:
     hooks = LifecycleLoggingHooks(context)
     deadline = timeout if timeout is not None else DEFAULT_AGENT_TIMEOUT
-    token = current_task()
-    await AGENT_THREAD_LIMITER.acquire_on_behalf_of(token)
+    limiter_task_token = current_task()
+    await AGENT_THREAD_LIMITER.acquire_on_behalf_of(limiter_task_token)
+    model_name = getattr(agent, "model", None)
+    model_limiter = (
+        MODEL_LIMITERS.get(model_name) if isinstance(model_name, str) else None
+    )
+    if model_limiter is not None:
+        await model_limiter.acquire_on_behalf_of(limiter_task_token)
+    trace_token = TRACE_ID_VAR.set(context.trace_id or context.run_id)
     try:
         result: Any = None
         with trio.move_on_after(deadline) as cancel_scope:
             result = await trio_asyncio.aio_as_trio(Runner.run)(
                 agent,
                 message,
                 context=context,
                 hooks=hooks,
                 run_config=run_config,
             )
         if cancel_scope.cancelled_caught:
+            with trio.move_on_after(5, shield=True):
+                await trio.sleep(0)
             raise TimeoutError(
-                f"Agent call timed out after {deadline} seconds during stage {context.stage}"
+                "Agent call timed out after "
+                f"{deadline} seconds during stage {context.stage}"
             )
         return result
     finally:
-        AGENT_THREAD_LIMITER.release_on_behalf_of(token)
+        try:
+            TRACE_ID_VAR.reset(trace_token)
+        except Exception:
+            pass
+        if model_limiter is not None:
+            model_limiter.release_on_behalf_of(limiter_task_token)
+        AGENT_THREAD_LIMITER.release_on_behalf_of(limiter_task_token)
 
 
 def build_run_config(config: PipelineConfig, context: AgentCallContext) -> RunConfig:
     trace_metadata = dict(config.trace_metadata)
     trace_metadata.update(
         {"stage": context.stage, "doc_url": context.doc_url, "run_id": context.run_id}
     )
     return RunConfig(
         workflow_name=config.workflow_name,
         trace_id=context.trace_id,
         trace_metadata=trace_metadata,
     )
 
 
 # ---------------------------------------------------------------------------
 # Pipeline implementation
 
 
 class Pipeline:
     def __init__(self, config: PipelineConfig, quiet: bool = False) -> None:
         self.config = config
         self.logger = StructuredLogger(quiet=quiet, verbose_path=config.log_file)
         self._openai_client = self._initialize_openai_client()
         self.factory = AgentFactory(config, self.logger)
         self.retry_policy = config.retry_policy
         self.failures: list[dict[str, Any]] = []
         self._failure_lock = trio.Lock()
 
     async def run(self) -> None:
         try:
             self.logger.attach_python_logger("openai.agents", level=logging.DEBUG)
             self.logger.attach_python_logger(
                 "openai.agents.tracing", level=logging.INFO
             )
             docs = self._load_documents()
             total_docs = len(docs)
             self.logger.info(
                 f"Loaded {total_docs} documents from {self.config.input_artifact}"
             )
             self.config.output_directory.mkdir(parents=True, exist_ok=True)
 
             router_send, router_receive = trio.open_memory_channel[DocTask](
-                self.config.channel_buffer
+                self.config.router_buffer
             )
             markdown_send, markdown_receive = trio.open_memory_channel[WorkItem](
-                self.config.channel_buffer
+                self.config.markdown_buffer
             )
             notebook_send, notebook_receive = trio.open_memory_channel[WorkItem](
-                self.config.channel_buffer
+                self.config.notebook_buffer
             )
             review_send, review_receive = trio.open_memory_channel[ProcessedDoc](
-                self.config.channel_buffer
+                self.config.review_buffer
             )
             naming_send, naming_receive = trio.open_memory_channel[ReviewedDoc](
-                self.config.channel_buffer
+                self.config.naming_buffer
             )
             write_send, write_receive = trio.open_memory_channel[NamedDoc](
-                self.config.channel_buffer
+                self.config.write_buffer
             )
 
             markdown_done = trio.Event()
             notebook_done = trio.Event()
             review_done = trio.Event()
             naming_done = trio.Event()
 
             completion_counter = CompletionCounter(total_docs)
             channel_map: dict[str, Any] = {
                 "router_send": router_send,
                 "markdown_send": markdown_send,
                 "notebook_send": notebook_send,
                 "review_send": review_send,
                 "naming_send": naming_send,
                 "write_send": write_send,
             }
             done_events: list[trio.Event] = [
                 markdown_done,
                 notebook_done,
                 review_done,
                 naming_done,
             ]
 
             async with trio.open_nursery() as nursery:
-                nursery.start_soon(self._ingest_documents, docs, router_send)
+                nursery.start_soon(
+                    self._ingest_documents,
+                    docs,
+                    router_send,
+                    name="ingest-docs",
+                )
                 nursery.start_soon(
                     self._router_supervisor,
                     router_receive,
                     markdown_send,
                     notebook_send,
                     completion_counter,
+                    name="router-supervisor",
                 )
                 nursery.start_soon(
                     self._markdown_supervisor,
                     markdown_receive,
                     review_send,
                     markdown_done,
                     completion_counter,
+                    name="markdown-supervisor",
                 )
                 nursery.start_soon(
                     self._notebook_supervisor,
                     notebook_receive,
                     review_send,
                     notebook_done,
                     completion_counter,
+                    name="notebook-supervisor",
                 )
                 nursery.start_soon(
                     self._close_when_both_done,
                     markdown_done,
                     notebook_done,
                     review_send,
+                    name="close-review-when-transform-done",
                 )
                 nursery.start_soon(
                     self._review_supervisor,
                     review_receive,
                     naming_send,
                     review_done,
                     completion_counter,
+                    name="review-supervisor",
+                )
+                nursery.start_soon(
+                    self._close_when_done,
+                    review_done,
+                    naming_send,
+                    name="close-naming-when-review-done",
                 )
-                nursery.start_soon(self._close_when_done, review_done, naming_send)
                 nursery.start_soon(
                     self._naming_supervisor,
                     naming_receive,
                     write_send,
                     naming_done,
                     completion_counter,
+                    name="naming-supervisor",
+                )
+                nursery.start_soon(
+                    self._close_when_done,
+                    naming_done,
+                    write_send,
+                    name="close-write-when-naming-done",
+                )
+                nursery.start_soon(
+                    self._writer,
+                    write_receive,
+                    completion_counter,
+                    name="writer",
                 )
-                nursery.start_soon(self._close_when_done, naming_done, write_send)
-                nursery.start_soon(self._writer, write_receive, completion_counter)
                 nursery.start_soon(
                     self._monitor_channels,
                     channel_map,
                     completion_counter,
+                    name="channel-monitor",
                 )
                 nursery.start_soon(
                     self._watch_completion,
                     completion_counter,
                     nursery,
                     done_events,
+                    name="watch-completion",
                 )
 
             if self.failures:
                 self.logger.info(f"Failures encountered: {len(self.failures)}")
                 for failure in self.failures:
                     self.logger.info(
                         f" - doc={failure['doc_id']} stage={failure['stage']} url={failure['url']} error={failure['error']}"
                     )
         finally:
             if self._openai_client is not None:
                 self._openai_client.close()
 
     async def _execute_with_retry(
         self,
         *,
         stage: str,
         doc_id: int,
         call_factory: Callable[[int], Awaitable[Any]],
     ) -> Any:
         attempt = 0
         while True:
             try:
                 return await call_factory(attempt)
             except Exception as exc:
                 attempt += 1
@@ -743,55 +826,56 @@ class Pipeline:
         self.logger.verbose(
             f"PIPELINE_FAILURE doc={doc_id} stage={stage} url={url} error={_truncate(error_repr, 300)}"
         )
         tb_str = "".join(
             traceback.format_exception(type(error), error, error.__traceback__)
         )
         timestamp = trio.current_time()
         async with self._failure_lock:
             self.failures.append(
                 {
                     "doc_id": doc_id,
                     "url": url,
                     "stage": stage,
                     "error": error_repr,
                     "traceback": tb_str,
                     "timestamp": timestamp,
                 }
             )
         await counter.increment()
 
     def _initialize_openai_client(self) -> AsyncOpenAI | None:
         api_key = os.getenv("OPENAI_API_KEY")
         if not api_key:
             self.logger.verbose("OPENAI_CLIENT skip reason=no_api_key")
             return None
-        timeout = httpx.Timeout(connect=5.0, read=120.0, write=30.0, pool=5.0)
+        timeout = httpx.Timeout(connect=5.0, read=None, write=30.0, pool=5.0)
         client = AsyncOpenAI(api_key=api_key, timeout=timeout)
         set_default_openai_client(client)
         self.logger.verbose(
-            "OPENAI_CLIENT timeout=connect:5.0s read:120.0s write:30.0s pool:5.0s"
+            "OPENAI_CLIENT timeout=connect:5.0s read:None(write via cancel) "
+            "write:30.0s pool:5.0s"
         )
         return client
 
     async def _ingest_documents(
         self, docs: list[DocTask], send_channel: trio.MemorySendChannel[DocTask]
     ) -> None:
         async with send_channel:
             for doc in docs:
                 await send_channel.send(doc)
 
     async def _router_supervisor(
         self,
         receive: trio.MemoryReceiveChannel[DocTask],
         markdown_send: trio.MemorySendChannel[WorkItem],
         notebook_send: trio.MemorySendChannel[WorkItem],
         completion_counter: CompletionCounter,
     ) -> None:
         router_agent = self.factory.get_router_agent()
         router_timeout = self.factory.get_timeout("router")
         router_pool = self.config.router_pool
 
         async def worker(worker_idx: int) -> None:
             async with receive.clone() as channel:
                 async for task in channel:
                     doc_size = len(task.content)
@@ -839,51 +923,55 @@ class Pipeline:
                                 error=exc,
                                 counter=completion_counter,
                             )
                             continue
 
                         decision = result.final_output
                         kind = decision.route
                         rationale = decision.rationale
                     self.logger.verbose(
                         f"ROUTED doc={task.doc_id} url={task.url} kind={kind} rationale={_truncate(rationale)}"
                     )
                     item = WorkItem(
                         doc_id=task.doc_id,
                         url=task.url,
                         content=task.content,
                         metadata=task.metadata,
                         kind=kind,  # type: ignore[arg-type]
                     )
                     if kind == "markdown":
                         await markdown_send.send(item)
                     else:
                         await notebook_send.send(item)
 
         async with trio.open_nursery() as router_nursery:
             for idx in range(router_pool):
-                router_nursery.start_soon(worker, idx)
+                router_nursery.start_soon(
+                    worker,
+                    idx,
+                    name=f"router-worker-{idx}",
+                )
         await markdown_send.aclose()
         await notebook_send.aclose()
 
     async def _markdown_supervisor(
         self,
         receive: trio.MemoryReceiveChannel[WorkItem],
         review_send: trio.MemorySendChannel[ProcessedDoc],
         finished_event: trio.Event,
         completion_counter: CompletionCounter,
     ) -> None:
         agent = self.factory.get_markdown_agent()
         markdown_timeout = self.factory.get_timeout("markdown_cleaner")
         pool = self.config.markdown_pool
 
         async def worker(worker_idx: int) -> None:
             async with receive.clone() as channel:
                 async for item in channel:
 
                     async def call(attempt_index: int, item=item) -> Any:
                         metadata = dict(item.metadata)
                         metadata.setdefault("stage", "markdown-clean")
                         ctx = AgentCallContext(
                             logger=self.logger,
                             workflow_name=self.config.workflow_name,
                             stage="markdown-clean",
@@ -910,51 +998,55 @@ class Pipeline:
                         )
                     except Exception as exc:
                         await self._record_failure(
                             doc_id=item.doc_id,
                             url=item.url,
                             stage="markdown",
                             error=exc,
                             counter=completion_counter,
                         )
                         continue
 
                     output: MarkdownCleanResult = result.final_output
                     processed = ProcessedDoc(
                         doc_id=item.doc_id,
                         url=item.url,
                         kind="markdown",
                         processed_text=output.cleaned_markdown,
                         metadata=item.metadata,
                         attempts=item.attempts,
                         summary=output.summary,
                     )
                     await review_send.send(processed)
 
         async with trio.open_nursery() as md_nursery:
             for idx in range(pool):
-                md_nursery.start_soon(worker, idx)
+                md_nursery.start_soon(
+                    worker,
+                    idx,
+                    name=f"markdown-worker-{idx}",
+                )
         finished_event.set()
 
     async def _notebook_supervisor(
         self,
         receive: trio.MemoryReceiveChannel[WorkItem],
         review_send: trio.MemorySendChannel[ProcessedDoc],
         finished_event: trio.Event,
         completion_counter: CompletionCounter,
     ) -> None:
         agent = self.factory.get_notebook_agent()
         notebook_timeout = self.factory.get_timeout("notebook_refactor")
         pool = self.config.notebook_pool
 
         async def worker(worker_idx: int) -> None:
             async with receive.clone() as channel:
                 async for item in channel:
 
                     async def call(attempt_index: int, item=item) -> Any:
                         metadata = dict(item.metadata)
                         metadata.setdefault("stage", "notebook-refactor")
                         ctx = AgentCallContext(
                             logger=self.logger,
                             workflow_name=self.config.workflow_name,
                             stage="notebook-refactor",
                             run_id=f"nb-{item.doc_id}-{worker_idx}-try{attempt_index}",
@@ -980,51 +1072,55 @@ class Pipeline:
                         )
                     except Exception as exc:
                         await self._record_failure(
                             doc_id=item.doc_id,
                             url=item.url,
                             stage="notebook",
                             error=exc,
                             counter=completion_counter,
                         )
                         continue
 
                     output: NotebookRefactorResult = result.final_output
                     processed = ProcessedDoc(
                         doc_id=item.doc_id,
                         url=item.url,
                         kind="notebook",
                         processed_text=output.python_script,
                         metadata=item.metadata,
                         attempts=item.attempts,
                         summary=output.summary,
                     )
                     await review_send.send(processed)
 
         async with trio.open_nursery() as nb_nursery:
             for idx in range(pool):
-                nb_nursery.start_soon(worker, idx)
+                nb_nursery.start_soon(
+                    worker,
+                    idx,
+                    name=f"notebook-worker-{idx}",
+                )
         finished_event.set()
 
     async def _close_when_both_done(
         self,
         event_one: trio.Event,
         event_two: trio.Event,
         send_channel: trio.MemorySendChannel[Any],
     ) -> None:
         await event_one.wait()
         await event_two.wait()
         await send_channel.aclose()
 
     async def _review_supervisor(
         self,
         receive: trio.MemoryReceiveChannel[ProcessedDoc],
         naming_send: trio.MemorySendChannel[ReviewedDoc],
         finished_event: trio.Event,
         counter: CompletionCounter,
     ) -> None:
         agent = self.factory.get_reviewer_agent()
         review_timeout = self.factory.get_timeout("reviewer")
         pool = max(1, self.config.review_pool)
 
         async def worker(worker_idx: int) -> None:
             async with receive.clone() as channel:
@@ -1065,51 +1161,55 @@ class Pipeline:
                             stage="review",
                             error=exc,
                             counter=counter,
                         )
                         continue
 
                     review: ReviewResult = result.final_output
                     if review.approved:
                         reviewed = ReviewedDoc(
                             doc_id=doc.doc_id,
                             url=doc.url,
                             kind=doc.kind,
                             processed_text=doc.processed_text,
                             metadata=doc.metadata,
                             title_hint=review.suggestions or review.issues,
                         )
                         await naming_send.send(reviewed)
                     else:
                         self.logger.verbose(
                             f"REVIEW_REJECT doc={doc.doc_id} issues={_truncate(review.issues)}"
                         )
                         await counter.increment()
 
         async with trio.open_nursery() as rv_nursery:
             for idx in range(pool):
-                rv_nursery.start_soon(worker, idx)
+                rv_nursery.start_soon(
+                    worker,
+                    idx,
+                    name=f"review-worker-{idx}",
+                )
         finished_event.set()
 
     async def _naming_supervisor(
         self,
         receive: trio.MemoryReceiveChannel[ReviewedDoc],
         write_send: trio.MemorySendChannel[NamedDoc],
         finished_event: trio.Event,
         completion_counter: CompletionCounter,
     ) -> None:
         agent = self.factory.get_namer_agent()
         naming_timeout = self.factory.get_timeout("namer")
         pool = max(1, self.config.naming_pool)
 
         async def worker(worker_idx: int) -> None:
             async with receive.clone() as channel:
                 async for doc in channel:
 
                     async def call(attempt_index: int, doc=doc) -> Any:
                         metadata = dict(doc.metadata)
                         metadata.setdefault("stage", "naming")
                         ctx = AgentCallContext(
                             logger=self.logger,
                             workflow_name=self.config.workflow_name,
                             stage="naming",
                             run_id=f"name-{doc.doc_id}-{worker_idx}-try{attempt_index}",
@@ -1134,117 +1234,150 @@ class Pipeline:
                             call_factory=call,
                         )
                     except Exception as exc:
                         await self._record_failure(
                             doc_id=doc.doc_id,
                             url=doc.url,
                             stage="naming",
                             error=exc,
                             counter=completion_counter,
                         )
                         continue
 
                     naming: NamingResult = result.final_output
                     named = NamedDoc(
                         doc_id=doc.doc_id,
                         url=doc.url,
                         file_slug=normalize_slug(naming.file_slug),
                         extension=_safe_extension(naming.extension, doc.kind),
                         processed_text=doc.processed_text,
                         metadata=doc.metadata,
                     )
                     await write_send.send(named)
 
         async with trio.open_nursery() as nm_nursery:
             for idx in range(pool):
-                nm_nursery.start_soon(worker, idx)
+                nm_nursery.start_soon(
+                    worker,
+                    idx,
+                    name=f"naming-worker-{idx}",
+                )
         finished_event.set()
 
     async def _writer(
         self, receive: trio.MemoryReceiveChannel[NamedDoc], counter: CompletionCounter
     ) -> None:
         existing_names: dict[str, int] = {}
         lock = trio.Lock()
         async with receive:
             async for doc in receive:
                 async with lock:
                     base = doc.file_slug or "document"
                     ext = (
                         doc.extension
                         if doc.extension.startswith(".")
                         else f".{doc.extension}"
                         if doc.extension
                         else ".md"
                     )
                     filename = f"{base}{ext}"
                     while (self.config.output_directory / filename).exists():
                         existing_names[base] = existing_names.get(base, 0) + 1
                         filename = f"{base}-{existing_names[base]}{ext}"
                 path = self.config.output_directory / filename
-                path.write_text(doc.processed_text, encoding="utf-8")
+                tmp_path = path.with_suffix(path.suffix + ".tmp")
+                await trio.to_thread.run_sync(
+                    tmp_path.write_text,
+                    doc.processed_text,
+                    "utf-8",
+                )
+                await trio.to_thread.run_sync(os.replace, tmp_path, path)
                 await counter.increment()
                 self.logger.verbose(f"WROTE doc={doc.doc_id} -> {path}")
 
     async def _close_when_done(
         self,
         done_event: trio.Event,
         send_channel: trio.MemorySendChannel[Any],
     ) -> None:
         await done_event.wait()
         await send_channel.aclose()
 
     async def _monitor_channels(
         self,
         channels: dict[str, Any],
         counter: CompletionCounter,
         *,
         interval: float = CHANNEL_MONITOR_INTERVAL,
     ) -> None:
         try:
             while True:
                 with trio.move_on_after(interval) as scope:
                     await counter.completed.wait()
                 if not scope.cancelled_caught:
                     break
                 for name, channel in channels.items():
                     stats_fn = getattr(channel, "statistics", None)
                     if stats_fn is None:
                         continue
                     try:
                         stats = stats_fn()
                     except (trio.ClosedResourceError, RuntimeError):
                         continue
                     max_size = getattr(stats, "max_buffer_size", None)
                     current = getattr(stats, "current_buffer_used", None)
-                    if not max_size:
-                        continue
-                    if current is None:
-                        continue
-                    if current >= max_size * CHANNEL_PRESSURE_FRACTION:
+                    waiting_senders = getattr(stats, "tasks_waiting_send", None)
+                    waiting_receivers = getattr(
+                        stats,
+                        "tasks_waiting_receive",
+                        None,
+                    )
+                    if (
+                        isinstance(max_size, int)
+                        and max_size > 0
+                        and isinstance(current, int)
+                        and current >= int(max_size * CHANNEL_PRESSURE_FRACTION)
+                    ):
                         self.logger.verbose(
                             f"CHANNEL_PRESSURE name={name} load={current}/{max_size}"
                         )
+                    if (
+                        isinstance(waiting_senders, int)
+                        and waiting_senders > 0
+                    ):
+                        self.logger.verbose(
+                            "CHANNEL_BACKPRESSURE name="
+                            f"{name} waiting_senders={waiting_senders}"
+                        )
+                    if (
+                        isinstance(waiting_receivers, int)
+                        and waiting_receivers > 0
+                    ):
+                        self.logger.verbose(
+                            "CHANNEL_STARVATION name="
+                            f"{name} waiting_receivers={waiting_receivers}"
+                        )
         finally:
             self.logger.verbose("Channel monitor exiting")
 
     async def _watch_completion(
         self,
         counter: CompletionCounter,
         nursery: trio.Nursery,
         done_events: Iterable[trio.Event],
     ) -> None:
         await counter.completed.wait()
         self.logger.verbose("All documents processed, initiating graceful shutdown")
         with trio.move_on_after(30) as scope:
             for event in done_events:
                 await event.wait()
             return
         if scope.cancelled_caught:
             self.logger.verbose(
                 "Timeout during graceful shutdown, forcing cancellation"
             )
             nursery.cancel_scope.cancel()
 
     def _load_documents(self) -> list[DocTask]:
         payload = json.loads(self.config.input_artifact.read_text(encoding="utf-8"))
         docs: list[DocTask] = []
         for bucket in ("scraped_documents", "follow_up_documents"):
@@ -1343,56 +1476,56 @@ def _build_naming_prompt(doc: ReviewedDoc) -> str:
 Type: {doc.kind}
 URL: {doc.url}
 Hint: {hint}
 --- Content ---
 {doc.processed_text}
 --- End ---"""
 
 
 def _safe_extension(ext: str, kind: str) -> str:
     ext = ext.strip()
     if not ext:
         return ".py" if kind == "notebook" else ".md"
     if not ext.startswith("."):
         ext = f".{ext}"
     if kind == "notebook" and ext.lower() not in {".py", ".txt"}:
         return ".py"
     if kind == "markdown" and ext.lower() not in {".md", ".markdown"}:
         return ".md"
     return ext
 
 
 # ---------------------------------------------------------------------------
 # CLI entry point
 
 
-def parse_args(argv: Iterable[str] | None = None) -> argparse.Namespace:
+def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
     parser = argparse.ArgumentParser(
         description="Run the agent-based document cleaning pipeline."
     )
     parser.add_argument(
         "--config",
         default="configs/agent_pipeline_optimized.json",
         help="Pipeline configuration JSON path.",
     )
     parser.add_argument(
         "--quiet",
         action="store_true",
         help="Suppress console logs (still writes verbose log).",
     )
     return parser.parse_args(argv)
 
 
-def main(argv: Iterable[str] | None = None) -> int:
+def main(argv: Sequence[str] | None = None) -> int:
     args = parse_args(argv)
     config_path = Path(args.config)
     if not config_path.exists():
         print(f"Config file not found: {config_path}", file=sys.stderr)
         return 1
     config = PipelineConfig.from_json(config_path)
     pipeline = Pipeline(config, quiet=args.quiet)
     trio_asyncio.run(pipeline.run)
     return 0
 
 
 if __name__ == "__main__":  # pragma: no cover - CLI entry
     raise SystemExit(main())
