# Companion for CCMCy-xGRkk: Fudge written guide

- URL: https://www.fudge.ai/guides/shopify-ai-toolkit-claude-code-setup (page says last updated 14 Sept 2026)
- Fetched: 2026-10-03 with curl (browser UA), HTML stripped to text

Product Store Builder Page Builder Store Editor All Features What’s new 

 Resources Customer Stories Blog Our Story Free Tools Guides 

 Partners Partner with Fudge Affiliate Program Find an Expert 

 Pricing 

 Start free trial Start trial 
 en English Deutsch Français 

 Menu 
 Product 
 Store Builder Page Builder Store Editor All Features What’s new 
 Resources 
 Customer Stories Blog Our Story Free Tools Guides 
 Partners 
 Partner with Fudge Affiliate Program Find an Expert 
 Pricing Language 
 English Deutsch Français 

 Start free trial 

 Guides 
 Shopify Ai Toolkit Claude Code Setup 

 How to Set Up Claude Code for Shopify (2026) 
 Last updated 14 Sept 2026 
 •
 Expert reviewed 
 •
 5 min read 

 Jacques Blom 
 CTO at Fudge. 

 On this page
 Connect Claude to Shopify: which path do you need? Why you can trust us Prerequisites Installation: plugin method (recommended) Step 1: Install the plugin Step 2: Verify installation Alternative: manual skills installation Install all skills Install a specific skill Shopify MCP + Claude Code: direct server setup Telemetry and code transmission Connecting to your store Authentication Scope selection What you can do with Claude Code + Shopify Validated GraphQL development Theme development Hydrogen storefront development Store operations Metafield management Functions and extensions Best practices Always query before mutating Be specific with mutations Push themes as unpublished One resource at a time for critical changes Keep your own backups Limitations Where Fudge fits Quick reference Summary 

Key takeaways

The plugin method is the fastest path and auto-updates. Two commands to install.

Manual skills installation works but doesn’t auto-update. Bundled schemas drift from the live platform over time.

Set OPT_OUT_INSTRUMENTATION=true before your first validation if you’re working with proprietary code. Validation payloads include your code by default.

Store operations execute immediately on your live store. There is no draft step.

Always query current state before running mutations. The toolkit has no undo.

Claude Code is one of the primary AI coding tools supported by the Shopify AI Toolkit. Once connected, your Claude Code session gets access to current Shopify documentation, code validation against bundled API schemas, and the ability to execute store operations through the Shopify CLI.

This guide covers setup and what to know. For the full breakdown of what the toolkit does, how it works, and the governance risks around store execution, see our Shopify AI Toolkit overview.

Connect Claude to Shopify: which path do you need?

“Connect Claude to Shopify” means different things depending on who’s connecting:

Merchants (no code): the official Shopify connector for Claude. Shopify ships a connector for Claude that you install from Claude’s connector directory - it redirects to your Shopify admin to approve access, with no App Store install involved. Once connected, Claude on the web or desktop can create and update products, look up orders (read-only), pull analytics with tables and charts, and manage collections, inventory, pages, and percentage-off discount codes. It can’t edit or publish themes, change store settings, or process refunds - so it’s an admin assistant, not a storefront editor. (Inside the admin, Shopify’s own assistant for this territory is Shopify Sidekick.) For AI changes to the storefront itself, with drafts and previews, that’s what Fudge does.

Developers: Claude Code + the Shopify AI Toolkit. The rest of this guide. This path gives Claude validated access to Shopify’s APIs, docs, and CLI - the right choice when you’re writing theme code, apps, or automation.

Shopping agents: storefront endpoints. Every Shopify store also exposes agent-facing storefront endpoints that AI shopping assistants use to browse catalogues and build carts. Nothing to set up here as a merchant - see our piece on Shopify’s Universal Commerce Protocol for what it means for your store.

Why you can trust us

Jacques has over 15 years of development experience and has worked with hundreds of Shopify stores. We built Fudge - an AI-native Shopify page builder and store editor with a 4.9 rating and a Built for Shopify badge. We use these tools daily.

Prerequisites

Claude Code installed and working

Node.js 18 or higher (node --version to check)

Shopify CLI installed (needed for store operations)

A Shopify store to connect to (only required for store operations - not needed for documentation search and code validation)

Installation: plugin method (recommended)

The plugin method is the fastest path and auto-updates whenever Shopify releases new capabilities.

Prefer to follow along visually? Watch the full plugin installation walkthrough:

Step 1: Install the plugin

Run this from your terminal (Shopify’s currently documented command, verified September 2026):

claude plugin install shopify-ai-toolkit@claude-plugins-official

This installs all available agent skills automatically. Our video shows the earlier two-step /plugin marketplace add Shopify/shopify-ai-toolkit flow from April 2026; the one-liner above is the path Shopify’s docs now document.

Step 2: Verify installation

Ask Claude something Shopify-specific to confirm the toolkit is active:

What's the correct GraphQL mutation to update a product's title in the Shopify Admin API?

If the toolkit is working, Claude will search current Shopify documentation and return a validated query rather than guessing from its training data.

