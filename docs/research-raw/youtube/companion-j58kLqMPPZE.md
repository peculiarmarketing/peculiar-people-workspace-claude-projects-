# Companion for j58kLqMPPZE: Maelify blog post + Shopify-AI-Toolkit GitHub README

- URL 1: https://www.maelify.com/blogs/news/claude-code-shopify-zero-to-hero (blog dated April 13, 2026)
- URL 2: https://raw.githubusercontent.com/Shopify/Shopify-AI-Toolkit/main/README.md (repo https://github.com/Shopify/Shopify-AI-Toolkit linked in description)
- Fetched: 2026-10-03 with curl (browser UA), HTML stripped to text

## Part 1: Maelify blog

Skip to content

 ● LIVE DEMO STORE · Travel Kit · headless DTC build, Shopify + Vercel + Claude Code ↗

 ● LIVE DEMO STORE · Travel Kit · headless DTC build, Shopify + Vercel + Claude Code ↗

 Home

 Services

 Case Studies

 Insights

 Book an Architecture Review

 More

 Home

 Services

 Case Studies

 Insights

 Book an Architecture Review

 More

 Account

 Other sign in options

 Sign in

 Orders

 Profile

 Account

 Other sign in options

 Sign in

 Orders

 Profile

 Total items in cart: 0

0

 Your cart is empty

 Have an account? Log in to check out faster.

 Continue shopping

 Claude Code + Shopify: Zero to Hero

April 13, 2026

 This article ships alongside the YouTube video Claude Code + Shopify: Zero to Hero. Watch it, then keep this tab open as a cheat sheet.

The problem with AI + Shopify, until now

Most AI coding workflows break the moment you touch a Shopify theme. The model hallucinates Liquid filters that do not exist, invents schema fields, and writes to the wrong theme. You end up copy-pasting between ChatGPT, your editor, and the theme editor, fixing broken output as you go. The flow is gone.

Claude Code plus the Shopify AI Toolkit plugin fixes that. The plugin gives the agent first-class access to Shopify docs, the Admin GraphQL schema, Liquid validation, and store execution. The agent stays in your terminal. No tab juggling.

The stack

Claude Code: Anthropic's CLI coding agent. Runs in your terminal, reads and edits files, runs shell commands, loads plugins.

Shopify AI Toolkit: Official plugin that exposes Shopify documentation, Admin GraphQL, Liquid, Hydrogen, Functions, and more as agent skills.

Shopify CLI: Pushes theme files to any theme on any store you own.

Install in 10 seconds

Copy Paste this prompt into Claude Code:

Install https://github.com/Shopify/Shopify-AI-Toolkit plugins

That is it. The agent now has Shopify brains.

What we shipped in this video

Live, on air, we added a new Latest Videos section to the Maelify DEV theme. One prompt, one image, one push. Here is the full flow:

Ask the agent to list the store's themes. It ran an Admin GraphQL query, returned the live theme and the DEV theme with their IDs. No dashboard required.

Describe the section: a centered video card that uses the dark scheme-5 color scheme, takes a YouTube URL, a thumbnail, a heading, and a subheading. The agent wrote sections/maelify-latest-video.liquid with a proper schema, scoped CSS, and a YouTube play-button overlay.

Upload the thumbnail. The agent ran Shopify's three-step staged upload (stagedUploadsCreate, POST to the signed Google Cloud Storage URL, fileCreate), polled until the file was READY, and returned a shopify://shop_images/... reference for the section settings.

Wire the section into templates/index.json. The agent added a new instance under sections, appended the key to order, and set the heading, YouTube URL, and color scheme.

Push to the DEV theme using shopify theme push --theme=<dev-theme-id> --only with the section file and template. Only the files that changed. No cleanup pass on unrelated remote files.

The one command you should steal

When you push to a specific theme, always scope it and always pass --nodelete:

set -a && source .env && set +a && shopify theme push \
 --store="$SHOPIFY_STORE" \
 --password="$SHOPIFY_ADMIN_API_TOKEN" \
 --theme=<theme-id> \
 --only=sections/<file>.liquid \
 --only=templates/<file>.json \
 --nodelete

Source the token, never paste it. Pass it as a variable. If you record your screen, your viewers will never see the credential.

Grab the starter CLAUDE.md

The file below is a clean, reusable CLAUDE.md you can drop at the root of any Shopify theme repo. Claude Code will load it automatically when you start a session in that directory. Copy it inline, or use the download button.

 CLAUDE.md

