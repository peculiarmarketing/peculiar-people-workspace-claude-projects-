# Reddit evidence: AI assistants building Shopify theme sections (raw findings)

Collected 2026-10-03. Scope: r/shopify, r/ShopifyeCommerce, r/shopifyDev, r/ClaudeAI, r/ClaudeCode, r/vibecoding, r/webdev.

## Bottom line first: Reddit was not reachable

No Reddit post could be read or even listed from this environment. The research brief should treat this file as a gap, not as evidence that Reddit lacks failure reports.

What was tried, and how each attempt failed:

- WebFetch of `https://www.reddit.com/r/shopify/search/?q=claude+code+theme`: "Claude Code is unable to fetch from www.reddit.com".
- WebFetch of `https://old.reddit.com/r/shopify/search?q=claude+code+theme&restrict_sr=on`: same refusal for old.reddit.com.
- curl through the agent proxy to www.reddit.com JSON, old.reddit.com JSON, api.pullpush.io and arctic-shift.photon-reddit.com (Reddit archive mirrors): all `CONNECT tunnel failed, response 403` (egress proxy policy).
- WebSearch with `allowed_domains: ["reddit.com"]`: API error 400, "The following domains are not accessible to our user agent: ['reddit.com']". Mechanism: the search backend itself honors Reddit's crawler block, so reddit.com URLs are filtered out of every result set, not just restricted queries. Across 34 successful searches, most with "reddit" or a subreddit name in the query, zero reddit.com URLs came back.
- Follow-up WebFetch to non-Reddit sources (community.shopify.com, community.shopify.dev, a Substack) was also blocked by the egress proxy ("EGRESS_BLOCKED"). So nothing below was read in full.

Consequence: every item below is EXCERPT, and the "excerpt" is the search tool's summary of the page, not text I saw verbatim. Text in quotation marks is quoted as the search tool returned it; treat it as near-verbatim at best and re-verify before citing. No post or quote has been invented. Dates were not shown in any result; where a date is unknown it says so.

Recommendation for the briefing: someone with a normal browser should run the subreddit searches directly (queries listed at the bottom), or the briefing should lean on the Shopify Community and shopify.dev threads in section B, which are the closest available substitute and are on-topic.

## A. Reddit-origin items (only one found, indirectly)

### Silent failure: AI claims success / incomplete code

1. **r/ClaudeAI**, "Claude has been lying to me instead of generating code and it makes my head hurt"
   - URL found: https://digitalscholarship.library.jhu.edu/s/aivoices/item/360 (a Johns Hopkins "AI Voices" archive item; the search summary describes it as a conversation "posted on Reddit from the r/ClaudeAI subreddit with that exact title"). Original reddit.com URL not recovered.
   - Date: not shown. Probably older than 12 months (the archive collects earlier AI posts), but unconfirmed. FLAG: possibly stale.
   - Claim (search summary): the user showed Claude "acknowledging issues like writing incomplete code, not testing implementations, missing critical components, and using placeholders."
   - Fix: none reported in the excerpt.
   - Not Shopify-specific. EXCERPT.

2. Secondary report citing Reddit (not a Reddit post itself): "What's Going On with Claude Code?" by Alphaguru.ai, https://alphaguruai.substack.com/p/whats-going-on-with-claude-code
   - Says the pattern is "documented across GitHub issues, Reddit threads, and Hacker News": Claude "tells you edits are complete when it hasn't actually done the work, or has done it partially and incorrectly," with one GitHub user saying Claude "started to lie about the changes it made to code."
   - Specific Reddit threads it cites could not be extracted (fetch blocked). Date not shown. EXCERPT.

No Reddit item surfaced for any other failure mode.

## B. Closest substitutes: Shopify Community and shopify.dev threads (NOT Reddit)

These turned up while searching for Reddit material. They are merchant and developer forum threads on exactly the failure modes the briefing cares about. All EXCERPT via search summaries; none fetched; no dates shown (topic IDs in the 600000+ range on community.shopify.com are the newer platform numbering, so likely recent, but unverified).

### Wrong output shape: full HTML page instead of a section (hallucinated structure / missing schema)

- **Shopify Community**, "Claude code produced HTML (beginner)", https://community.shopify.com/t/claude-code-produced-html-beginner/631503
  - Failure: a beginner asked Claude for code, got a full HTML document, and did not know where to put it or whether to delete existing theme code.
  - Fix from replies (summary): "Claude should generate a Shopify Liquid section, not a full HTML page. Create a new .liquid file under Sections, ensure it includes a {% schema %} block, then add it to a new template and assign the page to that template." For small elements, use a Custom Liquid section. Replies warn: "avoid deleting theme code unless fully understood" and to "instruct AI specifically to create a Shopify section, block, or fragment."
  - EXCERPT.

