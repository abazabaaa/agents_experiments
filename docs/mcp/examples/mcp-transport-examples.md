# MCP Transport Configuration Examples

This document shows how to configure different MCP transport types in your configuration file.

## Stdio Transport (Default)

The stdio transport is used for local MCP servers that communicate via standard input/output.

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "node",
      "args": ["path/to/mcp-server.js"],
      "env": {
        "NODE_ENV": "production"
      },
      "cwd": "/path/to/working/directory"
    }
  }
}
```

Or with explicit transport type:

```json
{
  "mcpServers": {
    "filesystem": {
      "transport": "stdio",
      "command": "node",
      "args": ["path/to/mcp-server.js"]
    }
  }
}
```

## WebSocket Transport

For MCP servers that expose a WebSocket endpoint:

```json
{
  "mcpServers": {
    "remote-server": {
      "transport": "websocket",
      "url": "ws://localhost:8080/mcp"
    }
  }
}
```

Or with secure WebSocket:

```json
{
  "mcpServers": {
    "remote-server": {
      "transport": "websocket",
      "url": "wss://api.example.com/mcp"
    }
  }
}
```

## SSE (Server-Sent Events) Transport

For MCP servers that use Server-Sent Events for real-time communication:

```json
{
  "mcpServers": {
    "sse-server": {
      "transport": "sse",
      "url": "https://api.example.com/mcp/sse"
    }
  }
}
```

With OAuth authentication (requires additional implementation):

```json
{
  "mcpServers": {
    "sse-server": {
      "transport": "sse",
      "url": "https://api.example.com/mcp/sse",
      "authProvider": {
        "clientId": "your-client-id",
        "clientSecret": "your-client-secret",
        "authorizationEndpoint": "https://auth.example.com/authorize",
        "tokenEndpoint": "https://auth.example.com/token",
        "redirectUri": "http://localhost:3000/callback",
        "scopes": ["read", "write"]
      }
    }
  }
}
```

## Streamable HTTP Transport

For MCP servers that implement the Streamable HTTP specification:

```json
{
  "mcpServers": {
    "http-server": {
      "transport": "streamableHttp",
      "url": "https://api.example.com/mcp"
    }
  }
}
```

With session management:

```json
{
  "mcpServers": {
    "http-server": {
      "transport": "streamableHttp",
      "url": "https://api.example.com/mcp",
      "sessionId": "existing-session-id"
    }
  }
}
```

## Multiple Transports

You can mix different transport types in the same configuration:

```json
{
  "mcpServers": {
    "local-filesystem": {
      "transport": "stdio",
      "command": "mcp-filesystem-server"
    },
    "remote-api": {
      "transport": "websocket",
      "url": "wss://api.example.com/mcp"
    },
    "streaming-service": {
      "transport": "sse",
      "url": "https://stream.example.com/mcp"
    }
  }
}
```

## Environment Variables

All transport types support environment variables:

```json
{
  "mcpServers": {
    "server-with-env": {
      "transport": "websocket",
      "url": "ws://localhost:8080/mcp",
      "env": {
        "API_KEY": "your-api-key",
        "DEBUG": "true"
      }
    }
  }
}
```

## Notes

- **Authentication**: OAuth authentication for SSE and Streamable HTTP transports requires implementing an `OAuthClientProvider`. This is currently logged as a warning if auth configuration is provided.
- **URLs**: WebSocket URLs must start with `ws://` or `wss://`, while HTTP-based transports use `http://` or `https://`.
- **Backward Compatibility**: Configurations without a `transport` field are treated as stdio transports for backward compatibility.