⬇ DOWNLOAD

# CLAUDE.md, Shopify Theme Project

Starter instructions for Claude Code working on a Shopify theme.
Drop this file at the root of your theme repo. Claude Code will load it automatically.

## Stack

- Claude Code as the primary agent (terminal)
- Shopify AI Toolkit plugin: `/plugin marketplace add Shopify/shopify-ai-toolkit` then `/plugin install shopify-plugin@shopify-ai-toolkit`
- Shopify CLI for theme deploys
- Liquid, JSON templates, scoped `{% stylesheet %}` blocks

## Environment

Credentials live in `.env` (gitignored). Variables:

- `SHOPIFY_STORE` = `yourstore.myshopify.com`
- `SHOPIFY_ADMIN_API_TOKEN` = Admin API access token (starts with `shpat_`)

Never paste the token inline. Always source the env file:

```bash
set -a && source .env && set +a
```

If you are recording your screen, anything that appears in terminal output is public. Use variable interpolation, not literal values.

## Deploy

Push individual files to a specific theme. Always scope with `--only` and always pass `--nodelete` so Shopify CLI does not run a cleanup pass on unrelated remote files:

```bash
set -a && source .env && set +a && shopify theme push \
 --store="$SHOPIFY_STORE" \
 --password="$SHOPIFY_ADMIN_API_TOKEN" \
 --theme=<theme-id> \
 --only=sections/<file>.liquid \
 --only=templates/<file>.json \
 --nodelete
```

For the live theme, add `--allow-live`.

## JSON templates

Shopify auto-generates a `/* ... */` banner at the top of JSON template files. Do not remove it. Shopify CLI and the theme editor accept these files as-is. Standard `json.loads()` fails on them, strip the first comment if you need to validate locally.

## Section + block settings

Reference uploaded images using the `shopify://shop_images/<filename>` scheme, not the CDN URL. The filename is whatever you uploaded to Shopify Files.

## Uploading images to Shopify Files (GraphQL, 3 steps)

1. `stagedUploadsCreate` mutation returns a signed Google Cloud Storage target with form parameters.
2. `POST` the bytes to that URL as multipart form data, including every parameter Shopify returned plus `file=@localpath`. Expect HTTP 201.
3. `fileCreate` mutation with `originalSource` set to the staged `resourceUrl` registers the file. Poll `node(id)` until `fileStatus` becomes `READY`.

## Theme check

```bash
shopify theme check --path . --fail-level error
```

If your repo has pre-existing errors you cannot fix, grep the output for the file you just touched to confirm you did not introduce new offenses:

```bash
shopify theme check --path . --fail-level error 2>&1 | grep -A 3 "<your-file>"
```

## Color schemes

Defined in `config/settings_schema.json` and `config/settings_data.json`. Reference them as `scheme-1`, `scheme-2`, etc. in section settings. Use scoped `{% stylesheet %}` blocks in sections and rely on the theme color-scheme classes rather than hardcoding colors.

## Section schema convention

```json
{
 "name": "Your Section",
 "tag": "section",
 "class": "section-your-kebab",
 "settings": [ ... ],
 "presets": [{ "name": "Your Section" }]
}
```

Presets make the section available in the theme editor's "Add section" menu.

## Security rules

- Never commit `.env`, `.env.*`, or any file with tokens
- Never inline credentials in bash commands or commits
- Never paste API keys into curl commands or environment update commands
- If a credential appears in your command, stop and find an alternative approach

## Pre-push scan

Run this before every push:

```bash
git log --all -p | grep -iE "(password|secret|token|shpat_|shpss_|sk-)"
```

Anything found: stop, rotate the credential, clean history, then push.

## Writing style for code comments

- Concise, why-not-what
- No decorative comment blocks
- Do not explain what well-named code already says

Direct link: cdn.shopify.com/…/CLAUDE.md

Takeaway

The gap between "I have an idea" and "it is live on a theme" used to be an afternoon. With Claude Code plus the Shopify AI Toolkit, it is one prompt. The agent knows the APIs, the schemas, and the CLI. You stay in the terminal. You ship.

If you run a Shopify store, install the plugin today. If you build for merchants, it will change how you quote work.

