URL: https://monkeyman.agency/insights/building-a-shopify-theme-with-claude-code/
Final URL: https://monkeyman.agency/insights/building-a-shopify-theme-with-claude-code/
HTTP status: 200
Fetched: 2026-10-03 via curl
Meta: {"description": "How a Shopify agency runs an AI coding agent against real client themes in 2026. Setup, prompts, guardrails, and what it still cannot do safely.", "og:title": "Claude Code on Shopify Themes · 2026 Agency Playbook | Monkeyman Agency", "og:description": "How a Shopify agency runs an AI coding agent against real client themes in 2026. Setup, prompts, guardrails, and what it still cannot do safely.", "twitter:description": "How a Shopify agency runs an AI coding agent against real client themes in 2026. Setup, prompts, guardrails, and what it still cannot do safely."}
Schema dates: 2026-05-26T00:00:00.000Z

---

Skip to content 
 
monkeyman.agency 
 Services 

Build

- Setup → 

- Theme Customization → 

- Migration → 

Redesign

- Redesign → 

- Speed → 

Scale

- CRO → 

- Multi-Region → 

- App Dev → 

- Maintenance → 

- Store Manager → 

- Hire a Developer → 

Empire

- Plus → 

- Headless → 

All services → 
Free audit

Migrations 

Hosted SaaS

- BigCommerce → 

- Volusion → 

- PinnacleCart → 

Open source

- WooCommerce → 

- Magento → 

- PrestaShop → 

- OpenCart → 

- X-Cart → 

- Zen Cart → 

Site builders

- Squarespace → 

- Wix → 

- GoDaddy → 

- Webflow → 

All migrations → 
Free audit

Work Industries Insights Contact 
Get a free store audit
→ 

monkeyman.agency 

- 
 Services 

- Setup 

- Theme Customization 

- Migration 

- Redesign 

- Speed 

- CRO 

- Multi-Region 

- App Dev 

- Maintenance 

- Store Manager 

- Hire a Developer 

- Plus 

- Headless 

- 
 Migrations 

- BigCommerce 

- Volusion 

- PinnacleCart 

- WooCommerce 

- Magento 

- PrestaShop 

- OpenCart 

- X-Cart 

- Zen Cart 

- Squarespace 

- Wix 

- GoDaddy 

- Webflow 

- 
 Work 

- 
 Industries 

- 
 Insights 

- 
 Contact 

Get a free store audit
→ 

industry 
# Building a Shopify Theme with Claude Code: A 2026 Agency Workflow 
 
 What it actually looks like when a Shopify agency moves a theme build into an AI coding agent. The setup, prompts, guardrails, and where it still loses to a senior dev. 
 
 Kapil Garg · May 26, 2026 · 9 min read 

## 
Key takeaways

- A scaffolded theme repo plus an AI coding agent will produce production-grade Liquid for metafield-driven sections, but only if the dev store, theme-check config and metaobject schema are wired up first. 

- Three prompting patterns work on real client themes: spec-then-build, paired editing on a single section, and audit-and-refactor against an existing Liquid file. 

- Guardrails matter more than prompts. A clean git branch, theme-check in CI, a staging dev store with real data, and a human PR review still catch about one in eight changes. 

- Per-outcome pricing fits this workflow better than hourly billing. Senior devs are paid for taste and risk-bearing, not typing. 

- Where it still loses: anything that requires reading the Shopify admin, anything with cross-app dependencies, and any change to checkout extensibility or Shop Pay flows. 

Marco runs a six-developer Shopify agency in Lisbon. Late March, he sent us a screenshot of his terminal at 11pm. He had asked an AI coding agent to add a metafield-driven shipping-cutoff badge to a 4,800-SKU jewelry client’s product grid. Twelve minutes later, it was done. Theme-check clean, Liquid syntax correct, the badge wired to a metaobject he had not even named yet. “I just sat there,” he told us the next morning. “Is this real?”

That’s the conversation we have on at least one onboarding call a week now. Sometimes the dev is excited. Sometimes spooked. Mostly they want to know what we actually do with it before billing a client.

So here’s what we run.

## The afternoon Marco emailed us the screenshot

Marco wasn’t experimenting. He was three days behind on a spring delivery and the badge was a half-day of Liquid he didn’t have. He pointed the agent at a fresh branch of the theme repo, gave it a paragraph of context (the jewelry brand, the metaobject he was about to create, the existing product card snippet), and asked for a render-safe badge that respected delivery zones.

The diff came back with the metaobject definition in a comment block, the Liquid in snippets/product-card-badge.liquid, the schema entry in sections/main-product-grid.liquid, and a fallback for the empty case. Theme-check passed first run.

