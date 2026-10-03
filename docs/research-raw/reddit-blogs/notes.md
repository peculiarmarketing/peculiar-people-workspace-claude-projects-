# Raw notes: AI coding assistants building Shopify theme sections, failure reports

Collected 2026-10-03. Research only.

## Access conditions (read first)

- WebSearch with allowed_domains reddit.com: refused by the search API ("domains are not accessible to our user agent"). Zero Reddit threads surfaced in any unrestricted search either. Result: NO Reddit content in this file. Every subreddit in scope (r/shopify, r/ShopifyeCommerce, r/ClaudeAI, r/ClaudeCode, r/vibecoding, r/webdev) is uncovered.
- WebFetch on www.reddit.com and old.reddit.com (.json search): "Claude Code is unable to fetch from ... reddit.com".
- WebFetch on community.shopify.com, community.shopify.dev, shopify.dev, dev.to, medium.com, substack, and every practitioner blog tried: EGRESS_BLOCKED by the network proxy.
- Only github.com was fetchable.
- Consequence: almost everything below is EXCERPT, meaning text from the search engine's result summary, which is itself a model-written paraphrase of the page. Treat every EXCERPT as PARAPHRASED, not as an exact quote from the author. Dates were mostly not visible in excerpts.
- Date heuristic used for Shopify Community: new Discourse URLs (community.shopify.com/t/slug/NNNNNN) with IDs above roughly 400000 appear to be 2025-2026 threads; old Khoros URLs (/c/.../td-p/NNNNNNN or /m-p/) are from the pre-2025 forum and are almost certainly OLDER THAN 12 MONTHS. This is an inference, not a verified date.

## Searches run (26 attempted, 23 returned results)

1. reddit shopify AI generated liquid section not showing in theme editor ChatGPT
2. "Invalid JSON in tag 'schema'" shopify section ChatGPT
3. Claude Code Shopify theme custom section 2026 experience
4. Cursor Shopify theme development liquid hallucinated filters
5. Shopify Sidekick generate theme section problems 2026
6. reddit r/shopify ChatGPT broke my theme live theme no backup
7. reddit ClaudeAI Shopify theme liquid section broke
8. vibecoding shopify theme AI custom section mistakes theme update overwrote custom code
9. Shrine PRO Shopify theme custom section
10. Easify Product Options not showing custom theme conflict
11. Kiwi Size Chart not showing custom theme conflict product page
12. site:reddit.com shopify liquid chatgpt section schema (no reddit results)
13. site:reddit.com claude code shopify theme (no reddit results)
14. AI generated Shopify section CSS leaking other sections scoped styles {% stylesheet %}
15. custom code broke product options app variant dropdown Shopify theme JavaScript conflict
16. reddit shopify "AI" said it fixed theme but nothing changed liquid
17. dev.to shopify theme AI coding agent lessons learned theme check preview theme 2026
18. AI-generated Shopify section mobile layout broken CLS images performance
19. Shopify GitHub integration theme AI agent pushed to live theme overwrote customizer settings_data.json
20. Shrine theme Shopify custom code support modifications voids support "Shrine"
21-23. three reddit.com allowed_domains searches: API ERROR 400, reddit not accessible
24. "Can Claude Build a Shopify Store" dominikatracy truth
25. Shopify theme AI edit "older versions" rollback duplicate theme before AI changes Sidekick theme edits undo
26. Shrine theme Easify OR Kiwi size chart product page app block not showing
27. AI coding assistant rewrote working Shopify theme code scope creep Liquid "only change" prompt lessons
28. AI generated Shopify section accessibility issues alt text aria hardcoded text not translatable
29. Shopify AI Toolkit Dev MCP validate theme Liquid Claude Code hallucinate April 2026 issues
30. "theme added: code edits could not be included" custom section lost after theme update
31. medium shopify ChatGPT custom section mistakes "schema" "presets" learned hard way
32. community.shopify.com AI generated section "ChatGPT" custom section theme editor not saving settings hardcoded
33. Sidekick generated section looks fine in preview misaligned live site page width

## Fetch log

