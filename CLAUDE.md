# Peculiar People / Claude Projects

Workspace for Peculiar People (peculiarpeopleco.com) automation. Everything here stays inside this folder plus the sibling `../Temples/` asset folders. Never touch Lease End files or projects from here.

## The brand

`BRAND.md` holds what Peculiar People is: purpose, vision, positioning, products, customer avatars, voice, guardrails, and the open decisions. Read it before any work touching copy, products, marketing, or brand direction. Its "Open decisions" section is load-bearing; do not treat an open question there as settled.

## Projects

- `temple-product-generator/`: generates Printify temple products from `../Temples/` folders. Phases 1-3 complete and gate-approved. Start with its `README.md` and `docs/decisions.md`; the settled decisions there are not up for re-derivation. Drive it via the `temple-product-generator` skill.
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
- Phase gates and product changes that touch the live store get Evan's explicit confirmation. Publishing runs through scripts/publish_drafts.py's gates: base products and verified With Date drafts auto-publish when Evan initiates a run; anything failing a gate stays held for Evan.
- The Printify token lives in `temple-product-generator/.env`, gitignored. Never commit or print it.
