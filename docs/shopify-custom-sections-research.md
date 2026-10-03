# Building custom Shopify theme sections with an AI assistant: briefing

Researched 2026-10-03 for Peculiar People (peculiarpeopleco.com). Read this before building, editing or reviewing any theme section, block or snippet.

**Who this is for.** An AI assistant (Claude Code or Claude.ai) working for a store owner who is not a developer. The owner approves; the assistant builds, checks and reports.

**Store facts this doc assumes**
- Theme: **Shrine PRO 1.9.0** by Shrine. Read from `config/settings_schema.json` `theme_info` through a read-only Admin API query, not from local files; no full theme folder exists locally. All three themes on the store report the same theme_info. See `research-raw/01-theme-observations.md`.
- Live theme: the API on 2026-10-03 reports **"Claude code original"** as MAIN. `temple-product-generator/theme/README.md` says "Claude Code V2" (id 194242150772) went live on 2 Oct. These conflict. Confirm by hand before any push.
- Apps that must keep working: **Easify Product Options** and **Kiwi Size Chart**. Both sit as **app blocks** in Shrine's product "Details" block, right after the variant picker (read from `templates/product.json`).
- Design tokens: Arial 16px body, Montserrat headings, black, white, navy #001A58, orange #F58000 buttons.
- About 136 products, Online Store 2.0.

**How to read the labels**
- **[OFFICIAL]**: shopify.dev or Anthropic docs, quoted from text the research actually returned.
- **[VENDOR]**: an app or theme maker's own docs.
- **[PRACTITIONER]**: a creator, agency or forum post.
- **[LOCAL]**: this workspace's own history or the store's own files.
- **UNVERIFIED**: could not be confirmed.
- **EXCERPT**: only a search engine's summary of the page was available, not the page itself. Treat EXCERPT text as paraphrase even when it sits in quotation marks.

**Access limits on this research.** The session's network policy blocked shopify.dev, help.shopify.com, youtube.com, instagram.com, reddit.com, shrine.io and most blogs.
- shopify.dev text came through Shopify's own docs search tool (`search_docs_chunks`), which returns verbatim page chunks.
- GitHub files were downloaded raw.
- Everything else is EXCERPT.
- No video was watched and no Reddit thread was read. Section 10 lists what to recheck.

---

## 1. Executive summary

1. **Build in a local copy of the theme, under git, and preview on a development or unpublished theme. Never touch the live theme.** Shopify's CLI requires `--allow-live` for a non-interactive push to the live theme, so never pass `--allow-live`, `--live` or `--publish` ([OFFICIAL] theme push). The owner publishes from the admin after review.
2. **Install Shopify's own Claude Code tooling before writing Liquid.**
   - Shopify AI Toolkit plugin, or the Dev MCP server: gives `validate_theme` and docs search.
   - Shopify's `liquid-skills` plugin: Liquid rules, standards and accessibility.

   These replace guessing from training data ([OFFICIAL] GitHub Shopify/Shopify-AI-Toolkit, Shopify/liquid-skills, npm @shopify/dev-mcp).
3. **Every section must have a valid `{% schema %}` with a `presets` entry,** or the owner cannot add it in the theme editor ([OFFICIAL] JSON templates page). Every word, image, colour and spacing value the owner may want to change becomes a setting or block.
4. **Run `shopify theme check` and the AI Toolkit / Dev MCP validator before saying "done".** Push with `--strict` so a Theme Check error blocks the upload ([OFFICIAL]). Validation lowers the error rate but does not remove it (EXCERPT, monkeyman.agency), so the visual checks in step 5 still matter.
5. **Look at the result.** Take Playwright screenshots of the preview at 375px and 1280px, test the section in the theme editor, and on a product page check that Easify options and the Kiwi size chart still appear and work.
6. **Put custom code only in new `pp-` prefixed files.** Never edit Shrine's own files: edits to shipped files are what theme updates drop ([PRACTITIONER] EXCERPT, ed.codes; Shopify help, EXCERPT). Shrine is sold outside the Theme Store, so updates arrive as a new ZIP (EXCERPT).
7. **Scope all CSS to the section** with a `pp-` BEM class or `#shopify-section-{{ section.id }}`. Use Shrine's CSS variables, such as `--font-heading-family` and `--color-base-accent-1`, instead of hardcoded fonts and hex values. No external JS libraries ([OFFICIAL] Shopify liquid-skills standards).
8. **One section per request, from a written spec** (template in section 6). Commit before each change, and show a diff of only the files named in the spec.
9. **Check what Shrine already ships before building anything.** The product Details block already accepts `product_sizing-chart`, `reviews`, `product_bundle-offer`, `product_complementary`, `collapsible-row` and `custom-liquid` ([LOCAL] theme read). Reviews, bundles and filters are better served by apps or built-in features than by hand-built sections (section 8, D).
10. **Owner-facing rule:** the assistant reports what it checked with evidence (command output, screenshots), lists anything it could not check, and never says "it works" without that evidence.

---

## 2. Recommended toolchain

"Non-dev?" means whether the owner can do the setup without developer help.