| URL | Result |
|---|---|
| https://old.reddit.com/r/shopify/search.json?q=chatgpt+liquid+section&restrict_sr=1 | FAIL: unable to fetch reddit |
| https://www.reddit.com/r/shopify/search.json?q=claude+theme+section | FAIL: unable to fetch reddit |
| https://community.shopify.com/t/overlapping-issue-with-ai-generated-section/621122 | FAIL: EGRESS_BLOCKED |
| https://community.shopify.com/t/not-been-to-center-the-section-which-i-created-using-sidekick/580094 | FAIL: EGRESS_BLOCKED |
| https://community.shopify.com/t/unable-to-generate-ai-theme-block/614173 | FAIL: EGRESS_BLOCKED |
| https://community.shopify.dev/t/sidekick-should-verify-theme-app-embed-block-section-placement-not-just-guide/36456 | FAIL: EGRESS_BLOCKED |
| https://dev.to/iamrobindhiman/the-liquid-you-lint-isnt-the-liquid-shopify-runs-5bhp | FAIL: EGRESS_BLOCKED |
| https://seotldr.substack.com/p/ai-shopify-theme-customisation | FAIL: EGRESS_BLOCKED |
| https://monkeyman.agency/insights/building-a-shopify-theme-with-claude-code/ | FAIL: EGRESS_BLOCKED |
| https://www.fudge.ai/guides/debug-shopify-liquid-with-claude/ | FAIL: EGRESS_BLOCKED |
| https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/valid-schema | FAIL: EGRESS_BLOCKED |
| https://www.adsx.com/blog/claude-code-shopify-theme-liquid-build-guide | FAIL: EGRESS_BLOCKED |
| https://github.com/github/awesome-copilot/blob/main/agents/shopify-expert.agent.md | OK (FULL READ, via summarizer) |
| https://blog.yoniakabecky.com/creating-shopify-theme-sections-with-cursor | FAIL: EGRESS_BLOCKED |
| https://easifyapps.com/docs/options-dont-show/ | FAIL: EGRESS_BLOCKED |
| https://help.kiwisizing.com/support/solutions/articles/44000554320--shopify-only-size-chart-is-not-showing-up-what-do-i-do- | FAIL: EGRESS_BLOCKED |
| https://github.com/ArtificialMonks/shopify-liquid | OK (FULL READ, via summarizer) |
| https://www.letstalkshop.com/blog/how-to-use-claude-code-for-shopify-liquid-theme | FAIL: EGRESS_BLOCKED |
| https://medium.com/@Cavlemasters/help-i-made-a-custom-section-in-shopify-but-now-its-not-showing-in-the-theme-editor-ui-9552060b57da | FAIL: EGRESS_BLOCKED |
| https://ed.codes/blog/how-shopify-theme-updates-work | FAIL: EGRESS_BLOCKED |
| https://bigredjelly.com/blog/how-to-use-chatgpt-to-code-features-for-your-shopify-store/ | FAIL: EGRESS_BLOCKED |
| https://www.appbrew.com/blogs/shopify-sidekick | FAIL: EGRESS_BLOCKED |
| https://shopcircle.co/blogs/news/product-options-not-showing-after-theme-update-shopify | FAIL: EGRESS_BLOCKED |
| (proxy status check via shell) | DENIED by permission classifier; not retried |

## Excerpts by source (all EXCERPT = search-engine paraphrase unless marked)

### community.shopify.com/t/why-is-my-custom-liquid-not-visible-in-theme-editor/205043/1
Date: not shown. Thread ID 205043 suggests OLDER THAN 12 MONTHS (inference).
EXCERPT: User built a custom Liquid section with ChatGPT; it did not appear in the Theme Editor. "the schema JSON, JavaScript, and CSS blocks are written backwards (reversed character order), making them unparsable." Fix noted in another excerpt (search 2): "fixing reversed text encoding, properly nesting settings within blocks, adding required 'name' fields for each block type, and correcting JSON syntax"; if a compatibility error appears after the fix, remove the section from the customizer and re-add it.

### Search 1 summary (unattributed in results; likely from qwe.edu.pl or similar)
EXCERPT: "AI generates schema blocks with invalid type values or malformed JSON. Shopify silently rejects these – your section won't show in the theme editor, no error message." Also: "Several sections were missing presets ... Once presets were added, the sections became visible." Fix: run `shopify theme check` before pushing.

### Medium @Cavlemasters "Help! I made a custom section in Shopify, but now it's not showing in the Theme Editor UI"
Date: not shown. EXCERPT: "Without at least one preset, Shopify won't display the section in the Theme Editor's 'Add section' interface."

### f22labs section customization (from search 31)
EXCERPT: invalid schema JSON from "comments, curly quotation marks, duplicate IDs, missing commas, and trailing commas can prevent the section from saving."

### bigredjelly.com ChatGPT for Shopify (search 31)
Date: not shown. EXCERPT: OS 2.0 features "postdate some of ChatGPT's training data, which means outputs for newer theme architecture may need more correction"; "sometimes ChatGPT recommends placing code in a section where it won't function properly."

