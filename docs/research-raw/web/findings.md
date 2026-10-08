# Web research: AI-built custom Shopify sections (practitioner, agency, community, app docs)

Compiled 2026-10-03 by a research subagent; saved by the main session because the subagent was not allowed to write report files. Content is the subagent's report, lightly condensed (queries list kept in full).

## How to read this file
- FULL = page fetched and read directly. EXCERPT = WebFetch was blocked by the container egress proxy, so the text comes from the search engine's result summary. Treat EXCERPT text as a close paraphrase, not a verified verbatim quote.
- Blocked for WebFetch: letstalkshop.com, askphill.com, adsx.com, commerce-media.info, neat.digital, dev.to, community.shopify.dev, fudge.ai, intercom.help (Kiwi docs), easifyapps.com, help.shrinetheme.com, shrine.io, baymard.com, plus shopify.dev, reddit, youtube, community.shopify.com. Only github.com and gist.github.com fetched.
- OLD = dated more than 12 months before 2026-10-03.

## A. Tooling

### A1. Shopify AI Toolkit (official, April 2026)
- https://github.com/Shopify/Shopify-AI-Toolkit | FULL | official. README: "Search Shopify's documentation and API schemas without leaving your editor"; "Validate GraphQL queries, Liquid templates, and UI extensions against Shopify's schemas". Claude Code install: `claude plugin install shopify-ai-toolkit@claude-plugins-official`. Telemetry on by default, sends "search queries, validation results, and code snippets"; opt out via `~/.config/shopify-ai-toolkit/opt-out` or `OPT_OUT_INSTRUMENTATION`. Also includes store management (real store operations) via CLI.
- https://claudefa.st/blog/tools/mcp-extensions/shopify-ai-toolkit (and others) | EXCERPT | practitioner. "On April 9, 2026, Shopify open-sourced the Shopify AI Toolkit ... under MIT license." Blog install: "/plugin marketplace add Shopify/shopify-ai-toolkit and /plugin install shopify-plugin@shopify-plugin." CONFLICT A1 with README; README is authoritative.
- https://community.shopify.dev/t/ai-toolkit-liquid-validator-still-ships-without-its-dependencies-in-2-0-0-github-11/38075 | EXCERPT (title only). "AI Toolkit Liquid validator still ships without its dependencies in 2.0.0 (GitHub #11)". CONFLICT A2: confirm the validator actually runs; keep Theme Check as an independent check.

### A2. Shopify Dev MCP
- https://www.npmjs.com/package/@shopify/dev-mcp | EXCERPT | official. "lets AI agents search Shopify's documentation and API schemas, validate GraphQL operations, Liquid and theme files, and UI-extension code". "LIQUID_VALIDATION_MODE defaults to full, which exposes validate_theme".
- https://www.adsx.com/blog/claude-code-shopify-theme-liquid-build-guide | EXCERPT | practitioner. Claims the Dev MCP validates "against your active theme schema before the file is written". CONFLICT A3: not in the official description. Unverified.
- https://www.fudge.ai/blog/ai-first-shopify-development/ | EXCERPT | vendor. "an AI model trained months ago does not know the current Admin API version or the exact Liquid filters available, and left alone, it hallucinates field names and stale syntax."

