Source URL: https://shopify.dev/docs/apps/build/ai-toolkit
Fetched: 2026-10-03 via curl https://shopify.dev/docs/apps/build/ai-toolkit.md (HTTP 200, markdown)

---
title: Shopify AI Toolkit
description: >-
  Shopify AI Toolkit connects your AI coding tools to Shopify's developer docs,
  API schemas, and CLI store management so they can help you build more
  accurately.
source_url:
  html: 'https://shopify.dev/docs/apps/build/ai-toolkit'
  md: 'https://shopify.dev/docs/apps/build/ai-toolkit.md'
---

# Shopify AI Toolkit

AI coding agents can search the web, read documentation, and inspect your codebase, but they still need the right context at the right time to be effective. Shopify development depends on platform-specific details: which API surface applies, what fields exist in a schema, which CLI command to run, and how an app or extension configuration should be validated.

Shopify AI Toolkit gives your AI coding tool a Shopify-aware starting point. The toolkit connects your agent to:

* **Developer docs and API schemas**: look up the relevant Shopify API surface and work from current reference material, rather than relying only on model memory or broad web search.
* **Code validation**: validate GraphQL queries, Liquid templates, and Shopify Extensions against Shopify schemas to catch issues earlier.
* **Store management**: prepare and run supported store-management tasks through Shopify CLI's authenticated store context, with you choosing when to execute them.

***

## Requirements

Before you install the Shopify AI Toolkit, make sure you have:

* Node.js 18 or higher installed on your system.
* A supported AI tool: Claude Code, Codex, Antigravity CLI, Cursor, Hermes (plugin only), OpenClaw (plugin only), Pi (plugin only), or Visual Studio Code.

***

## Install with a plugin (recommended)

Plugins are the recommended way to install the AI Toolkit. The plugin bundles everything into a single install and updates automatically as new capabilities are released.

#### Claude Code

In your terminal, run `claude plugin install`:

## Terminal

```terminal
claude plugin install shopify-ai-toolkit@claude-plugins-official
```

#### Codex

In your terminal, run `codex plugin add`:

## Terminal

```terminal
codex plugin add shopify@openai-curated
```

#### Antigravity CLI

In your terminal, install the Shopify plugin:

## Terminal

```terminal
agy plugin install https://github.com/Shopify/shopify-ai-toolkit
```

#### Cursor

In Cursor Chat, add the Shopify plugin:

## Cursor Chat

```terminal
/add-plugin shopify
```

#### Hermes

In your terminal, download the install script and run it:

## Terminal

```terminal
curl -fsSL https://raw.githubusercontent.com/Shopify/Shopify-AI-Toolkit/main/.hermes-plugin/install.sh -o /tmp/shopify-hermes-install.sh
bash /tmp/shopify-hermes-install.sh
```

#### OpenClaw

In your terminal, install the Shopify plugin from npm:

## Terminal

```terminal
openclaw plugins install npm:@shopify/ai-toolkit
```

#### Pi

In your terminal, install the package from npm:

## Terminal

```terminal
pi install npm:@shopify/ai-toolkit
```

#### VS Code

