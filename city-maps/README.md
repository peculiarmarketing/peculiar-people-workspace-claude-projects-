# City maps

Street maps of any town, from OpenStreetMap, as SVG and PNG. `church-history-sites.md` lists the 29 Church history sites already downloaded. This is raw material for designs (Nauvoo, Kirtland, Carthage, Palmyra and the rest). It only gets the map out. The designs happen later, somewhere else.

Two tools share one data folder:

- `fetch_map.py` names a town and writes print-ready files. Use it by default.
- `city-roads/` is our copy of anvaka's city-roads web app, for looking around and exporting by eye.

## Why anvaka's site fails on small towns

Checked 7 October 2026. Search was never the problem; Nominatim finds Nauvoo and Kirtland fine.

1. The site's fast cache only covers about 3,000 cities over 100,000 people. Every small town falls through to a live Overpass query.
2. That query reserves a 900 second timeout and 1 GB of server memory. A busy Overpass server refuses reservations that big with a 504 ("the server is probably too busy").
3. Most of its backup servers are dead (broken certificate, 500s, 504s), so nothing catches the failure.

Our versions ask for 180 seconds and the default memory, retry a busy server with a wait, use mirrors that work, and save every town to `data/` so it is downloaded once.

## fetch_map.py

```bash
city-maps/.venv.nosync/bin/python city-maps/fetch_map.py "Nauvoo, Illinois" "Kirtland, Ohio"
```

Each town gives four files in `out/<town>/`: black and white, SVG and PNG, transparent background, no other styling. PNGs are 6000 px wide at 300 dpi.

Options:

- `--filter roads` (default, every `highway`), `roads-basic`, `roads-strict`, `all-ways`, `buildings`. Same filters as the web app.
- `--format svg|png|both` and `--png-width 6000`.
- `--radius 3` maps a 6 km square around the place instead of its boundary, with roads cut at the edge. Use it for sites with no town (Far West, Adam-ondi-Ahman) and for tiny villages whose boundary map is mostly one passing highway. The first match wins, so write the name precisely.
- `--trim` cuts every road at the town's official boundary and writes `-trimmed` files beside the untrimmed ones, framed to the town's outline. The boundary is fetched once and saved as `data/<area id>-boundary.json`. Square (`--radius`) maps are skipped since they are already cropped.
- `--all-towns` runs every saved place that has a town boundary. `fetch_map.py --trim --all-towns` re-trims the whole set.
- `--refresh` downloads again even if the town is saved.

If a place fails (the Overpass servers are often busy for bigger cities), the rest of the batch still runs and the failures are listed at the end. Run those again a few minutes later.

Be specific with names. The script prints which place it matched, so check it. "Palmyra, New York" matches the village, not the larger Town of Palmyra. Ask for "Town of Palmyra, New York" when you want the township. A matched place is remembered in `data/index.json`; delete its entry to look it up again.

A road that crosses the town line comes back whole, so the untrimmed maps can have a highway trailing off past the edge (Carthage, Garden Grove). The `-trimmed` files fix that. The web app has the same trailing roads.

Setup, once, if the venv is missing:

```bash
/opt/homebrew/bin/python3 -m venv city-maps/.venv.nosync && city-maps/.venv.nosync/bin/pip install -r city-maps/requirements.txt
```

## The web app (city-roads/)

Our fork, github.com/peculiarmarketing/city-roads, on branch `peculiar` (the default). `origin` is the fork, `upstream` is anvaka. It is its own git repo and is ignored by this one. Changes from upstream:

- `src/lib/LoadOptions.js`: 180 s timeout, no 1 GB reservation.
- `src/lib/postData.js`: working mirror list, retries a busy server three times.
- `src/components/FindPlace.vue` and `src/config.js`: checks `city-maps/data/` first, so any town fetched by the script opens instantly.
- `vite.config.js`: serves `city-maps/data/` at `/local-data`.

Run it from a terminal, then open http://127.0.0.1:8080:

```bash
cd city-maps/city-roads && npx vite --host 127.0.0.1 --port 8080
```

The Claude app's preview button cannot start it, because macOS blocks that process from reading iCloud Drive. Start it from a terminal or ask Claude to. Export lives under Customize, then Export. `node_modules` is a symlink to `node_modules.nosync` so iCloud skips it; run `npm install` there if it goes missing.

## Licence: read before anything ships

The map data is OpenStreetMap, under the ODbL. A design made from it counts as a "Produced Work". That allows commercial use but needs the credit "© OpenStreetMap contributors" somewhere a buyer could reasonably see it, such as the product page. This is open and Evan decides how to handle it before any map design goes live.
