# Raw notes: Anthropic docs, GitHub, design tools (researched 2026-10-03)

Method notes:
- WebFetch on code.claude.com returns text through a summarizing model. Quotes from it marked "WebFetch quote" are what that model returned when asked for verbatim text; treat as near-verbatim, verify on the live page before publishing.
- GitHub MCP was scoped to three peculiarmarketing repos; `get_file_contents` on Shopify repos was denied. Repo search and code search worked across GitHub. File contents were pulled with `curl` from raw.githubusercontent.com (allowed by the proxy). Those quotes are exact (byte copies from the fetched file).
- shopify.dev and instagram.com are blocked by the egress proxy (WebFetch EGRESS_BLOCKED; curl CONNECT 403).
- "updated_at" below is GitHub repo metadata (last metadata/push activity), not necessarily last commit.
- Some quoted source text contains em dashes. They are kept only inside verbatim quotes.

---------------------------------------------------------------------------
## PART 1: Anthropic Claude Code docs

### Skills: https://code.claude.com/docs/en/skills (WebFetch, full page)
Minimal format (WebFetch quote):
```yaml
---
name: my-skill
description: What this skill does
---

Your skill instructions here...
```
- "All fields are optional. Only `description` is recommended."
- `name`: "Command name shown in the `/` menu. Defaults to the directory name."
- `description`: "What the skill does and when to use it. Claude uses this to decide when to apply the skill. If omitted, uses the first non-empty line of the markdown content. Combined `description` and `when_to_use` text is truncated at 1,536 characters in the skill listing."
- `allowed-tools`: "Tools Claude can use without asking permission during the turn that invokes this skill. Accepts a space- or comma-separated string, or a YAML list."
- Other fields listed: when_to_use, argument-hint, arguments, disable-model-invocation, user-invocable, disallowed-tools, model, effort, context (fork), agent, background, hooks, paths, shell, metadata, license, compatibility.
- Locations: Personal `~/.claude/skills/<skill-name>/SKILL.md`; Project `.claude/skills/<skill-name>/SKILL.md`; Plugin `<plugin>/skills/<skill-name>/SKILL.md` (invoked as `/plugin-name:skill-name`).
- `!`command`` blocks inject shell output into the skill (example uses `!`git diff HEAD``).

### Subagents: https://code.claude.com/docs/en/sub-agents (WebFetch)
Example (WebFetch quote):
```markdown
---
name: code-reviewer
description: Reviews code for quality and best practices
tools: Read, Glob, Grep
model: sonnet
---

You are a code reviewer. When invoked, analyze the code and provide
specific, actionable feedback on quality, security, and best practices.
```
- "Only `name` and `description` are required."
- `tools`: "comma-separated string such as `Read, Grep, Bash` or a YAML list. Inherits every tool available to subagents if omitted."
- `model`: "`sonnet`, `opus`, `haiku`, `fable`, a full model ID such as `claude-opus-5-5`, or `inherit`."
- Others: disallowedTools, permissionMode, maxTurns, skills, mcpServers, hooks, memory, background, omitClaudeMd, effort, isolation (worktree), color, initialPrompt, experimental.
- Locations/priority: managed settings (1), `--agents` CLI flag (2), `.claude/agents/` (3, project), `~/.claude/agents/` (4, user), plugin `agents/` (5).

