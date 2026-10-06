---
name: temple-product-generator
description: Generate Peculiar People temple products on Tapstitch from the Temples folder. Use when Evan asks to generate temple products, run the temple sweep, add a temple or garment, check catalog coverage, regenerate or backfill a product, or drops a new temple folder. Triggers include "generate [temple]", "run the sweep", "temple products", "new temple", "coverage report".
---

# Temple Product Generator

Project repo: `Claude Projects/temple-product-generator/`. Read `HANDOFF.md` (top) and `docs/decisions.md` before changing behavior; settled decisions there are not up for re-derivation. Voice: no em dashes in anything Evan-facing, explain a failure's mechanism before fixing it.

All commands run from the repo root with `./.venv.nosync/bin/python`. Credentials live in `.env` (gitignored); never print or commit it.

## The catalog

The store runs on Tapstitch. Three garment lines, one product per temple per line, 45 temples, 135 live products:

| Garment id | Tapstitch blank | Title pattern (`garments/{id}.json` under `naming`) |
|---|---|---|
| `tee` | RT0063 | `Essential Heavyweight Temple Tee ({place})` |
| `crew` | R00368 | `Ultra-soft Temple Sweatshirt ({place})` |
| `hoodie` | R00286 | `Ultra-soft Oversized Temple Hoodie ({place})` |

Never hardcode a title; read it from the garment config. A title renamed on the store by hand must be mirrored into the config, because the runner's duplicate guard compares titles.

**Salt Lake is the parent temple** (`config/catalog.json`). Its products carry the bare `title_parent`; every other temple carries the place in parentheses. Garment collections show only the parent (tagged `listing:parent`), and shoppers reach every other temple through the Easify Temple dropdown.

**Limited Edition titles are Evan's hand-built one-offs.** The pipeline never claims, publishes or gives a dropdown row to one.

## How a product gets made

Products are created from Python against Tapstitch's own JSON API (`tapstitch_api.py`). Auth is the dedicated Chrome profile's cookies (port 9223). Evan logs in once with `scripts/tapstitch_login.py`; `--check` verifies the session. Only `distribute()` reaches the storefront; everything before it stays inside Tapstitch.

Every row lives in the migration ledger (`artifacts/tapstitch/ledger.json`, readable copy `LEDGER.md`), one row per temple per garment. States, worst to best: `art-missing`, `error`, `art-ok`, `file-built`, `file-approved`, `product-created`, `description-written`, `card-pushed`, `live`. The ledger is not the authority on what is live; the runner checks the store's real titles before building.

## Commands

| Task | Command |
|---|---|
| Coverage / where things stand (read only) | `scripts/tapstitch_status.py` (`--full`, `--temple T`, `--state S`, `--problems`) |
| What blocks a run (read only) | `scripts/tapstitch_publish.py check` |
| Validate every design, write nothing | `scripts/tapstitch_build.py --report-only` |
| Build print files | `scripts/tapstitch_build.py` (`--temple T`, `--garments tee,crew,hoodie`, `--colors black,white`, `--no-trace`, `--verbose`) |
| Proof sheet for Evan | `scripts/tapstitch_preview.py` (`--temple T`, `--garment tee`, `--color white`) |
| Record Evan's approval | `scripts/tapstitch_approve.py --temple T` (`--all`, `--all --except "A,B"`, `--revoke --temple T`, `--list`, `--dry-run`) |
| Plan a run (default, writes nothing) | `scripts/tapstitch_run.py` (`--temple T`, repeatable; `--garments`; `--limit N`) |
| Build in Tapstitch, nothing public | `scripts/tapstitch_run.py --apply --temple T` |
| Build and publish (LIVE, no undo) | `scripts/tapstitch_run.py --apply --publish --temple T` (or `--limit N`; a bound is required) |
| Shopify half for one product | `scripts/tapstitch_publish.py finish --handle H --temple T --garment G` (`--dry-run`) |
| Bind variants to their back image | `scripts/tapstitch_variant_images.py` (`--report-only`, `--handle H`, `--template-id ID`) |
| Art close-up cards | `scripts/art_images.py make --temple T` / `make --all`; `push --temple T` / `push --all` |
| Easify dropdown sync | `scripts/easify_options.py sync` (`--report-only` first); `reseed --export PATH` |
| Back up facts fragments to git | `scripts/mirror_facts.py` (`--report-only`, `--check`) |
| Homepage marquee | `scripts/web_marquee.py check`; `sync` (both take `--theme ID`) |
| Pen stroke file | `scripts/pen_strokes.py ART.webp OLD.json OUT.json [--debug DEBUG.png]` |
| City-line snippet | `scripts/temple_city_snippet.py` (`web_marquee.py sync` runs it) |
| Colour swatches | `scripts/swatches.py check` (`--strict-theme`); `render`; `push --dry-run` |
| Colour order / product-type fixups | `scripts/shopify_fixups.py all --report-only` (`--handle H`) |
| Gallery composites | `scripts/composite_catalog.py --garment G --outdir DIR --temple T` (`--force`) |
| Gallery build | `scripts/build_garment_catalog.py --garment G --composites DIR --temple T --dry-run` (`--stages`, `--verify`, `--limit`) |

