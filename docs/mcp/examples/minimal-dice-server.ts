#!/usr/bin/env bun
/**
 * Minimal Dice Rolling MCP Server using Bun's built-in HTTP server
 *
 * This is a simplified version that uses Bun.serve() instead of Express.
 * It demonstrates the core MCP server concepts with minimal dependencies.
 *
 * Run with: bun run examples/minimal-dice-server.ts
 */

import { randomUUID } from 'node:crypto'
import { z } from 'zod'
import { McpServer } from '../typescript-sdk/src/server/mcp'
import { StreamableHTTPServerTransport } from '../typescript-sdk/src/server/streamableHttp'
import { CallToolResult, isInitializeRequest } from '../typescript-sdk/src/types'

// Simple dice rolling function
const rollDice = (sides: number): number => Math.floor(Math.random() * sides) + 1

// Create the MCP server
const createServer = () => {
  const server = new McpServer(
    {
      name: 'minimal-dice-server',
      version: '1.0.0',
    },
    {
      capabilities: {
        tools: {},
        logging: {},
      },
    }
  )

  // Register a simple dice rolling tool
  server.tool(
    'roll',
    'Roll a dice with the specified number of sides',
    {
      sides: z.number().int().min(2).max(1000).default(6).describe('Number of sides on the dice'),
    },
    async ({ sides }): Promise<CallToolResult> => {
      const result = rollDice(sides)

      return {
        content: [
          {
            type: 'text',
            text: `🎲 Rolled a d${sides}: **${result}**`,
          },
        ],
      }
    }
  )

  // Register a batch rolling tool
  server.tool(
    'roll_multiple',
    'Roll multiple dice at once',
    {
      sides: z.number().int().min(2).max(1000).default(6),
      count: z.number().int().min(1).max(20).default(1),
    },
    async ({ sides, count }): Promise<CallToolResult> => {
      const rolls = Array(count)
        .fill(0)
        .map(() => rollDice(sides))
      const total = rolls.reduce((sum, roll) => sum + roll, 0)

      return {
        content: [
          {
            type: 'text',
            text: `🎲 Rolled ${count}d${sides}\nRolls: [${rolls.join(', ')}]\nTotal: **${total}**`,
          },
        ],
      }
    }
  )

  return server
}

// Session storage
const sessions = new Map<string, StreamableHTTPServerTransport>()

// Simple event store for resumability
class SimpleEventStore {
  private events = new Map<string, Array<{ id: string; message: any }>>()

  async storeEvent(streamId: string, message: any): Promise<string> {
    const eventId = `${Date.now()}_${Math.random().toString(36).substr(2, 9)}`
    const streamEvents = this.events.get(streamId) || []
    streamEvents.push({ id: eventId, message })
    this.events.set(streamId, streamEvents)
    return eventId
  }

  async replayEventsAfter(
    lastEventId: string,
    { send }: { send: (eventId: string, message: any) => Promise<void> }
  ): Promise<string> {
    // Find the stream containing this event
    for (const [streamId, events] of this.events.entries()) {
      const eventIndex = events.findIndex((e) => e.id === lastEventId)
      if (eventIndex !== -1) {
        // Replay events after this one
        for (let i = eventIndex + 1; i < events.length; i++) {
          await send(events[i].id, events[i].message)
        }
        return events[events.length - 1]?.id || lastEventId
      }
    }
    return ''
  }
}