### A3. Claude Code plus Shopify CLI posts (2026)
- https://www.letstalkshop.com/blog/how-to-use-claude-code-for-shopify-liquid-theme (and /claude-code-shopify-cli-integration, /claude-code-for-shopify-development) | EXCERPT | practitioner. "running Claude Code in one terminal pane attached to your theme repo, running shopify theme dev in another pane with hot-reloading on a development theme". Refactor trap: Claude strips schema settings that "aren't used anywhere in the Liquid," but "merchants configure those settings through the theme editor, and removing them wipes their customizations." Suggested rule: "Preserve all existing schema settings unless I call one out by name. Adding new settings is fine; removing them is not." "config/settings_data.json file should never be touched by Claude Code." Never run "Claude Code with auto-approve modes on live stores."
- https://www.launchtip.com/blog/claude-shopify-theme-kit-build-faster-custom-themes-without-going-headless | EXCERPT | practitioner.
- https://www.get-ryze.ai/blog/claude-shopify-skills | EXCERPT | vendor.
- https://gist.github.com/karimmtarek/3a8a636a05ae1c349ad0bba9d10425f0 | FULL | practitioner CLAUDE.md. "Define schema settings (`{% schema %}`) for all configurable content - never hardcode merchant-facing copy." "Run `shopify theme check` before every commit and resolve all errors. Treat warnings as errors for new code." "Never push directly to a live theme. Use a development theme or a duplicate." "Scope component styles using a BEM-like convention or web component selectors - avoid broad tag selectors." "Write vanilla JS unless the project already uses a framework." "All customer-facing strings must use `{{ 'key' | t }}` translation keys defined in `locales/`." "Add `config/settings_data.json` to `.gitignore` for team projects unless you have a deliberate sync strategy".
- https://github.com/baslefeber/shopify-skills | FULL | practitioner (MIT). "shopify-section-builder: Scaffold a complete Horizon section or block". "review-ai-shopify-liquid: Audit AI-generated Liquid for classic mistakes: hallucinated filters, JS variant logic, hardcoded routes". Built for Horizon.

### A4. Theme Check
- https://github.com/Shopify/theme-tools | FULL | official.
- https://dev.to/yakohere/how-to-debug-shopify-liquid-a-complete-guide-2655 | EXCERPT. Theme Check "catches malformed syntax, undefined objects, unknown filters, and schema errors" but "is limited to static analysis only and doesn't catch runtime errors." "Variables can be nil or empty without producing an error - Liquid just outputs nothing."
- https://dev.to/iamrobindhiman/the-liquid-you-lint-isnt-the-liquid-shopify-runs-5bhp | EXCERPT. CONFLICT A4 (soft): lint is not runtime; preview with real products still required.

### A5. Horizon "Generate" AI blocks and Sidekick
- https://shopify.dev/docs/storefronts/themes/architecture/blocks/ai-generated-theme-blocks and help.shopify.com generate-blocks | EXCERPT | official. Plans: "Free trial, Basic, Growth, Advanced, or Plus". "Your account language must be set to English, your theme must support custom blocks, and you can only add blocks to sections that accept them." "The theme block generation feature is available for all themes on the Shopify Theme Store."
- https://www.eesel.ai/blog/shopify-magic-theme-block-generation | EXCERPT | vendor, possibly OLD. "some merchants have noticed that their page speed declines after adding AI-generated blocks". "Getting an 'add to cart' button to work right ... can be tricky." CONFLICT A5: any Theme Store theme vs Horizon in practice. Shrine is sold outside the Theme Store per these results.
- https://commerce-media.info/en/blogs/ec/shopify-new-theme-horizon | EXCERPT. "Advanced layout instructions may cause generation failures or bugs".
- https://neat.digital/blogs/blogs/shopify-ai-sidekick-magic-honest-review-2026 | EXCERPT | agency. Generated blocks "requires manual cleanup for production use, as generated code often has inconsistent spacing, does not match brand styles, and lacks proper schema settings for editor configurability."
- https://www.fudge.ai/guides/shopify-sidekick-use-cases/ | EXCERPT | vendor. Sidekick "still doesn't write theme code, build new sections, or create landing pages."
- https://www.tokenpost.com/news/technology/26198 | EXCERPT | unverified. Canvas workspace "bringing code and theme changes into a single view." CONFLICT A6 with Fudge.

### A6. Figma MCP to Shopify sections
- https://stargazerstudio.net/blog/figma-to-shopify-ai-workflow | EXCERPT | practitioner. Problem: "the model can't see what it's building ... three hours later you have a homepage that's vaguely correct." Loop: slice Figma PNG; screenshot local `shopify theme dev` render in headless Chrome at 1440 wide; gap list grouped by "layout / typography / colour / imagery / content"; fix "smallest blast radius first - JSON template setting before section schema setting before Liquid markup before section CSS before global CSS"; re-screenshot; loop.
- https://ionlyspeakliquid.beehiiv.com/p/i-only-speak-liquid-84-... | EXCERPT | possibly OLD. "80% faster" (unsourced).
- https://www.capaxe.com/blog/20251114-getting-started-figma-mcp/ | EXCERPT. "The quality of generated code is directly proportional to the quality of your Figma design".

