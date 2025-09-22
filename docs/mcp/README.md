# Model Context Protocol Documentation

This directory contains the complete Model Context Protocol (MCP) documentation, organized by topic.

## Documentation Structure

### 📚 [Getting Started](./getting-started/)
- [Introduction to MCP](./getting-started/intro.md) - What is the Model Context Protocol?

### 🏗️ [Learn](./learn/)
- [Architecture Overview](./learn/architecture.md) - MCP architecture fundamentals
- [Client Concepts](./learn/client-concepts.md) - Understanding MCP clients
- [Server Concepts](./learn/server-concepts.md) - Understanding MCP servers

### 💻 [Development](./development/)
- [Build an MCP Client](./development/build-client.md) - Create clients that integrate with MCP servers
- [Build an MCP Server](./development/build-server.md) - Create servers for Claude Desktop and other clients
- [Connect to Local Servers](./development/connect-local-servers.md) - Enable file system access and local integrations
- [Connect to Remote Servers](./development/connect-remote-servers.md) - Connect to internet-hosted tools and data sources
- [Roadmap](./development/roadmap.md) - Plans for evolving MCP

### 📋 [Specification](./specification/)
Core protocol specifications and technical details:
- [Specification Overview](./specification/index.md)
- [Architecture](./specification/architecture.md)
- [Schema Reference](./specification/schema.md)
- [Changelog](./specification/changelog.md)

#### Basic Protocol
- [Basic Overview](./specification/basic-overview.md)
- [Lifecycle](./specification/lifecycle.md)
- [Transports](./specification/transports.md)
- [Authorization](./specification/authorization.md)
- [Security Best Practices](./specification/security-best-practices.md)

#### Client Features
- [Roots](./specification/client-roots.md)
- [Sampling](./specification/client-sampling.md)
- [Elicitation](./specification/client-elicitation.md)

#### Server Features
- [Server Overview](./specification/server-overview.md)
- [Prompts](./specification/server-prompts.md)
- [Resources](./specification/server-resources.md)
- [Tools](./specification/server-tools.md)

### 🛠️ [Tools & SDKs](./tools/)
- [SDKs](./tools/sdk.md) - Official SDKs for building with MCP
- [MCP Inspector](./tools/inspector.md) - Testing and debugging MCP servers

### 📖 [Examples](./examples/)
- [Example Clients](./examples/clients.md) - Applications that support MCP integrations
- [Example Servers](./examples/examples.md) - Server implementations and examples

### 👥 [Community](./community/)
- [Communication](./community/communication.md) - Community communication strategy
- [Governance](./community/governance.md) - Governance structure and participation
- [SEP Guidelines](./community/sep-guidelines.md) - Specification Enhancement Proposal guidelines

### ℹ️ [About](./about/)
- [About MCP](./about/index.md) - The open protocol connecting AI applications to context

## Quick Links

- **Official Website**: [modelcontextprotocol.io](https://modelcontextprotocol.io)
- **GitHub Repository**: [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)
- **Specification Version**: 2025-06-18

## Usage in This Project

This project (`simple-harness-ts`) implements an MCP client that can connect to various MCP servers. The implementation can be found in:
- `src/services/MCPClient.ts` - MCP client implementation
- `src/tools/MCPToolAdapter.ts` - Tool adaptation layer
- `mcp-config.json` - MCP server configuration

To connect to an MCP server, configure it in `mcp-config.json` and the harness will automatically discover and make available all tools provided by that server.