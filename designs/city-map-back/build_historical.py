#!/usr/bin/env python3
"""Historical map backs: period street plans traced into the map-back line style.

    python3 designs/city-map-back/build_historical.py            # both
    python3 designs/city-map-back/build_historical.py slc-1847

A test for Evan (9 Oct 2026), not a product. It answers "are the historical
maps like the current maps, just older with fewer roads?" by drawing two of
them in the same 13.5 x 18 in frame as the live backs and putting them side
by side with today's map.

slc-1847  The 1847 Sherwood plat (LoC 2017587026) is a perfect grid: 9 blocks
          wide, 15 tall, Temple block 87 in column 6 of row 10. The scan is a
          warped sheepskin and its streets are drawn narrower than the true
          132 ft, so the grid is not copied pixel by pixel. The script counts
          the blocks on the scan, then lays the plat's grid on the ground with
          the spacing measured from today's TIGER streets (Main Street to West
          Temple, North to South Temple), anchored at Main and South Temple.

nauvoo-1859  The "City of Nauvoo" inset on the 1859 Hancock County map (LoC
          2013593101) is irregular (river, a rotated addition, open farm lots),
          so it is traced from the scan: blocks are found as enclosed paper
          areas, the streets are the centre lines of the gaps between them
          (a skeleton), and the result is fitted to the ground with an affine
          transform through street intersections whose 1859 names are still
          on today's TIGER map. The fit's error in metres is printed.

Writes to out/historical/ (gitignored): 100 ppi previews of each design, a
comparison sheet per place, and an overlay check. The traced street lines are
saved as GeoJSON in historical/traces/ (small, committed).
"""

import json
import math
import struct
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont
from scipy import ndimage as ndi
from skimage.morphology import skeletonize

import build_map_back as b

HERE = Path(__file__).resolve().parent
SAMPLES = HERE / "historical" / "samples"
TRACES = HERE / "historical" / "traces"
OUT = HERE / "out" / "historical"
PLACES = json.loads((HERE / "places.json").read_text())


# ---------------------------------------------------------------- TIGER names

def read_field(dbf, field):
    by = dbf.read_bytes()
    n, hlen, rlen = struct.unpack("<IHH", by[4:12])
    off, pos, col = 32, 1, None
    while by[off] != 0x0D:
        name, size = by[off:off + 11].split(b"\0")[0].decode(), by[off + 16]
        if name == field:
            col = (pos, size)
        pos += size
        off += 32
    return [by[hlen + i * rlen + col[0]:hlen + i * rlen + col[0] + col[1]].decode("latin1").strip()
            for i in range(n)]


def named_streets(county):
    shp = b.fetch_county(county)
    out = {}
    for name, parts in zip(read_field(shp.with_suffix(".dbf"), "FULLNAME"), b.read_lines(shp)):
        out.setdefault(name, []).extend(parts)
    return out


def dense(parts, step=1e-5):
    pts = []
    for p in parts:
        for (x0, y0), (x1, y1) in zip(p, p[1:]):
            n = max(1, int(math.hypot(x1 - x0, y1 - y0) / step))
            pts += [(x0 + (x1 - x0) * k / n, y0 + (y1 - y0) * k / n) for k in range(n)]
    return np.array(pts)


def crossing(streets, a, b_, near):
    """(lon, lat) where two named streets meet, the closest pair near `near`."""
    A, B = dense(streets[a]), dense(streets[b_])
    A = A[np.hypot(A[:, 0] - near[0], A[:, 1] - near[1]) < 0.01]
    B = B[np.hypot(B[:, 0] - near[0], B[:, 1] - near[1]) < 0.01]
    d = np.hypot(A[:, None, 0] - B[None, :, 0], A[:, None, 1] - B[None, :, 1])
    i, j = np.unravel_index(d.argmin(), d.shape)
    if d[i, j] > 2e-4:
        sys.exit(f"{a} and {b_} do not meet near {near}")
    return (A[i] + B[j]) / 2


def metres(lon, lat, lat0):
    return (np.radians(lon) * b.R * math.cos(math.radians(lat0)), np.radians(lat) * b.R)


