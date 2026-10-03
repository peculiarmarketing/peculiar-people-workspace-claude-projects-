# Building custom Shopify theme sections with an AI assistant: briefing

Researched 2026-10-03 for Peculiar People (peculiarpeopleco.com). Second pass the same day, after network access was widened.

**Who should read this.** Any Claude Code or Claude.ai session before it builds, edits or reviews a theme section, block or snippet. The reader is an AI assistant working for a store owner who is not a developer: the owner approves, and the assistant builds, checks and reports.

**Store facts this doc assumes**

- **Theme: Shrine PRO 1.9.0** by Shrine.
  - Read from `config/settings_schema.json` `theme_info` through a read-only Admin API query. There is no full local theme folder.
  - All three store themes report the same version.
  - Shrine's changelog dates Shrine PRO 1.9.0 to **July 9, 2026** and lists it as the latest Pro release ([VENDOR] https://shrine.io/pages/theme-updates, read in full).
  - Shrine is sold on shrine.io, not in the Shopify Theme Store.
- **Live theme: unclear.**
  - On 2026-10-03 the API reported "Claude code original" as MAIN.
  - `temple-product-generator/theme/README.md` says "Claude Code V2" (id 194242150772) went live on 2 Oct.
  - Confirm by hand before any push.
- **Apps that must keep working:** Easify Product Options and Kiwi Size Chart.
  - Both are installed as **app blocks** inside Shrine's product "Details" theme block, directly after the variant picker ([LOCAL] `templates/product.json`).
- **Design tokens:** Arial 16px body, Montserrat headings, black, white, navy #001A58, orange #F58000 buttons.
- **Store size:** about 136 products, Online Store 2.0.

**Labels**

- **[OFFICIAL]:** shopify.dev or Anthropic docs, read in full unless marked.
- **[VENDOR]:** app or theme maker docs.
- **[PRACTITIONER]:** creator, agency or forum post.
- **[VIDEO]:** YouTube transcript (captions only, no frames).
- **[LOCAL]:** this store's own files or this workspace's history.
- **UNVERIFIED:** could not be confirmed.
- **MY PROPOSAL:** my synthesis, not taken from a source.

How the sources were read is in section 9. Raw files are in `docs/research-raw/`.

---

## 1. Executive summary

1. **Never write to the live theme.** Build in a local git copy and preview on a development or unpublished theme.
   - Shopify CLI needs `--allow-live` to push to, or run `theme dev` on, a live theme from a non-interactive session ([OFFICIAL] theme-push, theme-dev). Ban `--allow-live`, `--live`, `--publish` and `theme publish`.
   - The owner publishes from the admin.
   - One creator's demo of Shopify's AI Toolkit edited a live theme with permissions skipped ([VIDEO] ptnWksC9TXY 6:48). This is a real risk, not a theoretical one.
2. **Install Shopify's own tooling before writing Liquid.**
   - Either the AI Toolkit plugin (`claude plugin install shopify-ai-toolkit@claude-plugins-official`) or the Dev MCP server.
   - Optionally, Shopify's `liquid-skills` plugin for Liquid, CSS and accessibility rules ([OFFICIAL] https://shopify.dev/docs/apps/build/ai-toolkit; GitHub Shopify/liquid-skills).
   - The Toolkit's telemetry is on by default and can send code and your last prompt to Shopify. Decide on the opt-out first (section 2).
3. **Validation is necessary but not sufficient.**
   - Shopify's Liquid validation runs Theme Check under the hood ([OFFICIAL] changelog 2025-10-01).
   - Theme Check passes code that still renders wrong: whitespace bugs ([PRACTITIONER] dev.to, Jul 2026), redirects for logged-out users ([PRACTITIONER] monkeyman.agency, May 2026).
   - Always add a visual check: Playwright screenshots of the preview at 375px and 1280px, plus a theme editor test.
4. **Every section must be editable by the owner.**
   - One valid `{% schema %}` with `presets`. Without presets it cannot be added in the editor ([OFFICIAL] json-templates).
   - Every visible word, image, colour and spacing value becomes a setting or block, with readable labels and real defaults.
   - Never rename an existing setting id. That orphans saved values ([VIDEO] uW39GOgc0wo 5:45).
5. **Only add new `pp-` files. Never edit Shrine files or `layout/theme.liquid`.**
   - A vague "add a banner" prompt led Claude to rewrite theme.liquid ([VIDEO] uW39GOgc0wo 0:00).
   - Uploaded themes like Shrine get no Shopify update flow ([PRACTITIONER] Shopify Community 686447, Sep 2026). Custom files must be re-applied by hand after a Shrine ZIP update, so keep them in git.
6. **Keep custom code away from the product form, variant picker and cart.**
   - Kiwi's own docs warn that scripts rebuilding the variant area make the chart "disappear, duplicate, jump position, or trigger script conflicts" ([VENDOR] Kiwi 13256403).
   - AI-written add-to-cart code commonly fails to update the cart drawer ([PRACTITIONER] Community 629483, May 2026; [VIDEO] hExRRN9rJ4o 15:23).
7. **Scope CSS to the section and use the theme's CSS variables.** No inline styles, no external JS libraries, no bare selectors ([OFFICIAL] liquid-skills standards; [VIDEO] uW39GOgc0wo 3:33).
8. **One section per request, from a written spec.**
   - Commit first. Show the diff. Stop if any file outside the spec changed.
   - "Improve this" prompts trigger whole-file rewrites ([VIDEO] uW39GOgc0wo 5:45).
9. **Check what Shrine and the apps already do before building.**
   - Shrine's Details block already accepts size chart, reviews, bundle offer, complementary products, collapsible rows and Custom Liquid ([LOCAL]).
   - Filters, reviews and bundles are better handled by apps or built-in features (section 8.3).
10. **Report with evidence or not at all.**
    - Name the theme id pushed to, the files, the check output and the screenshots, and list what could not be checked.
    - Do not move this theme into Shopify's new Canvas editor. Canvas does not support app blocks or app embeds, and Canvas themes get no updates ([OFFICIAL] merchant changelog, Oct 1 2026).

---

## 2. Recommended toolchain

"Non-dev?" means: can the owner do the setup without developer help?

| Tool | What it does | Setup for a non-developer | Cost | Source |
|---|---|---|---|---|
| **Shopify CLI** (`@shopify/cli`) | Pull and push theme files. `theme dev` runs a hot-reload preview on a development theme; development themes are "deleted from the store after seven days of inactivity". `theme check` lints. Needs Node 22.12+ and Git 2.28+. | **Developer-level once.** Terminal install `npm install -g @shopify/cli@latest`, then log in to the store. After that the assistant runs it. | Free | [OFFICIAL] https://shopify.dev/docs/api/shopify-cli ; /docs/storefronts/themes/tools/cli |
| **Theme Check** (inside the CLI) | Lints Liquid and schema: ValidSchema, ValidSchemaName, ValidSettingsKey, UnknownFilter, UndefinedObject, LiquidHTMLSyntaxError, StaticStylesheetAndJavascriptTags, ParserBlockingScript, ImgWidthAndHeight, RemoteAsset, ValidScopedCSSClass. Exit code 1 on any error. | The assistant runs it. Add a `.theme-check.yml` that sets `ValidSchema: severity: error`: the checks table lists it as a Warning, and `push --strict` lets warnings through. | Free | [OFFICIAL] /docs/storefronts/themes/tools/theme-check/checks ; /configuration |
| **Shopify AI Toolkit** (Claude Code plugin) | One `shopify` skill (Shopify merged the separate skills on 2026-09-25) that searches docs, validates code and can run store operations. The README states: "Validation is mandatory: never return generated code you have not run through this command". | **Easy:** `claude plugin install shopify-ai-toolkit@claude-plugins-official`. **Telemetry is on by default**. The GitHub README says the payload includes "the validated code when present" and, on Claude Code, "the user's most recent message verbatim (truncated to 2000 chars)". The shopify.dev page does not mention telemetry. Opt out: `mkdir -p ~/.config/shopify-ai-toolkit && touch ~/.config/shopify-ai-toolkit/opt-out`. Its store-write path ("store execute") has no dry run or undo ([VIDEO] j58kLqMPPZE 6:42; Fudge guide). | Free | [OFFICIAL] https://shopify.dev/docs/apps/build/ai-toolkit ; github.com/Shopify/Shopify-AI-Toolkit README; changelog 2026-04-09 and 2026-09-25 |
| **Shopify Dev MCP** (`@shopify/dev-mcp` 1.16.0, 2026-09-25) | Tools `learn_shopify_api`, `search_docs_chunks`, `validate`, `validate_theme`. Runs locally, no auth, Node 18+. Liquid validation is Theme Check. | **Easy:** `claude mcp add --transport stdio shopify-dev-mcp -- npx -y @shopify/dev-mcp@latest`. Same telemetry opt-out. Use this or the Toolkit. | Free | [OFFICIAL] ai-toolkit page; npm package |
| **Shopify liquid-skills** (Claude Code plugin) | Skills `shopify-liquid-themes`, `liquid-theme-standards` (BEM, design tokens, "No external dependencies"), `liquid-theme-a11y`. Separate from the Toolkit and still published. | **Easy:** `/plugin marketplace add Shopify/liquid-skills`, then `/plugin install liquid-skills@liquid-skills`. | Free | [OFFICIAL] github.com/Shopify/liquid-skills README (re-checked 2026-10-03) |
| **Playwright MCP** | The assistant opens the preview URL, sets phone and desktop widths, screenshots, and reads the console. The README notes coding agents "might benefit from using the CLI+SKILLS (microsoft/playwright-cli) instead". | **Easy:** `claude mcp add playwright npx @playwright/mcp@latest`. Chromium is already in this cloud environment. | Free | [OFFICIAL] github.com/microsoft/playwright-mcp ; [VIDEO] NjOqPbUecC4 (loop pattern, Aug 2025, OLDER THAN 12 MONTHS) |
| **Git + GitHub integration** | Version history. The integration syncs a branch with a theme both ways: "Files are updated in GitHub whenever changes are made to a connected theme. This can't be disabled." | **Medium.** Connect the repo to a **draft** theme, never the published one. Two creators published the connected theme, which makes every push live ([VIDEO] 0tEkfZ4vtcs 6:02, rNiw_9OO9ts 6:40). | Free | [OFFICIAL] /docs/storefronts/themes/tools/github |
| **Figma MCP** | Reads a Figma frame as reference. Output is "a structured React + Tailwind representation" that must be translated to Liquid. | **Easy:** `claude plugin install figma@claude-plugins-official`. Optional. | Free tier | [OFFICIAL] github.com/figma/mcp-server-guide |
| **Shopify Sidekick (theme editor)** | Generates AI theme blocks in sections that accept `@theme` blocks. Can also customize themes by chat. | **Non-developer friendly.** Whether it is offered on Shrine is UNVERIFIED. Shopify's changelog says block generation covers "Theme Store themes" (Dec 10, 2025), and Shrine is not one. Forum reports: hashed CSS classes that change on edit, mobile clipping, extra CSS weight (Community 615944, 599412, 2026). One test scored Sidekick theme work "2 out of 10" (appbrew.com, Sep 2026). | Included | [OFFICIAL] /docs/storefronts/themes/architecture/blocks/ai-generated-theme-blocks ; changelog.shopify.com |
| **Section apps** (Section Store and others) | Pre-built sections. | **Non-developer friendly.** Lock-in: one vendor's uninstall doc says sections and your edits to them are removed (EXCERPT, docs.appsections.com). | Mostly $0 to $9 per section (EXCERPT) | apps.shopify.com/section-factory (EXCERPT) |

