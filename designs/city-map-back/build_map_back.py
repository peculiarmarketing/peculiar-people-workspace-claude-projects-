#!/usr/bin/env python3
"""City map back print: street map art for a 13.5 x 18 in back panel.

    python designs/city-map-back/build_map_back.py san-antonio nauvoo
    python designs/city-map-back/build_map_back.py san-antonio --auto

Places live in places.json. Each one names its US counties, a frame centre,
a frame width in km, a line weight in mm and an optional temple position.
Roads come from the Census Bureau's TIGER/Line road files (public domain, with
road classes), downloaded once per county to city-maps/data/tiger/.

--auto searches for the widest frame whose fused ink stays at or under
--max-fused percent (default 6). Fused ink is the share of the ink that has
merged into solid patches wider than a single road line: the "everything blurs
into white" failure. Rule set by Evan, 8 Oct 2026: big cities at 0.5 mm with
the frame as wide as it holds; small towns at 1.5 mm.

Writes to out/<place>/: a 100 ppi preview PNG for mockups and a 300 ppi print
PNG, both white ink on transparent, every pixel's colour white (BRAND.md s8).
The back carries a 2.5 mm frame around the full 13.5 x 18 in map and the
city label inside the frame at the bottom right, on a knocked-out patch
(Evan, 8 Oct 2026).

Also writes the front: the box logo with the temple's coordinates set into the
box edge (layout "3A closed", Evan, 8 Oct 2026). Latitude breaks the top edge
at the left, longitude breaks the bottom edge at the right; the box is
otherwise whole and the lettering is the original logo, untouched.
"""

import argparse
import io
import json
import math
import struct
import sys
import urllib.request
import zipfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
TIGER = ROOT / "city-maps" / "data" / "tiger"
OUT = HERE / "out"
PLACES = HERE / "places.json"
TIGER_URL = "https://www2.census.gov/geo/tiger/TIGER2024/ROADS/tl_2024_{}_roads.zip"
LOGO = ROOT / "designs" / "logo" / "source" / "Peculiar People Logo - White copy.png"
OSWALD = ROOT / "designs" / "jacket-chest-logo" / "fonts" / "Oswald[wght].ttf"

W_IN, H_IN = 13.5, 18.0  # one frame fits the tee, crew and hoodie back areas
SS = 2                   # draw at 2x, scale down to antialias
MM = 1 / 25.4
R = 6378137.0
# MTFCC road classes kept: interstates, US/state highways, ramps, local streets.
# Dropped: service drives, alleys, parking aisles, walkways, trails, 4WD tracks.
KEEP = {"S1100", "S1200", "S1630", "S1400"}
FIRST = ("S1400", "S1630", "S1200", "S1100")  # draw order, highways on top


def fetch_county(code):
    shp = TIGER / f"tl_2024_{code}_roads.shp"
    if not shp.exists():
        TIGER.mkdir(parents=True, exist_ok=True)
        print(f"  downloading TIGER roads for county {code}")
        req = urllib.request.Request(TIGER_URL.format(code),
                                     headers={"User-Agent": "PeculiarPeople-city-maps/0.1"})
        with urllib.request.urlopen(req, timeout=300) as resp:
            zipfile.ZipFile(io.BytesIO(resp.read())).extractall(TIGER)
    return shp


def read_mtfcc(dbf):
    b = dbf.read_bytes()
    n, hlen, rlen = struct.unpack("<IHH", b[4:12])
    off, pos, col = 32, 1, None
    while b[off] != 0x0D:
        name, size = b[off:off + 11].split(b"\0")[0].decode(), b[off + 16]
        if name == "MTFCC":
            col = (pos, size)
        pos += size
        off += 32
    return [b[hlen + i * rlen + col[0]:hlen + i * rlen + col[0] + col[1]].decode().strip()
            for i in range(n)]


def read_lines(shp):
    b, off, recs = shp.read_bytes(), 100, []
    while off < len(b):
        clen = struct.unpack(">i", b[off + 4:off + 8])[0] * 2
        rec, off = b[off + 8:off + 8 + clen], off + 8 + clen
        if struct.unpack("<i", rec[:4])[0] != 3:  # 3 = polyline
            recs.append([])
            continue
        nparts, npts = struct.unpack("<ii", rec[36:44])
        parts = list(struct.unpack(f"<{nparts}i", rec[44:44 + 4 * nparts])) + [npts]
        p0 = 44 + 4 * nparts
        xy = struct.unpack(f"<{2 * npts}d", rec[p0:p0 + 16 * npts])
        recs.append([[(xy[2 * k], xy[2 * k + 1]) for k in range(parts[j], parts[j + 1])]
                     for j in range(nparts)])
    return recs


def merc(lon, lat):
    return math.radians(lon), -math.log(math.tan(math.pi / 4 + math.radians(lat) / 2))


