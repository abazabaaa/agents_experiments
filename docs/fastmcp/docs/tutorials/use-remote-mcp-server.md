# Connect to Remote MCP Servers

> Learn how to connect Claude to remote MCP servers and extend its capabilities with internet-hosted tools and data sources

Remote MCP servers extend AI applications' capabilities beyond your local environment, providing access to internet-hosted tools, services, and data sources. By connecting to remote MCP servers, you transform AI assistants from helpful tools into informed teammates capable of handling complex, multi-step projects with real-time access to external resources.

Many clients now support remote MCP servers, enabling a wide range of integration possibilities. This guide demonstrates how to connect to remote MCP servers using [Claude](https://claude.ai/) as an example, one of the [many clients that support MCP](/clients). While we focus on Claude's implementation through Custom Connectors, the concepts apply broadly to other MCP-compatible clients.

## Understanding Remote MCP Servers

Remote MCP servers function similarly to local MCP servers but are hosted on the internet rather than your local machine. They expose tools, prompts, and resources that Claude can use to perform tasks on your behalf. These servers can integrate with various services such as project management tools, documentation systems, code repositories, and any other API-enabled service.

The key advantage of remote MCP servers is their accessibility. Unlike local servers that require installation and configuration on each device, remote servers are available from any MCP client with an internet connection. This makes them ideal for web-based AI applications, integrations that emphasize ease-of-use and services that require server-side processing or authentication.

## What are Custom Connectors?

Custom Connectors serve as the bridge between Claude and remote MCP servers. They allow you to connect Claude directly to the tools and data sources that matter most to your workflows, enabling Claude to operate within your favorite software and draw insights from the complete context of your external tools.

With Custom Connectors, you can:

* [Connect Claude to existing remote MCP servers](https://support.anthropic.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp) provided by third-party developers
* [Build your own remote MCP servers to connect with any tool](https://support.anthropic.com/en/articles/11503834-building-custom-connectors-via-remote-mcp-servers)

## Connecting to a Remote MCP Server

The process of connecting Claude to a remote MCP server involves adding a Custom Connector through the [Claude interface](https://claude.ai/). This establishes a secure connection between Claude and your chosen remote server.

<Steps>
  <Step title="Navigate to Connector Settings">
    Open Claude in your browser and navigate to the settings page. You can access this by clicking on your profile icon and selecting "Settings" from the dropdown menu. Once in settings, locate and click on the "Connectors" section in the sidebar.

    This will display your currently configured connectors and provide options to add new ones.
  </Step>

  <Step title="Add a Custom Connector">
    In the Connectors section, scroll to the bottom where you'll find the "Add custom connector" button. Click this button to begin the connection process.

    <Frame>
      <img src="https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-remote/1-add-connector.png?maxW=1038&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=f1f67d7adae97ff0ad85f8402c469f52" alt="Add custom connector button in Claude settings" width="1038" height="809" data-path="images/quickstart-remote/1-add-connector.png" srcset="https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-remote/1-add-connector.png?w=280&maxW=1038&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=1c91c5de30259ed681ef33c6b5e43de3 280w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-remote/1-add-connector.png?w=560&maxW=1038&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=9c0460bab6ede671884b71c6d4ee730d 560w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-remote/1-add-connector.png?w=840&maxW=1038&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=b624664b4000c3041b62b4a613c929c1 840w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-remote/1-add-connector.png?w=1100&maxW=1038&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=55de29f7af41035374418ba28b0ba2bd 1100w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-remote/1-add-connector.png?w=1650&maxW=1038&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=59f5d9e8c26905ee9389b63cd5b9904d 1650w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-remote/1-add-connector.png?w=2500&maxW=1038&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=c92cebf44cba51d1e27852a5a208f898 2500w" data-optimize="true" data-opv="2" />
    </Frame>

    A dialog will appear prompting you to enter the remote MCP server URL. This URL should be provided by the server developer or administrator. Enter the complete URL, ensuring it includes the proper protocol (https\://) and any necessary path components.

    <Frame>
      <img src="https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-remote/2-connect.png?maxW=1616&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=20769374dd969dc3d54483e673f096cf" alt="Dialog for entering remote MCP server URL" width="1616" height="282" data-path="images/quickstart-remote/2-connect.png" srcset="https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-remote/2-connect.png?w=280&maxW=1616&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=3d7c5aafe6f53bdf42a8fe869a09cf37 280w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-remote/2-connect.png?w=560&maxW=1616&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=0c6bb336d1e69478ef9b5748f01e7dbd 560w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-remote/2-connect.png?w=840&maxW=1616&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=cc05410ca8ccb8dde1062c57b938f3c0 840w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-remote/2-connect.png?w=1100&maxW=1616&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=f53452170364b6cc458b5ee529ce724c 1100w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-remote/2-connect.png?w=1650&maxW=1616&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=98030d6a6956ba6cdd988dad249f8d4b 1650w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-remote/2-connect.png?w=2500&maxW=1616&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=4ace4e82ac45641942a98dee4bf49cf7 2500w" data-optimize="true" data-opv="2" />
    </Frame>

    After entering the URL, click "Add" to proceed with the connection.
  </Step>

  <Step title="Complete Authentication">
    Most remote MCP servers require authentication to ensure secure access to their resources. The authentication process varies depending on the server implementation but commonly involves OAuth, API keys, or username/password combinations.

    <Frame>
      <img src="https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-remote/3-auth.png?maxW=490&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=a1e5e74f8325627d180bdf079739216d" alt="Authentication screen for remote MCP server" width="490" height="806" data-path="images/quickstart-remote/3-auth.png" srcset="https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-remote/3-auth.png?w=280&maxW=490&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=02707ebbd70ea8872cbcc03beecd85c7 280w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-remote/3-auth.png?w=560&maxW=490&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=8617d8d71ff26429d7627d8c6304e903 560w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-remote/3-auth.png?w=840&maxW=490&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=152514eabcd985b29a33226850c8c6e7 840w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-remote/3-auth.png?w=1100&maxW=490&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=ef8d6ed20d5ae68ba414b062a3c66ace 1100w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-remote/3-auth.png?w=1650&maxW=490&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=0008511d29c2eb7c757869ba35fbfa5d 1650w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-remote/3-auth.png?w=2500&maxW=490&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=65ce80655b8c0153baf3495cb276c903 2500w" data-optimize="true" data-opv="2" />
    </Frame>

    Follow the authentication prompts provided by the server. This may redirect you to a third-party authentication provider or display a form within Claude. Once authentication is complete, Claude will establish a secure connection to the remote server.
  </Step>

  <Step title="Access Resources and Prompts">
    After successful connection, the remote server's resources and prompts become available in your Claude conversations. You can access these by clicking the paperclip icon in the message input area, which opens the attachment menu.

    <Frame>
      <img src="https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-remote/4-select-resources-menu.png?maxW=735&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=885a676879a4fba5413be3887b5939cd" alt="Attachment menu showing available resources" width="735" height="666" data-path="images/quickstart-remote/4-select-resources-menu.png" srcset="https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-remote/4-select-resources-menu.png?w=280&maxW=735&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=83ce863a0835bd72a969d8f50863712d 280w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-remote/4-select-resources-menu.png?w=560&maxW=735&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=155ab6b53114c19676d9ca2dbc60763b 560w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-remote/4-select-resources-menu.png?w=840&maxW=735&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=7711184aab56447909a4f82a7bc48b39 840w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-remote/4-select-resources-menu.png?w=1100&maxW=735&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=29edf402ea9e934c19fce384160da053 1100w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-remote/4-select-resources-menu.png?w=1650&maxW=735&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=f246dd3ddce438ff674319fc34bcb4ed 1650w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-remote/4-select-resources-menu.png?w=2500&maxW=735&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=888bf12815deed0763e6efb90d00758d 2500w" data-optimize="true" data-opv="2" />
    </Frame>

    The menu displays all available resources and prompts from your connected servers. Select the items you want to include in your conversation. These resources provide Claude with context and information from your external tools.

    <Frame>
      <img src="https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-remote/5-select-prompts-resources.png?maxW=648&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=753f8e5c1fa3f3176e2d256ae1c3ad94" alt="Selecting specific resources and prompts from the menu" width="648" height="920" data-path="images/quickstart-remote/5-select-prompts-resources.png" srcset="https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-remote/5-select-prompts-resources.png?w=280&maxW=648&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=fc7545975ff04da074a7ca899f054014 280w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-remote/5-select-prompts-resources.png?w=560&maxW=648&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=1f66c109424e0e219d2157d40a0b48b4 560w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-remote/5-select-prompts-resources.png?w=840&maxW=648&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=448413cd89585951b59a86544cc92101 840w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-remote/5-select-prompts-resources.png?w=1100&maxW=648&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=b349872102be26cad33e7b1982d6a20e 1100w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-remote/5-select-prompts-resources.png?w=1650&maxW=648&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=65f197dfc63853196b051fe4eefa25c6 1650w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-remote/5-select-prompts-resources.png?w=2500&maxW=648&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=0df3c8091facc70d6aab21760acef546 2500w" data-optimize="true" data-opv="2" />
    </Frame>
  </Step>

  <Step title="Configure Tool Permissions">
    Remote MCP servers often expose multiple tools with varying capabilities. You can control which tools Claude is allowed to use by configuring permissions in the connector settings. This ensures Claude only performs actions you've explicitly authorized.

    <Frame>
      <img src="https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-remote/6-configure-tools.png?maxW=604&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=b2f3d349398ce2204ac413b281e62108" alt="Tool permission configuration interface" width="604" height="745" data-path="images/quickstart-remote/6-configure-tools.png" srcset="https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-remote/6-configure-tools.png?w=280&maxW=604&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=94ace92787cc1196e5301e8157b62614 280w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-remote/6-configure-tools.png?w=560&maxW=604&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=c6efc3d84c287f1cc35849fcbce9fdcd 560w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-remote/6-configure-tools.png?w=840&maxW=604&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=7f64857d55c0c7eb0fc28941cba6ccb3 840w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-remote/6-configure-tools.png?w=1100&maxW=604&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=4456729d0c024751226237124cfbe735 1100w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-remote/6-configure-tools.png?w=1650&maxW=604&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=860fe142e29dd33cfbe541d352e47a7a 1650w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-remote/6-configure-tools.png?w=2500&maxW=604&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=96436342b7e453cb43f7f8616820bcea 2500w" data-optimize="true" data-opv="2" />
    </Frame>

    Navigate back to the Connectors settings and click on your connected server. Here you can enable or disable specific tools, set usage limits, and configure other security parameters according to your needs.
  </Step>
</Steps>

## Best Practices for Using Remote MCP Servers

When working with remote MCP servers, consider these recommendations to ensure a secure and efficient experience:

**Security considerations**: Always verify the authenticity of remote MCP servers before connecting. Only connect to servers from trusted sources, and review the permissions requested during authentication. Be cautious about granting access to sensitive data or systems.

**Managing multiple connectors**: You can connect to multiple remote MCP servers simultaneously. Organize your connectors by purpose or project to maintain clarity. Regularly review and remove connectors you no longer use to keep your workspace organized and secure.

## Next Steps

Now that you've connected Claude to a remote MCP server, you can explore its capabilities in your conversations. Try using the connected tools to automate tasks, access external data, or integrate with your existing workflows.

<CardGroup cols={2}>
  <Card title="Build your own remote server" icon="cloud" href="https://support.anthropic.com/en/articles/11503834-building-custom-connectors-via-remote-mcp-servers">
    Create custom remote MCP servers to integrate with proprietary tools and
    services
  </Card>

  <Card title="Explore available servers" icon="grid" href="https://github.com/modelcontextprotocol/servers">
    Browse our collection of official and community-created MCP servers
  </Card>

  <Card title="Connect local servers" icon="computer" href="/quickstart/user">
    Learn how to connect Claude Desktop to local MCP servers for direct system
    access
  </Card>

  <Card title="Understand the architecture" icon="book" href="/docs/learn/architecture">
    Dive deeper into how MCP works and its architecture
  </Card>
</CardGroup>

Remote MCP servers unlock powerful possibilities for extending Claude's capabilities. As you become familiar with these integrations, you'll discover new ways to streamline your workflows and accomplish complex tasks more efficiently.