# ------------------------------------------------------------- Salt Lake 1847

def slc_1847():
    """The plat's 9 x 15 grid placed on the ground. Returns (streets, blocks)
    as lon/lat polylines: streets are centre lines, blocks are outlines."""
    s = named_streets("49035")
    main_st = crossing(s, "S Main St", "W South Temple", (-111.891, 40.769))
    west_temple = crossing(s, "S West Temple", "W South Temple", (-111.894, 40.769))
    state_st = crossing(s, "S State St", "E South Temple", (-111.888, 40.769))
    north_temple = crossing(s, "N Main St", "W North Temple", (-111.891, 40.7715))
    hundred_s = crossing(s, "S Main St", "W 100 S", (-111.891, 40.767))
    dlon = (state_st[0] - west_temple[0]) / 2
    dlat = (north_temple[1] - hundred_s[1]) / 2
    lat0 = main_st[1]
    mx = dlon * math.radians(1) * b.R * math.cos(math.radians(lat0))
    my = dlat * math.radians(1) * b.R
    print(f"  TIGER pitch: {mx:.1f} m east-west, {my:.1f} m north-south "
          f"(1847 survey: 660 ft block + 132 ft street = 241.4 m)")
    # Plat columns 0..8 west to east, rows 0..14 south to north (block 1 is the
    # south-east corner, numbering runs in rows of nine). Temple block 87 is
    # column 5, row 9. Street line k runs west of column k; Main Street, east
    # of the Temple block, is line 6. Street line j runs south of row j;
    # South Temple is line 9.
    lon = lambda k: main_st[0] + (k - 6) * dlon
    lat = lambda j: main_st[1] + (j - 9) * dlat
    streets = [[(lon(k), lat(0)), (lon(k), lat(15))] for k in range(10)]
    streets += [[(lon(0), lat(j)), (lon(9), lat(j))] for j in range(16)]
    half = 0.5 * (132 / 792)  # half a street, as a fraction of the pitch
    blocks = []
    for k in range(9):
        for j in range(15):
            x0, x1 = lon(k + half), lon(k + 1 - half)
            y0, y1 = lat(j + half), lat(j + 1 - half)
            blocks.append([(x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0)])
    centre = (lat(7.5), lon(4.5))
    return streets, blocks, centre


def slc_scan_check():
    """Count the blocks on the scan and measure the plat's own proportions."""
    im = np.asarray(Image.open(SAMPLES / "slc-1847-sherwood-plat_loc_pct25.jpg").convert("L")).astype(float)
    dark = im < ndi.uniform_filter(im, 41) - 12
    dark[:150] = dark[1480:] = False
    lab, _ = ndi.label(ndi.binary_closing(dark, np.ones((3, 3))))
    boxes = []
    for sl in ndi.find_objects(lab):
        h, w = sl[0].stop - sl[0].start, sl[1].stop - sl[1].start
        if 65 < w < 95 and 65 < h < 95:
            boxes.append((sl[1].start + w / 2, sl[0].start + h / 2, w, h))
    bx = np.array(boxes)
    px = np.median([abs(q[0] - p[0]) for p in bx for q in bx if abs(q[1] - p[1]) < 20 and 70 < abs(q[0] - p[0]) < 110])
    py = np.median([abs(q[1] - p[1]) for p in bx for q in bx if abs(q[0] - p[0]) < 20 and 70 < abs(q[1] - p[1]) < 110])
    cols = round((bx[:, 0].max() - bx[:, 0].min()) / px) + 1
    rows = round((bx[:, 1].max() - bx[:, 1].min()) / py) + 1
    bw = np.median(bx[:, 2])
    print(f"  scan: {len(bx)} of 135 block outlines found cleanly, spanning {cols} x {rows}; "
          f"pitch {px:.1f} x {py:.1f} px (square to {abs(1 - py / px) * 100:.1f}%); "
          f"street drawn at {(px - bw) / bw:.2f} of a block (true 132/660 = 0.20)")
    return cols, rows


# --------------------------------------------------------------- Nauvoo 1859

