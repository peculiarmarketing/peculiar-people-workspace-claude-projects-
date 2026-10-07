---
name: temple-product-generator
description: Generate Peculiar People temple products on Tapstitch from the Temples folder, end to end. "Run a sweep" finds new temple folders (only the design PNG in them), researches the location and temple facts, builds and publishes the three products, and finishes the gallery, tags, homepage marquee, Temple Art File option and Easify CSV, then verifies it all on the live site. Use when Evan asks to run the sweep, generate temple products, add a temple or garment, check catalog coverage, regenerate or backfill a product, or drops a new temple folder. Triggers include "run a sweep", "run the sweep", "generate [temple]", "temple products", "new temple", "coverage report". Not the refs sweep ("run the refs sweep" is temple-ref-finder).
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
| **The sweep: new temple folders to live and verified** | `scripts/sweep.py scan`; `run --all-ready` (or `--temple T`); `verify --temple T` / `--all` |
| Coverage / where things stand (read only) | `scripts/tapstitch_status.py` (`--full`, `--temple T`, `--state S`, `--problems`) |
| What blocks a run (read only) | `scripts/tapstitch_publish.py check` |
| Validate every design, write no print files (it still rewrites the ledger: check `git diff`) | `scripts/tapstitch_build.py --report-only` |
| Build print files | `scripts/tapstitch_build.py` (`--temple T`, `--garments tee,crew,hoodie`, `--colors black,white`, `--no-trace`, `--verbose`) |
| Proof sheet for Evan | `scripts/tapstitch_preview.py` (`--temple T`, `--garment tee`, `--color white`) |
| Record an approval by hand (the sweep records its own) | `scripts/tapstitch_approve.py --temple T` (`--all`, `--all --except "A,B"`, `--revoke --temple T`, `--list`, `--dry-run`) |
| Plan a run (default, writes nothing) | `scripts/tapstitch_run.py` (`--temple T`, repeatable; `--garments`; `--limit N`) |
| Build in Tapstitch, nothing public | `scripts/tapstitch_run.py --apply --temple T` |
| Build and publish (LIVE, no undo) | `scripts/tapstitch_run.py --apply --publish --temple T` (or `--limit N`; a bound is required) |
| Shopify half for one product | `scripts/tapstitch_publish.py finish --handle H --temple T --garment G` (`--dry-run`) |
| Bind variants to their back image | `scripts/tapstitch_variant_images.py` (`--report-only`, `--handle H`, `--template-id ID`) |
| Art close-up cards | `scripts/art_images.py make --temple T` / `make --all`; `push --temple T` / `push --all` |
| Easify dropdown sync | `scripts/easify_options.py sync` (`--report-only` first); `reseed --export PATH` |
| Back up facts fragments to git | `scripts/mirror_facts.py` (`--report-only`, `--check`) |
| Homepage marquee | `scripts/web_marquee.py check`; `sync` (both take `--theme ID`) |
| Pen drawing files (the sweep runs both) | `scripts/web_drawings.py build --temple T`, then `scripts/pen_strokes.py ART.webp OLD.json OUT.json [--debug DEBUG.png]` (ART and OLD are the build's files in `artifacts/web_drawings/`). Never `web_drawings.py push`: it re-uploads stale first-generation stroke files |
| City-line snippet | `scripts/temple_city_snippet.py` (`web_marquee.py sync` runs it) |
| Colour swatches | `scripts/swatches.py check` (`--strict-theme`); `render`; `push --dry-run` |
| Colour order / product-type fixups | `scripts/shopify_fixups.py all --report-only` (`--handle H`) |
| Gallery composites | `scripts/composite_catalog.py --garment G --outdir DIR --temple T` (`--force`) |
| Gallery build | `scripts/build_garment_catalog.py --garment G --composites DIR --temple T --dry-run` (`--stages`, `--verify`, `--limit`) |
| Re-save every live product's design in place (the 7 Oct 2026 one-quarter lift) | `scripts/relift_rollout.py` plans; `--apply --limit N` (batches of 5); `--verify` read-only |

## Run a sweep (the default for any new temple)

When Evan says "run the sweep", "run a sweep" or drops a new temple folder, run the whole thing without stopping to ask. Saying it is his go-ahead to publish the temples the scan lists (`docs/decisions.md`, 7 Oct 2026). When the sweep ends, every new temple must be complete on the live site.

Evan's only input is a folder in `Temples/` holding the original design PNG.

1. **Preflight and scan.** Check for iCloud duplicate folders (`ls -d *\ 2`), then `scripts/sweep.py scan`. It lists each folder that is not live as `ready`, `needs-research` (location and/or facts), `finishing` (published by an earlier sweep that stopped before the end) or `no-art`. If nothing is listed, say so in one line and stop.
2. **Research every `needs-research` temple, without waiting for Evan.** Use parallel subagents when there are several.
   - **Location:** find the PHYSICAL city on churchofjesuschristtemples.org (see "New temple not in temples.json"). Add the entry to `temples.json` with `verified: true`, the official name, `location_line` and a `source` line that names the page and date. If the sources disagree or are unclear, do not guess: leave the temple out of this sweep and report it at the end. That is the only research stop.
   - **Facts:** follow "Writing descriptions" below in full: the source hierarchy, the myth screen, both humanizer passes, the fragment saved to `Working files/temple-facts.html`, and the source ledger saved under `artifacts/description-ledgers/`. Do not stop for Evan's spot-check; print the ledger in the end summary instead.
3. **Run.** `scripts/sweep.py run --all-ready`. LIVE, no undo. A preflight checks the Tapstitch login, `tapstitch_publish.py check`, `.env`, the stroke builder's packages and the colourway photos before anything is written. If the login has expired, ask Evan to run `scripts/tapstitch_login.py` (it needs his hands) and re-run. Per temple it runs, in order:
   - **build:** trace the PNG if needed (tracer health checks), flatten and validate the print files.
   - **proof:** render the proof sheet into `artifacts/tapstitch-previews/`, kept as the record.
   - **approve:** recorded by the sweep once those automated gates pass.
   - **publish:** `tapstitch_run.py --apply --publish`. This creates the product with its description, distributes it, then sets the product type, the art card, the colour renames, the swatch gate and the variant images.
   - **tags:** `temple:`, `garment:`, `country:` and `state:` tags. The marquee, the product band and the state collections read them.
   - **gallery:** on-model composites, then the standard gallery: on-model back in the flat-lay colour in slot 1.
   - **drawing:** `web_drawings.py build`, then `pen_strokes.py`, then the city-line snippet. All three are uploaded straight to the live theme and read back.
   - **download:** the black SVG goes into `Temples/All/`.
   - **artfile:** the temple is added as a Temple Art File option, sold out until its file is attached.

   Then, once for the whole run: `easify_options.py sync`, the facts mirror, and `verify` on every temple.
4. **If a step fails,** explain the mechanism first, fix it, and re-run `sweep.py run --temple T`. Every step skips what is already done, so a re-run resumes where the last one stopped.
5. **Commit and push** (see "After every run") without asking.
6. **Summarize for Evan:**
   - each temple as DONE (verified live), STOPPED (at which step, and why) or SKIPPED (unclear location);
   - each new temple's source ledger;
   - the proof-sheet path;
   - the manual steps the run printed, and nothing else. Today these are the Easify CSV import, and attaching each new Art File download (`Temples/All/{Temple} black.svg`) in the Digital Products app.

`scripts/sweep.py verify --temple T` (or `--all`) is the read-only proof that a temple is complete. It checks:
- all three products are ACTIVE, with the right title, type, tags and facts;
- the gallery is in the standard order, with slot 1 on-model and every colour bound to its own photo;
- no Tapstitch colour names remain;
- the tee is in `temple-tees`;
- the drawing files and city line are in the live theme;
- the Easify CSV has the rows, the Art File has the option, and the download file and facts mirror exist.

## One-off steps, by hand

Run the sweep for new temples. The scripts below are for repairs and for anything outside a sweep:

1. **Art.** PNG-only folders are traced during the build (`trace_art.py`, `--trim --drop-label`) and must pass the tracer's health checks (lost solid about 0%, lost faint under 10%, weight delta within 8%, no ink touching the frame), or the temple stops with the reason. A "{Temple} trace check (auto).png" lands in the folder. The manifest scaffolds itself from `temples.json`.
2. **Build:** `scripts/tapstitch_build.py --temple "{Name}"`. **Proof:** `scripts/tapstitch_preview.py --temple "{Name}"`. **Approve:** `scripts/tapstitch_approve.py --temple "{Name}"`.
3. **Publish:** `scripts/tapstitch_run.py --temple "{Name}"` to plan, then `--apply --publish --temple "{Name}"`. Every step is resumable: a re-run reads the ids already in the ledger and never distributes twice.
4. **Everything after publishing** is `scripts/sweep.py run --temple "{Name}"`. It skips the steps already done and finishes the rest.

## Writing descriptions

A Tapstitch product carries its description from birth: `generate.description_for()` composes the garment's fixed sections (`reference/garment-copy/{tee,crew,hoodie}/` plus the shared `care-instructions.html`) with the temple's facts fragment, and the runner bakes it into the create call. Research once per temple; all three garments use it.

1. Follow the methodology in `reference/skills/cc1717-temple-description-builder/cc1717-temple-description-builder/SKILL.md` exactly (only its research method and fragment format apply; that folder name is historical): source hierarchy (Tier 1 official Church sources and Church News; Tier 2 churchofjesuschristtemples.org; Tier 3 needs three independent sources), screen every claim against `references/known-myths.md`, check `references/special-cases.md` first, omit what cannot be tiered, no em dashes, the exact HTML format with h3/h4 and time elements.
2. New prose goes through the `humanizer` skill, then the `structural-humanizer` skill (one or two structural interventions, varied per temple), before Evan sees it. The fixed sections and existing fragments are stored assets and are never edited by either pass.
3. Save ONLY the `<section class="temple-facts">` fragment to `Temples/{Name}/Working files/temple-facts.html` with the as-of line dated to the research date. Fragments belong in `Working files/`; a fragment at the folder root still resolves through the fallback, which is how ten ended up misplaced.
4. Print the source ledger in chat (VERIFIED by tier / CONFLICTS RESOLVED / VOLATILE / OMITTED) and save it under `artifacts/description-ledgers/`. Evan spot-checks it.
5. Run `scripts/mirror_facts.py` after editing a fragment outside a run, and commit `artifacts/temple-facts/`.

`description_html.compose_description()` collapses the facts and the fixed sections into `<details>` rows; never wrap them by hand. Live descriptions are not rewritten retroactively unless Evan asks. For an existing live product, `tapstitch_publish.py finish` writes the composed description; `scripts/collapse_live_sections.py` (`--report-only`, `--handle H`) makes the smallest splice-and-collapse change to live pages instead of recomposing them.

## New temple: the homepage marquee (required, done by the sweep)

The marquee (`theme/sections/pp-temple-marquee.liquid`) shows a temple only when:
- its tee is in `temple-tees`, by its `garment:tee` tag;
- the live theme has its art (`assets/pp-temple-<slug>.webp`);
- the live theme has its stroke file (`assets/pp-temple-<slug>.json`);
- the live theme has its city line (`snippets/pp-temple-city.liquid`).

A temple missing any of these is left off, with no error. The sweep's tags and drawing steps cover all four, and they upload through the PP Pipeline app token, which has `write_themes`. No Shopify CLI step is needed. `scripts/web_marquee.py check` is the read-only confirmation. Commit the regenerated snippet and the new stroke file.

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

`Temples/All/` holds a flat copy of every temple's black SVG, named by its clean place token (`Manhattan black.svg`, `Ogden Original black.svg`, no stars). It feeds the Temple Art File digital product's delivery app. The sweep copies each new temple's file (`generate.mirror_black_art`) and adds the temple as a sold-out option on the Temple Art File. Attaching the file in the Digital Products app is manual, because that app opens a file picker. `All` is not a temple folder: any script walking `Temples/` must skip it.

## Art close-up cards

Every product gets a black-art-on-white card in the gallery. Cards render to `Temples/{Name}/{Name} art closeup (auto).png` (an Evan-made file without "(auto)" overrides). The runner pushes the card for each temple it publishes; `art_images.py push --all` catches anything missing. Idempotent via the alt marker "Temple line art close-up". Needs `SHOPIFY_STORE_DOMAIN` and `SHOPIFY_ADMIN_TOKEN` in `.env`; if absent, say so and skip.

## Temple dropdown (Easify)

Every product page shows a "Temple" dropdown cross-linking the same garment line's other temples. The canonical CSV is `artifacts/easify/option-sets.csv`; `artifacts/easify/sets.json` maps garment lines to sets. `easify_options.py sync` reads the live catalog, checks every label and URL against real handles, adds new temples alphabetically, and rewrites the CSV only on change. Rows are never deleted. Evan imports the CSV by hand. If an import created a new set, Evan exports fresh from Easify and we run `easify_options.py reseed --export <file>`, then commit.

## After every run

The sweep runs the Easify sync, the marquee steps and the facts mirror itself. Evan's manual steps are only the Easify CSV import and attaching new Art File downloads, and the sweep prints them only when they are needed.

Commit and push repo changes the run produced: `temples.json` entries, the ledger and `sweep-state.json` in `artifacts/tapstitch/`, description ledgers, `artifacts/temple-facts/`, the Easify CSV, the city-line snippet and stroke files, and any code or config changes. The remote is Evan's PERSONAL GitHub, peculiarmarketing, over HTTPS using the repo's configured origin; never wire this repo to his work GitHub account (edavis821). Files in `Temples/` live outside the repo and are not committed.

## Hard rules

- Publishing is `--apply --publish` with a bound, run only when Evan initiated it. "Run a sweep" is that initiation for the temples the scan lists. Nothing else distributes.
- Place tokens live in manifests and may differ from folder names ("Washington DC" folder, "Washington D.C." token). Folder names may carry a ref-finder star ("Lehi*"); `--temple "Lehi"` resolves it.
- Never create a product whose title duplicates a live one.
- Do not modify the description skill, the tracer outputs, or anything in `Temples/` beyond manifests, facts fragments, print files, `(auto)` renders and the `Temples/All/` mirror.
- Do not touch Lease End files or projects, ever.