// Create Bun HTTP server
const server = Bun.serve({
  port: 3000,
  async fetch(req) {
    const url = new URL(req.url)

    // Only handle /mcp endpoint
    if (url.pathname !== '/mcp') {
      return new Response('Not Found', { status: 404 })
    }

    const method = req.method
    const sessionId = req.headers.get('mcp-session-id')

    try {
      // Handle POST requests
      if (method === 'POST') {
        const body = await req.json()

        let transport: StreamableHTTPServerTransport

        if (sessionId && sessions.has(sessionId)) {
          // Existing session
          transport = sessions.get(sessionId)!
        } else if (!sessionId && isInitializeRequest(body)) {
          // New session
          transport = new StreamableHTTPServerTransport({
            sessionIdGenerator: () => randomUUID(),
            eventStore: new SimpleEventStore(),
            onsessioninitialized: (sid) => {
              console.log(`New session: ${sid}`)
              sessions.set(sid, transport)
            },
          })

          transport.onclose = () => {
            const sid = transport.sessionId
            if (sid && sessions.has(sid)) {
              console.log(`Session closed: ${sid}`)
              sessions.delete(sid)
            }
          }

          // Connect to MCP server
          const mcpServer = createServer()
          await mcpServer.connect(transport)
        } else {
          return new Response(
            JSON.stringify({
              jsonrpc: '2.0',
              error: {
                code: -32000,
                message: 'Invalid request: missing session ID or not an initialize request',
              },
              id: null,
            }),
            {
              status: 400,
              headers: { 'Content-Type': 'application/json' },
            }
          )
        }

        // Create a mock Express-like request/response
        const mockReq = {
          method: 'POST',
          headers: Object.fromEntries(req.headers.entries()),
          body,
        }

        let responseData: any
        let responseHeaders: Record<string, string> = {}
        let responseStatus = 200

        const mockRes = {
          status(code: number) {
            responseStatus = code
            return this
          },
          set(name: string, value: string) {
            responseHeaders[name] = value
          },
          setHeader(name: string, value: string) {
            responseHeaders[name] = value
          },
          json(data: any) {
            responseData = data
            responseHeaders['Content-Type'] = 'application/json'
          },
          write(chunk: any) {
            // For streaming responses
            if (!responseData) responseData = ''
            responseData += chunk
          },
          end() {
            // Response complete
          },
        }

        await transport.handleRequest(mockReq as any, mockRes as any, body)

        return new Response(
          typeof responseData === 'string' ? responseData : JSON.stringify(responseData),
          {
            status: responseStatus,
            headers: responseHeaders,
          }
        )
      }

      // Handle GET requests (SSE)
      if (method === 'GET' && sessionId && sessions.has(sessionId)) {
        const transport = sessions.get(sessionId)!

        // Create SSE response
        const stream = new ReadableStream({
          async start(controller) {
            const mockReq = {
              method: 'GET',
              headers: Object.fromEntries(req.headers.entries()),
            }

            const mockRes = {
              writeHead(status: number, headers: Record<string, string>) {
                // Headers are set in the Response constructor
              },
              write(data: string) {
                controller.enqueue(new TextEncoder().encode(data))
              },
              end() {
                controller.close()
              },
            }

            await transport.handleRequest(mockReq as any, mockRes as any)
          },
        })

        return new Response(stream, {
          headers: {
            'Content-Type': 'text/event-stream',
            'Cache-Control': 'no-cache',
            Connection: 'keep-alive',
          },
        })
      }

      // Handle DELETE requests
      if (method === 'DELETE' && sessionId && sessions.has(sessionId)) {
        const transport = sessions.get(sessionId)!
        await transport.close()
        sessions.delete(sessionId)
        return new Response('', { status: 204 })
      }

      return new Response('Method Not Allowed', { status: 405 })
    } catch (error) {
      console.error('Error:', error)
      return new Response(
        JSON.stringify({
          jsonrpc: '2.0',
          error: {
            code: -32603,
            message: 'Internal server error',
          },
          id: null,
        }),
        {
          status: 500,
          headers: { 'Content-Type': 'application/json' },
        }
      )
    }
  },
})

console.log(`🎲 Minimal Dice Server running at http://localhost:${server.port}/mcp`)
console.log('\nAvailable tools:')
console.log('  • roll - Roll a single dice')
console.log('  • roll_multiple - Roll multiple dice')
console.log('\nTest with:')
console.log('curl -X POST http://localhost:3000/mcp \\')
console.log('  -H "Content-Type: application/json" \\')
console.log(
  '  -d \'{"jsonrpc": "2.0", "method": "initialize", "params": {"protocolVersion": "2025-03-26", "capabilities": {}, "clientInfo": {"name": "test", "version": "1.0"}}, "id": 1}\''
)

// Graceful shutdown
process.on('SIGINT', () => {
  console.log('\nShutting down...')
  for (const [sid, transport] of sessions) {
    transport.close()
  }
  sessions.clear()
  server.stop()
  process.exit(0)
})