| Tool | What it does | Setup for a non-developer | Cost | Source |
|---|---|---|---|---|
| **Shopify CLI** (`@shopify/cli`) | Pull and push theme files; `theme dev` hot-reload preview on a development theme; `theme check` lint. Needs Node.js 22.12+ and Git 2.28+. | **Developer-level once**: terminal install `npm install -g @shopify/cli@latest` and a store login. After that the assistant runs it. | Free | [OFFICIAL] https://shopify.dev/docs/api/shopify-cli |
| **Theme Check** (built into the CLI) | Lints Liquid and schema: ValidSchema, UnknownFilter, UndefinedObject, MissingTemplate, ParserBlockingScript, ImgWidthAndHeight, and more. | Assistant runs it. No owner setup beyond the CLI. | Free | [OFFICIAL] https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks |
| **Shopify AI Toolkit** (Claude Code plugin) | One `shopify` skill that routes to docs search and validation. Its rule: "Validation is mandatory: never return generated code you have not run through this command". Announced 9 Apr 2026. | **Easy**: `claude plugin install shopify-ai-toolkit@claude-plugins-official`. **Telemetry is on by default** and can send the validated code and the most recent prompt (up to 2000 characters) to Shopify. Opt out: `mkdir -p ~/.config/shopify-ai-toolkit && touch ~/.config/shopify-ai-toolkit/opt-out`. | Free | [OFFICIAL] https://github.com/Shopify/Shopify-AI-Toolkit (README), changelog 2026-04-09 |
| **Shopify Dev MCP** (`@shopify/dev-mcp`, 1.16.0, 2026-09-25) | MCP tools `learn_shopify_api`, `search_docs_chunks`, `validate`, `validate_theme` ("ensure they don't have hallucinated Liquid content, invalid syntax, or incorrect references"). Runs locally, no auth, Node 18+. | **Easy, one command**: `claude mcp add --transport stdio shopify-dev-mcp -- npx -y @shopify/dev-mcp@latest`. Same telemetry opt-out. Use this or the AI Toolkit, not necessarily both. | Free | [OFFICIAL] npm README and package; command from https://shopify.dev/docs/apps/build/ai-toolkit (via docs search) |
| **Shopify liquid-skills** (Claude Code plugin, official) | Three skills: `shopify-liquid-themes`, `liquid-theme-standards`, `liquid-theme-a11y`; plus a Liquid language server plugin. | **Easy**: `/plugin marketplace add Shopify/liquid-skills`, then `/plugin install liquid-skills@liquid-skills`. The LSP plugin (`liquid-lsp@liquid-skills`) needs the CLI installed. | Free | [OFFICIAL] https://github.com/Shopify/liquid-skills (created 2026-03-13) |
| **Playwright MCP** | Lets the assistant open the preview URL, resize to phone and desktop, and screenshot. The README notes coding agents "might benefit from using the CLI+SKILLS (microsoft/playwright-cli) instead". | **Easy**: `claude mcp add playwright npx @playwright/mcp@latest`. In this cloud environment Chromium is already installed. | Free | [OFFICIAL] https://github.com/microsoft/playwright-mcp |
| **Git + GitHub** | Version history and rollback for theme code. Shopify's GitHub integration syncs a branch to a theme both ways. | **Medium**: a repo needs creating once. The GitHub integration needs a "buildless" folder layout, and theme editor saves commit back to the branch automatically ("This can't be disabled"). | Free | [OFFICIAL] https://shopify.dev/docs/storefronts/themes/tools/github |
| **Figma MCP** | Reads a Figma frame as a design reference. Output is "a structured React + Tailwind representation" that must be translated to Liquid and CSS. | **Easy** (`claude plugin install figma@claude-plugins-official`). Only useful if designs are made in Figma. Optional. | Free tier | [OFFICIAL] https://github.com/figma/mcp-server-guide |
| **Shopify Sidekick "Generate" theme blocks** | In the theme editor: Add block > Generate, describe the block. Needs a section that accepts `@theme` blocks; generated blocks are saved to `/blocks`. | **Non-developer friendly**, no setup. Whether it is offered on Shrine (not a Theme Store theme) is UNVERIFIED. Forum reports of misalignment and failures (EXCERPT). | Included in Shopify | [OFFICIAL] https://shopify.dev/docs/storefronts/themes/architecture/blocks/ai-generated-theme-blocks |
| **Section Store** and similar section apps | Pre-built sections installed into the theme. | **Non-developer friendly.** Lock-in risk: one vendor's uninstall doc says sections it added, and edits to them, are removed (EXCERPT, docs.appsections.com). | Mostly $0 to $9 per section; optional $15/mo (EXCERPT) | apps.shopify.com/section-factory (EXCERPT) |

**Design skills named in the reels.** None are Shopify-specific.
- **Emil Kowalski skills** (`npx skills@latest add emilkowalski/skills`) and **Impeccable** (`npx impeccable install`): framework-neutral design and animation rules, partly usable for section CSS. Community projects.
- **Taste Skill**: leans on the React stack. Community project.
- **Motion.dev, Bklit UI, Kokonut UI ("Coconut UI" in the reel), Manus**: React libraries or hosted builders. Not relevant to Liquid sections, and they conflict with Shopify's "No external dependencies" rule.

Source: research-raw/github-anthropic/notes.md (GitHub READMEs, downloaded).

---

## 3. Failure modes

Each row gives the symptom, the cause, and a prevention rule. Rule IDs (R1 to R27) map to the CLAUDE.md block in section 4.