### A7. Playwright / screenshot checks
- https://dev.to/esunitha/the-tester-agent-visual-qa-with-playwright-and-a-vision-model-256m | EXCERPT. Not Shopify-specific.
- https://bug0.com/knowledge-base/playwright-visual-regression-testing | EXCERPT. "toHaveScreenshot() assertion."

### A8. Shopify GitHub integration
- https://community.shopify.dev/t/github-integration-doesnt-always-sync-settings/18881 | EXCERPT. Git JSON settings changes "aren't always synced to the connected theme".
- https://community.shopify.dev/t/config-settings-data-json-not-syncing-to-local-files-with-theme-editor-sync/34943 | EXCERPT. settings_data.json changes "are silently not synced" with --theme-editor-sync.
- https://github.com/Shopify/cli/issues/4715 | EXCERPT (title). "CLI always requesting reconciliation strategy for settings_data.json".
- https://appycodes.com/blog/shopify-theme-git-ai-workflow/ | EXCERPT | agency. "letting an AI coding agent work the repository - never the live theme editor." "feature branch wired to an unpublished preview theme; Theme Check and a human review the pull request; merging to the branch the live theme mirrors is the deploy, and reverting that commit is the rollback."
- https://github.com/ShopLab-Team/shoplab-pr-shopify-theme-preview | EXCERPT. Preview theme per pull request.

### A9. Third-party section apps (all EXCERPT; verify prices on listings)
- Section Store (section.store; apps.shopify.com/section-factory): "Individual sections cost $9 each as a one-time purchase"; "$10/month Plus subscription"; "730+ sections".
- Shogun: Build $39, Grow $199, Advanced $499; AI Section Builder Starter $0, Pro $19, Unlimited $199. CONFLICT A7: older $149 tier.
- GemPages: Build $29 "20 sections", Optimize $59 "100 sections", Enterprise $199.
- PageFly: "$24" vs "around $18/month ... Unlimited $99/month".
- EComposer: CONFLICT A8, monthly vs annual pricing.
- https://help.fluorescent.co/stiletto/general/theme-updates (another theme vendor): "Any third-party apps or custom code will need to be reinstalled into the new theme files."

## B. Safe store connection
- shopify.dev theme dev / CLI pages | EXCERPT | official. Development themes "don't count toward your theme limit, and are deleted from the store after seven days of inactivity." For a lasting preview link "push your development theme to an unpublished theme".
- Shopify CLI live guard (github.com/Shopify/shopify-cli/pull/1798): "This is the live theme on my-store. If you wish to make changes to it, then you will have to pass the --allow-live flag".
- https://github.com/Shopify/themekit/issues/699 | FULL | OLD (2020). Misspelled theme id sent a deploy to the live theme.
- community.shopify.com threads (EXCERPT, titles): "Shopify CLI: Pushing a theme overwrites settings and section data"; "Sections get removed on pushing theme from local to live store".
- https://www.shopify.com/blog/staging-site | EXCERPT | official blog. Duplicate theme "contains the visual and structural elements of your store, not any backend settings like apps, checkout, or inventory." "Duplicate the theme, edit the copy, and share a preview link before publishing." "Ideally, launch during low-traffic hours."
- https://www.qeretail.com/blog/shopify-theme-architecture | EXCERPT. "Test custom sections across templates, devices, markets, and theme-editor states."
- https://nisonco.com/using-codex-for-shopify-development/ | EXCERPT. "requires a knowledgeable person to review the finished store before publication."
- https://community.shopify.dev/t/cart-based-app-extensions-cant-be-previewed-in-the-theme-editor/36458 | EXCERPT (title).

