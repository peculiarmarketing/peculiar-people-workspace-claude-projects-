#!/usr/bin/env python3
"""Download a town's street map from OpenStreetMap and export it as SVG and PNG.

    python fetch_map.py "Nauvoo, Illinois" "Kirtland, Ohio"

Each town is looked up once with Nominatim and downloaded once from Overpass.
The raw result is saved in data/, so later runs (and the city-roads web app)
read it from disk. Exports land in out/<slug>/ in black and in white, on a
transparent background, with no other styling.

    python fetch_map.py --trim --all-towns

--trim cuts every road at the town's official boundary (fetched once from
Nominatim and saved next to the road data) and writes "-trimmed" files beside
the untrimmed ones.

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

import numpy as np
import shapely
from PIL import Image, ImageDraw

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
OUT = HERE / "out"
INDEX = DATA / "index.json"

USER_AGENT = "PeculiarPeople-city-maps/0.1 (+https://peculiarpeopleco.com)"
NOMINATIM = "https://nominatim.openstreetmap.org/search"
NOMINATIM_LOOKUP = "https://nominatim.openstreetmap.org/lookup"

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


class FetchError(Exception):
    """One place failed; the rest of the batch should still run."""


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


def lookup(query, index, radius=None):
    """Resolve a place name to an OSM area id (or a bbox), using the index first.

    With `radius` (km), the map is a square that far around the first match
    instead of a boundary. Use it for sites with no town boundary (Far West,
    Adam-ondi-Ahman) and write the query precisely, since the first hit wins.
    """
    slug = slugify(query) + (f"-{radius:g}km" if radius else "")
    if slug in index:
        return slug, index[slug]

    rows = http(NOMINATIM + "?" + urllib.parse.urlencode({"format": "json", "q": query}))
    time.sleep(1)  # Nominatim usage policy: at most one request per second
    if not rows:
        raise FetchError(f"Nominatim found nothing for {query!r}")

    if radius:
        row = rows[0]
        lat, lon = float(row["lat"]), float(row["lon"])
        dlat = radius / 111.32
        dlon = radius / (111.32 * math.cos(math.radians(lat)))
        place = {
            "query": query,
            "name": row["display_name"],
            "osm": f'{row["osm_type"]}/{row["osm_id"]}',
            "area_id": None,
            "bbox": [lat - dlat, lon - dlon, lat + dlat, lon + dlon],
            "radius_km": radius,
        }
        index[slug] = place
        save_index(index)
        return slug, place

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
    raise FetchError(f"every Overpass server failed (last: {last})")


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


def mercator(lon, lat):
    lat = max(min(lat, 85.0), -85.0)
    return math.radians(lon), -math.log(math.tan(math.pi / 4 + math.radians(lat) / 2))


def clip_segment(a, b, box):
    """Liang-Barsky: the part of segment a-b inside box (x0, y0, x1, y1), or None."""
    (x0, y0), (x1, y1) = a, b
    dx, dy = x1 - x0, y1 - y0
    t0, t1 = 0.0, 1.0
    for p, q in ((-dx, x0 - box[0]), (dx, box[2] - x0), (-dy, y0 - box[1]), (dy, box[3] - y0)):
        if p == 0:
            if q < 0:
                return None
            continue
        r = q / p
        if p < 0:
            t0 = max(t0, r)
        else:
            t1 = min(t1, r)
        if t0 > t1:
            return None
    return (x0 + t0 * dx, y0 + t0 * dy), (x0 + t1 * dx, y0 + t1 * dy)


def clip_line(pts, box):
    """Split a polyline into the runs that fall inside box."""
    runs, run = [], []
    for a, b in zip(pts, pts[1:]):
        seg = clip_segment(a, b, box)
        if seg is None:
            if len(run) >= 2:
                runs.append(run)
            run = []
            continue
        if not run or run[-1] != seg[0]:
            if len(run) >= 2:
                runs.append(run)
            run = [seg[0]]
        run.append(seg[1])
    if len(run) >= 2:
        runs.append(run)
    return runs


def project(result, clip_bbox=None):
    """Turn ways into lists of Web Mercator (x, y) points, y pointing down.

    With clip_bbox ([s, w, n, e]), lines are cut at its edges and the box
    itself is returned as the frame, so the map is exactly that square.
    """
    nodes = {el["id"]: mercator(el["lon"], el["lat"])
             for el in result["elements"] if el["type"] == "node"}
    box = None
    if clip_bbox:
        s, w, n, e = clip_bbox
        (x0, y1), (x1, y0) = mercator(w, s), mercator(e, n)
        box = (x0, y0, x1, y1)
    lines = []
    for el in result["elements"]:
        if el["type"] == "way":
            pts = [nodes[n] for n in el.get("nodes", []) if n in nodes]
            if len(pts) < 2:
                continue
            lines.extend(clip_line(pts, box) if box else [pts])
    return lines, box


def get_boundary(place, refresh=False):
    """The place's boundary polygon in Web Mercator, from disk when we have it."""
    path = DATA / f'{place["area_id"]}-boundary.json'
    if path.exists() and not refresh:
        geojson = json.loads(path.read_text())
    else:
        osm_type, osm_id = place["osm"].split("/")
        ref = {"relation": "R", "way": "W"}[osm_type] + osm_id
        rows = http(NOMINATIM_LOOKUP + "?" + urllib.parse.urlencode(
            {"osm_ids": ref, "format": "json", "polygon_geojson": 1}))
        time.sleep(1)  # Nominatim usage policy
        if not rows or rows[0].get("geojson", {}).get("type") not in ("Polygon", "MultiPolygon"):
            raise FetchError(f"no boundary polygon for {place['osm']}")
        geojson = rows[0]["geojson"]
        path.write_text(json.dumps(geojson, separators=(",", ":")))
        print(f"  saved boundary: {path.relative_to(HERE)}")

    def to_mercator(coords):
        lon, lat = coords[:, 0], np.clip(coords[:, 1], -85.0, 85.0)
        return np.column_stack((np.radians(lon),
                                -np.log(np.tan(np.pi / 4 + np.radians(lat) / 2))))
    return shapely.transform(shapely.geometry.shape(geojson), to_mercator).buffer(0)


