# 07. Shopify Dev MCP server and Shopify AI Toolkit

## https://shopify.dev/docs/apps/build/ai-toolkit
> "Shopify AI Toolkit gives your AI coding tool a Shopify-aware starting point. The toolkit connects your agent to: Developer docs and API schemas ... Code validation: validate GraphQL queries, Liquid templates, and Shopify Extensions against Shopify schemas ... Store management: prepare and run supported store-management tasks through Shopify CLI's authenticated store context"
> Requirements: "Node.js 18 or higher" ; supported "Claude Code, Codex, Antigravity CLI, Cursor, Hermes (plugin only), OpenClaw (plugin only), Pi (plugin only), or Visual Studio Code."
> "Plugins are the recommended way to install the AI Toolkit."
Claude Code plugin install (verbatim):
```
claude plugin install shopify-ai-toolkit@claude-plugins-official
```
Agent skills install:
```
npx skills add Shopify/shopify-ai-toolkit
```
> "The shopify skill covers every Shopify developer surface, including the GraphQL Admin API, Shopify Functions, Polaris, Liquid, Hydrogen, and Shopify CLI." ; "Unlike the plugin, skills that you install this way don't update automatically. To get the latest versions, run npx skills update." ; "Earlier versions of the toolkit shipped a separate skill for each surface, such as shopify-admin and shopify-liquid. These skills are deprecated"
Dev MCP server for Claude Code (verbatim):
```
claude mcp add --transport stdio shopify-dev-mcp -- npx -y @shopify/dev-mcp@latest
```
> "The server runs locally and doesn't require authentication." "Restart Claude Code to load the new configuration."

## Changelog Oct 1, 2025: https://shopify.dev/changelog/posts/dev-mcp-now-supports-liquid
> "The Shopify Dev MCP server can now search for Liquid docs, and validate Liquid to catch common errors before deployment ... The built-in theme-check integration identifies syntax errors and best practice violations in your generated code"

## npm README, @shopify/dev-mcp v1.16.0 (registry.npmjs.org, fetched 2026-10-03)
> "lets AI agents search Shopify's documentation and API schemas, validate GraphQL operations, Liquid and theme files, and UI-extension code, and resolve supported API versions."
> "`LIQUID_VALIDATION_MODE` defaults to `full`, which exposes `validate_theme` for validating entire theme directories. Set it to `partial` to validate individual code blocks instead: `validate_theme` is not registered, and `liquid` joins the `api` enum of the merged `validate` tool."
> Telemetry: "Published release builds send usage events to https://shopify.dev/mcp/usage ... Events can include tool inputs and results". Opt out: `mkdir -p ~/.config/shopify-ai-toolkit && touch ~/.config/shopify-ai-toolkit/opt-out` or `OPT_OUT_INSTRUMENTATION=true` or `DO_NOT_TRACK=1`.

## Tool names found in the v1.16.0 package source (dist/index-*.js), inspected locally
learn_shopify_api, search_docs_chunks, validate, validate_theme, validate_theme_codeblocks, validate_graphql_codeblocks, validate_component_codeblocks, feedback.
- learn_shopify_api description: "MANDATORY FIRST STEP: This tool MUST be called before any other Shopify tools ... ALL OTHER SHOPIFY TOOLS WILL FAIL without a conversationId from this tool."
- validate_theme: "This tool validates Liquid codeblocks, Liquid files, and supporting Theme files (e.g. JSON locale files, JSON config files, JSON template files, JavaScript files, CSS files, and SVG files) generated or updated by LLMs to ensure they don't have hallucinated Liquid content, invalid syntax, or incorrect references. Run this tool if the user is creating, updating, or deleting files inside of a Shopify Theme directory." Inputs: absoluteThemePath, filesCreatedOrUpdated[].path
- validate: "MANDATORY after generating or editing Shopify code ... One call validates one `api`"
NOTE: Which of these are registered at runtime depends on version and LIQUID_VALIDATION_MODE; validate_graphql_codeblocks / validate_component_codeblocks / validate_theme_codeblocks may be legacy names superseded by the merged `validate` tool. Not confirmed on shopify.dev itself; the shopify.dev pages returned did not list tool names.

## Shopify-adjacent: Polaris page https://shopify.dev/docs/api/polaris/using-mcp
> `npx -y @shopify/dev-mcp@latest` ; JSON config `{ "mcpServers": { "shopify-dev-mcp": { "command": "npx", "args": ["-y", "@shopify/dev-mcp@latest"] } } }` (this page says node 20 or higher; AI toolkit page says Node.js 18 or higher; README says Node.js 18 or later.)