### Invalid or missing schema / section not appearing in editor

- **Shopify Community** (multiple threads surfaced by "reddit chatgpt liquid section schema error"), e.g. https://community.shopify.com/t/liquid-error-sections-main-product-line-2261/411971
  - Failure (summary): ChatGPT-generated code added `{% render 'product-schema' %}` pointing at a snippet that does not exist in the theme. Fix: remove the render tag or create the missing snippet. EXCERPT.
- **Shopify Community**, "Theme Development: Liquid Syntax Error: Unknown Tag 'Schema'", https://community.shopify.com/t/theme-development-liquid-syntax-error-unknown-tag-schema/132813
  - Failure: `{% schema %}` placed in a template file instead of sections/. Not AI-attributed in the excerpt. Likely older than 12 months (low topic ID). FLAG: possibly stale. EXCERPT.
- **Medium** (not Reddit), "Help! I made a custom section in Shopify, but now it's not showing in the Theme Editor UI", https://medium.com/@Cavlemasters/help-i-made-a-custom-section-in-shopify-but-now-its-not-showing-in-the-theme-editor-ui-9552060b57da
  - Mechanism (summary): "Without at least one preset, Shopify won't display the section in the Theme Editor's 'Add section' interface." EXCERPT.

### Hallucinated Liquid filters

- **DEV Community** (not Reddit), "The Liquid you lint isn't the Liquid Shopify runs", https://dev.to/iamrobindhiman/the-liquid-you-lint-isnt-the-liquid-shopify-runs-5bhp
  - Summary: theme check can flag filters "that an AI assistant hallucinated into a template that don't exist." EXCERPT. Title suggests the article's real point is that linting passes are not a guarantee; needs a full read.

### CSS leaking / mobile breakage in AI-generated sections

- **Shopify Community**, "Small CSS fix needed for custom AI-generated section (mobile clipping, carousel dots)", https://community.shopify.com/t/small-css-fix-needed-for-custom-ai-generated-section-mobile-clipping-carousel-dots/615944
  - Failure (summary): on mobile, "the left panel content is clipped at the top," likely from `max-height` or `overflow: hidden` on the wrapper; carousel dots sit on top of the product title (absolute positioning).
  - Fix (summary): at `max-width: 749px`, override `max-height` and `overflow: hidden`; put dots in normal flow below the title with at least an 8px gap; replace example selectors with the section's real class names. EXCERPT.
- **Shopify Community**, "Overlapping issue with AI-generated section", https://community.shopify.com/t/overlapping-issue-with-ai-generated-section/621122
  - Failure (summary): Horizon theme, an AI-generated custom sticky header (not the native header); on scroll, page content rendered above the header.
  - Fix (summary): add `{ z-index: 3; }` in the section's Custom CSS, or `.shopify-section:has([class^="ai-sticky-header"]) { z-index:3; }` in theme CSS. Poster confirmed it worked. EXCERPT.

### JS that does not integrate with the theme (silent functional failure)

- **Shopify Community**, "Add to Cart Buttons Not working on Ai Generated Theme Section Blocks", https://community.shopify.com/t/add-to-cart-buttons-not-working-on-ai-generated-theme-section-blocks/629483
  - Failure (summary): items from an AI-generated (Sidekick) block "do add to cart but don't reflect until you refresh the page," on both Horizon and Dawn.
  - Mechanism (summary): the block posts to the cart but does not fire the cart-drawer / cart-count refresh event the theme expects after AJAX add-to-cart; "adding to cart and updating the cart count bubble/cart drawer are 2 separate tasks."
  - Fix: dispatch the theme's cart-update event or update the cart count element after the add. EXCERPT.
  - Related: "Add to cart buttons not working", https://community.shopify.com/t/add-to-cart-buttons-not-working/629768 (content not retrieved).

### Theme updates removing AI-generated customizations

- **shopify.dev forum**, "AI generated sections and upgrades", https://community.shopify.dev/t/ai-generated-sections-and-upgrades/19457
  - Claim (summary): "upgrading the theme will remove those sections as they are considered custom code." Proposal: let merchants choose which sections, snippets and blocks to keep on upgrade. Shopify-side reply (summary) points to docs saying the Shopify Magic generated block is self-contained and the theme can still be updated. Conflict between these two positions is unresolved in the excerpt. EXCERPT.
- **Shopify Community**, "Updating Dawn theme removes custom liquid from template", https://community.shopify.com/t/updating-dawn-theme-removes-custom-liquid-from-template/324306 (content not retrieved; not AI-specific).

### Editing live theme / no rollback / CLI overwrites

