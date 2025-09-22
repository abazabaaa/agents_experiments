#!/usr/bin/env bun
/**
 * Test client for the Dice Rolling MCP Server
 *
 * This demonstrates how to connect to and use the dice rolling MCP server.
 *
 * First start the server:
 *   bun run examples/dice-rolling-mcp-server.ts
 *
 * Then run this client:
 *   bun run examples/dice-rolling-client.ts
 */

import { McpClient } from '../typescript-sdk/src/client/index'
import { StreamableHTTPClientTransport } from '../typescript-sdk/src/client/streamableHttp'

async function main() {
  console.log('🎲 Dice Rolling MCP Client\n')

  // Create transport
  const transport = new StreamableHTTPClientTransport({
    url: new URL('http://localhost:3000/mcp'),
  })

  // Create client
  const client = new McpClient(
    {
      name: 'dice-client',
      version: '1.0.0',
    },
    {
      capabilities: {
        tools: {},
      },
    }
  )

  try {
    // Connect to server
    console.log('Connecting to dice server...')
    await client.connect(transport)
    console.log('Connected! Session ID:', transport.sessionId)

    // List available tools
    console.log('\n📋 Available tools:')
    const tools = await client.listTools()
    for (const tool of tools.tools) {
      console.log(`  • ${tool.name} - ${tool.description}`)
    }

    // Example 1: Roll a single d20
    console.log('\n\n--- Example 1: Rolling a d20 ---')
    const d20Result = await client.callTool({
      name: 'roll_dice',
      arguments: {
        dice_type: 'd20',
        count: 1,
      },
    })
    console.log(d20Result.content[0].text)

    // Example 2: Roll multiple d6 with modifier
    console.log('\n\n--- Example 2: Rolling 3d6+2 ---')
    const multiDiceResult = await client.callTool({
      name: 'roll_dice',
      arguments: {
        dice_type: 'd6',
        count: 3,
        modifier: 2,
      },
    })
    console.log(multiDiceResult.content[0].text)

    // Example 3: Get dice statistics
    console.log('\n\n--- Example 3: d12 Statistics ---')
    const statsResult = await client.callTool({
      name: 'dice_stats',
      arguments: {
        dice_type: 'd12',
      },
    })
    console.log(statsResult.content[0].text)

    // Example 4: Roll for initiative
    console.log('\n\n--- Example 4: Roll for Initiative ---')
    const initiativeResult = await client.callTool({
      name: 'roll_initiative',
      arguments: {
        character_name: 'Gandalf the Grey',
        dexterity_modifier: 2,
      },
    })
    console.log(initiativeResult.content[0].text)

    // Interactive mode
    console.log('\n\n--- Interactive Mode ---')
    console.log('Try some rolls yourself! (Press Ctrl+C to exit)\n')

    const readline = await import('readline')
    const rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout,
    })

    const question = (prompt: string): Promise<string> =>
      new Promise((resolve) => rl.question(prompt, resolve))

    while (true) {
      try {
        const diceType = await question('Enter dice type (d4/d6/d8/d10/d12/d20/d100): ')
        if (!['d4', 'd6', 'd8', 'd10', 'd12', 'd20', 'd100'].includes(diceType)) {
          console.log('Invalid dice type. Try again.')
          continue
        }

        const countStr = await question('How many dice? (1-100): ')
        const count = parseInt(countStr) || 1

        const modifierStr = await question('Modifier? (optional, e.g., +2 or -1): ')
        const modifier = modifierStr ? parseInt(modifierStr) : undefined

        console.log('\nRolling...\n')
        const result = await client.callTool({
          name: 'roll_dice',
          arguments: {
            dice_type: diceType,
            count: count,
            modifier: modifier,
          },
        })

        console.log(result.content[0].text)
        console.log('\n' + '='.repeat(50) + '\n')
      } catch (error) {
        if (error.message?.includes('SIGINT')) break
        console.error('Error:', error.message)
      }
    }

    rl.close()
  } catch (error) {
    console.error('Error:', error)
  } finally {
    // Clean up
    console.log('\nClosing connection...')
    await client.close()
    console.log('Goodbye! 🎲')
  }
}

// Run the client
main().catch(console.error)
