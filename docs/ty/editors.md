[Skip to content](https://docs.astral.sh/ty/editors/#editor-integration)

# [Editor integration](https://docs.astral.sh/ty/editors/\#editor-integration)

ty can be integrated with various editors to provide a seamless development experience.

## [VS Code](https://docs.astral.sh/ty/editors/\#vs-code)

The Astral team maintains an official VS Code extension.

Install the [ty extension](https://marketplace.visualstudio.com/items?itemName=astral-sh.ty) from the VS Code Marketplace.

See the extension's [README](https://github.com/astral-sh/ty-vscode) for more details on usage.

## [Neovim](https://docs.astral.sh/ty/editors/\#neovim)

For Neovim 0.10 or earlier (with [`nvim-lspconfig`](https://github.com/neovim/nvim-lspconfig)):

```
require('lspconfig').ty.setup({
  settings = {
    ty = {
      -- ty language server settings go here
    }
  }
})

```

For Neovim 0.11+ (with [`vim.lsp.config`](https://neovim.io/doc/user/lsp.html#vim.lsp.config())):

```
-- Optional: Only required if you need to update the language server settings
vim.lsp.config('ty', {
  settings = {
    ty = {
      -- ty language server settings go here
    }
  }
})

-- Required: Enable the language server
vim.lsp.enable('ty')

```

## [Other editors](https://docs.astral.sh/ty/editors/\#other-editors)

ty can be used with any editor that supports the [language server\\
protocol](https://microsoft.github.io/language-server-protocol/).

To start the language server, use the `server` subcommand:

```
ty server

```

Refer to your editor's documentation to learn how to connect to an LSP server.

See the [editor settings](https://docs.astral.sh/ty/reference/editor-settings/) for more details on configuring the language
server.
