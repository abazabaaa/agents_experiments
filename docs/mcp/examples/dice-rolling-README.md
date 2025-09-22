# Dice Rolling MCP Server

A fun and interactive MCP (Model Context Protocol) server that provides dice rolling functionality through a streamable HTTP transport. Perfect for tabletop RPG games, probability demonstrations, or just having fun with random numbers!

## Features

- **Multiple Dice Types**: Supports d4, d6, d8, d10, d12, d20, and d100
- **Batch Rolling**: Roll multiple dice at once (up to 100)
- **Modifiers**: Add positive or negative modifiers to your rolls
- **Statistics**: Get probability distributions and expected values for any dice type
- **Initiative Rolling**: Special RPG-style initiative rolls with character names and dexterity modifiers
- **Fun Descriptions**: Contextual messages based on roll results (critical hits, fails, etc.)
- **Real-time Notifications**: Uses MCP notifications to provide roll-by-roll updates

## Installation

Make sure you have Bun installed, then install dependencies:

```bash
bun install express zod
```

## Running the Server

```bash
bun run examples/dice-rolling-mcp-server.ts
```

The server will start on port 3000 by default. You can change this with the `PORT` environment variable:

```bash
PORT=8080 bun run examples/dice-rolling-mcp-server.ts
```

## Available Tools

### 1. `roll_dice`
Roll one or more dice with optional modifiers.

**Parameters:**
- `dice_type` (required): Type of dice to roll (d4, d6, d8, d10, d12, d20, d100)
- `count` (optional): Number of dice to roll (1-100, default: 1)
- `modifier` (optional): Modifier to add to the total (can be negative)

**Example:**
```json
{
  "name": "roll_dice",
  "arguments": {
    "dice_type": "d20",
    "count": 2,
    "modifier": 3
  }
}
```

### 2. `dice_stats`
Get statistical information about a dice type.

**Parameters:**
- `dice_type` (required): Type of dice to analyze

**Example:**
```json
{
  "name": "dice_stats",
  "arguments": {
    "dice_type": "d12"
  }
}
```

### 3. `roll_initiative`
Roll for initiative in tabletop RPG style.

**Parameters:**
- `character_name` (required): Name of the character rolling
- `dexterity_modifier` (optional): DEX modifier (-5 to +5, default: 0)

**Example:**
```json
{
  "name": "roll_initiative",
  "arguments": {
    "character_name": "Legolas",
    "dexterity_modifier": 4
  }
}
```

## Testing with the Client

Run the included test client:

```bash
# First, make sure the server is running
bun run examples/dice-rolling-mcp-server.ts

# In another terminal, run the client
bun run examples/dice-rolling-client.ts
```

The client demonstrates all available tools and includes an interactive mode for manual dice rolling.

## Testing with cURL

You can test the server directly with cURL:

### Initialize Session
```bash
curl -X POST http://localhost:3000/mcp \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "method": "initialize",
    "params": {
      "protocolVersion": "2025-03-26",
      "capabilities": {},
      "clientInfo": {
        "name": "curl-client",
        "version": "1.0.0"
      }
    },
    "id": 1
  }'
```

Save the session ID from the response headers, then use it for subsequent requests:

### List Tools
```bash
curl -X POST http://localhost:3000/mcp \
  -H "Content-Type: application/json" \
  -H "mcp-session-id: YOUR_SESSION_ID" \
  -d '{
    "jsonrpc": "2.0",
    "method": "tools/list",
    "params": {},
    "id": 2
  }'
```

### Roll Dice
```bash
curl -X POST http://localhost:3000/mcp \
  -H "Content-Type: application/json" \
  -H "mcp-session-id: YOUR_SESSION_ID" \
  -d '{
    "jsonrpc": "2.0",
    "method": "tools/call",
    "params": {
      "name": "roll_dice",
      "arguments": {
        "dice_type": "d20",
        "count": 1
      }
    },
    "id": 3
  }'
```

## MCP Protocol Details

This server implements the MCP protocol with:
- **Transport**: Streamable HTTP with SSE support
- **Protocol Version**: 2025-03-26
- **Capabilities**: Tools and Logging
- **Session Management**: Persistent sessions with in-memory event store
- **Resumability**: Supports reconnection with Last-Event-ID

## Architecture

The server uses:
- Express.js for HTTP handling
- MCP SDK's `McpServer` for protocol implementation
- `StreamableHTTPServerTransport` for client communication
- In-memory session storage for active connections
- Zod for parameter validation

## Error Handling

The server includes comprehensive error handling:
- Invalid dice types return clear error messages
- Session management errors are logged
- Graceful shutdown cleans up all active sessions
- Request validation ensures proper parameter types

## Development

To modify or extend the server:

1. Add new tools using the `server.tool()` method
2. Define parameters using Zod schemas
3. Implement tool logic in the callback function
4. Use `sendNotification` for real-time updates
5. Return results in the CallToolResult format

Example of adding a new tool:
```typescript
server.tool(
  'coin_flip',
  'Flip a coin',
  {
    count: z.number().int().min(1).max(100).default(1)
  },
  async ({ count }): Promise<CallToolResult> => {
    const results = Array(count).fill(0).map(() => 
      Math.random() < 0.5 ? 'Heads' : 'Tails'
    );
    
    return {
      content: [{
        type: 'text',
        text: `Flipped ${count} coin(s): ${results.join(', ')}`
      }]
    };
  }
);
```

Happy rolling! 🎲