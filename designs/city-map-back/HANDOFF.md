# City map line: handoff (9 October 2026)

Read `README.md` in this folder first: it holds every settled decision (frame, line weights, hand-drawn style, front logo, product page, stages). This file is only where the work stopped and what is next.

## Where it stands

| Stage | Maps |
|---|---|
| live | Nauvoo, Salt Lake City (tee, sweatshirt, hoodie each; Salt Lake City is the map line's parent) |
| ready (Evan confirmed) | Kirtland, Sharon |
| review (design package and history built, waiting on Evan on the review page) | the other 25: San Antonio plus 24 Church history sites |

Stages live in `places.json` (`status`), defined in its `_status` note and in README "Product stages".

- **Design packages** (print files per garment, gallery cards, a review sheet) are built for all 29 by `temple-product-generator/scripts/map_run.py <place> --review`. They are gitignored and rebuild in about 20 seconds per map: `artifacts/maps/<place>/` (print files, `<place> map card.png`, `<place> logo card.png` when the front has coordinates, `<place> review.png`). The 300 dpi art they are made from is in `out/<place>/` here, also gitignored, rebuilt by `build_map_back.py <place>`.
- **History sections** exist for Nauvoo, Salt Lake City, Kirtland and Sharon (`history/<place>.html` with `history/<place>-sources.md`). **None exist yet for the other 24 Church history sites.** San Antonio needs none (`history: false`).

## What Evan asked for and what is next

Evan (9 Oct): "make them all and I will confirm them in one go".

**Done 9 Oct (second session):** all 24 history sections written by eight regional research agents to the History brief below, each with its `-sources.md` ledger; reviewed in full by the main session (two edits: Whitingham's birth hill hedged, Winter Quarters "land of the Omaha people"). Palmyra: one section, written against the small village frame, copied byte for byte to `palmyra-township.html`. Haun's Mill has a "Notes" heading in place of Trivia. All 28 sections parse with `map_run.py`'s `history_section`.

**Waiting on Evan: the review page** https://claude.ai/artifact/W18sJPW4zEjL2a5Rb89Kew (private to Evan). Every map in review with its back print, the print-file and card strip, the open points for him, and its history section. He picks Confirm / Needs changes / Drop per map with a note, plus the Palmyra village-or-township question. Choices save to the page's database: read them with ArtifactData `list` on collection `decisions` (doc id = place key: `choice`, `note`, `at`) and `get` `questions/palmyra`. The page builder (`build_page.py`, `template.html`, `notes.json`, `make_images.py`) lived in the session scratchpad and was not kept; the open points per map are in each history ledger and summarised on the page.

Next, once Evan has chosen:
1. `map_run.py <place> --confirm` for each he confirmed (status ready). Apply his notes for "Needs changes" (history fixes go back through the History brief; re-check the ledger). "Drop" on San Antonio means no product; on a history site, ask whether to remove it from `places.json`.
2. **Products** only when Evan asks: `map_run.py <place> --apply --publish` (refuses anything below ready), then `easify_options.py sync --maps-only` and Evan imports the CSV, then he exports and the CSV is reseeded (every Easify import renumbers all sets).

Open points Evan was asked on the page (also in the ledgers): Fayette organized in Fayette or both accounts; Independence's July 1833 editorial left out under the no-blame rule; Sacred Grove witness-tree source (BYU article, not a Church page); Council Bluffs replica tabernacle demolished 2022 (copy says so); Quincy stake today unconfirmed.

## Decisions Evan still owes

- **Palmyra has two maps** (`palmyra-village`, 3 km; `palmyra-township`, 10 km, with the temple in frame). Both are labelled PALMYRA, NEW YORK, so they would get the same product title and Easify label; `map_run.py` refuses a duplicate title. Pick one, or rename one. One Palmyra history section can serve both if its "On the Map" list holds only places inside the smaller village frame.
- **San Antonio** is a city, not a Church history site: confirm it should be a product at all.
- **Salt Lake City prints at 0.5 mm** lines, under the 0.71 mm DTG minimum for the tee. A sample tee was suggested, not yet ordered.
- **Fayette's** frame takes in Waterloo and Seneca Falls, which show as dense knots (flagged 8 Oct, no action requested).

## Also open (from earlier in the line)

- Four collections (Tees, Sweatshirts, Hoodies, Jackets) were created unpublished; Evan ticks Online Store on each in the admin if not done.
- On-model gallery photos for map products need the Mac (blank garment photos live only there).
- Preston, England is not built: TIGER is US only and OpenStreetMap was unreachable.
- The two temple-worded FAQ rows ("Is it appropriate to wear a temple on a shirt?", Temple Art File) still show on map pages; Evan has not decided.

## Historical maps: closed (Evan, 9 Oct)

Evan saw the side-by-side (1847 Salt Lake plat, 1859 Nauvoo inset, next to today's backs) and decided: **no historical maps; every map stays on today's TIGER roads.** Do not reopen it. The research (`historical-maps.md`), the LoC samples with their license manifest, the traces and `build_historical.py` stay in the repo as the record of why.

## History brief

Each agent reads this, plus the four finished sections for format, tone and ledger style.

- Invoke the `anthropic-skills:temple-fact-checker` skill and follow its research standard (source hierarchy, myths screen, every fact sourced, never from memory). Read BRAND.md voice and guardrails.
- Sources in order: churchofjesuschrist.org (Church History Topics, Saints, Gospel Library, D&C headings, Church History Sites, Newsroom), Church News, Joseph Smith Papers, Church History Library, BYU Studies, Ensign/Liahona; then academic and state or NPS/National Register sources. Wikipedia, blogs, Find a Grave and tourism sites are leads only. When good sources disagree: the more authoritative, or both when both are Church sources, or leave it out.
- Sensitivity: persecution and loss (Missouri 1833 and 1838, Haun's Mill, Liberty Jail, Carthage, the trail, the handcart companies) stated plainly from Church sources, no graphic detail, no blame beyond the sources, no speculation. Sites owned or shared by other churches described neutrally or left out. Haun's Mill gets no light trivia.
- Shape: `<section class="site-history">`, an h3 "Place, State", 2 to 4 `site-history__row` spec rows (bold label, br, text), h4 What Happened Here (3 to 7 dated bullets with `<time>`), h4 On the Map (2 to 6 landmarks inside the map frame, plain sentences), h4 Trivia (2 to 3, not ending reverent or moral), then the `site-history__asof` line. No em dashes, no en dashes as dashes, no inline styles, never describe the shirt. Fewer, stronger items beat padding.
- Ledger: `history/<key>-sources.md` with every fact, URL and tier, a Dropped list with reasons, and landmark coordinates.
- Run `.claude/skills/humanizer/scripts/copy_scan.py` and `.claude/skills/structural-humanizer/scripts/structural_scan.py` on each and fix what they flag. Agents do not commit.