### Hooks: https://code.claude.com/docs/en/hooks (WebFetch x2)
PostToolUse example on file writes (WebFetch quote):
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "/path/to/lint-check.sh"
          }
        ]
      }
    ]
  }
}
```
- Exit 2: "Exit 2 means a blocking error. On events that can block, exit 2 blocks whether or not you print JSON: even a JSON `permissionDecision` of `"allow"` can't override it."
- Per-event table: PreToolUse "Yes | Blocks the tool call"; PostToolUse "No | Shows stderr to Claude; the tool already ran"; Stop "Yes | Prevents Claude from stopping, continues the conversation"; UserPromptSubmit "Yes | Blocks the prompt, so it never reaches Claude".
- Other exit codes: non-blocking error for most events; transcript shows "`<hook name> hook error`" with first stderr line.
- Input: JSON on stdin (session_id, cwd, hook_event_name, tool_name, tool_input, ...).
- `${CLAUDE_PROJECT_DIR}` placeholder, also exported as env var.
- Config files: `~/.claude/settings.json` (all projects), `.claude/settings.json` (project, committable), `.claude/settings.local.json` (project, not committed).
- Events include SessionStart, UserPromptSubmit, PreToolUse, PostToolUse, PostToolUseFailure, PermissionRequest, Stop, SessionEnd, FileChanged, SubagentStart/Stop, PreCompact, and more.

### Memory / CLAUDE.md: https://code.claude.com/docs/en/memory (WebFetch, full page saved, exact lines grepped)
- Managed policy: macOS `/Library/Application Support/ClaudeCode/CLAUDE.md`, Linux `/etc/claude-code/CLAUDE.md`.
- User: `~/.claude/CLAUDE.md`. Project: `./CLAUDE.md` or `./.claude/CLAUDE.md`. Local: `./CLAUDE.local.md` ("add to `.gitignore`").
- Imports: "CLAUDE.md files can import additional files using `@path/to/import` syntax."
- Size: "target under 200 lines per CLAUDE.md file. Longer files consume more context and reduce adherence."
- Memory is advisory: "Claude treats them as context, not enforced configuration. To block an action regardless of what Claude decides, use a PreToolUse hook instead."
- Path-scoped rules in `.claude/rules/*.md`:
```markdown
---
paths:
  - "src/api/**/*.ts"
---
```
  "Path-scoped rules trigger when Claude uses the Read, Write, or Edit tool on a file matching the pattern".
- AGENTS.md is read when no CLAUDE.md exists (default setting `claude-md-or-agents-md`).

### MCP: https://code.claude.com/docs/en/mcp (WebFetch)
- HTTP: `claude mcp add --transport http <name> <url>` (example `claude mcp add --transport http notion https://mcp.notion.com/mcp`)
- SSE: `claude mcp add --transport sse <name> <url>`
- stdio: `claude mcp add [options] <name> -- <command> [args...]`; "The `--` (double dash) separates Claude's options from the server command and arguments."
- Scopes: local (default, `~/.claude.json`, private, this project), project (`.mcp.json` at root, shared via git, approval prompt), user (`~/.claude.json`, all projects).
- `.mcp.json`:
```json
{
  "mcpServers": {
    "shared-server": {
      "type": "http",
      "url": "https://example.com/mcp"
    }
  }
}
```

---------------------------------------------------------------------------
## PART 2: GitHub

### OFFICIAL (Shopify) Shopify/liquid-skills
URL https://github.com/Shopify/liquid-skills | desc "Liquid language support plugin for Claude Code" | stars 35 | created 2026-03-13 | updated_at 2026-09-21 | commits page shows last commit Mar 18, 2026 (5 commits).
README (exact):
```
/plugin marketplace add Shopify/liquid-skills
/plugin install liquid-lsp@liquid-skills
/plugin install liquid-skills@liquid-skills
```
"The [Shopify CLI](https://shopify.dev/docs/api/shopify-cli) must be installed (required by the LSP plugin): `npm install -g @shopify/cli`"
Skills: shopify-liquid-themes, liquid-theme-standards, liquid-theme-a11y.

plugins/liquid-skills/skills/shopify-liquid-themes/SKILL.md (314 lines, read fully). Exact frontmatter:
```
name: shopify-liquid-themes
description: "Generate Shopify Liquid theme code (sections, blocks, snippets) with correct schema JSON, LiquidDoc headers, translation keys, and CSS/JS patterns. Use when creating or editing .liquid files for Shopify themes, working with schema, doc, stylesheet, javascript tags, or Shopify Liquid objects/filters/tags."
```
Exact rules:
- "Sections and blocks require `{% schema %}` with a valid JSON object. Sections use `section.settings.*`, blocks use `block.settings.*`."
- Critical gotchas: "No parentheses in conditions", "No ternary", "`for` loops max 50 iterations", "`{% stylesheet %}`/`{% javascript %}` don't render Liquid", "Snippets can't access outer-scope variables", "`include` is deprecated".
- "One tag each per file", "No Liquid inside", "Only supported in `sections/`, `blocks/`, and `snippets/`".
- `{% style %}` for Liquid-aware CSS (e.g. `.section-{{ section.id }}`).
- "Single CSS property: use CSS variables"; "Multiple CSS properties: use CSS classes as select values".
- "Every user-facing string must use the `t` filter"; keys snake_case, max 3 levels, sentence case, schema labels with `t:` prefix.
- Section schema example includes `"presets": [{ "name": "t:sections.hero.name" }]`, `"blocks": [{ "type": "@theme" }]`, `enabled_on` / `disabled_on`.
- Range: "`min`, `max`, `default` (all required), `step`, `unit`".