Alternative: manual skills installation

If you prefer to install skills manually (e.g., you only need specific capabilities):

Install all skills

npx skills add Shopify/shopify-ai-toolkit

Install a specific skill

npx skills add Shopify/shopify-ai-toolkit --skill shopify-admin

Manually installed skills don’t auto-update. You’ll need to re-run the install command periodically to stay current with Shopify’s API changes. Over time, the bundled schemas will drift from the live platform.

Shopify MCP + Claude Code: direct server setup

For direct MCP integration without the plugin, add Shopify’s Dev MCP server to Claude Code with one command:

claude mcp add --transport stdio shopify-dev-mcp -- npx -y @shopify/dev-mcp@latest

The server runs locally but makes network calls to Shopify endpoints for documentation search. Authentication depends on which MCP server you’re connecting to - Dev MCP for docs doesn’t require store auth; store operations do.

Refer to the Shopify AI Toolkit docs for configuration format and options.

Telemetry and code transmission

Before you start validating code, know this: both validate.mjs and search_docs.mjs send usage payloads to Shopify’s servers by default.

The SKILL.md files describe this as “anonymized validation results (pass/fail and skill name).” However, the actual validation payload includes the code being validated - your GraphQL queries, Liquid templates, and other code you run through the validator.

To opt out, set this environment variable:

export OPT_OUT_INSTRUMENTATION=true

If you’re working with proprietary code, client code, or anything you don’t want transmitted to Shopify’s endpoints, set this before your first validation.

Connecting to your store

To execute operations on a live store (not just generate and validate code), you need to authenticate through the Shopify CLI.

Authentication

The toolkit handles this automatically when you request a store operation, but the underlying command is:

shopify store auth --store yourstore.myshopify.com --scopes write_products,read_products

This prompts you to authorize access through the Shopify admin.

Scope selection

The toolkit’s validation script detects the minimum required OAuth scopes for each operation. Common scopes:

OperationScope
Read productsread_products
Update productswrite_products
Read inventoryread_inventory
Adjust inventorywrite_inventory
Read ordersread_orders
Read customersread_customers

Stick to the minimum scopes needed. write_products gives access to ALL product write operations, not just the specific mutation you’re running.

What you can do with Claude Code + Shopify

Validated GraphQL development

Ask Claude to write Shopify GraphQL queries and mutations. The toolkit validates them against the bundled API schema before you use them.

Claude will search current Shopify Admin API docs, generate the query, validate it against the bundled schema, and report any issues or required scopes. No more hallucinated fields or deprecated patterns.

Theme development

Work with Liquid templates with validation against Shopify’s theme rules. The toolkit validates schemas against JSON definitions and enforces LiquidDoc headers.

Related: adding custom Liquid logic in Shopify.

Hydrogen storefront development

Build headless storefronts with validated React components and correct imports from @shopify/hydrogen.

Store operations

Execute operations directly on your connected store. Claude generates the mutation, validates it, authenticates with your store, and executes it via shopify store execute --allow-mutations.

The change is live immediately. There is no draft step. See the risks section in our main guide for why this matters.

Metafield management

Extend your store’s data model with metafield definitions. The toolkit uses TOML for metafield definitions and knows the difference between app-owned and merchant-owned data.

Related: adding metafields to Shopify products.

Functions and extensions

Build backend customization - discounts, cart validation, delivery rules - and scaffold UI extensions with Polaris components. The Functions skill knows that Shopify Functions must be pure (no network calls, no filesystem, no randomness).

Related: adding custom JavaScript in Shopify.

Best practices

Always query before mutating

Before updating anything, read the current state first:

Show me the current title, description, and SEO fields for the product with handle "classic-tee"

This gives you a baseline and helps prevent unintended overwrites.

Be specific with mutations

Vague prompts lead to broad mutations. Instead of “Optimize my products for SEO,” be specific:

Update ONLY the meta description for the product with handle "classic-tee" to "Shop the Classic Tee - premium cotton, 5 colors, free shipping over $50"

Push themes as unpublished

When pushing theme changes, always push as unpublished first. The toolkit supports shopify theme push --unpublished, but doesn’t enforce it by default. Make it a habit.

One resource at a time for critical changes

For important updates, run them one product at a time rather than in bulk. This limits blast radius if something goes wrong.

Keep your own backups

The toolkit has no undo. Before running mutations that update existing content, export or note down the current values.

Limitations

These are structural to the toolkit, not Claude Code-specific. For the full risk analysis, see our Shopify AI Toolkit overview.

No draft mode - Store mutations execute on your live store immediately

No preview - You can’t see what changes will look like before they happen

No undo/rollback - Changes are permanent once executed

No audit trail - No toolkit-level record of what was changed

Broad scopes - OAuth permissions apply to entire resource types, not individual items

Code sent to Shopify - Validation payloads include your code by default (opt out with OPT_OUT_INSTRUMENTATION=true)

Manual skills decay - If you installed skills manually, they won’t auto-update

Where Fudge fits