NAUVOO_CROP = SAMPLES / "nauvoo-1859-hancock-county-inset_loc_crop.jpg"
# Street intersections named on the 1859 inset and still named on TIGER.
# Pixel positions are read off the inset by eye (full-resolution crop pixels)
# and then snapped to the nearest junction of the traced skeleton.
NAUVOO_PINS = [
    ("Main St", "Young St", (981, 274)),
    ("Main St", "Mulholland St", (978, 512)),
    ("Main St", "White St", (975, 734)),
    ("Main St", "Munson St", (969, 966)),
    ("Partridge St", "Young St", (1233, 274)),
    ("Partridge St", "Mulholland St", (1230, 512)),
    ("Partridge St", "Munson St", (1222, 966)),
    ("Wells St", "Mulholland St", (1490, 512)),
]


def trace_inset(path):
    """Blocks are closed outlines on the inset; streets are the skeleton of the gaps."""
    im = np.asarray(Image.open(path).convert("L")).astype(float)
    raw = im < ndi.uniform_filter(im, 151) - 14
    ink = raw.copy()
    # Lettering in the streets (MAIN, CARLIN, ST.) would bridge two blocks once
    # filled, so small free-standing ink marks go before the gaps are closed.
    lab, _ = ndi.label(ink)
    for i, sl in enumerate(ndi.find_objects(lab), 1):
        if max(sl[0].stop - sl[0].start, sl[1].stop - sl[1].start) < LETTER:
            ink[sl][lab[sl] == i] = False
    ink = ndi.binary_closing(ink, iterations=5)
    # An opening wider than any lettering, hatching or lot line but narrower
    # than a block keeps only the solid blocks.
    blocks = ndi.binary_opening(ndi.binary_fill_holes(ink), structure=np.ones((41, 41), bool))
    # River hatching and the title vignette also survive; they are long curved
    # shapes that fill little of their bounding box. A block, even the rotated
    # ones in the north-west addition, fills at least about half.
    lab, n = ndi.label(blocks)
    kept = 0
    for i, sl in enumerate(ndi.find_objects(lab), 1):
        part = lab[sl] == i
        # River hatching: many thin parallel strokes, so many ink edges per column.
        edges = (np.diff(raw[sl].astype(np.int8), axis=0) == 1) & part[1:]
        per_100px = 100 * edges.sum() / max(part.sum(), 1) * part.sum() / max(part.any(axis=0).sum(), 1) / max(part.any(axis=1).sum(), 1)
        if part.sum() / part.size < 0.45 or per_100px > HATCH or min(part.shape) < MIN_BLOCK:
            blocks[sl][part] = False
        else:
            kept += 1
    print(f"  inset: {kept} blocks found ({n - kept} other shapes dropped: river hatching, title letters)")
    band = ndi.binary_dilation(blocks, structure=np.ones((3, 3), bool), iterations=BAND) & ~blocks  # square brush keeps corners square
    # Where four blocks meet, the crossing's centre lies just beyond the band
    # and leaves a small hole that would skeletonise into a loop: fill it.
    holes, m = ndi.label(~(band | blocks))
    sizes = ndi.sum(np.ones_like(holes), holes, range(1, m + 1))
    small = np.isin(holes, 1 + np.nonzero(sizes < 3000)[0])
    return skeletonize(band | small), blocks


MIN_BLOCK = 55  # px; rotated north-west blocks trace at 60 to 75, title letters at about 43
HATCH = 8    # ink strokes per 100 px down a column; a block has a few, hatching many
LETTER = 36  # px; free-standing ink marks smaller than this are lettering
BAND = 20   # px; half a street gap is about 14 to 16 px on the inset


