---
name: store-cro-audit
description: Visually audit the live peculiarpeopleco.com storefront for conversion and credibility problems by driving a real browser, screenshotting every page state on desktop and mobile, and scoring 68 checkable rules with a screenshot as evidence for every failure. Produces a ranked report separating "makes the store look established" fixes from "removes friction" fixes. Use when Evan asks to audit the store, review the site, check the storefront, run a CRO audit, find out why the site does not look professional or trustworthy, or check how the store looks on mobile. Read only, so it proposes changes and never edits the store, a theme, a product, or any copy.
---

# Store CRO audit

Audits the live storefront against `references/rules.md`, 68 rules derived from
`research/CRO-FINDINGS.md` in this project.

## Non-negotiable constraints

1. **Read only.** Never edit the live store, a theme, a product, a collection, or any copy.
   Shopify tools are for *reading* which products exist. Never call a mutation. This skill
   proposes; Evan decides.
2. **Never complete a checkout.** Reaching the checkout entry screen and screenshotting it
   is the end of the journey. Never type payment details, never submit a form with real
   data, never place a test order.
3. **Look, do not read the markup.** Findings come from rendered pixels. Fetching HTML and
   reasoning about the DOM is explicitly not enough and does not satisfy this skill: it
   cannot see contrast, hierarchy, crowding, whether a button is visually dominant, or
   whether a mockup looks cheap, which is most of what this audit is for. `read_page` is
   allowed as a supplement to confirm what an element is, never as a substitute for looking.
4. **No finding without an image.** Every FAIL names the screenshot file that proves it. A
   finding with no evidence file does not go in the report.
5. **If the browser will not run, stop.** If Playwright cannot launch and the in-app browser
   tools are unavailable, say so plainly and stop. Do not fall back to fetching HTML and do
   not produce a report from markup. A markup-based report would look like an audit and be
   worthless.
6. **No em dashes.** Anywhere in the report. House rule, absolute.
7. **Any suggested customer-facing copy is a draft only.** Label it
   `DRAFT COPY - needs humanizer + structural-humanizer before it ships`. Never present it
   as ready.
8. **Never quote a conversion statistic.** The source research discarded every number; see
   the header of `references/rules.md`.

## Before starting

Read, in this order:

1. `BRAND.md` (project root). Voice, guardrails, open decisions, and the print-on-demand
   constraints. Section 19 open decisions are open: do not report an open question as a defect.
2. `.claude/skills/store-cro-audit/references/rules.md`. The rules, their basis labels, and
   which are blocked at zero orders.

## Workflow

### Step 1: pick real products

Use the Shopify MCP tools (`search_products`, `get-product`) to list live products and pick
**at least two** product pages that differ in a way that matters:

- one tee and one fleece item, since the garment lines differ, and
- ideally the Temple Art File as well, since the one digital product has a different
  buying flow (no size or colour choice). The personalisable date tee is paused and not
  live, so do not look for it.

Never guess a product URL. Take the real handle from Shopify. Also take the real collection
handle; the store has seven collections (all temples, one per garment line, Utah, Idaho,
California) alongside the Easify Temple dropdown, so confirm which collection URL resolves.

### Step 2: capture

```bash
node .claude/skills/store-cro-audit/scripts/capture.js \
  --base https://peculiarpeopleco.com \
  --out audits/<YYYY-MM-DD> \
  --collection /collections/<handle> \
  --pdp /products/<handle-1> --pdp /products/<handle-2> \
  --search temple
```

Requires Playwright with Chromium (`npx playwright install chromium`). If `playwright` is
not resolvable from the working directory, set `PW_PATH` to its module path.

The script runs the same journey twice, desktop (1440x900) and mobile (iPhone 13 emulation,
which reloads with a mobile user agent so load-time device logic re-runs), and saves PNGs
into `audits/<date>/shots/` plus a `manifest.json` recording what was captured and what
failed.

It covers: home fold and full page, nav opened, search results, collection fold and full
page, desktop card hover, each product page fold and full page, a colour change, a size
change, the page scrolled far enough to test for a sticky add-to-cart, add to cart, the cart
drawer, the cart page, the checkout entry screen, and the footer.

**It deliberately does not dismiss popups or cookie banners.** Those are findings. The first
screenshot must show what a real first-time visitor actually sees.

### Step 3: look at every screenshot

`Read` every PNG the script saved. All of them, both viewports. This is the audit. The
screenshots are not illustrations for a report written from assumptions; they are the only
evidence there is.

Check `manifest.json` for failures. A step that failed is itself informative: if the script
could not find an add-to-cart button, or the checkout button, that is worth investigating
live rather than silently omitting.

### Step 4: verify live where a screenshot is ambiguous

Use the in-app browser for anything a static PNG cannot settle:

- `mcp__Claude_Browser__navigate` then `computer` with `action: "screenshot"` to see a state
  interactively.
- `computer` with `left_click` / `scroll` / `hover` to test behaviour, such as whether a
  sticky bar actually appears or whether a card has a hover state.
- `resize_window` with `preset: "mobile"`, then reload, to re-check a mobile state.
- `read_page` only to confirm what an element is, for example whether a control is a real
  `<select>` or styled buttons, after you have already looked at it.

Reset with `resize_window` `preset: "desktop"` when finished.

### Step 5: score every rule

Work through all 68 rules in `references/rules.md`. Each gets exactly one of:

- **PASS**
- **FAIL** plus the screenshot filename that proves it
- **N/A - blocked**, for rules needing reviews, ratings, customer photos or press coverage.
  Say what would unblock it. Blocked is not failure; scoring it as failure produces a report
  that reads as damning and cannot be acted on.
- **N/A - not applicable**, where the rule does not fit this store's structure. Say why.

Carry the basis label through. When a **SINGLE** source rule drives a finding, say in the
report that it rests on one unverified opinion and name the source.

### Step 6: write the report

Write `audits/<YYYY-MM-DD>/REPORT.md`. Structure:

1. **What was checked.** Pages, both viewports, the date, and anything the capture failed to
   reach. State plainly that the source is twelve YouTube videos, not research, and that
   SINGLE-source lines are unverified.
2. **Makes the store look established.** Findings about credibility and perceived quality.
3. **Removes friction.** Findings about the mechanics of buying.

   These are different problems with different fixes and they must not be mixed. A visitor
   who does not trust the store never reaches the friction.
4. **Blocked, and what would unblock it.**
5. **Full rule scorecard**, all 68, as a table.

Rank findings within sections 2 and 3 by expected impact against effort. Every finding names
the page, the rule id, the evidence image, and a specific fix. Not "improve the hero" but
what to change and to what.

Do not pad. A rule that passes needs no paragraph; the scorecard covers it.

## Judgment notes

- **Do not report an open decision as a defect.** BRAND.md section 19 lists genuinely open
  questions, including the beachhead. The garment blanks are decided (14 September 2026). Navigation organised by temple
  rather than by shopper intent is an open question, not a bug.
- **Distinguish blocked from broken.** Most social-proof rules fail because the store has
  never had an order. That is a state, not a mistake.
- **Weight the two rules that carry the most for this store.** L1, consistent photography
  across the grid, is the finding most likely to move perceived credibility, and it is
  enforceable in the generator pipeline. P5, stating the size shown in the image, is the
  only part of the fit research that needs no customers.
- **Say when the audit cannot answer something.** No source in the underlying research
  reached a real checkout, so checkout findings rest on a 2014 study and on what is visible
  on screen. Do not overstate them.
