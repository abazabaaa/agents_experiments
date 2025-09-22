# Documentation Master Index

This is the central documentation index for all project documentation. Each sub-index provides comprehensive navigation for specific libraries and tools.

## 📚 Documentation Categories

### AI SDKs & Agent Frameworks
- **[Claude Code SDK Index](./claudecode-sdk-index.md)**
  - Comprehensive SDK for building AI agents with Claude
  - Python and TypeScript implementations with async support
  - Enterprise agent examples, MCP integration, and custom tools
  - Session management, permissions, and production deployment guides

- **[Anthropic API Index](./anthropic-api-index.md)**
  - Complete reference for Claude API endpoints and services
  - Core Messages API, Admin API, batch processing, and file handling
  - Cloud platform integrations (AWS Bedrock, Google Vertex AI)
  - SDKs in 7+ languages and developer tools

- **[Anthropic Documentation Index](./anthropic-docs-index.md)**
  - Conceptual guides and best practices for building with Claude
  - Prompt engineering, tool use, and agent development
  - Claude Code CLI documentation and SDK guides
  - Testing, evaluation, and production deployment strategies

- **[Anthropic Examples Index](./anthropic-examples-index.md)**
  - Production-ready applications and code examples
  - Agent patterns, tool use, and multimodal capabilities
  - Skill-specific implementations (RAG, classification, SQL)
  - Interactive notebooks and evaluation frameworks

- **[OpenAI Responses API Index](./openai-responses-index.md)**
  - Complete documentation for the new OpenAI Responses API
  - Includes guides for reasoning models, streaming, function calling, and conversation management
  - Code examples and best practices

- **[OpenAI Agents SDK Index](./openai-agents-sdk-index.md)**
  - Documentation for the OpenAI Agents SDK
  - Agent development guides, models reference, and tracing
  - Examples and API reference

### Async Programming
- **[Trio & Trio-Asyncio Index](./trio-index.md)**
  - Comprehensive Trio async/await documentation
  - Trio-asyncio compatibility layer documentation
  - Structured concurrency patterns and examples

### Interactive Notebooks
- **[Marimo Index](./marimo-index.md)**
  - Comprehensive documentation for reactive Python notebooks
  - 700+ documentation files and example notebooks
  - Interactive UI components, SQL support, and AI integrations
  - Deployment guides and framework integrations

### Development Tools
- **[Development Tools Index](./tools-index.md)**
  - **UV**: Modern Python package installer and resolver
  - **Ruff**: Fast Python linter and formatter
  - **Ty**: Python type checking documentation

### Parsing & Protocols
- **[Lark Parser Index](./lark-index.md)**
  - Complete Lark parsing library documentation
  - Grammar reference, tutorials, and extensive examples
  - 80+ documentation files including LLGuidance extensions for language models

- **[FastMCP Index](./fastmcp-index.md)**
  - Model Context Protocol (MCP) comprehensive documentation
  - Protocol specification, architecture, and implementation guides
  - 40 documentation files covering clients, servers, and protocol details

## 🗂️ Documentation Structure

```
docs/
├── indexes/              # All index files
│   ├── INDEX.md         # This file
│   ├── claudecode-sdk-index.md
│   ├── anthropic-api-index.md
│   ├── anthropic-docs-index.md
│   ├── anthropic-examples-index.md
│   ├── openai-responses-index.md
│   ├── openai-agents-sdk-index.md
│   ├── trio-index.md
│   ├── marimo-index.md
│   ├── tools-index.md
│   ├── lark-index.md
│   └── fastmcp-index.md
│
├── anthropic/            # Anthropic Claude documentation
│   ├── api/             # API reference documentation
│   ├── docs/            # Conceptual guides and tutorials
│   └── examples/        # Code examples and applications
├── claudecode_sdk/        # Claude Code SDK docs
├── openai_responses_api/  # OpenAI Responses API docs
├── openai-agents-sdk/     # OpenAI Agents SDK docs
├── trio/                  # Trio documentation
├── trio-asyncio/          # Trio-asyncio documentation
├── marimo/               # Marimo documentation
├── uv_docs/              # UV package manager docs
├── ruff/                 # Ruff linter docs
├── ty/                   # Type checking docs
├── fastmcp/              # FastMCP docs
└── larkdocs/             # Lark parser docs
```

## 🔍 Quick Navigation

- For **Claude API reference**, see the Anthropic API index
- For **Claude concepts and guides**, see the Anthropic Documentation index
- For **Claude code examples**, see the Anthropic Examples index
- For **AI agent development**, start with the Claude Code SDK or OpenAI indexes
- For **reactive notebooks**, see the Marimo index
- For **async programming**, see the Trio index
- For **development workflow**, check the tools index
- For **parsing and DSLs**, see the Lark index
- For **AI protocol integration**, see the FastMCP index
- For **specific libraries**, navigate directly to their folders

## 📝 Contributing

When adding new documentation:
1. Place documentation files in the appropriate subdirectory
2. Update the relevant index file in `docs/indexes/`
3. If creating a new category, add a new index and link it here