| # | Failure | Symptom | Why it happens | Prevention rule or check | Sources |
|---|---|---|---|---|---|
| F1 | Hallucinated Liquid | Error on save, blank output, or a filter that silently does nothing. Example reported: Claude inventing `product.featured_variant`. | The model mixes in syntax from other template languages, from older Liquid, or invents plausible names. Liquid also has quirks: no ternaries, no parentheses in conditions, `for` loops capped at 50 iterations. | Validate every Liquid file with `validate_theme` / AI Toolkit and `shopify theme check` (UnknownFilter, UndefinedObject, LiquidHTMLSyntaxError). Look up any object or filter the assistant is not sure of in the Liquid reference. **R5, R6, R7** | [OFFICIAL] theme-check checks; Shopify liquid-skills SKILL.md; [PRACTITIONER] EXCERPT letstalkshop.com, adsx.com (2026) |
| F2 | Broken or missing `{% schema %}` | Section does not appear under "Add section", or "Invalid JSON in tag 'schema'", or settings are not editable. | Trailing commas, comments, curly quotes, duplicate setting ids, block without `name`, a range without `default`, richtext default not wrapped in `<p>`, more than one schema tag, schema nested inside another tag, **no `presets`**. One forum report: ChatGPT emitted reversed (unparsable) schema code. | One `{% schema %}` per file, top level, valid JSON. Always include `presets` with a `name`. Range needs numeric `min`, `max`, `default`. Run Theme Check (ValidSchema, ValidSettingsKey, ValidBlockTarget). Open the theme editor and add the section before reporting done. **R8, R9, R10** | [OFFICIAL] section-schema page ("Each section can have only a single {% schema %} tag..."); JSON templates page ("Section files must define presets..."); input-settings page; [PRACTITIONER] EXCERPT community.shopify.com threads 205043, 169273, 329958 (likely older than 12 months), medium.com/@Cavlemasters |
| F3 | Hardcoded content | The owner cannot change text, image or colour without code. The next AI edit then has to touch code for a copy change. | Faster for the model to inline values. | Every visible string, image, link, colour and spacing value is a setting or block, with the current value as `default`. Theme strings use the `t` filter where the theme has locale keys. Shopify's standards skill says "never hardcode colors, spacing, or fonts". **R11, R12** | [OFFICIAL] Shopify liquid-skills `liquid-theme-standards`; [PRACTITIONER] EcomExperts-io/Base CLAUDE.md (every section exposes padding and `color_scheme` plus `presets`) |
| F4 | Editing the live theme, no rollback | The store breaks for customers. An AI "undo" does not restore the exact old code. Theme editor saves have no history. | Working in the admin code editor or pushing to MAIN. Code editor history is per file, and "can't recover deleted theme files". | Work only in a local git copy and on a development or unpublished theme. Commit before every change. Never pass `--allow-live`, `--live`, `--publish`. Use `--nodelete` and `--only` on pushes to an existing theme. **R1, R2, R3, R4** | [OFFICIAL] theme push flags ("-a, --allow-live ... Required in non-interactive environments when targeting the live theme"); help center version history (EXCERPT); [PRACTITIONER] EXCERPT seotldr.substack.com ("it won't necessarily restore it exactly as it was"), community.shopify.com 417178; [LOCAL] theme/README.md: "without it a push removes every theme file that is not in this folder" |
| F5 | Overwriting the owner's editor settings | Settings the owner set in the theme editor vanish after a push. | `config/settings_data.json` and `templates/*.json` are written by the theme editor. A push of an old local copy replaces them. Whichever save lands last wins. | Pull before editing. Never push `config/settings_data.json`. Push a `templates/*.json` file only when the spec says so, after pulling it fresh. Never push while the owner has the theme editor open on that theme. **R4, R13** | [PRACTITIONER] EXCERPT appycodes.com; [OFFICIAL] GitHub integration ("The version of the file in the code editor overwrites the GitHub version"); [LOCAL] temple-product-generator/docs/decisions.md 18 Sep 2026 ("the editor writes the whole file on save and whichever saves last wins") |
| F6 | CSS leaking | A new section restyles arrows, buttons or headings elsewhere on the page. | Bare selectors such as `.button` or `h2`. Also: CSS in `{% stylesheet %}` is bundled once per file, not per instance. | Prefix every selector with the section's `pp-` BEM root class. Put per-instance values in an inline `<style>` scoped to `#shopify-section-{{ section.id }}`. Never restyle Shrine's own classes. **R14, R15** | [OFFICIAL] stylesheet tags page ("If you need instance-specific CSS, then use an inline <style> tag"); section.id is dynamic ("Read the ID from {{ section.id }}... instead of hardcoding it"); [PRACTITIONER] EXCERPT community.shopify.com 166189 |
| F7 | Ignoring theme tokens | Section uses a different font, blue or button style from the rest of the store. Looks bolted on. | Model picks its own defaults. | Use Shrine's CSS variables: `--font-heading-family`, `--font-body-family`, `--color-base-text`, `--color-base-accent-1`, `--buttons-radius`, `--page-width`, `--spacing-sections-desktop` / `-mobile`. Where a store colour must be fixed, use only #000000, #FFFFFF, #001A58 and #F58000, via a `color` setting with that default. **R16** | [LOCAL] layout/theme.liquid variable list; [OFFICIAL] liquid-skills standards |
| F8 | JavaScript conflicts with the theme and apps | Variant picker, Easify options or the Kiwi size chart stop working, duplicate or jump. Console errors. | Custom JS that listens to or rewrites the product form, variant picker or `product-info`. Global variables. Libraries loaded twice. Kiwi's own docs: when variant apps rebuild the variant area, an injected chart "may disappear, duplicate, jump position, or trigger script conflicts" (EXCERPT). | No custom JS on the product form, variant picker, buy buttons or inside `main-product_details`. Custom JS goes in a custom element or IIFE in a `pp-` asset, loaded with `defer`. No external libraries. After any product page change, test option selection, the Easify fields, the Kiwi chart and add to cart. **R17, R18, R19** | [VENDOR] EXCERPT intercom.help/kiwi-sizing-chart article 13256403; easifyapps.com/docs/options-dont-show; [OFFICIAL] liquid-skills standards ("No external dependencies"); [LOCAL] product.json block order |
| F9 | App blocks lost | Easify or Kiwi missing on some products after a template change or theme update. | A template or section without the app block, or without an `@app` block type. Kiwi: "an update may remove or overwrite app blocks" (EXCERPT). Easify: must be reactivated on a new theme (EXCERPT). | Never remove or reorder the two app blocks in `templates/product.json`. Any new product template must include both. Any custom product-area section that should host apps must accept `{"type": "@app"}`. **R18, R20** | [OFFICIAL] app-blocks ("For app blocks to function, a theme must contain... Sections that support and render blocks of type @app"); [VENDOR] EXCERPT Kiwi 10291102, Easify app-activation |
| F10 | Mobile layout and tap targets | Fine on desktop, cramped or overflowing on a phone. Editor preview differs from a real device. Sidekick sections "misaligned live" because the theme's grid overrides the preview (EXCERPT). | Desktop-first CSS, fixed widths, small tap targets. The editor iframe is not a phone. | Build mobile-first. Screenshot at 375px and 1280px from the preview URL, not only in the editor. Tap targets at least 24 by 24 CSS pixels (Theme Store minimum); aim for 44px on primary buttons (UNVERIFIED as a Shopify rule). The owner checks once on a real iPhone. **R21, R22** | [OFFICIAL] Theme Store requirements (24x24 touch targets); [PRACTITIONER] EXCERPT community.shopify.com 580094 |
| F11 | Performance | Layout shift, slow largest image, blocking scripts. | `<img>` without width and height; lazy-loading the first visible image; `<script>` without `defer`; huge images; remote assets. | Use `image_url \| image_tag` with `widths` and `sizes`. Do not set `loading` on images in the first three sections; `image_tag` handles it. Scripts get `defer`. No remote CDNs. Theme Check covers ImgWidthAndHeight, ParserBlockingScript, RemoteAsset. **R23** | [OFFICIAL] image_tag lazy-loading page ("Don't set the loading attribute when relying on this default"); theme-check checks; Theme Store Lighthouse minimum 60 performance |
| F12 | Accessibility regressions | Images without alt text, buttons without names, animation ignoring reduced motion, low contrast. | Model omits alt and ARIA, uses divs as buttons. | Every image has an `alt` setting or meaningful fallback. Interactive parts are real `<button>` / `<a>`, keyboard reachable. Respect `prefers-reduced-motion`. Contrast at least 4.5:1. Measured (WCAG 2 formula, computed in this session): #F58000 vs #FFFFFF is **2.63:1**, so orange text on white AND white text on orange buttons both fail. Black on orange is 7.97:1; navy on white is 16.3:1. **R24** | [OFFICIAL] Theme Store requirements (contrast 4.5:1, alt on every image); liquid-skills `liquid-theme-a11y`; [LOCAL] contrast computed with the WCAG relative luminance formula |
| F13 | Breaking on theme updates; name collisions | Custom work lost after a Shrine update, or a custom file overwrites or is overwritten by a theme file with the same name. | Edits inside Shrine's shipped files. Generic file names such as `sections/testimonials.liquid`. | Only add new files with the `pp-` prefix. Never edit Shrine files; if a Shrine file must change, record it in `theme/CUSTOMIZATIONS.md` with the reason so it can be re-applied. Keep the repo copy of every `pp-` file. **R25** | [PRACTITIONER] EXCERPT ed.codes, community.shopify.com 686447 (2026); Shopify help updating-themes (EXCERPT); [VENDOR] EXCERPT Shrine updates by ZIP |
| F14 | Silent failure | Assistant says "done". Nothing changed, or part of the data is missing with no error. Causes reported: editing one theme while previewing another, or editing the wrong file. | Pushing to a different theme than the preview; a section with no preset that never appears; Liquid that renders nothing for missing data. [LOCAL] example: the temple marquee drops a temple with no art "without any error". | Report must name the theme id pushed to, the files pushed, and the preview URL. Show screenshot evidence of the change. Sections that depend on data must render a visible placeholder in the editor (`request.design_mode`) when data is missing, and the assistant must state which items were skipped. **R26** | [PRACTITIONER] EXCERPT community.shopify.com 1362 (older than 12 months); [LOCAL] theme/README.md marquee note |
| F15 | Overwriting working code; scope creep | A request for one change rewrites other sections. A working fix gets reverted in a later edit. | Large prompts ("redo the homepage"); the model regenerates whole files; no diff review. | One section per request. Edit only files named in the spec. Show `git diff --stat` and the diff before pushing; if a file outside the spec changed, stop and ask. **R27** | [PRACTITIONER] EXCERPT letstalkshop.com ("one section or file" per prompt); dominikatracy.com (2026, "will need a lot of steering") |

