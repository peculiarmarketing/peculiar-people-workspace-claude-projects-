#!/usr/bin/env python3
"""Pen drawings of the maps for the product page, in the temple band's format.

    python designs/city-map-back/web_map_drawing.py nauvoo san-antonio
    python designs/city-map-back/web_map_drawing.py --all

The temple product pages draw the temple with pp-pen-draw.js (temple-product-
generator/web_drawing.py and theme/): a JSON of centre-line strokes in pen order
plus a WebP of the finished art; the browser uses the strokes as a mask over the
art and fades the rest in at the end. The temple tool has to trace centre lines
out of filled artwork. A map already is centre lines, so this writes the same
two files straight from the road data:

    {"version": 1, "box": [x, y, w, h], "penWidth": px, "city": label,
     "strokes": ["M x y L x y ...", ...], "lens": [px, ...]}

Pen order: every street by its distance from the temple
(or the frame centre when there is none), so the city grows out from the halo,
then the frame closes around it.
The finished art is the back print without its label (the band shows the label
as its city line), at ART_H px tall. Budget per map matches the temples: gzipped
strokes plus image at most 250,000 bytes; streets too short to see at this size
are left to the final fade, and if a map is still over budget the shortest
strokes go first.

Writes out/<place>/web/pp-map-<place>.json and .webp. Uploading them to the
theme, and the band that shows them, come when the map products are published.
"""

import argparse
import gzip
import io
import json
import math
import sys
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_map_back as b  # noqa: E402

ART_H = 840                  # finished art height, px (the temple art's limit)
BUDGET = 250_000             # gzipped JSON + WebP, bytes
IMAGE_CAP = 150_000          # the image's share; the rest is for strokes
SIMPLIFY_PX = 0.6            # Douglas-Peucker tolerance at art size
MIN_LEN_PX = 4.0             # shorter streets are left to the final fade


def simplify(pts, tol):
    if len(pts) < 3:
        return pts
    (x0, y0), (x1, y1) = pts[0], pts[-1]
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy) or 1e-9
    i, dmax = 0, 0.0
    for k in range(1, len(pts) - 1):
        d = abs(dy * (pts[k][0] - x0) - dx * (pts[k][1] - y0)) / L
        if d > dmax:
            i, dmax = k, d
    if dmax <= tol:
        return [pts[0], pts[-1]]
    return simplify(pts[:i + 1], tol)[:-1] + simplify(pts[i:], tol)


def clip(pts, W, H):
    """Split a polyline into the runs inside the art box (Liang-Barsky per segment)."""
    runs, run = [], []
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        t0, t1, dx, dy = 0.0, 1.0, x1 - x0, y1 - y0
        ok = True
        for p, q in ((-dx, x0), (dx, W - x0), (-dy, y0), (dy, H - y0)):
            if p == 0:
                if q < 0:
                    ok = False
                    break
                continue
            r = q / p
            if p < 0:
                t0 = max(t0, r)
            else:
                t1 = min(t1, r)
            if t0 > t1:
                ok = False
                break
        if not ok:
            if len(run) > 1:
                runs.append(run)
            run = []
            continue
        a = (x0 + t0 * dx, y0 + t0 * dy)
        c = (x0 + t1 * dx, y0 + t1 * dy)
        if not run or run[-1] != a:
            if len(run) > 1:
                runs.append(run)
            run = [a]
        run.append(c)
    if len(run) > 1:
        runs.append(run)
    return runs


def length(pts):
    return sum(math.hypot(x1 - x0, y1 - y0) for (x0, y0), (x1, y1) in zip(pts, pts[1:]))