liquid-theme-standards/SKILL.md (429 lines, head read): principles "Progressive enhancement", "No external dependencies, native browser APIs only for JavaScript", "Design tokens, never hardcode colors, spacing, or fonts", "BEM naming", "Defensive CSS".
liquid-theme-a11y/SKILL.md (477 lines, head read): "Every interactive component must work with keyboard only, screen readers, and reduced-motion preferences." Decision table maps carousel, modal (`<dialog>`), accordion (`<details>`), etc.

### OFFICIAL (Shopify) Shopify/Shopify-AI-Toolkit
URL https://github.com/Shopify/Shopify-AI-Toolkit | stars 584 | created 2026-04-01 | updated_at 2026-10-02 | 74 commits.
Install (exact): `claude plugin install shopify-ai-toolkit@claude-plugins-official`
"If your platform doesn't support plugins, you can install agent skills or the Dev MCP server directly."
Telemetry (exact): "Telemetry is **on by default**." Opt-out: `mkdir -p ~/.config/shopify-ai-toolkit && touch ~/.config/shopify-ai-toolkit/opt-out` or `export OPT_OUT_INSTRUMENTATION=true`. Plugin registers a PostToolUse hook; on Claude Code it can attach "the user's most recent prompt verbatim (truncated to 2000 chars)" when a Shopify skill activates. validate.mjs sends "the validated code when present".
"we don't accept pull requests".
skills/shopify/SKILL.md (123 lines, read fully): one skill `shopify`, version "1.17.1", routing table; liquid row: search `--api liquid`, validate `--api liquid --filename <name.liquid> --filetype <filetype> --context <theme|app>`. "Validation is mandatory: never return generated code you have not run through this command". "Three attempts, then return your best effort with an explanation."
references/liquid.md (278 lines, head read): full-theme mode `--api liquid --theme-path <absolute-path-to-theme> --files <rel1,rel2,...>`; "Use `{{ block.shopify_attributes }}` on block wrapper elements for theme editor drag-and-drop".

### OFFICIAL (Shopify) @shopify/dev-mcp (npm)
https://www.npmjs.com/package/@shopify/dev-mcp | latest 1.16.0 | modified 2026-09-25 | no `repository` field; GitHub repo `Shopify/dev-mcp` NOT found in search (only Shopify/dev-mcp-gemini-cli, 31 stars).
README (exact): "runs locally over standard input/output without authentication: `npx -y @shopify/dev-mcp@latest`". "`LIQUID_VALIDATION_MODE` defaults to `full`, which exposes `validate_theme` for validating entire theme directories."
Claude Code command (from web search results, third-party guides, not seen on shopify.dev because blocked): `claude mcp add --transport stdio shopify-dev-mcp -- npx -y @shopify/dev-mcp@latest`. This matches the documented generic stdio syntax.

### OFFICIAL (Shopify) Shopify/theme-liquid-docs: ai/claude/CLAUDE.md
https://github.com/Shopify/theme-liquid-docs/blob/main/ai/claude/CLAUDE.md | repo stars 109 | updated_at 2026-10-02 | 1487 lines.
First line (exact): "🚨 MANDATORY: YOU MUST CALL "learn_shopify_api" ONCE WHEN WORKING WITH LIQUID THEMES."
"**Key principles: focus on generating snippets, blocks, and sections; users may create templates using the theme editor**"
"Snippets must have the `{% doc %}` tag as the header"
"Sections are made customizable by including the required `{% schema %}` tag ... Validate that JSON object using the `schemas/section.json` JSON schema"