**Conflicts between sources**

1. **Does validation make AI output safe?**
   - Vendor blogs present the Dev MCP and Theme Check as the fix for hallucinations.
   - monkeyman.agency (EXCERPT) says guardrails including theme-check in CI and human review "still catch about one in eight changes", meaning about one in eight changes still has a problem that gets caught at review.
   - A dev.to title says "The Liquid you lint isn't the Liquid Shopify runs" (EXCERPT).
   - Treat validation as necessary but not sufficient.
2. **Can Sidekick write Liquid?**
   - fudge.ai (EXCERPT) says Sidekick "cannot generate, edit, or debug Liquid code".
   - Shopify docs describe AI-generated theme blocks in the editor.
   - Likely Sidekick chat and the editor's Generate feature differ. Unresolved.
3. **Do custom files survive theme updates?**
   - Sources agree that edits to shipped files are lost and new files carry over (all EXCERPT).
   - No Shrine document confirms this for Shrine's ZIP updates.
4. **Theme Check severity for ValidSchema.** The checks table lists it as a warning; its own page says `severity: error`. Treat it as an error.
5. **Dev MCP install command.**
   - One creator blog cites `npx @shopify/mcp-cli@latest init` (EXCERPT, websensepro.com).
   - Shopify's docs and npm give `@shopify/dev-mcp@latest`.
   - Use the official one.

---

## 4. CLAUDE.md rules block for a Shopify theme repo

Paste this into the theme repo's `CLAUDE.md`. Anthropic's docs note that CLAUDE.md is "context, not enforced configuration"; the hooks in section 5 enforce the critical rules. Each rule cites the failure it prevents.

```markdown
# Shopify theme rules (Peculiar People, Shrine PRO 1.9.0)

## Safety
- R1. Never push to the live theme. Never pass --allow-live, --live or --publish to any shopify command. (F4)
- R2. Before any push, run `shopify theme list` and confirm the target theme id is not the one with role [live]. Write the id in your report. (F4, F14)
- R3. Commit to git before every change and after every working step. Never rewrite history. (F4, F15)
- R4. Run `shopify theme pull --theme <id> --only config/settings_data.json --only "templates/*.json"` before editing, and push existing themes only with --nodelete and explicit --only flags. (F4, F5)
- R13. Never push config/settings_data.json. Push a templates/*.json file only when the spec names it, and only right after pulling it fresh. Ask the owner to close the theme editor first. (F5)

## Correct Liquid
- R5. Call the Shopify validator (AI Toolkit `shopify` skill or Dev MCP `validate_theme`) on every Liquid file you create or change. Never return code that has not passed it. (F1)
- R6. Run `shopify theme check` and fix every error before pushing. Push with --strict. (F1, F2)
- R7. If you are not certain a Liquid object, filter, tag or setting type exists, look it up with the docs search tool. Never guess. Use render, never include. (F1)

## Editable sections
- R8. Every section has exactly one top-level {% schema %} with valid JSON, a "name" of 25 characters or fewer, and a "presets" entry with a "name". (F2)
- R9. Range settings have numeric min, max and default. Richtext defaults are wrapped in <p>. Block types each have a "name". Setting ids are unique. (F2)
- R10. After pushing to a preview theme, add the section in the theme editor (or open the template that has it) and confirm every setting changes the output. (F2, F14)
- R11. Every visible string, image, link, colour and spacing value is a setting or a block. The current value goes in "default". Nothing the owner might change is hardcoded. (F3)
- R12. Repeating items (cards, rows, logos, FAQs) are blocks, with max_blocks set. (F3)

## Styling
- R14. Name every new file and CSS class with the pp- prefix (pp-<section-name>, BEM: pp-faq__item). Every selector starts with the section's root class. Never style Shrine's own classes or bare elements. (F6, F13)
- R15. Per-instance values go in an inline <style> scoped to #shopify-section-{{ section.id }}. Shared section CSS goes in assets/pp-<name>.css or a {% stylesheet %} tag with no Liquid inside. (F6)
- R16. Use the theme's CSS variables for fonts, colours, buttons and spacing (--font-heading-family, --font-body-family, --color-base-text, --color-base-accent-1, --buttons-radius, --page-width, --spacing-sections-desktop, --spacing-sections-mobile). Fixed brand colours are only #000000, #FFFFFF, #001A58 and #F58000, and only as defaults of color settings. (F7)

## Apps and JavaScript
- R17. Never add or change JavaScript that touches the product form, variant picker, buy buttons, product-info, or anything inside the main-product_details block. (F8)
- R18. Never remove, move or rename the Easify Product Options and Kiwi Size Chart app blocks in templates/product.json. Any new product template includes both. (F8, F9)
- R19. JavaScript goes in a custom element or an IIFE in assets/pp-<name>.js, loaded with defer. No global variables. No external libraries or CDNs. (F8, F11)
- R20. A custom section meant for the product area accepts {"type": "@app"} blocks. (F9)

## Quality
- R21. Write CSS mobile-first. No fixed pixel widths on containers. Tap targets at least 24 by 24 CSS pixels; primary buttons at least 44px tall. (F10)
- R22. Screenshot the preview URL at 375px and 1280px wide and look at both before reporting. (F10, F14)
- R23. Images use image_url | image_tag with widths and sizes. Do not set loading on images in the first three sections. Every script has defer. (F11)
- R24. Every image has alt text from a setting or a meaningful fallback. Interactive elements are <button> or <a>. Animations stop under prefers-reduced-motion. Text contrast at least 4.5:1. Never put orange #F58000 text on white or white text on orange (2.63:1). Labels on orange buttons are black (7.97:1) unless Evan decides otherwise. (F12)

## Scope and updates
- R25. Never edit a Shrine file. If one must change, stop and ask, then record the change and reason in theme/CUSTOMIZATIONS.md. (F13)
- R26. Never say done without evidence: name the theme id pushed to, the files pushed, the preview URL, the check output and the screenshots. If any data was skipped or a check could not run, say so first. (F14)
- R27. One section per request. Change only files the spec names. Show git diff --stat before pushing; if any other file changed, stop and ask. (F15)
- No em dashes in anything the owner reads.
```

---

## 5. Proposed Claude Code skills, subagent and hooks

The file formats come from Anthropic's docs ([OFFICIAL] https://code.claude.com/docs/en/skills, /sub-agents, /hooks):
- **Skills:** `.claude/skills/<name>/SKILL.md` with `name` and `description` frontmatter.
- **Subagents:** `.claude/agents/<name>.md`, where `name` and `description` are required.
- **Hooks:** live in `.claude/settings.json`. Exit code 2 blocks a PreToolUse call. A PostToolUse hook "Shows stderr to Claude; the tool already ran".

### 5.1 Skill: `shopify-section-builder`

**MY PROPOSAL.** It builds on Shopify's official skills; the a11y and standards rules are ADAPTED FROM https://github.com/Shopify/liquid-skills.

