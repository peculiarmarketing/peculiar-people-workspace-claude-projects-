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

## Numbered landmark markers (Evan, 9 Oct: build on all Church history maps)

Evan: "build the numbered list structure on all the church history maps with any relevant history, locations, events, as best as we might know where they are. If we are not positive that's where they are or where they happened, note that in the on the map section. Also ensure that the numbers are big enough to be printed correctly, but not ridiculously big. Do this on all church history maps, including Salt Lake and Nauvoo."

Done 9 Oct:
- Each of the 26 Church history maps has `history/<place>-markers.json` (n, name, lat, lon, certainty exact/approximate/traditional, kind site/temple, coordinate source) and its On the Map list is now `<ol class="site-history__list site-history__map">`, one item per marker in the same order. Every approximate or traditional item says so in plain words. Each ledger has a "## Markers (9 Oct 2026)" section (coordinates, sources, merges, places left out). 85 markers in all; places closer than 0.35 in on the print were merged into one number.
- `build_map_back.py` draws them (`draw_markers`): a 0.055 in radius dot with streets cleared to 0.11 in, and the number in Oswald 500 at 0.264 in (10 percent over the first 0.24 in, which measured 0.85 mm strokes and 4.9 mm tall; DTG minimum 0.71 mm) on a knocked-out patch placed automatically clear of other markers, the halo, the frame and the city label. A temple entry gets only its number, outside the halo. `web_map_drawing.py` passes the markers too, so the product-page drawing band shows them.
- `map_run.py` (temple repo) ships a scoped style that forces the On the Map numbers on, whatever the theme does to lists.
- Status: all 26 stay at ready (Evan confirmed the maps and asked for the markers). Nauvoo and Salt Lake City are LIVE with the old art and old list: they need `map_run.py <place> --apply --publish` again to carry the markers, only when Evan says. Same for every other map when its products go up.
- **Confirmed by Evan, 9 Oct (final pass):** all 26 maps with markers, the thin crowded patches, numbers directly above the dot with 2 mm clearance and 1 mm more space, 0.29 in numbers. Nothing left to review on the map line; products wait only on Evan saying to publish (`map_run.py <place> --apply --publish`, then Easify; Nauvoo and Salt Lake City republish to carry the new art).
- The markers review page https://claude.ai/artifact/1aJvbn7Hgn7tYgY1H7EN8p (private to Evan). All 26 maps with markers, the print strip and the numbered list. Choices save to collection `markers` (doc id = place key: `choice` confirm/change/drop, `note`); read with ArtifactData `list`. "Drop" there means drop the markers, keep the map. The earlier map review page (https://claude.ai/artifact/W18sJPW4zEjL2a5Rb89Kew, collection `decisions`) holds his 9 Oct map choices.
- **Evan's markers review (9 Oct):** 24 confirmed. Mendon: "the actual number for #1 lies in the roadway so it looks like the road ... it should be moved off the road" (fixed for every map: number spots are now scored by the street ink under them). Salt Lake City: "#7 is covered by the location text, zoom out just enough" (widened 22 to 24.5 km, Davis County 49011 loaded, 5.3 percent fused). Then, for all maps: numbers and dots 10 percent bigger, and then (after the road-avoiding placement pushed numbers away from their dots) Evan: numbers go directly above the dot with 2 mm of clearance around number and dot, except Mendon 1 (number to the right, `label_at` in its markers file), and another 10 percent bigger: number 0.29 in, dot radius 0.06 in.
- Flags for Evan on that page: Whitingham marker 1 (traditional birth site) is placed from a non-Church lead; Colesville's tavern source says Harpursville but names a corner 4.6 km away.

## Thin lines in crowded patches (Evan, 9 Oct)

Evan: "where the roads start blending together and forming solid white blocks ... make the roads where that's the case 0.5 millimeters, but then all the roads outside of it the 1.5", naming Fayette's far left and lower rows. Built into `build_map_back.py` (`dense_field`, see README) and `web_map_drawing.py`; applies to every 1.5 mm map automatically, so all small-town maps were rebuilt 9 Oct. Share of each map thinned (patches under 0.2 sq in skipped as lone knots): Fayette 6.3 percent, Mendon 3.8, Winter Quarters 2.7, Colesville 1.7, Afton 1.4, Richmond 1.2, Manchester 1.1, Harmony 1.0, the rest under 1; Nauvoo, Far West, Haun's Mill, Garden Grove and Mount Pisgah unchanged. Shown to Evan on the markers review page and a Fayette before-and-after. Thin patches are under the 0.71 mm DTG tee minimum, like Salt Lake City; the sample tee would settle both.

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
