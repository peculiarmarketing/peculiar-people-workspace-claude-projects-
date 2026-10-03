# Environment inventory (2026-10-03, cloud Claude Code session)

## Theme
- No theme folder with config/settings_schema.json in local files. Local
  temple-product-generator/theme/ holds only the custom pp-* sections, assets,
  one snippet and templates/index.json.
- Read-only Admin API query (Shopify MCP connector, graphql_query, `themes` with
  config/settings_schema.json) returned theme_info for all three store themes:
  theme_name "Shrine PRO", theme_version "1.9.0", theme_author "Shrine".
  - "Claude code original": role MAIN, updated 2026-10-03T06:11:21Z
  - "Claude Code V2": UNPUBLISHED, updated 2026-10-03T06:21:25Z
  - "Original ": UNPUBLISHED, updated 2026-10-02T21:09:45Z
- Conflict: temple-product-generator/theme/README.md says the live theme since
  2 Oct 2026 is "Claude Code V2" (id 194242150772). The API on 3 Oct reports
  "Claude code original" as MAIN. Owner should confirm which is live.

## Skills available
humanizer, structural-humanizer, idea-triage, store-cro-audit,
temple-product-generator, temple-ref-finder, session-start-hook, plus built-ins
(run, code-review, simplify, skill-creator, docs, pdf, etc.). None is
Shopify-theme specific.

## MCP servers connected
Shopify (Admin API connector: graphql_query read, graphql_mutation, search_docs_chunks,
product tools), GitHub, Figma, Google Drive, Higgsfield, Claude Docs, claude-code-remote.
Not present: Shopify Dev MCP (@shopify/dev-mcp), Playwright MCP.

## Command-line tools
Present: python3, node 22, npm, npx, playwright CLI (Chromium preinstalled at
/opt/pw-browsers), ffmpeg, git, gh.
Missing: shopify CLI, yt-dlp, whisper/faster-whisper, google-genai python package.

## Owner's YouTube watch stack: youtube-to-agent (repo /home/user/youtube-to-agent)
Per its SKILL.md and SETUP.md: /watch plugin (bradautomates/claude-video, gives
frames plus timestamped transcript), yt-dlp and ffmpeg, and a Gemini second
reader (scripts/gemini_review.py, needs GEMINI_API_KEY and google-genai).
Status in this session:
- /watch plugin: NOT INSTALLED (no plugin found under ~/.claude/plugins)
- yt-dlp: NOT INSTALLED
- ffmpeg: installed
- GEMINI_API_KEY: NOT SET; google-genai: NOT INSTALLED
- Network: shell egress to youtube.com, instagram.com, reddit.com and shopify.dev
  is denied by the environment's network policy (proxy CONNECT 403).
Nothing was installed (owner instruction). Video work therefore used WebFetch on
watch pages and transcript mirror sites. No frames or screenshots could be taken.