def load_roads(counties):
    roads = []
    for code in counties:
        shp = fetch_county(code)
        for cls, parts in zip(read_mtfcc(shp.with_suffix(".dbf")), read_lines(shp)):
            if cls in KEEP:
                roads += [(cls, [merc(x, y) for x, y in p]) for p in parts if len(p) > 1]
    return roads


def render(roads, centre, width_km, line_mm, ppi, temple=None, label=None):
    """Return an L-mode mask at ppi * SS, frame centred on `centre`."""
    lat, lon = centre
    cx, cy = merc(lon, lat)
    span = width_km * 1000 / (R * math.cos(math.radians(lat)))
    W, H = round(W_IN * ppi * SS), round(H_IN * ppi * SS)
    s = W / span
    x0, y0 = cx - span / 2, cy - span * (H / W) / 2
    to_px = lambda x, y: ((x - x0) * s, (y - y0) * s)
    lw = max(1, round(line_mm * MM * ppi * SS))
    mask = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(mask)
    for cls in FIRST:
        for c, pts in roads:
            if c != cls:
                continue
            xy = [to_px(x, y) for x, y in pts]
            xs, ys = [p[0] for p in xy], [p[1] for p in xy]
            if max(xs) < 0 or min(xs) > W or max(ys) < 0 or min(ys) > H:
                continue
            d.line(xy, fill=255, width=lw, joint="curve")
    if temple:
        halo(mask, to_px(*merc(temple[1], temple[0])), ppi * SS)
    if label:
        frame_and_label(mask, label, ppi * SS)
    return mask


FRAME_MM = 2.5           # frame border, about three times a 0.8 mm street
LABEL_IN = 0.25          # label font size; Oswald 500 gives ~0.9 mm strokes
LABEL_TRACK = 0.16       # letter spacing, as a fraction of the font size
LABEL_INSET_IN = 0.25    # from the frame's inner edge to the label
LABEL_PAD_IN = 0.08      # knocked-out space around the label


def frame_and_label(mask, label, px_per_in):
    """Draw the frame on the map's outer edge and the label inside it, bottom right."""
    d = ImageDraw.Draw(mask)
    fw = round(FRAME_MM * MM * px_per_in)
    W, H = mask.size
    for box in ((0, 0, W, fw), (0, H - fw, W, H), (0, 0, fw, H), (W - fw, 0, W, H)):
        d.rectangle(box, fill=255)
    f = ImageFont.truetype(str(OSWALD), round(LABEL_IN * px_per_in))
    f.set_variation_by_axes([COORD_WEIGHT])
    track = LABEL_TRACK * LABEL_IN * px_per_in
    widths = [d.textlength(ch, font=f) for ch in label]
    text_w = sum(widths) + track * (len(label) - 1)
    _, top, _, bottom = d.textbbox((0, 0), "A", font=f, anchor="ls")  # cap height
    inset, pad = LABEL_INSET_IN * px_per_in, LABEL_PAD_IN * px_per_in
    x = W - fw - inset - text_w
    base = H - fw - inset
    d.rectangle((x - pad, base + top - pad, x + text_w + pad, base + pad), fill=0)
    for ch, w in zip(label, widths):
        d.text((x, base), ch, font=f, fill=255, anchor="ls")
        x += w + track


def halo(mask, xy, px_per_in):
    """Temple marker: streets cleared in a circle, a thin ring and a centre dot."""
    x, y = xy
    if not (0 < x < mask.width and 0 < y < mask.height):
        return
    d = ImageDraw.Draw(mask)
    ko, ring, dot = 0.32 * px_per_in, 0.22 * px_per_in, 0.06 * px_per_in
    d.ellipse((x - ko, y - ko, x + ko, y + ko), fill=0)
    d.ellipse((x - ring, y - ring, x + ring, y + ring), outline=255,
              width=round(1.0 * MM * px_per_in))
    d.ellipse((x - dot, y - dot, x + dot, y + dot), fill=255)