def skeleton_lines(skel, min_spur=40):
    """Vectorise a one-pixel skeleton into polylines; drop short dead-end spurs."""
    ys, xs = np.nonzero(skel)
    pts = set(zip(xs.tolist(), ys.tolist()))
    nb = lambda p: [(p[0] + dx, p[1] + dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1)
                    if (dx or dy) and (p[0] + dx, p[1] + dy) in pts]
    deg = {p: len(nb(p)) for p in pts}
    nodes = {p for p, d in deg.items() if d != 2}
    seen, lines = set(), []
    for s in nodes:
        for q in nb(s):
            if (s, q) in seen:
                continue
            path, prev, cur = [s], s, q
            while True:
                seen.add((prev, cur))
                seen.add((cur, prev))
                path.append(cur)
                if cur in nodes:
                    break
                nxt = [r for r in nb(cur) if r != prev and (cur, r) not in seen]
                if not nxt:
                    break
                prev, cur = cur, nxt[0]
            lines.append(path)
    ends = {p for p, d in deg.items() if d == 1}
    keep = [l for l in lines if not ((l[0] in ends or l[-1] in ends) and len(l) < min_spur)]
    return [rdp(l, 1.5) for l in keep if len(l) > 3], {p for p, d in deg.items() if d >= 3}


def rdp(pts, eps):
    if len(pts) < 3:
        return pts
    a, c = np.array(pts[0], float), np.array(pts[-1], float)
    v = c - a
    L = np.hypot(*v) or 1e-9
    d = [abs(v[0] * (p[1] - a[1]) - v[1] * (p[0] - a[0])) / L for p in pts[1:-1]]
    i = int(np.argmax(d)) + 1
    if d[i - 1] > eps:
        return rdp(pts[:i + 1], eps)[:-1] + rdp(pts[i:], eps)
    return [pts[0], pts[-1]]


def nauvoo_1859():
    skel, blocks = trace_inset(NAUVOO_CROP)
    lines, junctions = skeleton_lines(skel)
    s = named_streets("17067")
    J = np.array(sorted(junctions), float)
    src, dst = [], []
    for a, c, guess in NAUVOO_PINS:
        d = np.hypot(J[:, 0] - guess[0], J[:, 1] - guess[1])
        if d.min() > 30:
            print(f"  pin {a} / {c}: no traced junction within 30 px of {guess}, skipped")
            continue
        src.append(J[d.argmin()])
        dst.append(crossing(s, a, c, (-91.388, 40.548)))
    src, dst = np.array(src), np.array(dst)
    lat0 = dst[:, 1].mean()
    gx, gy = metres(dst[:, 0], dst[:, 1], lat0)
    A = np.c_[src, np.ones(len(src))]
    cx, *_ = np.linalg.lstsq(A, gx, rcond=None)
    cy, *_ = np.linalg.lstsq(A, gy, rcond=None)
    err = np.hypot(A @ cx - gx, A @ cy - gy)
    print(f"  affine fit through {len(src)} intersections: error {err.mean():.0f} m mean, "
          f"{err.max():.0f} m worst (a block is about 120 to 140 m)")
    for (a, c, _), e in zip(NAUVOO_PINS, err):
        print(f"    {a} / {c}: {e:.0f} m")
    to_ll = lambda x, y: (math.degrees((cx[0] * x + cx[1] * y + cx[2]) / (b.R * math.cos(math.radians(lat0)))),
                          math.degrees((cy[0] * x + cy[1] * y + cy[2]) / b.R))
    streets = [[to_ll(x, y) for x, y in l] for l in lines]
    return streets, err


# ------------------------------------------------------------------ drawing

def to_roads(lines):
    return [("S1400", [b.merc(lon, lat) for lon, lat in l]) for l in lines]


def draw(roads, centre, width_km, line_mm, swing, temple, label, ppi=100):
    b.HAND_SWING = swing
    m = b.render(roads, centre, width_km, line_mm, ppi, temple, hand=True)
    b.frame_and_label(m, label, ppi * b.SS)
    return m


def as_png(mask, path, ppi=100):
    b.save(mask, path, ppi)
    return path


def on_dark(path, w):
    """A white-on-transparent preview flattened onto garment black, w px wide."""
    im = Image.open(path).convert("RGBA")
    bg = Image.new("RGBA", im.size, (24, 24, 26, 255))
    bg.alpha_composite(im)
    return bg.convert("RGB").resize((w, round(w * im.height / im.width)), Image.LANCZOS)


