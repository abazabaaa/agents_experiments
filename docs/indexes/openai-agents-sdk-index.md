# OpenAI Agents SDK Documentation Index

## Table of Contents

- [Core Guides](#core-guides)
- [Agent Building Blocks and Operations](#agent-building-blocks-and-operations)
- [Voice Agents](#voice-agents)
- [Realtime Agents](#realtime-agents)
- [API Reference Stubs](#api-reference-stubs-auto-generated-via-mkdocstrings)
- [Localization](#localization)

## Core Guides

**../openai-agents-sdk/docs/index.md**
- **Summary:** Introduces the SDK primitives (agents, handoffs, guardrails, sessions), installation expectations, and a hello-world agent run so newcomers understand the building blocks before diving deeper
- **Related docs:** ../openai-agents-sdk/docs/quickstart.md, ../openai-agents-sdk/docs/agents.md, ../openai-agents-sdk/docs/running_agents.md
- **Examples to review:** ../openai-agents-sdk/examples/basic/hello_world.py, ../openai-agents-sdk/examples/basic/hello_world_gpt_5.py, ../openai-agents-sdk/examples/basic/hello_world_gpt_oss.py

**../openai-agents-sdk/docs/quickstart.md**
- **Summary:** Step-by-step project setup, agent creation, orchestration, guardrail wiring, and tracing review for a first workflow
- **Related docs:** ../openai-agents-sdk/docs/agents.md, ../openai-agents-sdk/docs/guardrails.md, ../openai-agents-sdk/docs/handoffs.md
- **Examples to review:** ../openai-agents-sdk/examples/basic/hello_world.py, ../openai-agents-sdk/examples/agent_patterns/input_guardrails.py, ../openai-agents-sdk/examples/agent_patterns/output_guardrails.py

**../openai-agents-sdk/docs/examples.md**
- **Summary:** High-level map of the repository’s runnable examples grouped by pattern (agent patterns, tools, model providers, handoffs, MCP, voice, realtime, etc.).
- **Related docs:** ../openai-agents-sdk/docs/tools.md, ../openai-agents-sdk/docs/multi_agent.md
- **Examples to review:** Every subdirectory in ../openai-agents-sdk/examples/, especially the README files in agent_patterns, model_providers, voice/static, voice/streamed, realtime/cli

**../openai-agents-sdk/docs/release.md**
- **Summary:** Versioning policy (`0.Y.Z`) with notes on what triggers minor vs patch bumps and the latest breaking changes
- **Related docs:** README.md, ../openai-agents-sdk/docs/index.md for onboarding context
- **Examples to review:** Confirm upgrade impact by running representative flows such as ../openai-agents-sdk/examples/basic/hello_world.py or ../openai-agents-sdk/examples/customer_service/main.py when bumping versions

**../openai-agents-sdk/docs/repl.md**
- **Summary:** Documents `run_demo_loop` for terminal-based interactive testing, including streaming output behavior and exit controls
- **Related docs:** ../openai-agents-sdk/docs/running_agents.md, ../openai-agents-sdk/docs/streaming.md
- **Examples to review:** Adapt ../openai-agents-sdk/examples/basic/hello_world.py or ../openai-agents-sdk/examples/basic/tools.py into a demo loop when experimenting live

## Agent Building Blocks and Operations

**../openai-agents-sdk/docs/agents.md**
- **Summary:** Deep dive into agent configuration (names, instructions, models, tools), context typing, output schemas, multi-agent patterns, dynamic prompts, lifecycle hooks, cloning, and tool-use controls
- **Related docs:** ../openai-agents-sdk/docs/tools.md, ../openai-agents-sdk/docs/handoffs.md, ../openai-agents-sdk/docs/guardrails.md
- **Examples to review:** ../openai-agents-sdk/examples/basic/tools.py, ../openai-agents-sdk/examples/agent_patterns/agents_as_tools.py, ../openai-agents-sdk/examples/agent_patterns/forcing_tool_use.py

**../openai-agents-sdk/docs/running_agents.md**
- **Summary:** Explains synchronous/async/streamed runners, the agent loop, run configuration knobs, manual vs session-based conversation management, long-running patterns, and core exceptions
- **Related docs:** ../openai-agents-sdk/docs/results.md, ../openai-agents-sdk/docs/streaming.md, ../openai-agents-sdk/docs/sessions.md
- **Examples to review:** ../openai-agents-sdk/examples/basic/stream_text.py, ../openai-agents-sdk/examples/handoffs/message_filter.py, ../openai-agents-sdk/examples/basic/previous_response_id.py

**../openai-agents-sdk/docs/results.md**
- **Summary:** Breaks down `RunResult`/`RunResultStreaming`, accessing final outputs, collecting inputs for follow-up turns, inspecting run items, guardrail results, and raw responses
- **Related docs:** ../openai-agents-sdk/docs/running_agents.md, ../openai-agents-sdk/docs/usage.md
- **Examples to review:** ../openai-agents-sdk/examples/basic/stream_items.py, ../openai-agents-sdk/examples/basic/stream_function_call_args.py

**../openai-agents-sdk/docs/usage.md**
- **Summary:** Describes automatic usage tracking (requests, tokens, reasoning usage), LiteLLM opt-in, session behavior, and hook-based reporting
- **Related docs:** ../openai-agents-sdk/docs/models/litellm.md, ../openai-agents-sdk/docs/config.md
- **Examples to review:** ../openai-agents-sdk/examples/basic/usage_tracking.py, ../openai-agents-sdk/examples/model_providers/litellm_provider.py

**../openai-agents-sdk/docs/config.md**
- **Summary:** Covers global configuration helpers for API keys, OpenAI clients/APIs, tracing toggles, verbose logging, and sensitive-data redaction environment flags
- **Related docs:** ../openai-agents-sdk/docs/tracing.md, ../openai-agents-sdk/docs/models/index.md
- **Examples to review:** ../openai-agents-sdk/examples/model_providers/custom_example_global.py, ../openai-agents-sdk/examples/model_providers/custom_example_provider.py

**../openai-agents-sdk/docs/context.md**
- **Summary:** Clarifies local `RunContextWrapper` injection vs LLM-visible context, with patterns for typed dependencies and data surfacing to prompts, inputs, or tools
- **Related docs:** ../openai-agents-sdk/docs/sessions.md, ../openai-agents-sdk/docs/tools.md
- **Examples to review:** ../openai-agents-sdk/examples/basic/dynamic_system_prompt.py, ../openai-agents-sdk/examples/customer_service/main.py, ../openai-agents-sdk/examples/agent_patterns/agents_as_tools_conditional.py

**../openai-agents-sdk/docs/sessions.md**
- **Summary:** Explains built-in memory options (OpenAI Conversations, SQLite, SQLAlchemy), CRUD operations, correction workflows, custom session protocol, and complete example flow
- **Related docs:** ../openai-agents-sdk/docs/running_agents.md, ../openai-agents-sdk/docs/context.md
- **Examples to review:** ../openai-agents-sdk/examples/memory/sqlite_session_example.py, ../openai-agents-sdk/examples/memory/sqlalchemy_session_example.py, ../openai-agents-sdk/examples/memory/encrypted_session_example.py

**../openai-agents-sdk/docs/streaming.md**
- **Summary:** Details streaming with `Runner.run_streamed`, differentiating raw response events vs run-item and agent-update events, plus handling logic
- **Related docs:** ../openai-agents-sdk/docs/results.md, ../openai-agents-sdk/docs/guardrails.md (streaming guardrails)
- **Examples to review:** ../openai-agents-sdk/examples/basic/stream_text.py, ../openai-agents-sdk/examples/agent_patterns/streaming_guardrails.py, ../openai-agents-sdk/examples/tools/code_interpreter.py

**../openai-agents-sdk/docs/tools.md**
- **Summary:** Catalogues hosted OpenAI tools, function tool wrapping, manual FunctionTool construction, agents-as-tools, conditional enablement, custom output extraction, and error handling
- **Related docs:** ../openai-agents-sdk/docs/agents.md, ../openai-agents-sdk/docs/mcp.md
- **Examples to review:** ../openai-agents-sdk/examples/tools/code_interpreter.py, ../openai-agents-sdk/examples/tools/web_search.py, ../openai-agents-sdk/examples/agent_patterns/agents_as_tools.py

**../openai-agents-sdk/docs/guardrails.md**
- **Summary:** Explains parallel input/output guardrails, tripwire behavior, implementation via decorated functions, and agent wiring
- **Related docs:** ../openai-agents-sdk/docs/agents.md, ../openai-agents-sdk/docs/streaming.md
- **Examples to review:** ../openai-agents-sdk/examples/agent_patterns/input_guardrails.py, ../openai-agents-sdk/examples/agent_patterns/output_guardrails.py, ../openai-agents-sdk/examples/agent_patterns/streaming_guardrails.py

**../openai-agents-sdk/docs/handoffs.md**
- **Summary:** Describes configuring handoffs, custom tool metadata, lifecycle callbacks, input types/filters, recommended prompt helpers, and on-handoff hooks
- **Related docs:** ../openai-agents-sdk/docs/agents.md, ../openai-agents-sdk/docs/multi_agent.md
- **Examples to review:** ../openai-agents-sdk/examples/handoffs/message_filter.py, ../openai-agents-sdk/examples/handoffs/message_filter_streaming.py, ../openai-agents-sdk/examples/customer_service/main.py

**../openai-agents-sdk/docs/multi_agent.md**
- **Summary:** Discusses LLM-directed vs code-directed orchestration, decomposition strategies, and best practices for multi-agent workflows
- **Related docs:** ../openai-agents-sdk/docs/handoffs.md, ../openai-agents-sdk/docs/tools.md
- **Examples to review:** ../openai-agents-sdk/examples/agent_patterns/deterministic.py, ../openai-agents-sdk/examples/agent_patterns/parallelization.py, ../openai-agents-sdk/examples/financial_research_agent/manager.py

**../openai-agents-sdk/docs/mcp.md**
- **Summary:** Comprehensive guide to Model Context Protocol integrations across hosted tools, streamable HTTP, SSE, and stdio transports, including approvals, filtering, prompts, caching, and tracing
- **Related docs:** ../openai-agents-sdk/docs/tools.md, ../openai-agents-sdk/docs/tracing.md
- **Examples to review:** ../openai-agents-sdk/examples/mcp/filesystem_example/, ../openai-agents-sdk/examples/mcp/sse_example/, ../openai-agents-sdk/examples/hosted_mcp/approvals.py

**../openai-agents-sdk/docs/models/index.md**
- **Summary:** Explains default OpenAI model behavior, environment overrides, GPT-5 reasoning defaults, using non-OpenAI models, mixing providers, and troubleshooting provider differences
- **Related docs:** ../openai-agents-sdk/docs/models/litellm.md, ../openai-agents-sdk/docs/config.md
- **Examples to review:** ../openai-agents-sdk/examples/model_providers/custom_example_agent.py, ../openai-agents-sdk/examples/model_providers/custom_example_provider.py, ../openai-agents-sdk/examples/model_providers/litellm_auto.py

**../openai-agents-sdk/docs/models/litellm.md**
- **Summary:** Shows how to enable the LiteLLM integration, build agents backed by external providers, and capture usage metrics
- **Related docs:** ../openai-agents-sdk/docs/models/index.md, ../openai-agents-sdk/docs/usage.md
- **Examples to review:** ../openai-agents-sdk/examples/model_providers/litellm_provider.py, ../openai-agents-sdk/examples/model_providers/litellm_auto.py

**../openai-agents-sdk/docs/tracing.md**
- **Summary:** Covers built-in tracing architecture, spans, customization hooks, sensitive data controls, cross-run tracing, and external exporter integrations
- **Related docs:** ../openai-agents-sdk/docs/config.md, ../openai-agents-sdk/docs/voice/tracing.md
- **Examples to review:** ../openai-agents-sdk/examples/customer_service/main.py, ../openai-agents-sdk/examples/mcp/prompt_server/main.py, ../openai-agents-sdk/examples/tools/web_search.py

**../openai-agents-sdk/docs/visualization.md**
- **Summary:** Documents Graphviz-based graph rendering for agent networks via `draw_graph`, including node semantics and output options
- **Related docs:** ../openai-agents-sdk/docs/multi_agent.md, ../openai-agents-sdk/docs/handoffs.md
- **Examples to review:** Generate graphs for orchestrators defined in ../openai-agents-sdk/examples/agent_patterns/agents_as_tools.py or ../openai-agents-sdk/examples/customer_service/main.py using agents.extensions.visualization

## Voice Agents

**../openai-agents-sdk/docs/voice/quickstart.md**
- **Summary:** Introduces installing voice extras, building agents with voice-aware prompts/handoffs/tools, constructing `VoicePipeline`, and streaming synthesized audio
- **Related docs:** ../openai-agents-sdk/docs/voice/pipeline.md, ../openai-agents-sdk/docs/voice/tracing.md
- **Examples to review:** ../openai-agents-sdk/examples/voice/static/main.py, ../openai-agents-sdk/examples/voice/streamed/main.py

**../openai-agents-sdk/docs/voice/pipeline.md**
- **Summary:** Explains `VoicePipeline` configuration (workflow, STT/TTS models, config), accepted audio inputs, streamed result events, and interruption handling
- **Related docs:** ../openai-agents-sdk/docs/voice/quickstart.md, ../openai-agents-sdk/docs/tracing.md
- **Examples to review:** ../openai-agents-sdk/examples/voice/streamed/my_workflow.py, ../openai-agents-sdk/examples/voice/static/util.py

**../openai-agents-sdk/docs/voice/tracing.md**
- **Summary:** Highlights tracing options specific to voice pipelines, including sensitive audio handling and workflow metadata fields
- **Related docs:** ../openai-agents-sdk/docs/tracing.md, ../openai-agents-sdk/docs/voice/pipeline.md
- **Examples to review:** Inspect tracing toggles inside ../openai-agents-sdk/examples/voice/static/main.py or ../openai-agents-sdk/examples/voice/streamed/main.py when instrumenting pipelines

## Realtime Agents

**../openai-agents-sdk/docs/realtime/quickstart.md**
- **Summary:** Beta quickstart for realtime voice agents covering prerequisites, agent/runner setup, session loop, event handling, configuration, and authentication
- **Related docs:** ../openai-agents-sdk/docs/realtime/guide.md, ../openai-agents-sdk/docs/voice/quickstart.md
- **Examples to review:** ../openai-agents-sdk/examples/realtime/cli/, ../openai-agents-sdk/examples/realtime/app/, ../openai-agents-sdk/examples/realtime/twilio/

**../openai-agents-sdk/docs/realtime/guide.md**
- **Summary:** In-depth architecture for realtime sessions, agent/session configuration, tool support, handoffs, event stream semantics, guardrails, audio processing, and direct model access
- **Related docs:** ../openai-agents-sdk/docs/realtime/quickstart.md, ../openai-agents-sdk/docs/guardrails.md
- **Examples to review:** ../openai-agents-sdk/examples/realtime/app/server.py, ../openai-agents-sdk/examples/realtime/cli/main.py, ../openai-agents-sdk/examples/realtime/twilio/server.py

## API Reference Stubs (Auto-generated via mkdocstrings)

Each file below renders the API reference for the indicated module. Pair these with the narrative guides above and the source under src/agents/… when implementing features

**../openai-agents-sdk/docs/ref/index.md**
- **Summary:** Top-level `agents` module functions (`set_default_openai_key`, tracing helpers, etc.).
- **Related docs:** ../openai-agents-sdk/docs/config.md
- **Examples to review:** ../openai-agents-sdk/examples/model_providers/custom_example_global.py, ../openai-agents-sdk/examples/customer_service/main.py

**../openai-agents-sdk/docs/ref/agent.md**
- **Summary:** API reference for `agents.agent` (Agent/AgentBase classes, cloning, hooks, tool behaviour)
- **Related docs:** ../openai-agents-sdk/docs/agents.md
- **Examples to review:** ../openai-agents-sdk/examples/basic/tools.py, ../openai-agents-sdk/examples/agent_patterns/agents_as_tools.py

**../openai-agents-sdk/docs/ref/agent_output.md**
- **Summary:** Reference for output structures returned by agents (typed outputs, helpers)
- **Related docs:** ../openai-agents-sdk/docs/results.md
- **Examples to review:** ../openai-agents-sdk/examples/basic/stream_items.py

**../openai-agents-sdk/docs/ref/computer.md**
- **Summary:** Reference for computer-use tooling integration
- **Related docs:** ../openai-agents-sdk/docs/tools.md
- **Examples to review:** ../openai-agents-sdk/examples/tools/computer_use.py

**../openai-agents-sdk/docs/ref/exceptions.md**
- **Summary:** Lists SDK exception classes (guardrail tripwires, MaxTurnsExceeded, ModelBehaviorError, etc.).
- **Related docs:** ../openai-agents-sdk/docs/running_agents.md
- **Examples to review:** ../openai-agents-sdk/examples/agent_patterns/input_guardrails.py (exception handling), ../openai-agents-sdk/examples/basic/tools.py

**../openai-agents-sdk/docs/ref/extensions/handoff_filters.md**
- **Summary:** API reference for reusable handoff input filters
- **Related docs:** ../openai-agents-sdk/docs/handoffs.md
- **Examples to review:** ../openai-agents-sdk/examples/handoffs/message_filter.py

**../openai-agents-sdk/docs/ref/extensions/handoff_prompt.md**
- **Summary:** Prompt helpers that add recommended handoff instructions
- **Related docs:** ../openai-agents-sdk/docs/handoffs.md
- **Examples to review:** ../openai-agents-sdk/examples/voice/static/main.py

**../openai-agents-sdk/docs/ref/extensions/litellm.md**
- **Summary:** Shared LiteLLM configuration helpers and registry types
- **Related docs:** ../openai-agents-sdk/docs/models/litellm.md
- **Examples to review:** ../openai-agents-sdk/examples/model_providers/litellm_provider.py

**../openai-agents-sdk/docs/ref/extensions/memory/sqlalchemy_session.md**
- **Summary:** SQLAlchemy-backed session implementation reference
- **Related docs:** ../openai-agents-sdk/docs/sessions.md
- **Examples to review:** ../openai-agents-sdk/examples/memory/sqlalchemy_session_example.py

**../openai-agents-sdk/docs/ref/extensions/models/litellm_model.md**
- **Summary:** `LitellmModel` wrapper API reference
- **Related docs:** ../openai-agents-sdk/docs/models/litellm.md
- **Examples to review:** ../openai-agents-sdk/examples/model_providers/litellm_provider.py

**../openai-agents-sdk/docs/ref/extensions/models/litellm_provider.md**
- **Summary:** LiteLLM model-provider integration reference
- **Related docs:** ../openai-agents-sdk/docs/models/litellm.md
- **Examples to review:** ../openai-agents-sdk/examples/model_providers/litellm_auto.py

**../openai-agents-sdk/docs/ref/extensions/visualization.md**
- **Summary:** Programmatic API for building visualization graphs
- **Related docs:** ../openai-agents-sdk/docs/visualization.md
- **Examples to review:** Apply to agents defined in ../openai-agents-sdk/examples/agent_patterns/agents_as_tools.py

**../openai-agents-sdk/docs/ref/function_schema.md**
- **Summary:** Utilities for generating tool schemas from Python signatures/docstrings
- **Related docs:** ../openai-agents-sdk/docs/tools.md
- **Examples to review:** ../openai-agents-sdk/examples/basic/tools.py

**../openai-agents-sdk/docs/ref/guardrail.md**
- **Summary:** Guardrail decorator classes, result containers, and helper APIs
- **Related docs:** ../openai-agents-sdk/docs/guardrails.md
- **Examples to review:** ../openai-agents-sdk/examples/agent_patterns/input_guardrails.py, ../openai-agents-sdk/examples/agent_patterns/output_guardrails.py

**../openai-agents-sdk/docs/ref/handoffs.md**
- **Summary:** Core handoff types (`Handoff`, `handoff()` helper) and lifecycle interfaces
- **Related docs:** ../openai-agents-sdk/docs/handoffs.md
- **Examples to review:** ../openai-agents-sdk/examples/handoffs/message_filter.py

**../openai-agents-sdk/docs/ref/items.md**
- **Summary:** Run item data structures (messages, tool calls, handoffs, reasoning) produced during runs
- **Related docs:** ../openai-agents-sdk/docs/results.md
- **Examples to review:** ../openai-agents-sdk/examples/basic/stream_items.py

**../openai-agents-sdk/docs/ref/lifecycle.md**
- **Summary:** Agent hook interfaces (`AgentHooks`, `RunHooks`) and lifecycle event types
- **Related docs:** ../openai-agents-sdk/docs/agents.md, ../openai-agents-sdk/docs/running_agents.md
- **Examples to review:** ../openai-agents-sdk/examples/basic/agent_lifecycle_example.py, ../openai-agents-sdk/examples/basic/lifecycle_example.py

**../openai-agents-sdk/docs/ref/logger.md**
- **Summary:** Logger configuration utilities for verbose output and handlers
- **Related docs:** ../openai-agents-sdk/docs/config.md
- **Examples to review:** Enable when debugging ../openai-agents-sdk/examples/customer_service/main.py

**../openai-agents-sdk/docs/ref/mcp/server.md**
- **Summary:** MCP server classes (Hosted, Streamable HTTP, SSE, stdio) and lifecycle APIs
- **Related docs:** ../openai-agents-sdk/docs/mcp.md
- **Examples to review:** ../openai-agents-sdk/examples/mcp/streamablehttp_example/main.py, ../openai-agents-sdk/examples/hosted_mcp/simple.py

**../openai-agents-sdk/docs/ref/mcp/util.md**
- **Summary:** MCP helper utilities (tool filters, prompt helpers)
- **Related docs:** ../openai-agents-sdk/docs/mcp.md
- **Examples to review:** ../openai-agents-sdk/examples/mcp/prompt_server/main.py

**../openai-agents-sdk/docs/ref/memory.md**
- **Summary:** Memory protocol definitions and helper factories
- **Related docs:** ../openai-agents-sdk/docs/sessions.md
- **Examples to review:** ../openai-agents-sdk/examples/memory/sqlite_session_example.py

**../openai-agents-sdk/docs/ref/memory/openai_conversations_session.md**
- **Summary:** OpenAI-hosted Conversations session adapter reference
- **Related docs:** ../openai-agents-sdk/docs/sessions.md
- **Examples to review:** ../openai-agents-sdk/examples/memory/openai_session_example.py

**../openai-agents-sdk/docs/ref/memory/session.md**
- **Summary:** Session protocol/base classes for memory backends
- **Related docs:** ../openai-agents-sdk/docs/sessions.md
- **Examples to review:** ../openai-agents-sdk/examples/memory/encrypted_session_example.py

**../openai-agents-sdk/docs/ref/memory/sqlite_session.md**
- **Summary:** SQLite-backed session implementation
- **Related docs:** ../openai-agents-sdk/docs/sessions.md
- **Examples to review:** ../openai-agents-sdk/examples/memory/sqlite_session_example.py

**../openai-agents-sdk/docs/ref/model_settings.md**
- **Summary:** ModelSettings dataclass and configuration helpers
- **Related docs:** ../openai-agents-sdk/docs/models/index.md
- **Examples to review:** ../openai-agents-sdk/examples/model_providers/custom_example_agent.py

**../openai-agents-sdk/docs/ref/models/chatcmpl_converter.md**
- **Summary:** Helpers for mapping Chat Completions responses into agent structures
- **Related docs:** ../openai-agents-sdk/docs/models/index.md
- **Examples to review:** ../openai-agents-sdk/examples/model_providers/custom_example_provider.py

**../openai-agents-sdk/docs/ref/models/chatcmpl_helpers.md**
- **Summary:** Utility helpers for Chat Completions model integration
- **Related docs:** ../openai-agents-sdk/docs/models/index.md
- **Examples to review:** ../openai-agents-sdk/examples/model_providers/custom_example_agent.py

**../openai-agents-sdk/docs/ref/models/chatcmpl_stream_handler.md**
- **Summary:** Stream handling utilities for Chat Completions models
- **Related docs:** ../openai-agents-sdk/docs/streaming.md
- **Examples to review:** ../openai-agents-sdk/examples/basic/stream_text.py

**../openai-agents-sdk/docs/ref/models/default_models.md**
- **Summary:** Default model lookup tables and helpers
- **Related docs:** ../openai-agents-sdk/docs/models/index.md
- **Examples to review:** ../openai-agents-sdk/examples/basic/hello_world.py

**../openai-agents-sdk/docs/ref/models/fake_id.md**
- **Summary:** Helper utilities for deterministic fake IDs in tests
- **Related docs:** ../openai-agents-sdk/tests/ (for patterns when writing tests)
- **Examples to review:** Apply when scripting deterministic demos such as ../openai-agents-sdk/examples/basic/tools.py

**../openai-agents-sdk/docs/ref/models/interface.md**
- **Summary:** Base `Model`/`ModelProvider` interfaces
- **Related docs:** ../openai-agents-sdk/docs/models/index.md
- **Examples to review:** ../openai-agents-sdk/examples/model_providers/custom_example_provider.py

**../openai-agents-sdk/docs/ref/models/multi_provider.md**
- **Summary:** Support for mixing providers in a single run
- **Related docs:** ../openai-agents-sdk/docs/models/index.md
- **Examples to review:** ../openai-agents-sdk/examples/financial_research_agent/manager.py

**../openai-agents-sdk/docs/ref/models/openai_chatcompletions.md**
- **Summary:** OpenAI Chat Completions model wrapper reference
- **Related docs:** ../openai-agents-sdk/docs/models/index.md
- **Examples to review:** ../openai-agents-sdk/examples/model_providers/custom_example_agent.py

**../openai-agents-sdk/docs/ref/models/openai_provider.md**
- **Summary:** Default OpenAI model provider implementation
- **Related docs:** ../openai-agents-sdk/docs/models/index.md
- **Examples to review:** ../openai-agents-sdk/examples/basic/hello_world.py

**../openai-agents-sdk/docs/ref/models/openai_responses.md**
- **Summary:** OpenAI Responses API-based model wrapper reference
- **Related docs:** ../openai-agents-sdk/docs/models/index.md
- **Examples to review:** ../openai-agents-sdk/examples/basic/hello_world.py

**../openai-agents-sdk/docs/ref/prompts.md**
- **Summary:** Prompt helper APIs (templating, transformations)
- **Related docs:** ../openai-agents-sdk/docs/context.md
- **Examples to review:** ../openai-agents-sdk/examples/basic/prompt_template.py

**../openai-agents-sdk/docs/ref/realtime/agent.md**
- **Summary:** `RealtimeAgent` API surface
- **Related docs:** ../openai-agents-sdk/docs/realtime/guide.md
- **Examples to review:** ../openai-agents-sdk/examples/realtime/cli/main.py

**../openai-agents-sdk/docs/ref/realtime/config.md**
- **Summary:** Realtime runner/session configuration schemas
- **Related docs:** ../openai-agents-sdk/docs/realtime/quickstart.md
- **Examples to review:** ../openai-agents-sdk/examples/realtime/app/server.py

**../openai-agents-sdk/docs/ref/realtime/events.md**
- **Summary:** Event stream types emitted by realtime sessions
- **Related docs:** ../openai-agents-sdk/docs/realtime/guide.md
- **Examples to review:** ../openai-agents-sdk/examples/realtime/app/server.py

**../openai-agents-sdk/docs/ref/realtime/handoffs.md**
- **Summary:** Handoff helpers specialized for realtime agents
- **Related docs:** ../openai-agents-sdk/docs/realtime/guide.md, ../openai-agents-sdk/docs/handoffs.md
- **Examples to review:** ../openai-agents-sdk/examples/realtime/app/server.py

**../openai-agents-sdk/docs/ref/realtime/items.md**
- **Summary:** Data structures representing realtime conversation history items
- **Related docs:** ../openai-agents-sdk/docs/realtime/guide.md
- **Examples to review:** ../openai-agents-sdk/examples/realtime/app/server.py

**../openai-agents-sdk/docs/ref/realtime/model.md**
- **Summary:** Realtime model interface and lifecycle controls
- **Related docs:** ../openai-agents-sdk/docs/realtime/guide.md
- **Examples to review:** ../openai-agents-sdk/examples/realtime/cli/main.py

**../openai-agents-sdk/docs/ref/realtime/model_events.md**
- **Summary:** Low-level events emitted by realtime models
- **Related docs:** ../openai-agents-sdk/docs/realtime/guide.md
- **Examples to review:** ../openai-agents-sdk/examples/realtime/app/server.py

**../openai-agents-sdk/docs/ref/realtime/model_inputs.md**
- **Summary:** Data contracts for sending audio/text into realtime sessions
- **Related docs:** ../openai-agents-sdk/docs/realtime/quickstart.md
- **Examples to review:** ../openai-agents-sdk/examples/realtime/twilio/server.py

**../openai-agents-sdk/docs/ref/realtime/openai_realtime.md**
- **Summary:** Concrete OpenAI realtime model client reference
- **Related docs:** ../openai-agents-sdk/docs/realtime/guide.md
- **Examples to review:** ../openai-agents-sdk/examples/realtime/app/server.py

**../openai-agents-sdk/docs/ref/realtime/runner.md**
- **Summary:** `RealtimeRunner` orchestration API reference
- **Related docs:** ../openai-agents-sdk/docs/realtime/quickstart.md
- **Examples to review:** ../openai-agents-sdk/examples/realtime/cli/main.py

**../openai-agents-sdk/docs/ref/realtime/session.md**
- **Summary:** `RealtimeSession` methods for streaming, sending audio, and lifecycle handling
- **Related docs:** ../openai-agents-sdk/docs/realtime/guide.md
- **Examples to review:** ../openai-agents-sdk/examples/realtime/app/server.py

**../openai-agents-sdk/docs/ref/repl.md**
- **Summary:** Reference for `run_demo_loop` and REPL helpers
- **Related docs:** ../openai-agents-sdk/docs/repl.md
- **Examples to review:** Convert ../openai-agents-sdk/examples/basic/hello_world.py into a demo loop script

**../openai-agents-sdk/docs/ref/result.md**
- **Summary:** `RunResult`/`RunResultStreaming` classes, accessors, and helpers
- **Related docs:** ../openai-agents-sdk/docs/results.md
- **Examples to review:** ../openai-agents-sdk/examples/basic/stream_items.py

**../openai-agents-sdk/docs/ref/run.md**
- **Summary:** `Runner` API reference including run methods and configuration
- **Related docs:** ../openai-agents-sdk/docs/running_agents.md
- **Examples to review:** ../openai-agents-sdk/examples/basic/stream_text.py

**../openai-agents-sdk/docs/ref/run_context.md**
- **Summary:** `RunContextWrapper` and related helpers
- **Related docs:** ../openai-agents-sdk/docs/context.md
- **Examples to review:** ../openai-agents-sdk/examples/customer_service/main.py

**../openai-agents-sdk/docs/ref/stream_events.md**
- **Summary:** Stream event classes emitted during `run_streamed`
- **Related docs:** ../openai-agents-sdk/docs/streaming.md
- **Examples to review:** ../openai-agents-sdk/examples/basic/stream_text.py

**../openai-agents-sdk/docs/ref/strict_schema.md**
- **Summary:** Strict schema tooling for structured outputs
- **Related docs:** ../openai-agents-sdk/docs/agents.md (output types)
- **Examples to review:** ../openai-agents-sdk/examples/basic/non_strict_output_type.py

**../openai-agents-sdk/docs/ref/tool.md**
- **Summary:** Tool classes (function tools, hosted MCP tools, etc.).
- **Related docs:** ../openai-agents-sdk/docs/tools.md
- **Examples to review:** ../openai-agents-sdk/examples/tools/file_search.py, ../openai-agents-sdk/examples/tools/image_generator.py

**../openai-agents-sdk/docs/ref/tool_context.md**
- **Summary:** Tool execution context data structures
- **Related docs:** ../openai-agents-sdk/docs/tools.md
- **Examples to review:** ../openai-agents-sdk/examples/tools/code_interpreter.py

**../openai-agents-sdk/docs/ref/tracing/create.md**
- **Summary:** APIs for manually creating traces/spans
- **Related docs:** ../openai-agents-sdk/docs/tracing.md
- **Examples to review:** ../openai-agents-sdk/examples/tools/web_search.py

**../openai-agents-sdk/docs/ref/tracing/index.md**
- **Summary:** Tracing module entry point (provider setup, helpers)
- **Related docs:** ../openai-agents-sdk/docs/tracing.md
- **Examples to review:** ../openai-agents-sdk/examples/customer_service/main.py

**../openai-agents-sdk/docs/ref/tracing/logger.md**
- **Summary:** Tracing-specific logging utilities
- **Related docs:** ../openai-agents-sdk/docs/tracing.md
- **Examples to review:** Inspect when debugging ../openai-agents-sdk/examples/mcp/* flows

**../openai-agents-sdk/docs/ref/tracing/processor_interface.md**
- **Summary:** Interfaces for custom trace processors/exporters
- **Related docs:** ../openai-agents-sdk/docs/tracing.md
- **Examples to review:** Extend when instrumenting ../openai-agents-sdk/examples/tools/web_search_filters.py

**../openai-agents-sdk/docs/ref/tracing/processors.md**
- **Summary:** Built-in trace processors (batch exporter, etc.).
- **Related docs:** ../openai-agents-sdk/docs/tracing.md
- **Examples to review:** Evaluate against ../openai-agents-sdk/examples/mcp/prompt_server/main.py when plugging alternative exporters

**../openai-agents-sdk/docs/ref/tracing/provider.md**
- **Summary:** Trace provider setup and configuration
- **Related docs:** ../openai-agents-sdk/docs/tracing.md
- **Examples to review:** ../openai-agents-sdk/examples/customer_service/main.py

**../openai-agents-sdk/docs/ref/tracing/scope.md**
- **Summary:** Scope/context managers for spans
- **Related docs:** ../openai-agents-sdk/docs/tracing.md
- **Examples to review:** ../openai-agents-sdk/examples/agent_patterns/parallelization.py

**../openai-agents-sdk/docs/ref/tracing/setup.md**
- **Summary:** Initialization helpers for tracing
- **Related docs:** ../openai-agents-sdk/docs/tracing.md
- **Examples to review:** ../openai-agents-sdk/examples/tools/web_search.py

**../openai-agents-sdk/docs/ref/tracing/span_data.md**
- **Summary:** Span payload data classes (agent spans, tool spans, etc.).
- **Related docs:** ../openai-agents-sdk/docs/tracing.md
- **Examples to review:** Inspect outputs from ../openai-agents-sdk/examples/tools/code_interpreter.py in traces

**../openai-agents-sdk/docs/ref/tracing/spans.md**
- **Summary:** Span helper constructors for common operations
- **Related docs:** ../openai-agents-sdk/docs/tracing.md
- **Examples to review:** ../openai-agents-sdk/examples/tools/file_search.py

**../openai-agents-sdk/docs/ref/tracing/traces.md**
- **Summary:** Trace object definitions and management APIs
- **Related docs:** ../openai-agents-sdk/docs/tracing.md
- **Examples to review:** ../openai-agents-sdk/examples/tools/web_search_filters.py

**../openai-agents-sdk/docs/ref/tracing/util.md**
- **Summary:** Miscellaneous tracing utilities
- **Related docs:** ../openai-agents-sdk/docs/tracing.md
- **Examples to review:** ../openai-agents-sdk/examples/mcp/git_example/main.py

**../openai-agents-sdk/docs/ref/usage.md**
- **Summary:** Usage metrics data structures and helpers
- **Related docs:** ../openai-agents-sdk/docs/usage.md
- **Examples to review:** ../openai-agents-sdk/examples/basic/usage_tracking.py

**../openai-agents-sdk/docs/ref/version.md**
- **Summary:** SDK version metadata helpers
- **Related docs:** ../openai-agents-sdk/docs/release.md
- **Examples to review:** Validate when packaging via scripts in ../openai-agents-sdk/examples/basic/hello_world.py for compatibility checks

**../openai-agents-sdk/docs/ref/voice/events.md**
- **Summary:** Voice pipeline stream event classes
- **Related docs:** ../openai-agents-sdk/docs/voice/pipeline.md
- **Examples to review:** ../openai-agents-sdk/examples/voice/streamed/main.py

**../openai-agents-sdk/docs/ref/voice/exceptions.md**
- **Summary:** Voice-specific exception hierarchy
- **Related docs:** ../openai-agents-sdk/docs/voice/pipeline.md
- **Examples to review:** Handle in ../openai-agents-sdk/examples/voice/static/main.py

**../openai-agents-sdk/docs/ref/voice/imports.md**
- **Summary:** Public import surface for voice helpers
- **Related docs:** ../openai-agents-sdk/docs/voice/quickstart.md
- **Examples to review:** ../openai-agents-sdk/examples/voice/static/main.py

**../openai-agents-sdk/docs/ref/voice/input.md**
- **Summary:** Input data types for voice workflows (`AudioInput`, `StreamedAudioInput`)
- **Related docs:** ../openai-agents-sdk/docs/voice/pipeline.md
- **Examples to review:** ../openai-agents-sdk/examples/voice/static/main.py, ../openai-agents-sdk/examples/voice/streamed/main.py

**../openai-agents-sdk/docs/ref/voice/model.md**
- **Summary:** Voice model interfaces for STT/TTS abstractions
- **Related docs:** ../openai-agents-sdk/docs/voice/pipeline.md
- **Examples to review:** ../openai-agents-sdk/examples/voice/streamed/my_workflow.py

**../openai-agents-sdk/docs/ref/voice/models/openai_model_provider.md**
- **Summary:** OpenAI voice model provider reference
- **Related docs:** ../openai-agents-sdk/docs/voice/pipeline.md
- **Examples to review:** ../openai-agents-sdk/examples/voice/streamed/main.py

**../openai-agents-sdk/docs/ref/voice/models/openai_provider.md**
- **Summary:** OpenAI voice provider wiring for workflows
- **Related docs:** ../openai-agents-sdk/docs/voice/pipeline.md
- **Examples to review:** ../openai-agents-sdk/examples/voice/static/main.py

**../openai-agents-sdk/docs/ref/voice/models/openai_stt.md**
- **Summary:** Speech-to-text model reference
- **Related docs:** ../openai-agents-sdk/docs/voice/pipeline.md
- **Examples to review:** ../openai-agents-sdk/examples/voice/streamed/my_workflow.py

**../openai-agents-sdk/docs/ref/voice/models/openai_tts.md**
- **Summary:** Text-to-speech model reference
- **Related docs:** ../openai-agents-sdk/docs/voice/pipeline.md
- **Examples to review:** ../openai-agents-sdk/examples/voice/streamed/main.py

**../openai-agents-sdk/docs/ref/voice/pipeline.md**
- **Summary:** `VoicePipeline` class reference
- **Related docs:** ../openai-agents-sdk/docs/voice/pipeline.md (guide)
- **Examples to review:** ../openai-agents-sdk/examples/voice/static/main.py

**../openai-agents-sdk/docs/ref/voice/pipeline_config.md**
- **Summary:** `VoicePipelineConfig` settings reference
- **Related docs:** ../openai-agents-sdk/docs/voice/pipeline.md, ../openai-agents-sdk/docs/voice/tracing.md
- **Examples to review:** ../openai-agents-sdk/examples/voice/streamed/main.py

**../openai-agents-sdk/docs/ref/voice/result.md**
- **Summary:** Voice pipeline result/stream interfaces
- **Related docs:** ../openai-agents-sdk/docs/voice/pipeline.md
- **Examples to review:** ../openai-agents-sdk/examples/voice/static/main.py

**../openai-agents-sdk/docs/ref/voice/utils.md**
- **Summary:** Helper utilities for audio buffers and playback
- **Related docs:** ../openai-agents-sdk/docs/voice/quickstart.md
- **Examples to review:** ../openai-agents-sdk/examples/voice/static/util.py

**../openai-agents-sdk/docs/ref/voice/workflow.md**
- **Summary:** Voice workflow base classes and single-agent workflow helpers
- **Related docs:** ../openai-agents-sdk/docs/voice/pipeline.md
- **Examples to review:** ../openai-agents-sdk/examples/voice/streamed/my_workflow.py

## Localization

**../openai-agents-sdk/docs/ja/*.md**
- **Summary:** Japanese translations of the core guides (index, quickstart, agents, guardrails, handoffs, MCP, multi-agent, models, realtime, release, repl, results, running agents, sessions, streaming, tools, tracing, usage, visualization, voice, etc.).
- **Related docs:** The corresponding English files listed above
- **Examples to review:** Same example files referenced for the English documentation—code paths do not change between languages