## New temple, end to end

1. **Art.** Evan drops a folder in `Temples/` with either the black and white SVGs or just the source sketch PNG ("{Temple}.png", or any single unambiguous PNG). PNG-only folders are traced during the build (`trace_art.py`, `--trim --drop-label`) and must pass the tracer's health checks (lost solid about 0%, lost faint under 10%, weight delta within 8%, no ink touching the frame) or the temple stops with the reason. A "{Temple} trace check (auto).png" lands in the folder for Evan's eyeball. The manifest scaffolds itself from `temples.json`.
2. **Location.** If the temple is not in `temples.json`, the build stops rather than guessing. See "New temple not in temples.json" below.
3. **Facts.** Research and save `temple-facts.html` (see "Writing descriptions"). The runner blocks any row without it; that is a workflow step, not a bug.
4. **Build.** `scripts/tapstitch_build.py --temple "{Name}"` writes the flattened back print files into the temple folder and adds the rows to the ledger as `file-built`.
5. **Proof.** `scripts/tapstitch_preview.py --temple "{Name}"` renders the proof page into `artifacts/tapstitch-previews/`. Show it to Evan.
6. **Approve.** Only after Evan approves: `scripts/tapstitch_approve.py --temple "{Name}"`. Approval is per temple and covers all three garments.
7. **Plan, then run.** `scripts/tapstitch_run.py --temple "{Name}"` prints the plan and any blockers. Publishing puts listings live with no undo, so run `--apply --publish --temple "{Name}"` only when Evan has initiated it. Per row the runner creates the template, uploads the back and front files, saves the design, creates the store product with the description baked in, distributes, waits for Shopify, then runs the Shopify half (product type, art card at slot 2, colour fixups, swatch gate) and rebinds each variant to its back image. Every step is resumable: a re-run reads the ids already in the ledger and never distributes twice. On the way out it mirrors the facts fragments into `artifacts/temple-facts/` and runs the marquee check.
8. **Easify.** `scripts/easify_options.py sync --report-only`, then `sync`. Evan imports `artifacts/easify/option-sets.csv` in the Easify app by hand; importing is never automated.
9. **Marquee.** Required, see below.
10. **Gallery (optional, per Evan).** The standard gallery (flat back, flat front, art card, on-model backs, fabric details) comes from `composite_catalog.py` then `build_garment_catalog.py`. Dry-run first; `--prune` deletes images.
11. **Commit** (see "After every run").

## Writing descriptions

