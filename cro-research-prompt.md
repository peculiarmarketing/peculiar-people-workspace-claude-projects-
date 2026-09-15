# Prompt: CRO video research, then build a visual store-audit skill

Paste everything below the line into a fresh Claude Code session in the
`Claude Projects` folder.

---

I want to run a two-phase job: first research conversion rate optimization for
ecommerce using the YouTube watcher, then turn that research into a reusable
skill that audits my live store visually. Do NOT start phase 2 until I approve
phase 1. Stop and wait at the gate.

My store is peculiarpeopleco.com (Shopify, print-on-demand apparel featuring
Latter-day Saint temple line art). The problem I am solving: the site does not
look professional or established enough to earn trust from a first-time visitor.
Read BRAND.md before you synthesize anything so the recommendations fit the
brand instead of generic DTC advice.

## Phase 1: Research

### 1a. Build the watchlist and show it to me first

Use WebSearch to find 8 to 12 YouTube videos. Do not watch anything yet.
Verify every URL actually resolves and is on topic before you put it on the
list. Never invent a URL or a title.

Split the list roughly like this:

- 4 to 5 on general ecommerce CRO fundamentals: product page structure, above
  the fold, trust signals, social proof placement, cart and checkout friction,
  mobile behavior.
- 3 to 4 that are specifically about clothing and apparel brands: apparel PDPs,
  size and fit information, model and flat-lay photography, collection page
  merchandising, apparel store teardowns and redesigns.
- 2 to 3 on the "looks established vs looks like a dropshipper" problem
  specifically: brand credibility, visual polish, first-impression trust,
  Shopify theme critiques.

Starting points for your search, each of which you must verify exists before
relying on it: Baymard Institute, CXL, Shopify's own channel, Kurt Elster,
Ezra Firestone, Andrew Faris, Sabir Semerkant, Nik Sharma, and the general
"Shopify store teardown" and "ecommerce website review" video genres.

For each candidate give me: title, channel, URL, length, and one line on why it
earns a slot. Flag anything over 25 minutes and tell me which section you would
watch instead of the whole thing. Show me the list and wait for my go-ahead
before watching. This is a real stop.

### 1b. Watch them

Once I approve, use the /watch skill on each video, one at a time.

- Always pass --no-whisper. Transcription stays local, never a paid API.
- Pick the detail mode on purpose: `transcript` for a talking head, `balanced`
  when you need to read what is on screen, `efficient` for a first pass at a
  long screen recording.
- Use --start and --end to watch only the section that matters on long videos.
- Actually Read every frame path the script prints. The screen content in a
  teardown video is the whole point; the transcript alone will miss it.

After each video, append to `research/cro-videos/<slug>.md`:
- source (title, channel, URL, what section you watched)
- the concrete, testable claims it makes, each as an imperative you could check
  on a real page ("above the fold shows price, primary image, and add to cart
  without scrolling") rather than a vibe ("make it feel premium")
- anything apparel-specific called out by name
- what the presenter showed on screen that contradicts what they said

### 1c. Synthesize

Write `research/CRO-FINDINGS.md`. Organize it by page type: home, collection,
product detail page, cart, checkout entry, plus a cross-cutting section for
trust and credibility signals and one for mobile.

Label every claim:
- CONFIRMED: two or more independent videos say it
- SINGLE SOURCE: one video only, keep it but mark it
- CONFLICT: sources disagree, say so and give your read with reasoning

Throw away every specific statistic unless two sources give the same number.
"Adding X lifted conversion 47%" from one guy on YouTube is not evidence.

Then add a section called "Checkable rules" that converts the CONFIRMED and the
strongest SINGLE SOURCE items into a flat list of pass/fail checks a person
could run against a screenshot. That list is the raw material for phase 2, so
write it for that purpose.

Also flag which findings conflict with BRAND.md or with the constraints of
print-on-demand, and set those aside rather than quietly dropping them.

### Gate

Show me the watchlist results, CRO-FINDINGS.md, and the checkable rules list.
Stop. Do not build anything until I say go.

## Phase 2: Build the audit skill

Use the skill-creator skill. Name it `store-cro-audit`, put it in this project's
`.claude/skills/`. Feed it CRO-FINDINGS.md as the source material and say
plainly that it came from videos and that SINGLE SOURCE lines are unverified.

Before you write it, check what `anthropic-skills:cro-analyzer` already does and
tell me whether this should extend it or replace it for my store. Do not build a
duplicate by accident.

The skill must actually look at the site, not read its code:

- Drive a real browser. Use the in-app browser tools in this session
  (`mcp__Claude_Browser__navigate`, `computer` for screenshot / left_click /
  scroll, `read_page`, `resize_window`). Screenshot each page state, save the
  PNGs into the run folder, and Read them back so the findings are based on what
  a visitor sees. Fetching HTML and reasoning about markup is explicitly not
  enough. Say so inside the skill so a future session does not shortcut it.
- Click through, do not just load pages. At minimum: open a product, change the
  size and color variants, add to cart, open the cart drawer, reach the checkout
  screen without completing an order, open the nav and the footer links, and try
  the search.
- Check desktop and mobile. Use the `mobile` preset and reload so any load-time
  device logic re-runs. Capture both for every page type.
- Cover home page, one collection page, at least two product detail pages
  (pick them via the Shopify tools so it audits real live products, not a
  guessed URL), cart, and checkout entry.
- Score each checkable rule from phase 1 as pass, fail, or not applicable, with
  the screenshot filename as the evidence for every fail. No finding without an
  image behind it.
- Output `audits/<date>/REPORT.md`: findings ranked by expected impact against
  effort, each one naming the page, the rule, the evidence image, and the
  specific fix. Separate "makes the store look established" fixes from "removes
  friction" fixes, because those are different problems.

Hard constraints for the skill:

- Read only. It never edits the live store, a theme, a product, or any copy. It
  proposes and I decide.
- Any suggested customer-facing copy inside the report is a draft only, and gets
  flagged as needing the humanizer and structural-humanizer passes before it
  could ship. No em dashes anywhere.
- It never completes a checkout or submits a form with real data.
- If browser tools are unavailable in a future session, it says so and stops
  rather than silently falling back to reading HTML.

Then run the new skill once, end to end, on peculiarpeopleco.com and show me the
report. Fix whatever breaks. A skill built from videos and never executed is a
summary of some videos, not a tool.