**Design skills from the reels.** All are community projects, not Shopify-specific.

- **Emil Kowalski skills** (`npx skills@latest add emilkowalski/skills`) and **Impeccable** (`npx impeccable install`): framework-neutral design critique, partly usable.
- **Taste Skill:** leans on the React stack.
- **Motion.dev, Bklit UI, Kokonut UI (the "Coconut UI" in the reel) and Manus:** React libraries or a hosted builder. Not usable in Liquid sections.

Source: research-raw/github-anthropic/notes.md.

---

## 3. Failure modes

Rule numbers (R1 to R33) refer to the CLAUDE.md block in section 4.

| # | Failure | Symptom | Why it happens | Prevention rule or check | Sources |
|---|---|---|---|---|---|
| F1 | **Hallucinated or wrong Liquid** | Error on save, blank output, a filter that does nothing. Claude "references properties that don't actually exist on the objects" and uses deprecated syntax. "A nil object prints nothing, so the page renders blank." | Mixed-up template languages, training data older than Shopify changes, invented names. Liquid quirks: no ternaries, no parentheses in conditions. Shopify's parser has been stricter since Jan 2026. | Validate every file with the Toolkit or Dev MCP and `shopify theme check`. Look up any object or filter you are unsure of. Use `render`, never `include`. **R5 R6 R7** | [VIDEO] uW39GOgc0wo 2:14; [PRACTITIONER] fudge.ai debug guide (Jul 2026); [OFFICIAL] theme-check checks; changelog 2026-01-13 (strict parsing); liquid-skills |
| F2 | **Wrong file type** | Claude returns a full HTML page, or code "not meant for Shopify". It will "most definitely break things". | The target format (a section file with schema) was never stated. | The spec names the file type. The CLAUDE.md says sections live in `sections/pp-*.liquid` with a schema. **R8** | [PRACTITIONER] Community 631503 (Jun 2026); [VIDEO] YXamW3c_J-s 3:14 |
| F3 | **Schema missing, invalid or unusable** | The section is missing from "Add section", or "Invalid JSON in tag 'schema'", or settings are not editable. Labels that just repeat the setting ID, lorem ipsum defaults, no info text. | No `presets`. Trailing commas or `//` comments. More than one schema tag. Settings put inside `blocks`. A block without `name`. A range without a numeric `default`. A richtext default not wrapped in `<p>` or `<ul>`. | One top-level `{% schema %}`, valid JSON, name of 25 characters or less, `presets` with `name`. Range: numeric min, max and default. Human labels and real defaults. Theme Check with ValidSchema set to error. Add the section in the editor before reporting. **R8 R9 R10** | [OFFICIAL] section-schema ("Each section can have only a single {% schema %} tag"), json-templates ("Section files must define presets..."), input-settings, limits (25-character names); [PRACTITIONER] Community 205043 (2023, ChatGPT section with no presets; OLDER THAN 12 MONTHS), 169273 (2022, "name is required"; OLDER), 329958 (2024; OLDER); [VIDEO] uW39GOgc0wo 4:58 |
| F4 | **Hardcoded content** | The owner cannot change text, icons or colours without code. Examples: trust badge icons with no setting; an upsell with "hardcoded" values. | It is faster for the model to inline values. | Every visible string, image, icon, link, colour and spacing value is a setting or block, with the current value as the default. **R11 R12** | [VIDEO] CGjPQmC6ttY 6:21, hExRRN9rJ4o 14:51 and 16:27; [OFFICIAL] liquid-skills standards ("never hardcode colors, spacing, or fonts"); [PRACTITIONER] EcomExperts-io/Base CLAUDE.md |
| F5 | **Editing the live theme, no rollback** | Customers see a broken store. A ChatGPT paste wiped a collection page and "version history not working". A Toolkit prompt "applied the update to my live theme". | Admin code editor edits, or pushes to MAIN. Code editor history "restores one file at a time... does not bring back files that were deleted, there is no history at all for the assets folder". | Local git copy plus a development or unpublished theme only. Commit before every change. Ban `--allow-live`, `--live`, `--publish` and `theme publish`. Use `--nodelete` and `--only` on pushes. **R1 R2 R3 R4** | [OFFICIAL] theme-push ("-a, --allow-live... Required in non-interactive environments when targeting the live theme"); [VIDEO] ptnWksC9TXY 6:48; [PRACTITIONER] Community 417178 (May 2025), 667662 (Aug 2026); monkeyman.agency ("A merchant prompting an AI agent directly against a live theme will, within a week, push a broken section"); [LOCAL] theme/README.md (`--nodelete` note) |
| F6 | **Overwriting the owner's editor settings** | Settings the owner changed in the theme editor silently revert after a push. | `shopify theme push` "overwrites JSON templates and settings_data.json too, so if anyone has touched the theme editor since you pulled, you'll quietly revert their work". With GitHub sync, the code editor version overwrites GitHub with no conflict alert. | Pull right before editing. Never push `config/settings_data.json`. Push `templates/*.json` only if the spec names it and right after a fresh pull. Never push while the theme editor is open on that theme. **R4 R13** | [PRACTITIONER] Community 667662 (Aug 2026); appycodes.com (Sep 2026: never "Rewrite config/settings_data.json"); [OFFICIAL] GitHub integration page; [LOCAL] decisions.md 18 Sep 2026 ("whichever saves last wins") |
| F7 | **Touching core files or rewriting working code** | A banner request rewrote theme.liquid, the file every page depends on. "Improve this product section" renamed CSS classes, schema IDs and JS, which broke styles elsewhere and orphaned saved settings. The agent also "changed a lot of stuff just like for formatting" in base CSS. | Broad prompts, and the model regenerating whole files. | Never edit layout files or Shrine files; create new `pp-` files. Never rename existing setting ids, block types or classes. One change per request. Review `git diff`. **R25 R27 R28** | [VIDEO] uW39GOgc0wo 0:00, 0:33, 5:45; hExRRN9rJ4o 9:50 |
| F8 | **CSS leaking, inline styles, stacking** | A new section restyles sliders elsewhere. A sticky AI header ends up under page content (fix: `z-index: 3`). Inline styles "can't update styles from the theme editor". | Bare selectors. Inline `style=""`. `{% stylesheet %}` CSS is bundled once per file, not once per instance. No z-index plan. | Every selector under the section's `pp-` root class. Per-instance values in an inline `<style>` scoped with `#shopify-section-{{ section.id }}` (MY PROPOSAL, built from the official facts quoted here). No inline style attributes. **R14 R15 R31** | [OFFICIAL] stylesheet tags page ("If you need instance-specific CSS, then use an inline <style> tag"); section object (IDs "dynamically generated"); [PRACTITIONER] Community 166189 (2022, OLDER), 621122 (May 2026); [VIDEO] uW39GOgc0wo 3:33 |
| F9 | **Ignoring theme tokens** | The section uses its own fonts, colours or button style and looks bolted on. | The model picks its own defaults. | Use Shrine's CSS variables. Fixed brand colours only as `color` setting defaults. **R16** | [LOCAL] layout/theme.liquid variables; [OFFICIAL] liquid-skills |
| F10 | **JS conflicts with the theme and apps** | Easify options or the Kiwi chart vanish, duplicate or jump. Add to cart works but the cart count and drawer do not update until refresh. The cart drawer does not re-render. | Custom JS on the product form or variant area. AI "tries to dispatch an update event, but it does not pass proper data into it". | No custom JS on the product form, variant picker, buy buttons, cart drawer or inside `main-product_details`. Sections that sell products link to the product or use Shrine's own blocks; they do not build their own add-to-cart. JS goes in a custom element in a `pp-` asset with `defer` and no libraries. **R17 R18 R19 R29** | [VENDOR] Kiwi 13256403 (Jun 2026): "the chart may disappear, duplicate, jump position, or trigger script conflicts"; Easify options-dont-show ("If apps use the same resources, it often causes conflicts"); [PRACTITIONER] Community 629483 (May 2026); [VIDEO] hExRRN9rJ4o 15:23; tXkpsim6sfI 4:53 (overlay after add to bag) |
| F11 | **App blocks lost** | Easify or Kiwi missing on some products, or after a template or theme change. | A template without the app block. A section without `@app`. A theme switch: Easify "will result in the app being disabled on the new theme"; Kiwi "needs to be re-enabled for the new theme". | Never remove or move the two app blocks. Every new product template includes both. Product-area sections accept `{"type": "@app"}` (no `limit` on @app). After a theme duplicate or switch, check App embeds and both blocks. **R18 R20** | [OFFICIAL] theme-app-extensions/configuration ("Sections that support and render blocks of type @app"), app-blocks ("Blocks of type @app don't accept the limit parameter"); [VENDOR] Easify app-activation (Jul 2026); Kiwi 10290927, 15165730 (Sep 2026) |
| F12 | **Mobile and editor-vs-live mismatch** | Fine in the editor, misaligned or clipped on the live site. "You can't see it in 'Edit theme' because the site width is limited there." Mobile images "a little small". | Desktop-first CSS and fixed widths. The editor iframe is not a phone. | Mobile-first. Screenshot the preview URL at 375px and 1280px. Touch targets: 24x24 minimum, and **44x44 on primary controls** (now official). The owner checks once on a real iPhone. **R21 R22** | [OFFICIAL] store/requirements (24x24); accessibility best practices ("Touch targets on primary controls and links need to be at least 44 by 44 pixels"); [PRACTITIONER] Community 580094 (Dec 2025), 615944 (May 2026); [VIDEO] tXkpsim6sfI 3:50, NjOqPbUecC4 9:10 |
| F13 | **Performance** | Layout shift, a slow hero image, blocking scripts. One AI block "added dozens of videos playing in parallel". | `<img>` without dimensions, a lazy-loaded first image, scripts without `defer`, huge media. | `image_url \| image_tag` with `widths` and `sizes`. Do not set `loading` in the first three sections ("Don't set the loading attribute when relying on this default"). `fetchpriority: 'high'` on a section-1 hero. Scripts get `defer`. No remote assets. **R23** | [OFFICIAL] never-lazy-load-lcp-image; theme-check; store/requirements (Lighthouse 60); [PRACTITIONER] Community 599412 (Mar 2026) |
| F14 | **Accessibility regressions** | Missing alt text, unlabeled buttons, animation ignoring reduced motion, low contrast, H1 used in the wrong place. | The model omits alt and ARIA and uses divs as buttons. "AI assistant does not look at your page as a whole". | Alt from a setting. Real `<button>` and `<a>`. Reduced motion respected. Contrast 4.5:1 for body text, 3:1 for large text and icons. **Measured: #F58000 vs white = 2.63:1**, so orange text on white and white text on orange both fail even 3:1. Black on orange = 7.97:1. Navy on white = 16.3:1. **R24** | [OFFICIAL] store/requirements ("4.5:1 for main body content... 3:1" for large text and icons); liquid-skills a11y; [PRACTITIONER] Community 599412; [LOCAL] contrast computed with the WCAG formula |
| F15 | **Lost on theme update; name collisions** | Custom work disappears after an update. Edits to shipped files are discarded. | Shopify keeps "the theme developer's version" when both sides changed a file. Shrine is uploaded, and "Uploaded themes get no updates. Theme Store installs only." So a Shrine update is a new ZIP and custom files must be copied across by hand. | Only new `pp-` files. Never edit Shrine files or `config/settings_schema.json` ("those collide with new theme settings"). Keep every `pp-` file in git. If a Shrine file must change, log it in `theme/CUSTOMIZATIONS.md`. **R25** | [PRACTITIONER] ed.codes (Apr 2026); Community 686447 (Sep 2026), 590065 (Feb 2026); [VENDOR] Shrine FAQ ("1 year of support... including updates") |
| F16 | **Silent failure** | The assistant says done but nothing changed, or data was skipped with no error. Examples: the wrong file was edited; CDN cache; a stray word "liquid" printed by an AI block. | Pushing to a different theme than the preview. A section with no preset. Liquid that renders nothing on missing data. [LOCAL] example: the temple marquee drops a temple with no art "without any error". | The report names the theme id, files, preview URL and screenshot evidence. Data-driven sections show a visible editor placeholder (`request.design_mode`) and list skipped items. **R26** | [PRACTITIONER] Community 1362 (2018, OLDER), 582682 (Jan 2026), 590610 (Mar 2026); [LOCAL] theme/README.md |
| F17 | **Side effects outside the theme** | During a footer build, Claude created 18+ pages, menus and collections on the store. Product data was mass-edited in one prompt. | Broad connector or Toolkit permissions, plus "always allow" or skip-permission modes. | Theme work never creates or edits products, pages, menus, collections, files or discounts. Use least-privilege scopes (`read_themes`, `write_themes` for theme work). Never run with permission prompts skipped. **R30 R32** | [VIDEO] CGjPQmC6ttY 7:52, 10:28; ptnWksC9TXY 0:00; uW39GOgc0wo 1:38; 62Zc8DUVjbg 7:04 |
| F18 | **Fragile targeting of generated markup** | Custom CSS aimed at AI block classes or Kiwi containers breaks later. "Hashed class suffixes like that regenerate when the block is edited". | Selectors tied to auto-generated IDs or classes. Kiwi warns against selectors like `#ProductForm-20669957144825`. | Never target hashed or numeric IDs or classes. Use stable `pp-` classes or documented app selectors. **R31** | [PRACTITIONER] Community 615944, 583083 (2026); [VENDOR] Kiwi 13256240 (May 2026) |
| F19 | **Images the assistant cannot place** | Section images are missing. "This is one thing that Claude can't do". | The CLI cannot upload to Content > Files. | The spec lists images. The owner uploads them in Content > Files or picks them in the editor. Sections use `image_picker` with a visible placeholder. **R11** | [VIDEO] tXkpsim6sfI 2:45; companion repo AGENTS.md ("You cannot upload Files with the CLI") |