```markdown
---
name: shopify-section-builder
description: Build or change one custom Shopify theme section for the Peculiar People store (Shrine PRO). Use when Evan asks for a new section, block, homepage band, product page module, or a change to a pp- section. Works from the section spec template, validates, previews on an unpublished theme, and reports with screenshots. Never publishes.
---
1. Read the theme repo CLAUDE.md and docs/shopify-custom-sections-research.md sections 3 and 4.
2. Get a filled spec (section 6 template). If a required field is empty, list the gaps and stop.
3. Check if Shrine already has a section or block that does this (search sections/ and blocks/ by name). If yes, say so and stop for a decision.
4. Run `shopify theme list`. Note the live theme id and the preview theme id. Commit the current state.
5. Pull fresh templates/*.json and config/settings_data.json from the preview theme.
6. Write sections/pp-<name>.liquid (and assets/pp-<name>.css / .js if needed). Follow R8 to R24.
7. Validate: Shopify validator on each file, then `shopify theme check`. Fix and repeat until clean.
8. Show `git diff --stat`. Confirm only spec files changed.
9. Push to the preview theme: `shopify theme push --theme <preview id> --nodelete --strict --only <each file>`.
10. Run the QA checklist (section 7) with Playwright screenshots at 375 and 1280.
11. Report using the QA report format. Leave publishing to Evan.
```

### 5.2 Subagent: `theme-reviewer`