Watch the full build on YouTube: Claude Code + Shopify: Zero to Hero.

 Join our email list

 Get exclusive deals and early access to new products. 

 Email

 © 2026
 Maelify, Powered by Shopify

 Privacy policy

 Terms of service

 Contact information

 Refund policy

 Facebook

 Instagram

 Tiktok

 Youtube

 Payment methods

 Search

 Clear

 Products

 Anchor Latch · MO-A1

 Anchor Latch · MO-A1

 €28,00

 Cube · L

 Cube · L

 €58,00

 Cube · M

 Cube · M

 €48,00

 Cube · S

 Cube · S

 €38,00

 View all

## Part 2: GitHub README (raw markdown)

# Shopify AI Toolkit - AI Agent Plugin

Connect your AI tools to the Shopify platform.

The Toolkit gives your agent access to Shopify's documentation, API schemas, and code validation for building apps, and store management through the CLI's store execute capabilities. For more info, [see the docs](https://shopify.dev/docs/apps/build/ai-toolkit).

## Install

- **For Claude Code**: In your terminal, run `claude plugin install`:

  ```
  claude plugin install shopify-ai-toolkit@claude-plugins-official
  ```

- **For OpenAI Codex**: In your terminal, run `codex plugin add`:

  ```
  codex plugin add shopify@openai-curated
  ```

- **For Antigravity CLI**: In your terminal, install the Shopify plugin:

  ```
  agy plugin install https://github.com/Shopify/shopify-ai-toolkit
  ```

- **For Cursor**: In Cursor Chat, add the Shopify plugin:

  ```
  /add-plugin shopify
  ```

- **For Hermes**: In your terminal, download the install script and run it:

  ```
  curl -fsSL https://raw.githubusercontent.com/Shopify/Shopify-AI-Toolkit/main/.hermes-plugin/install.sh -o /tmp/shopify-hermes-install.sh
  bash /tmp/shopify-hermes-install.sh
  ```

- **For OpenClaw**: In your terminal, install the package from npm:

  ```
  openclaw plugins install npm:@shopify/ai-toolkit
  ```

  Alternatively, install from ClawHub with `openclaw plugins install clawhub:@shopify/ai-toolkit`, or directly from the git mirror with `openclaw plugins install git:github.com/Shopify/Shopify-AI-Toolkit`. The plugin is recognized as a native OpenClaw plugin and a compatible Agent Plugins bundle.

- **For Pi**: In your terminal, install the package from npm:

  ```
  pi install npm:@shopify/ai-toolkit
  ```

  Alternatively, install directly from the git mirror:

  ```
  pi install git:github.com/Shopify/Shopify-AI-Toolkit
  ```

- **For VS Code**:
  1. Ensure the [Agent plugins](https://code.visualstudio.com/docs/copilot/customization/agent-plugins) preview is enabled in your VS Code settings.

  2. Open the Command Palette (`Cmd+Shift+P` on macOS, `Ctrl+Shift+P` on Windows/Linux) and run:

     ```
     Chat: Install Plugin From Source
     ```

  3. When prompted, enter the repository URL:

     ```
     https://github.com/Shopify/shopify-ai-toolkit
     ```

## What you get

- **Docs and API schemas**: Search Shopify's documentation and API schemas without leaving your editor
- **Code validation**: Validate GraphQL queries, Liquid templates, and UI extensions against Shopify's schemas
- **Store management**: Manage your Shopify store through the CLI's store execute capabilities
- **Auto-updates**: The plugin updates automatically as new capabilities are released

## Telemetry

The skill scripts (`scripts/search_docs.mjs`, `scripts/validate.mjs`, `scripts/log_skill_use.mjs`) send a usage event to `https://shopify.dev/mcp/usage` on each invocation. The payload includes:

- tool name, skill name and version
- model name, client name, and client version (when supplied as flags)
- the search query text and search response or error text (for `search_docs.mjs`)
- the validation result, the validated code when present, and validator-specific context such as API name, extension target, filename, file type, theme path, and file list (for `validate.mjs`)
- artifact ID and revision number (when supplied)
- the routing-table topic in use, from `--topic` for `log_skill_use.mjs`, and for
  `search_docs.mjs` from `--api` on a scoped search or `--topic` on an unscoped one
- the user's most recent message verbatim (truncated to 2000 chars), when the agent passes it base64-encoded via `--user-prompt-base64` to `validate.mjs` (for topics with a validator) or `log_skill_use.mjs` (for topics without). Encoding the prompt keeps untrusted message text out of shell syntax. Exactly one designated capture point per topic, `search_docs.mjs` does not carry user_prompt.
- the agent's `sessionId` and `toolUseId` (when supplied via `--session-id` / `--tool-use-id`) so analytics can join script events with the hook's `skill_invocation` event for the same activation.

The plugin also registers a `PostToolUse` hook (`hooks/track-telemetry.sh`, `.ps1`) on Claude Code, Cursor, and GitHub Copilot. It emits a `skill_invocation` event to the same endpoint whenever the agent calls the host `Skill` tool with a Shopify AI Toolkit skill or reads a `SKILL.md` from a recognized install path. The payload includes:

- skill name, skill version (when recoverable from the install path)
- trigger (`skill-tool` or `skill-md-read`)
- detected client (`claude-code` / `cursor` / `copilot-cli` / `vscode` / `vscode-insiders`)
- hook source (`plugin` or `skill`)
- the agent's `sessionId` and `toolUseId` (when supplied)
- on Claude Code only: the user's most recent prompt verbatim (truncated to 2000 chars), captured out-of-band via a `UserPromptSubmit` hook that stashes it locally and attached here only when a skill activates. Honors `OPT_OUT_INSTRUMENTATION`; other hosts carry no prompt on this surface.

The same script is also injected into each generated SKILL.md as a `hooks:` frontmatter block, so Claude Code emits the same event when skills are installed standalone (e.g. via `npx skills add Shopify/shopify-ai-toolkit`) without the plugin. Events from each source are labeled with `hookSource` and carry `sessionId` + `toolUseId` inside the body's `parameters` object, so downstream consumers can dedup on `(sessionId, toolUseId)` when both surfaces are installed.

The hook does not report tool inputs, file contents, generated code, or other tool arguments. On Claude Code it can additionally attach `user_prompt` (the most recent prompt verbatim) via the `UserPromptSubmit` stash, but only when a Shopify skill activates. On other hosts (Cursor, Copilot) the hook carries no prompt and `user_prompt` capture happens on the script surfaces only (`validate.mjs` for topics with a validator, `log_skill_use.mjs` for topics without). See [`hooks/README.md`](./hooks/README.md) for full coverage details.

### Opting out

Telemetry is **on by default**. Opting out applies to every surface at once, skill scripts, the MCP server, and the hooks, and also stops local capture (no prompt is stashed to disk).

There are two ways to opt out. Either is sufficient on its own.

**1. A user-level opt-out file (recommended).** This is the only method that reliably works everywhere, because it does not depend on the agent passing your shell environment through to the processes it spawns:

```sh
mkdir -p ~/.config/shopify-ai-toolkit && touch ~/.config/shopify-ai-toolkit/opt-out
```

The file is checked at:

| Platform      | Path                                                                                       |
| ------------- | ------------------------------------------------------------------------------------------ |
| Linux / macOS | `$XDG_CONFIG_HOME/shopify-ai-toolkit/opt-out`, else `~/.config/shopify-ai-toolkit/opt-out` |
| macOS (also)  | `~/Library/Application Support/shopify-ai-toolkit/opt-out`                                 |
| Windows       | `%APPDATA%\shopify-ai-toolkit\opt-out`                                                     |

An empty file opts you out, the filename is the signal. Writing `false`, `0`, `no`, or `off` into it means "present, but do not opt me out", which is useful if the file is managed by a dotfiles repo. Set `SHOPIFY_AI_TOOLKIT_OPT_OUT_FILE` to point every surface at a different absolute path.

**2. An environment variable.**

```sh
export OPT_OUT_INSTRUMENTATION=true
```

`DO_NOT_TRACK=1` ([donottrack.sh](https://donottrack.sh/)) is honored as well.

Environment variables only reach a telemetry surface if the process emitting it inherits your exported environment. Several hosts spawn skill scripts, hooks, MCP child processes, and sub-agents from non-interactive subshells that do not, Hermes' `terminal` tool, Codex's `exec` mode, and GUI-launched MCP servers among them. If you use one of those, use the file.

**Opt-out is monotone.** Any signal that says "opted out" wins, and nothing can turn telemetry back on for that process. In particular, a wrapper script or CI image exporting `OPT_OUT_INSTRUMENTATION=false` cannot override the file you created.

## Other install methods

If your platform doesn't support plugins, you can install agent skills or the Dev MCP server directly. For instructions, see [shopify.dev/docs/apps/build/ai-toolkit](https://shopify.dev/docs/apps/build/ai-toolkit).

## Contributing

Thanks for your interest but we don't accept pull requests. Any pull requests will be automatically closed.