1. Ensure the [Agent plugins](https://code.visualstudio.com/docs/copilot/customization/agent-plugins) preview is enabled in your VS Code settings.

2. Open the Command Palette (`Cmd+Shift+P` on macOS, `Ctrl+Shift+P` on Windows/Linux) and run:

   ## VS Code: Command Palette

   Chat: Install Plugin From Source

3. When prompted, enter the repository URL:

   ## VS Code: Plugin source URL

   https://github.com/Shopify/shopify-ai-toolkit

***

## Install with agent skills

If your AI tool doesn't support plugins, or you'd rather manage skills yourself, then you can install the toolkit's agent skills directly. The `shopify` skill covers every Shopify developer surface, including the GraphQL Admin API, Shopify Functions, Polaris, Liquid, Hydrogen, and Shopify CLI. Your agent reads the guidance for a surface only when a task needs it. You can [view the skill on GitHub](https://github.com/Shopify/Shopify-AI-Toolkit/tree/main/skills/shopify).

To install the toolkit's skills:

## Terminal

```terminal
npx skills add Shopify/shopify-ai-toolkit
```

Unlike the plugin, skills that you install this way don't update automatically. To get the latest versions, run `npx skills update`.

### Migrate from individual skills

Earlier versions of the toolkit shipped a separate skill for each surface, such as `shopify-admin` and `shopify-liquid`. These skills are deprecated and no longer receive updates. If you installed any of them, then replace them with the `shopify` skill. For a global install, add the `-g` flag to each command.

1. Remove the individual skills. The command skips any skills that you didn't install:

   ## Terminal

   ```terminal
   npx skills remove shopify-admin shopify-admin-execution shopify-app-pricing shopify-app-review shopify-app-store-review shopify-custom-data shopify-customer shopify-dev shopify-functions shopify-hydrogen shopify-liquid shopify-onboarding-dev shopify-onboarding-merchant shopify-partner shopify-payments-apps shopify-polaris-admin-extensions shopify-polaris-app-home shopify-polaris-checkout-extensions shopify-polaris-customer-account-extensions shopify-pos-ui shopify-shopifyql shopify-storefront-graphql shopify-use-shopify-cli
   ```

2. Install the toolkit's skills:

   ## Terminal

   ```terminal
   npx skills add Shopify/shopify-ai-toolkit
   ```

***

## Install with the Dev MCP server

If you prefer MCP, you can connect to Shopify's developer resources through the Dev MCP server. The server runs locally and doesn't require authentication.

#### Claude Code

1. In your terminal, tell `claude` to add the MCP server:

   ## Terminal

   ```terminal
   claude mcp add --transport stdio shopify-dev-mcp -- npx -y @shopify/dev-mcp@latest
   ```

2. Restart Claude Code to load the new configuration.

#### Codex CLI

1. Add this configuration to your `~/.codex/config.toml` file:

   ## Codex configuration

   ```toml
   [mcp_servers.shopify-dev-mcp]
   command = "npx"
   args = ["-y", "@shopify/dev-mcp@latest"]
   ```

   **Note:**

   Codex uses TOML format with `mcp_servers` (snake\_case) instead of JSON with `mcpServers` (camelCase). For more information, see the [Codex MCP documentation](https://github.com/openai/codex/blob/main/docs/config.md#mcp_servers).

2. Restart Codex to load the new configuration.

#### Antigravity CLI

1. Add this configuration to your `~/.gemini/config/mcp_config.json` file:

   ## Antigravity CLI configuration

   ```json
   {
     "mcpServers": {
       "shopify-dev-mcp": {
         "command": "npx",
         "args": ["-y", "@shopify/dev-mcp@latest"]
       }
     }
   }
   ```

2. Restart Antigravity CLI to load the new configuration.

#### Cursor

1. Open Cursor and go to **Cursor** > **Settings** > **Cursor Settings** > **Tools and MCP** > **New MCP server**.

2. Add this configuration to your MCP servers (or [use this link](https://cursor.com/en/install-mcp?name=shopify-dev-mcp\&config=eyJjb21tYW5kIjoibnB4IC15IEBzaG9waWZ5L2Rldi1tY3BAbGF0ZXN0In0%3D) to add it automatically):

   ## Cursor configuration

   ```json
   {
     "mcpServers": {
       "shopify-dev-mcp": {
         "command": "npx",
         "args": ["-y", "@shopify/dev-mcp@latest"]
       }
     }
   }
   ```

   If you see connection errors on Windows, try this alternative configuration:

   ## Alternative configuration for Windows

   ```json
   {
     "mcpServers": {
       "shopify-dev-mcp": {
         "command": "cmd",
         "args": ["/k", "npx", "-y", "@shopify/dev-mcp@latest"]
       }
     }
   }
   ```

3. Save your configuration and restart Cursor.

#### VS Code

1. Open VS Code and open the Command Palette (`Cmd+Shift+P` on MacOS, `Ctrl+Shift+P` on Windows/Linux).

2. Search for and select **MCP: Open User Configuration**.

3. Add this configuration to your user-level `mcp.json` file:

   ## VS Code MCP configuration

   ```json
   {
     "servers": {
       "shopify-dev-mcp": {
         "command": "npx",
         "args": ["-y", "@shopify/dev-mcp@latest"]
       }
     }
   }
   ```

4. Save your configuration and restart VS Code.

***

## Example: migrate extensions with the toolkit

One clear use case is extension migration. Checkout and customer account Shopify Extensions on API versions before 2025-10 need to adopt Polaris web components when upgrading to newer API versions.

These migrations involve repetitive, detail-heavy work:

* Updating the extension API version in `shopify.extension.toml`.
* Converting React-based extension code to Preact where required.
* Replacing legacy components with Polaris web components.
* Updating extension APIs and target-specific imports.
* Reviewing the migration guide to confirm all required steps.
* Running and testing the migrated extension locally.

With the toolkit installed, you can ask your agent to handle the migration. For example:

## Example prompt

Migrate the extensions/my-checkout-extension extension to API version 2026-04.

The toolkit doesn't remove the need to review and test the result. It helps automate the bulk of the migration work so you can spend more time validating behavior and preparing the updated extension for release.

***

## Next steps

After installing, your AI tool automatically draws on Shopify's developer resources when you ask it Shopify-related questions. Ask it to:

* Use Shopify CLI to scaffold a new Shopify app.
* Explain what Shopify app surfaces are and help you choose the right one.
* Explore Shopify APIs and find the right one for your use case.
* Review your app against Shopify App Store requirements.

***