The piece that surprised him was not the speed. It was that the agent had matched the existing card snippet’s indentation, used the same assign naming the previous dev had used, and quoted the metaobject keys the way Shop’s GraphQL admin returns them. The output looked like a junior who had been on the project for two months.

This is the new floor. And it changes the math on what an agency dev is for.

## What we set up before we’d touch a client theme

Speed without guardrails is how you push a broken cart.liquid to production at 9pm Friday. We’ve run this setup on eleven client themes in the last sixty days and it’s not negotiable.

The repo is git, not the Shopify online editor. Every theme we own is private, pulled with the Shopify CLI, branched per ticket. The agent works against the local working tree. The online editor is read-only on these stores after kickoff.

A development store gets cloned from live with realistic data: a minimum of 200 products in the categories we’ll touch, three or four representative collections, the actual metaobject and metafield definitions, and a Recharge or Shop Subscriptions sandbox if the merchant runs subscriptions. Empty dev stores hide a lot of bugs.

Theme-check config sits at the repo root with the merchant’s strictness rules baked in. We run it on every save and in CI. The agent can ask theme-check what’s broken, but it can’t disable rules without a human approval.

The last piece is a CLAUDE.md at the repo root: the brand, the merchant’s tone, the metaobjects and their keys, the apps installed, the things we never change without a Slack thread. Without the file the agent guesses, and the guesses are mostly fine, but “mostly fine” is what you pay a senior dev to filter.

## Three prompting patterns that produce shippable Liquid

Most agentic-coding prompt advice is generic. On a real theme, three specific patterns produce code we’d actually ship.

Spec-then-build is the slowest and the safest. The dev writes a 6-to-10-line spec for the section, pastes it in, lets the agent draft. The diff lands as one section plus one snippet plus a schema entry, reviewed like a junior PR.

Paired editing on a single section is the most common one. You open the file, the agent has read context, you riff: “add a swatch row under the price, only when the metaobject is populated, match the existing spacing tokens”. This is where Marco lives now. Like having a junior at his shoulder who never gets tired.

Audit-and-refactor is the one we underused for the first month. Point the agent at an old section a previous agency wrote, ask it to flag render-blocking JS, inline styles, forloops that should be paginated. It hands back a list ranked by impact. We had it audit a 3,200-line theme.js last month and it caught seventeen issues a human would have skipped on a first pass.

What doesn’t work: open-ended “make this better” prompts. The agent has no taste without context. It will clean up indentation while ignoring the cart-drawer.js race condition costing the merchant conversions.

## Where the guardrails saved us

Backups, theme-check, PR review. None exciting. All have caught something.

Theme-check in CI is the one we lean on hardest. The Shopify theme-check rules cover most obvious Liquid failures, but the deprecation checks alone have flagged three breaking changes in the last six months that the agent did not know about. The agent reads the report after each commit and is generally good at fixing what it broke. The part it can’t do is decide whether to fix or rewrite. That’s the senior’s call.

The dev-store data is a guardrail too. An agent confidently produced a “buy two, get one free” cart bundle in pure Liquid that worked beautifully with three products in cart and broke at twelve. Realistic test data caught it before staging.

PR review still catches roughly 12 percent of changes by our count over forty PRs. Mostly not bugs. Small things: a margin token that doesn’t match the brand system, a metafield naming convention the agent invented, an alt-text string that needs the merchant’s voice.

And then there are the things the guardrails missed. A header section shipped to staging with a {% if customer.tags contains %} block that worked perfectly except the empty case redirected logged-out users to /account/login. No theme-check rule for that. The PR review caught it because a human knows logged-out users are 78 percent of traffic on that store.

## Where it beats a senior dev, where it costs you a week

A senior dev billing 95 dollars an hour writes a metafield-driven product badge in two and a half hours. Our internal data on twenty-three of these tickets says the AI-assisted version lands in 28 minutes including PR review. That’s an eight-to-one speedup on a class of tickets that was filling our junior queue.

Wireframes-to-section is another big win. Hand the agent a tagged screenshot or a Figma export, the existing token system, the section schema convention, and it produces a working section in one shot. Fourteen of these shipped last quarter.

The losses are real though. Checkout extensibility, where the agent has no safe sandbox access to a Shop Pay flow, is where we still pair a senior dev for the whole session. Anything reading the Shopify admin (custom apps, app extensions, app blocks the agent cannot inspect) the senior has to do. Cross-app flows, like a draft order touching Klaviyo plus Recharge plus a custom shipping rate, the agent hallucinates webhooks that do not exist. We’ve caught three of those before ship. We’re sure we’ve missed others.

