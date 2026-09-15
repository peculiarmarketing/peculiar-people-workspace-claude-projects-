---
name: temple-product-generator
description: Generate Peculiar People temple products on Printify from the Temples folder. Use when Evan asks to generate temple products, run the temple sweep, add a temple or garment, check catalog coverage, regenerate or backfill a product, or drops a new temple folder. Triggers include "generate [temple]", "run the sweep", "temple products", "new temple", "coverage report".
---

# Temple Product Generator

Project repo: `Claude Projects/temple-product-generator/`. Read `docs/decisions.md` before changing behavior; those decisions are settled and gate-approved. Voice: no em dashes in anything Evan-facing, explain a failure's mechanism before fixing it.

All commands run from the repo root with `./.venv.nosync/bin/python`.

## Commands

| Task | Command |
|---|---|
| Coverage report (read-only) | `generate.py --sweep --report-only` |
| Morning sweep (generate everything possible) | `generate.py --sweep` |
| One temple, specific garments | `generate.py --temple "Salt Lake" --garments cc1717-dated` |
| One-time catalog rename backfill | `scripts/rename_catalog.py` (`--report-only` first, always) |
| Backfill a live product in place | `generate.py --temple Logan --garments cc1717 --in-place` |
| Replace-alongside (retire old at publish) | `... --replace` |
| Preview a layout without touching Printify | `preview.py --temple Logan --location "LOGAN, UTAH" --garment cc1717` |
| Add date layers to dated drafts | `scripts/add_date_layer.py` (`--report-only` to preview; drives the Printify editor via the dedicated Chrome, see `scripts/printify_login.py` for the one-time login) |
| Publish eligible drafts (base plus verified dated) | `scripts/publish_drafts.py` (`--report-only` to preview, `--only "title text"` to restrict) |
| Shopify fixups (hoodie colorway, color order, featured photo) | `scripts/shopify_fixups.py all` (`--report-only` to preview, `--handle H` for one) |
| Re-push published products to Shopify | `scripts/republish.py` (destructive, repairs itself; read the warning below first) |
| Default variant onto the wanted colorway | `scripts/default_variant.py` (`--report-only` to preview) |
| Easify dropdown sync (after publishing) | `scripts/easify_options.py sync` (`--report-only` to preview) |

## Product naming

Titles lead with the garment line and carry the temple in parentheses. The
patterns live in `garments/*.json` under `naming`; never hardcode one.

| Garment | Title | Salt Lake (parent) |
|---|---|---|
| cc1567 hoodie | `Pillar Temple Hoodie ({place})` | `Pillar Temple Hoodie` |
| cc1566 crew | `Classic Temple Crew Sweatshirt ({place})` | `Classic Temple Crew Sweatshirt` |
| cc1717 tee | `Essential Temple Tee ({place})` | `Essential Temple Tee` |
| cc1717-dated | `Essential Temple Tee – with personalizable date ({place})` | `Essential Temple Tee – with personalizable date` |

En dash, lowercase after it. No em dashes anywhere.

**Salt Lake is the parent temple** (`config/catalog.json`). Its four products
carry the bare garment title; every other temple's title carries the temple in
parentheses, and shoppers can reach any temple through the Easify Temple
dropdown on every product page. ALL products publish ACTIVE on Shopify (Evan's
26 Aug 2026 decision; the unlist fixup is removed). Children published before
that date remain UNLISTED and keep working URLs; nothing in the pipeline sets
a product's status in either direction anymore. Build a title with
`generate.build_title()` and read one back with `art_images.match_temple()`;
both handle the parent case.