### Invalid JSON in tag 'schema' threads (search 2)
community.shopify.com/c/shopify-design/custom-section-invalid-json-schema-and-not-selectable-in/td-p/1557385 (old Khoros URL: OLDER THAN 12 MONTHS)
community.shopify.com/t/invalid-json-in-tag-schema-error-for-whole-code/169273 (OLDER THAN 12 MONTHS, inference)
community.shopify.com/t/how-to-fix-this-error-invalid-json-in-tag-schema-when-i-add-a-collapsible-section/329958 (likely OLDER THAN 12 MONTHS)
EXCERPT causes: trailing commas; "you cannot mix HTML in with JSON"; missing block 'name'.

### Shopify Community: Overlapping issue with AI generated section /621122
Date not shown; ID suggests 2026 (inference). Only title surfaced in search 14. Fetch blocked. No content.

### Shopify Community: Section Interrupting Aesthetics of Another? /166189
OLDER THAN 12 MONTHS (inference). EXCERPT: an "Image Marquee" section caused slider arrows across other sections to change appearance (CSS leak).

### mgroupweb.com custom Shopify sections guide (2026 in title)
EXCERPT: "Keep styles scoped with the #shopify-section-{{ section.id }} selector to avoid leaking styles to other sections."

### Shopify Community: Not been to center the section which I created using Sidekick /580094
Date not shown; ID suggests late 2025 or 2026 (inference). EXCERPT (search 33, appears to be the accepted reply): Sidekick section looks right in preview but misaligned live "because Sidekick creates content that is not theme-aware, and after saving, the theme's grid, widths, and spacing override the preview." Fix: use Image with text / Multicolumn / Text columns instead of Rich text or Custom liquid; use real H2/H3; CSS `.section-about-us .rte { max-width: 1200px; margin: 0 auto; }`.

### Shopify Community: Unable to generate AI theme block /614173 and Generate with AI button missing /577864
Dates not shown; IDs suggest 2026 / late 2025. EXCERPT: error "Unable to generate theme block at the moment"; the "Generate with AI" option disappeared for some users.

### community.shopify.dev /36456 "Sidekick Should Verify Theme App Embed & Block/Section Placement - Not Just Guide"
Title only. Implies Sidekick gives instructions for app embed/block placement but does not verify. Content not retrieved.

### Shopify Community: Generate Blocks in Any Theme /417074 and HELP - Using AI to generate blocks in product information /422282
EXCERPT: workaround to get AI block generation in non-supporting themes by adding a section whose schema accepts "@theme" blocks. Also: request layout/alignment settings via follow-up prompts before saving.

### appbrew.com "Shopify Sidekick: What It Can and Can't Do in 2026 (An Honest, Tested Review)"
2026. EXCERPT: "theme work scored 2 out of 10, with wrong-page section builds and non-functional CSS that took four to six iterations to fix on simple tasks." (attribution to appbrew is the most likely of the search-5 sources but not certain)

### fudge.ai "Shopify Sidekick Limitations (2026)"
EXCERPT: "Sidekick cannot generate, edit, or debug Liquid code." Also "If you're on Dawn 11.0 or later, Sidekick can generate full theme sections from a description". (Note internal tension, see conflicts.)

### monkeyman.agency "Claude Code on Shopify Themes · 2026 Agency Playbook"
2026. EXCERPT: merchants "prompting agents directly against live themes risk pushing broken sections within a week"; prompting patterns "spec-then-build, paired editing on single sections, and audit-and-refactor"; guardrails "a clean git branch, theme-check in CI, a staging dev store with real data, and human PR review still catch about one in eight changes."

### letstalkshop.com, launchtip.com, adsx.com, askphill.com, claudefa.st (search 3, 27, 29)
2026. EXCERPT: Shopify open-sourced AI Toolkit / Dev MCP April 9, 2026; `validate_theme_codeblocks` validates Liquid against schemas. "you may occasionally see Claude invent properties like `product.featured_variant`" or misremember pagination syntax. Advice: do not ask Claude to "convert Dawn into a custom theme"; scope per section, specify a single file, preserve existing block types.
Note: launchtip, letstalkshop, fudge, get-ryze are vendor content-marketing blogs; they read as SEO pages, not first-hand failure reports.

### dev.to "The Liquid you lint isn't the Liquid Shopify runs" (iamrobindhiman)
Date not shown. Title only plus EXCERPT: "Linters flag filters that AI assistants hallucinate into templates that don't exist". The title claims a gap between local lint and Shopify's runtime; content not retrieved.

### seotldr.substack.com "Using AI to customise your store (without breaking it later)"
EXCERPT: "with AI, you can ask it to change something back but it won't necessarily restore it exactly as it was."