def build_web(name, p):
    roads = b.load_roads(p["counties"])
    W, H = round(ART_H * b.W_IN / b.H_IN), ART_H
    ppi = H / b.H_IN
    # Finished art: the back print's map, halo and frame, no label.
    swing = b.swing_for(p)
    b.HAND_SWING = swing
    k = 3   # render the art at 3x (times build_map_back's own 2x) and scale down, so thin lines stay crisp
    art = b.render(roads, p["centre"], p["width_km"], p["line_mm"], ppi * k, p.get("temple"), hand=True,
                   markers=b.markers_for(name), marker_label=p["label"], field=b.dense_field(roads, p))
    fw = max(2, round(b.FRAME_MM * b.MM * ppi * k * b.SS))
    d = ImageDraw.Draw(art)
    for box in ((0, 0, art.width, fw), (0, art.height - fw, art.width, art.height),
                (0, 0, fw, art.height), (art.width - fw, 0, art.width, art.height)):
        d.rectangle(box, fill=255)
    art = art.resize((W, H), Image.LANCZOS)
    white = Image.new("L", art.size, 255)
    rgba = Image.merge("RGBA", (white, white, white, art))
    out = io.BytesIO()
    rgba.save(out, "WEBP", lossless=True, method=6)
    image = out.getvalue()
    for q in (90, 80, 70, 60):   # dense cities: lossy alpha until the image leaves room for strokes
        if len(image) <= IMAGE_CAP:
            break
        out = io.BytesIO()
        rgba.save(out, "WEBP", quality=q, alpha_quality=q, method=6)
        image = out.getvalue()

    # Strokes: the same projection as render(), at art size.
    lat, lon = p["centre"]
    cx, cy = b.merc(lon, lat)
    span = p["width_km"] * 1000 / (b.R * math.cos(math.radians(lat)))
    s = W / span
    x0, y0 = cx - span / 2, cy - span * (H / W) / 2
    to_px = lambda x, y: ((x - x0) * s, (y - y0) * s)
    if p.get("temple"):
        ox, oy = to_px(*b.merc(p["temple"][1], p["temple"][0]))
    else:
        ox, oy = W / 2, H / 2
    strokes = []
    for _, pts in roads:
        for run in clip([to_px(x, y) for x, y in pts], W, H):
            run = simplify(run, SIMPLIFY_PX)
            if length(run) >= MIN_LEN_PX:
                strokes.append(run)
    pen = max(1.5, p["line_mm"] * b.MM * ppi * 2.4)   # pen a bit wider than the line

    def payload(strokes):
        def key(st):
            return min(math.hypot(x - ox, y - oy) for x, y in st)
        ordered = sorted(strokes, key=key)
        # orient each stroke to start at its end nearest the origin
        ordered = [st if math.hypot(st[0][0] - ox, st[0][1] - oy) <= math.hypot(st[-1][0] - ox, st[-1][1] - oy)
                   else st[::-1] for st in ordered]
        frame = [[(1, 1), (W - 1, 1)], [(W - 1, 1), (W - 1, H - 1)],
                 [(W - 1, H - 1), (1, H - 1)], [(1, H - 1), (1, 1)]]
        allst = ordered + frame   # the frame closes around the finished map
        data = {"version": 1, "box": [0, 0, W, H], "penWidth": round(pen, 1), "city": p["label"],
                "strokes": ["M" + " L".join(f"{round(x)} {round(y)}" for x, y in st) for st in allst],
                "lens": [round(length(st), 1) for st in allst]}
        return data, gzip.compress(json.dumps(data, separators=(",", ":")).encode(), 9)

    data, gz = payload(strokes)
    dropped = 0
    while len(gz) + len(image) > BUDGET and strokes:
        strokes.sort(key=length)
        cut = max(1, len(strokes) // 10)
        dropped += cut
        strokes = strokes[cut:]
        data, gz = payload(strokes)
    webdir = b.OUT / name / "web"
    webdir.mkdir(parents=True, exist_ok=True)
    (webdir / f"pp-map-{name}.json").write_text(json.dumps(data, separators=(",", ":")))
    (webdir / f"pp-map-{name}.webp").write_bytes(image)
    total = len(gz) + len(image)
    print(f"{name}: {len(data['strokes'])} strokes, {len(gz):,} + {len(image):,} = {total:,} bytes"
          f"{' (over budget)' if total > BUDGET else ''}"
          f"{f', {dropped} shortest strokes left to the fade' if dropped else ''}")
    return data, art


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("places", nargs="*")
    ap.add_argument("--all", action="store_true")
    args = ap.parse_args()
    places = {k: v for k, v in json.loads(b.PLACES.read_text()).items() if not k.startswith("_")}
    for name in (list(places) if args.all else args.places):
        build_web(name, places[name])


if __name__ == "__main__":
    main()
