# Agent Pipeline System Architecture

## Overview

This system is a sophisticated document processing pipeline that orchestrates OpenAI Agents through a multi-stage workflow using Trio for structured concurrency and trio-asyncio for bridging with the asyncio-based OpenAI SDK.

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    ENTRY POINT                               │
│  gpt5_nano_smoke.py                                         │
│  • Loads configuration (smoke_gpt5_nano.json)              │
│  • Optionally limits document count                        │
│  • Calls run_pipeline()                                    │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              INITIALIZATION LAYER                            │
│  agent_pipeline/__init__.py                                 │
│  • Loads .env for API keys                                 │
│  • Configures SDK diagnostics & telemetry                  │
│  • Sets up trace exporters & loggers                       │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                 PIPELINE ORCHESTRATION                       │
│  Pipeline class (pipeline.py)                               │
│  • Creates run directory & logging                         │
│  • Initializes AgentRegistry & LimiterPool                 │
│  • Builds instrumented AsyncOpenAI client                  │
│  • Runs main orchestration with trio_asyncio.run()         │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              TRIO STRUCTURED CONCURRENCY                     │
│  Pipeline.run() method                                      │
│  • Opens Trio nursery for concurrent tasks                 │
│  • Creates memory channels for stage communication         │
│  • Spawns document processing tasks (limited by semaphore) │
│  • Spawns writer stage task                                │
│  • Manages completion tracking                             │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│               DOCUMENT PROCESSING                            │
│  Pipeline._process_document()                               │
│  • Acquires semaphore slot                                 │
│  • Calls WorkflowRunner.process_document()                 │
│  • Handles failures with structured logging                │
│  • Sends results to writer channel                         │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│               WORKFLOW EXECUTION                             │
│  WorkflowRunner (workflow/runner.py)                        │
│  Two modes:                                                │
│  1. Orchestrator Mode (single agent manages workflow)      │
│  2. Manual Mode (sequential stage execution)               │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                  AGENT STAGES                               │
│  Sequential execution (manual mode):                        │
│  1. Router → Decides markdown vs notebook path             │
│  2. Transformer → MarkdownCleaner OR NotebookRefactor      │
│  3. Reviewer → Validates output quality                    │
│  4. Namer → Generates filename and metadata                │
│  Optional: Rework loop if review fails                     │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              TRIO-ASYNCIO BRIDGE                            │
│  bridge/asyncio.py                                         │
│  • Creates isolated asyncio event loop per agent call      │
│  • Wraps Runner.run() with trio_asyncio.aio_as_trio()     │
│  • Handles cancellation and cleanup                        │
│  • Prevents loop reuse across documents                    │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                 AGENT EXECUTION                             │
│  agents/runner.py                                          │
│  • Acquires rate limiter slot (per model)                  │
│  • Sets up lifecycle logging hooks                         │
│  • Applies timeout with trio.move_on_after()              │
│  • Calls OpenAI SDK Runner.run() or run_streamed()        │
│  • Handles MaxTurnsExceeded and timeouts                   │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                  OUTPUT STAGE                               │
│  Writer Stage (stages/writer.py)                           │
│  • Receives processed documents via channel                │
│  • Writes to artifacts/smoke_output/                       │
│  • Updates completion counter                              │
│  • Logs success/failure per document                       │
└──────────────────────────────────────────────────────────────┘
```

## Key Components

### 1. Concurrency Model (Trio + trio-asyncio)

The system uses **Trio** for structured concurrency with **trio-asyncio** to bridge with the asyncio-based OpenAI SDK:

- **Trio Nursery**: All concurrent tasks run within a single nursery in `Pipeline.run()`
- **Semaphore Control**: Limits parallel document processing (default: agent_thread_limit)
- **Memory Channels**: Trio channels connect processing stages asynchronously
- **Isolated Event Loops**: Each agent call gets its own asyncio loop via `trio_asyncio.open_loop()`

**Critical Design Decisions:**
- Never reuse asyncio loops across documents
- Always clean up loops on cancellation
- Use `aio_as_trio` wrapper for SDK calls
- Disable HTTP keep-alives to prevent stale connections

### 2. Agent System

Agents are OpenAI SDK `Agent` instances with structured output:

**Agent Types:**
- **Router**: Decides markdown vs notebook processing path
- **MarkdownCleaner**: Transforms markdown documents
- **NotebookRefactor**: Converts notebooks to Python scripts
- **Reviewer**: Validates output quality
- **Namer**: Generates filenames and metadata
- **Orchestrator**: (Optional) Manages entire workflow

**Agent Configuration:**
- Model selection (e.g., gpt-5-turbo)
- Timeout controls
- Max turns limit
- Retry policies
- Tool specifications

### 3. Rate Limiting

Multi-level rate limiting via `LimiterPool`:

- **Overall Limit**: Total concurrent agent calls
- **Per-Model Limits**: Specific limits per model type
- **Acquisition Pattern**: `async with limiter_pool.acquire(model=model_key)`

### 4. Instrumentation & Telemetry

Comprehensive observability stack:

**Trace Collection:**
- Custom `JSONLinesTraceExporter` writes to `logs/openai_sdk/traces/`
- Batched processing with configurable flush intervals
- Full span/trace data from SDK

**Logging Hierarchy:**
- **Pipeline Logger**: Structured high-level events
- **Agent Logger**: Per-agent lifecycle events
- **HTTP Logger**: Request/response diagnostics
- **SDK Logger**: Internal SDK debug output

**HTTP Instrumentation:**
- Custom `InstrumentedAsyncClient` wraps httpx
- Logs all requests with timing and status
- Captures x-request-id for correlation

### 5. Error Handling & Retry

Multi-layer error handling:

**Retry Levels:**
1. HTTP retries in OpenAI client (max_retries=5)
2. Agent-level retries via `call_agent_with_retry()`
3. Workflow rework cycles for review failures

**Failure Tracking:**
- Failures recorded with full context
- Traceback preservation
- Structured failure reports at pipeline end

### 6. Workflow Stages

**Document Flow:**
1. **Ingestion**: Load from JSON input file
2. **Routing**: Determine processing path
3. **Transformation**: Clean/refactor content
4. **Review**: Validate quality
5. **Rework** (Optional): Re-process if review fails
6. **Naming**: Generate output filename
7. **Writing**: Save to output directory

**Rework Logic:**
- Configurable max cycles (default: 2)
- Three rework targets: router, same stage, or specific type
- Feedback propagation via developer messages

## Performance Characteristics

### Concurrency
- Parallel document processing up to `agent_thread_limit`
- Async I/O for all external calls
- Non-blocking channel communication between stages

### Memory Management
- Bounded channels prevent memory overflow
- Incremental processing (no full batch loading)
- Automatic cleanup via context managers

### Timeout Hierarchy
1. HTTP timeouts (connect/read/write/pool)
2. Agent call timeouts (per-stage configuration)
3. Trio cancellation scopes
4. Progress monitoring for stuck agents

## Configuration

Key configuration parameters in `smoke_gpt5_nano.json`:

```json
{
  "workflow_name": "smoke_pipeline",
  "concurrency": {
    "agent_thread_limit": 10,
    "model_limits": {
      "gpt-4o-mini": 5
    },
    "stage_buffers": {
      "write": 10
    }
  },
  "httpx_timeout": {
    "connect": 10.0,
    "read": 180.0,
    "write": 60.0,
    "pool": 10.0
  },
  "retry_policy": {
    "max_attempts": 3,
    "initial_delay": 1.0
  }
}
```

## File Organization

```
src/agent_pipeline/
├── __init__.py           # Package init, env loading, diagnostics setup
├── pipeline.py           # Main Pipeline class
├── config.py            # Configuration models
├── openai_client.py     # Instrumented AsyncOpenAI
├── tracing_config.py    # SDK telemetry setup
├── agents/
│   ├── registry.py      # Agent factory/registry
│   ├── runner.py        # Agent execution helpers
│   └── runconfig.py     # Run configuration builder
├── bridge/
│   └── asyncio.py       # Trio-asyncio integration
├── workflow/
│   └── runner.py        # WorkflowRunner orchestration
├── stages/
│   ├── types.py         # Stage data models
│   ├── models.py        # Pydantic output models
│   └── writer.py        # Output writing stage
└── logging.py           # Structured logging utilities
```

## Critical Implementation Notes

### Trio-AsyncIO Integration
The system carefully manages the boundary between Trio and asyncio:

1. **Loop Lifecycle**: Each agent call creates and destroys its own event loop
2. **Cancellation**: Trio cancellations properly clean up asyncio tasks
3. **No Keep-Alive**: HTTP connections don't persist across loops
4. **Explicit Contexts**: Always use `async with trio_asyncio.open_loop()`

### Why This Matters
- Prevents orphaned asyncio tasks
- Ensures clean shutdown
- Avoids "Event loop is closed" errors
- Maintains Trio's structured concurrency guarantees

### Performance Tuning
For optimal performance:
- Adjust `agent_thread_limit` based on API rate limits
- Configure per-model limits to prevent throttling
- Tune HTTP timeouts for your network conditions
- Monitor trace logs for bottleneck identification