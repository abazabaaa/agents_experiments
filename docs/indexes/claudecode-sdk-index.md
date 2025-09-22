# Claude Code SDK Documentation Index

> Your comprehensive guide to building powerful AI agents with the Claude Code Software Development Kit

## Table of Contents

### Core Documentation
1. [What is the Claude Code SDK?](#what-is-the-claude-code-sdk)
2. [Quick Start & Getting Started](#quick-start--getting-started)
3. [Core SDK Documentation](#core-sdk-documentation)

### Implementation & Integration
4. [Session & State Management](#session--state-management)
5. [Extensibility & Integration](#extensibility--integration)
6. [Security & Permissions](#security--permissions)

### Learning & Examples
7. [Examples & Tutorials](#examples--tutorials)
8. [Advanced Features](#advanced-features)

### Reference & Best Practices
9. [Tools & Built-in Capabilities](#tools--built-in-capabilities)
10. [Best Practices & Workflows](#best-practices--workflows)

### Quick Navigation
- **New to the SDK?** Start with [What is the Claude Code SDK?](#what-is-the-claude-code-sdk) and [Quick Start](#quick-start--getting-started)
- **Ready to build?** Jump to [Examples & Tutorials](#examples--tutorials)
- **Need API reference?** See [Core SDK Documentation](#core-sdk-documentation)
- **Production deployment?** Check [Security & Permissions](#security--permissions) and [Best Practices](#best-practices--workflows)

---

## What is the Claude Code SDK?

The Claude Code SDK is a powerful toolkit that transforms Claude from a conversational AI into a sophisticated agentic system capable of autonomous task execution, tool usage, and complex workflow orchestration. Originally designed for software development workflows, the SDK has evolved into a comprehensive framework for building AI agents across any domain.

### Key Capabilities
- **Autonomous task execution** with intelligent tool selection and usage
- **Multi-turn conversation management** with persistent session state
- **Custom tool creation** through Model Context Protocol (MCP) servers
- **Advanced permission systems** for secure operation in production environments
- **Subagent orchestration** for complex, multi-stage workflows
- **Streaming input/output** for real-time interaction patterns

---

## Quick Start & Getting Started

> **⚠️ CRITICAL CONTENT MISMATCH**: The `overview.md` file contains todo management documentation instead of SDK overview content. This file should be renamed or replaced with proper SDK overview documentation to avoid user confusion.

### Core Overview
- **Path**: `./claudecode_sdk/overview.md`
- **Summary**: **⚠️ FILE CONTENT MISMATCH**: This file contains todo management documentation instead of SDK overview content. The todo documentation is duplicated in `./claudecode_sdk/todo.md`. Users seeking SDK overview information should refer to other documentation files or wait for this issue to be resolved.
- **Examples**: Todo tracking classes in both TypeScript and Python

### Cost Tracking and Usage
- **Path**: `./claudecode_sdk/usage.md`
- **Summary**: Essential guide for tracking costs and token usage in SDK applications. Covers message-level usage reporting, handling parallel tool execution, and implementing cost tracking systems for billing.
- **Examples**: Cost tracking classes, billing aggregation, usage monitoring patterns

### Quick Start Example
- **Path**: `./claudecode_sdk/examples/quickstart.py`
- **Summary**: Minimal working Python example demonstrating basic SDK usage patterns. Shows simple queries, options configuration, and tool integration.
- **Examples**: Basic query, with-options query, file operations with tools

---

## Core SDK Documentation

### Python SDK Reference
- **Path**: `./claudecode_sdk/pythonsdk.md`
- **Summary**: Complete API reference for Python SDK including all functions, types, and classes. Covers `query()` async function, tool decorators, `ClaudeSDKClient` class, and comprehensive type definitions for all tools.
- **Examples**:
  - `./claudecode_sdk/examples/quickstart.py`
  - `./claudecode_sdk/examples/streaming_mode.py`
  - `./claudecode_sdk/examples/permissions_callbacks.py`

### TypeScript SDK Reference
- **Path**: `./claudecode_sdk/typescript_sdk.md`
- **Summary**: Complete API reference for TypeScript SDK with detailed type definitions, interfaces, and usage patterns. Includes streaming, permissions, hooks, and tool input/output types using Zod schemas.
- **Examples**: TypeScript code samples throughout the reference documentation

### Todo Management
- **Path**: `./claudecode_sdk/todo.md`
- **Summary**: Shows how to track and display todos using the Claude Code SDK for organized task management. Demonstrates todo lifecycle, real-time progress tracking, and structured task organization.
- **Examples**: Todo tracking classes in both TypeScript and Python
- **⚠️ Note**: This content is duplicated in `overview.md` - file consolidation recommended to eliminate confusion

---

## Session & State Management

### Session Management
- **Path**: `./claudecode_sdk/session_management.md`
- **Summary**: Comprehensive guide to SDK's file-based session system covering conversation persistence, state restoration, and session resumption. Session files are stored in `~/.config/claude/` with JSONL format for conversation transcripts.
- **Examples**: Session resumption patterns, interrupted session recovery, metadata handling

### Slash Commands
- **Path**: `./claudecode_sdk/slash_commands.md`
- **Summary**: Demonstrates creating custom user-friendly shortcuts for common operations within the SDK. Covers command definition, parameter handling, and integration patterns.
- **Examples**: Command registration, parameter validation, usage patterns

---

## Extensibility & Integration

### Custom Tools Development
- **Path**: `./claudecode_sdk/custom_tools.md`
- **Summary**: Comprehensive guide to building and integrating custom tools through in-process MCP servers. Uses `createSdkMcpServer` and `tool` decorators/helpers with Zod schemas for type safety.
- **Examples**: Weather API tool, database query tool, API gateway tool, calculator with compound interest

### MCP Integration Guide
- **Path**: `./claudecode_sdk/mcp_in_sdk.md`
- **Summary**: Explains how to extend Claude Code with external Model Context Protocol (MCP) servers supporting stdio, HTTP/SSE, and SDK transport types. Configuration is done via `.mcp.json` files.
- **Examples**: Server configurations for filesystem and custom servers, authentication patterns, error handling

### Subagents in SDK
- **Path**: `./claudecode_sdk/subagents_in_sdk.md`
- **Summary**: Shows how to work with specialized AI subagents for context management and parallelization. Covers filesystem-based subagent creation and orchestration patterns.
- **Examples**: Subagent definition files, tool restrictions, invocation patterns

---

## Security & Permissions

### Permission Handling
- **Path**: `./claudecode_sdk/handlingpermissions.md`
- **Summary**: Demonstrates implementing custom permission systems for tool usage control in production environments. Covers callback functions, permission modes, and security patterns.
- **Examples**:
  - `./claudecode_sdk/examples/permissions_callbacks.py`

### System Prompt Modification
- **Path**: `./claudecode_sdk/modifying_system_prompts.md`
- **Summary**: Explains how to customize and append to system prompts for specialized agent behavior. Covers prompt engineering techniques and best practices.
- **Examples**: Custom prompt patterns, specialized instructions

---

## Examples & Tutorials

### Comprehensive Agent Tutorial Series
- **Path**: `./claudecode_sdk/examples/claude_code_sdk/README.md`
- **Summary**: Step-by-step tutorial series for building sophisticated general-purpose agentic systems. Requires uv, Node.js, and Claude Code CLI installation. Progresses from simple research agents to multi-agent orchestration with external system integration.
- **Examples**: Three Jupyter notebooks demonstrating research, chief of staff, and observability agents

### Jupyter Notebook Tutorials

#### Research Agent Tutorial
- **Path**: `./claudecode_sdk/examples/claude_code_sdk/00_The_one_liner_research_agent.ipynb`
- **Summary**: Start with a simple yet powerful research agent demonstrating core SDK concepts, WebSearch tool usage, and multimodal capabilities with the Read tool for analyzing images and charts.

#### Chief of Staff Agent Tutorial
- **Path**: `./claudecode_sdk/examples/claude_code_sdk/01_The_chief_of_staff_agent.ipynb`
- **Summary**: Build a comprehensive AI Chief of Staff for TechStart Inc showcasing advanced features: memory management with CLAUDE.md, output styles for different stakeholders, plan mode, custom commands, hooks, and subagent orchestration.

#### Observability Agent Tutorial
- **Path**: `./claudecode_sdk/examples/claude_code_sdk/02_The_observability_agent.ipynb`
- **Summary**: Create a DevOps monitoring agent with external system integration through Git and GitHub MCP servers (requires GitHub token and Docker), demonstrating real-time monitoring and incident response.

### Complete Agent Implementations
- **Path**: `./claudecode_sdk/examples/claude_code_sdk/research_agent/agent.py`
- **Summary**: Standalone Python implementation of autonomous research agent with web search and multimodal analysis capabilities using ClaudeSDKClient.

- **Path**: `./claudecode_sdk/examples/claude_code_sdk/chief_of_staff_agent/agent.py`
- **Summary**: Multi-agent executive assistant implementation with financial modeling, compliance tracking via hooks, and specialized subagent coordination (financial-analyst and recruiter subagents).
- **Related Scripts**:
  - Financial forecast analysis
  - Decision matrix generation
  - Hiring impact analysis
  - Simple calculations
  - Talent scoring algorithms

- **Path**: `./claudecode_sdk/examples/claude_code_sdk/observability_agent/agent.py`
- **Summary**: DevOps monitoring agent with GitHub integration, CI/CD pipeline analysis, and automated incident response.

### Architecture Documentation
- **Path**: `./claudecode_sdk/examples/claude_code_sdk/research_agent/architecture_diagram.md`
- **Summary**: Visual architecture diagram showing the communication flow and tool integration for the research agent system.

- **Path**: `./claudecode_sdk/examples/claude_code_sdk/chief_of_staff_agent/flow_diagram.md`
- **Summary**: Detailed workflow diagram illustrating the multi-agent coordination and decision-making processes in the chief of staff agent.

- **Path**: `./claudecode_sdk/examples/claude_code_sdk/observability_agent/architecture_diagram.md`
- **Summary**: System architecture visualization for the DevOps monitoring agent, showing GitHub integration and monitoring workflows.

### MCP Server Examples
- **Path**: `./claudecode_sdk/examples/mcp_calculator.py`
- **Summary**: Complete example of creating an MCP server with mathematical tools. Demonstrates server setup, tool definition, and integration patterns.

### Advanced Streaming Examples
- **Path**: `./claudecode_sdk/examples/streaming_mode.py`
- **Summary**: Comprehensive streaming implementation using ClaudeSDKClient showing real-time interaction patterns, message handling with display_message function, and various streaming scenarios.

- **Path**: `./claudecode_sdk/examples/streaming_trio.py`
- **Summary**: Demonstrates async streaming using the Trio library for concurrent message processing and advanced async patterns.

- **Path**: `./claudecode_sdk/examples/streaming_mode_ipython.md`
- **Summary**: Specialized streaming implementation for IPython/Jupyter environments with interactive features and notebook-specific optimizations.

### Utility Libraries
- **Path**: `./claudecode_sdk/examples/claude_code_sdk/utils/agent_visualizer.py`
- **Summary**: Visualization utilities for monitoring agent activity, tool usage, and cost tracking in real-time applications.

### Context & Configuration Files
- **Path**: `./claudecode_sdk/examples/claude_code_sdk/chief_of_staff_agent/CLAUDE.md`
- **Summary**: Complete company context file for TechStart Inc, a 50-person Series A startup. Provides financial metrics ($2.4M ARR, $500K monthly burn), team structure, compensation benchmarks, and strategic priorities.

### Output Reports & Examples
- **Path**: `./claudecode_sdk/examples/claude_code_sdk/chief_of_staff_agent/output_reports/hiring_decision.md`
- **Summary**: Example output demonstrating structured decision-making analysis generated by the chief of staff agent.

- **Path**: `./claudecode_sdk/examples/claude_code_sdk/chief_of_staff_agent/output_reports/Q2_2024_Financial_Forecast.md`
- **Summary**: Sample financial forecasting report showcasing the agent's analytical capabilities and reporting format.

### Hooks & Automation
- **Path**: `./claudecode_sdk/examples/hooks.py`
- **Summary**: Shows how to implement hooks for automated compliance tracking, audit trails, and workflow automation in enterprise environments.

---

## Advanced Features

### Headless Mode Operation
- **Path**: `./claudecode_sdk/headless.md`
- **Summary**: Complete guide to running Claude Code programmatically without interactive UI using the `claude` CLI with `--print` flag. Supports JSON and stream-JSON output formats, session resumption, and MCP configuration.
- **Examples**: SRE incident response bot, automated security review, multi-turn legal assistant

### Streaming Input/Output
- **Path**: `./claudecode_sdk/streaminginput.md`
- **Summary**: Explains streaming input capabilities using AsyncIterable for real-time interaction, dynamic message sending, and bidirectional communication patterns in SDK applications.
- **Examples**: Real-time interaction patterns, streaming JSON input/output

---

## Tools & Built-in Capabilities

### Overview of Available Tools

The SDK provides comprehensive tool access across multiple categories:

#### File & Code Operations
- **File Operations**: Read, Write, Edit, MultiEdit, Glob
- **Code Analysis**: Grep with regex support and context
- **Notebook Support**: NotebookEdit for Jupyter notebook manipulation

#### System & Web Integration
- **System Interaction**: Bash with background execution and output monitoring
- **Web Capabilities**: WebSearch, WebFetch for content analysis
- **MCP Integration**: ListMcpResources, ReadMcpResource for external server communication

#### Workflow & Management
- **Task Management**: TodoWrite for progress tracking
- **Session Management**: Built-in conversation persistence and state restoration

### Detailed Tool Documentation

Comprehensive tool documentation with input/output schemas and usage patterns:

- **Python SDK Reference**: [`./claudecode_sdk/pythonsdk.md`](./claudecode_sdk/pythonsdk.md)
  *Complete API reference including Tool Input/Output Types section*
- **TypeScript SDK Reference**: [`./claudecode_sdk/typescript_sdk.md`](./claudecode_sdk/typescript_sdk.md)
  *Full type definitions and Tool Input/Output Types section*

---

## Best Practices & Workflows

### Architecture Patterns

Key architectural patterns derived from comprehensive examples:

- **Single-Purpose Agents**: Focused tasks (research, analysis)
- **Multi-Agent Orchestration**: Complex workflows requiring specialized expertise
- **Hook-Based Automation**: Compliance and audit requirements
- **Session-Based Persistence**: Long-running tasks and conversation continuity

### Production Considerations

- **Permission Management**: Custom callbacks and restricted tool access
- **Cost Tracking**: Detailed usage monitoring and billing integration
- **Error Handling**: Graceful fallbacks and recovery patterns
- **Security Patterns**: Tool restrictions and audit trails

### Integration Guidelines

- **External Systems**: Integration through MCP servers for APIs, databases, and services
- **Workflow Automation**: Headless mode for scripting and CI/CD pipelines
- **Real-time Interaction**: Streaming input/output for responsive user interfaces
- **Enterprise Features**: Hooks, permissions, and compliance tracking systems

---

## Navigation Summary

This comprehensive index provides structured navigation through the complete Claude Code SDK documentation ecosystem. The organization progresses from foundational concepts to advanced enterprise implementations, with each section building upon previous knowledge while offering practical, production-ready examples for building sophisticated AI agent systems.

### Getting Help
- **File Issues**: Content mismatches and duplications have been identified and marked with warning indicators
- **Missing Content**: The overview.md content mismatch should be prioritized for resolution
- **Version Updates**: This index reflects the current state of documentation and should be updated as content evolves

---

*Last Updated: 2025-09-21 | Documentation Status: Polished and Production-Ready*