# Building custom Shopify theme sections with an AI assistant: briefing

Researched 2026-10-03 for Peculiar People (peculiarpeopleco.com). Written for Claude Code and Claude.ai sessions that will build theme sections for Evan, who owns the store and is not a developer. Read this whole file before writing any theme code.

**Store facts this briefing assumes**
- Theme: **Shrine PRO, version 1.9.0, author Shrine**. Read from `config/settings_schema.json` (`theme_info`) of the live theme through the Admin API, read only. No full theme is in the local repos; `temple-product-generator/theme/` only holds Peculiar People's own `pp-*` files. Details: `docs/research-raw/theme-inspection.md`.
- Live (MAIN) theme: "Claude code original" (ID 193770258804). Unpublished: "Claude Code V2" (ID 194242150772), "Original" (ID 192015073652).
- Online Store 2.0, about 136 products, apparel print on demand. Installed apps that must keep working: Easify Product Options (product page dropdowns) and Kiwi Size Chart.
- Design tokens: Arial 16px body, Montserrat headings, black, white, navy #001A58, orange #F58000 buttons.

**How to read the labels**
- OFFICIAL = shopify.dev, help.shopify.com, Anthropic docs, or an official Shopify/Anthropic repo. PRACTITIONER = a named builder's blog, repo or video. UNVERIFIED = a claim no second source confirms. EXCERPT = read from a search-result summary because the page itself was blocked; treat the wording as close paraphrase.
- Network limits during this research: youtube.com, instagram.com, reddit.com, shopify.dev, help.shopify.com and community.shopify.com were blocked by this environment's network policy. shopify.dev was read through the Shopify connector's docs search (verbatim chunks with URLs). Videos were read through Higgsfield's video analysis (machine transcript plus machine description of the frames; no image files). See the source log, section 9.

---

## 1. Executive summary