### dominikatracy.com "Can Claude Build a Shopify Store? I Tried. Here's the Truth"
2026 (per excerpt). EXCERPT: Claude can build a store "if you connect it to your theme through GitHub or a code editor, though it will not do it in one click and the first version will need a lot of steering"; you "copy and paste it bit by bit into the Shopify backend"; conclusion "Claude can build Shopify stores, eventually, after a fight."

### appycodes.com "Shopify Theme + Git + AI Development Workflow" (search 19)
EXCERPT: when anyone saves in the theme editor, "Shopify commits them back to the connected branch-mostly config/settings_data.json and templates/*.json"; "never rewrite config/settings_data.json"; "Put the theme in Git, connect the branch to Shopify, and let an AI coding agent work the repository-never the live theme editor."

### github.com/github/awesome-copilot shopify-expert.agent.md: FULL READ (summarizer)
Recommends `shopify theme dev` for preview, `shopify theme push` to deploy, "Test on development stores before production deployment." No explicit settings_data.json protection rule found in the summarized text.

### github.com/ArtificialMonks/shopify-liquid: FULL READ (summarizer)
README lists validation targets: "hallucinated filter detection", "over-engineering prevention", "CSP compliance", "Performance optimization". CSS scoping via section-ID namespacing. Only 4 commits; date not visible.

### dev.to "Shopify's ChatGPT and Claude Connectors: What They Expose and Where the Limits Are" (search 6)
EXCERPT: connected AI tools "can only change unpublished themes, not your live theme. They cannot edit your live theme, publish a theme, or delete one."

### Shopify Community: Urgent matter! Sahara theme collection code went wrong /417178
EXCERPT: user corrupted the Shop All collection page after pasting source code per ChatGPT's instructions into the backend of a page.

### Rollback mechanics (search 6, 25; help.shopify.com, fudge.ai)
EXCERPT: per-file "Older versions" dropdown in the code editor; theme editor (customizer) saves have no history once saved; duplicate theme first.

### Theme updates (search 8, 30): community.shopify.com/t/how-to-update-your-shopify-theme-without-losing-your-custom-code/686447 (ID suggests 2026), /t/theme-updates-delete-all-custom-codes/415152, veronicajeans.com, ed.codes, techrbun
EXCERPT: only edits to theme-shipped files are at risk; merchants get "Theme added: code edits could not be included" on conflict and must reapply; one source says on conflict Shopify "keeps the theme developer's version"; another says Shopify "now supports theme updates with custom section preservation".
Note: veronicajeans title says 2024-2025: OLDER THAN 12 MONTHS likely.

### Product options apps (search 15)
shopcircle.co (2026 in title) EXCERPT: options "fail to show after a theme update ... because new template files lack the app block injections or underlying code hooks". community.shopify.com/c/shopify-design/product-variants-stopped-working-dawn-theme/td-p/1468709 (OLDER THAN 12 MONTHS): JS conflicts from installing apps or adding custom JS; "check the browser console".

### Easify Product Options (search 10)
easifyapps.com/docs/options-dont-show/ EXCERPT: possible "conflict between the app and your theme, or you have installed and enabled multiple product options apps simultaneously, or there is a conflict with another existing app"; check App embeds tab enabled; check option set assignment; then contact support@tigren.com. No user report found tying Easify to AI-written custom code specifically.

### Kiwi Size Chart (search 11, 26)
intercom.help/kiwi-sizing-chart and help.kiwisizing.com EXCERPT: chart missing if a product template lacks the Kiwi app block; custom templates/themes may lack snippets; snippets auto-installed at install time and must be reinstalled if auto-install fails or theme changes; "If the size chart loads when you refresh the page but not when you click from another page, then it's likely an issue with your theme settings"; "Sizing Injection Selector" article for repositioning. Kiwi "may conflict with heavily modified theme code" (attribution uncertain, likely bestgrowthapps review). developers.kiwisizing.com/docs/app-integration exists (not fetched).

### Shrine / Shrine PRO (search 9, 20)
No report found of AI edits or custom sections on Shrine specifically. EXCERPT: Shrine by "Shrine Solutions", Pro around $349 (debutify); support "via email and GitHub tickets by a small external team" (identixweb/clyro). Notable: search results include Etsy, gumroad, doniaweb and nullforums listings selling or leaking "Shrine Pro" copies (e.g. "Shrine Pro Theme 1.9.0 +200 Sections"). Pirated copies would not receive official updates or support. community.shopify.com/t/shrine-theme-help/418729 exists (not fetched). entaice.com has "Solving Styling Woes in Shopify's Shrine Pro Theme" (not fetched; looks like content farm).