**Limited Edition titles are Evan's hand-built one-offs** (`Essential Temple
Tee – Limited Edition (Nauvoo)` and the two Nauvoo front-logo garments). The
pipeline never claims one as a duplicate, never auto-publishes one, and never
gives one a dropdown row. This marker replaced the old `(front logo)` one.

## The workflow

1. Evan drops a temple folder in `Temples/` containing either the black + white SVGs OR just the source sketch PNG (named "{Temple}.png", or any single unambiguous PNG). PNG-only folders are traced automatically during the run (trace_art.py wraps the exported tracer with the standard --trim --drop-label flags) and must pass the tracer skill's health checks (lost solid ~0%, lost faint under 10%, weight delta within 8%, no ink touching the frame) or that temple hard-stops with the reason. A "{Temple} trace check (auto).png" composite lands in the folder for Evan's eyeball; his real quality gate remains reviewing the unpublished product before publishing. The manifest scaffolds itself from `temples.json`.
2. For each product wanted, Evan duplicates ANY product of that garment in the Printify UI (dated sources only for the dated line,; the duplicate carries mockups, personalization config, and variant visibility, but NOT the Economy shipping toggle: new drafts default Economy off, observed 18 Aug 2026).
3. Run the sweep or a targeted generate. The generator claims duplicates, uploads art (resolution bumped in memory to 4096), renders location text in Alata (Evan's own `*location text*` files override; `(auto)` files are the generator's, always regenerated), computes ink-anchored layout, and PUTs the design with the real title.
4. After descriptions are written, run `scripts/add_date_layer.py` for any dated drafts: it drives the Printify editor via the dedicated Chrome (CDP attach; Evan logs in once via `scripts/printify_login.py`) to add the personalization date text layer to all colorway groups, then verifies via API. Manual editor flow remains the fallback.
5. Run `scripts/publish_drafts.py`: drafts publish to Shopify automatically when they pass every gate: never published, not locked by an in-progress publish, not a "Copy of" or Limited Edition title, temple-facts section present, and for dated/personalizable drafts a clean date-layer verification (Evan's 18 Aug 2026 evening decision reversing the earlier never-publish-dated rule). Unverified dated drafts stay held for Evan to finish by hand. Economy shipping is NOT a gate (Evan's 19 Aug 2026 decision): drafts publish with Economy off and the run output notes each one so Evan can flip the toggle in the Printify UI whenever, post-publish. Evan retires old products when a draft was a `--replace`ment. Publishing puts listings live immediately, so run it only as part of a run Evan initiated. Confirmation is checked against Shopify itself (Printify's own status lags the push by several minutes; the product is typically live in 1 to 4). After each publish confirms, the script applies the Shopify fixups for that product: a hoodie's "True Navy" colorway is renamed to "Blue Jean", and the garment's `storefront_first_color` is moved to the front of the Color option (Moss on tees, True Navy on crews, Denim on hoodies). The product's listing status is left alone: everything publishes ACTIVE (Evan's 26 Aug 2026 decision; children were unlisted before then and stay that way). That last one sets which variant the product page opens on, since Shopify preselects variant position 1 and derives position from the option value order; it is also the swatch display order. Caveat: Shopify re-derives every option's order from the resulting variant sequence, so a first color missing a size pushes that size to the back. Denim lacks S and 3XL on the hoodies, which is why hoodie sizes read M, L, XL, 2XL, S, 3XL; Evan accepted that on 22 Aug 2026. It also puts the default variant on the garment's declared `default_colorway` (Moss on the dated tee), preserving the size: "True Navy / L" becomes "Moss / L". That moves Printify's default, which mockup selection follows; Shopify orders variants itself and does not follow it.

## Writing descriptions (after generating a temple's products)

Descriptions are written to PRINTIFY pre-publish, so products go live complete. Research once per temple, apply to all its garments:

1. Follow the methodology in `reference/skills/cc1717-temple-description-builder/.../SKILL.md` EXACTLY: source hierarchy (Tier 1 official Church sources and Church News; Tier 2 churchofjesuschristtemples.org; Tier 3 needs three independent sources), screen every claim against `references/known-myths.md`, check `references/special-cases.md` first, omit what cannot be tiered, no em dashes, the exact HTML format with h3/h4 and time elements.
2. Save ONLY the `<section class="temple-facts">` fragment to `Temples/{Name}/temple-facts.html` with the as-of line dated to the research date.
3. Run `scripts/write_description.py --temple "{Name}"`. It assembles the garment-correct fixed sections plus the fragment and PUTs it to every product in the temple's status.json. The dated tee's fixed sections open with the Personalization block at `reference/description-blocks/personalization-intro.html`, wired in by `description_prefix` in `garments/cc1717-dated.json`.
4. Print the source ledger in chat (VERIFIED by tier / CONFLICTS RESOLVED / VOLATILE / OMITTED). Evan spot-checks it.

Every description passes through `description_html.compose_description()` at assembly (all three compose sites): the temple facts are rewrapped as collapsed `<details>` rows (temple name + spec rows, then one row per h4 block; the as-of line stays visible) styled by a scoped `<style>` block shipped inside the section (dividers, 12px rows, +/− indicator; the theme hides default markers), the size-guide video gains `controls="controls"` and `preload="metadata"` so iPhones that decline autoplay still get a play button, and the size-guide measurements table is trimmed off because the video is the size guide (all Evan's 26 Aug 2026 decisions). The vendored skill assets and the Temples/ fragments stay verbatim; never wrap them by hand. Transforms are idempotent, so re-composing extracted live facts converges byte-exact.

Catalog-wide description passes: `scripts/write_description.py --normalize [--via-publish] [--only "title text"] [--report-only]`. `--normalize` rewrites anything differing from the repo's current copy; `--via-publish` syncs stale Shopify copies by publishing from Printify with ONLY the description flag on (measured safe 26 Aug 2026: art card, color order, handle, status all survive; a full-flag publish is the destructive republish, never use it for this). Without `--via-publish` it writes descriptionHtml to Shopify directly. The Shopify comparison is entity-insensitive because the Printify connector decodes entities on push (&sup2; arrives as a literal superscript two).

Deltas from the claude.ai skills: write target is Printify (never the Shopify connector from here), no product resolution step (product ids come from status.json), and With Date products DO get descriptions. Evan's claude.ai description event still runs post-publish; it currently hard-stops on the new title patterns, and if revived it would write un-collapsed markup that a `--normalize` run re-converges.

## New temple not in temples.json

The generator hard-stops rather than guessing. Research the temple's PHYSICAL city (churchofjesuschristtemples.org is the reference; the physical city can differ from the name: Washington D.C. Temple prints KENSINGTON, MARYLAND). Add the entry with `verified: true` and the format `CITY, STATE` (spelled out) or `CITY, COUNTRY`, then re-run. If sources are unclear, ask Evan instead of guessing.

## Adding a garment

1. Evan duplicates a product of the new garment type in Printify.
2. Copy an existing `garments/*.json`; fill blueprint_id, print_provider_id, and print area px from the duplicate/catalog API; set layout_profile, product_type, naming pattern, description_skill.
3. Run one temple with `--garments {new_id}`, Evan eyeballs it in the editor before it goes near the sweep. Spacing overrides go in the garment config, never in code.

Adding a layout profile (genuinely new arrangement): one function in `layout.py` plus a `PROFILES` entry. That is the only layout code change ever needed.

## Temples/All mirror (digital download files)

`Temples/All/` holds a flat duplicate of every temple's black SVG named by
its CLEAN place token (`Manhattan black.svg`, `Ogden Original black.svg`,
no stars). It feeds the Temple Art File digital product's delivery app.
`mirror_black_art()` in generate.py maintains it automatically on every
sweep and `--temple` run (refreshes when source art is newer). `All` is NOT
a temple folder: the sweep skips it, and any new script walking `Temples/`
must skip it too.

## Art close-up images (post-publish, Shopify side)

Every product gets a black-art-on-white close-up card at gallery position 2 on Shopify. Cards auto-render to `Temples/{Name}/{Name} art closeup (auto).png` (an Evan-made file without "(auto)" overrides). Run `scripts/art_images.py push --all` at the end of every sweep: it snapshots the whole catalog in a few bulk queries, matches every temple product by longest place token (Provo City Center beats Provo), and cards anything missing one. Scope per Evan's explicit rule (17 Aug 2026): ANY temple product on Shopify, hand-built or generated; copies, templates, and test titles are excluded. Idempotent via the alt marker "Temple line art close-up". Requires SHOPIFY_STORE_DOMAIN and SHOPIFY_ADMIN_TOKEN in .env; if absent, say so and skip.

## Temple dropdown option sets (Easify, Shopify side)

Every product page shows a "Temple" dropdown (Easify Product Options app) cross-linking the other temples' products of the same garment line. The canonical option-sets CSV lives at `artifacts/easify/option-sets.csv` (committed); the Easify app is downstream of it. `artifacts/easify/sets.json` maps garment lines to sets.

Run `scripts/easify_options.py sync` after `art_images.py push --all` whenever Evan has published products (or on request). It reads the live catalog, verifies every option's label and URL against the real handles (never derived from titles), adds newly published temples alphabetically, creates configured sets that do not exist yet (placeholder ids 900001+), and rewrites the CSV only when something changed. Rows are never deleted, only fixed, added, or reported. Evan then imports the CSV in the Easify app by hand; importing is manual like publishing, never automated. If an import created a new set, Evan exports fresh from Easify once and we run `scripts/easify_options.py reseed --export <file>` so the real ids replace the placeholders; commit the reseeded CSV. Same .env Shopify creds as the art push; if absent, say so and skip.

## After every run

End-of-run sequence once generation and descriptions are done: `scripts/add_date_layer.py` (adds date layers to dated drafts via the browser), then `scripts/publish_drafts.py` (auto-publishes base drafts and verified dated drafts, and applies the Shopify fixups to each; wait for it to confirm), then `scripts/art_images.py push --all` (give Shopify a couple of minutes to finish ingesting mockups first), then `scripts/easify_options.py sync`, then `scripts/shopify_fixups.py all` (a no-op after a clean publish run, but any Printify republish re-syncs variants and pushes the hoodie colorway back to True Navy, so it is worth the pass). Evan's remaining manual steps: flip Economy shipping on for newly published products in the Printify UI (post-publish, whenever; the publish output lists which ones need it), and the Easify CSV import.

Commit and push any repo changes the run produced: new or edited temples.json entries, description ledgers in artifacts/description-ledgers/, the Easify CSV in artifacts/easify/, and any code or config changes. The remote is Evan's PERSONAL GitHub, peculiarmarketing, over HTTPS using the repo's configured origin; never wire this repo to his work GitHub account (edavis821). Files in Temples/ (manifests, facts fragments, status, auto renders) live outside the repo and are not committed.

## Republishing an already-published product

`scripts/republish.py` re-pushes title, description, images and variants
together. Measured 22 Aug 2026: it keeps the title and the listing status,
but it DELETES the art close-up cards, reverts the hoodie's Blue Jean colorway
to Printify's True Navy, reverts the Color option order so pages stop opening
on the wanted color, and does NOT change the featured image. The script runs
the three repair passes itself afterward; never run it with `--skip-repair`
and walk away. Unclaimed "Copy of ..." drafts are never republished because
publishing one creates a junk storefront product.

Three different things are called "default" and setting one does not set the
others: Printify's `variants[].is_default` (`scripts/default_variant.py`),
Shopify's preselected variant, which is variant position 1 and follows the
Color option value order (`shopify_fixups.py color-order`), and the featured
photo, which is gallery position 1 (`shopify_fixups.py featured-photo`).

## Hard rules

- Place tokens live in manifests and may differ from folder names ("Washington DC" folder, "Washington D.C." token). Never derive one garment's title from another's.
- Never create a title that exactly duplicates an existing product except via `--replace`. Nesting is no longer a concern: the place token is parenthesized at the end of the title.
- Do not modify the description skills, the tracer outputs, or anything in `Temples/` beyond manifests, status files, and `(auto)` renders.
- Do not touch Lease End files or projects, ever.
