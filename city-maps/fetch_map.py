#!/usr/bin/env python3
"""Download a town's street map from OpenStreetMap and export it as SVG and PNG.

    python fetch_map.py "Nauvoo, Illinois" "Kirtland, Ohio"

Each town is looked up once with Nominatim and downloaded once from Overpass.
The raw result is saved in data/, so later runs (and the city-roads web app)
read it from disk. Exports land in out/<slug>/ in black and in white, on a
transparent background, with no other styling.

Map data (c) OpenStreetMap contributors, ODbL. See README.md before shipping
anything made from it.
"""

import argparse
import json
import math
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image, ImageDraw

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
OUT = HERE / "out"
INDEX = DATA / "index.json"

USER_AGENT = "PeculiarPeople-city-maps/0.1 (+https://peculiarpeopleco.com)"
NOMINATIM = "https://nominatim.openstreetmap.org/search"

# Checked 7 Oct 2026. overpass.osm.jp has a broken TLS certificate and
# maps.mail.ru / overpass.private.coffee were returning 504 and 500.
OVERPASS = [
    "https://overpass-api.de/api/interpreter",
    "https://overpass.kumi.systems/api/interpreter",
    "https://overpass.private.coffee/api/interpreter",
]

# Same filters as the statics in city-roads/src/lib/Query.js.
FILTERS = {
    "roads": 'way[highway]',
    "roads-basic": 'way[highway~"^(motorway|primary|secondary|tertiary)|residential"]',
    "roads-strict": 'way[highway~"^(((motorway|trunk|primary|secondary|tertiary)(_link)?)|unclassified|residential|living_street|pedestrian|service|track)$"][area!=yes]',
    "all-ways": 'way',
    "buildings": 'way[building]',
}

SVG_WIDTH = 2000      # SVG user units; the stroke below is relative to this
SVG_STROKE = 1.2
MARGIN = 0.02         # fraction of the long side left empty on each edge
SUPERSAMPLE = 2       # PNG lines are drawn this much larger, then scaled down to antialias


