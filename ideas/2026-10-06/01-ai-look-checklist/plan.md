# Plan: catch the "AI-made" look before a customer does

Verdict: **Useful.** From four reels in the 4:02 PM batch: @millee.md (20 reasons your app looks vibecoded), @zanderwhitehurst (stop centring stacked text), @lincolndevine (5 tells your app was vibe coded), @adam_ha_yes (20 UX laws to tell Claude).

## Why this one

The store has zero reviews and a premium price (BRAND.md sections 5 and 16). The thing that kills trust fastest on a store like that is looking like a template someone generated in an afternoon. Section 17 also says every store image today is a mockup, so the rest of the page has to carry credibility on its own.

Two of the reels are checklists of exactly that failure. A lot of it does not apply to a Shopify theme (shadcn, Lucide icons, React glassmorphism), but a useful slice does, and some of it is already house style: "em dashes everywhere" is item 16 on @millee.md's list and an absolute rule here.

The store-cro-audit skill already exists and already checks contrast (T9), default typeface (T1), palette (T3), above-the-fold animation (H14), the carousel (H3) and button dominance (P6). So this extends that skill. It does not create a new one.

## What changes

### Part 1. New rules in `.claude/skills/store-cro-audit/references/rules.md`

A new section, "Looks generated", plus a short "Forms" section. Every rule is SINGLE basis, sourced to the reel creator, and the file's own warning applies: these are practitioners on a marketing channel, not research.

| ID | Rule | Source | Applies here because |
|---|---|---|---|
| G1 | No stacked block of three or more centred lines of body text | @zanderwhitehurst | Centred multi-line text is a common theme default on Shopify sections |
| G2 | No emoji in headings or section titles | @millee.md | Cheap to check, reads as generated |
| G3 | No gradient text and no purple-to-blue gradient anywhere | @millee.md | BRAND.md section 8 already removed purple `#6d388b` and its gradient; this checks it stays gone |
| G4 | No small badge or pill sitting above a hero headline | @millee.md | A very common AI landing-page pattern |
| G5 | No content fades or slides in on scroll | @millee.md | Extends H14, which only covers above the fold |
| G6 | No generic buzzword copy ("elevate", "seamless", "curated", "unlock") in any section heading or button | @millee.md | Pairs with the humanizer rule for new copy |
| G7 | Spacing between sections is consistent on a page | @millee.md | Checked by eye on the screenshots, flagged only when obvious |
| G8 | No em dash in any visible storefront text | @millee.md, and house rule | Currently a constraint on the report; this makes it a check on the store |

Forms (the contact form today, and the bulk inquiry form BRAND.md section 9 recommends building):

| ID | Rule | Source |
|---|---|---|
| F1 | Submitting a form twice quickly does not send it twice; the button disables or shows progress | @lincolndevine |
| F2 | A failed submit shows a plain-language message, never raw error text | @lincolndevine |
| F3 | On mobile, the keyboard does not cover the field being typed in | @lincolndevine |
| F4 | Going back from a form error does not wipe what was typed | @lincolndevine |

F1 and F4 can only be tested by submitting, and the audit never submits a form with real data (store-cro-audit SKILL.md). So F1 and F4 are checked by reading the form's behaviour where possible, or marked "not testable read-only" in the report. Never by submitting.

Not added: the 20 UX laws. Most already map to existing rules (Hick's law to H7, Fitts's law to M2, Von Restorff to P6, Jakob's law to the whole CONFIRMED set). Note the mapping in a comment rather than adding duplicates.

### Part 2. A short `DESIGN.md` at the project root

A single page that design-producing work reads before making anything visual: idea-triage mockups, any landing page or section Claude drafts, and future theme edits. Contents:

- The tokens from BRAND.md section 8, copied with a pointer back: Arial 16px body, Montserrat headings, black, white, navy `#001A58`, orange `#F58000` for buttons, red for errors only.
- The "do not" list: the G rules above, written as instructions.
- One line at the top: "BRAND.md section 8 wins if this file disagrees with it."

The DESIGN.md idea is from @nick_saraev's reel (the Awesome DESIGN.md repo, a format Google Stitch introduced). Nothing needs installing; it is one markdown file.

Add DESIGN.md to the CLAUDE.md "material change" list so it gets updated when section 8 does.

## Files touched

- `.claude/skills/store-cro-audit/references/rules.md` (new sections)
- `.claude/skills/store-cro-audit/SKILL.md` (one line: also score the G and F rules)
- `DESIGN.md` (new)
- `CLAUDE.md` (one line in the material-change list)
- `.claude/skills/idea-triage/SKILL.md` (mockups read DESIGN.md)

## Risks

- **Rule creep.** The audit already has 68 rules. Eight more is fine; adding every listicle would not be. Keep the bar at "a customer would notice".
- **Two sources of truth.** DESIGN.md copies section 8. Mitigated by the "BRAND.md wins" line and the CLAUDE.md update rule.
- **Single-source rules.** All twelve are SINGLE. The report must say so whenever one drives a finding, as the skill already requires.

## How to test

Run the store-cro-audit after the change and check that every G and F rule gets a pass, a fail with a screenshot, or "not testable read-only". No rule should be silently skipped.

## Effort

About an hour in a session with Evan: 30 minutes for the rules, 20 for DESIGN.md, 10 for the audit run.

## Next step for Evan

Say "go" on this plan in a session, or strike any rule you disagree with first. G6 (buzzwords) is the most judgement-based.