def trim(lines, boundary):
    """Cut lines at the boundary; return the pieces inside it as point lists."""
    inside = shapely.MultiLineString(lines).intersection(boundary)
    inside = shapely.line_merge(shapely.MultiLineString(
        [g for g in getattr(inside, "geoms", [inside]) if g.geom_type == "LineString"]))
    return [list(g.coords) for g in getattr(inside, "geoms", [inside])
            if g.geom_type == "LineString" and not g.is_empty]


def fit(lines, width, frame=None):
    """Scale lines to fit a canvas `width` wide; return (lines, width, height).

    The frame is the lines' own extent unless a box (x0, y0, x1, y1) is given.
    """
    if frame:
        minx, miny, maxx, maxy = frame
    else:
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


def write_svg(lines, path, colour, title, frame=None):
    fitted, w, h = fit(lines, SVG_WIDTH, frame)
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


def render_mask(lines, png_width, frame=None):
    """Draw the lines into a greyscale mask at PNG size, antialiased by supersampling."""
    big = png_width * SUPERSAMPLE
    fitted, w, h = fit(lines, big, frame)
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
    ap.add_argument("places", nargs="*", help='e.g. "Nauvoo, Illinois"')
    ap.add_argument("--all-towns", action="store_true",
                    help="every saved place that has a town boundary")
    ap.add_argument("--trim", action="store_true",
                    help='cut roads at the town boundary; writes "-trimmed" files')
    ap.add_argument("--filter", choices=FILTERS, default="roads")
    ap.add_argument("--format", choices=("svg", "png", "both"), default="both")
    ap.add_argument("--png-width", type=int, default=6000)
    ap.add_argument("--radius", type=float, metavar="KM",
                    help="map a square this far around the place instead of its boundary")
    ap.add_argument("--refresh", action="store_true", help="re-download even if cached")
    args = ap.parse_args()
    if not args.places and not args.all_towns:
        ap.error("name at least one place, or use --all-towns")

    DATA.mkdir(exist_ok=True)
    index = load_index()
    failed = []
    places = list(args.places)
    if args.all_towns:
        places += [p["query"] for p in index.values()
                   if p["area_id"] and p["query"] not in places]
    for query in places:
        try:
            make_maps(query, index, args)
        except FetchError as err:
            print(f"  FAILED: {err}")
            failed.append(query)
    if failed:
        print("\nFailed, run these again later:\n  " + "\n  ".join(failed))
        return 1


def make_maps(query, index, args):
    slug, place = lookup(query, index, args.radius)
    print(f"{query} -> {place['name']} ({place['osm']})")
    result = get_data(slug, place, args.filter, args.refresh)
    lines, frame = project(result, place["bbox"] if place.get("radius_km") else None)
    if not lines:
        print(f"  no ways found for {query}, skipping")
        return

    base = f"{slug}-{args.filter}"
    if args.trim:
        if not place["area_id"]:
            print("  no town boundary (a radius map is already square), skipping trim")
            return
        boundary = get_boundary(place, args.refresh)
        lines = trim(lines, boundary)
        frame = boundary.bounds
        base += "-trimmed"

    outdir = OUT / slug
    outdir.mkdir(parents=True, exist_ok=True)
    title = f"{place['name']}: {args.filter}"
    if args.format in ("svg", "both"):
        write_svg(lines, outdir / f"{base}-black.svg", "#000", title, frame)
        write_svg(lines, outdir / f"{base}-white.svg", "#fff", title, frame)
    if args.format in ("png", "both"):
        mask = render_mask(lines, args.png_width, frame)
        write_png(mask, outdir / f"{base}-black.png", (0, 0, 0))
        write_png(mask, outdir / f"{base}-white.png", (255, 255, 255))
    print(f"  {len(lines)} ways -> {outdir.relative_to(HERE)}/")


if __name__ == "__main__":
    sys.exit(main())
