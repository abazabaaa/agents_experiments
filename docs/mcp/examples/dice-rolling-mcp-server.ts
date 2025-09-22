#!/usr/bin/env bun
/**
 * Dice Rolling MCP Server
 *
 * A fun MCP server that implements dice rolling functionality with streamable HTTP transport.
 * Supports various dice types (d4, d6, d8, d10, d12, d20, d100) and multiple rolls.
 *
 * Run with: bun run examples/dice-rolling-mcp-server.ts
 *
 * Test with curl:
 * curl -X POST http://localhost:3000/mcp \
 *   -H "Content-Type: application/json" \
 *   -d '{"jsonrpc": "2.0", "method": "initialize", "params": {"protocolVersion": "2025-03-26", "capabilities": {}, "clientInfo": {"name": "test-client", "version": "1.0.0"}}, "id": 1}'
 */

import express, { Request, Response } from 'express'
import { randomUUID } from 'node:crypto'
import { z } from 'zod'
import { McpServer } from '../typescript-sdk/src/server/mcp'
import { StreamableHTTPServerTransport } from '../typescript-sdk/src/server/streamableHttp'
import { CallToolResult, isInitializeRequest } from '../typescript-sdk/src/types'
import { InMemoryEventStore } from '../typescript-sdk/src/examples/shared/inMemoryEventStore'

// Dice types we support
const DICE_TYPES = ['d4', 'd6', 'd8', 'd10', 'd12', 'd20', 'd100'] as const
type DiceType = (typeof DICE_TYPES)[number]

// Fun descriptors for different roll results
const ROLL_DESCRIPTORS = {
  critical: ['💥 CRITICAL HIT!', '🎯 PERFECT ROLL!', '⚡ LEGENDARY!', '🌟 INCREDIBLE!'],
  high: ['🔥 Great roll!', '✨ Excellent!', '👍 Very nice!', '🎉 Impressive!'],
  medium: ['👌 Not bad!', '😊 Decent roll!', '🎲 Fair result!', '✅ Solid!'],
  low: ['😅 Could be better...', '🤷 Meh...', '😐 Average...', '💭 Hmm...'],
  criticalFail: ['💀 CRITICAL FAIL!', '😱 Disaster!', '🙈 Oh no!', '💔 Terrible luck!'],
}

// Get a random element from an array
const randomFrom = <T>(arr: T[]): T => arr[Math.floor(Math.random() * arr.length)]

// Roll a single die
const rollDie = (sides: number): number => Math.floor(Math.random() * sides) + 1

// Get descriptor based on roll value and die type
const getDescriptor = (value: number, sides: number): string => {
  const percentage = value / sides

  if (value === sides) return randomFrom(ROLL_DESCRIPTORS.critical)
  if (value === 1) return randomFrom(ROLL_DESCRIPTORS.criticalFail)
  if (percentage >= 0.8) return randomFrom(ROLL_DESCRIPTORS.high)
  if (percentage >= 0.5) return randomFrom(ROLL_DESCRIPTORS.medium)
  return randomFrom(ROLL_DESCRIPTORS.low)
}