### OFFICIAL (Shopify) Shopify/theme-tools
https://github.com/Shopify/theme-tools | stars 235 | updated_at 2026-10-01. Monorepo: liquid-html-parser, prettier-plugin-liquid, theme-check-common/node/browser, theme-language-server, VS Code extension. "These tools are also integrated in the Online Store Code Editor and the Shopify CLI."
packages/theme-check-node/configs/recommended.yml (exact head): `ignore: - node_modules/**`, checks like `AssetPreload`, `DeprecatedFilter`, `ExcessiveSettingsCount ... maxSettings: 40`, `HardcodedRoutes`.

### OFFICIAL (Shopify) Shopify/dawn, Shopify/horizon
- dawn: stars 3097, updated_at 2026-10-02. `.theme-check.yml` (exact, whole file):
```yaml
MatchingTranslations:
  enabled: false
TemplateLength:
  enabled: false
```
- horizon: stars 464, created 2025-07-18, updated_at 2026-10-02. No `.theme-check.yml`, `AGENTS.md`, `CLAUDE.md`, `.cursorrules` at root (404 each).

### .theme-check.yml community examples
- erikthalen/shopify-starter (exact):
```yaml
extends: theme-check:recommended
MissingTemplate:
  enabled: true
  ignore_missing:
    - snippets/vite.liquid
```
- EcomExperts-io/Base (exact excerpt): `extends:\n  - theme-check:recommended`, ignore list, `UndefinedObject: enabled: false` with comment explaining a false positive, `TemplateLength: severity: warning`. Comment: "Theme Check catches Liquid and schema correctness ... It does NOT check the merchant settings contract or hardcoded English in markup".
- GitHub code search: 129 `.theme-check.yml` files contain `extends theme-check:recommended`.

### COMMUNITY: EcomExperts-io/Base (best end-to-end Claude Code + Liquid example found)
https://github.com/EcomExperts-io/Base | stars 28 | default branch `development` | updated_at 2026-10-02 | "simplified take on Shopify's Dawn theme".
CLAUDE.md (205 lines, first 120 read). Exact: "Every new section exposes `padding_top`, `padding_bottom`, `padding_top_mobile`, `padding_bottom_mobile` and `color_scheme`, plus a `presets` entry." "Every string is a translation key". "Interactive JS is a custom element, registered once behind `if (!customElements.get(...))`". "Figma is design-only. Values come from Shopify; absent values render nothing."
.claude/settings.json (exact excerpt): PostToolUse matcher `"Edit|Write|MultiEdit"` runs `sh "${CLAUDE_PROJECT_DIR}/.claude/hooks/post-edit-gate.sh"`; Stop hook runs `stop-gate.py`; permissions allow `mcp__shopify-dev-mcp__validate_theme` and `Bash(shopify theme check*)`.
.claude/agents/shopify-pr-reviewer.md frontmatter (exact): `tools: Bash, Read, Grep, Glob, WebFetch`, `model: opus`, `memory: project`; "You **report**. You do not edit files." "**Figma is a source of design, never a source of data.**"

### COMMUNITY: other skills/agents (frontmatter read only)
- jonathanmoore/kona-theme `.claude/skills/shopify-liquid/SKILL.md` (stars 7, updated 2026-09-25); content closely mirrors Shopify's shopify-liquid-themes skill.
- mrvedmutha/bassface-theme-2026 `.claude/agents/shopify-section-developer.md` (stars 1, updated 2026-03-26): planner-then-developer pipeline, "Section name must be ≤ 25 characters total", Dawn conventions, breakpoints 1440/1024/767/375.
- dylanburkey/shopify-development-toolkit `.claude/agents/shopify-theme-developer.md` (stars 0): `model: sonnet`, long example-laden description.
- Code search `filename:SKILL.md shopify liquid` = 2880 hits (many registries/scrapers). `path:.claude/agents shopify liquid theme` = 60 hits. `filename:CLAUDE.md shopify theme liquid sections schema` = 156 hits.
- Awesome lists: hesreallyhim/awesome-claude-code, travisvn/awesome-claude-skills, VoltAgent/awesome-claude-code-subagents: zero "shopify" or "liquid" matches in README. ComposioHQ/awesome-claude-skills: one entry "Shopify Automation" (store admin, not themes).