So the rule: theme work (sections, snippets, metaobject UI, custom page templates, PDP variants) is agent-first with senior review. Checkout, app extensions, admin integrations stay senior-written.

Work type

Agent-first

Senior reviews

Senior writes

Sections & snippets

yes

required

no

Metaobject UI

yes

required

no

Custom page templates

yes

required

no

Theme refactors

yes

required

no

Checkout extensions

no

n/a

yes

App extensions / blocks

no

n/a

yes

Cross-app integrations

no

n/a

yes

## Pricing the new workflow

Hourly billing for theme work doesn’t survive an eight-to-one speedup. We tried for a month. The client conversation went badly twice. (“You’re billing me four hours for something that took your tool 28 minutes?”) The senior dev felt punished for the speed. We moved off hourly in April.

What we run now is per-outcome pricing for theme tickets and a retainer for senior review hours. A metafield-driven section is a flat 1,400 dollars. A new PDP variant is 1,800. A gift finder is 2,400. A theme migration onto OS 2.0 is a scoped fixed bid based on section count and complexity tier. The senior review retainer is eight hours a month at the merchant’s normal blended rate. Most clients pay it without blinking.

The thing we tell senior devs honestly: you’re getting paid for taste and risk-bearing. Not for typing. If you can’t articulate that, you’ll feel like the workflow is replacing you. It isn’t. It’s paying for the part you were always actually paid for.

## The checklist we run before every session

Quick. Boring. Bills get paid because of it.

We pull the latest from the client repo onto a clean branch. We confirm the dev store has the data we need. We check that theme-check.yml reflects the merchant’s strictness profile. We update CLAUDE.md with anything that has changed since the last session, often something from the Shopify partner changelog. And we draft a ticket spec for the agent, even when the dev would normally just start typing.

The ticket spec is the step junior devs skip and then wonder why the output is generic. Six lines is enough. The agent reads it, the senior reviewer reads it, the merchant reads it later when they ask what changed and why.

If any of the five steps fails, we don’t run the session.

## What we keep telling clients

Marco’s jewelry client got the badge that night. He committed at 11:47pm, pushed it to staging, and the merchant approved it the next morning over coffee. He billed the work at a fixed 1,400 dollars and a half-hour of senior review against the retainer. The merchant didn’t ask how it was built. She asked when the next thing could ship.

That’s the part we keep telling new clients. The badge is the badge. What you’re paying for is the agency knowing which badges to ship and in what order, what they’ll do to PDP conversion, and what to roll back if they don’t.

We also tell them honestly: not every ticket fits. Checkout, payment routing, anything involving Shop Pay, anything touching a custom app stays senior-written and senior-reviewed and billed accordingly. We don’t pretend the agent does work it cannot do.

The number that matters is not “how fast does your agency type”. It is “how fast does the next revenue feature land, and how often do we have to roll it back”. On both, by our data, the AI-assisted workflow is materially better than the old one. And we’ll keep being honest about the parts where it still loses.

## Questions we get every week

Can a non-developer use it on their own theme?
Honestly, no. Not safely. The setup we describe (git, dev store, theme-check, a curated context file) requires a developer’s instincts. A merchant prompting an AI agent directly against a live theme will, within a week, push a broken section.

Does this work with custom themes, or only Dawn-based ones?
Both, with caveats. On a clean Dawn fork the agent has the strongest priors and the highest hit rate. On a deeply customized theme with non-standard naming, you spend more time documenting conventions in CLAUDE.md. On a fully custom Hydrogen storefront the workflow is different again.

What about Shopify’s own AI tools?
Shopify Magic and the admin-side AI features are useful for merchants writing product copy, generating images, and surfacing analytics. They don’t replace the dev workflow we describe. The two layers are complementary.

How do we sell this to a client who hates AI-generated work?
We don’t sell the workflow. We sell the outcomes. If a merchant asks how the badge got built, we say “our senior dev and our coding agent, with a PR review, and theme-check in CI”. Most merchants care about the work shipping and the bugs not shipping.

What’s the next thing changing in 2026?
Probably storefront MCP plus theme tooling getting closer. The agent reading the merchant’s actual store catalog and metaobjects directly, not just the repo. We’re piloting it internally now and will write it up when we have data we trust.

If you want a walk-through of the last three theme builds we shipped this way, including the prompts, the PR diffs and the pricing math, book a 45-minute Shopify agency review with us.

If you want help with this

## The services that fix what this post describes.

The post diagnoses; these sprints solve.

- Build
### Shopify Store Setup

