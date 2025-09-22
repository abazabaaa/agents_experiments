# FastMCP Documentation Index

## Overview

The Model Context Protocol (MCP) is an open protocol that enables seamless integration between LLM applications and external data sources and tools. It provides a secure, standardized way to connect AI systems to context through a client-server architecture, like a "USB-C port for AI applications."

MCP enables AI applications to:
- Access real-time data from external systems
- Execute actions through standardized tools
- Use templated prompts for consistent interactions
- Maintain secure connections with proper authorization

## Table of Contents

- [Quick Navigation](#quick-navigation)
- [About & Overview](#about--overview)
- [Getting Started](#getting-started)
- [Learning MCP](#learning-mcp)
- [Quickstart Guides](#quickstart-guides)
- [Protocol Specification](#protocol-specification)
- [Community & Development](#community--development)
- [Reference](#reference)
- [File Organization Summary](#file-organization-summary)

---

## Quick Navigation

### 🚀 For New Users
*Start here to understand MCP and get up and running quickly*

1. [About MCP](#about--overview) - What is MCP and why it matters
2. [Getting Started](#getting-started) - Core concepts and getting started
3. [User Quickstart](#quickstart-guides) - Use existing MCP servers immediately

### 🔨 For Developers
*Build your own MCP servers and clients*

1. [Architecture Overview](#learning-mcp) - Understand how MCP works
2. [Server Quickstart](#quickstart-guides) - Build your first server
3. [Client Quickstart](#quickstart-guides) - Create client applications
4. [SDKs](#reference) - Official development kits

### 📄 For Protocol Engineers
*Deep dive into the specification*

1. [Specification Overview](#protocol-specification) - Complete protocol documentation
2. [Architecture Details](#protocol-specification) - System design and message flow
3. [Transport Layer](#protocol-specification) - Communication mechanisms

---

## About & Overview

### Main Introduction
- **Path**: `../fastmcp/about/index.md`
- **Summary**: Main landing page explaining MCP as "the open protocol that connects AI applications to the systems where context lives." Details the 3-step process (choose MCP servers, connect your AI application, work with context) and showcases the ecosystem with 9 official SDKs and 1000+ available servers.

---

[⬆ Back to Top](#fastmcp-documentation-index)

## Getting Started

### Core Introduction
- **Path**: `../fastmcp/docs/getting-started/intro.md`
- **Summary**: Essential introduction comparing MCP to a "USB-C port for AI applications." Provides four distinct learning paths: understand concepts, use MCP, build servers, and build clients. Emphasizes MCP as a standardized protocol for connecting `LLMs` to data sources and tools.

---

[⬆ Back to Top](#fastmcp-documentation-index)

## Learning MCP

### Architecture & Concepts
- **Path**: `../fastmcp/docs/learn/architecture.md`
- **Summary**: Technical architecture overview explaining MCP's scope (specification, SDKs, dev tools, reference implementations) and core concepts. Details the three participants (host, client, server) with one-to-one connection model, and explains the two-layer architecture (data layer with `JSON-RPC`, transport layer for communication).

- **Path**: `../fastmcp/docs/learn/client-concepts.md`
- **Summary**: Explains client-side MCP concepts and capabilities that servers can leverage, including sampling (`LLM` completions), elicitation (user input), and logging. Shows how servers can build richer interactions through client features.

- **Path**: `../fastmcp/docs/learn/server-concepts.md`
- **Summary**: Details server-side MCP primitives: tools (executable functions), resources (contextual data), and prompts (interaction templates). Covers discovery mechanisms and how servers expose functionality to AI applications.

### SDK Information
- **Path**: `../fastmcp/docs/sdk.md`
- **Summary**: Official SDKs page listing 9 language implementations (TypeScript, Python, Go, Kotlin, Swift, Java, C#, Ruby, Rust). Emphasizes that all SDKs provide the same core functionality: creating servers with tools/resources/prompts, building clients, supporting local/remote transports, and ensuring protocol compliance.

### Tutorials
- **Path**: `../fastmcp/docs/tutorials/use-remote-mcp-server.md`
- **Summary**: Tutorial for using remote MCP servers, demonstrating connection setup, configuration patterns, and practical usage of existing server integrations. Focuses on leveraging pre-built servers for immediate functionality.

---

[⬆ Back to Top](#fastmcp-documentation-index)

## Quickstart Guides

### For End Users
- **Path**: `../fastmcp/quickstart/user.md`
- **Summary**: Guide for connecting local MCP servers to Claude Desktop (and other MCP clients), demonstrating filesystem integration. Details prerequisites (Claude Desktop, Node.js), server installation via `npx`, `JSON` configuration in `claude_desktop_config.json`, and security model requiring explicit user approval for all server actions.

### For Server Developers
- **Path**: `../fastmcp/quickstart/server.md`
- **Summary**: Step-by-step tutorial for building a weather server with `get_alerts` and `get_forecast` tools. Provides implementations in multiple languages (Python, TypeScript, Go) with detailed logging guidance for `STDIO` servers (must use `stderr`, not `stdout`). Demonstrates tool creation, server setup, and testing with Claude Desktop as the MCP host.

### For Client Developers
- **Path**: `../fastmcp/quickstart/client.md`
- **Summary**: Guide for building MCP client applications that connect to MCP servers. Covers client architecture, connection management, capability negotiation, and implementing support for tools, resources, and prompts in your applications.

---

[⬆ Back to Top](#fastmcp-documentation-index)

## Protocol Specification

### Core Specification (2025-06-18)
- **Path**: `../fastmcp/specification/2025-06-18/index.md`
- **Summary**: Authoritative protocol specification defining MCP requirements for clients and servers. Covers security principles, key capabilities (resources, tools, prompts, sampling), and provides links to detailed component specifications.

- **Path**: `../fastmcp/specification/2025-06-18/schema.md`
- **Summary**: Complete protocol schema definition with TypeScript source of truth and generated `JSON Schema`. Defines message structures, data types, and protocol-level metadata including reserved `_meta` field conventions.

- **Path**: `../fastmcp/specification/2025-06-18/changelog.md`
- **Summary**: Detailed changelog documenting all changes, additions, and improvements made in the 2025-06-18 protocol revision. Essential for understanding version differences and migration requirements.

### Architecture
- **Path**: `../fastmcp/specification/2025-06-18/architecture/index.md`
- **Summary**: Technical architecture specification defining system components, participant roles, data/transport layer separation, and core protocol primitives. Provides detailed message flow examples and protocol interaction patterns.

### Basic Protocol Components
- **Path**: `../fastmcp/specification/2025-06-18/basic/index.md`
- **Summary**: Foundation protocol specification covering `JSON-RPC` 2.0 message types (requests, responses, notifications), authentication framework, and schema definitions. Establishes core communication patterns and metadata conventions.

- **Path**: `../fastmcp/specification/2025-06-18/basic/lifecycle.md`
- **Summary**: Protocol lifecycle management specification covering connection initialization, capability negotiation, and session control. Defines handshake process and version negotiation between clients and servers.

- **Path**: `../fastmcp/specification/2025-06-18/basic/authorization.md`
- **Summary**: Authorization specification for `HTTP`-based transports using `OAuth` 2.1 draft (draft-ietf-oauth-v2-1-13). Defines MCP servers as `OAuth` resource servers, clients as `OAuth` clients, with authorization server discovery via `RFC8414`/`RFC9728`, and Dynamic Client Registration support (`RFC7591`). `STDIO` transports retrieve credentials from environment variables instead.

- **Path**: `../fastmcp/specification/2025-06-18/basic/transports.md`
- **Summary**: Transport specification defining two mechanisms: `stdio` (subprocess communication via `stdin`/`stdout` with newline-delimited `JSON-RPC`, `stderr` for logging) and Streamable `HTTP` (`HTTP` POST/GET with optional `SSE` support, includes security warnings about DNS rebinding). Specifies `UTF-8` encoding requirements, message delimiting, and custom transport extensibility.

- **Path**: `../fastmcp/specification/2025-06-18/basic/security_best_practices.md`
- **Summary**: Comprehensive security guidelines for MCP implementations covering user consent, data privacy, tool safety, and `LLM` sampling controls. Provides implementation guidelines for building secure MCP applications.

### Basic Utilities
- **Path**: `../fastmcp/specification/2025-06-18/basic/utilities/cancellation.md`
- **Summary**: Specification for request cancellation mechanism allowing clients and servers to abort long-running operations. Defines cancellation message format and proper handling of cancelled requests.

- **Path**: `../fastmcp/specification/2025-06-18/basic/utilities/ping.md`
- **Summary**: Simple ping/pong mechanism for connection health monitoring and keepalive functionality. Enables clients and servers to verify connection status and prevent timeout disconnections.

- **Path**: `../fastmcp/specification/2025-06-18/basic/utilities/progress.md`
- **Summary**: Progress reporting specification for long-running operations. Allows servers to provide real-time progress updates to clients during tool execution or resource processing operations.

### Server Features
- **Path**: `../fastmcp/specification/2025-06-18/server/index.md`
- **Summary**: Overview of server-side MCP capabilities including tools (executable functions), resources (contextual data), and prompts (interaction templates). Defines how servers expose functionality to clients and handle discovery patterns.

- **Path**: `../fastmcp/specification/2025-06-18/server/tools.md`
- **Summary**: Tools specification defining how servers expose executable functions to language models. Covers model-controlled tool discovery and invocation, `JSON-RPC` message patterns for `tools/list` and `tools/call`, input/output schemas with `JSON Schema` validation, pagination support, and critical security requirements mandating human-in-the-loop confirmation.

- **Path**: `../fastmcp/specification/2025-06-18/server/resources.md`
- **Summary**: Resources specification defining how servers expose data via `URI`-identified resources. Covers application-driven interaction models, resource discovery with `resources/list`, reading with `resources/read`, subscribe/listChanged capabilities for dynamic updates, and support for text/binary content with annotations.

- **Path**: `../fastmcp/specification/2025-06-18/server/prompts.md`
- **Summary**: Prompts specification for user-controlled message templates. Designed for explicit user selection (e.g., slash commands), supports prompt discovery via `prompts/list`, template rendering with custom arguments via `prompts/get`, and embedded resource references for contextual interactions.

### Server Utilities
- **Path**: `../fastmcp/specification/2025-06-18/server/utilities/completion.md`
- **Summary**: Completion utility enabling servers to request text completions from clients. Supports context-aware suggestions, partial text completion, and auto-completion features for enhanced server capabilities.

- **Path**: `../fastmcp/specification/2025-06-18/server/utilities/logging.md`
- **Summary**: Logging specification for servers to send structured log messages to clients via logging/message notifications. Defines log levels (debug, info, warn, error), message structure, and debugging support for server development.

- **Path**: `../fastmcp/specification/2025-06-18/server/utilities/pagination.md`
- **Summary**: Pagination specification for handling large result sets using cursor-based patterns. Applies to `resources/list`, `tools/list`, `prompts/list`, and other enumerable responses, ensuring consistent handling of large datasets across MCP operations.

### Client Features
- **Path**: `../fastmcp/specification/2025-06-18/client/sampling.md`
- **Summary**: Sampling specification enabling servers to request `LLM` completions from clients without server `API` keys. Supports nested agentic behaviors within MCP server features, multi-modal messages (text, audio, image), model preferences with intelligence/speed priorities, and emphasizes human-in-the-loop security for all sampling requests.

- **Path**: `../fastmcp/specification/2025-06-18/client/roots.md`
- **Summary**: Roots specification allowing servers to query client filesystem boundaries via `roots/list`. Enables servers to discover available root directories, understand operational context, and work within client-defined filesystem constraints.

- **Path**: `../fastmcp/specification/2025-06-18/client/elicitation.md`
- **Summary**: Elicitation specification enabling servers to request user input via client `UI`. Supports interactive workflows through `elicitation/createMessage`, confirmation dialogs, user input gathering, and maintaining human-in-the-loop control for sensitive operations.

### Versioning
- **Path**: `../fastmcp/specification/versioning.md`
- **Summary**: Versioning specification using YYYY-MM-DD format (current: 2025-06-18) for backwards-incompatible changes. Defines three revision states (draft, current, final), explains that backwards-compatible changes don't increment version, and details version negotiation during connection initialization.

---

[⬆ Back to Top](#fastmcp-documentation-index)

## Community & Development

### Community Guidelines
- **Path**: `../fastmcp/community/communication.md`
- **Summary**: Community communication guidelines and official channels for MCP participation. Details Discord server usage, contribution etiquette, and engagement expectations for productive collaboration within the MCP ecosystem.

- **Path**: `../fastmcp/community/governance.md`
- **Summary**: Governance model with four-tier hierarchy: contributors, maintainers, core maintainers, and two lead maintainers (Justin Spahr-Summers and David Soria Parra as BDFLs). Describes individual-not-company membership, Discord-based coordination, bi-weekly meetings, and project/working group organization principles.

- **Path**: `../fastmcp/community/sep-guidelines.md`
- **Summary**: Guidelines for Specification Enhancement Proposals (`SEPs`) to evolve MCP protocol. Details proposal submission process, required sponsorship from maintainers, review procedures, and community participation standards for protocol improvements.

### Development Roadmap
- **Path**: `../fastmcp/development/roadmap.md`
- **Summary**: Six-month development roadmap (last updated 2025-07-22) focusing on agents (async operations with resilient reconnection), authentication improvements (enterprise `SSO`, fine-grained auth, `DCR` alternatives), validation tools (reference implementations, test suites), MCP Registry `API` for server discovery, and multimodality support including video and streaming.

---

[⬆ Back to Top](#fastmcp-documentation-index)

## Reference

### Examples & Implementations
- **Path**: `../fastmcp/examples.md`
- **Summary**: Catalog of MCP server examples organized into current reference servers (Everything, Fetch, Filesystem, Git, Memory, Sequential Thinking, Time), archived servers (moved to servers-archived repo for historical reference), official platform integrations, and community implementations. Includes `npx` (TypeScript) and `uvx` (Python) usage instructions for quick deployment.

### Clients
- **Path**: `../fastmcp/clients.md`
- **Summary**: Directory of MCP client applications capable of connecting to MCP servers. Includes official clients like Claude Desktop, third-party implementations, and guidance for developers building new MCP-compatible client applications.

### FAQ
- **Path**: `../fastmcp/faqs.md`
- **Summary**: FAQ explaining MCP's core value as a standardized protocol for `AI` context integration. Addresses common questions about benefits for users and developers, how MCP functions as a "universal adapter," and its role in the `AI` ecosystem.

---

[⬆ Back to Top](#fastmcp-documentation-index)

## File Organization Summary

**Total Files**: 40 markdown files

| Category | Files | Description |
|----------|-------|-------------|
| **About** | 1 | Project overview and landing content |
| **Documentation** | 6 | Getting started, learning materials, and tutorials |
| **Quickstart** | 3 | User, server, and client quickstart guides |
| **Specification** | 26 | Complete protocol specification with detailed technical documentation |
| **Community** | 3 | Governance, communication, and contribution guidelines |
| **Reference** | 3 | Examples, clients, and FAQ |

**Navigation Notes**:
- All file paths use relative notation (`../fastmcp/`) from the indexes folder location
- Original directory structure is preserved for accurate navigation
- The specification section represents the most comprehensive portion, reflecting MCP's status as a formal protocol with detailed technical requirements

---

*This index provides comprehensive navigation for the FastMCP documentation. For the latest updates and additional resources, refer to the individual documentation files.*