// Create the MCP server instance
const createDiceServer = () => {
  const server = new McpServer(
    {
      name: 'dice-rolling-server',
      version: '1.0.0',
    },
    {
      capabilities: {
        tools: {},
        logging: {},
      },
    }
  )

  // Register the main dice rolling tool
  server.tool(
    'roll_dice',
    'Roll one or more dice of various types (d4, d6, d8, d10, d12, d20, d100)',
    {
      dice_type: z.enum(DICE_TYPES).describe('Type of dice to roll'),
      count: z.number().int().min(1).max(100).default(1).describe('Number of dice to roll'),
      modifier: z
        .number()
        .int()
        .optional()
        .describe('Modifier to add to the total (can be negative)'),
    },
    async ({ dice_type, count, modifier }, { sendNotification }): Promise<CallToolResult> => {
      const sides = parseInt(dice_type.substring(1))
      const rolls: number[] = []

      // Send initial notification
      await sendNotification({
        method: 'notifications/message',
        params: {
          level: 'info',
          data: `🎲 Rolling ${count} ${dice_type}${modifier ? ` with ${modifier > 0 ? '+' : ''}${modifier} modifier` : ''}...`,
        },
      })

      // Roll each die with a small delay for dramatic effect
      for (let i = 0; i < count; i++) {
        const roll = rollDie(sides)
        rolls.push(roll)

        // Add suspense with notifications for each roll
        if (count > 1) {
          await new Promise((resolve) => setTimeout(resolve, 300))
          await sendNotification({
            method: 'notifications/message',
            params: {
              level: 'debug',
              data: `Die ${i + 1}: ${roll}`,
            },
          })
        }
      }

      const total = rolls.reduce((sum, roll) => sum + roll, 0)
      const modifiedTotal = total + (modifier || 0)

      // Build result message
      let resultText = ''

      if (count === 1) {
        const descriptor = getDescriptor(rolls[0], sides)
        resultText = `${descriptor}\n\nYou rolled a **${rolls[0]}** on a ${dice_type}!`
        if (modifier) {
          resultText += `\nWith modifier: ${rolls[0]} ${modifier > 0 ? '+' : ''}${modifier} = **${modifiedTotal}**`
        }
      } else {
        resultText = `🎲 **Roll Results** 🎲\n\n`
        resultText += `Dice: ${count}${dice_type}\n`
        resultText += `Rolls: [${rolls.join(', ')}]\n`
        resultText += `Sum: ${total}\n`

        if (modifier) {
          resultText += `Modifier: ${modifier > 0 ? '+' : ''}${modifier}\n`
          resultText += `**Total: ${modifiedTotal}**\n`
        } else {
          resultText += `**Total: ${total}**\n`
        }

        // Add some flavor text for multiple dice
        const average = total / count
        const expectedAverage = (sides + 1) / 2
        if (average > expectedAverage * 1.2) {
          resultText += `\n✨ The dice favor you today!`
        } else if (average < expectedAverage * 0.8) {
          resultText += `\n😅 Better luck next time!`
        }
      }

      return {
        content: [
          {
            type: 'text',
            text: resultText,
          },
        ],
      }
    }
  )

  // Register a dice statistics tool
  server.tool(
    'dice_stats',
    'Calculate statistics for a dice type (probability distributions, expected values)',
    {
      dice_type: z.enum(DICE_TYPES).describe('Type of dice to analyze'),
    },
    async ({ dice_type }): Promise<CallToolResult> => {
      const sides = parseInt(dice_type.substring(1))
      const probability = ((1 / sides) * 100).toFixed(2)
      const expectedValue = (sides + 1) / 2

      let statsText = `📊 **${dice_type} Statistics** 📊\n\n`
      statsText += `• Sides: ${sides}\n`
      statsText += `• Range: 1-${sides}\n`
      statsText += `• Probability per face: ${probability}%\n`
      statsText += `• Expected value: ${expectedValue}\n`
      statsText += `• Variance: ${((sides * sides - 1) / 12).toFixed(2)}\n`
      statsText += `• Standard deviation: ${Math.sqrt((sides * sides - 1) / 12).toFixed(2)}\n\n`

      // Add probability distribution visualization
      statsText += `**Probability Distribution:**\n`
      const barLength = 20
      for (let i = 1; i <= Math.min(sides, 20); i++) {
        const bar = '█'.repeat(Math.ceil(barLength / sides))
        statsText += `${i.toString().padStart(3)}: ${bar} ${probability}%\n`
      }

      if (sides > 20) {
        statsText += `... (showing first 20 values)\n`
      }

      return {
        content: [
          {
            type: 'text',
            text: statsText,
          },
        ],
      }
    }
  )

  // Register a fun "roll for initiative" tool
  server.tool(
    'roll_initiative',
    'Roll for initiative in a tabletop RPG style',
    {
      character_name: z.string().describe('Name of the character rolling'),
      dexterity_modifier: z.number().int().min(-5).max(5).default(0).describe('Dexterity modifier'),
    },
    async (
      { character_name, dexterity_modifier },
      { sendNotification }
    ): Promise<CallToolResult> => {
      await sendNotification({
        method: 'notifications/message',
        params: {
          level: 'info',
          data: `⚔️ ${character_name} rolls for initiative!`,
        },
      })

      await new Promise((resolve) => setTimeout(resolve, 500))

      const roll = rollDie(20)
      const total = roll + dexterity_modifier

      let resultText = `⚔️ **Initiative Roll** ⚔️\n\n`
      resultText += `Character: ${character_name}\n`
      resultText += `D20 Roll: ${roll}\n`
      resultText += `DEX Modifier: ${dexterity_modifier >= 0 ? '+' : ''}${dexterity_modifier}\n`
      resultText += `**Total Initiative: ${total}**\n\n`

      // Add flavor text based on result
      if (roll === 20) {
        resultText += `🌟 Natural 20! ${character_name} moves with lightning speed!`
      } else if (roll === 1) {
        resultText += `💀 Natural 1! ${character_name} stumbles at the start!`
      } else if (total >= 20) {
        resultText += `⚡ Incredible reflexes! ${character_name} is first to act!`
      } else if (total >= 15) {
        resultText += `🏃 Quick on the draw! ${character_name} is ready for action!`
      } else if (total >= 10) {
        resultText += `👍 Decent speed! ${character_name} is prepared!`
      } else if (total >= 5) {
        resultText += `😅 A bit slow... ${character_name} needs to be careful!`
      } else {
        resultText += `🐌 Very slow start... ${character_name} might be in trouble!`
      }

      return {
        content: [
          {
            type: 'text',
            text: resultText,
          },
        ],
      }
    }
  )

  return server
}

