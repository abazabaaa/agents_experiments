# Connect to Local MCP Servers

> Learn how to extend Claude Desktop with local MCP servers to enable file system access and other powerful integrations

Model Context Protocol (MCP) servers extend AI applications' capabilities by providing secure, controlled access to local resources and tools. Many clients support MCP, enabling diverse integration possibilities across different platforms and applications.

This guide demonstrates how to connect to local MCP servers using Claude Desktop as an example, one of the [many clients that support MCP](/clients). While we focus on Claude Desktop's implementation, the concepts apply broadly to other MCP-compatible clients. By the end of this tutorial, Claude will be able to interact with files on your computer, create new documents, organize folders, and search through your file system—all with your explicit permission for each action.

<Frame>
  <img src="https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-filesystem.png?maxW=1732&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=e38a90e4a739f20a51943087f3777612" alt="Claude Desktop with filesystem integration showing file management capabilities" width="1732" height="2060" data-path="images/quickstart-filesystem.png" srcset="https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-filesystem.png?w=280&maxW=1732&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=b3d8e9db92f23ed623789f57d60a932f 280w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-filesystem.png?w=560&maxW=1732&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=e11646be6c633fe669f79cb1c0668db5 560w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-filesystem.png?w=840&maxW=1732&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=3f9a662eaa217b39040ad4424cc746a1 840w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-filesystem.png?w=1100&maxW=1732&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=d2155bee1d6766978906c939ef4cbe59 1100w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-filesystem.png?w=1650&maxW=1732&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=e7860661d4c1dc4bddfa59a48516f0ed 1650w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-filesystem.png?w=2500&maxW=1732&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=3993011b9ca682242e2368eb3e7ed48e 2500w" data-optimize="true" data-opv="2" />
</Frame>

## Prerequisites

Before starting this tutorial, ensure you have the following installed on your system:

### Claude Desktop