A Tapstitch product carries its description from birth: `generate.description_for()` composes the garment's fixed sections (`reference/garment-copy/{tee,crew,hoodie}/` plus the shared `care-instructions.html`) with the temple's facts fragment, and the runner bakes it into the create call. Research once per temple; all three garments use it.

1. Follow the methodology in `reference/skills/cc1717-temple-description-builder/cc1717-temple-description-builder/SKILL.md` exactly (only its research method and fragment format apply; that folder name is historical): source hierarchy (Tier 1 official Church sources and Church News; Tier 2 churchofjesuschristtemples.org; Tier 3 needs three independent sources), screen every claim against `references/known-myths.md`, check `references/special-cases.md` first, omit what cannot be tiered, no em dashes, the exact HTML format with h3/h4 and time elements.
2. New prose goes through the `humanizer` skill, then the `structural-humanizer` skill (one or two structural interventions, varied per temple), before Evan sees it. The fixed sections and existing fragments are stored assets and are never edited by either pass.
3. Save ONLY the `<section class="temple-facts">` fragment to `Temples/{Name}/Working files/temple-facts.html` with the as-of line dated to the research date. Fragments belong in `Working files/`; a fragment at the folder root still resolves through the fallback, which is how ten ended up misplaced.
4. Print the source ledger in chat (VERIFIED by tier / CONFLICTS RESOLVED / VOLATILE / OMITTED) and save it under `artifacts/description-ledgers/`. Evan spot-checks it.
5. Run `scripts/mirror_facts.py` after editing a fragment outside a run, and commit `artifacts/temple-facts/`.

`description_html.compose_description()` collapses the facts and the fixed sections into `<details>` rows; never wrap them by hand. Live descriptions are not rewritten retroactively unless Evan asks. For an existing live product, `tapstitch_publish.py finish` writes the composed description; `scripts/collapse_live_sections.py` (`--report-only`, `--handle H`) makes the smallest splice-and-collapse change to live pages instead of recomposing them.

## New temple: add it to the homepage marquee (required)

Every new temple must reach the homepage marquee; this is part of the pipeline, not an optional extra. The marquee (`theme/sections/pp-temple-marquee.liquid`) shows a temple only when the live theme has its art (`assets/pp-temple-<slug>.webp`), its stroke file (`assets/pp-temple-<slug>.json`, from `scripts/pen_strokes.py`, see `theme/README.md`) and its city line (`snippets/pp-temple-city.liquid`). A temple missing any of them is left off with no error. After publishing, run `scripts/web_marquee.py sync`, upload what it lists with the `shopify theme push --nodelete` command it prints (from the Mac; the store connector cannot write the live theme), and re-run `scripts/web_marquee.py check` until it is clean. `tapstitch_run.py --publish` runs the check itself at the end. Commit the regenerated snippet and the new stroke file.

## New temple not in temples.json

The build hard-stops rather than guessing. Research the temple's PHYSICAL city (churchofjesuschristtemples.org is the reference; the physical city can differ from the name: Washington D.C. Temple prints KENSINGTON, MARYLAND). Add the entry with `verified: true` and the format `CITY, STATE` (spelled out) or `CITY, COUNTRY`, then re-run. If sources are unclear, ask Evan instead of guessing.

## Adding a garment

1. Copy `garments/tee.json` to `garments/{new_id}.json` with `"channel": "tapstitch"`. Fill the `blank` (model, variant code, sizes), `print_area` and `front_print_area`, `colorways`, `storefront_first_color`, `shopify_product_type`, `naming`, `price_usd`, `costs_usd`, and `garment_copy` pointing at a new `reference/garment-copy/{new_id}/` folder.
2. Every storefront colour name needs a hex in `config/swatches.json` and an entry in `colour_names.py`, or the swatch gate stops the publish.
3. Add the line to `artifacts/easify/sets.json` so it gets a Temple dropdown set.
4. `scripts/tapstitch_publish.py check` until nothing blocks, then build, preview and approve one temple with `--garments {new_id}`, and have Evan eyeball it before it goes near the rest of the catalog. Spacing overrides go in the garment config, never in code.