## C. Failure writeups
- C1 Hallucinated fields: https://www.fudge.ai/guides/debug-shopify-liquid-with-claude/ | EXCERPT. "made-up fields like product.custom_price resolve to nil and reintroduce blank-output bugs."
- C2 Invalid schema: https://github.com/Shopify/cli/issues/4871 | FULL | OLD (Nov 2024). "Invalid schema: class is invalid" from a Tailwind class with brackets in schema `class`. Also titles: "setting link_list type can only be inserted once" (Shopify/shopify-cli#2388, Shopify/cli#1965); "Invalid JSON in tag 'schema'"; "Invalid preset". Summary (unverified): missing `label`, invalid `type`, blocks missing `name`, duplicate block types.
- C3 App/JS conflicts: https://community.shopify.dev/t/issues-with-implementing-app-blocks-that-depend-on-variant-changes/8885 | EXCERPT. "It's very challenging to find a fully reliable method for apps to respond to changes like a variant changing". https://craftshift.com/shopify-variant-image-not-changing-on-click-fix/ | EXCERPT | vendor. Event capture blocks the theme's own script.
- C4 Theme updates: https://help.shopify.com/en/manual/online-store/themes/managing-themes/updating-themes | EXCERPT | official. "Customizations made to your theme using the theme editor are copied over". Status: "Theme added: code edits successfully included" / "Theme added: code edits could not be included". fuelthemes.net and others: code edits "won't be included". Pattern: create new section files, do not edit shipped ones. CONFLICT C1.
- C5 Easify: https://easifyapps.com/docs/options-dont-show/ | EXCERPT | official app doc. Causes: "a conflict between the app and your theme, having multiple product options apps enabled simultaneously, or conflicts with other apps", especially "price adjustments, discounts, cart drawer, delivery and pickup, or booking features." First check: App embeds enabled. Add-on products are hidden via the `meta.hidden` metafield and must be active on the Online Store (easifyapps.com/docs/custom-option-prices-not-included-in-orders/). Inference (unverified): custom sections that list all products could surface Easify's hidden add-on products. Vendor-hosted review: add-to-cart "malfunctioned due to a conflict with the Kaching Bundles plugin".
- C6 Kiwi: https://intercom.help/kiwi-sizing-chart/en/articles/10291102-size-chart-missing-after-theme-update | EXCERPT | official. "Theme updates can remove or overwrite the KiwiSizing app block". Fix: theme editor, Products, Default product, Apps, Add block, "Kiwi". Sizing Injection Selector (CSS selector) setting exists; inference: custom product-form markup can break selector-based injection. "Enabling Kiwi Theme Helper is necessary for optimal app performance".
- C7 Shrine: https://shrine.io/pages/theme-updates | EXCERPT | vendor changelog. 1.9.0 dated July 09, 2026: "custom columns rework where each column is now a block that accepts other blocks inside of it". 1.9.1 fixed "sticky product information content and sticky header issues that occurred in version 1.9.0." Shrine Pro marketing: "46+ premium sections". help.shrinetheme.com blocked: GAP. Nulled Shrine copies rank highly; ignored.

## D. Section patterns (apparel)
- Size guide near size selector: https://baymard.com/research-articles/apparel-size-information | EXCERPT | independent research. "only 17% of desktop sites and 13% of mobile sites provide sufficient sizing information". Link "should be included near the size selector."
- Accordions vs tabs: https://byteandbuy.com/blog/100-shopify-pdps-design-patterns-that-drive-3-cvr | EXCERPT | vendor. "27% of users overlook tabbed content entirely" (unverified origin).
- Collection filters: help.shopify.com Search & Discovery filters (official); https://www.charleagency.com/articles/shopify-custom-filters/ | EXCERPT. "These filters only work if the underlying product data is consistent."
- Photo reviews: studioniza.com, wiserreview.com, eevy.ai | EXCERPT | vendor. Judge.me "Forever Free plan collects unlimited reviews with photos and videos". Conversion lift numbers unverified.
- Brand story: shopidevs.com, shopify.com/blog/how-to-write-an-about-us-page | EXCERPT. Stats unsourced.
- Complete the look / bundles: branvas.com, easyappsecom.com, apps.shopify.com/shop-the-look-4 | EXCERPT | vendor. "Product bundling can increase AOV by 15-25%" (unverified).
- Shrine Pro already advertises upsell sections; check existing sections before building custom.