**ADAPTED FROM** EcomExperts-io/Base `.claude/agents` reviewer (https://github.com/EcomExperts-io/Base). It is read-only: "You **report**. You do not edit files."

```markdown
---
name: theme-reviewer
description: Independent read-only review of a Shopify theme change before it is pushed. Use after the section builder finishes and before reporting to Evan.
tools: Read, Grep, Glob, Bash
---
You report. You do not edit files.
Check the diff against CLAUDE.md rules R5 to R27. For each rule: PASS, FAIL (file:line, what), or NOT CHECKED (why).
Specifically look for: bare CSS selectors, hardcoded colours or text, missing presets, scripts without defer,
any change to the product form, variant picker, main-product_details, or the Easify/Kiwi app blocks,
any Shrine (non pp-) file in the diff, and any push command with --allow-live, --live or --publish.
```

### 5.3 Hooks (`.claude/settings.json`)

**MY PROPOSAL.** The pattern is ADAPTED FROM EcomExperts-io/Base `.claude/settings.json` (PostToolUse on `Edit|Write|MultiEdit`, plus a Stop gate running Theme Check). Here is the event JSON format from Anthropic's hooks docs:

```json
{
  "hooks": {
    "PreToolUse": [
      { "matcher": "Bash",
        "hooks": [{ "type": "command", "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/block-live-push.sh" }] }
    ],
    "PostToolUse": [
      { "matcher": "Edit|Write|MultiEdit",
        "hooks": [{ "type": "command", "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/theme-check-changed.sh" }] }
    ]
  }
}
```

- **`block-live-push.sh`** (MY PROPOSAL). It reads the tool input JSON from stdin. If the command contains `shopify theme` and any of `--allow-live`, `--live`, `--publish`, `theme publish` or `theme delete`, it prints a reason to stderr and exits 2, which blocks the call.
- **`theme-check-changed.sh`** (MY PROPOSAL). It runs `shopify theme check` and prints errors to stderr so the assistant sees them. A PostToolUse hook cannot undo the edit.

**Not built or tested.** These scripts are proposals. Test them on a scratch repo before relying on them.

### 5.4 Existing skills to install rather than write

- **Shopify AI Toolkit `shopify` skill** and **Shopify liquid-skills** ([OFFICIAL], links in section 2).
- **Existing workspace skill `store-cro-audit`.** Use it after a section goes live to check it on the real storefront. [LOCAL]

---

## 6. Section spec template

Fill one of these per section. The builder stops if any field marked * is empty.

```markdown
# Section spec: <name>

* Purpose (one sentence, what the shopper should do or feel):
* Page(s) and position (e.g. product page, after Description; homepage, after hero):
* Does Shrine already have something close? (section/block name, or "checked, no"):
* Content the owner edits (each becomes a setting):
  - text: <label> | default: <current wording>
  - image: <label> | alt default: <text>
  - link: <label> | default: <url>
* Repeating items (each becomes a block; say max count):
* Desktop layout (describe or attach screenshot/mockup):
* Mobile layout at 375px (stacking order, what hides):
* Colours: theme variables only, or which of black / white / navy #001A58 / orange #F58000:
* Fonts: theme heading (Montserrat) and body (Arial 16px) unless stated:
- Motion: none / subtle (must stop under reduced motion):
- Data source (static settings, product metafield, metaobject, collection):
- Behaviour when data is missing:
- Must not affect: product form, variant picker, Easify options, Kiwi size chart, <other>:
* Done when (observable checks, e.g. "owner can change heading in editor", "shows 3 cards on mobile in one column"):
* Target theme for preview (name and id; never the live one):
- Reference sites or screenshots:
- Out of scope:
```

**Why this shape.** Practitioners report that the first output is usable when a request is scoped to one section, names the content and editable settings, and states mobile behaviour (EXCERPT, letstalkshop.com, dominikatracy.com). The "Shrine already has it?" field comes from this store: [LOCAL] Shrine ships 50+ blocks, including size chart, reviews, bundle and complementary blocks.

---

## 7. Pre-publish QA checklist

The assistant runs every item and reports each one as PASS, FAIL or NOT CHECKED, with evidence. Publishing stays with the owner.

**Code**
1. Shopify validator (AI Toolkit or Dev MCP `validate_theme`) on each changed file. Paste a summary of the output.
2. `shopify theme check`: zero errors. Paste the summary line.
3. `git diff --stat`: only spec files changed, and no Shrine file or `config/settings_data.json` is in the list.
4. Schema review:
   - one schema tag
   - `presets` present
   - every owner-editable value is a setting
   - range `default` present
   - name is 25 characters or fewer

**Push**
5. `shopify theme list`. Report:
   - the target theme id and its role, which must not be live
   - the exact push command used, which must include `--nodelete`, `--only` and `--strict`
   - the preview URL

**Theme editor**
6. The section can be added from "Add section" (or is present on its template). Change each setting and confirm the output changes.
7. Remove and re-add the section, if it has a preset. No errors.

**Visual** (Playwright, from the preview URL, not the editor)
8. Screenshot at 375px and at 1280px. Attach both. Describe anything overlapping, cut off or misaligned.
9. Fonts and colours match the theme. There are no hex values other than the four brand colours.
10. Tap targets on mobile are at least 24px (primary buttons 44px). There is no horizontal scroll at 375px.

**Apps and product page** (when the change touches the product template or product pages)
11. Select a different size and colour: the image and price update.
12. Easify option fields appear and accept input, and the add to cart line item carries them (check the cart).
13. The Kiwi size chart link or button opens the chart.
14. Browser console: no new errors. List any errors found.

**Accessibility and performance**
15. Every image has alt text. Tab through the section with the keyboard: every control is reachable and visible on focus.
16. Reduced motion: with `prefers-reduced-motion: reduce` emulated, animations stop.
17. Lighthouse (mobile) on the preview page, if available: report performance and accessibility scores. Theme Store minimums are 60 and 90 ([OFFICIAL] requirements). NOT CHECKED is acceptable if the tool is missing, but say so.

**Report format**
- First line: "Ready for your review on <theme name> (not live)" or "Not ready: <reason>".
- Then the PASS / FAIL / NOT CHECKED list.
- Then screenshots.
- Then the line "What I could not check".

---

## 8. Reel and video findings, plus section patterns

### 8.1 Instagram reels

None of the three could be fetched (EGRESS_BLOCKED, see research-raw/instagram/fetch-attempts.md). The owner pasted transcripts, saved in research-raw/instagram/reel-transcripts-from-owner.md, and those are what this section works from. No frames were captured. The reel 3 screenshot is the owner's own.

**Reel 1, DdJ5ynbDxqS.** Coverage: owner-pasted transcript only; not accessible directly.
- **What it claims:** add "Emile Kowalski design and impeccable skills", then the "taste skill", then "connect Figma MCP and Playwright" so Claude can "design, build, and test and screenshot". The transcript states nothing about the build or about failures.
- **Tools, verified on GitHub:**
  - emilkowalski/skills (community)
  - pbakaus/impeccable (community)
  - Leonxlnx/taste-skill (community)
  - Figma MCP and Playwright MCP (official)
- **Copy:** Playwright screenshots as a self-check (already in R22). Impeccable or Emil's rules are optional design critique.
- **Ignore:** "Claude just killed web designers" and "let it handle the rest". This briefing's evidence points the other way: review is still needed.
- **Date:** unknown.

**Reel 2, DdiYr7wOmsE.** Coverage: owner-pasted transcript only; not accessible directly.
- **What it claims:** Motion.dev, "BKLit.ui", "Coconut UI" (actually Kokonut UI) and Manus.io "build flawless backend-powered sites".
- **Verdict:** all are React libraries or a hosted site builder, not relevant to Liquid sections. They conflict with Shopify's no-external-dependency rule. "Flawless" is an unverified claim.
- **Copy:** nothing.
- **Date:** unknown.

**Reel 3, DcwkX6OyduT** (adam_ha_yes, "20 UX Laws to tell Claude for better Design"). Coverage: owner-pasted transcript plus the owner's screenshot; not accessible directly.
- **Content:** a list of UX laws (Hick, Fitts, Jakob, proximity, Miller, Doherty threshold, Von Restorff, and more), with plain rules such as "Reduce choices per screen", "Make targets large" and "Highlight the primary action". The screen lists Postel's law twice. The promised md file was not found.
- **Copy:** these are framework-neutral and fit the spec template's "purpose" and the QA visual checks. Example: one primary action per section, in orange; large tap targets.
- **Ignore:** treating 20 laws as a checklist for every section.
- **Date:** unknown.

### 8.2 YouTube

**Every video below: NOT ACCESSIBLE.** youtube.com and all transcript mirrors were blocked. The owner's watch stack (youtube-to-agent: the /watch plugin, yt-dlp and Gemini) is not installed in this environment, and nothing was installed. For each video only the title and URL from a search index were seen, plus a one-line search snippet. So for every video:
- no transcript, frames, prompts or commands were captured
- channel and length are unknown unless stated
- "what went wrong" is unknown

Raw records are in research-raw/youtube/<id>.md. Watch order for a later pass with the stack: 1, 2, 3, 5, 4, 9.

| # | URL | Title (from search index) | Date | Snippet says it covers | Worth a real watch? |
|---|---|---|---|---|---|
| 1 | https://www.youtube.com/watch?v=uW39GOgc0wo | Claude Code for Shopify: 10 Mistakes That Will Break Your Store | about Apr 2026 (UNVERIFIED) | 10 mistakes from using Claude Code on live stores | Yes, highest priority |
| 2 | https://www.youtube.com/watch?v=rNiw_9OO9ts | How to Build Shopify Themes Faster with Claude Code | unknown | AI theme workflow; channel possibly Will Misback (UNVERIFIED) | Yes |
| 3 | https://www.youtube.com/watch?v=0tEkfZ4vtcs | Build Shopify Themes in MINUTES -[Claude Code & MCP] | unknown | Claude Code in VS Code, MCP, GitHub; channel likely WebSensePro (UNVERIFIED). Companion blog cites a different MCP install command (see conflicts). | Yes |
| 4 | https://www.youtube.com/watch?v=iVDU0oDNuVE | How I Use Claude to Build Shopify Sections (My Exact Process) | unknown | A prompting process for sections | Yes |
| 5 | https://www.youtube.com/watch?v=ptnWksC9TXY | New Shopify AI Toolkit: Claude Code Setup + Demo (April 2026) | Apr 2026 (title) | AI Toolkit setup, theme edits by prompt | Yes |
| 6 | https://www.youtube.com/watch?v=hh7i8Bs8-JI | How to Edit Shopify Theme Using Claude Code [Full Tutorial] | unknown | Beginner, VS Code | Maybe |
| 7 | https://www.youtube.com/watch?v=x2pRavsHdls | Claude Code Just Killed Every Shopify Agency Ever | about May 2026 (UNVERIFIED) | Full store end to end. Clickbait. | Low |
| 8 | https://www.youtube.com/watch?v=pNCx-1F5oIs | How to use AI to create custom Shopify theme blocks | unknown, likely older than 12 months | Sidekick Generate blocks | Maybe (no-code option) |
| 9 | https://www.youtube.com/watch?v=NjOqPbUecC4 | Claude Code Now Has Eyes | unknown | Playwright MCP to stop "coding blind" (not Shopify) | Yes, for the QA loop |
| 10 | https://www.youtube.com/watch?v=Mk6cv0f_nnc | Build Shopify Themes FAST with Cursor AI | about Dec 2024, OLDER THAN 12 MONTHS | CLI pull, edit in Cursor, push | No |

Also found but not recorded individually: odzauqmNFUA (Claude vs Cursor), -msIYvPVM9E (Codex CLI), pom070QQgpQ and 9Rq868HPqJk (AI Toolkit), HsMGvW2TE64, hXU4HceI6Jc, bBMp5tLxShQ, _YRmbRFAjYY, tc5NaxUrOyU, q2gxq6oOjcE (Sidekick custom section), V2qjnBDZZ7A (Playwright CLI vs MCP), UDNKhiQtw9M.

**What to copy, ignore and verify across the videos**
- **Copy:** nothing can be copied from the videos themselves until they are watched. The recurring advice in search snippets matches what the official sources say: unpublished theme, CLAUDE.md, Dev MCP, commit first, one section per prompt, give the agent a browser. That advice is already in this doc on official grounds.
- **Ignore:** speed claims ("28 minutes", "8x"). They come from blog summaries, not videos.
- **Verify by watching:** the 10 mistakes in video 1.

### 8.3 Section patterns that similar stores add (question D)

Only what the sources show. All Baymard and vendor figures are EXCERPT (pages blocked), so verify them before quoting externally. The "Already in Shrine?" column comes from the [LOCAL] read of the Details block schema.

| Pattern | What sources show | Already in Shrine? | Best route |
|---|---|---|---|
| Collapsible detail blocks | Baymard: vertical collapsed sections beat horizontal tabs. In one test, 27% of users never found content in unopened horizontal tabs (EXCERPT, baymard.com/blog/avoid-horizontal-tabs, likely older than 12 months). A 2026 practitioner reading of Baymard: key fit, fabric and size facts should be visible, not hidden in collapsed tabs (EXCERPT, styleimprint.app). | Yes: `collapsible-row` block (4 in use) and the `collapsible-content` section | Built-in. Keep fit and fabric facts visible above the accordions. |
| Collection filters | Baymard: 61% of sites don't promote filters; for apparel, price, size and colour are the most used; a size filter near the top and expanded led 90% of participants to filter by size first (EXCERPT). | Theme filters, through Shopify Search & Discovery | Free Search & Discovery app plus theme settings. Not a custom section. |
| Reviews and customer photos | Baymard: 34% of sites don't let reviewers upload images; 33% don't aggregate fit feedback (2026 apparel research, EXCERPT). Spiegel Research Center: 5 reviews give 270% higher purchase likelihood than none (2017, OLDER THAN 12 MONTHS, EXCERPT). Vendor UGC lift numbers have no primary data (UNVERIFIED). | `reviews`, `review-avatars`, `rating-stars` blocks exist (data source unknown) | A review app with an app block. Not hand-built. |
| Size guide embed | Baymard: the size guide link must sit next to the size selector; 82-83% of apparel sites give too little sizing info; give metric and imperial (EXCERPT). | Kiwi app block sits right after the variant picker. Shrine also has a `product_sizing-chart` block. | Keep Kiwi where it is. Do not build a second one. |
| Brand story | No quantified evidence found. Orbit Media: top-converting pages are one third to one half "evidence" (EXCERPT). | `pp-founder` already exists [LOCAL] | Existing custom section or built-in image-with-text. |
| Bundles, upsells, frequently bought together | Baymard: 52% of desktop sites don't make cart cross-sells relevant; suggests "Complete the Look" for apparel (EXCERPT). AOV lift claims of 15-35% come from vendor blogs (UNVERIFIED). | `product_bundle-offer`, `product_complementary`, `product_upsell-block--product-info`, `product_quantity-gifts`, `cart_product-upsells` blocks exist | Built-in Shrine blocks plus Search & Discovery complementary products. Free Shopify Bundles app handles fixed bundles only (EXCERPT, fudge.ai). |

**Conclusion for this store.** The patterns in question D are mostly covered by Shrine blocks or apps already. Custom sections earn their place for brand-specific content that no app offers, like the existing temple marquee and garment anatomy.

**When to use which.** This is a synthesis, labelled MY PROPOSAL, from the [OFFICIAL] quotes in research-raw/official-docs/notes.md.

| Option | Use when | Non-developer can run it? |
|---|---|---|
| Built-in Shrine section or block | It already exists; adjust settings | Yes |
| App with app block (theme app extension) | Feature needs data or logic (reviews, bundles, options). Officially "don't edit theme code" and are removed cleanly on uninstall. | Yes |
| Custom `pp-` Liquid section | Brand-specific layout or content no app gives | No: assistant builds, owner reviews |
| Metafields or metaobjects with dynamic sources | Same section, different content per product (e.g. temple facts). "Dynamic sources aren't available for general theme settings." | Owner edits data in admin once set up; setup is developer-level |
| Custom Liquid block | One small snippet, no reuse | Risky: no validation, 50 KB limit, easy to break |
| Third-party section app | Need a generic section fast | Yes, but lock-in on uninstall |

---

## 9. Source log

Read depth key:
- **CHUNKS:** verbatim chunks from Shopify's docs search tool.
- **FULL:** the whole file was downloaded.
- **SUMMARIZED-FULL:** the whole page came back through WebFetch's summarizer.
- **EXCERPT:** search summary only.
- **BLOCKED:** could not be fetched.

Full per-agent logs with every query are in research-raw/*/notes.md.

### Official: Shopify
| Source | Date | Tool | Read depth |
|---|---|---|---|
| https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema | undated | search_docs_chunks | CHUNKS |
| https://shopify.dev/docs/storefronts/themes/architecture/templates/json-templates | undated | search_docs_chunks | CHUNKS |
| https://shopify.dev/docs/storefronts/themes/architecture/limits | undated | search_docs_chunks | CHUNKS |
| https://shopify.dev/docs/storefronts/themes/architecture/blocks (+ theme-blocks/schema, app-blocks) | undated | search_docs_chunks | CHUNKS |
| https://shopify.dev/docs/storefronts/themes/architecture/settings/input-settings | undated | search_docs_chunks | CHUNKS |
| https://shopify.dev/docs/storefronts/themes/architecture/settings/dynamic-sources | undated | search_docs_chunks | CHUNKS |
| https://shopify.dev/docs/storefronts/themes/best-practices/javascript-and-stylesheet-tags | undated | search_docs_chunks | CHUNKS |
| https://shopify.dev/docs/storefronts/themes/best-practices/performance (+ never-lazy-load-lcp-image, use-filter-chains, theme-check-tool) | undated | search_docs_chunks | CHUNKS |
| https://shopify.dev/docs/storefronts/themes/best-practices/accessibility | undated | search_docs_chunks | CHUNKS |
| https://shopify.dev/docs/storefronts/themes/store/requirements | undated | search_docs_chunks | CHUNKS |
| https://shopify.dev/docs/api/liquid (image_url, image_tag, stylesheet_tag, include) | undated | search_docs_chunks | CHUNKS |
| https://shopify.dev/docs/api/shopify-cli (+ theme-dev, theme-push, theme-pull, theme-share, theme-package, theme-check) | undated | search_docs_chunks | CHUNKS (theme-push read by me directly) |
| https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks (+ configuration, migrate) | undated | search_docs_chunks | CHUNKS |
| https://shopify.dev/docs/storefronts/themes/tools/github | undated | search_docs_chunks | CHUNKS |
| https://shopify.dev/docs/storefronts/themes/os20 ; /docs/apps/build/online-store/theme-app-extensions/configuration ; verify-support | undated | search_docs_chunks | CHUNKS |
| https://shopify.dev/docs/storefronts/themes/architecture/blocks/ai-generated-theme-blocks | undated | search_docs_chunks | CHUNKS |
| https://shopify.dev/docs/apps/build/ai-toolkit | undated | search_docs_chunks | CHUNKS |
| shopify.dev changelog: Dev MCP supports Liquid (2025-10-01, OLDER THAN 12 MONTHS); AI Toolkit (2026-04-09); Liquid developer preview (2026-07-21) | as stated | search_docs_chunks | CHUNKS |
| help.shopify.com: updating themes, version history, Custom Liquid, generate blocks, duplicate themes | undated | WebSearch | EXCERPT |
| npm @shopify/dev-mcp 1.16.0 (registry README + package tool registry) | 2026-09-25 | curl npm registry, tarball read (not installed) | FULL |
| https://github.com/Shopify/Shopify-AI-Toolkit (README, skills/shopify/SKILL.md, references/liquid.md) | updated 2026-10-02 | raw download, shallow clone in scratchpad | FULL / head |
| https://github.com/Shopify/liquid-skills (README, 3 SKILL.md) | created 2026-03-13 | raw download | FULL / head |
| https://github.com/Shopify/theme-liquid-docs ai/claude/CLAUDE.md | updated 2026 | raw download | lines 1-178 |
| https://github.com/Shopify/theme-tools (README, recommended.yml) | updated 2026-10-01 | raw download | FULL / head |
| https://github.com/Shopify/dawn .theme-check.yml ; Shopify/horizon (no CLAUDE.md, 404) | current | raw download | FULL |

### Official: Anthropic, Microsoft, Figma
| Source | Tool | Read depth |
|---|---|---|
| https://code.claude.com/docs/en/skills | WebFetch | SUMMARIZED-FULL |
| https://code.claude.com/docs/en/sub-agents | WebFetch | SUMMARIZED-FULL |
| https://code.claude.com/docs/en/hooks | WebFetch | SUMMARIZED-FULL |
| https://code.claude.com/docs/en/memory | WebFetch | FULL (saved, searched) |
| https://code.claude.com/docs/en/mcp | WebFetch | SUMMARIZED-FULL |
| https://github.com/microsoft/playwright-mcp README | raw download | searched |
| https://github.com/figma/mcp-server-guide README | raw download | lines 107-330 |

### Vendor
| Source | Tool | Read depth |
|---|---|---|
| easifyapps.com/docs (options-dont-show, app-activation, reposition-option-set-on-product-page) | WebSearch | EXCERPT (fetch BLOCKED) |
| intercom.help/kiwi-sizing-chart articles 10290927, 13256240, 10291102, 13256403; developers.kiwisizing.com | WebSearch | EXCERPT |
| shrine.io (features, theme-updates, terms, blog) | WebSearch | EXCERPT (fetch BLOCKED) |
| apps.shopify.com section-factory and other section apps; docs.appsections.com | WebSearch | EXCERPT |
| Baymard Institute articles listed in 8.3 | WebSearch | EXCERPT (fetch BLOCKED) |

### Practitioner
| Source | Date | Tool | Read depth |
|---|---|---|---|
| https://github.com/EcomExperts-io/Base (CLAUDE.md, .claude/settings.json, reviewer agent, .theme-check.yml) | updated 2026-10-02 | raw download | FULL / head |
| github.com/erikthalen/shopify-starter .theme-check.yml; jonathanmoore/kona-theme; mrvedmutha/bassface-theme-2026; dylanburkey/shopify-development-toolkit | 2026 | raw download | head |
| github.com/github/awesome-copilot shopify-expert.agent.md; github.com/ArtificialMonks/shopify-liquid | undated | WebFetch | SUMMARIZED-FULL |
| emilkowalski/skills, pbakaus/impeccable, Leonxlnx/taste-skill READMEs | 2026 | raw download | head |
| community.shopify.com threads 205043, 169273, 329958, 1557385 (older); 417178, 166189, 580094, 614173, 577864, 621122, 686447, 415152, 1362 | mostly undated | WebSearch | EXCERPT |
| letstalkshop.com, adsx.com, askphill.com, claudefa.st, monkeyman.agency, appycodes.com, seotldr.substack.com, fudge.ai, ed.codes, dominikatracy.com, appbrew.com, bigredjelly.com, dev.to (iamrobindhiman), medium.com/@Cavlemasters, websensepro.com, mgroupweb.com, shopcircle.co | 2025-2026 mostly, often undated | WebSearch | EXCERPT |
| Reddit (r/shopify, r/ShopifyeCommerce, r/ClaudeAI, r/ClaudeCode, r/vibecoding, r/webdev) | n/a | WebSearch (refused for reddit.com), WebFetch (refused) | NOT ACCESSIBLE |
| 10 YouTube videos in 8.2 plus 13 more found | various | WebSearch; WebFetch BLOCKED | NOT ACCESSIBLE (title and snippet only) |
| 3 Instagram reels | unknown | WebFetch, curl BLOCKED | NOT ACCESSIBLE; owner-pasted transcripts used |

### Local
| Source | Read depth |
|---|---|
| Store themes via Admin GraphQL (read only): theme_info, templates/product.json, sections/main-product.liquid, blocks/main-product_details.liquid, blocks/custom-liquid.liquid, layout/theme.liquid | FULL (research-raw/01-theme-observations.md) |
| temple-product-generator/theme/README.md, sections/pp-*.liquid, docs/decisions.md (18 Sep 2026 entries) | FULL / relevant sections |

---

## 10. Open gaps and what the owner should check by hand

**Not researched because of network blocks**
1. **No video was watched.** To fill section 8.2 properly, widen network access, or run on the Mac where the youtube-to-agent stack is installed. Start with uW39GOgc0wo (10 mistakes) and rNiw_9OO9ts. Network access is set under the cloud environment's settings, Edit, Network access; add youtube.com, or use a broader level.
2. **No Reddit thread was read.** First-hand failure reports, such as "AI said fixed but nothing changed" or "AI rewrote working code", likely live there and are missing here.
3. **Baymard, Easify, Kiwi and Shrine pages were seen only as search summaries.** Check the numbers in section 8.3 on baymard.com before quoting them anywhere public.

**Check by hand**
4. **Which theme is live?** The API says "Claude code original"; the repo README says "Claude Code V2". Confirm in Online Store > Themes before any push.
5. **Shrine licence and updates.** Search results show unofficial copies of Shrine PRO for sale. Confirm the store's copy has a valid shrine.io licence key, since updates depend on it.
6. **Latest Shrine version.** Shrine PRO 1.9.0 is dated 8 Jul 2025 (EXCERPT), which is older than 12 months. One summary mentions a "2.1.0" release in Dec 2025 that may be the non-PRO line. Check shrine.io/pages/theme-updates.
7. **How Shrine updates treat custom `pp-` files** (ZIP upload). No Shrine document found. Ask Shrine support, or test on a duplicate.
8. **Is the Sidekick "Generate" block feature offered on Shrine?** Shopify's changelog says Theme Store themes (EXCERPT); Shrine is not one.
9. **Kiwi developer name.** Listings name "Staytuned", not "Kiwi Commerce". Confirm it is the installed app (the app block handle is `kiwi-size-chart-recommender`).

**Not yet tested**
10. **Easify and Kiwi together.** No source tests them side by side. Both sit next to the variant picker. Kiwi's docs warn about variant apps that rebuild that area. After any product page change, test both by hand on a phone.
11. **AI Toolkit / Dev MCP telemetry.** It is on by default and can send code and the last prompt to Shopify. Decide whether to opt out before installing.
12. **The hook scripts in section 5.3** are untested proposals.

**My own claims to verify**
13. **Orange buttons fail contrast.** #F58000 against white measures 2.63:1 (computed in this session with the WCAG formula). White labels on the store's orange buttons fail the Theme Store 4.5:1 bar and even the 3:1 large-text bar. Black labels pass at 7.97:1. This is a brand decision for Evan; check the live buttons with any contrast checker to confirm.
14. **"44px primary buttons"** is a common practice, not a Shopify requirement. Shopify's Theme Store minimum is 24 by 24.
