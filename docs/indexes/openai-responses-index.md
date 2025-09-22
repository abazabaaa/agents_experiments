# OpenAI Responses API Documentation Index

## Overview

This index provides comprehensive navigation for the OpenAI Responses API documentation, including core concepts, practical guides, API references, and code examples. The Responses API represents a new unified approach that combines the best capabilities from Chat Completions and Assistants APIs with enhanced features for reasoning models, function calling, and conversation management.

---

## 📖 Table of Contents

1. [Getting Started](#getting-started)
2. [Core Concepts](#core-concepts)
3. [API Reference](#api-reference)
4. [Model-Specific Guides](#model-specific-guides)
5. [Advanced Features](#advanced-features)
6. [Platform Integration](#platform-integration)
7. [Code Examples](#code-examples)
8. [Interactive Notebooks & Examples](#interactive-notebooks--examples)

---

## 🚀 Getting Started

### **Chat vs Responses API**
- **Path**: `./responses/chat-vs-responses.md`
- **Summary**: Demonstrates the evolution from Chat Completions to Responses API. Explains key differences in conversation management, function calling patterns, and when to migrate from the legacy API.
- **Key Topics**: API migration strategies, conversation state management, function calling improvements

### **Conversation State Management**
- **Path**: `./responses/conversation-state.md`
- **Summary**: Shows three approaches to managing conversation state: manual message chaining, using previous_response_id, and leveraging the Conversations API for persistent multi-turn interactions.
- **Key Topics**: Context window management, token optimization, conversation persistence
- **Examples**: `./responses/examples/background.py`, `./responses/examples/background-async.py`, `./responses/examples/background-streaming.py`, `./responses/examples/background-streaming-async.py`

---

## 🧠 Core Concepts

### **Reasoning Models Best Practices**
- **Path**: `./responses/reasoning-best-practices.md`
- **Summary**: Comprehensive guide to reasoning models (o-series) vs GPT models. Explains when to use each model family, cost optimization strategies, and performance considerations for complex problem-solving tasks.
- **Key Topics**: Model selection criteria, reasoning tokens, cached vs uncached performance, agentic workflows

### **Reasoning with Models**
- **Path**: `./responses/reasoning.md`
- **Summary**: Detailed exploration of reasoning models' internal processes. Covers reasoning tokens, effort levels, and how to leverage reasoning capabilities for complex tasks requiring step-by-step analysis.
- **Key Topics**: Chain of thought, reasoning effort settings, reasoning summaries, encrypted reasoning items

### **Streaming Responses**
- **Path**: `./responses/streaming.md`
- **Summary**: Demonstrates real-time streaming of model responses using server-sent events. Shows how to handle different event types and implement responsive user interfaces with incremental content delivery.
- **Key Topics**: SSE implementation, event handling, streaming function calls, moderation considerations
- **Examples**: `./responses/examples/streaming.py`, `./responses/examples/streaming-tools.py`

---

## 📚 API Reference

### **Response Objects Structure**
- **Path**: `./responses/response_api/responses-object.md`
- **Summary**: Minimal placeholder for response object structure documentation. This would typically contain the complete schema and field descriptions for Response objects returned by the API.

### **GET Response Endpoint**
- **Path**: `./responses/response_api/get-response.md`
- **Summary**: Comprehensive API reference for retrieving responses. Includes streaming capabilities, field inclusion options, resumable streaming, and background response polling with detailed examples.
- **Key Features**: Selective field inclusion, streaming obfuscation, sequence-based resumption, error handling patterns

### **Create & Retrieve Operations**
- **Path**: `./responses/response_api/create-get-responses.md`
- **Summary**: Shows basic response creation and retrieval patterns with practical Python examples. Demonstrates the fundamental request-response cycle and response object structure.
- **Key Features**: Basic API usage, response parsing, model output access

### **Delete & List Operations**
- **Path**: `./responses/response_api/delete-list.md`
- **Summary**: Covers response lifecycle management including deletion, cancellation of background responses, and pagination through input items with comprehensive error handling examples.
- **Key Features**: Response cleanup, background task cancellation, input item pagination, batch operations

---

## 🤖 Model-Specific Guides

### **GPT-5 Integration**
- **Path**: `./responses/usinggpt-5.md`
- **Summary**: Detailed guide for leveraging GPT-5's capabilities through the Responses API. Covers new parameters, enhanced reasoning features, and integration patterns specific to the GPT-5 model family.

### **GPT-5 Prompting Strategies**
- **Path**: `./responses/gpt5-specific/gpt5-prompting.md`
- **Summary**: Advanced prompting techniques optimized for GPT-5. Includes meta-prompting strategies, instruction clarity principles, and performance optimization tips specific to GPT-5's architecture.

### **GPT-5 New Parameters**
- **Path**: `./responses/gpt5-specific/gpt5-new-params.md`
- **Summary**: Comprehensive reference for GPT-5 specific parameters and configuration options. Explains new capabilities and how to leverage them for improved performance and control.

### **Prompting Preamble Guide for GPT-5**
- **Path**: `./responses/prompting-preamble-guide-gpt5.md`
- **Summary**: Specialized guide for crafting effective preambles and system instructions for GPT-5. Demonstrates how to establish context and behavioral guidelines for optimal model performance.

---

## ⚡ Advanced Features

### **Background Mode**
- **Path**: `./responses/background-mode.md`
- **Summary**: Enables asynchronous execution of long-running tasks on models like o3 and o1-pro. Provides reliable handling of complex problems that may take several minutes, with polling for status updates and no timeout concerns.
- **Key Topics**: Asynchronous task execution, background response polling, long-running model operations
- **Examples**: `./responses/examples/background.py`, `./responses/examples/background-async.py`, `./responses/examples/background-streaming.py`, `./responses/examples/background-streaming-async.py`

### **Function Calling**
- **Path**: `./responses/functions.md`
- **Summary**: Comprehensive guide to function calling with the Responses API. Covers tool definitions, structured outputs with function calls, parallel execution, and complex multi-step workflows.
- **Key Topics**: Tool definitions, argument validation, parallel function calls, error handling
- **Examples**: `./responses/examples/structured-outputs-tools.py`

### **Structured Outputs**
- **Path**: `./responses/structured-output.md`
- **Summary**: Complete guide to generating JSON responses that adhere to strict schemas. Covers JSON Schema validation, Pydantic integration, streaming structured outputs, and handling edge cases like refusals.
- **Key Features**: Schema adherence, type safety, refusal handling, streaming support
- **Examples**: `./responses/examples/structured-output.py`

### **Images and Vision**
- **Path**: `./responses/images.md`
- **Summary**: Comprehensive guide to image processing with OpenAI models. Covers both image generation with GPT-Image/DALL·E and vision capabilities for analyzing visual inputs. Explains multimodal applications and the differences between specialized image models and natively multimodal LLMs.
- **Key Topics**: Image generation, vision analysis, multimodal applications, GPT-Image vs DALL·E
- **API Support**: Responses API, Images API, Chat Completions API

### **Prompt Caching**
- **Path**: `./responses/prompt-caching.md`
- **Summary**: Automatic optimization that reduces latency by up to 80% and costs by up to 75% for repetitive prompts. Works transparently on all API requests without code changes, routing to servers that recently processed the same prompt prefix.
- **Key Features**: Automatic caching for prompts ≥1024 tokens, exact prefix matching, cache routing with prompt_cache_key, 5-60 minute cache persistence
- **Best Practices**: Place static content at prompt beginning, variable content at end

---

## 🌐 Platform Integration

### **Local Shell**
- **Path**: `./responses/local-shell.md`
- **Summary**: Tool enabling agents to run shell commands locally on user-provided machines. Designed for Codex CLI and codex-mini-latest model, with commands executed in user's runtime under full user control. Requires careful sandboxing and security measures.
- **Key Features**: Local command execution, continuous loop with terminal access, build-test-run workflows
- **Security**: Always sandbox execution, implement allow/deny lists, commands run on user infrastructure only
- **Integration**: Works with Responses API and codex-mini-latest model

### **Production Best Practices**
- **Path**: `./responses/production.md`
- **Summary**: Comprehensive guide for transitioning AI projects from prototype to production. Covers organizational setup, API key management, billing controls, scaling architecture, and deployment strategies for high-traffic applications.
- **Key Topics**: Organization management, API key security, staging environments, rate limiting, monitoring
- **Best Practices**: Environment variables for keys, separate staging/production projects, usage tracking, quota management

### **Azure OpenAI Integration**
- **Path**: `./responses/azure/azure-responses.md`
- **Summary**: Comprehensive guide for using the Responses API with Azure OpenAI Service. Covers authentication methods, region availability, model support, and Azure-specific features like computer use and MCP servers.
- **Key Features**:
  - Region availability and model support matrix
  - Authentication with API keys and Microsoft Entra ID
  - Code Interpreter with containerized execution
  - File input support (PDF, images, documents)
  - Function calling and tool orchestration
  - Background task processing and streaming
  - Model Context Protocol (MCP) integration
  - Image generation capabilities

---

## 💻 Code Examples

### **API Patterns Reference**
- **Path**: `./responses/patterns-reference.md`
- **Summary**: Distilled patterns for effective Responses API usage. Contrasts background resume vs multi-turn chaining, explains text_format vs function tools, and demonstrates combining both in agent loops.
- **Key Patterns**: Background + resume for long generations, multi-turn chaining for conversations, structured outputs vs tools decision matrix
- **Best Practices**: Tool discovery workflows, concurrent execution, error handling strategies

### **Basic Streaming Implementation**
- **Path**: `./responses/examples/streaming.py`
- **Summary**: Simple streaming example using Pydantic models for structured math problem solving. Shows event handling and final response retrieval patterns.
- **Dependencies**: rich, openai, pydantic
- **Use Case**: Real-time math tutoring with step-by-step explanations

### **Background Streaming with Recovery**
- **Path**: `./responses/examples/background-streaming.py`
- **Summary**: Advanced streaming example demonstrating interruption and resumption capabilities. Shows how to break and resume streams at specific sequence points for robust user experiences.
- **Dependencies**: rich, openai, pydantic
- **Use Case**: Long-running tasks with interruption handling

### **Structured Function Calling**
- **Path**: `./responses/examples/structured-outputs-tools.py`
- **Summary**: Complex example combining structured outputs with function calling. Demonstrates database query generation with strict typing and validation using Pydantic models and enums.
- **Dependencies**: openai, rich, pydantic
- **Use Case**: Business intelligence and database query automation

### **Basic Structured Output Parsing**
- **Path**: `./responses/examples/structured-output.py`
- **Summary**: Fundamental structured output example showing response parsing, validation, and error handling. Demonstrates accessing parsed objects from structured JSON responses.
- **Dependencies**: rich, openai, pydantic
- **Use Case**: Structured data extraction and validation

### **Background Processing**
- **Path**: `./responses/examples/background.py`
- **Summary**: Simple background task processing example showing response creation with interruption and stream resumption capabilities for long-running operations.
- **Dependencies**: rich, openai, pydantic
- **Use Case**: Asynchronous task processing

### **Async Background Processing**
- **Path**: `./responses/examples/background-async.py`
- **Summary**: Asynchronous implementation of background processing with proper async/await patterns and error handling for high-performance applications.
- **Dependencies**: rich, openai, pydantic
- **Use Case**: High-throughput async applications

---

## 📓 Interactive Notebooks & Examples

### **Reasoning Cookbook**
- **Path**: `./responses/reasoning-cookbook.md`
- **Summary**: Python notebook demonstrating optimal usage of reasoning models (o3, o4-mini) with the Responses API. Shows how to leverage reasoning items for higher intelligence, lower costs, and efficient token usage. Includes practical examples of reasoning summaries and hosted-tool use.
- **Key Concepts**: Reasoning token preservation, multi-turn reasoning context, encrypted content for compliance
- **Performance**: Demonstrates cost optimization and intelligence improvements through proper API usage

### **Reasoning Items Performance Optimization**
- **Path**: `./reasoning_items.py`
- **Summary**: In-depth exploration of reasoning models performance optimization using the Responses API. Demonstrates how reasoning items improve function calling performance, token efficiency, and caching utilization with practical benchmarks.
- **Key Features**:
  - Reasoning vs completion tokens breakdown
  - Function calling with reasoning context preservation
  - Encrypted reasoning items for zero data retention compliance
  - Caching optimization strategies (40% to 80% improvement)
  - Reasoning summaries for transparency
  - Performance comparisons and cost analysis

### **Multi-Tool RAG Orchestration**
- **Path**: `./responses_api_tool_orchestration.py`
- **Summary**: Comprehensive guide to building dynamic multi-tool workflows with RAG (Retrieval-Augmented Generation). Shows intelligent query routing between built-in tools (web search) and external vector databases (Pinecone) for context-aware responses.
- **Key Features**:
  - Pinecone vector database integration
  - Medical dataset processing and embedding
  - Dynamic tool selection based on query type
  - Multi-step tool orchestration workflows
  - Built-in web search preview tool
  - Parallel tool calling capabilities
  - Context-aware response generation

### **Text Generation**
- **Path**: `./responses/text-generation.md`
- **Summary**: Guide for generating text responses using the Responses API. Demonstrates simple prompt-based text generation with GPT-5 and other models, showing basic API usage patterns and response handling.
- **Key Features**: Simple text generation, response structure, output parsing
- **API Examples**: JavaScript, Python, and cURL implementations

### **Responses API Introduction**
- **Path**: `./responses_example.py`
- **Summary**: Interactive introduction to the Responses API showcasing its core features. Demonstrates stateful conversation management, hosted tools (web search), multimodal capabilities combining images and text, and the simplified API design compared to Chat Completions. Perfect starting point for developers new to the Responses API.
- **Key Features**:
  - Basic response creation and retrieval
  - Stateful conversation management with forking
  - Web search tool integration
  - Multimodal inputs (text + images)
  - Side-by-side comparison with Chat Completions API

---

## 🔗 Related Resources

### **External Documentation**
- [OpenAI Platform Documentation](https://platform.openai.com/docs/api-reference/responses)
- [Responses API Reference](https://platform.openai.com/docs/api-reference/responses)
- [Reasoning Models Guide](https://platform.openai.com/docs/guides/reasoning)

### **Community Examples**
- [OpenAI Cookbook](https://cookbook.openai.com)
- [Structured Outputs Introduction](https://cookbook.openai.com/examples/structured_outputs_intro)
- [Multi-Agent Systems with Structured Outputs](https://cookbook.openai.com/examples/structured_outputs_multi_agent)

---

## 📋 Quick Reference

### **Common Patterns**
1. **Basic Response**: `client.responses.create(model="gpt-4o", input="query")`
2. **Streaming**: `client.responses.stream(model="gpt-4o", input="query")`
3. **Function Calling**: Include `tools` parameter with function definitions
4. **Structured Output**: Use `text_format` parameter with Pydantic models
5. **Background Processing**: Set `background=True` for long-running tasks
6. **Conversation Chaining**: Use `previous_response_id` or manual context management

### **Model Recommendations**
- **GPT Models**: Fast execution, cost-effective, well-defined tasks
- **Reasoning Models (o-series)**: Complex problem-solving, high accuracy, agentic planning
- **GPT-5**: Latest capabilities, enhanced reasoning, improved performance

### **Error Handling**
- Always check `response.status` for completion state
- Handle `incomplete_details` for truncated responses
- Implement retry logic for transient failures
- Use structured error responses for debugging

---

*Last Updated: Based on documentation analysis as of the indexed date*
*For the most current information, please refer to the official OpenAI Platform documentation.*