def fused_pct(mask, line_mm, ppi):
    """Share of ink in solid patches wider than a line plus a margin (opening)."""
    small = mask.resize((mask.width // SS, mask.height // SS), Image.LANCZOS)
    small = small.point(lambda v: 255 if v > 127 else 0)
    k = max(3, round(line_mm * MM * ppi) + 3) | 1
    opened = small.filter(ImageFilter.MinFilter(k)).filter(ImageFilter.MaxFilter(k))
    ink = small.histogram()[255]
    return 100 * opened.histogram()[255] / max(ink, 1)


def save(mask, path, ppi):
    small = mask.resize((mask.width // SS, mask.height // SS), Image.LANCZOS)
    img = Image.new("RGBA", small.size, (255, 255, 255, 0))
    img.putalpha(small)
    img.save(path, dpi=(ppi, ppi), optimize=True)


# Front: box logo with coordinates. Geometry measured from the logo PNG
# (3125 x 625, ink 3051 px wide, so about 508 px per inch at the 6 in front size).
BOX = (31, 25, 1893, 604)   # outer edge of the box around PECULIAR
BOX_STROKE = 19             # about 0.95 mm at 6 in
FRONT_IN = 6.0              # BRAND.md s8: front logo is 6 in wide, ink to ink
# Oswald 500 at 110 px: 0.8 mm strokes at 6 in, clear of the 0.71 mm DTG floor
# (design-audit PRINT-01). Weight 400 at the earlier size measured 0.45 mm.
COORD_PX, COORD_WEIGHT, COORD_INSET, COORD_GAP = 110, 500, 180, 40


def fmt_coords(lat, lon):
    return (f"{abs(lat):.4f}\u00b0 {'N' if lat >= 0 else 'S'}",
            f"{abs(lon):.4f}\u00b0 {'E' if lon >= 0 else 'W'}")


def front(lat, lon):
    """Return the front artwork as an L mask at the logo's own resolution."""
    logo = Image.open(LOGO).getchannel("A")
    pad = 120  # room for the coordinates, which sit centred on the box line
    m = Image.new("L", (logo.width + 2 * pad, logo.height + 2 * pad), 0)
    m.paste(logo, (pad, pad))
    d = ImageDraw.Draw(m)
    f = ImageFont.truetype(str(OSWALD), COORD_PX)
    f.set_variation_by_axes([COORD_WEIGHT])
    x0, y0, x1, y1 = (v + pad for v in BOX)
    top, bottom = fmt_coords(lat, lon)
    for xy, text, anchor in (((x0 + COORD_INSET, y0 + BOX_STROKE / 2), top, "lm"),
                             ((x1 - COORD_INSET, y1 - BOX_STROKE / 2), bottom, "rm")):
        l, _, r, _ = d.textbbox(xy, text, font=f, anchor=anchor)
        d.rectangle((l - COORD_GAP, xy[1] - BOX_STROKE / 2 - 4,
                     r + COORD_GAP, xy[1] + BOX_STROKE / 2 + 4), fill=0)
        d.text(xy, text, font=f, fill=255, anchor=anchor)
    return m.crop(m.getbbox())


def save_front(mask, path, ppi=300):
    """Scale so the ink is FRONT_IN wide at ppi, then save white on transparent."""
    w = round(FRONT_IN * ppi)
    mask = mask.resize((w, round(mask.height * w / mask.width)), Image.LANCZOS)
    img = Image.new("RGBA", mask.size, (255, 255, 255, 0))
    img.putalpha(mask)
    img.save(path, dpi=(ppi, ppi), optimize=True)


def auto_width(roads, p, max_fused, lo=3.0, hi=80.0):
    """Widest frame (km) with fused ink at or under max_fused, by bisection."""
    best = lo
    for _ in range(7):
        mid = (lo + hi) / 2
        f = fused_pct(render(roads, p["centre"], mid, p["line_mm"], 100), p["line_mm"], 100)
        print(f"  {mid:5.1f} km: {f:4.1f}% fused")
        if f <= max_fused:
            best, lo = mid, mid
        else:
            hi = mid
    return round(best, 1)


def build(name, p, args):
    print(f"{name}: {p['label']}")
    roads = load_roads(p["counties"])
    if args.auto:
        p["width_km"] = auto_width(roads, p, args.max_fused)
        print(f"  widest frame that holds: {p['width_km']} km")
    outdir = OUT / name
    outdir.mkdir(parents=True, exist_ok=True)
    tag = f"{name}-{p['width_km']:g}km-{p['line_mm']:g}mm"
    preview = render(roads, p["centre"], p["width_km"], p["line_mm"], 100, p.get("temple"))
    fused = fused_pct(preview, p["line_mm"], 100)
    frame_and_label(preview, p["label"], 100 * SS)
    print(f"  {p['width_km']:g} km at {p['line_mm']:g} mm: "
          f"{fused:.1f}% fused")
    save(preview, outdir / f"{tag}-preview.png", 100)
    if not args.preview_only:
        save(render(roads, p["centre"], p["width_km"], p["line_mm"], 300, p.get("temple"), p["label"]),
             outdir / f"{tag}-print-300dpi.png", 300)
    if p.get("temple"):
        save_front(front(*p["temple"]), outdir / f"{name}-front-6in-300dpi.png")
    print(f"  -> {outdir.relative_to(ROOT)}/")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("places", nargs="+", help="keys in places.json")
    ap.add_argument("--auto", action="store_true", help="find the widest frame that holds")
    ap.add_argument("--max-fused", type=float, default=6.0)
    ap.add_argument("--preview-only", action="store_true", help="skip the 300 ppi print file")
    args = ap.parse_args()
    places = {k: v for k, v in json.loads(PLACES.read_text()).items() if not k.startswith("_")}
    for name in args.places:
        if name not in places:
            sys.exit(f"unknown place {name!r}; known: {', '.join(places)}")
        build(name, places[name], args)


if __name__ == "__main__":
    main()