// Express app setup
const app = express()
app.use(express.json())

const PORT = process.env.PORT || 3000

// Map to store transports by session ID
const transports: { [sessionId: string]: StreamableHTTPServerTransport } = {}

// MCP POST endpoint handler
const mcpPostHandler = async (req: Request, res: Response) => {
  console.log('Received MCP request:', JSON.stringify(req.body, null, 2))

  try {
    const sessionId = req.headers['mcp-session-id'] as string | undefined
    let transport: StreamableHTTPServerTransport

    if (sessionId && transports[sessionId]) {
      // Reuse existing transport
      transport = transports[sessionId]
    } else if (!sessionId && isInitializeRequest(req.body)) {
      // New initialization request
      const eventStore = new InMemoryEventStore()
      transport = new StreamableHTTPServerTransport({
        sessionIdGenerator: () => randomUUID(),
        eventStore,
        onsessioninitialized: (sessionId) => {
          console.log(`🎲 Dice server session initialized: ${sessionId}`)
          transports[sessionId] = transport
        },
      })

      // Set up cleanup handler
      transport.onclose = () => {
        const sid = transport.sessionId
        if (sid && transports[sid]) {
          console.log(`Session ${sid} closed, cleaning up...`)
          delete transports[sid]
        }
      }

      // Connect transport to server
      const server = createDiceServer()
      await server.connect(transport)

      await transport.handleRequest(req, res, req.body)
      return
    } else {
      // Invalid request
      res.status(400).json({
        jsonrpc: '2.0',
        error: {
          code: -32000,
          message: 'Bad Request: No valid session ID provided',
        },
        id: null,
      })
      return
    }

    await transport.handleRequest(req, res, req.body)
  } catch (error) {
    console.error('Error handling MCP request:', error)
    if (!res.headersSent) {
      res.status(500).json({
        jsonrpc: '2.0',
        error: {
          code: -32603,
          message: 'Internal server error',
        },
        id: null,
      })
    }
  }
}

// MCP GET endpoint for SSE streams
const mcpGetHandler = async (req: Request, res: Response) => {
  const sessionId = req.headers['mcp-session-id'] as string | undefined
  if (!sessionId || !transports[sessionId]) {
    res.status(400).send('Invalid or missing session ID')
    return
  }

  const lastEventId = req.headers['last-event-id'] as string | undefined
  if (lastEventId) {
    console.log(`Client reconnecting with Last-Event-ID: ${lastEventId}`)
  } else {
    console.log(`Establishing SSE stream for session ${sessionId}`)
  }

  const transport = transports[sessionId]
  await transport.handleRequest(req, res)
}

// MCP DELETE endpoint for session termination
const mcpDeleteHandler = async (req: Request, res: Response) => {
  const sessionId = req.headers['mcp-session-id'] as string | undefined
  if (!sessionId || !transports[sessionId]) {
    res.status(400).send('Invalid or missing session ID')
    return
  }

  console.log(`Terminating session ${sessionId}`)

  try {
    const transport = transports[sessionId]
    await transport.handleRequest(req, res)
  } catch (error) {
    console.error('Error handling session termination:', error)
    if (!res.headersSent) {
      res.status(500).send('Error processing session termination')
    }
  }
}

// Set up routes
app.post('/mcp', mcpPostHandler)
app.get('/mcp', mcpGetHandler)
app.delete('/mcp', mcpDeleteHandler)

// Health check endpoint
app.get('/health', (req, res) => {
  res.json({
    status: 'ok',
    server: 'dice-rolling-mcp-server',
    sessions: Object.keys(transports).length,
  })
})

// Start server
app.listen(PORT, () => {
  console.log(`🎲 Dice Rolling MCP Server listening on port ${PORT}`)
  console.log(`   Health check: http://localhost:${PORT}/health`)
  console.log(`   MCP endpoint: http://localhost:${PORT}/mcp`)
  console.log('\nAvailable tools:')
  console.log('  • roll_dice - Roll various dice types with modifiers')
  console.log('  • dice_stats - Get statistics for dice types')
  console.log('  • roll_initiative - Roll for initiative in RPG style')
})

// Graceful shutdown
process.on('SIGINT', async () => {
  console.log('\nShutting down dice server...')

  for (const sessionId in transports) {
    try {
      console.log(`Closing session ${sessionId}`)
      await transports[sessionId].close()
      delete transports[sessionId]
    } catch (error) {
      console.error(`Error closing session ${sessionId}:`, error)
    }
  }

  console.log('Dice server shutdown complete 🎲')
  process.exit(0)
})