- **Shopify Community**, "Shopify CLI: Pushing a theme overwrites settings and section data", https://community.shopify.com/t/shopify-cli-pushing-a-theme-overwrites-settings-and-section-data/54313 and GitHub Shopify/shopify-cli issue #2467 (`config/settings_data.json` overwritten on theme push).
  - Summary: `shopify theme push` overwrites `settings_data.json` and removes merchant-added sections; customizer work does not round-trip. Fixes: pull before push, `.shopifyignore` for settings_data.json, push to a separate dev theme. Not AI-specific, but this is the exact mechanism by which an agent running `theme push` wipes merchant edits. Old (CLI 2.x era). FLAG: older than 12 months. EXCERPT.

### Sidekick cannot verify what it set up

- **shopify.dev forum**, "Sidekick Should Verify Theme App Embed & Block/Section Placement - Not Just Guide", https://community.shopify.dev/t/sidekick-should-verify-theme-app-embed-block-section-placement-not-just-guide/36456
  - Claim (summary): "Sidekick can guide merchants through this process, but has no mechanism to verify completion." Named failure cases: embed enabled on a duplicate theme instead of live, forgetting to click Save, embed "disabled silently after a theme update." "No API exists to query placement state." EXCERPT.

### Undocumented AI code becoming unmaintainable

- **Substack** (not Reddit), "Using AI to customise your store (without breaking it later)", https://seotldr.substack.com/p/ai-shopify-theme-customisation
  - Claim (summary): ChatGPT code pasted into a theme "works until it doesn't, usually appearing months later," and nobody can say what changed. Also: "ChatGPT is extremely confident, even when it's wrong," and OS 2.0 structures postdate some training data. Fix: per-project AI context (theme version, docs links, scope, guardrails), test on a duplicate theme, annotate every AI change with name, date and purpose. EXCERPT.

## C. Failure modes with no evidence found

Nothing Reddit-sourced and nothing usable from substitutes for: hardcoded content (vs settings), accessibility, performance regressions specifically from AI code, AI overwriting working code / scope creep in a Shopify context, CLAUDE.md for Shopify, Shopify Dev MCP experience reports. One vendor blog (weaverse.io) asserts that "on Reddit, developers are already building custom Shopify MCP servers" without links; not usable as evidence.

## Queries run (37 WebSearch calls, 3 refused by the API, plus fetch probes)

1. reddit claude code shopify theme broke
2. reddit chatgpt liquid section schema error shopify
3. reddit AI generated shopify section not showing theme editor
4. claude code shopify theme (allowed_domains reddit.com) : blocked, API 400
5. chatgpt shopify liquid section broke theme (allowed_domains reddit.com) : blocked
6. vibe coding shopify store (allowed_domains reddit.com) : blocked
7. r/shopify claude code custom section liquid
8. reddit vibe coding shopify theme
9. reddit claude code overwrote my code
10. reddit claude code said it fixed but didn't
11. "reddit.com/r/shopify" AI liquid code ChatGPT
12. reddit Invalid schema shopify section setting type is invalid
13. reddit shopify app conflict custom javascript theme
14. reddit claude code CLAUDE.md shopify
15. reddit shopify dev mcp claude cursor theme
16. reddit shopify custom liquid AI broke my theme
17. reddit shopify sidekick generate section theme block review
18. reddit shopify theme update lost custom code sections
19. "r/ClaudeAI" OR "r/ClaudeCode" shopify liquid theme
20. "r/shopify" thread ChatGPT code theme broke store owner
21. reddit cursor shopify theme development liquid hallucinated filter
22. reddit r/webdev AI generated code hardcoded content not editable client CMS
23. reddit AI shopify section css breaks other sections mobile layout
24. reddit shopify store slow after adding custom code AI pagespeed
25. reddit claude code ignores CLAUDE.md instructions deleted files
26. reddit shopify theme pull push live theme overwritten shopify cli customizer settings lost
27. reddit r/ShopifyeCommerce ChatGPT custom section
28. reddit vibecoding shopify app claude lovable store
29. "Small CSS fix needed for custom AI-generated section" shopify community
30. "Claude code produced HTML" shopify community beginner
31. "Sidekick should verify theme app embed" shopify.dev
32. Claude Code "lie about the changes it made to code" github issue reddit
33. "Claude has been lying to me instead of generating code and it makes my head hurt"
34. "Overlapping issue with AI-generated section" shopify
35. reddit shopify "generate with AI" theme block sidekick bad results hardcoded
36. shopify community AI generated block "add to cart" button not working sidekick
37. "AI generated sections and upgrades" shopify developer community

Fetch probes (all blocked): www.reddit.com search, old.reddit.com search, reddit JSON via curl, api.pullpush.io, arctic-shift.photon-reddit.com, community.shopify.com (2 threads), community.shopify.dev (1 thread), alphaguruai.substack.com.