Adding a layout profile (a genuinely new arrangement): one function in `layout.py` plus a `PROFILES` entry.

## Coverage check

`scripts/tapstitch_status.py` gives the per-state counts; `--full` or `--problems` lists rows. `scripts/tapstitch_run.py` with no flags shows what is ready and what is blocked, with reasons, against the live store's titles. `scripts/web_marquee.py check` covers the homepage side.

## Regenerating or repairing a live product

Most damage is Shopify-side and repaired in place, all idempotent:

- Product type, description, art card, colour fixups: `tapstitch_publish.py finish --handle H --temple T --garment G` (`--dry-run` first).
- Variants opening on the blank front: `tapstitch_variant_images.py --handle H`.
- Missing art card: `art_images.py push --temple T`.
- Colour order: `shopify_fixups.py all --handle H`.

Tapstitch cannot add a colour to an existing listing, and distributing a rebuilt store product creates a second Shopify product with the same title rather than updating the first. A full rebuild is therefore a swap: new product, old one set to DRAFT at a `-retired-<date>` address. `scripts/eden_green_rollout.py` is the worked example; its docstring holds the sequence and traps. Any swap needs Evan's explicit go-ahead.

## Temples/All mirror (digital download files)

`Temples/All/` holds a flat copy of every temple's black SVG named by its clean place token (`Manhattan black.svg`, `Ogden Original black.svg`, no stars). It feeds the Temple Art File digital product's delivery app. The Tapstitch scripts do not refresh it, so check that a new temple's black SVG is there. `All` is not a temple folder: any script walking `Temples/` must skip it.

## Art close-up cards

Every product gets a black-art-on-white card in the gallery. Cards render to `Temples/{Name}/{Name} art closeup (auto).png` (an Evan-made file without "(auto)" overrides). The runner pushes the card for each temple it publishes; `art_images.py push --all` catches anything missing. Idempotent via the alt marker "Temple line art close-up". Needs `SHOPIFY_STORE_DOMAIN` and `SHOPIFY_ADMIN_TOKEN` in `.env`; if absent, say so and skip.

## Temple dropdown (Easify)

Every product page shows a "Temple" dropdown cross-linking the same garment line's other temples. The canonical CSV is `artifacts/easify/option-sets.csv`; `artifacts/easify/sets.json` maps garment lines to sets. `easify_options.py sync` reads the live catalog, checks every label and URL against real handles, adds new temples alphabetically, and rewrites the CSV only on change. Rows are never deleted. Evan imports the CSV by hand. If an import created a new set, Evan exports fresh from Easify and we run `easify_options.py reseed --export <file>`, then commit.

## After every run

Once products are published: `scripts/easify_options.py sync`, then the marquee steps above, then `scripts/mirror_facts.py --check`. Evan's manual steps: the Easify CSV import and the theme upload.

Commit and push repo changes the run produced: `temples.json` entries, the ledger in `artifacts/tapstitch/`, description ledgers, `artifacts/temple-facts/`, the Easify CSV, the city-line snippet and stroke files, and any code or config changes. The remote is Evan's PERSONAL GitHub, peculiarmarketing, over HTTPS using the repo's configured origin; never wire this repo to his work GitHub account (edavis821). Files in `Temples/` live outside the repo and are not committed.

## Hard rules

- Publishing is `--apply --publish` with a bound, run only when Evan initiated it. Nothing else distributes.
- Place tokens live in manifests and may differ from folder names ("Washington DC" folder, "Washington D.C." token). Folder names may carry a ref-finder star ("Lehi*"); `--temple "Lehi"` resolves it.
- Never create a product whose title duplicates a live one.
- Do not modify the description skill, the tracer outputs, or anything in `Temples/` beyond manifests, facts fragments, print files and `(auto)` renders.
- Do not touch Lease End files or projects, ever.
