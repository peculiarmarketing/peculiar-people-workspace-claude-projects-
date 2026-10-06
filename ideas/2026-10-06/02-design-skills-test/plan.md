# Test plan: do third-party design skills make better pages here?

Verdict: **Plausible.** From @nateherkai ("Claude just killed web designers") and @nick_saraev ("5 plugins for better front-end design").

## The claim

Add design skills to Claude Code and its pages stop looking generic. The skills named:

- Emil Kowalski's design skill
- "impeccable"
- the Taste Skill ("Anti-Slop Frontend Framework for AI Agents", 76,000 stars claimed in the caption, unverified)
- Vercel's Web Design Guidelines skill, which audits a page against Vercel's rules

Then connect Playwright and the Figma MCP so Claude screenshots its own work and fixes it.

## Why only Plausible

- **The store is a Shopify theme, not a hand-built site.** These skills are tuned for React and Tailwind pages. Most of what Peculiar People shows customers comes from the theme and its settings, not from code Claude writes.
- **Where they could help is narrower:** idea-triage mockups, a future landing page, and the bulk inquiry form.
- **The screenshot loop already exists.** `store-cro-audit` drives a real browser and screenshots every state (`scripts/capture.js`). Playwright adds nothing new here.
- **No repo URLs were shown** for impeccable, the Taste Skill or the Kowalski skill. Both reels withhold links behind "comment DESIGN" or "comment DIE". So none of these can be vetted from the reels alone.

## Cheapest test (about 30 minutes, in a session with Evan)

1. **Do plan 01 first.** Its DESIGN.md is the free version of what these skills sell: house tokens plus a "do not" list.
2. **Pick one skill, the Vercel Web Design Guidelines skill.** It comes from a known company, and it audits rather than generates, so it changes nothing by itself. Evan finds and reads its source before anything is installed. Never install from a link a reel or DM supplies.
3. **Point it at one live product page** (read-only), and compare its findings with what store-cro-audit already reports for the same page.
4. **Keep it only if** it finds something real that the audit missed. Otherwise uninstall it and close this idea.

## What would change the verdict

If Peculiar People ever builds custom pages outside the theme (a landing page for a temple dedication, say), the generating skills (Taste, impeccable) become worth a real trial on that page.

## Risks

Third-party skills run with the same access as Claude Code in this workspace, including the `.env` in temple-product-generator. That is the reason Evan reads any skill's files before installing it.