Download and install [Claude Desktop](https://claude.ai/download) for your operating system. Claude Desktop is currently available for macOS and Windows. Linux support is coming soon.

If you already have Claude Desktop installed, verify you're running the latest version by clicking the Claude menu and selecting "Check for Updates..."

### Node.js

The Filesystem Server and many other MCP servers require Node.js to run. Verify your Node.js installation by opening a terminal or command prompt and running:

```bash
node --version
```

If Node.js is not installed, download it from [nodejs.org](https://nodejs.org/). We recommend the LTS (Long Term Support) version for stability.

## Understanding MCP Servers

MCP servers are programs that run on your computer and provide specific capabilities to Claude Desktop through a standardized protocol. Each server exposes tools that Claude can use to perform actions, with your approval. The Filesystem Server we'll install provides tools for:

* Reading file contents and directory structures
* Creating new files and directories
* Moving and renaming files
* Searching for files by name or content

All actions require your explicit approval before execution, ensuring you maintain full control over what Claude can access and modify.

## Installing the Filesystem Server

The process involves configuring Claude Desktop to automatically start the Filesystem Server whenever you launch the application. This configuration is done through a JSON file that tells Claude Desktop which servers to run and how to connect to them.

<Steps>
  <Step title="Open Claude Desktop Settings">
    Start by accessing the Claude Desktop settings. Click on the Claude menu in your system's menu bar (not the settings within the Claude window itself) and select "Settings..."

    On macOS, this appears in the top menu bar:

    <Frame style={{ textAlign: "center" }}>
      <img src="https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-menu.png?maxW=644&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=18d240ffc2e61a773afa41c5d63cae8a" width="400" alt="Claude Desktop menu showing Settings option" width="644" height="568" data-path="images/quickstart-menu.png" srcset="https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-menu.png?w=280&maxW=644&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=8b1db4344e5eb19a4e7912b2952bc749 280w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-menu.png?w=560&maxW=644&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=b4c622d5312dfe40fafc5a26432e3c5e 560w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-menu.png?w=840&maxW=644&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=6fafa3de7f65c49d527cbcd42535f754 840w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-menu.png?w=1100&maxW=644&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=00957d1ae453098cf2896e920959fc6b 1100w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-menu.png?w=1650&maxW=644&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=11964c1951f2bedddf2e2228087aa13e 1650w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-menu.png?w=2500&maxW=644&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=a458f9c1ddc2134e8b0a3c3f8f044d8b 2500w" data-optimize="true" data-opv="2" />
    </Frame>

    This opens the Claude Desktop configuration window, which is separate from your Claude account settings.
  </Step>

  <Step title="Access Developer Settings">
    In the Settings window, navigate to the "Developer" tab in the left sidebar. This section contains options for configuring MCP servers and other developer features.

    Click the "Edit Config" button to open the configuration file:

    <Frame>
      <img src="https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-developer.png?maxW=1688&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=6e727696744412091be2ca61ba12464d" alt="Developer settings showing Edit Config button" width="1688" height="534" data-path="images/quickstart-developer.png" srcset="https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-developer.png?w=280&maxW=1688&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=0a506f53284388d4da26a6a1b7ff869d 280w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-developer.png?w=560&maxW=1688&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=bf13fedafd285156edc5d39786de1490 560w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-developer.png?w=840&maxW=1688&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=afbc7034da8d5b6e76acfda23fee15af 840w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-developer.png?w=1100&maxW=1688&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=1415644bb0151ea68d5354a6b4685330 1100w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-developer.png?w=1650&maxW=1688&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=a0a90f74a0a9ae081f91719abc5453f9 1650w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-developer.png?w=2500&maxW=1688&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=d99bd0283206eea95a34b52def20e620 2500w" data-optimize="true" data-opv="2" />
    </Frame>

    This action creates a new configuration file if one doesn't exist, or opens your existing configuration. The file is located at:

    * **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
    * **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
  </Step>

  <Step title="Configure the Filesystem Server">
    Replace the contents of the configuration file with the following JSON structure. This configuration tells Claude Desktop to start the Filesystem Server with access to specific directories:

    <CodeGroup>
      ```json macOS
      {
        "mcpServers": {
          "filesystem": {
            "command": "npx",
            "args": [
              "-y",
              "@modelcontextprotocol/server-filesystem",
              "/Users/username/Desktop",
              "/Users/username/Downloads"
            ]
          }
        }
      }
      ```

      ```json Windows
      {
        "mcpServers": {
          "filesystem": {
            "command": "npx",
            "args": [
              "-y",
              "@modelcontextprotocol/server-filesystem",
              "C:\\Users\\username\\Desktop",
              "C:\\Users\\username\\Downloads"
            ]
          }
        }
      }
      ```
    </CodeGroup>

    Replace `username` with your actual computer username. The paths listed in the `args` array specify which directories the Filesystem Server can access. You can modify these paths or add additional directories as needed.

    <Tip>
      **Understanding the Configuration**

      * `"filesystem"`: A friendly name for the server that appears in Claude Desktop
      * `"command": "npx"`: Uses Node.js's npx tool to run the server
      * `"-y"`: Automatically confirms the installation of the server package
      * `"@modelcontextprotocol/server-filesystem"`: The package name of the Filesystem Server
      * The remaining arguments: Directories the server is allowed to access
    </Tip>

    <Warning>
      **Security Consideration**

      Only grant access to directories you're comfortable with Claude reading and modifying. The server runs with your user account permissions, so it can perform any file operations you can perform manually.
    </Warning>
  </Step>

  <Step title="Restart Claude Desktop">
    After saving the configuration file, completely quit Claude Desktop and restart it. The application needs to restart to load the new configuration and start the MCP server.

    Upon successful restart, you'll see an MCP server indicator <img src="https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/claude-desktop-mcp-slider.svg?maxW=24&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=9105b71f51c1869d5d1e1d74679ae61a" style={{display: 'inline', margin: 0, height: '1.3em'}} width="24" height="24" data-path="images/claude-desktop-mcp-slider.svg" srcset="https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/claude-desktop-mcp-slider.svg?w=280&maxW=24&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=6de6b0fd8bf730ea026f4b387ad7a185 280w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/claude-desktop-mcp-slider.svg?w=560&maxW=24&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=a4db4c16eeb7888c776d3b9f52776bd3 560w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/claude-desktop-mcp-slider.svg?w=840&maxW=24&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=d969e267d511a8e53111b71fd7916b1d 840w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/claude-desktop-mcp-slider.svg?w=1100&maxW=24&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=159679ffa63074d80f4a6034a37ee902 1100w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/claude-desktop-mcp-slider.svg?w=1650&maxW=24&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=de2024d414b0bf946b407161ddf311e8 1650w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/claude-desktop-mcp-slider.svg?w=2500&maxW=24&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=e28f3fcb0826b575fd00346dd7edb543 2500w" data-optimize="true" data-opv="2" /> in the bottom-right corner of the conversation input box:

    <Frame>
      <img src="https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-slider.png?maxW=1414&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=4cbeff7cdfdddd6f06f822e31baca92b" alt="Claude Desktop interface showing MCP server indicator" width="1414" height="410" data-path="images/quickstart-slider.png" srcset="https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-slider.png?w=280&maxW=1414&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=9412fc5bd7d4ded8dc235024b5f83842 280w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-slider.png?w=560&maxW=1414&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=56489ad7caf40709095c90c7cc915687 560w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-slider.png?w=840&maxW=1414&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=3936ef40ea32f29216c29734ee3173fd 840w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-slider.png?w=1100&maxW=1414&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=2fe9afeb4ad020c712587d593a7e4734 1100w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-slider.png?w=1650&maxW=1414&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=51e7e66ad9c8b7b8a88f51decdfb97f3 1650w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-slider.png?w=2500&maxW=1414&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=b9c1360ad4ace64d212df20842c254d9 2500w" data-optimize="true" data-opv="2" />
    </Frame>

    Click on this indicator to view the available tools provided by the Filesystem Server:

    <Frame style={{ textAlign: "center" }}>
      <img src="https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-tools.png?maxW=978&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=3ec44fbb7c34655267e6bea6305c207b" width="400" alt="Available filesystem tools in Claude Desktop" width="978" height="902" data-path="images/quickstart-tools.png" srcset="https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-tools.png?w=280&maxW=978&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=1c788324df2f8fd68f4f533eff73774d 280w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-tools.png?w=560&maxW=978&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=5fa54fc8161282cd66c6ac7df639c9ef 560w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-tools.png?w=840&maxW=978&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=cf952c86f10f162d2dcd192df9f33b2d 840w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-tools.png?w=1100&maxW=978&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=2d19def5365c319ef32d75e76f951ec4 1100w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-tools.png?w=1650&maxW=978&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=ef3a86132fbbc5345fa21b504d9cb1ad 1650w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-tools.png?w=2500&maxW=978&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=a0564d48c04bab327923d1a6cccbb0af 2500w" data-optimize="true" data-opv="2" />
    </Frame>

    If the server indicator doesn't appear, refer to the [Troubleshooting](#troubleshooting) section for debugging steps.
  </Step>
</Steps>

## Using the Filesystem Server

With the Filesystem Server connected, Claude can now interact with your file system. Try these example requests to explore the capabilities:

### File Management Examples

* **"Can you write a poem and save it to my desktop?"** - Claude will compose a poem and create a new text file on your desktop
* **"What work-related files are in my downloads folder?"** - Claude will scan your downloads and identify work-related documents
* **"Please organize all images on my desktop into a new folder called 'Images'"** - Claude will create a folder and move image files into it

### How Approval Works

Before executing any file system operation, Claude will request your approval. This ensures you maintain control over all actions:

<Frame style={{ textAlign: "center" }}>
  <img src="https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-approve.png?maxW=962&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=26d0a966eb9f26ed15973085b8c43b81" width="500" alt="Claude requesting approval to perform a file operation" width="962" height="464" data-path="images/quickstart-approve.png" srcset="https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-approve.png?w=280&maxW=962&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=9615f3436383aaa7aaf4ccca6fda02b4 280w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-approve.png?w=560&maxW=962&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=3b46aa8b351c2f36d669661477f29fac 560w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-approve.png?w=840&maxW=962&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=c7df86da28d88fb5ada84f2a1cf27392 840w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-approve.png?w=1100&maxW=962&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=5ef30875373bdab84f896e2efae6bf0d 1100w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-approve.png?w=1650&maxW=962&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=70ee5322d10fc60acfc36dac9404d264 1650w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-approve.png?w=2500&maxW=962&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=109a3da88bb58950208d8dad5a04ef5c 2500w" data-optimize="true" data-opv="2" />
</Frame>

Review each request carefully before approving. You can always deny a request if you're not comfortable with the proposed action.

## Troubleshooting

If you encounter issues setting up or using the Filesystem Server, these solutions address common problems:

<AccordionGroup>
  <Accordion title="Server not showing up in Claude / hammer icon missing">
    1. Restart Claude Desktop completely
    2. Check your `claude_desktop_config.json` file syntax
    3. Make sure the file paths included in `claude_desktop_config.json` are valid and that they are absolute and not relative
    4. Look at [logs](#getting-logs-from-claude-for-desktop) to see why the server is not connecting
    5. In your command line, try manually running the server (replacing `username` as you did in `claude_desktop_config.json`) to see if you get any errors:

    <CodeGroup>
      ```bash macOS/Linux
      npx -y @modelcontextprotocol/server-filesystem /Users/username/Desktop /Users/username/Downloads
      ```

      ```powershell Windows
      npx -y @modelcontextprotocol/server-filesystem C:\Users\username\Desktop C:\Users\username\Downloads
      ```
    </CodeGroup>
  </Accordion>

  <Accordion title="Getting logs from Claude Desktop">
    Claude.app logging related to MCP is written to log files in:

    * macOS: `~/Library/Logs/Claude`

    * Windows: `%APPDATA%\Claude\logs`

    * `mcp.log` will contain general logging about MCP connections and connection failures.

    * Files named `mcp-server-SERVERNAME.log` will contain error (stderr) logging from the named server.

    You can run the following command to list recent logs and follow along with any new ones (on Windows, it will only show recent logs):

    <CodeGroup>
      ```bash macOS/Linux
      tail -n 20 -f ~/Library/Logs/Claude/mcp*.log
      ```

      ```powershell Windows
      type "%APPDATA%\Claude\logs\mcp*.log"
      ```
    </CodeGroup>
  </Accordion>

  <Accordion title="Tool calls failing silently">
    If Claude attempts to use the tools but they fail:

    1. Check Claude's logs for errors
    2. Verify your server builds and runs without errors
    3. Try restarting Claude Desktop
  </Accordion>

  <Accordion title="None of this is working. What do I do?">
    Please refer to our [debugging guide](/legacy/tools/debugging) for better debugging tools and more detailed guidance.
  </Accordion>

  <Accordion title="ENOENT error and `${APPDATA}` in paths on Windows">
    If your configured server fails to load, and you see within its logs an error referring to `${APPDATA}` within a path, you may need to add the expanded value of `%APPDATA%` to your `env` key in `claude_desktop_config.json`:

    ```json
    {
      "brave-search": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-brave-search"],
        "env": {
          "APPDATA": "C:\\Users\\user\\AppData\\Roaming\\",
          "BRAVE_API_KEY": "..."
        }
      }
    }
    ```

    With this change in place, launch Claude Desktop once again.

    <Warning>
      **NPM should be installed globally**

      The `npx` command may continue to fail if you have not installed NPM globally. If NPM is already installed globally, you will find `%APPDATA%\npm` exists on your system. If not, you can install NPM globally by running the following command:

      ```bash
      npm install -g npm
      ```
    </Warning>
  </Accordion>
</AccordionGroup>

## Next Steps

Now that you've successfully connected Claude Desktop to a local MCP server, explore these options to expand your setup:

<CardGroup cols={2}>
  <Card title="Explore other servers" icon="grid" href="https://github.com/modelcontextprotocol/servers">
    Browse our collection of official and community-created MCP servers for
    additional capabilities
  </Card>

  <Card title="Build your own server" icon="code" href="/quickstart/server">
    Create custom MCP servers tailored to your specific workflows and
    integrations
  </Card>

  <Card title="Connect to remote servers" icon="cloud" href="/docs/tutorials/use-remote-mcp-server">
    Learn how to connect Claude to remote MCP servers for cloud-based tools and
    services
  </Card>

  <Card title="Understand the protocol" icon="book" href="/docs/learn/architecture">
    Dive deeper into how MCP works and its architecture
  </Card>
</CardGroup>