**Conflicts between sources**

1. **Does validation make AI output safe?**
   - Vendor blogs present the Dev MCP and Theme Check as the fix.
   - monkeyman.agency (May 2026): even with theme-check in CI and human review, guardrails "still catch about one in eight changes". In other words, about one change in eight still has a problem that only review catches.
   - dev.to (Jul 2026): "shopify theme check passed clean" on a size chart that rendered "as one long, mangled line".
   - Shopify says its Liquid validator is Theme Check.
   - Conclusion: lint plus visual check plus human review.
2. **Can the Toolkit change themes?**
   - 62Zc8DUVjbg (11:28) says it is "not built for... changes directly to the theme layer".
   - ptnWksC9TXY (6:48) and j58kLqMPPZE (4:23) both changed themes with it.
   - The first claim is wrong.
3. **Can Sidekick write Liquid?**
   - fudge.ai (Mar 2026): "Sidekick cannot generate, edit, or debug Liquid code."
   - Shopify's changelog and Community threads show Sidekick generating theme blocks with code.
   - fudge sells a competing product.
4. **Section style: theme-matched or self-contained?**
   - uW39GOgc0wo: point Claude at the theme's CSS and match it.
   - tXkpsim6sfI's AGENTS.md: no theme classes or variables, everything self-contained, for portability across themes.
   - For one store on one theme, use the theme's variables (R16) and scoped classes. Self-contained is right only for sections sold to many stores.
5. **Permissions.**
   - uW39GOgc0wo: least privilege.
   - CGjPQmC6ttY: "always allow". hh7i8Bs8-JI: auto-edit. 62Zc8DUVjbg: "generally just say yes". ptnWksC9TXY: skip permissions.
   - This doc sides with least privilege.
6. **Kiwi placement on Shrine.**
   - Kiwi's help center has a "Shrine PRO" article (Aug 2026) recommending selector `#size-inject-anchor`.
   - It labels the theme "Fuel Themes (v1.2.0 to v1.6.1)", and that anchor does **not** exist in this store's Shrine PRO 1.9.0 ([LOCAL] read-only search).
   - The store already uses the Kiwi app block. Leave it.