def overlay(today_roads, old_roads, centre, width_km, ppi=100):
    """Today's streets in grey under the traced period streets in orange."""
    b.HAND_SWING = 0.0
    t = b.render(today_roads, centre, width_km, 0.6, ppi, hand=False)
    o = b.render(old_roads, centre, width_km, 1.0, ppi, hand=False)
    t, o = (x.resize((x.width // b.SS, x.height // b.SS), Image.LANCZOS) for x in (t, o))
    img = Image.new("RGB", t.size, (24, 24, 26))
    img.paste((110, 110, 115), mask=t)
    img.paste((255, 140, 40), mask=o)
    return img


def sheet(panels, title, path, w=600):
    font = ImageFont.truetype(str(b.OSWALD), 26)
    font.set_variation_by_axes([500])
    small = ImageFont.truetype(str(b.OSWALD), 18)
    small.set_variation_by_axes([400])
    gap, top, cap = 30, 70, 80
    imgs = [p[0].resize((w, round(w * p[0].height / p[0].width)), Image.LANCZOS) for p in panels]
    H = top + max(i.height for i in imgs) + cap
    out = Image.new("RGB", (gap + len(imgs) * (w + gap), H), (240, 238, 233))
    d = ImageDraw.Draw(out)
    d.text((gap, 22), title, font=font, fill=(20, 20, 20))
    for k, (im, (_, head, note)) in enumerate(zip(imgs, panels)):
        x = gap + k * (w + gap)
        out.paste(im, (x, top))
        d.text((x, top + im.height + 10), head, font=small, fill=(20, 20, 20))
        d.text((x, top + im.height + 36), note, font=small, fill=(90, 90, 90))
    out.save(path, optimize=True)
    return path


def save_trace(name, lines, props):
    TRACES.mkdir(parents=True, exist_ok=True)
    fc = {"type": "FeatureCollection", "properties": props,
          "features": [{"type": "Feature", "properties": {},
                        "geometry": {"type": "LineString",
                                     "coordinates": [[round(x, 6), round(y, 6)] for x, y in l]}}
                       for l in lines]}
    (TRACES / f"{name}.geojson").write_text(json.dumps(fc, separators=(",", ":")) + "\n")


LOC_CREDIT = "Library of Congress, Geography and Map Division"


def build_slc():
    print("slc-1847: Salt Lake City, 1847 Sherwood plat")
    slc_scan_check()
    streets, blocks, plat_centre = slc_1847()
    save_trace("slc-1847", streets, {
        "source": "https://www.loc.gov/item/2017587026/",
        "credit": LOC_CREDIT,
        "method": "plat grid (9 x 15 blocks, Temple block 87) placed at TIGER 2024 spacing, anchored at Main St / South Temple"})
    p = PLACES["salt-lake-city"]
    today = b.load_roads(p["counties"])
    old = to_roads(streets)
    OUT.mkdir(parents=True, exist_ok=True)
    plat_km = 2.0
    files = {
        "plat": as_png(draw(old, plat_centre, plat_km, 1.5, 0.4, p["temple"], "SALT LAKE CITY, UTAH 1847"),
                       OUT / f"slc-1847-plat-frame-{plat_km:g}km-1.5mm-preview.png"),
        "blocks": as_png(draw(to_roads(blocks), plat_centre, plat_km, 1.5, 0.4, p["temple"], "SALT LAKE CITY, UTAH 1847"),
                         OUT / f"slc-1847-block-outlines-{plat_km:g}km-1.5mm-preview.png"),
        "same": as_png(draw(old, p["centre"], p["width_km"], p["line_mm"], 0.1, p["temple"], "SALT LAKE CITY, UTAH 1847"),
                       OUT / f"slc-1847-todays-frame-{p['width_km']:g}km-{p['line_mm']:g}mm-preview.png"),
        "today": as_png(draw(today, p["centre"], p["width_km"], p["line_mm"], 0.1, p["temple"], p["label"]),
                        OUT / f"slc-today-{p['width_km']:g}km-{p['line_mm']:g}mm-preview.png"),
    }
    ov = overlay(today, old, plat_centre, 4.0)
    ov.save(OUT / "slc-1847-overlay-check.png", optimize=True)
    scan = Image.open(SAMPLES / "slc-1847-sherwood-plat_loc_pct25.jpg").convert("RGB")
    W = 600
    sheet([
        (scan, "The source: 1847 plat (LoC scan)", "Sheepskin, 9 x 15 blocks, Temple block 87"),
        (on_dark(files["plat"], W), "1847, traced: framed to the plat", f"{plat_km:g} km across, 1.5 mm lines"),
        (on_dark(files["blocks"], W), "1847, block outlines instead", "Same frame; the plat's own look"),
        (on_dark(files["same"], W), "1847, in today's frame", f"{p['width_km']:g} km, {p['line_mm']:g} mm, like the live back"),
        (on_dark(files["today"], W), "Today (the live back)", f"TIGER 2024, {p['width_km']:g} km, {p['line_mm']:g} mm"),
    ], "Salt Lake City: the 1847 plat in the map-back style, next to today's back", OUT / "slc-1847-vs-today.png", W)
    sheet([(ov, "Overlay check, 4 km around the plat", "Grey: today's streets. Orange: 1847 plat.")],
          "Salt Lake City: does the 1847 grid sit on today's streets?", OUT / "slc-1847-overlay-sheet.png", 900)
    print(f"  -> {OUT.relative_to(b.ROOT)}/")


def build_nauvoo():
    print("nauvoo-1859: Nauvoo, 1859 Hancock County map inset")
    streets, err = nauvoo_1859()
    save_trace("nauvoo-1859", streets, {
        "source": "https://www.loc.gov/item/2013593101/",
        "credit": LOC_CREDIT,
        "method": "skeleton of the gaps between enclosed blocks on the inset, affine-fitted to TIGER 2024 intersections",
        "fit_error_m": {"mean": round(float(err.mean()), 1), "max": round(float(err.max()), 1)}})
    p = PLACES["nauvoo"]
    today = b.load_roads(p["counties"])
    old = to_roads(streets)
    OUT.mkdir(parents=True, exist_ok=True)
    files = {
        "same": as_png(draw(old, p["centre"], p["width_km"], p["line_mm"], 0.4, p["temple"], "NAUVOO, ILLINOIS 1859"),
                       OUT / f"nauvoo-1859-todays-frame-{p['width_km']:g}km-{p['line_mm']:g}mm-preview.png"),
        "today": as_png(draw(today, p["centre"], p["width_km"], p["line_mm"], 0.4, p["temple"], p["label"]),
                        OUT / f"nauvoo-today-{p['width_km']:g}km-{p['line_mm']:g}mm-preview.png"),
    }
    ov = overlay(today, old, p["centre"], p["width_km"])
    ov.save(OUT / "nauvoo-1859-overlay-check.png", optimize=True)
    inset = Image.open(NAUVOO_CROP).convert("RGB")
    inset = inset.crop((0, 0, inset.width, round(inset.width * 4 / 3)) if inset.height > inset.width * 4 / 3 else (0, 0, inset.width, inset.height))
    W = 600
    sheet([
        (inset, "The source: 1859 county map inset (LoC)", "\"City of Nauvoo\", Holmes & Arnold"),
        (on_dark(files["same"], W), "1859, traced, in today's frame", f"{p['width_km']:g} km, {p['line_mm']:g} mm, like the live back"),
        (on_dark(files["today"], W), "Today (the live back)", f"TIGER 2024, {p['width_km']:g} km, {p['line_mm']:g} mm"),
        (ov, "Overlay check, same frame", "Grey: today. Orange: 1859 trace."),
    ], "Nauvoo: the 1859 inset in the map-back style, next to today's back", OUT / "nauvoo-1859-vs-today.png", W)
    print(f"  -> {OUT.relative_to(b.ROOT)}/")


if __name__ == "__main__":
    want = sys.argv[1:] or ["slc-1847", "nauvoo-1859"]
    if "slc-1847" in want:
        build_slc()
    if "nauvoo-1859" in want:
        build_nauvoo()