The AI Toolkit makes you faster at writing Shopify code, schemas, themes, Hydrogen, custom apps. It is not the right surface for the merch team running daily ops, and it doesn’t add the workflow that real store changes need: drafts, previews, approvals, version history, scheduled launches, rollbacks. Code lives in git; store state doesn’t. That’s the gap Fudge fills, an AI-native Shopify editor with drafts, previews, and rollback for the people on your team who shouldn’t be writing GraphQL.

Quick reference

TaskCommand
Install pluginclaude plugin install shopify-ai-toolkit@claude-plugins-official
Add Dev MCP directlyclaude mcp add --transport stdio shopify-dev-mcp -- npx -y @shopify/dev-mcp@latest
Install all skills manuallynpx skills add Shopify/shopify-ai-toolkit
Install one skillnpx skills add Shopify/shopify-ai-toolkit --skill shopify-admin
Auth with storeshopify store auth --store domain --scopes list
Opt out of telemetryexport OPT_OUT_INSTRUMENTATION=true
Check Node versionnode --version (need 18+)

Summary

The Shopify AI Toolkit turns Claude Code into a Shopify-aware development environment. The documentation search and code validation make it worth installing for any Shopify developer - the accuracy loop alone saves time.

For development work - app building, theme creation, Hydrogen storefronts - it’s a clear productivity upgrade. For store operations, the governance gaps apply: no drafts, no preview, no undo, and code telemetry enabled by default. Be deliberate about what you enable.

For the full picture on risks and governance, read our Shopify AI Toolkit overview. For setup on other platforms, see our Cursor guide and OpenAI Codex guide.

We last re-verified the commands and capabilities on this page against Shopify’s current docs in September 2026.

FAQ
 Should I install the Shopify AI Toolkit via the plugin or manually?
Plugin if you want the simplest setup and auto-updates as Shopify releases new capabilities. Manual install if you only need specific skills (e.g., just shopify-admin for backend work) or want explicit version control. Plugin is the recommended default for most Claude Code users.

What if my Node version is below 18?
Upgrade Node before installing the toolkit, the validation scripts use modern Node features unavailable in older versions. Use nvm (Node Version Manager) to install Node 20 LTS without disrupting other projects. The toolkit may install but produce confusing runtime errors on older Node.

Does the toolkit work without authenticating to a Shopify store?
Yes for documentation search and code validation, those don't require store auth. Store operations (executing mutations against a live store) require authentication. You can use the toolkit purely for development reference without ever connecting a store.

Can I use the toolkit on a Shopify development store?
Yes, and recommended for testing mutations safely. Connect to a development store first, run the operations there to verify they behave as expected, then re-auth to production. Development stores are free to create and let you experiment without affecting real data.

Why does the toolkit send my code to Shopify by default?
The validation payloads include the code being checked so Shopify can validate against current schemas server-side. Documented as "anonymized validation results" but the payload includes your queries/code. Set OPT_OUT_INSTRUMENTATION=true to disable for proprietary or client work.

 Edit your Shopify storefront without code.

 Try Fudge for Free 

 See how Fudge edits themes 
 4.9 

 Jacques Blom 
 CTO at Fudge. 

 Jacques is CTO at Fudge and has been coding since age 13 and building on Shopify for 15+ years. He previously led engineering at several YC-backed startups before joining Fudge to architect its AI Page Builder and Store Editor, systems that have generated 22,000+ production pages for over 400 Shopify merchants. He writes about Shopify performance, theme architecture, and applying LLMs safely to production Liquid code. 

 Build pages & edit your store just by typing what you want 

 Build on-brand pages for every campaign. 

 Make any change you want to your store. 

 Say goodbye to templates & expensive developers. 

 Try Fudge for Free 
 Rated 4.9 • Loved by 100s 

You might also be interested in

 AI-Generated Metafields: A Practical Shopify Workflow 
 AI Shopify metafields workflow: define namespace/key/type, generate specs and care copy with Claude, validate types, and push via metafieldsSet. 
 How to Set Up the Shopify AI Toolkit with OpenAI Codex 
 Set up Shopify AI Toolkit with OpenAI Codex. Covers plugin install, MCP config, store auth, telemetry opt-out, and first validated query. 
 Shopify Flow AI Assistant Prompts: A Practical Guide (2026) 
 Practical prompts for Shopify Flow's AI assistant. Tagging, notifications, inventory, segments, B2B, fraud, and tips for building reliable workflows. 

 --> Product Store Builder AI Page Builder AI Store Editor All Features What’s New Pricing 
 About 
 Our Story Customer Stories Contact Us Free Tools AI Readiness Checker Catalog Data Audit AI Store Builder Website Redesign 
 Guides Create a Landing Page Customize a Product Page Speed Up Your Theme Create a Collection Page Add Structured Data Lazy Load Images All Guides 
 Compare 
 Fudge AI vs PageFly Fudge AI vs Instant Fudge AI vs Shogun Fudge AI vs GemPages Fudge AI vs Replo 
 Partners Partner with Fudge Affiliate Program Find an Expert 
 Utility 
 Privacy Policy Terms of Service Affiliate Program Terms 

 © 2026 Fudge IT, Inc 
 · All rights reserved
