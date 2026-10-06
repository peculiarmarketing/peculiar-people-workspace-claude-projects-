# Peculiar People / Claude Projects

Workspace for Peculiar People (peculiarpeopleco.com) automation. Everything here stays inside this folder plus the sibling `../Temples/` asset folders. Never touch Lease End files or projects from here.

## The brand

`BRAND.md` holds what Peculiar People is: purpose, vision, positioning, products, customer avatars, voice, guardrails, and the open decisions. Read it before any work touching copy, products, marketing, or brand direction. Its "Open decisions" section is load-bearing; do not treat an open question there as settled.

## Projects

- `temple-product-generator/`: generates Tapstitch temple products from `../Temples/` folders. Phases 1-3 complete and gate-approved. Start with its `README.md` and `docs/decisions.md`; the settled decisions there are not up for re-derivation. Drive it via the `temple-product-generator` skill. Work in flight is at the top of its `HANDOFF.md`; read that before anything else there.
- `idea-inbox/`: nightly pipeline. The Mac mini collects reels and notes Evan saves (iMessage to self, two Instagram chats) at 1:15 AM; the `idea-triage` skill turns them into verdicts and plans, drafts, or mockups in `ideas/` around 2 AM. Plans and drafts only. Start with `idea-inbox/README.md`.

## Writing outward-facing copy

Any text a customer or the public will read (website copy, product descriptions, social posts, marketing emails) gets two editing passes before it is shown to Evan or shipped:

1. `humanizer` skill: surface pass for word-level AI tells.
2. `structural-humanizer` skill: structural pass for shape-level tells. Pick 1 or 2 structural interventions per piece and vary them across pieces; never apply the whole menu at once.

Both skills live in `.claude/skills/`, adapted from the vendored `humanizer-stack/` repo (update with `git pull` there, then re-copy per the provenance notes in each SKILL.md). Their deterministic scanners (`.claude/skills/humanizer/scripts/copy_scan.py` and `.claude/skills/structural-humanizer/scripts/structural_scan.py`) are an optional final check on drafts. The no-em-dash house rule below stays absolute; it already matches the top-ranked tell.

This applies only to new prose being drafted (new temple facts sections, scheduled description rewrites, website copy, posts). It never applies to text assembled from stored files: the fixed description sections (product-intro, size-guide, personalization) and existing temple-facts fragments are hardcoded assets that get copied in byte-identical, and no editing pass may touch them during composition or publishing. Existing published copy is not retroactively rewritten unless Evan asks.

## House rules

- No em dashes in anything Evan-facing (chat, docs, product copy). Plain, direct language.
- Explain the mechanism of a failure before fixing it.
- Phase gates and product changes that touch the live store get Evan's explicit confirmation.
- API tokens live in `temple-product-generator/.env`, gitignored. Never commit or print them.

## Keeping the claude.ai project in sync

The "Peculiar People" Project on claude.ai holds copies of three docs so chat work matches what is live. They go stale unless this workspace pushes updates.

| Project doc | Source here |
|---|---|
| `claude/BRAND.md` | `BRAND.md` |
| `claude/pipeline-and-tools.md` | `project-sync/pipeline-and-tools.md` |
| `claude/unit-economics.md` | `project-sync/unit-economics.md` |

At the end of any session that makes a material change, update the matching source file here first, then re-upload it to the Project. Material means:

- BRAND.md changed (a decision closed or opened, products, prices, colours, avatars, voice, direction).
- A pipeline or tool changed: a skill added or retired, a new app or vendor, a change to how art or products get made.
- A HANDOFF.md item finished or a new one opened that Evan has to act on. Update the "Current state" and "Still open" sections of `project-sync/pipeline-and-tools.md`, and its date.
- Costs, prices or margins changed. Update `project-sync/unit-economics.md`.

How to push:

- If a Projects tool is available in the session, write each changed file to its Project path above (`project_write` with `local_path`, replacing the existing doc). Only push files that changed, since every write clears the Project's cache.
- If no Projects tool is available, end the session by telling Evan which Project docs are stale and which source files to upload.

Routine product runs that change nothing in the three docs need no sync. The Project copies are never the source of truth; if they disagree with this folder, this folder wins.