### COMMUNITY: Liquid MCP servers
- florinel-chis/shopify-liquid-mcp: stars 3, updated 2026-05-04, "offline-first MCP server for Shopify Liquid documentation with 198 comprehensive docs".
- shopmanagerai/shopify-mcp: stars 1, created 2026-09-15, "122 read-only tools for Shopify themes, Liquid ...".
- tmill313/shopbuddy-plugin: stars 0, created 2026-09-02.
Recommendation: prefer the official Dev MCP / AI Toolkit; these are tiny and new.

### OFFICIAL (Microsoft) microsoft/playwright-mcp
https://github.com/microsoft/playwright-mcp | stars 37,775 | updated_at 2026-10-03. README (exact):
```bash
claude mcp add playwright npx @playwright/mcp@latest
```
"This server enables LLMs to interact with web pages through structured accessibility snapshots, bypassing the need for screenshots or visually-tuned models."
"If you are using a **coding agent**, you might benefit from using the [CLI+SKILLS](https://github.com/microsoft/playwright-cli) instead."
Flags: `--viewport-size <size>`, `--headless` ("headed by default"), `--caps` vision/pdf/devtools.

### OFFICIAL (Figma) figma/mcp-server-guide
https://github.com/figma/mcp-server-guide | stars 2,042 | updated_at 2026-10-03. README (exact):
`claude plugin install figma@claude-plugins-official` (recommended), manual `claude mcp add --transport http figma https://mcp.figma.com/mcp`.
Desktop server (web search result, Figma help center): `claude mcp add --transport http figma-desktop http://127.0.0.1:3845/mcp`.
"**get_design_context** provides a structured **React + Tailwind** representation of your Figma selection." Suggested rule: "Translate the output (usually React + Tailwind) into this project's conventions, styles and framework."

---------------------------------------------------------------------------
## PART 3: tools named in reels (verification only)

| Tool | What it is (source) | Official/community | Stars | Shopify Liquid relevance |
|---|---|---|---|---|
| Emil Kowalski skills | github.com/emilkowalski/skills, install `npx skills@latest add emilkowalski/skills`; main skill `emil-design-eng` "mostly animation, but also some design advice" | Community (individual author) | 42,900 | Partial: rules are CSS-level (e.g. "`transition: transform 200ms ease-out`", avoid `scale(0)`), usable in `{% stylesheet %}`. Some content React-specific. |
| Impeccable | github.com/pbakaus/impeccable, impeccable.style; "1 skill, 24 commands ... 61 deterministic detector rules"; `npx impeccable install`, `/impeccable init` writes PRODUCT.md | Community (Paul Bakaus) | 74,531 | Partial: design critique/audit is framework-neutral; live mode wiring is framework-specific. |
| Taste Skill | github.com/Leonxlnx/taste-skill, tasteskill.dev; FAQ "Rules target design intent, not a single framework API." | Community (sponsored README) | 92,136 | Partial: aesthetic direction applies; search snippet says it maps to shadcn/Tailwind/Motion stacks. |
| Figma MCP | figma/mcp-server-guide | Official (Figma) | 2,042 | Useful for design input only; output is React+Tailwind to be translated into Liquid/CSS. |
| Playwright MCP | microsoft/playwright-mcp | Official (Microsoft) | 37,775 | Directly useful: screenshot/verify `shopify theme dev` preview at multiple viewports. |
| Motion (motion.dev) | motiondivision/motion "A modern animation library for React and JavaScript"; vanilla `import { animate } from "motion"` | Community OSS (company Motion Division) | 33,811 | Possible via vanilla JS in an asset, but conflicts with Shopify liquid-theme-standards "No external dependencies". |
| Bklit UI | bklit/bklit-ui, ui.bklit.com; shadcn-registry React chart components | Community | 1,723 | Not relevant (React/shadcn charts). |
| "Coconut UI" = Kokonut UI | kokonut-labs/kokonutui, kokonutui.com; "Tailwind CSS, shadcn/ui and Motion" | Community | 2,132 | Not relevant (React/Next.js). |
| Manus | manus.im; hosted AI website/app builder with built-in analytics and SEO | Commercial product | n/a | Not relevant; separate hosting platform, not a Shopify theme tool. |
| adam_ha_yes UX laws md | Not found by web search. Nearest: keysjoao/laws-of-ux-skills (3 stars) "Three Claude Code skills bringing the 30 Laws of UX". | Unverified | n/a | Principles are framework-neutral and apply to sections. |
