# City map line: handoff (9 October 2026)

Read `README.md` in this folder first: it holds every settled decision (frame, line weights, hand-drawn style, front logo, product page, stages). This file is only where the work stopped and what is next.

## Where it stands

| Stage | Maps |
|---|---|
| live | Nauvoo, Salt Lake City (tee, sweatshirt, hoodie each; Salt Lake City is the map line's parent) |
| ready (Evan confirmed) | Kirtland, Sharon |
| review (design package built, waiting on Evan) | the other 25: San Antonio plus 24 Church history sites |

Stages live in `places.json` (`status`), defined in its `_status` note and in README "Product stages".

- **Design packages** (print files per garment, gallery cards, a review sheet) are built for all 29 by `temple-product-generator/scripts/map_run.py <place> --review`. They are gitignored and rebuild in about 20 seconds per map: `artifacts/maps/<place>/` (print files, `<place> map card.png`, `<place> logo card.png` when the front has coordinates, `<place> review.png`). The 300 dpi art they are made from is in `out/<place>/` here, also gitignored, rebuilt by `build_map_back.py <place>`.
- **History sections** exist for Nauvoo, Salt Lake City, Kirtland and Sharon (`history/<place>.html` with `history/<place>-sources.md`). **None exist yet for the other 24 Church history sites.** San Antonio needs none (`history: false`).

## What Evan asked for and what is next

Evan (9 Oct): "make them all and I will confirm them in one go". The packages are built; the history sections are not.

1. **Write the 24 history sections.** The brief every research agent follows is reproduced below under "History brief". Eight regional groups worked well in planning (Whitingham, Mendon, Fayette | Palmyra, Manchester, Sacred Grove | Colesville, Afton, Harmony | Hiram, Richmond, Liberty | Independence, Far West, Adam-ondi-Ahman | Haun's Mill, Quincy, Carthage | Garden Grove, Mount Pisgah, Council Bluffs | Winter Quarters, Martin's Cove). Each map's frame bounds come from `places.json` (centre, width_km, 3:4 portrait). The first attempt was stopped by Evan before any agent ran; nothing was written.
2. **Review each section yourself** after the agent: both editing passes (CLAUDE.md), check any phrase that sounds like a guess against the `-sources.md` ledger, and vary the shapes. Shape convergence is the main risk across 28 sections: the existing four end on a concrete fact (Nauvoo), a myth correction (Salt Lake City), a light anecdote (Kirtland), a weather story (Sharon). Do not let them all close the same way.
3. **One review page for Evan** with every map's review sheet and history section side by side, so he confirms in one go. Then `map_run.py <place> --confirm` for each he approves (it refuses a history site with no history file).
4. **Products** only when Evan asks: `map_run.py <place> --apply --publish` (refuses anything below ready), then `easify_options.py sync --maps-only` and Evan imports the CSV, then he exports and the CSV is reseeded (every Easify import renumbers all sets).

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

## Historical maps: the next session starts here (9 Oct)

Evan wants to understand these before anything is made. Do not build products or confirm any history section until he has seen this. Full research: `historical-maps.md` in this folder (per-place tables, licenses word for word, earliest USGS quads, OpenHistoricalMap counts, failed requests). Starting brief: the Claude Docs page "Historical Street Map Sources: Research Brief for Claude Code" (https://claude.ai/artifact/YWqHSXnAKpZ9bZn4Rpa85e); read it with the Claude Docs connector (`read` ref node `8fd64ecc-b638` in container project `ff359f9f-4266-45de-99dd-f44f27f43861`).

**Evan's questions for the next session, in his words:** "how do these historic maps work? are they like the current maps just older with less roads? Do all of the resources work? None of them?"

### How they work (the short answer to give him, then show it)

They are not the current maps with fewer roads. The current maps are data: every road is a line in the Census TIGER files, and the code draws it. For the Church-era years no such data exists, except a little in OpenHistoricalMap (OHM). What does exist is **pictures of old maps**: scanned period plats and county maps. To get our white-line look from one, someone (or a script, with checking) has to **trace** its streets, then fit them to the modern street grid so the frame, the temple halo and the coordinates still line up (georeferencing). The result would be a much sparser drawing (Salt Lake City 1847 is 135 square blocks; Nauvoo 1859 about 150 blocks; Palmyra 1853 about 15 streets), and the old map's own year often trails the Saints' years by 15 to 30 years. The alternative is to print the old map itself as a vintage image, which is a different product look.

**Show, do not tell: done (9 Oct, second session).** `build_historical.py` drew the 1847 Salt Lake plat and the 1859 Nauvoo inset in the map-back style next to today's backs; results and method are in `historical-maps.md` under "Side-by-side test". Sheets: `out/historical/slc-1847-vs-today.png` and `nauvoo-1859-vs-today.png` (rebuild in about 25 seconds). Evan has seen them and has been walked through the six questions; **his answers are the next step.** Nothing else on historical maps until then.

### Did the resources work? (tested 9 Oct)

| Source | Worked? | What it gave | Commercial use |
|---|---|---|---|
| Library of Congress maps (loc.gov, IIIF image server) | **Yes, fully.** Item JSON, IIIF info.json and region crops all downloaded | The good maps: 1847 Salt Lake plat; 1850s county maps with insets for Nauvoo, Carthage, Palmyra, Kirtland, Hiram, Sharon; bird's-eye views | **Yes.** "free to use and reuse unless a Rights Advisory statement is present"; checked: none on the Salt Lake, Nauvoo, Palmyra or Kirtland items |
| OpenHistoricalMap (Overpass `https://overpass-api.openhistoricalmap.org/api/interpreter`) | **Yes, but nearly empty** for these places | Salt Lake City: 38 era streets. Elsewhere only turnpikes and the Mormon Trail; 12 of 28 frames have no roads at all | Yes (CC0 unless a feature says otherwise) |
| USGS topo maps (TNM API) | **Yes** | Earliest editions 1885 to 1954 per place: too late to be period maps | Yes (public domain) |
| Joseph Smith Papers / Church History Library | Pages load; catalog rights fields could not be read (JavaScript app) | City of Zion 1833, Kirtland 1833, Far West plats | **No without permission** (© Intellectual Reserve, all rights reserved; Intellectual Property Office, about 45 days) |
| NYPL Digital Collections | **No:** bot check blocks scripted requests | The true 1842 Gustavus Hills map of Nauvoo (NYPL calls it public domain) | Unconfirmed; Evan can open it in a browser |
| DPLA, a Missouri archive site | **No:** HTTP 403 | (Winter Quarters, Jackson County plat book leads) | Unknown |
| Allmaps (georeferencing lookup) | **No:** HTTP 403 for all six maps | Whether any of these maps is already georeferenced: unknown | Annotations CC0; images per holder |
| David Rumsey | Searched, not used: its robots.txt disallows the search path (8 searches were sent before that was read; then stopped, nothing downloaded) | Copies of maps LoC also holds | **No** (CC BY-NC-SA, non-commercial) |
| OldMapsOnline | Not tested (a finder that links to holding libraries) | | Per holding library |

So: **LoC works and is the backbone; OHM and USGS work but add little; the Church, NYPL, DPLA and Allmaps routes were blocked or restricted.** Places with nothing usable: the Missouri sites, the Iowa camps, Winter Quarters, Martin's Cove.

### Decisions to ask Evan after he has seen a side-by-side

The six questions at the end of `historical-maps.md`: separate "Historical" version vs replacement vs no; planned-but-never-built cities (City of Zion) in scope?; Church-held plats (ask permission, draw our own City of Zion from its written dimensions, or LoC only); an 1850s map for an 1830s site and which year the label shows; the NYPL 1842 Nauvoo map (Evan to open it in a browser); keep Missouri, Iowa, Winter Quarters and Martin's Cove on today's roads?

Rules carried from the brief: no scraping where a dump or bucket exists, respect robots.txt and terms, keep downloads small and in `historical/` with `manifest.json` recording source URL, license text and license URL for every file, report failed requests instead of working around them.

## History brief

Each agent reads this, plus the four finished sections for format, tone and ledger style.

- Invoke the `anthropic-skills:temple-fact-checker` skill and follow its research standard (source hierarchy, myths screen, every fact sourced, never from memory). Read BRAND.md voice and guardrails.
- Sources in order: churchofjesuschrist.org (Church History Topics, Saints, Gospel Library, D&C headings, Church History Sites, Newsroom), Church News, Joseph Smith Papers, Church History Library, BYU Studies, Ensign/Liahona; then academic and state or NPS/National Register sources. Wikipedia, blogs, Find a Grave and tourism sites are leads only. When good sources disagree: the more authoritative, or both when both are Church sources, or leave it out.
- Sensitivity: persecution and loss (Missouri 1833 and 1838, Haun's Mill, Liberty Jail, Carthage, the trail, the handcart companies) stated plainly from Church sources, no graphic detail, no blame beyond the sources, no speculation. Sites owned or shared by other churches described neutrally or left out. Haun's Mill gets no light trivia.
- Shape: `<section class="site-history">`, an h3 "Place, State", 2 to 4 `site-history__row` spec rows (bold label, br, text), h4 What Happened Here (3 to 7 dated bullets with `<time>`), h4 On the Map (2 to 6 landmarks inside the map frame, plain sentences), h4 Trivia (2 to 3, not ending reverent or moral), then the `site-history__asof` line. No em dashes, no en dashes as dashes, no inline styles, never describe the shirt. Fewer, stronger items beat padding.
- Ledger: `history/<key>-sources.md` with every fact, URL and tier, a Dropped list with reasons, and landmark coordinates.
- Run `.claude/skills/humanizer/scripts/copy_scan.py` and `.claude/skills/structural-humanizer/scripts/structural_scan.py` on each and fix what they flag. Agents do not commit.