7. **ValidSchema severity.** The checks table says Warning; its own page says error. Set it to error in `.theme-check.yml`.
8. **Corrections to this doc's first pass.** These came from search summaries that the full pages did not support. Removed or corrected:
   - "reversed code" (Community 205043)
   - the seotldr "restore" quote
   - a Sidekick "not theme-aware" quote (Community 580094)
   - Baymard "27%" and "43%"
   - the Kiwi and Easify listing numbers
   - "Shrine PRO 1.9.0 dated 2025"

---

## 4. CLAUDE.md rules block for a Shopify theme repo

Paste into the theme repo's `CLAUDE.md`. Anthropic's docs: CLAUDE.md is "context, not enforced configuration". The hooks in section 5 enforce the critical rules.

```markdown
# Shopify theme rules (Peculiar People, Shrine PRO 1.9.0)

## Safety
- R1. Never push to or develop on the live theme. Never pass --allow-live, --live or --publish, and never run `shopify theme publish` or `shopify theme delete`. (F5)
- R2. Before any push, run `shopify theme list`, confirm the target theme id is not the [live] one, and write the id in your report. (F5, F16)
- R3. Commit to git before every change and after every working step. Never rewrite history. (F5, F7)
- R4. Pull config/settings_data.json and templates/*.json from the target theme right before editing. Push only with --nodelete and one --only flag per file. (F5, F6)
- R13. Never push config/settings_data.json. Push a templates/*.json file only when the spec names it, right after pulling it fresh, with the owner's theme editor closed. (F6)
- R30. Never create or edit products, pages, menus, collections, files, discounts or metafield data during theme work. If the spec seems to need it, stop and ask. (F17)
- R32. Never run with permission prompts skipped or set to always allow for Shopify write tools. Read each permission request. (F17)

## Correct Liquid
- R5. Run the Shopify validator (AI Toolkit `shopify` skill or Dev MCP validate_theme) on every Liquid file you create or change. Never return code that has not passed it. (F1)
- R6. Run `shopify theme check` and fix every error. Push with --strict. Keep ValidSchema set to severity error in .theme-check.yml. (F1, F3)
- R7. If you are not certain a Liquid object, filter, tag or setting type exists, look it up in the docs tool. Never guess. Use render, never include. (F1)

## Editable sections
- R8. A section is a file in sections/pp-<name>.liquid. It has exactly one top-level {% schema %} with valid JSON, a "name" of 25 characters or fewer, and a "presets" entry with a "name". Never deliver a full HTML page. (F2, F3)
- R9. Range settings have numeric min, max and default. Richtext defaults use <p> or <ul> as top-level tags. Every block type has a "name". Setting ids are unique. Labels are plain words, not ids. Defaults are real text, never lorem ipsum. (F3)
- R10. After pushing to the preview theme, add the section in the theme editor and confirm every setting changes the output. (F3, F16)
- R11. Every visible string, image, icon, link, colour and spacing value is a setting or a block with the current value as default. Images use image_picker with a visible placeholder; list any image the owner must upload. (F4, F19)
- R12. Repeating items are blocks with max_blocks set. (F4)
- R28. Never rename or remove an existing setting id, block type, CSS class or file name in a section already in use. Add new ones instead. (F7)

## Styling
- R14. Name every new file and CSS class with the pp- prefix (BEM: pp-faq__item). Every selector starts with the section root class. Never style Shrine's classes or bare elements. (F8, F15)
- R15. Per-instance values go in an inline <style> scoped to #shopify-section-{{ section.id }}. Shared CSS goes in assets/pp-<name>.css or a {% stylesheet %} tag with no Liquid inside. No style="" attributes. (F8)
- R16. Use the theme's CSS variables: --font-heading-family, --font-body-family, --color-base-text, --color-base-background-1, --color-base-accent-1, --buttons-radius, --page-width, --spacing-sections-desktop, --spacing-sections-mobile. Fixed brand colours are only #000000, #FFFFFF, #001A58, #F58000, and only as defaults of color settings. (F9)
- R31. Never target auto-generated ids or hashed classes (AI block classes, #ProductForm-123, block ids). Give anything sticky or overlaid an explicit z-index and check it against the header. (F8, F18)

## Apps and JavaScript
- R17. Never add or change JavaScript that touches the product form, variant picker, buy buttons, cart drawer, product-info, or anything inside the main-product_details block. (F10)
- R18. Never remove, move or rename the Easify Product Options and Kiwi Size Chart app blocks in templates/product.json. Every new product template includes both. (F10, F11)
- R19. JavaScript lives in a custom element in assets/pp-<name>.js, loaded with defer, guarded so it can load twice. No globals, no external libraries or CDNs. (F10, F13)
- R20. A custom section meant for the product area accepts {"type": "@app"} blocks (with no limit). (F11)
- R29. Custom sections never implement their own add-to-cart. Link to the product, or use Shrine's own product blocks. (F10)

## Quality
- R21. Write CSS mobile-first. No fixed pixel widths on containers. Touch targets at least 24 by 24 CSS pixels, and 44 by 44 on primary controls and links. (F12)
- R22. Screenshot the preview URL at 375px and 1280px and look at both before reporting. Check the browser console. (F12, F16)
- R23. Images use image_url | image_tag with widths and sizes. Do not set loading on images in the first three sections. Every script has defer. (F13)
- R24. Every image has alt text from a setting. Interactive elements are <button> or <a>. Animations stop under prefers-reduced-motion. Body text contrast at least 4.5:1, large text and icons 3:1. Never orange #F58000 text on white or white text on orange (2.63:1). (F14)

## Scope and updates
- R25. Never edit layout/theme.liquid, config/settings_schema.json or any Shrine file. If one must change, stop and ask, then log the change and reason in theme/CUSTOMIZATIONS.md. (F7, F15)
- R26. Never say done without evidence: theme id, files pushed, preview URL, check output, screenshots. Say first if any data was skipped or any check could not run. (F16)
- R27. One section per request. Change only files the spec names. Show git diff --stat before pushing; if any other file changed, stop and ask. (F7)
- R33. Never move this theme into Shopify Canvas: Canvas drops app blocks and app embeds (Easify, Kiwi) and stops theme updates.
- No em dashes in anything the owner reads.
```

---

## 5. Proposed Claude Code skills, subagent and hooks

