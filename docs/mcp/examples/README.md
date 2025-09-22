# MCP Examples

This directory contains examples of MCP (Model Context Protocol) servers and configurations.

## Available Examples

### 1. Dice Rolling Server (`dice-rolling-server.ts`)
A simple MCP server that demonstrates:
- Tool implementation (roll_dice)
- Stdio transport
- TypeScript implementation

See [dice-rolling-README.md](dice-rolling-README.md) for detailed setup instructions.

### 2. Minimal Dice Server (`minimal-dice-server.ts`)
A stripped-down version showing the bare minimum needed for an MCP server.

### 3. Dice Rolling Client (`dice-rolling-client.ts`)
Example client code showing how to connect to an MCP server.

### 4. Transport Examples (`mcp-transport-examples.md`)
Comprehensive guide to different MCP transport options:
- Stdio (default)
- WebSocket
- SSE (Server-Sent Events)
- Streamable HTTP

### 5. Configuration Examples (`mcp-configs/`)
Ready-to-use MCP configuration files for different transport types.

## Quick Start

1. **Run the dice server:**
   ```bash
   bun run dice-rolling-server.ts
   ```

2. **Use it with the agent:**
   ```bash
   # Create config
   cat > mcp-config.json << EOF
   {
     "servers": {
       "dice": {
         "command": "bun",
         "args": ["run", "examples/dice-rolling-server.ts"]
       }
     }
   }
   EOF

   # Run agent with dice server
   bun run dev "Roll 3d6 for me" --mcp-config mcp-config.json
   ```

## Creating Your Own MCP Server

Use the dice server as a template. Key requirements:
1. Implement the MCP protocol over your chosen transport
2. Define tools with proper schemas
3. Handle initialize/list_tools/call_tool requests
4. Return responses in the correct format

See the MCP SDK documentation for more details.