Our Shopify store setup service delivers a clean, conversion-ready store, theme installed, products loaded, payments connected, and ready to take orders.
Learn more→

- Redesign
### Shopify Redesign

A complete redesign focused on the parts that make money, homepage, PDPs, checkout, mobile UX.
Learn more→

- Build
### Shopify Theme Customization

A focused 2-week sprint that turns a stock Shopify theme into a brand-perfect storefront.
Learn more→

Keep reading
 
## 
More field notes.

See all Industry posts → 
 
- industry 
### Vibe Coding Versus Traditional Shopify Development: A 2026 Decision Framework for Agencies 
 
 Vibe coding is reshaping Shopify agency economics. The framework we use to decide when AI-generated code wins, when it loses money, and how to price the work. 
 8 min read →

- industry 
### Is Your Shopify Theme Blocking GPTBot, ClaudeBot and PerplexityBot? Here's How to Check 
 
 Shopify themes silently block AI crawlers more often than you would expect. Here is the 12-point bot audit we run on every onboard, with the exact fixes. 
 10 min read →

- industry 
### How to Add an llms.txt File to Shopify (and What Should Actually Go in It) 
 
 Shopify does not ship llms.txt natively yet. Here is the redirect-or-worker setup we use, the seven sections that earn citations, and a 14-day rollout. 
 9 min read →

Need help with this? 
 
## Send us your store. We'll send back an audit.
 
 Send us your store URL. We'll send back a free audit within 48 hours. 

Name 

 Email 

Store URL 

Phone (optional) 
 🇦🇷 +54 AR 🇦🇺 +61 AU 🇦🇹 +43 AT 🇧🇩 +880 BD 🇧🇪 +32 BE 🇧🇷 +55 BR 🇨🇦 +1 CA 🇨🇱 +56 CL 🇨🇳 +86 CN 🇨🇴 +57 CO 🇨🇿 +420 CZ 🇩🇰 +45 DK 🇪🇬 +20 EG 🇫🇮 +358 FI 🇫🇷 +33 FR 🇩🇪 +49 DE 🇬🇷 +30 GR 🇭🇰 +852 HK 🇭🇺 +36 HU 🇮🇳 +91 IN 🇮🇩 +62 ID 🇮🇪 +353 IE 🇮🇱 +972 IL 🇮🇹 +39 IT 🇯🇵 +81 JP 🇰🇪 +254 KE 🇲🇾 +60 MY 🇲🇽 +52 MX 🇲🇦 +212 MA 🇳🇱 +31 NL 🇳🇿 +64 NZ 🇳🇬 +234 NG 🇳🇴 +47 NO 🇵🇰 +92 PK 🇵🇭 +63 PH 🇵🇱 +48 PL 🇵🇹 +351 PT 🇷🇴 +40 RO 🇷🇺 +7 RU 🇸🇦 +966 SA 🇸🇬 +65 SG 🇿🇦 +27 ZA 🇰🇷 +82 KR 🇪🇸 +34 ES 🇱🇰 +94 LK 🇸🇪 +46 SE 🇨🇭 +41 CH 🇹🇼 +886 TW 🇹🇭 +66 TH 🇹🇷 +90 TR 🇺🇦 +380 UA 🇦🇪 +971 AE 🇬🇧 +44 GB 🇺🇸 +1 US 🇻🇳 +84 VN 

What's the biggest issue? 

Leave this field empty

Get my free audit → 

Almost done. Pick a 30-minute slot below and we'll confirm by email.

Loading scheduler… 

Our embedded scheduler didn't load, your browser may be blocking it.
 You can still book a 30-minute slot here:

Open scheduler in a new tab
→ 

monkeyman.agency 

We build, redesign, and scale Shopify stores designed to evolve.

Get a free store audit
→ 

Build

- Setup 

- Theme Customization 

- Redesign 

- Migration 

Scale

- Speed 

- CRO 

- Multi-Region 

- App Dev 

- Maintenance 

- Store Manager 

- Hire a Developer 

Empire

- Plus 

- Headless 

Company

- About 

- Work 

- Reviews 

- Insights 

- Contact 

Resources

- Best Ecommerce Platform 

- Platform Comparisons 

- Migration Guides 

Locations

- United States 

- Dubai, UAE 

- United Kingdom 

- Germany 

Legal

- Privacy 

- Terms 

Connect

- LinkedIn 

- Email 

From idea to empire.

01 · Idea → 02 · Build → 03 · Launch → 04 · Scale → 05 · Empire 

Working with US · UK · EU · UAE · ANZ 

A brand of APPWRK IT Solutions 
 
© 2026 Monkeyman.agency
 
Built for stores that evolve.