**File formats** ([OFFICIAL] https://code.claude.com/docs/en/skills, /sub-agents, /hooks):
- **Skills:** `.claude/skills/<name>/SKILL.md` with `name` and `description` frontmatter.
- **Subagents:** `.claude/agents/<name>.md`; `name` and `description` are required.
- **Hooks:** go in `.claude/settings.json`.
  - Exit code 2 in a PreToolUse hook blocks the call.
  - A PostToolUse hook "Shows stderr to Claude; the tool already ran".

### 5.1 Skill: `shopify-section-builder`

**MY PROPOSAL.** Steps 3, 7 and 8 are ADAPTED FROM the lookbook repo's AGENTS.md (https://github.com/BeauchampAndrew/shopify-lookbook-gallery: "validate the schema JSON", `node --check` the JS, "push to an unpublished theme first"). Step 6 is ADAPTED FROM the Maelify blog (read the existing sections first).

```markdown
---
name: shopify-section-builder
description: Build or change one custom Shopify theme section for the Peculiar People store (Shrine PRO). Use when Evan asks for a new section, block, homepage band, product page module, or a change to a pp- section. Works from the section spec, validates, previews on an unpublished theme, and reports with screenshots. Never publishes.
---
1. Read the theme repo CLAUDE.md and docs/shopify-custom-sections-research.md sections 3 and 4.
2. Get a filled spec (section 6 template). If a required field is empty, list the gaps and stop.
3. Check whether Shrine already has a section or block for this (search sections/ and blocks/ by name, and the Shrine changelog). If yes, say so and stop for a decision.
4. Run `shopify theme list`. Note the live theme id and the preview theme id. Commit the current state.
5. Pull fresh templates/*.json and config/settings_data.json from the preview theme.
6. Read two existing pp- sections to match their structure, then write sections/pp-<name>.liquid (plus assets/pp-<name>.css/.js if needed), following R8 to R31.
7. Validate: the Shopify validator on each file, `node --check` on any JS, `shopify theme check`. Fix and repeat until clean.
8. Show `git diff --stat`. Confirm only spec files changed.
9. Push: `shopify theme push --theme <preview id> --nodelete --strict --only <each file>`.
10. Run the QA checklist (section 7) with Playwright at 375 and 1280.
11. Report in the QA report format. Publishing stays with Evan.
```

### 5.2 Subagent: `theme-reviewer`

**ADAPTED FROM** the EcomExperts-io/Base reviewer agent (https://github.com/EcomExperts-io/Base): "You **report**. You do not edit files."

```markdown
---
name: theme-reviewer
description: Independent read-only review of a Shopify theme change before it is pushed. Use after the section builder finishes and before reporting to Evan.
tools: Read, Grep, Glob, Bash
---
You report. You do not edit files.
Check the diff against CLAUDE.md rules R1 to R33. For each rule: PASS, FAIL (file:line, what), or NOT CHECKED (why).
Look specifically for: bare or hashed-class selectors, style="" attributes, hardcoded text or colours, missing presets,
renamed setting ids, scripts without defer, any change to the product form, variant picker, cart drawer,
main-product_details or the Easify/Kiwi app blocks, any non-pp- file in the diff, layout/theme.liquid or
settings_schema.json changes, and any command with --allow-live, --live, --publish, theme publish or theme delete.
```

### 5.3 Hooks (`.claude/settings.json`)

**MY PROPOSAL.** The pattern is ADAPTED FROM EcomExperts-io/Base: a PostToolUse gate on `Edit|Write|MultiEdit`, and a Stop gate that runs Theme Check.

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

- **`block-live-push.sh`:** reads the tool input JSON from stdin. If the command contains `shopify theme` together with `--allow-live`, `--live`, `--publish`, `publish` or `delete`, it prints the reason to stderr and exits 2.
- **`theme-check-changed.sh`:** runs `shopify theme check --fail-level error` and prints the errors to stderr.

Both scripts are untested proposals. Test them on a scratch repo first.

### 5.4 Install rather than write

- **Shopify's tooling:** the AI Toolkit `shopify` skill and `liquid-skills` ([OFFICIAL], links in section 2).
- **Existing workspace skill:** `store-cro-audit`, to check a section on the real storefront after it goes live ([LOCAL]).

---

## 6. Section spec template

Fill one spec per section. The builder stops if any field marked * is empty.

**Why this shape:** creators found that vague prompts ("improve this", "add a banner") caused rewrites. Specific prompts with screenshots and constraints worked ([VIDEO] uW39GOgc0wo 2:53 and 5:45, YXamW3c_J-s, 62Zc8DUVjbg 4:53).

```markdown
# Section spec: <name>

* Purpose (one sentence, what the shopper should do or feel):
* Page(s) and position (e.g. product page, after Description; homepage, after hero):
* Does Shrine already have something close? (section/block name, or "checked, no"):
* File type: new section sections/pp-<name>.liquid (default) / theme block / other:
* Content the owner edits (each becomes a setting):
  - text: <label> | default: <real wording>
  - image: <label> | alt default: <text> | who uploads it: <owner>
  - link: <label> | default: <url>
* Repeating items (each becomes a block; max count):
* Desktop layout (describe, attach screenshot or mockup):
* Mobile layout at 375px (stacking order, what hides):
* Colours: theme variables only, or which of black / white / navy #001A58 / orange #F58000 (no orange text on white):
* Fonts: theme heading (Montserrat) and body (Arial 16px) unless stated:
- Motion: none / subtle (must stop under reduced motion):
- Data source (static settings, product metafield, metaobject, collection):
- Behaviour when data is missing:
* Must not affect: product form, variant picker, cart drawer, Easify options, Kiwi size chart, existing pp- sections, <other>:
* Done when (observable checks, e.g. "owner can change heading in editor", "one column at 375px"):
* Target theme for preview (name and id; never the live one):
- Reference sites or screenshots (inspiration only, do not copy another brand's design):
- Out of scope:
```

---

## 7. Pre-publish QA checklist

The assistant reports each item as PASS, FAIL or NOT CHECKED, with evidence. Publishing stays with the owner.

**Code**
1. Shopify validator on each changed file. Paste a summary.
2. `shopify theme check`: zero errors. Paste the summary line.
3. `node --check` on each changed JS file.
4. `git diff --stat`: only spec files. Specifically not:
   - Shrine files
   - `layout/theme.liquid`
   - `config/settings_data.json`
   - `config/settings_schema.json`
5. Schema review:
   - one schema tag, with `presets`
   - every owner-editable value is a setting
   - labels are readable and defaults are real
   - no existing setting id renamed
   - name is 25 characters or fewer

**Push**
6. `shopify theme list`: report the target id and role (not live), the exact push command (with `--nodelete`, `--only`, `--strict`) and the preview URL.

**Theme editor**
7. The section can be added from "Add section". Change each setting and see the output change. Remove and re-add it with no errors.

**Visual** (Playwright, using the preview URL)
8. Screenshots at 375px and 1280px, attached. Note anything overlapping, cut off or misaligned. No horizontal scroll at 375px.
9. Fonts and colours match the theme. Only the four brand hex values appear. Sticky or overlaid elements sit correctly against the header.
10. Touch targets: 24px minimum, 44px for primary controls.

**Apps and product page** (when the change touches product pages or templates)
11. Changing size and colour updates the image and price.
12. Easify fields appear, accept input, and their values reach the cart line item.
13. The Kiwi size chart opens, and does not duplicate or move after a variant change.
14. Add to cart updates the cart count and drawer without a page refresh.
15. Browser console shows no new errors. List any found.

**Store data**
16. Confirm no products, pages, menus, collections, files or discounts were created or changed.

**Accessibility and performance**
17. Every image has alt text. Keyboard tab order reaches every control, with visible focus.
18. Under emulated `prefers-reduced-motion: reduce`, animations stop.
19. If available, Lighthouse mobile on the preview page: report performance and accessibility. Theme Store minimums are 60 and 90.

**Report format**
- First line: "Ready for your review on <theme name> (not live)" or "Not ready: <reason>".
- Then the item list, the screenshots, and "What I could not check".

---

## 8. Reel and video findings, plus section patterns

### 8.1 Instagram reels

All three reels were NOT ACCESSIBLE, on both passes.
- **First pass:** proxy blocked.
- **Second pass:** HTTP 200, but a 640 KB JavaScript shell with no caption data, on the page and the `/embed/captioned/` URL (research-raw/instagram/fetch-attempts.md).
- **What was used instead:** the transcripts you pasted (research-raw/instagram/reel-transcripts-from-owner.md). No frames were taken. The reel 3 screenshot is your own.

**Reel 1, DdJ5ynbDxqS.** Owner transcript only.
- **What it says:** add "Emile Kowalski design and impeccable skills", then the "taste skill", then "Figma MCP and Playwright" so Claude can "design, build, and test and screenshot".
- **Tools:** all exist (community skills; Figma and Playwright MCP are official).
- **Copy:** the Playwright screenshot loop (R22).
- **Ignore:** "Claude just killed web designers" and "let it handle the rest". Every Shopify video in 8.2 needed human steering.
- **Date:** unknown.

**Reel 2, DdiYr7wOmsE.** Owner transcript only.
- **What it says:** Motion.dev, "BKLit.ui", "Coconut UI" (Kokonut UI) and Manus.io, which "build flawless backend-powered sites".
- **Verdict:** React libraries and a hosted builder. Not usable in Liquid sections, and against Shopify's no-external-dependency rule.
- **Copy:** nothing.
- **Date:** unknown.

**Reel 3, DcwkX6OyduT** (adam_ha_yes, "20 UX Laws to tell Claude for better Design"). Owner transcript plus your screenshot.
- **What it says:** UX laws such as Hick, Fitts, Jakob and the Doherty threshold, as plain rules: "Reduce choices per screen", "Make targets large", "Highlight the primary action".
- **Notes:** the screen lists Postel's law twice. The promised md file was not found online.
- **Copy:** use as design criteria in specs. For example: one primary action per section, large targets (R21).
- **Ignore:** running all 20 as a checklist on every section.
- **Date:** unknown.

### 8.2 YouTube videos

**How they were fetched.** yt-dlp in a scratchpad venv, YouTube captions plus metadata, 17 videos.

**Coverage for every entry: FULL TRANSCRIPT, NO FRAMES.**
- Video download was refused by the session's safety check, so on-screen code, settings and typed commands were never seen.
- Quotes are caption text and may be misheard.
- Transcripts are in research-raw/youtube/<id>-transcript.md. Companion pages are in companion-<id>.md.

**Not fetched:**
- **Blocked by YouTube's bot check:** WnrzGqRFuzk ("This MCP Turns Claude Code Into a Premium Shopify Designer"), Sgyyn-4xZWo ("Figma to Shopify with Claude Code + MCP") and dHa5MQKhnQk (Playwright).
- **Found but not watched:** iVDU0oDNuVE, x2pRavsHdls, Mk6cv0f_nnc and others in research-raw/youtube/first-pass-blocked/.

**V1. Claude Code for Shopify: 10 Mistakes That Will Break Your Store**
- **Source:** Will Misback, 2026-04-15, 8:00. https://www.youtube.com/watch?v=uW39GOgc0wo
- **Built:** nothing. It is a list of 10 mistakes and fixes.
- **Tools:** Claude Code, CLAUDE.md, git, Shopify Admin MCP scopes, Theme Check.
- **Said aloud:**
  - 0:00: the bad prompt was "Add a promotional banner to the homepage." Claude "went straight into the theme.liquid and rewrote the entire layout file."
  - 0:33: his rule: "Do not edit theme.liquid and do not touch the layout files... Create a new section file or a new snippet instead."
  - 1:05: "I run git checkout dot and I'm back exactly where I started" [caption].
  - 1:38: on scopes, "just read themes and write themes".
  - 2:43: "run Shopify theme check after Claude Code changes before you push them".
- **Went wrong:**
  - 2:14: properties that do not exist on objects.
  - 3:33: inline styles.
  - 4:23: an experiment tangled across 6 files on main.
  - 4:58: ID-as-label schema with lorem ipsum defaults.
  - 5:45: "improve this" renamed classes and schema IDs, breaking CSS and orphaning settings.
- **Unverified:** the good-prompt example at 2:53 was shown only on screen. His CLAUDE.md template is behind an email gate and was not fetched.
- **Copy:** all ten fixes. They map to R3, R5, R6, R14, R15, R25, R27, R28 and R32.
- **Ignore:** "10x" claims.

**V2. How to Build Shopify Themes Faster with Claude Code**
- **Source:** Will Misback, 2026-01-03, 11:15. https://www.youtube.com/watch?v=rNiw_9OO9ts
- **Built:** setup only: GitHub, Shopify CLI preview, GitHub-connected theme, Claude Code in VS Code.
- **Said aloud:** "Shopify theme dev" with a store flag (3:19), then git init, add and commit (4:26) [caption, may be misheard].
- **Went wrong:** nothing much. He hit "credit balance is too low" before logging in.
- **Risk:** at 6:40 he suggests publishing the GitHub-connected theme, which makes every push live.
- **Honest caveat:** "still makes tons of mistakes and it makes mistakes in weird ways" (10:32).
- **Copy:** `shopify theme dev` preview; a private repo as history.
- **Ignore:** publishing the connected theme.

**V3. Claude Code + Shopify: I Built a Custom Theme Section in Minutes (Free Code)**
- **Source:** Andrew Beauchamp, 2026-09-25, 8:01, creator captions. https://www.youtube.com/watch?v=tXkpsim6sfI
- **Built:** a shoppable lookbook section (grid of looks, popup, quick add, deep links) on a dev store.
- **Repo:** https://github.com/BeauchampAndrew/shopify-lookbook-gallery. Its schema has 48 settings, a "look" block and presets.
- **Prompts:** none spoken (PARAPHRASED: he gave Claude the inspiration URL).
- **Went wrong:**
  - 2:45: images had to be uploaded by hand.
  - 3:50: mobile images too small.
  - 4:20: full quick view dropped because it "can break" across themes.
  - 4:53: "funky overlay" after add to bag.
- **Copy:** the repo's AGENTS.md:
  - prefix everything
  - expose every string as a setting
  - guard custom element definitions
  - validate schema JSON
  - `node --check`
  - theme check
  - "Ask the human before pushing to the live theme (--allow-live)"
- **Ignore:** its no-theme-variables rule (that is for cross-theme portability; see conflict 4). Do not copy another brand's design.

**V4. how to make custom liquid sections on shopify using claude**
- **Source:** uzi prints, 2026-06-07, 6:39. https://www.youtube.com/watch?v=YXamW3c_J-s
- **Built:** a "scientifically backed" callout with a study link, copied from Claude chat into a Custom Liquid block.
- **Said aloud:**
  - 3:14: "Please make sure the copy is short and contains a button to take them to a new tab that opens the study..." [caption].
  - 3:46: a circled-screenshot change request.
- **Went wrong:**
  - 3:14: Claude sent "the wrong type of coding that wasn't meant for Shopify".
  - 4:18 to 4:49: every change was a full re-paste.
  - His companion docs contradict each other: one says no schema (Custom Liquid), the other demands a full schema section.
- **Unverified:** student revenue claims, and the health claim.
- **Copy:** give Claude screenshots of the real site.
- **Ignore:** the Custom Liquid copy-paste workflow (no settings, no history) and the health-claim framing.

**V5. I Used A Screenshot and Claude Code to Build A New Shopify Theme**
- **Source:** BitBranding, 2026-05-21, 20:05, creator captions. https://www.youtube.com/watch?v=CGjPQmC6ttY
- **Built:** a trust badge section, a homepage rebuilt from a screenshot, and a copied footer. Used the Claude desktop app with the official Shopify connector, and Claude Design.
- **Said aloud:**
  - 3:09: "I'm going to all just hit always allow".
  - 4:47: "on the horizon theme on the homepage at a three column section with shipping returns and secure payment options with an icon for each column".
- **Went wrong:**
  - 4:47: the connector refused to write to the live theme.
  - 6:21: icons were not editable.
  - 8:53: "very very basic sections".
  - 10:28: 18+ pages and menus created on the store.
  - 14:13: the design handoff errored.
  - 15:16: "allow like 20 times".
  - 15:47: everything was "dumped into one single section".
- **Copy:** the connector's live-theme block; mock up before building; ask for editable icons.
- **Ignore:** always-allow, store data side effects, and cloning a competitor's site (which he himself warns against at 4:14).

**V6. Build Shopify Themes in MINUTES -[Claude Code & MCP]**
- **Source:** WebSensePro, 2026-03-12, 11:35. https://www.youtube.com/watch?v=0tEkfZ4vtcs
- **Built:** setup only (GitHub, Claude Code, Dev MCP).
- **Commands from the description:** `git init` / `git add .` / `git commit -m "Initial commit"`.
- **Went wrong:**
  - 6:02: he published the GitHub-connected theme.
  - The companion blog's MCP command, `npx @shopify/mcp-cli@latest init`, does not match Shopify's official `@shopify/dev-mcp@latest`.
- **Copy:** install the Dev MCP.
- **Ignore:** the blog command; publishing the connected theme.

**V7. How to Edit Shopify Theme Using Claude Code [Full Tutorial]**
- **Source:** CheckoutClass, 2026-06-03, 12:14. https://www.youtube.com/watch?v=hh7i8Bs8-JI
- **Built:** setup plus one read-only question: "Can you scan my theme files? Tell me three things to improve page speed." (8:08).
- **Went wrong:** 10:48, the push failed because of a git remote mismatch.
- **Advice:**
  - 8:40: "only use it for like small things... or if it's like a completely new section".
  - 9:12: turn on auto edit.
- **Copy:** use AI for new sections, not for rewriting complex code; work on a copy of the theme.
- **Ignore:** auto edit, and the "API key required" claim (contradicted by V2, V6 and V8).

**V8. How to Connect Claude AI to Your Shopify Store (No More Copy-Pasting Code)**
- **Source:** WEBEXP, 2026-04-22, 6:08. https://www.youtube.com/watch?v=qlB9JppKGQw
- **Built:** a "Hello, world" announcement bar on a GitHub-connected **draft** theme, using Claude Cowork and GitHub Desktop.
- **Command from the description:** `git remote set-url origin https://YOUR_TOKEN@github.com/YOUR_USERNAME/YOUR_REPO.git`.
- **Went wrong:** nothing on camera.
- **Notes:**
  - Claude wired the section into the header group: an edit to existing theme data.
  - He pushes straight to main.
  - The token is stored in plain text in .git/config.
- **Copy:** a fine-grained token with an expiry, used on a draft theme.
- **Ignore:** a token embedded in the URL; pushing to main.

**V9. New Shopify AI Toolkit: Claude Code Setup + Demo (April 2026)**
- **Source:** Jonathan Lewell, 2026-04-11, 7:45. https://www.youtube.com/watch?v=ptnWksC9TXY
- **Built:** a product list, revenue and LTV queries, and a homepage title change on the live theme.
- **Said aloud:**
  - 0:00: Claude launched with "dangerously skip permissions".
  - 6:09: "edit the uh home page uh title. Change it to... Science-Backed Supplements for real results" [caption].
- **Went wrong:** 6:48, "applied the update to my live theme" with no confirmation narrated.
- **Copy:** nothing from the process. This video is the evidence for R1 and R32.
- **Ignore:** the April install flow (now outdated; see section 2).

**V10. Claude Code + Shopify AI Toolkit: Zero to Hero Tutorial | Maelify**
- **Source:** Maelify, 2026-04-14, 8:18, creator captions. https://www.youtube.com/watch?v=j58kLqMPPZE
- **Built:** a "Latest Videos" homepage section on a **dev theme** from one prompt, plus a blog post.
- **Said aloud:**
  - 3:17: "the new section called latest videos. Show a thumbnail, link it to my most recent YouTube video. Use the scheme number five because that's how my theme's already set up" [caption].
  - 2:45: "there's no undo on production".
  - 6:42: store execute "writes to your shop... there is no undo".
  - 7:06: his rules: use a dev store, save prompts as skills, and re-read the prompt before pressing enter.
- **How Claude worked:** it read the existing sections "schema by schema" before writing (3:51).
- **Companion blog:** push only the changed files with `--only` and `--nodelete`; run `shopify theme check --path . --fail-level error`; use colour scheme settings.
- **Unverified:**
  - "16 skills": now merged into one skill.
  - "no API keys": his own blog uses an Admin token.
- **Copy:** the dev theme, read-existing-first, colour schemes, presets, prompts saved as skills.

**V11. Shopify AI Toolkit: Run Your Entire Store With Claude Code! (Setup + Use Cases)**
- **Source:** Ryan AI SEO Tips, 2026-04-11, 15:31. https://www.youtube.com/watch?v=62Zc8DUVjbg
- **Built:** admin data changes on a test store (alt text, a discount, SEO fields, a reorder list). No theme work.
- **Said aloud:**
  - 4:53: avoid broad prompts like "Optimize my products for SEO"; if you use one, add "Confirm with me before making any specific change".
  - 7:04: "generally just say yes" to permission prompts.
- **Wrong claim:** 11:28, that the Toolkit cannot change themes. Contradicted by V9 and V10.
- **Copy:** narrow prompts with a confirm step.
- **Ignore:** "say yes"; the theme claim; the LinkGPT pitch.

**V12. Shopify AI Toolkit: Claude Code Setup Tutorial (2026)**
- **Source:** Fudge, 2026-04-14, 3:12. https://www.youtube.com/watch?v=CCMCy-xGRkk
- **Built:** install plus a verification question ("how many products").
- **Said aloud:** check the Node and CLI versions first; verify with a question you know the answer to; editing touches "your live actual store, so things can go wrong" (2:48).
- **Companion guide** (updated Sep 2026):
  - the current install command
  - telemetry sends your code by default
  - "push themes as unpublished"
  - store operations have no undo
- **Ignore:** the Fudge product pitch.

**V13. Build with AI with full dev MCP support (official Shopify)**
- **Source:** Shopify, 2025-12-10, 2:49, creator captions. https://www.youtube.com/watch?v=25Bc6-4qti8
- **Built:** a checkout UI extension in Cursor, then moved its content into a metaobject so the merchant can configure it. Not about theme sections.
- **Said aloud:** "Help me create a metaobject declaratively. Store the image URL, the heading, and the list items." (1:06). The agent "pulls in the relevant docs, and then it validates the output" (0:30).
- **Copy:** the pattern of moving hardcoded content into merchant-editable data.
- **Ignore:** "production-ready" marketing.

**V14. How to use AI as a SHOPIFY DEVELOPER in 2026 (Cursor + Shopify Dev MCP)**
- **Source:** Bosidev, 2025-04-05, 22:27. **OLDER THAN 12 MONTHS.** https://www.youtube.com/watch?v=hExRRN9rJ4o
- **Built:** a shop-the-look section, announcement bar icons, a shipping info block and a cart upsell on a test theme.
- **Said aloud:**
  - 9:50: "can you make the icon rendering the same as in the other cases in the theme".
  - 15:55: "Card drawer does not rerender. We have to reload. Can you fix that?" [caption].
- **Went wrong:**
  - 6:35: buttons did nothing.
  - 9:50: unrelated CSS reformatting.
  - 14:51: no editor settings, wrong data source.
  - 15:23: no cart re-render.
  - 16:27: hardcoded values, cropped image, duplicate add.
- **His tips:** short prompts; restart a conversation that is not converging; always check the output; read the docs.
- **Copy:** this failure list (F4, F7, F10).
- **Ignore:** Cursor specifics; the old two-tool MCP.

**V15. Claude Code Now Has Eyes | Playwright MCP Integration**
- **Source:** Eric Tech, 2025-08-25, 13:04. **OLDER THAN 12 MONTHS**, not Shopify. https://www.youtube.com/watch?v=NjOqPbUecC4
- **Built:** a screenshot verification loop with a CLAUDE.md "visual development" section and a design-review subagent.
- **Said aloud:** the checklist covers mobile 375px and tablet 768px (5:22). A mobile sidebar "collapsed into one cluster" (9:10) and was caught only by screenshots.
- **Copy:** the loop, pointed at the preview theme URL, never the live site (my inference). This is R22.

**V16. How to use AI to create custom Shopify theme blocks**
- **Source:** Digismoothie, 2025-06-13, 2:14. **OLDER THAN 12 MONTHS.** https://www.youtube.com/watch?v=pNCx-1F5oIs
- **Built:** a UGC and reviews block via Sidekick on Dawn. The prompt was not read aloud.
- **Said aloud:** Sidekick expands your prompt for review before generating (1:06).
- **Unverified:** "works with any theme".
- **Copy:** Sidekick is a no-code option for small blocks, if it is offered on Shrine.

**V17. How to Use Claude to Build and Run a Shopify Store**
- **Source:** Learn with Shopify (official), 2026-07-13, 7:03. https://www.youtube.com/watch?v=Ih5RapM8XKw
- **Built:** a store from a screenshot in Claude chat; connected the Shopify connector; rewrote descriptions; ran pricing analysis. No theme code safety content.
- **Said aloud:** the connector "requests extensive access to your store, so make sure you are comfortable with that" (4:08). "Don't forget to review everything before publishing" (5:10).
- **Copy:** read permissions before granting them.

**Recurring advice across videos**
- Work on a dev, draft or unpublished theme: V3, V5, V7, V8, V10, V12.
- Have Claude read existing theme patterns first: V10, V14.
- Narrow prompts, one change at a time: V1, V11, V14.
- New sections are where AI does well; rewrites of existing code are where it breaks: V1, V7.
- Make everything editable: V1, V3, V5, V13, V14.
- Verify visually: V15. No Shopify video used an automated screenshot loop; all checked by hand.

**Gap in all 17 videos.** None mentions pulling before pushing, or that a push can overwrite the owner's theme editor changes. That warning comes from Shopify Community 667662.

### 8.3 Section patterns similar stores add (question D)

This lists only what the sources show. Baymard pages were read in full; their dates are given. "Already in Shrine?" comes from the [LOCAL] read of the Details block schema and the Shrine changelog.

| Pattern | What sources show | Already in Shrine? | Best route |
|---|---|---|---|
| Collapsible detail blocks | Baymard (published 2018, updated Jul 8 2026): horizontal tabs are "still used by 29% of sites". Better options are "Expanded Sections" or "Vertically Collapsed Sections". "On desktop, the 'Expanded Sections' layout should be considered." | Yes: `collapsible-row` blocks (4 in use) and the `collapsible-content` section | Built-in. Keep key fit and fabric facts visible. |
| Collection filters | Baymard (Nov 2023, OLDER THAN 12 MONTHS): "61% of sites... don't promote filters at all". Apparel size filter (Jun 2024, OLDER): "39% of participants... found out on the product page that their size was in fact not available". The 90% size-first finding came from "the one test site that did this (Levi's)". | Theme filters via Shopify Search & Discovery | The free app plus theme settings. Not a custom section. |
| Reviews and customer photos | Baymard (Aug 2020, OLDER): "34% of e-commerce sites don't allow users to upload an image along with their review"; "up to 95% of users" seek reviews. Vendor uplift numbers have no primary data (UNVERIFIED). | `reviews`, `review-avatars`, `rating-stars` blocks | A review app with an app block. |
| Size guide embed | Baymard (Jul 2022, OLDER): "83% of desktop apparel sites, and 87% of mobile apparel sites, fail to provide sufficient sizing information". "If this link isn't adjacent to size selectors many users will overlook it entirely." Give inches and centimetres. | The Kiwi app block is right after the variant picker. Shrine also has a `product_sizing-chart` block. | Keep Kiwi where it is. Do not build a second chart. |
| Brand story | No quantified evidence found. | `pp-founder` exists [LOCAL] | Existing section. |
| Bundles, upsells, frequently bought together | Baymard (Jan 2021, OLDER): "52% of desktop sites... present cross-sells in the cart... that are either completely irrelevant or based only on what other customers bought". Suggested label: "'Complete the Look' for coordinating apparel". AOV lift claims are vendor-only (UNVERIFIED). | `product_bundle-offer`, `product_complementary`, `product_upsell-block--product-info`, `cart_product-upsells` blocks | Built-in blocks plus Search & Discovery complementary products. AI-written cart code is a known failure (F10). |

**Shrine release notes worth checking before building** ([VENDOR] theme-updates):
- **Pro 1.9.0** added "Swatch pills", "SEO improvements and h tag settings to Heading block" and infinite load on collections.
- **Pro 1.8.0** added a "Sticky CTA" section and a "Bestseller badge" block.

**Conclusion.** The patterns in question D are mostly covered by Shrine or by apps. Custom sections are worth building for brand-specific content no app offers, like the temple marquee and garment anatomy.

**When to use which option.** MY PROPOSAL, built from the [OFFICIAL] quotes.

| Option | Use when | Can a non-developer run it? |
|---|---|---|
| Built-in Shrine section or block | It already exists | Yes |
| App with app block | Needs data or logic (reviews, bundles, options). App blocks "don't edit theme code" and are removed cleanly on uninstall. | Yes |
| Custom `pp-` section | Brand-specific content no app gives | No: the assistant builds, the owner reviews |
| Metafields or metaobjects as dynamic sources | Same section, different content per product. "Dynamic sources aren't available for general theme settings." | The owner edits data once it is set up; the setup is developer-level |
| Custom Liquid block | A tiny snippet | Risky: no settings, no validation, copy-paste edits (V4) |
| Section app | A generic section, fast | Yes, but locked in on uninstall |

---

## 9. Source log

Full per-source logs are in research-raw/*/notes.md and the pages/ folders.

### Read depth by source type

| Source type | How fetched | Depth |
|---|---|---|
| shopify.dev (50 pages) | curl, `.md` endpoint | FULL |
| Shopify changelogs | curl | FULL |
| Anthropic docs | WebFetch summarizer; memory page saved | Mostly FULL |
| GitHub | raw download | FULL or head |
| Shopify Community (40+ threads) | Discourse JSON | FULL, with real dates |
| Practitioner blogs | curl | FULL where listed |
| Vendors (Easify, Kiwi, Shrine, App Store) | curl | FULL |
| Baymard | curl | FULL |
| YouTube | yt-dlp captions | FULL transcript, NO FRAMES |
| Instagram | curl | NOT ACCESSIBLE |
| Reddit | curl | NOT ACCESSIBLE |
| help.shopify.com | curl | NOT ACCESSIBLE |

### Official
| Source | Date | Depth |
|---|---|---|
| shopify.dev: section-schema, json-templates, limits, sections, blocks (app-blocks, theme-blocks, schema), input-settings, javascript-and-stylesheet-tags, performance (index, never-lazy-load-lcp-image, section rendering API), accessibility, store/requirements, api/liquid (image_tag, section, stylesheet), shopify-cli (index, theme-push, theme-dev), tools/cli, theme-check (checks, valid-schema, valid-scoped-css-class, static-stylesheet-and-javascript-tags, configuration), tools/github, version-control, apps/build/ai-toolkit, ai-generated-theme-blocks, theme-app-extensions (+ configuration), strict-liquid-migration | undated (current) | FULL, saved in research-raw/official-docs/pages/ |
| shopify.dev changelog: Dev MCP supports Liquid | 2025-10-01 (OLDER THAN 12 MONTHS) | FULL |
| shopify.dev changelog: AI Toolkit launch | 2026-04-09 | FULL |
| shopify.dev changelog: strict Liquid parsing | 2026-01-13 | FULL |
| shopify.dev changelog: GitHub commits name the editor | 2026-08-26 | FULL |
| shopify.dev changelog: skills consolidated | 2026-09-25 | FULL |
| changelog.shopify.com: AI blocks for Theme Store themes | 2025-12-10 | FULL |
| changelog.shopify.com: Sidekick theme customize | 2025-12-10 | FULL |
| changelog.shopify.com: Shopify Magic blocks | 2025-05-21 (OLDER) | FULL |
| changelog.shopify.com: Canvas | 2026-10-01 | FULL |
| changelog.shopify.com: Sidekick mobile editor | 2026-06-17 | FULL |
| help.shopify.com | n/a | NOT ACCESSIBLE (403); earlier search summaries only, marked EXCERPT |
| github.com/Shopify/Shopify-AI-Toolkit README, skills | updated 2026-10 | FULL |
| github.com/Shopify/liquid-skills README, SKILL.md files | created 2026-03-13, re-checked 2026-10-03 | FULL or head |
| github.com/Shopify/theme-liquid-docs ai/claude/CLAUDE.md; Shopify/theme-tools; Shopify/dawn .theme-check.yml | 2026 | partial or FULL |
| npm @shopify/dev-mcp 1.16.0 | 2026-09-25 | FULL |
| code.claude.com docs: skills, sub-agents, hooks, memory, mcp | current | SUMMARIZED-FULL (memory FULL) |
| github.com/microsoft/playwright-mcp; github.com/figma/mcp-server-guide | 2026-10 | searched or partial |

### YouTube: 17 videos, FULL TRANSCRIPT, NO FRAMES
uW39GOgc0wo, rNiw_9OO9ts, tXkpsim6sfI, YXamW3c_J-s, CGjPQmC6ttY, 0tEkfZ4vtcs, hh7i8Bs8-JI, qlB9JppKGQw, ptnWksC9TXY, j58kLqMPPZE, 62Zc8DUVjbg, CCMCy-xGRkk, 25Bc6-4qti8 (Shopify), hExRRN9rJ4o (OLDER), NjOqPbUecC4 (OLDER), pNCx-1F5oIs (OLDER), Ih5RapM8XKw (Shopify). Dates and links are in 8.2.

Not fetched: WnrzGqRFuzk, Sgyyn-4xZWo, dHa5MQKhnQk (YouTube bot check).

Companion pages read:
- the lookbook repo README and AGENTS.md
- the Maelify blog plus its starter CLAUDE.md
- the Fudge guide (Sep 2026)
- the WebSensePro blog
- the uzi prints prompt docs
- willmisback.com: email-gated, title only

### Vendor
| Source | Date | Depth |
|---|---|---|
| easifyapps.com/docs: options-dont-show | 2024-01 | FULL |
| easifyapps.com/docs: app-activation | modified 2026-07-23 | FULL |
| easifyapps.com/docs: reposition-option-set-on-product-page | 2024-08 | FULL |
| apps.shopify.com Easify listing: developer "Easify", 4.9 (3,104), launched 2023-04-20 | current | FULL |
| intercom.help/kiwi-sizing-chart articles 10290927, 13256240, 10291102, 13256403, 13342679, 13342634, 13768426, 15165730, 11564460, 10290960, 16520899 (Shrine PRO) | 2025-12 to 2026-09 | FULL |
| apps.shopify.com/kiwi-sizing: developer "Staytuned", 4.7 (1,226), $7.99 / $14.99 / $26.99 per month, launched 2018-03-05 | current | FULL |
| shrine.io: theme-updates, faq, features, legal, pricing blog post (2025-05-09) | 2026 | FULL |
| app.shrine.io help center | n/a | NOT ACCESSIBLE (login app) |
| baymard.com: avoid-horizontal-tabs | 2018, updated 2026-07-08 | FULL |
| baymard.com: apparel-size-information | 2022 | FULL |
| baymard.com: allow-reviewers-to-upload-images | 2020 | FULL |
| baymard.com: promoting-product-filters | 2023 | FULL |
| baymard.com: apparel size filter | 2024 | FULL |
| baymard.com: product-recommendations-cart | 2021 | FULL |

### Practitioner
| Source | Date | Depth |
|---|---|---|
| Shopify Community 2026: 621122, 614173, 686447, 667662, 631503, 676367, 615944, 629483, 599412, 585614, 583083, 590065, 590610, 582682, 615219, 668092, 653757, 600137, 667049 | 2026 | FULL |
| Shopify Community 2025: 580094, 577864, 415152, 417178, 417074, 422282, 567471 | 2025 | FULL |
| Shopify Community older: 166189, 205043, 169273, 329958, 1362, 316747 | 2018 to 2024 (OLDER) | FULL |
| monkeyman.agency | 2026-05-26 | FULL |
| seotldr.substack.com | 2026-03-04 | FULL |
| ed.codes | 2026-04-14 | FULL |
| dev.to/iamrobindhiman | 2026-07-16 | FULL |
| adsx.com | 2026-06 | FULL |
| fudge.ai: debug guide | 2026-07-06 | FULL |
| fudge.ai: Sidekick limitations | 2026-03-09 | FULL |
| appbrew.com | 2026-09-15 | FULL |
| appycodes.com | 2026-09-14 | FULL |
| github.com/EcomExperts-io/Base (CLAUDE.md, settings.json, reviewer agent) | 2026-10 | FULL or head |
| github.com/BeauchampAndrew/shopify-lookbook-gallery | 2026-09 | FULL |
| letstalkshop.com | n/a | NOT ACCESSIBLE (429) |
| dominikatracy.com | n/a | NOT ACCESSIBLE (captcha) |
| Reddit (r/shopify, r/ShopifyeCommerce, r/ClaudeAI, r/ClaudeCode, r/vibecoding, r/webdev) | n/a | NOT ACCESSIBLE (Reddit 403, login wall) |
| Instagram reels DdJ5ynbDxqS, DdiYr7wOmsE, DcwkX6OyduT | n/a | NOT ACCESSIBLE; owner transcripts used |

### Local
| Source | Depth |
|---|---|
| Store themes via Admin GraphQL (read only): theme_info, templates/product.json, sections/main-product, blocks/main-product_details, blocks/custom-liquid, blocks/product_*, snippets/product-variant-*, layout/theme.liquid | FULL (research-raw/01-theme-observations.md, 00-environment-inventory.md) |
| temple-product-generator/theme/README.md, sections/pp-*.liquid, docs/decisions.md (18 Sep 2026) | FULL / relevant parts |

---

## 10. Open gaps and what the owner should check by hand

**Not researched**
1. **No video frames.** On-screen code, settings and typed commands in the 17 videos were never seen; downloading video was refused by the session's safety check. To see them, run the youtube-to-agent stack (/watch) on the Mac. Start with uW39GOgc0wo, tXkpsim6sfI and j58kLqMPPZE.
2. **Three videos unfetched** (YouTube bot check): WnrzGqRFuzk, Sgyyn-4xZWo, dHa5MQKhnQk.
3. **Reddit unread.** Reddit refuses this server. First-hand failure reports from Reddit are missing. Shopify Community threads partly fill the gap.
4. **help.shopify.com unread.** Its pages on theme updates, version history and Sidekick block generation remain search-summary only.

**Check by hand**
5. **Which theme is live?** The API says "Claude code original"; the repo README says "Claude Code V2". Confirm in Online Store > Themes.
6. **Shrine licence and update period.** Shrine includes "1 year of support... including updates". Check the purchase date and that the licence key is valid. Search results show unofficial copies of Shrine PRO for sale.
7. **How a Shrine ZIP update treats custom `pp-` files.** No Shrine page explains this, and the Shrine help center needs a login. Ask Shrine support, or test on a duplicate theme.
8. **Is Sidekick block generation offered on Shrine?** Open the theme editor, Add block, and look for Generate.
9. **Kiwi on Shrine.** Kiwi's Shrine PRO article (v1.2.0 to v1.6.1, "Fuel Themes") recommends `#size-inject-anchor`, which 1.9.0 does not have. The current app block works, so change nothing unless the chart misbehaves.
10. **Easify and Kiwi together.** No source tests them side by side. After any product page change, test both on a phone.

**Decisions for Evan**
11. **AI Toolkit telemetry.** It is on by default and can send code and your last prompt to Shopify. Decide on the opt-out before installing.
12. **Orange buttons fail contrast.** White on #F58000 is 2.63:1, below Shopify's 4.5:1 for text and 3:1 for large text. Black labels pass at 7.97:1.

**Not yet tested**
13. **The hook scripts in 5.3.** They are untested proposals.