## E. Workflow writeups
- Appycodes branch, preview theme, Theme Check, PR review, merge = deploy, revert = rollback (A8).
- Stargazer visual loop (A6).
- Spec writing: https://www.fudge.ai/guides/claude-prompts-shopify/ ; https://flagship.inc/en/columns/ai-for-shopify-theme-development | EXCERPT. "state the Shopify constraints upfront." Checklist: "making every text and image field a schema setting (not hard-coded), adding a 'presets' entry for section picker integration, using semantic HTML and BEM-style class names, avoiding inline styles, and returning a complete .liquid file". "Provide reference files like section structure rules and a canonical section template example".
- https://www.firstpier.com/resources/shopify-section-schema | EXCERPT. Presets give "default block instances when first added".
- https://mgroupweb.com/blogs/custom-shopify-sections-guide/ | EXCERPT. "uses blocks for repeatable content and delegates reusable markup to snippets".
- Repeated guardrails: never touch settings_data.json; never remove existing schema settings; no auto-approve on live; always dev or unpublished theme. GAP: no source describes a non-developer reviewer.

## Queries run (49)
1. Claude Code Shopify theme section CLI workflow blog 2026
2. Shopify Dev MCP server theme Liquid validation experience
3. Shopify Horizon "generate block" AI Sidekick theme blocks review limitations
4. "theme check" AI generated Liquid Shopify lint Claude Cursor
5. Figma MCP to Shopify section Liquid workflow
6. Shopify AI Toolkit April 2026 validate_theme Claude Code plugin release
7. AI hallucinated Liquid filter Shopify ChatGPT code doesn't exist
8. Shopify "Invalid schema" section error setting type community
9. shopify theme dev hot reload development theme unpublished preview safe editing live theme warning
10. Easify Product Options theme conflict custom code troubleshooting help
11. Kiwi Size Chart app block theme placement Online Store 2.0 help
12. Shrine theme Shopify update keep custom code help center
13. Shopify theme update lose custom code customizations what carries over
14. Shopify GitHub integration theme branch sync settings_data.json conflicts
15. "Size Chart Missing After Theme Update" Kiwi
16. help.shrinetheme.com update theme guide custom code Shrine PRO
17. Easify product options app block "app embed" theme editor price add-on cart drawer conflict
18. Section Store Shopify app pricing sections per section purchase review
19. PageFly vs GemPages vs Shogun vs EComposer pricing 2026 sections only theme sections
20. Playwright screenshot visual regression Shopify theme sections AI agent QA
21. Shopify development store vs duplicate theme test custom section before publishing live store
22. how to write a spec prompt for AI to build Shopify section schema settings blocks presets
23. Shopify custom section library consistency CLAUDE.md conventions sections naming schema design tokens
24. Shopify app conflicts custom JavaScript variant change event product form theme custom code breaks app
25. shopify.dev "AI generated theme blocks" requirements theme support limitations
26. Shopify Sidekick edit theme code 2026 Editions theme changes review
27. apparel Shopify product page collapsible tabs accordion size guide conversion case study
28. Baymard apparel product page size guide accordion findings e-commerce UX
29. "complete the look" upsell section Shopify apparel AOV results bundle section
30. Shopify photo reviews UGC wall section apparel trust conversion Judge.me Okendo
31. Shopify collection filters Search & Discovery apparel size color filters best practice
32. brand story about us section Shopify homepage small brand trust conversion
33. agency workflow AI Shopify theme development spec mockup build QA publish 2026 lessons learned
34. fudge.ai "AI-first Shopify development" what still needs review Liquid
35. appycodes Shopify theme Git AI workflow pull requests preview theme
36. "shopify theme push" accidentally live theme overwrote published theme --allow-live warning
37. stargazerstudio figma to shopify AI workflow section by section
38. Easify product options review "theme" conflict "add to cart" broke support fixed
39. Easify "custom option prices" not included orders add-on product hidden variant mechanism
40. Kiwi Theme Helper app embed enable size chart not showing "Sizing Injection Selector"
41. Shrine Pro theme community custom section added code update version 1.9
42. Shopify Help Center edit theme code duplicate theme before editing code "we recommend" backup
43. Section Store sections survive theme update install into theme code app sections how they work
44. Shopify theme blocks @theme older themes not supported static blocks app blocks "@app" section schema custom section app block support
45. Claude Code Shopify theme mistakes lessons "settings_data.json" overwritten theme editor changes lost AI agent
46. Shogun Shopify sections pricing 2026 "Shopify sections" plan limit
47. EComposer "theme sections" pricing GemPages theme section builder Shopify sections inside theme editor 2026
48. "theme check" catches what does not catch runtime Liquid errors nil objects limitations
49. "Kiwi Size Chart" location help community shopify size chart position theme
