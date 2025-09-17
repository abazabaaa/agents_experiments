# FAQs

> Explaining MCP and why it matters in simple terms

## What is MCP?

MCP (Model Context Protocol) is a standard way for AI applications and agents to connect to and work with your data sources (e.g. local files, databases, or content repositories) and tools (e.g. GitHub, Google Maps, or Puppeteer).

Think of MCP as a universal adapter for AI applications, similar to what USB-C is for physical devices. USB-C acts as a universal adapter to connect devices to various peripherals and accessories. Similarly, MCP provides a standardized way to connect AI applications to different data and tools.

Before USB-C, you needed different cables for different connections. Similarly, before MCP, developers had to build custom connections to each data source or tool they wanted their AI application to work with—a time-consuming process that often resulted in limited functionality. Now, with MCP, developers can easily add connections to their AI applications, making their applications much more powerful from day one.

## Why does MCP matter?

### For AI application users

MCP means your AI applications can access the information and tools you work with every day, making them much more helpful. Rather than AI being limited to what it already knows about, it can now understand your specific documents, data, and work context.

For example, by using MCP servers, applications can access your personal documents from Google Drive or data about your codebase from GitHub, providing more personalized and contextually relevant assistance.

Imagine asking an AI assistant: "Summarize last week's team meeting notes and schedule follow-ups with everyone."

By using connections to data sources powered by MCP, the AI assistant can:

* Connect to your Google Drive through an MCP server to read meeting notes
* Understand who needs follow-ups based on the notes
* Connect to your calendar through another MCP server to schedule the meetings automatically

### For developers

MCP reduces development time and complexity when building AI applications that need to access various data sources. With MCP, developers can focus on building great AI experiences rather than repeatedly creating custom connectors.

Traditionally, connecting applications with data sources required building custom, one-off connections for each data source and each application. This created significant duplicative work—every developer wanting to connect their AI application to Google Drive or Slack needed to build their own connection.

MCP simplifies this by enabling developers to build MCP servers for data sources that are then reusable by various applications. For example, using the open source Google Drive MCP server, many different applications can access data from Google Drive without each developer needing to build a custom connection.

This open source ecosystem of MCP servers means developers can leverage existing work rather than starting from scratch, making it easier to build powerful AI applications that seamlessly integrate with the tools and data sources their users already rely on.

## How does MCP work?

<Frame>
  <img src="https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/mcp-simple-diagram.png?maxW=3840&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=e50b1bd510710f3e4bd782e79eca68cb" width="3840" height="1500" data-path="images/mcp-simple-diagram.png" srcset="https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/mcp-simple-diagram.png?w=280&maxW=3840&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=94883d47fa6aa36bad789337a2db059b 280w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/mcp-simple-diagram.png?w=560&maxW=3840&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=3330b3315b8c436151a2316431064f95 560w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/mcp-simple-diagram.png?w=840&maxW=3840&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=885c3dcfa17929b4472f528ee8a93aa2 840w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/mcp-simple-diagram.png?w=1100&maxW=3840&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=f61c6b2e16e7454fa7ac0b2c3f53f5f8 1100w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/mcp-simple-diagram.png?w=1650&maxW=3840&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=52de2e3c6b830d556a681e66842b60c1 1650w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/mcp-simple-diagram.png?w=2500&maxW=3840&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=81ea386e56527b9dc0c714a972c582bc 2500w" data-optimize="true" data-opv="2" />
</Frame>

MCP creates a bridge between your AI applications and your data through a straightforward system:

* **MCP servers** connect to your data sources and tools (like Google Drive or Slack)
* **MCP clients** are run by AI applications (like Claude Desktop) to connect them to these servers
* When you give permission, your AI application discovers available MCP servers
* The AI model can then use these connections to read information and take actions

This modular system means new capabilities can be added without changing AI applications themselves—just like adding new accessories to your computer without upgrading your entire system.

## Who creates and maintains MCP servers?

MCP servers are developed and maintained by:

* Developers at Anthropic who build servers for common tools and data sources
* Open source contributors who create servers for tools they use
* Enterprise development teams building servers for their internal systems
* Software providers making their applications AI-ready

Once an open source MCP server is created for a data source, it can be used by any MCP-compatible AI application, creating a growing ecosystem of connections. See our [list of example servers](/examples), or [get started building your own server](/quickstart/server).