def slugify(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def http(url, data=None, timeout=200):
    body = urllib.parse.urlencode(data).encode() if data else None
    req = urllib.request.Request(url, data=body, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read())


def load_index():
    return json.loads(INDEX.read_text()) if INDEX.exists() else {}


def save_index(index):
    INDEX.write_text(json.dumps(index, indent=2, sort_keys=True) + "\n")


def lookup(query, index):
    """Resolve a place name to an OSM area id (or a bbox), using the index first."""
    slug = slugify(query)
    if slug in index:
        return slug, index[slug]

    rows = http(NOMINATIM + "?" + urllib.parse.urlencode({"format": "json", "q": query}))
    time.sleep(1)  # Nominatim usage policy: at most one request per second
    if not rows:
        raise SystemExit(f"Nominatim found nothing for {query!r}")

    # Prefer a place with a boundary; fall back to the first hit's bounding box.
    row = next((r for r in rows if r["osm_type"] in ("relation", "way")), rows[0])
    area_id = None
    if row["osm_type"] == "relation":
        area_id = int(row["osm_id"]) + 3600000000
    elif row["osm_type"] == "way":
        area_id = int(row["osm_id"]) + 2400000000
    s, n, w, e = (float(x) for x in row["boundingbox"])
    place = {
        "query": query,
        "name": row["display_name"],
        "osm": f'{row["osm_type"]}/{row["osm_id"]}',
        "area_id": area_id,
        "bbox": [s, w, n, e],
    }
    index[slug] = place
    save_index(index)
    return slug, place


def overpass_query(place, wayfilter):
    if place["area_id"]:
        return (f'[timeout:180][out:json];area({place["area_id"]})->.a;'
                f'({wayfilter}(area.a);node(w););out skel;')
    bbox = ",".join(str(x) for x in place["bbox"])
    return f'[timeout:180][out:json][bbox:{bbox}];({wayfilter};node(w););out skel;'


def download(place, wayfilter):
    """Ask each Overpass server in turn, retrying busy ones with backoff."""
    query = overpass_query(place, wayfilter)
    last = None
    for server in OVERPASS:
        for attempt in range(3):
            try:
                result = http(server, {"data": query})
                if "elements" not in result:
                    raise ValueError("no elements in response")
                return result
            except urllib.error.HTTPError as err:
                last = f"{server}: HTTP {err.code}"
                if err.code not in (429, 503, 504):
                    break  # this server is broken, not busy; try the next one
            except (urllib.error.URLError, TimeoutError, ValueError) as err:
                last = f"{server}: {err}"
                break
            wait = 10 * (attempt + 1)
            print(f"  {last}, retrying in {wait}s")
            time.sleep(wait)
        print(f"  {last}, trying next server")
    raise SystemExit(f"Every Overpass server failed. Last error: {last}")


def get_data(slug, place, filter_name, refresh):
    """Return the Overpass result for this place, from disk when we have it."""
    # Named by area id so the web app can find it from a search result.
    key = place["area_id"] or slug
    path = DATA / f"{key}-{filter_name}.json"
    if path.exists() and not refresh:
        print(f"  cached: {path.relative_to(HERE)}")
        return json.loads(path.read_text())

    print(f"  downloading {filter_name} from Overpass...")
    result = download(place, FILTERS[filter_name])
    result["pp_meta"] = {
        "query": place["query"],
        "name": place["name"],
        "filter": filter_name,
        "fetched": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    path.write_text(json.dumps(result, separators=(",", ":")))
    print(f"  saved: {path.relative_to(HERE)} ({path.stat().st_size // 1024} KB)")
    return result


def project(result):
    """Turn ways into lists of Web Mercator (x, y) points, y pointing down."""
    nodes = {}
    for el in result["elements"]:
        if el["type"] == "node":
            lat = max(min(el["lat"], 85.0), -85.0)
            nodes[el["id"]] = (
                math.radians(el["lon"]),
                -math.log(math.tan(math.pi / 4 + math.radians(lat) / 2)),
            )
    lines = []
    for el in result["elements"]:
        if el["type"] == "way":
            pts = [nodes[n] for n in el.get("nodes", []) if n in nodes]
            if len(pts) >= 2:
                lines.append(pts)
    return lines


def fit(lines, width):
    """Scale lines to fit a canvas `width` wide; return (lines, width, height)."""
    xs = [x for line in lines for x, _ in line]
    ys = [y for line in lines for _, y in line]
    minx, maxx, miny, maxy = min(xs), max(xs), min(ys), max(ys)
    spanx, spany = (maxx - minx) or 1e-9, (maxy - miny) or 1e-9
    pad = MARGIN * max(spanx, spany)
    scale = width / (spanx + 2 * pad)
    height = round((spany + 2 * pad) * scale)
    fitted = [[((x - minx + pad) * scale, (y - miny + pad) * scale) for x, y in line]
              for line in lines]
    return fitted, width, height


def write_svg(lines, path, colour, title):
    fitted, w, h = fit(lines, SVG_WIDTH)
    paths = "\n".join(
        '<path d="M' + " L".join(f"{x:.1f} {y:.1f}" for x, y in line) + '"/>'
        for line in fitted
    )
    path.write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<!-- Map data (c) OpenStreetMap contributors, ODbL. -->\n'
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">\n'
        f'<title>{title}</title>\n'
        f'<g fill="none" stroke="{colour}" stroke-width="{SVG_STROKE}" '
        f'stroke-linecap="round" stroke-linejoin="round">\n{paths}\n</g>\n</svg>\n'
    )


def render_mask(lines, png_width):
    """Draw the lines into a greyscale mask at PNG size, antialiased by supersampling."""
    big = png_width * SUPERSAMPLE
    fitted, w, h = fit(lines, big)
    stroke = max(1, round(SVG_STROKE * big / SVG_WIDTH))
    mask = Image.new("L", (w, h), 0)
    draw = ImageDraw.Draw(mask)
    r = stroke / 2
    for line in fitted:
        draw.line(line, fill=255, width=stroke, joint="curve")
        for x, y in (line[0], line[-1]):  # round caps
            draw.ellipse((x - r, y - r, x + r, y + r), fill=255)
    return mask.resize((png_width, round(h / SUPERSAMPLE)), Image.LANCZOS)


def write_png(mask, path, rgb):
    img = Image.new("RGBA", mask.size, rgb + (0,))
    img.putalpha(mask)
    img.save(path, dpi=(300, 300), optimize=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("places", nargs="+", help='e.g. "Nauvoo, Illinois"')
    ap.add_argument("--filter", choices=FILTERS, default="roads")
    ap.add_argument("--format", choices=("svg", "png", "both"), default="both")
    ap.add_argument("--png-width", type=int, default=6000)
    ap.add_argument("--refresh", action="store_true", help="re-download even if cached")
    args = ap.parse_args()

    DATA.mkdir(exist_ok=True)
    index = load_index()
    for query in args.places:
        slug, place = lookup(query, index)
        print(f"{query} -> {place['name']} ({place['osm']})")
        result = get_data(slug, place, args.filter, args.refresh)
        lines = project(result)
        if not lines:
            print(f"  no ways found for {query}, skipping")
            continue

        outdir = OUT / slug
        outdir.mkdir(parents=True, exist_ok=True)
        base = f"{slug}-{args.filter}"
        title = f"{place['name']}: {args.filter}"
        if args.format in ("svg", "both"):
            write_svg(lines, outdir / f"{base}-black.svg", "#000", title)
            write_svg(lines, outdir / f"{base}-white.svg", "#fff", title)
        if args.format in ("png", "both"):
            mask = render_mask(lines, args.png_width)
            write_png(mask, outdir / f"{base}-black.png", (0, 0, 0))
            write_png(mask, outdir / f"{base}-white.png", (255, 255, 255))
        print(f"  {len(lines)} ways -> {outdir.relative_to(HERE)}/")


if __name__ == "__main__":
    sys.exit(main())
