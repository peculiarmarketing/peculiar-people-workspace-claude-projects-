# City map line: handoff (9 October 2026)

Read `README.md` in this folder first: it holds every settled decision (frame, line weights, hand-drawn style, front logo, product page, stages). This file is only where the work stopped and what is next.

## Where it stands

| Stage | Maps |
|---|---|
| live | Nauvoo, Salt Lake City (tee, sweatshirt, hoodie each; Salt Lake City is the map line's parent) |
| ready (Evan confirmed) | Kirtland, Sharon, and 22 confirmed on the review page 9 Oct: San Antonio, Whitingham, Manchester, Fayette, Mendon, Colesville, Afton, Harmony, Hiram, Independence, Liberty, Richmond, Far West, Adam-ondi-Ahman, Haun's Mill, Quincy, Carthage, Garden Grove, Mount Pisgah, Council Bluffs, Winter Quarters, Martin's Cove |
| review | Palmyra township only: rebuilt 9 Oct to Evan's note (widened to 12.5 km, centre 43.0737, -77.2066, to take in the old Sacred Grove frame; history section merged from the village and Sacred Grove sections). Waits on Evan's look |
| dropped (9 Oct) | Palmyra village, Sacred Grove: removed from `places.json` (see its `_dropped` note); their ledgers stay as sources for Palmyra township |

- **Design packages** (print files per garment, gallery cards, a review sheet) are built for all 29 by `temple-product-generator/scripts/map_run.py <place> --review`. They are gitignored and rebuild in about 20 seconds per map: `artifacts/maps/<place>/` (print files, `<place> map card.png`, `<place> logo card.png` when the front has coordinates, `<place> review.png`). The 300 dpi art they are made from is in `out/<place>/` here, also gitignored, rebuilt by `build_map_back.py <place>`.
- **History sections** exist for Nauvoo, Salt Lake City, Kirtland and Sharon (`history/<place>.html` with `history/<place>-sources.md`). **None exist yet for the other 24 Church history sites.** San Antonio needs none (`history: false`).

## What Evan asked for and what is next

Evan (9 Oct): "make them all and I will confirm them in one go".

**Done 9 Oct (second session):** all 24 history sections written by eight regional research agents to the History brief below, each with its `-sources.md` ledger; reviewed in full by the main session (two edits: Whitingham's birth hill hedged, Winter Quarters "land of the Omaha people"). Palmyra: one section, written against the small village frame, copied byte for byte to `palmyra-township.html`. Haun's Mill has a "Notes" heading in place of Trivia. All 28 sections parse with `map_run.py`'s `history_section`.

**Waiting on Evan: the review page** https://claude.ai/artifact/W18sJPW4zEjL2a5Rb89Kew (private to Evan). Every map in review with its back print, the print-file and card strip, the open points for him, and its history section. He picks Confirm / Needs changes / Drop per map with a note, plus the Palmyra village-or-township question. Choices save to the page's database: read them with ArtifactData `list` on collection `decisions` (doc id = place key: `choice`, `note`, `at`) and `get` `questions/palmyra`. The page builder (`build_page.py`, `template.html`, `notes.json`, `make_images.py`) lived in the session scratchpad and was not kept; the open points per map are in each history ledger and summarised on the page.

Next, once Evan has chosen:
1. `map_run.py <place> --confirm` for each he confirmed (status ready). Apply his notes for "Needs changes" (history fixes go back through the History brief; re-check the ledger). On a history site, "Drop" means ask whether to remove it from `places.json`.
2. **Products** only when Evan asks: `map_run.py <place> --apply --publish` (refuses anything below ready), then `easify_options.py sync --maps-only` and Evan imports the CSV, then he exports and the CSV is reseeded (every Easify import renumbers all sets).

Evan's calls, 9 Oct: Fayette's "In Fayette or Manchester?" row removed ("skip it if you aren't sure"); Independence's July 1833 Star article added, verified by two Church sources ("include it if verified by multiple sources"); San Antonio stays a product, as a plain city map with no history section. Still open on the page: Sacred Grove witness-tree source (BYU article, not a Church page); Council Bluffs replica tabernacle demolished 2022 (copy says so); Quincy stake today unconfirmed.

## Proposal waiting on Evan: numbered landmark markers (9 Oct)

Evan asked for a way to mark where things happened on the Church history maps, explained on the product page. Mock-up on Palmyra township (built by a scratchpad script, not kept): a 0.11 in dot at each landmark with streets knocked out around it, and a number in Oswald 500 at 0.22 in (the city label's size, so strokes clear the DTG minimum) on a knocked-out patch beside it, placed automatically so it does not hit another marker or the temple halo. The numbers match a numbered On the Map list on the product page. Coordinates already sit in every history ledger. Not built into `build_map_back.py`; no decision yet. If approved: a `markers` list per place in `places.json` (number, name, lat, lon from the ledger), drawn by `build_map_back.py`, the On the Map list rendered as a numbered list, and the confirmed maps rebuilt and re-shown before any publish. Note: live Nauvoo and Salt Lake City would change design if markers are added to them.

## Next line of work (Evan, 9 Oct; not started)

Every city with a temple product gets a plain city map "in the near future": no history section (`history: false`), built and reviewed like San Antonio. Only plan or build this when Evan asks. A temple city's map should carry the temple halo and the coordinates front, since the temple is in frame by definition.

## Decisions Evan still owes

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