1. **Check Shrine first.** The live theme already has 89 sections and 103 theme blocks, including collapsible content, content tabs, bundle deals, testimonials, reviews, a sizing-chart block, complementary products and upsell blocks (theme inspection, read only). Many "custom section" requests are a settings change on an existing Shrine section. Only build when Shrine cannot do it.
2. **Stack:** Claude Code + Shopify's official AI Toolkit plugin (docs search and a Theme Check based validator) + Shopify CLI (`theme dev`, `theme push`, `theme check`) + git + Playwright screenshots at phone and desktop widths. All free apart from the Claude subscription. ([AI Toolkit](https://github.com/Shopify/Shopify-AI-Toolkit), [Shopify CLI docs](https://shopify.dev/docs/api/shopify-cli/theme/theme-dev))
3. **Never work on the live theme.** Build on an unpublished theme (today: "Claude Code V2") or a CLI development theme, preview there, and leave publishing to Evan. Every source that describes a safe workflow says the same; the one video that edited a live theme did it with permission prompts switched off (video V1).
4. **Only add new files, prefixed `pp-`.** For Theme Store themes, Shopify auto-updates only while the shipped files are untouched, and code edits may not carry over in an update ([shopify.dev theme updates](https://shopify.dev/docs/storefronts/themes/store/success/updates)). Shrine appears to be sold outside the Theme Store (EXCERPT, web findings C7), so its updates are probably a new theme copy you move work into (UNVERIFIED). Either way, new `pp-` files are easy to find and re-copy. Editing a Shrine file is a last resort and gets logged.
5. **Everything a merchant would want to change is a schema setting or a block**, with `presets` so the section appears in the theme editor's Add section list. Hardcoded copy, images and colours are the most visible failure in the videos and community threads (failure F3).
6. **Shrine's product page accepts app blocks but not generic theme blocks.** `blocks/main-product_details.liquid` lists `@app` plus 48 named block types and no `@theme`. Kiwi and Easify app blocks can go there; a new custom block or a Shopify Magic generated block cannot without editing that Shrine file (theme inspection).
7. **Shrine uses old-style colour schemes** (`select` values `accent-1`, `accent-2`, `background-1`, `background-2`, `inverse`), not `color_scheme_group`. A `color_scheme` setting would return nil on this theme ([shopify.dev input settings](https://shopify.dev/docs/storefronts/themes/architecture/settings/input-settings)). Copy the pattern an existing Shrine section uses.
8. **"Done" means evidence:** Theme Check (or the AI Toolkit validator) output with zero errors on the new files, screenshots at 390px and 1440px wide, the section added and edited in the theme editor, and Easify plus Kiwi still working on a product page. Anthropic's own guidance is to give Claude a check it can run and to show evidence instead of claiming success ([best practices](https://code.claude.com/docs/en/best-practices)).
9. **Enforce the dangerous rules with hooks, not just CLAUDE.md.** CLAUDE.md is "context, not enforced configuration"; a PreToolUse hook that exits 2 actually blocks the command ([memory docs](https://code.claude.com/docs/en/memory), [hooks guide](https://code.claude.com/docs/en/hooks-guide)). Block publishing, pushing to the live theme, `theme push` without `--nodelete`, and edits to `config/settings_data.json`.
10. **One section per session, from a written spec** (template in section 6), committed to git before and after. AI editing of existing files tends to strip settings that look unused, which erases what the merchant entered (F12).

---

## 2. Recommended toolchain

"Non-dev?" says whether Evan can do it himself or it needs a developer-level setup step (done once, by Claude or a developer, then reused).

| Tool | What it does | Non-dev? | Cost | Source |
|---|---|---|---|---|
| Claude Code | Agent that reads and edits the theme files, runs CLI commands and checks | Using it: yes. Installing: one-time terminal step | Claude subscription. One creator says a $20 plan is enough (UNVERIFIED price) | [docs](https://code.claude.com/docs/en/best-practices); video V3 |
| Shopify AI Toolkit (Claude Code plugin) | Official Shopify skill: docs search plus a Liquid validator built on Theme Check. Install: `claude plugin install shopify-ai-toolkit@claude-plugins-official`. Released 9 April 2026 (EXCERPT, claudefa.st) | Install: one command. Use: automatic | Free, MIT. Sends usage data to Shopify by default; opt out by creating `~/.config/shopify-ai-toolkit/opt-out` | [GitHub](https://github.com/Shopify/Shopify-AI-Toolkit); [shopify.dev ai-toolkit](https://shopify.dev/docs/apps/build/ai-toolkit) |
| Shopify Dev MCP (`@shopify/dev-mcp`) | MCP server with `learn_shopify_api`, `search_docs_chunks`, `validate`, `validate_theme` (runs Theme Check on a theme folder, reads `.theme-check.yml`). Add: `claude mcp add --transport stdio shopify-dev-mcp -- npx -y @shopify/dev-mcp@latest` | Developer setup (Node.js) | Free | [npm](https://www.npmjs.com/package/@shopify/dev-mcp); shopify.dev ai-toolkit page; package source v1.16.0 |
| Shopify/liquid-skills (Claude Code plugin) | Official Shopify Liquid skills (`shopify-liquid-themes`, `liquid-theme-standards`, `liquid-theme-a11y`) plus a Liquid language server hookup | Install: three `/plugin` commands | Free | [GitHub](https://github.com/Shopify/liquid-skills) |
| Shopify CLI | `shopify theme dev` (local preview with hot reload on a hidden development theme), `theme pull`, `theme push --unpublished`, `theme check`, `theme share`, `theme duplicate` | Developer setup; Evan's Mac already has it logged in (temple-product-generator/theme/README.md) | Free | [theme dev](https://shopify.dev/docs/api/shopify-cli/theme/theme-dev), [theme push](https://shopify.dev/docs/api/shopify-cli/theme/theme-push) |
| Theme Check | Linter: syntax errors, unknown objects and filters, invalid schema, missing assets, image width/height, parser-blocking scripts | Runs inside the CLI or validator; no setup | Free | [checks list](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks), [theme-tools](https://github.com/Shopify/theme-tools) |
| Git + GitHub | History and rollback for the theme's custom files. Shopify's GitHub integration can also two-way sync a branch to a theme | Git: Claude runs it. GitHub integration: one-time admin setup | Free for private repos (UNVERIFIED current GitHub pricing) | [shopify.dev GitHub integration](https://shopify.dev/docs/storefronts/themes/tools/github); video V2 |
| Playwright (or the store-cro-audit capture script) | Opens the preview in a headless browser and saves screenshots at set widths so Claude can look at its own output | Claude runs it | Free; Chromium is preinstalled in cloud sessions | [Anthropic subagent example](https://code.claude.com/docs/en/sub-agents); `.claude/skills/store-cro-audit/scripts/capture.js` |
| Claude in Chrome | Claude drives a real Chrome window, reads console errors, takes screenshots | Evan can enable it; needs a direct Anthropic plan | Included in plan | [docs](https://code.claude.com/docs/en/chrome) |
| Figma MCP | Reads a Figma frame (layout, tokens, screenshot) so the agent builds to a design | Needs a Figma file to start from | Figma plan; one creator says a premium plan is needed (V10, UNVERIFIED) | Videos V7, V10; [Stargazer workflow](https://stargazerstudio.net/blog/figma-to-shopify-ai-workflow) (EXCERPT) |
| Shopify Magic / Sidekick "Generate" block | Writes a theme block from a text prompt inside the theme editor | Yes, no code | Free on eligible plans | [shopify.dev AI blocks](https://shopify.dev/docs/storefronts/themes/architecture/blocks/ai-generated-theme-blocks). **Limited on Shrine:** the section must accept `@theme`, and Shrine's product info block does not |
| Section Store (third-party sections) | Buy prebuilt sections; installed as theme code | Yes | "$9 each as a one-time purchase" (EXCERPT, vendor) | [section.store](https://section.store/) |

Not recommended as the default: page builders (Shogun, GemPages, PageFly, EComposer). They add a second editor and their own scripts; pricing in sources conflicts (see web findings A9).

**Which approach for which job (for a non-developer)**

| Need | Best fit | Why |
|---|---|---|
| Content or layout Shrine almost does | Existing Shrine section, change settings | No code, survives updates |
| Something this one store needs (story band, temple marquee, garment callouts) | Custom `pp-` section in the theme | shopify.dev positions theme app extensions for apps that serve many stores without editing theme code ([TAE config](https://shopify.dev/docs/apps/build/online-store/theme-app-extensions/configuration)); a single store's feature belongs in its theme (inference) |
| Same content structure repeated per product or temple (facts, care, fit notes) | Metafields or metaobjects connected to section settings through dynamic sources | Content lives in admin data, not code; dynamic sources work for section and block settings ([dynamic sources](https://shopify.dev/docs/storefronts/themes/architecture/settings/dynamic-sources)) |
| A small one-off block on a page that accepts theme blocks | Shopify Magic generated block | Quick, but check its settings and styling by hand (EXCERPT, neat.digital) |
| Reviews, size charts, product options | The app's own app block | Kiwi and Easify ship app blocks; Shrine's product column accepts `@app` |

---

## 3. Failure modes

Each row has an ID used by the CLAUDE.md rules in section 4. "Confirmed by" separates official sources from practitioner claims.

| ID | Symptom | Cause | Prevention rule or check | Sources |
|---|---|---|---|---|
| F1 | Section renders blank where data should be, or upload fails with a Liquid error | The model used an object, filter, tag or setting type that does not exist or is out of date. Liquid outputs nothing for a nil value instead of erroring | Look up unfamiliar objects and filters in the docs (AI Toolkit / Dev MCP `search_docs_chunks`) before using them. Run Theme Check (`UndefinedObject`, `UnknownFilter`, `ValidSchema`, `LiquidHTMLSyntaxError`). Then look at the rendered page with a real product, because lint does not catch nil values | OFFICIAL: [Theme Check checks](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks); Dev MCP `validate_theme` description ("hallucinated Liquid content"). PRACTITIONER (EXCERPT): [fudge.ai](https://www.fudge.ai/guides/debug-shopify-liquid-with-claude/) ("made-up fields like product.custom_price resolve to nil"), [dev.to](https://dev.to/yakohere/how-to-debug-shopify-liquid-a-complete-guide-2655) |
| F2 | Section missing from "Add section", or "Invalid schema" on save or push | No `presets`; invalid JSON; Liquid inside `{% schema %}`; schema `name` over 25 characters; duplicate setting ids; wrong setting type or a default a type does not allow; a `class` with characters Shopify rejects; file in the wrong folder; or the AI returned a whole HTML page instead of a section | One `{% schema %}` per file with valid JSON. Include `presets`. Keep `name` at 25 characters or fewer. Unique setting ids. Check each setting type against the input settings list. Run Theme Check. Then open the theme editor and add the section | OFFICIAL: [section schema](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema), [limits](https://shopify.dev/docs/storefronts/themes/architecture/limits), [integrate sections](https://shopify.dev/docs/storefronts/themes/best-practices/editor/integrate-sections-and-blocks) ("Files without presets ... can't be removed using the theme editor"). PRACTITIONER: [Shopify/cli#4871](https://github.com/Shopify/cli/issues/4871) ("Invalid schema: class is invalid", Nov 2024, older than 12 months); [Community 631503](https://community.shopify.com/t/claude-code-produced-html-beginner/631503) (EXCERPT, Claude returned full HTML) |
| F3 | Evan cannot change text, image, link or colour in the editor; colours ignore the theme | AI hardcodes values to match a description or design. Designs specify one value, so the agent sees no reason to add a control | Every merchant-facing string, image, link, colour choice and spacing value is a setting or block setting. Write the settings list in the spec before building. Review the schema against the spec | PRACTITIONER: video V4 (Cursor "hardcoded the styles of the navigational bar"); [EcomExperts-io/Base rules](https://github.com/EcomExperts-io/Base) ("30 of 31 new sections shipped without any of this"; "a Figma frame specifies exactly one spacing value"); EXCERPT [neat.digital](https://neat.digital/blogs/blogs/shopify-ai-sidekick-magic-honest-review-2026) (AI blocks "lacks proper schema settings") |
| F4 | Customers see a broken page; Evan's editor changes vanish; files disappear; no way back | Editing the live theme; `theme push` overwriting `config/settings_data.json` or templates the merchant edited in the editor; `theme push` without `--nodelete` deleting every remote file missing from the local folder; development themes deleted after 7 days idle; admin history is per file only | Work on an unpublished theme. Never push to or publish the live theme (hook-enforced). Always `--nodelete` and `--only` on push. Never write `config/settings_data.json`. Pull templates before changing them. Commit before every change | OFFICIAL: [theme push flags](https://shopify.dev/docs/api/shopify-cli/theme/theme-push), [theme dev](https://shopify.dev/docs/api/shopify-cli/theme/theme-dev) (7-day deletion). LOCAL: `temple-product-generator/theme/README.md` ("without it a push removes every theme file that is not in this folder"). PRACTITIONER: video V1 (live theme edit), video V6 (Claude pushes to the git branch connected to a store theme), video V9 (push rejected as non-fast-forward; work on a copy "so the live theme doesn't get affected"), Community thread "Pushing a theme overwrites settings and section data" (EXCERPT, older than 12 months), [letstalkshop](https://www.letstalkshop.com/blog/how-to-use-claude-code-for-shopify-liquid-theme) (EXCERPT, "config/settings_data.json file should never be touched by Claude Code"). UNVERIFIED (Help Center snippet): per-file "Older versions" is the only built-in rollback |
| F5 | New section changes how other sections look, or other sections break it; content clipped or overlapping on mobile | Broad selectors (`h2`, `.button`), global CSS in assets, `!important`, z-index fights, `overflow: hidden` wrappers. `{% stylesheet %}` does not render Liquid and is injected once per file, so per-instance values put there do not work | Prefix every class with `pp-`. Scope rules under the section wrapper (`#shopify-section-{{ section.id }}` or a `pp-` root class). Per-instance values go in an inline `<style>` or CSS variables on the element. No `!important`, no tag selectors, no edits to Shrine CSS files. Use Shrine's colour scheme classes and font settings instead of new hex values | OFFICIAL: [stylesheet tags](https://shopify.dev/docs/storefronts/themes/best-practices/javascript-and-stylesheet-tags); [liquid-skills standards](https://github.com/Shopify/liquid-skills) ("Never use `!important`", "Never use IDs as selectors"). PRACTITIONER (EXCERPT): Community [615944](https://community.shopify.com/t/small-css-fix-needed-for-custom-ai-generated-section-mobile-clipping-carousel-dots/615944) (mobile clipping in an AI section), [621122](https://community.shopify.com/t/overlapping-issue-with-ai-generated-section/621122) (AI sticky header overlap). CONFLICT: liquid-skills says never use IDs as selectors; Shrine's own blocks scope by `#ContentContainer-{{ block.id }}`. Follow the `pp-` class approach and use the id only for per-instance values. UNCONFIRMED: a shopify.dev rule requiring `#shopify-section-` selectors |
| F6 | Add to cart does nothing visible, cart count stale, variant change does not update, Easify options vanish, Kiwi size chart moves or disappears | Custom JS rebinds the product form or variant events; adds to cart without firing the theme's cart refresh; loads a library that clashes; changes markup an app injects into. Easify docs list theme, cart drawer and price-app conflicts. Kiwi can inject by CSS selector | Do not modify Shrine's product form, variant picker, `<product-info>` element or cart drawer. New JS is a custom element registered once, scoped to its own root, no external libraries. Re-initialise on `shopify:section:load`. Test a product page with Easify options and the Kiwi chart before and after | OFFICIAL: [editor JS events](https://shopify.dev/docs/storefronts/themes/best-practices/editor/integrate-sections-and-blocks). APP DOCS (EXCERPT): [Easify options don't show](https://easifyapps.com/docs/options-dont-show/), [Kiwi injection selector](https://intercom.help/kiwi-sizing-chart/en/articles/10290924-how-to-change-where-size-chart-shows-on-product-page-using-sizing-injection-selector). PRACTITIONER (EXCERPT): Community [629483](https://community.shopify.com/t/add-to-cart-buttons-not-working-on-ai-generated-theme-section-blocks/629483) ("adding to cart and updating the cart count bubble/cart drawer are 2 separate tasks"), [shopify.dev forum 8885](https://community.shopify.dev/t/issues-with-implementing-app-blocks-that-depend-on-variant-changes/8885) |
| F7 | Looks fine in the editor on a laptop, broken on a phone; buttons too small to tap | Agent only checked desktop or did not check at all. `theme dev` preview works only in Chrome | Screenshot at 390px and 1440px wide and look at both. Interactive targets at least 24x24px (Shopify's accessibility page). Evan checks the preview link on his own phone before publishing | OFFICIAL: [theme dev](https://shopify.dev/docs/api/shopify-cli/theme/theme-dev) (Chrome only), [accessibility](https://shopify.dev/docs/storefronts/themes/best-practices/accessibility). PRACTITIONER: video V4 used screenshots to catch misalignment; [Stargazer](https://stargazerstudio.net/blog/figma-to-shopify-ai-workflow) (EXCERPT, "the model can't see what it's building") |
| F8 | Slower pages, layout jumping as images load | Raw `<img>` tags without width and height; full-size images; lazy-loading the first big image; scripts without `defer`; remote CDN libraries | `image_url` with a width piped into `image_tag` with `widths` and `sizes`. Eager load only the first large image in a section that can sit at the top of a page. `defer` scripts, no remote assets. Theme Check `ImgWidthAndHeight`, `ParserBlockingScript`, `RemoteAsset` must pass | OFFICIAL: [filter chains](https://shopify.dev/docs/storefronts/themes/best-practices/performance/use-filter-chains), [responsive images](https://shopify.dev/docs/storefronts/themes/best-practices/performance/use-responsive-images), [never lazy-load LCP](https://shopify.dev/docs/storefronts/themes/best-practices/performance/never-lazy-load-lcp-image). UNVERIFIED (EXCERPT, eesel.ai, possibly older than 12 months): page speed drops after AI blocks |
| F9 | Keyboard users cannot reach or operate the section; screen readers read nothing useful; animation cannot be stopped | Div-and-click markup, missing alt text, no focus styles, colour contrast too low, motion ignoring reduced-motion | Semantic HTML (`button`, `a`, headings in order). Alt text from the image setting. Visible focus. Contrast 4.5:1 for body text, 3:1 for large text and icons. Respect `prefers-reduced-motion`; autoplay must be pausable | OFFICIAL: [accessibility](https://shopify.dev/docs/storefronts/themes/best-practices/accessibility); [liquid-theme-a11y skill](https://github.com/Shopify/liquid-skills). Note: orange #F58000 with white text likely fails 4.5:1 for normal-size text; measure it (UNVERIFIED, not measured here) |
| F10 | After a Shrine update, custom work is gone, the Kiwi block is missing, or a custom file clashes with a new Shrine file | Updates install as a new theme copy; code edits to shipped files may not carry over; an update can add a file with the same name; Kiwi's own docs say updates can remove its app block | New files only, all prefixed `pp-`. Keep a manifest of custom files and of any Shrine file edited. After any update, re-copy from git, re-add app blocks, and rerun the QA checklist | OFFICIAL: [updates](https://shopify.dev/docs/storefronts/themes/store/success/updates) (auto-update only when files are untouched). APP DOCS (EXCERPT): [Kiwi after theme update](https://intercom.help/kiwi-sizing-chart/en/articles/10291102-size-chart-missing-after-theme-update). CONFLICT: Help Center (EXCERPT) says theme editor customisations carry over and code edits carry over when they do not conflict; practitioner posts say code edits never carry over. Treat it as "may not carry over" and check |
| F11 | Claude says the section is done; it is not on the page, the validator did not actually run, or a setting does nothing | Agents report success from intent, not from a result. Liquid fails silently. The AI Toolkit validator was reported shipping without its dependencies in 2.0.0. Sidekick cannot verify placement | Require evidence in the report: the exact command run and its output, screenshots, and the editor test. A Stop hook runs Theme Check before Claude can finish. If a validator prints nothing, treat it as not run | OFFICIAL: [best practices](https://code.claude.com/docs/en/best-practices) ("show evidence rather than asserting success"). PRACTITIONER (EXCERPT): [alphaguru](https://alphaguruai.substack.com/p/whats-going-on-with-claude-code), r/ClaudeAI post archived at [JHU AI Voices](https://digitalscholarship.library.jhu.edu/s/aivoices/item/360), [shopify.dev forum 36456](https://community.shopify.dev/t/sidekick-should-verify-theme-app-embed-block-section-placement-not-just-guide/36456), [forum 38075](https://community.shopify.dev/t/ai-toolkit-liquid-validator-still-ships-without-its-dependencies-in-2-0-0-github-11/38075) (title only) |
| F12 | A later edit breaks something that worked; Evan's saved settings disappear; a "small" request rewrites half a file | Agent refactors beyond the ask, removes schema settings that look unused (which wipes merchant values), renames setting ids, or keeps patching after repeated failures. Checkpoints do not track Bash edits | One section per session. Never remove or rename an existing setting id. Commit before each change and show the diff. After two failed fixes on the same issue, stop, summarise and start a fresh session | PRACTITIONER (EXCERPT): [letstalkshop](https://www.letstalkshop.com/blog/how-to-use-claude-code-for-shopify-liquid-theme) ("removing them wipes their customizations"). OFFICIAL: [checkpointing](https://code.claude.com/docs/en/checkpointing) ("does not track files modified by Bash commands"), [best practices](https://code.claude.com/docs/en/best-practices) ("corrected Claude more than twice ... Run /clear") |
| F13 | Agent changes products, theme or store data without being asked | AI Toolkit can operate on the real store once authorised; creators run Claude with permission prompts switched off | Never run with permission prompts disabled. Grant the toolkit only the scopes the task needs. Theme work never needs product write access | PRACTITIONER: videos V1 and V3 (permission prompts skipped, live edits, bulk product edits) |

---

## 4. Ready-to-paste CLAUDE.md rules for a Shopify theme repo

Paste into the CLAUDE.md of whatever folder holds the theme files. Each rule ends with the failure mode it prevents. Keep it short; Anthropic's guidance is under 200 lines per CLAUDE.md ([memory](https://code.claude.com/docs/en/memory)).

```markdown
# Shopify theme rules (Shrine PRO 1.9.0)

## Where you work
- Never edit, push to, or publish the live theme. Work only on the unpublished theme named in the task. (F4)
- Never run `shopify theme publish`. Publishing is Evan's decision. (F4)
- Every `shopify theme push` uses `--nodelete` and `--only` for the files you changed, plus `--theme <unpublished id>`. (F4)
- Never create, edit or push `config/settings_data.json`. (F4, F12)
- Commit to git before you change a file and after the change passes QA. (F4, F12)
- At the start of every session, pull the current theme files (git pull, or shopify theme pull --theme <id> --only <files>) before editing, because editor saves change the theme behind your back. (F4)

## What you build
- Before building, check whether an existing Shrine section or block already does the job, and say which one. (F12)
- New files only. Name every new section, block, snippet and asset `pp-<name>`. Do not edit Shrine's shipped files. If a Shrine file must change, stop, explain why, and log it in THEME-EDITS.md. (F10)
- One section per session, built from the written spec. Do not touch files the spec does not name. (F12)
- Every section has exactly one `{% schema %}` with valid JSON, a `name` of 25 characters or fewer, unique setting ids, and a `presets` entry. (F2)
- Every piece of text, image, link, colour choice and spacing value a merchant would change is a setting or a block setting. Defaults match the store: Arial body, Montserrat headings, black, white, navy #001A58, orange #F58000 buttons. (F3)
- For colour, copy the colour scheme setting pattern an existing Shrine section uses (select values accent-1, accent-2, background-1, background-2, inverse). Do not use the `color_scheme` setting type; this theme has no color_scheme_group. (F3, F5)
- Never remove or rename an existing setting id. Adding settings is fine. (F12)

## How you write it
- Look up any Liquid object, filter, tag or setting type you have not used in this repo before, using the Shopify AI Toolkit or Dev MCP docs search. Do not guess. (F1)
- Use `render`, never `include`. (F1)
- Images: `image_url` with a width, then `image_tag` with `widths` and `sizes`. Only the first large image of a top-of-page section loads eagerly. (F8)
- CSS: every class starts with `pp-`, every rule is scoped to the section root, no tag selectors, no `!important`, no edits to Shrine CSS files. Per-instance values go in an inline `<style>` or CSS variables, because `{% stylesheet %}` does not render Liquid. (F5)
- JavaScript: one custom element per feature, registered once with `if (!customElements.get(...))`, deferred, no external libraries, re-initialised on `shopify:section:load`. (F6)
- Do not modify the product form, variant picker, `<product-info>` element or cart drawer. Easify and Kiwi depend on them. (F6)
- Semantic HTML, alt text from the image setting, visible focus, 4.5:1 text contrast, and `prefers-reduced-motion` respected. (F9)

## Before you say done
- Run Theme Check (AI Toolkit validator in full-theme mode, Dev MCP `validate_theme`, or `shopify theme check`) and paste the output. Zero errors in the files you changed. (F1, F2, F8, F11)
- Take screenshots at 390px and 1440px wide of the preview with a real product, and look at them. (F7, F11)
- Add the section in the theme editor, change each setting once, and confirm the page updates. (F2, F3)
- Open one product page and confirm the Easify options and the Kiwi size chart still show and work. (F6)
- Report the commands you ran, their output, and the screenshot paths. Never report success you did not observe. (F11)
- If the same problem survives two fix attempts, stop and summarise instead of trying a third. (F12)
- Never run Claude Code with permission prompts disabled for theme work. (F13)
```

---

## 5. Proposed skills, subagents and hooks

Install paths follow Anthropic's docs: skills in `.claude/skills/<name>/SKILL.md`, subagents in `.claude/agents/<name>.md`, hooks in `.claude/settings.json` ([skills](https://code.claude.com/docs/en/skills), [subagents](https://code.claude.com/docs/en/sub-agents), [hooks](https://code.claude.com/docs/en/hooks-guide)). None of these exist in the repo yet. Setting them up is a developer-level step done once; using them is not.

### 5.1 Use first: Shopify's own skills (ADAPTED FROM, install rather than rewrite)
- `shopify-ai-toolkit` plugin. ADAPTED FROM [Shopify/Shopify-AI-Toolkit](https://github.com/Shopify/Shopify-AI-Toolkit). Its skill says "Validation is mandatory: never return generated code you have not run through this command" and "Three attempts, then return your best effort with an explanation." Use the full-theme mode (`--theme-path` plus `--files`), which the GitHub research found catches missing translation keys and assets that single-block mode skips.
- `liquid-skills` plugin. ADAPTED FROM [Shopify/liquid-skills](https://github.com/Shopify/liquid-skills). Gives Liquid, CSS standards and accessibility rules plus the Liquid language server.
- Do not copy rules from [Shopify/skeleton-theme AGENTS.md](https://github.com/Shopify/skeleton-theme/blob/main/AGENTS.md): it describes a theme with no `sections/` folder.

### 5.2 `pp-section-spec` skill (MY PROPOSAL, based on Anthropic's "interview first, then write SPEC.md" advice)
```markdown
---
name: pp-section-spec
description: Turn Evan's request for a new store section into a written spec before any code. Use when Evan asks for a new section, block, or page element on the Shopify store.
disable-model-invocation: false
---
1. Read docs/shopify-custom-sections-research.md sections 1 to 4.
2. List Shrine sections and blocks that could already do this (sections/ and blocks/ in the pulled theme). If one fits, say which settings to change and stop.
3. Ask Evan only what the spec template (section 6 of the briefing) still lacks, in plain language, max 5 questions.
4. Write specs/pp-<name>.md from the template. Every editable element gets a named setting with type and default.
5. Show the spec to Evan. Do not build until he approves it.
```
Basis: [best practices](https://code.claude.com/docs/en/best-practices) ("have Claude interview you first", write SPEC.md, run it in a fresh session).

### 5.3 `pp-section-builder` skill (ADAPTED FROM Shopify/liquid-skills, Shopify AI Toolkit references/liquid.md, and EcomExperts-io/Base rules)
```markdown
---
name: pp-section-builder
description: Build one approved pp- section for the Shrine PRO theme from specs/pp-<name>.md, on the unpublished theme only. Use after a spec is approved.
---
1. Confirm the spec file exists and is approved. Confirm the target theme ID is unpublished (shopify theme list). Stop if it is live.
2. git commit the current state.
3. Read one existing Shrine section of similar shape and copy its colour scheme and spacing pattern.
4. Write sections/pp-<name>.liquid (and blocks/snippets/assets only if the spec names them). Follow the CLAUDE.md rules.
5. Validate: AI Toolkit validator in full-theme mode on the changed files, or shopify theme check. Fix errors. Max three rounds, then report.
6. Push only the new files: shopify theme push --theme <id> --nodelete --only <each file>.
7. Hand off to the pp-section-qa subagent. Do not report done until it returns PASS.
```
Sources: liquid-skills rules quoted in section 3; AI Toolkit `references/liquid.md` ("Use `{{ block.shopify_attributes }}` on block wrapper elements", "DO NOT reference JS/CSS libraries"); EcomExperts Base CLAUDE.md ("Every new section exposes ... plus a `presets` entry").

### 5.4 `pp-section-qa` subagent (ADAPTED FROM Anthropic's `browser-tester` example and mrvedmutha/bassface-theme-2026's `shopify-validator` agent)
```markdown
---
name: pp-section-qa
description: Independently verify a newly built pp- section on the unpublished theme. Use proactively after any section is built or changed.
tools: Read, Grep, Glob, Bash
mcpServers:
  - playwright:
      type: stdio
      command: npx
      args: ["-y", "@playwright/mcp@latest"]
---
You did not write this code. Assume it is broken until you see otherwise.
Rules that apply even if CLAUDE.md is not loaded: never push, never publish, never touch config/settings_data.json, flag only real problems with evidence.
Run every item of the pre-publish QA checklist (briefing section 7) and return a table: item, PASS or FAIL, evidence (command output excerpt or screenshot path).
Never edit theme files. Never push. Never publish.
```
The `mcpServers` block is copied from Anthropic's subagent docs example ([sub-agents](https://code.claude.com/docs/en/sub-agents)). A fresh subagent reviews better because "Claude won't be biased toward code it just wrote" ([best practices](https://code.claude.com/docs/en/best-practices)).

### 5.5 Guard hooks (ADAPTED FROM theoseleve-glitch/volta_web, Ez-flove/shopify-theme-training, EcomExperts-io/Base; script is MY PROPOSAL, untested)

`.claude/settings.json`:
```json
{
  "permissions": {
    "deny": [
      "Edit(config/settings_data.json)",
      "Write(config/settings_data.json)"
    ]
  },
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          { "type": "command", "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/theme-guard.sh" }
        ]
      }
    ]
  }
}
```

`.claude/hooks/theme-guard.sh` (must be executable):
```bash
#!/bin/bash
# Blocks live-theme pushes, publishing, and pushes that could delete remote files.
cmd=$(jq -r '.tool_input.command // ""')
if echo "$cmd" | grep -Eq 'shopify +theme +publish'; then
  echo "Blocked: publishing is Evan's decision." >&2; exit 2
fi
if echo "$cmd" | grep -Eq 'shopify +theme +push'; then
  if echo "$cmd" | grep -Eq -- '(--live|-l( |$)|--allow-live|-a( |$)|--publish|-p( |$))'; then
    echo "Blocked: push to the unpublished theme by --theme <id>, never --live, --allow-live or --publish." >&2; exit 2
  fi
  if ! echo "$cmd" | grep -q -- '--nodelete' || ! echo "$cmd" | grep -q -- '--only'; then
    echo "Blocked: theme push needs --nodelete and --only <files>." >&2; exit 2
  fi
fi
exit 0
```
Mechanism from the docs: hook input arrives as JSON on stdin with `tool_input.command`; exit 2 "blocks the tool call" and the stderr text goes back to Claude ([hooks](https://code.claude.com/docs/en/hooks)). Flags taken from the shopify.dev `theme push` page (`-l/--live`, `-a/--allow-live`, `-p/--publish`, `-n/--nodelete`, `-o/--only`). Caveat from Anthropic's permission docs: a command written another way may not match a pattern, so this is a safety net, not a guarantee.

A Stop hook that runs Theme Check (the EcomExperts Base pattern: "a Theme Check error in any file changed this session" blocks the turn) is worth adding after the first build, once the output format of `shopify theme check --output json` on this theme has been looked at. Shrine's own files may already have offences, so the hook must only fail on files changed in the session. Anthropic caps repeated Stop-hook continuations at 8 ([hooks](https://code.claude.com/docs/en/hooks)).

---

## 6. Spec template for one custom section

Copy into `specs/pp-<name>.md`. A spec is ready when every field is filled or marked "not needed".

```markdown
# Section spec: pp-<name>

## 1. Purpose (one sentence)
What the shopper should understand or do after seeing this section.

## 2. Shrine check
Existing Shrine sections/blocks considered and why they do not fit:
-

## 3. Where it goes
- Template(s): (home / product / collection / page:<handle>)
- Position: (above / below which existing section)
- Must it sit inside the product info column? (yes means a Shrine file edit; see briefing F10)

## 4. Content and settings (every editable thing)
| Element | Setting id | Type | Default | Notes |
|---|---|---|---|---|
| Heading | heading | inline_richtext | "..." | |
| Body | body | richtext | "..." | |
| Image | image | image_picker | none (pickers have no default) | alt text from the image |
| Button label | button_label | text | "..." | |
| Button link | button_link | url | | |
| Colour scheme | color_scheme | select (Shrine values) | background-1 | copy from an existing Shrine section |
| Top/bottom padding | padding_top / padding_bottom | range | | min, max, step, default all set |

## 5. Repeating items (blocks)
- Block type(s), their settings, min/max count, preset count:

## 6. Layout
- Desktop (1440px):
- Phone (390px):
- Reference: (screenshot, Figma frame, or a URL with what to copy and what to ignore)

## 7. Behaviour
- Interactions (accordion opens, slider moves, nothing):
- Motion and its reduced-motion fallback:

## 8. Data
- Pulls from: (static settings / product / collection / metafield <namespace.key> / metaobject <type>)
- Empty state when data is missing:

## 9. Must not break
- Easify options and Kiwi size chart on product pages
- Other sections' styles

## 10. Done means
- QA checklist (briefing section 7) all PASS, with evidence
- Evan has seen the preview link on his phone
```

Why this shape: sources agree the first output is usable when the prompt states the Shopify constraints up front and lists every setting ("making every text and image field a schema setting (not hard-coded), adding a 'presets' entry", EXCERPT, [fudge.ai](https://www.fudge.ai/guides/claude-prompts-shopify/) / [flagship.inc](https://flagship.inc/en/columns/ai-for-shopify-theme-development), attribution between the two unclear). Video V3 notes that adding the theme ID to the prompt made the result more reliable (creator claim).

---

## 7. Pre-publish QA checklist (the AI runs it and reports each line)

Report as a table: item, PASS / FAIL / NOT RUN, evidence. NOT RUN is never reported as PASS.

**Code**
1. Theme Check or AI Toolkit validator run on the theme folder; zero errors in changed files. Paste the command and output. (F1, F2, F8)
2. Schema: one `{% schema %}`, valid JSON, `name` ≤ 25 characters, unique ids, `presets` present. (F2)
3. Every element in spec section 4 exists as a setting with the stated type and default. (F3)
4. No hex colours or font names hardcoded in markup or CSS except as setting defaults. (F3, F5)
5. All classes `pp-` prefixed, rules scoped, no `!important`, no tag selectors. (F5)
6. JS: custom element, defined once, deferred, no remote scripts, handles `shopify:section:load`. (F6, F8)
7. Images use `image_url` + `image_tag` with `widths` and `sizes`; width and height present. (F8)
8. `git diff --stat` shows only files named in the spec; no Shrine file changed; `config/settings_data.json` untouched. (F4, F10, F12)

**Rendered** (on the unpublished theme's preview, with a real product)
9. Screenshot at 1440px wide, saved and looked at. (F7)
10. Screenshot at 390px wide, saved and looked at; nothing clipped or overlapping; tap targets at least 24x24px. (F7)
11. Browser console shows no new errors. (F6, F11)
12. Keyboard: Tab reaches every control with a visible focus ring; images have alt text; text contrast 4.5:1. (F9)
13. With reduced motion turned on, animations stop or simplify. (F9)

**Theme editor**
14. Section appears under Add section and can be added, moved and removed. (F2)
15. Each setting changed once updates the preview; blocks can be added, reordered, removed. (F3)

**Apps and neighbours**
16. One product page: Easify options appear, a selection changes the price or line item as before, add to cart works and the cart updates. (F6)
17. Kiwi size chart link/button still appears in the same place and opens. (F6, F10)
18. Header, footer and the sections above and below look unchanged. (F5)

**Handoff**
19. Preview link given to Evan, with the theme name, so he can check on his phone. Publishing stays with Evan. (F4, F7)

---

## 8. Video and reel findings

Method: YouTube could not be opened from this environment. Each video was run through Higgsfield's video analysis, which returns, per scene, an "audio" field (machine transcription, sometimes condensed) and a "visual" field (machine description of the frames). No image frames were saved, so on-screen code and commands are only known when the presenter read them aloud or the description mentions them. Treat every quote below as close paraphrase. Raw output: `docs/research-raw/youtube/`. Lengths come from the last scene timestamp. Upload dates came from search-result "days ago" text and are approximate.

The `/watch` skill Evan's earlier research used (yt-dlp, ffmpeg frames, local Whisper) is not installed in this cloud container; nothing was installed.

### V1. New Shopify AI Toolkit: Claude Code Setup + Demo (April 2026)
- https://www.youtube.com/watch?v=ptnWksC9TXY | channel UNKNOWN | approx 12 April 2026 | 7:45 | worked from: machine transcript plus frame descriptions (full video)
- Built: no section. Installed the AI Toolkit in Claude Code, queried products and analytics, then changed a homepage headline from "True Results" to "Real Results".
- Tools: Claude Code, Shopify AI Toolkit plugin, store auth in the browser.
- Commands (as spoken, paraphrased by the analysis): launched Claude with "dangerously skip permissions" so "it doesn't keep asking me about permissions"; "plugin marketplace add shopify-ai-toolkit"; then the plugin install command, "user scope".
- What went wrong on screen: the theme edit was "applied ... to my live theme". The presenter says "I've just skipped ahead", so the edit itself is not shown. No duplicate theme, git or preview.
- Copy: the install route and the idea of asking the agent to find which template and section hold a piece of text.
- Ignore: skipping permissions and editing the live theme (F4, F13).
- Unverified: the exact commands typed; the analysis gives no on-screen text.

### V2. Build Shopify Themes in MINUTES -[Claude Code & MCP]
- https://www.youtube.com/watch?v=0tEkfZ4vtcs | channel likely WebSensePro (UNVERIFIED) | approx 13 March 2026 | 11:35 | machine transcript plus frame descriptions
- Built: no section. Set up a Horizon theme in a GitHub repo, connected it with Shopify's GitHub integration on a development store, installed the Claude Code VS Code extension and the Dev MCP.
- Commands (spoken): "'git init', 'git add .', 'git commit'"; checked the MCP with "/mcp" showing "shopify-dev-mcp connected". The MCP add command was copied from shopify.dev but its text is not in the analysis.
- Shown working: an edit saved in the admin code editor appeared on GitHub as a commit by the Shopify bot (two-way sync).
- Copy: GitHub integration as the history and rollback layer; development store for testing.
- Ignore: the title's "in MINUTES"; no theme is built.

### V3. [Shopify AI Toolkit Tutorial] - Build Themes & Automate SEO in Minutes
- https://www.youtube.com/watch?v=pom070QQgpQ | presenter's store is "devwebsensepro.myshopify.com" (channel likely WebSensePro, UNVERIFIED) | approx 21 April 2026 | 15:26 | machine transcript plus frame descriptions
- Built: a before/after image slider section on a duplicate of the "Savor" theme, on a development store with dummy data.
- Tools: Node.js, Claude Code, Shopify CLI, AI Toolkit plugin, Dev MCP, Shopify CLI connector app (installed in the store during auth).
- Prompts (spoken): "please create duplicate of live Savor theme and let me know once done"; "please create before/after slider section in theme ID, let me know once done". The presenter says adding the theme ID makes it "more specific".
- Shown working: the section appeared in Add section in the theme editor and the image pickers worked.
- Concerns: the presenter clicked "publish" on the new theme copy before testing in the editor (spoken: "hit refresh again and let's click on publish"); bulk updates to 200+ image alt tags and SEO fields from one prompt; says connecting by store name "hallucinates sometimes" and uses a prepared command instead (text not captured). Toolkit needed extra scopes mid-task (edit products, edit themes).
- Copy: duplicate first, name the theme ID in every prompt, check the result in the theme editor.
- Ignore: publishing before QA; bulk store edits as part of theme work (F13).
- Unverified: whether the slider had presets, settings, accessibility or mobile behaviour beyond what is shown.

### V4. Vibe Coding For Shopify Theme Developers
- https://www.youtube.com/watch?v=Hi2p1ajssmE | channel: Coding with Jan (from search result) | date UNKNOWN; the presenter uses "Claude 3.7 Sonnet" and Shopify CLI "3.76.2", which suggests early 2025: **likely older than 12 months** | 13:42 | machine transcript plus frame descriptions
- Built: in Cursor, a new theme from `shopify theme init`, a custom announcement bar, nav bar colour change, and a homepage-only sale popup.
- Commands (spoken): the agent tried "Shopify theme serve", which the presenter says is wrong; it then used "Shopify theme dev". It hit a port in use and moved to 9293.
- What went wrong on screen: button label misaligned (fixed by pasting a screenshot); "a small dot" instead of a dotted background; the logo disappeared after the nav colour change; the agent "hardcoded the styles of the navigational bar" instead of using the colour scheme setting.
- Presenter's conclusion (spoken): learn enough to "identify issues", and "use Git whenever you work with cursor or vibe coding tools".
- Copy: screenshot-driven fixes; telling the agent the project was made with Shopify CLI so it does not assume Theme Kit.
- Ignore: hardcoding settings; the model and CLI versions are dated.

### V5. The NEW Shopify Horizon theme & AI Theme blocks (SHOPIFY DEVELOPER analysis)
- https://www.youtube.com/watch?v=PBnQeTjOggM | presenter "Bosidev" (spoken) | refers to Summer Editions 2025 "last week": **older than 12 months** | 17:49 | machine transcript plus frame descriptions
- Built: Horizon theme tour, an AI-generated hero banner block, a Sidekick-generated block, a code walkthrough.
- Points that are still useful (spoken): generated blocks are saved in `blocks/` as normal files; `{% stylesheet %}` does not render Liquid, so conditionals need a `<style>` tag; stylesheet assets are "only injected once for each section, block, or snippet file"; `visible_if` hides settings conditionally; AI blocks need checking because "when it gets complicated, for example, create an upsell in the cart, then the AI sometimes is not the best".
- Copy: the stylesheet caveat (matches shopify.dev); checking AI blocks by hand.
- Ignore: Horizon-specific structure; Shrine is built differently.

### V6. How I Use Claude to Build Shopify Sections (My Exact Process)
- https://www.youtube.com/watch?v=iVDU0oDNuVE | channel UNKNOWN | approx 23 June 2026 | 5:31 | machine transcript plus frame descriptions
- Built: a "Claude CTA" call-to-action section ("we created this with Claude"), visible in the theme editor's Add section list.
- Workflow shown: compares three routes. (1) Shopify's AI "Generate" in Add section: "still a good method if you need to prompt a section quickly" but "gives you very little control". (2) Prompting Claude chat and pasting the code into a new file in the admin code editor: works but "arduous". (3) Download the theme, put it in a GitHub repo with GitHub Desktop, connect the repo to the store with "Connect from GitHub", open the folder as a Claude Cowork project, and have Claude push to the repo.
- Commands and prompts (spoken): a fine-grained GitHub personal access token with Contents "read and write", scoped to one repo, set to "no expiration"; first Cowork prompt "git remote set-url origin" with the token embedded in the HTTPS URL; section prompt "create a simple call to action section that says we created this with Claude ... push to main theme in GitHub". The presenter credits "WebEx" (spelling as transcribed) for the method.
- What went wrong or is risky on screen: the token is typed into the chat and stored in the git remote URL, with no expiry (the presenter says he will delete it); Claude pushes straight to `main`, which is the branch connected to a store theme, so a push changes that theme immediately. Requirements stated: at least a Claude Pro plan for Cowork, GitHub Desktop.
- Copy: the GitHub integration as the bridge for sessions without Shopify CLI; one token per repo, scoped to Contents only.
- Ignore: no-expiry tokens in a remote URL; pushing to a branch connected to a live theme. Connect only an unpublished theme to the branch Claude pushes to.
- Note: ends with a pitch for the presenter's paid section library (vendor interest).

### V7. Figma to Shopify with Claude Code + MCP AI Shopify Development
- https://www.youtube.com/watch?v=Sgyyn-4xZWo | channel UNKNOWN | approx 7 September 2026 | 5:00 | machine transcript plus frame descriptions
- Built: a countdown announcement bar section from a Figma desktop frame and a Figma mobile frame, added to the header section group, running on a local `theme dev` preview.
- Tools: Claude Code in VS Code, Figma MCP (Claude asked permission to read "the Figma design context"), Shopify AI Toolkit.
- Prompt (spoken, paraphrased): the Figma links for desktop and mobile, "I want to keep the CSS and JS for this section in the same section Liquid file", "add the section in the top of page in header section group".
- What went wrong on screen: the section did not load; the `theme dev` terminal showed "the name is too long in the schema". The presenter fixed the schema name by hand and resaved `header-group.json`. He says "while you are developing you just need to keep an eye on the terminal". Claude then reran Theme Check on the section file.
- Result shown: colours and layout match the Figma frame on desktop and mobile, and the section has settings in the editor.
- Copy: give desktop and mobile frames separately; watch the `theme dev` output, because upload errors show there and not in the chat.
- Ignore: the "five minutes versus 1.5 hours" claim; ends with a pitch for the presenter's paid course.
- Matches F2: the 25-character schema name limit, caught at upload rather than by the agent.

### V8. How to Build Shopify Themes Faster with Claude Code
- https://www.youtube.com/watch?v=rNiw_9OO9ts | channel UNKNOWN | approx 4 January 2026 | 11:15 | machine transcript plus frame descriptions
- Built: no section. Setup: GitHub account, Shopify GitHub connector, Shopify CLI, local preview, git repo connected to the store, Claude Code VS Code extension, `/login`.
- Commands (spoken): `shopify version`, `shopify help`; "shopify theme dev --store" followed by the store's myshopify.com handle; "git init", "git add star", "git commit"; then the GitHub "push an existing repository" commands, SSH preferred over HTTPS.
- Risk on screen: the Shopify GitHub app was given "All repositories" access ("a lot easier for the purposes of this tutorial"). Limit it to the theme repo.
- Presenter's claims: GitHub gives "free theme backups as well as version history", and rollback is "going back to a previous commit"; AI "still makes tons of mistakes and it makes mistakes in weird ways".
- Copy: download the theme into git before any AI edits; preview locally with `theme dev`.

### V9. How to Edit Shopify Theme Using Claude Code [Full Tutorial]
- https://www.youtube.com/watch?v=hh7i8Bs8-JI | channel UNVERIFIED ("Somath" per a search summary) | approx 4 June 2026 | 12:13 | machine transcript plus frame descriptions
- Built: no section. Setup for non-coders: download the Dawn theme, private GitHub repo, VS Code, Claude Code extension, connect the repo to a draft theme.
- Safety advice (spoken): "Claude Code is an LLM and there's a very good chance that it's gonna mess up things ... We create a copy of the theme of the live theme so the live theme doesn't get affected." Also: use it for "small things" or "a completely new section", but with an existing "complicated piece of like sections setup ... don't try to mess with it too much".
- Commands (spoken): "git add .", "git commit -m 'I changed the comment'", "git push origin main"; or ask Claude "can you push this theme to github - use branch main".
- What went wrong on screen: the final `git push` failed with a non-fast-forward error. The presenter said that repo was a different one. Mechanism (inference): when a repo is connected to a theme, Shopify commits admin and editor saves back to the branch, so the local copy falls behind and a push is rejected until you pull. Pull before every session.
- Also shown: the presenter suggests turning on "edit automatically" so Claude stops asking permission (see F13).
- Prompt shown on screen: "can you scan my theme files and tell me 3 things i can do to improve my page speed?"

### V10. Shopify Theme Development Just Changed
- https://www.youtube.com/watch?v=tc5NaxUrOyU | channel UNKNOWN | approx 10 June 2026 | 7:27 | machine transcript plus frame descriptions
- Built: no section. Ran `shopify theme init`, which asks which AI tool you use and writes instructions for it; for Claude it created a `CLAUDE.md` describing the theme structure, with "Learn Shopify API" marked mandatory. The theme generated is Shopify's Skeleton theme.
- Presenter's claims: the CLAUDE.md "is a great way to save tokens"; "You can keep this file in any existing Shopify theme you want to develop." Figma MCP needs "Figma and a premium plan". Claude "cannot generate images", so tell it to use placeholders.
- CONFLICT: the GitHub research found Skeleton's agent instructions describe a theme with "no `sections/` folder, no `{% section %}`/`{% sections %}` tags, no JSON templates, no schema `presets`" ([skeleton-theme AGENTS.md](https://github.com/Shopify/skeleton-theme/blob/main/AGENTS.md)). Copying that file into Shrine would give the agent the wrong architecture. Use section 4 of this briefing instead.
- Copy: designs from screenshots work as references; say which images to use or that placeholders are fine.

### V11. 19 Claude Code Mistakes "Pro" Users Are Still Making
- https://www.youtube.com/watch?v=icM0ewXGvAw | channel UNKNOWN | approx 23 August 2026 | 20:13 | machine transcript plus frame descriptions
- Not Shopify-specific. Points relevant to section work (creator claims, several attributed to Anthropic docs):
  - Prompts should say where to look, what done looks like, and a self-check ("before you finish, verify your answer against ...").
  - "Stop writing 'do not do X'", say what to do instead. UNVERIFIED as stated; the rules in section 4 keep a few "never" lines because the dangerous ones are also enforced by hooks.
  - CLAUDE.md is read at session start; edits mid-session are not picked up until a new session or `/clear`. Consistent with the [memory docs](https://code.claude.com/docs/en/memory) ("loaded at launch").
  - If Claude ignores a CLAUDE.md rule, "the file is probably too long".
  - Subagents get no conversation history, and the built-in Explore and Plan agents skip CLAUDE.md, so restate critical constraints in the subagent prompt. Consistent with the [subagent docs](https://code.claude.com/docs/en/sub-agents).
  - Verification is the top tip: same-prompt check, `/goal`, Stop hooks that "physically block the turn from ending", and an adversarial review agent told to flag only real problems.
- Copy: restate the theme rules inside the `pp-section-qa` subagent prompt; keep CLAUDE.md short.

### Not watched
- How To Build Shopify Themes Faster with Codex CLI, https://www.youtube.com/watch?v=-msIYvPVM9E. The analysis request was blocked by this session's permission check as a credit-spending action; no further analyses were requested after that.
- 11 further candidates are listed in `docs/research-raw/youtube/candidates.md`, unwatched.

### Instagram reels
All four NOT ACCESSIBLE. instagram.com is blocked in this environment; a search for each reel ID found nothing; routing a reel through a third-party importer was denied by the session's permission check. No captions were supplied. Nothing is inferred about their content. Details: `docs/research-raw/reels/README.md`.
- https://www.instagram.com/reel/DcN2nJEu9L2/ NOT ACCESSIBLE
- https://www.instagram.com/reel/DdJ5ynbDxqS/ NOT ACCESSIBLE
- https://www.instagram.com/reel/DdiYr7wOmsE/ NOT ACCESSIBLE
- https://www.instagram.com/reel/DcwkX6OyduT/ NOT ACCESSIBLE

### Section patterns (research question D)
Only what sources show. Shrine already has a matching section or block for most of them (theme inspection).

| Pattern | What sources show | Shrine already has |
|---|---|---|
| Collapsible detail blocks | Accordion content beats tabs for discovery on product pages (EXCERPT, vendor, [byteandbuy](https://byteandbuy.com/blog/100-shopify-pdps-design-patterns-that-drive-3-cvr); figures unverified) | `collapsible-content` section, `collapsible-row` and `product_tabs` blocks |
| Size guide near the size selector | "only 17% of desktop sites and 13% of mobile sites provide sufficient sizing information"; link "should be included near the size selector" (EXCERPT, [Baymard](https://baymard.com/research-articles/apparel-size-information)) | Kiwi app block; Shrine `product_sizing-chart` block |
| Collection filters | Built with Shopify Search & Discovery, per collection; "only work if the underlying product data is consistent" (EXCERPT, official Help Center plus [charleagency](https://www.charleagency.com/articles/shopify-custom-filters/)) | Filters come from Search & Discovery, not a custom section |
| Reviews and customer photos | Photo reviews and review apps with photo support (EXCERPT, vendor; lift figures unverified) | `reviews`, `review-avatars`, `testimonials`, `trustpilot-reviews`, `facebook-testimonials` |
| Story section | Short brand story answering "why us" (EXCERPT, vendor and Shopify blog; stats unsourced) | `image-with-text`, `rich-text`, and the `pp-founder` section on Claude Code V2 |
| Bundles and complete-the-look upsells | "Complete the Look" framing beats generic "You May Also Like" (EXCERPT, vendor); AOV claims unverified | `bundle-deals`, `product_bundle-offer`, `product_complementary`, `product_upsell-block--product-info`, cart upsell blocks |

---

## 9. Source log

Reliability: OFFICIAL, PRACTITIONER, VENDOR, UNVERIFIED. Read: FULL (whole page or file), EXCERPT (search summary or partial), NONE.

### Environment inventory (done first)
- Skills in the repo: humanizer, structural-humanizer, idea-triage, store-cro-audit, temple-product-generator, temple-ref-finder. Account skills: docs, docx, pdf, pptx, xlsx, skill-creator and the creative skills. None are Shopify-theme skills.
- MCP servers connected: Shopify (store admin, read used only; docs search `search_docs_chunks`), GitHub, Figma, Higgsfield (includes YouTube video analysis), Google Drive, Claude Docs, claude-code-remote.
- CLI tools present: node/npx 22, python3, ffmpeg, Playwright (Chromium preinstalled), git, gh, curl. Missing: yt-dlp, whisper / faster-whisper, Shopify CLI. Nothing was installed.
- Evan's YouTube watch stack: the `/watch` skill referenced in `cro-research-prompt.md` (yt-dlp download, ffmpeg frames, local Whisper, `--no-whisper` for captions) and the idea-inbox collector (`idea-inbox/collector/media.py`: yt-dlp, faster-whisper, ffmpeg frames). Neither runs here. Substitute used: Higgsfield `video_analysis_create` (machine transcript plus scene descriptions, no frames). Credit balance before and after all 11 completed analyses: 1111.75 (no charge observed).
- Network: youtube.com, instagram.com, reddit.com, shopify.dev, help.shopify.com, community.shopify.com and many blogs were blocked (EGRESS_BLOCKED). code.claude.com, github.com (git and raw), npm and pypi worked. To allow the blocked sites, change Network access in this cloud environment's settings ([docs](https://code.claude.com/docs/en/cloud-environments#network-access)).

### Store and local files
| Source | Date | Tool | Reliability | Read |
|---|---|---|---|---|
| Live theme `config/settings_schema.json`, `sections/*`, `blocks/*` list, `sections/main-product.liquid`, `blocks/main-product_details.liquid`, `blocks/container--product.liquid` | 2026-10-03 | Shopify connector graphql_query (read only) | OFFICIAL (the store itself) | FULL for the named files |
| `temple-product-generator/theme/README.md`, `docs/decisions.md` (swatch notes) | 2026-10 | Read | LOCAL | FULL / EXCERPT |

### Official Shopify (via Shopify connector docs search unless noted)
| URL | Tool | Read |
|---|---|---|
| https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema | search_docs_chunks | EXCERPT (verbatim chunks) |
| https://shopify.dev/docs/storefronts/themes/architecture/limits | search_docs_chunks | EXCERPT |
| https://shopify.dev/docs/storefronts/themes/architecture/settings/input-settings | search_docs_chunks | EXCERPT |
| https://shopify.dev/docs/storefronts/themes/architecture/settings | search_docs_chunks | EXCERPT |
| https://shopify.dev/docs/storefronts/themes/architecture/blocks (and /theme-blocks/schema, /app-blocks) | search_docs_chunks | EXCERPT |
| https://shopify.dev/docs/api/liquid/tags/content_for , /include | search_docs_chunks | EXCERPT |
| https://shopify.dev/docs/storefronts/themes/tools/liquid-doc | search_docs_chunks | EXCERPT |
| https://shopify.dev/docs/storefronts/themes/architecture/templates/json-templates , /section-groups | search_docs_chunks | EXCERPT |
| https://shopify.dev/docs/storefronts/themes/best-practices/editor/integrate-sections-and-blocks | search_docs_chunks | EXCERPT |
| https://shopify.dev/docs/api/shopify-cli/theme/theme-dev , /theme-push (plus pull, check, share, duplicate, publish) | search_docs_chunks | EXCERPT |
| https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks , /configuration , /migrate | search_docs_chunks | EXCERPT |
| https://shopify.dev/docs/apps/build/ai-toolkit ; https://shopify.dev/changelog/posts/dev-mcp-now-supports-liquid | search_docs_chunks | EXCERPT |
| https://shopify.dev/docs/apps/build/online-store/theme-app-extensions/configuration | search_docs_chunks | EXCERPT |
| https://shopify.dev/docs/storefronts/themes/architecture/settings/dynamic-sources | search_docs_chunks | EXCERPT |
| https://shopify.dev/docs/storefronts/themes/best-practices/performance/use-filter-chains , /use-responsive-images , /never-lazy-load-lcp-image | search_docs_chunks | EXCERPT |
| https://shopify.dev/docs/storefronts/themes/best-practices/javascript-and-stylesheet-tags | search_docs_chunks | EXCERPT |
| https://shopify.dev/docs/storefronts/themes/best-practices/accessibility ; /store/requirements | search_docs_chunks | EXCERPT |
| https://shopify.dev/docs/storefronts/themes/store/success/updates | search_docs_chunks | EXCERPT |
| https://shopify.dev/docs/storefronts/themes/tools/github | search_docs_chunks | EXCERPT |
| https://shopify.dev/docs/storefronts/themes/architecture/blocks/ai-generated-theme-blocks | search_docs_chunks | EXCERPT |
| https://shopify.dev/docs/storefronts/themes/tools/online-editor | search_docs_chunks | EXCERPT |
| help.shopify.com updating themes, generate blocks, theme limits, older versions | WebSearch | EXCERPT (blocked), marked SECONDHAND |
Raw notes: `docs/research-raw/shopify-docs/01` to `11`.

### Official Anthropic (code.claude.com, WebFetch, raw markdown saved)
skills, sub-agents, hooks, hooks-guide, memory, mcp, settings, permissions, permission-modes, checkpointing, best-practices, common-workflows, chrome. All FULL, 2026-10-03, OFFICIAL. Raw: `docs/research-raw/anthropic-docs/`.

### GitHub (git clone / raw.githubusercontent.com, 2026-10-03)
| Repo | Reliability | Read |
|---|---|---|
| https://github.com/Shopify/liquid-skills (last commit 2026-03-18) | OFFICIAL | FULL (skills) |
| https://github.com/Shopify/Shopify-AI-Toolkit (last commit 2026-10-01) | OFFICIAL | FULL (skill, references/liquid.md, validator script) |
| https://www.npmjs.com/package/@shopify/dev-mcp 1.16.0 (2026-09-25); GitHub repo not public | OFFICIAL | FULL (README, dist tool registrations) |
| https://github.com/Shopify/theme-liquid-docs/tree/main/ai (2026-09-23) | OFFICIAL | FULL (claude/CLAUDE.md, cursor rules) |
| https://github.com/Shopify/skeleton-theme | OFFICIAL | FULL (AGENTS.md, .theme-check.yml) |
| https://github.com/Shopify/horizon , https://github.com/Shopify/dawn | OFFICIAL | FULL (file tree, configs) |
| https://github.com/Shopify/theme-tools | OFFICIAL | EXCERPT (check list, configs) |
| https://github.com/Shopify/agent-skills (superseded), https://github.com/Shopify/shopify-plugins | OFFICIAL | EXCERPT |
| https://github.com/EcomExperts-io/Base | PRACTITIONER | FULL (CLAUDE.md, rules, hooks) |
| theoseleve-glitch/volta_web, Ez-flove/shopify-theme-training, AvsarSuvagiyaCelvion/Perfume_Rimzim_New_theme, lucasmeelz/atelier-theme | PRACTITIONER (0 stars) | FULL (settings, hooks) |
| mrvedmutha/bassface-theme-2026, domocarroll/shopify-builds, sarojpunde/shopify-dev-toolkit-claude-plugins, jonathanmoore/kona-theme, mattiadragone/storefront-theme-kit, osea-malibu/ocean-theme | PRACTITIONER | FULL or EXCERPT |
| https://gist.github.com/karimmtarek/3a8a636a05ae1c349ad0bba9d10425f0 | PRACTITIONER | FULL |
| https://github.com/baslefeber/shopify-skills | PRACTITIONER | FULL |
| Shopify/cli#4871 (Nov 2024, older than 12 months), Shopify/themekit#699 (2020, older than 12 months) | OFFICIAL repo, user reports | FULL |
Raw: `docs/research-raw/github/official/`, `docs/research-raw/github/community/`.

### Practitioner and vendor web (WebSearch excerpts unless noted)
letstalkshop.com (3 posts), launchtip.com, get-ryze.ai, adsx.com, fudge.ai (4 pages), claudefa.st, dev.to (3 posts), stargazerstudio.net, capaxe.com, ionlyspeakliquid (possibly older than 12 months), eesel.ai (possibly older than 12 months), neat.digital, commerce-media.info, tokenpost.com, appycodes.com, qeretail.com, nisonco.com, shopify.com/blog/staging-site, fuelthemes.net, craftshift.com, easifyapps.com (3 pages), intercom.help Kiwi (4 pages), shrine.io/pages/theme-updates, shrinetheme.io, baymard.com (2 pages), byteandbuy.com, charleagency.com, studioniza.com, wiserreview.com, branvas.com, firstpier.com, mgroupweb.com, flagship.inc, section.store and app listings, gempages.net, help.fluorescent.co. All EXCERPT, 2026-10-03, PRACTITIONER or VENDOR. Full list with quotes and all 49 queries: `docs/research-raw/web/findings.md`.

### Community forums (WebSearch excerpts; sites blocked)
community.shopify.com threads 631503, 411971, 132813 (older than 12 months), 615944, 621122, 629483, 629768, 324306, 54313 (older than 12 months), 298691, 344578; community.shopify.dev threads 19457, 36456, 38075, 18881, 34943, 8885, 36458. All EXCERPT, UNVERIFIED. Details: `docs/research-raw/reddit/findings.md` and `docs/research-raw/web/findings.md`.

### Reddit
No Reddit page could be read. reddit.com is blocked and the search tool drops reddit.com results. 37 queries run (listed in `docs/research-raw/reddit/findings.md`). One r/ClaudeAI post was found only as an archive copy at JHU AI Voices (EXCERPT).

### YouTube and Instagram
See section 8 and `docs/research-raw/youtube/candidates.md` (29 discovery queries, 22 ranked candidates).

---

## 10. Open gaps and what Evan should check by hand

**Could not verify**
1. Reddit: no posts read. Run the queries in `docs/research-raw/reddit/findings.md` in a normal browser if Reddit evidence matters.
2. One shortlisted video (Codex CLI) was not analysed, and 11 lower-ranked candidates were not watched. All 11 analysed videos are machine transcripts with frame descriptions, not frames.
3. No video frames were captured, so on-screen code and exact typed commands are unknown. Evan's `/watch` skill on the Mac would capture them.
4. All four Instagram reels.
5. Shrine's help centre and update procedure (help.shrinetheme.com, app.shrine.io) were blocked. Shrine's changelog excerpt says 1.9.1 fixed "sticky product information content and sticky header issues that occurred in version 1.9.0" (EXCERPT, shrine.io). Check whether updating to 1.9.1 or later is worth doing before building product-page sections.
6. Whether the AI Toolkit validator runs correctly today (a shopify.dev forum thread title says it shipped without dependencies in 2.0.0; the toolkit is now 2.1.0). On first use, confirm it prints real Theme Check output.
7. Exact JSON output format of `shopify theme check --output json`, needed before writing a Stop hook.
8. Whether Easify hides its add-on products in a way a custom product-listing section would accidentally show (inference from Easify docs, UNVERIFIED).
9. Colour contrast of white text on #F58000 orange and on navy #001A58 (not measured).
10. Prices for Claude plans, Figma MCP access, page builders and section apps (sources conflict or are vendor pages).
11. The live store's actual colour values and which Shrine scheme maps to navy and orange (they live in `config/settings_data.json`, which was deliberately not read).

**Evan should check by hand**
- In the theme editor, open a product page and confirm where the Kiwi size chart and Easify options sit today (app block or app embed). Write it down so QA has a baseline.
- Decide which unpublished theme is the build target. "Claude Code V2" holds the newest homepage work and is not live.
- Before any new section ships, look at its preview link on your own phone.
- After any Shrine update, check that Kiwi and Easify still appear and that every `pp-` section is still on the page.
