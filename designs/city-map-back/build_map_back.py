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


def render(roads, centre, width_km, line_mm, ppi, temple=None, label=None, hand=False,
           markers=None, marker_label=None, field=None):
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
    if hand:
        polys = []
        for cls in FIRST:
            for c, pts in roads:
                if c != cls:
                    continue
                xy = [to_px(x, y) for x, y in pts]
                xs, ys = [p[0] for p in xy], [p[1] for p in xy]
                if max(xs) < -lw or min(xs) > W + lw or max(ys) < -lw or min(ys) > H + lw:
                    continue
                polys.append(xy)
        draw_hand(d, polys, lw, ppi * SS, field=field)
    else:
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
    if markers:
        draw_markers(mask, markers, to_px, ppi * SS,
                     to_px(*merc(temple[1], temple[0])) if temple else None, label or marker_label)
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


# Hand-drawn style: width wanders like pen pressure and dead ends taper to a
# point, like the temple line art. The wobble is a smooth field over the page
# (not per line), so two streets meeting at a junction agree on width there.
HAND_SWING = 0.40        # default width swing (+/-40 percent); see swing_for()
SWING_SMALL, SWING_BUSY = 0.40, 0.10   # Evan, 8 Oct 2026
HAND_TAPER = 7           # a dead end tapers over this many line widths
HAND_STEP_MM = 0.4       # resampling step along each line


def swing_for(p):
    """Small towns swing 40 percent, busy cities 10 percent, unless a place sets "swing"."""
    return p.get("swing", SWING_BUSY if p.get("busy") else SWING_SMALL)


def hand_width(x_in, y_in, ph):
    a = math.sin(2 * math.pi * x_in / 1.1 + ph[0]) * math.cos(2 * math.pi * y_in / 1.4 + ph[1])
    b = math.sin(2 * math.pi * (x_in * 0.8 + y_in) / 0.45 + ph[2])
    return 1 + HAND_SWING * (0.65 * a + 0.35 * b)


def draw_hand(d, lines, lw, px_per_in, ph=(0.7, 2.1, 4.4), field=None):
    """lines: pixel point lists. An end tapers only if no other street touches it
    (checked on the page, since a side street often meets a main road mid-segment
    without sharing a point with it)."""
    step = HAND_STEP_MM * MM * px_per_in
    taper = HAND_TAPER * lw
    sampled = []
    for pts in lines:
        res, acc = [pts[0]], [0.0]
        for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
            seg = math.hypot(x1 - x0, y1 - y0)
            n = max(1, int(seg / step))
            for k in range(1, n + 1):
                res.append((x0 + (x1 - x0) * k / n, y0 + (y1 - y0) * k / n))
                acc.append(acc[-1] + seg / n)
        sampled.append((res, acc))
    cell = max(step, lw) * 2
    grid = {}
    for li, (res, _) in enumerate(sampled):
        for x, y in res:
            grid.setdefault((int(x // cell), int(y // cell)), []).append((li, x, y))
    near = (lw * 1.5) ** 2
    def touched(li, x, y):
        gx, gy = int(x // cell), int(y // cell)
        for cx in (gx - 1, gx, gx + 1):
            for cy in (gy - 1, gy, gy + 1):
                for lj, px, py in grid.get((cx, cy), ()):
                    if lj != li and (px - x) ** 2 + (py - y) ** 2 < near:
                        return True
        return False
    for li, (res, acc) in enumerate(sampled):
        total = acc[-1]
        if total <= 0:
            continue
        dead0, dead1 = not touched(li, *res[0]), not touched(li, *res[-1])
        t_len = min(taper, total * 0.45)
        radii = []
        for (x, y), a in zip(res, acc):
            w = lw * hand_width(x / px_per_in, y / px_per_in, ph) / 2
            if field is not None:
                w *= field.factor(x / px_per_in, y / px_per_in)
            for dead, dist in ((dead0, a), (dead1, total - a)):
                if dead and dist < t_len:
                    w *= (dist / t_len) ** 0.7
            radii.append(max(0.0, w - 0.5))  # polygon fill adds ~0.5 px per side
        for i in range(len(res) - 1):
            (x0, y0), (x1, y1) = res[i], res[i + 1]
            r0, r1 = radii[i], radii[i + 1]
            L = math.hypot(x1 - x0, y1 - y0) or 1e-9
            nx, ny = -(y1 - y0) / L, (x1 - x0) / L
            d.polygon([(x0 + nx * r0, y0 + ny * r0), (x1 + nx * r1, y1 + ny * r1),
                       (x1 - nx * r1, y1 - ny * r1), (x0 - nx * r0, y0 - ny * r0)], fill=255)
            if r1 > 0.5:
                d.ellipse((x1 - r1, y1 - r1, x1 + r1, y1 + r1), fill=255)
        if radii[0] > 0.5:
            x, y = res[0]
            d.ellipse((x - radii[0], y - radii[0], x + radii[0], y + radii[0]), fill=255)


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


# Numbered landmark markers (Evan, 9 Oct 2026). Each Church history map can
# carry a history/<place>-markers.json list; the numbers match the numbered
# On the Map list on the product page. A site gets a dot with the streets
# cleared around it and its number beside it on a knocked-out patch; the
# temple keeps its halo and gets only the number, set outside the ring.
# Number size: Oswald 500 at 0.29 in, about 1 mm strokes (DTG minimum 0.71 mm)
# and about 6 mm tall: Evan asked for 10% over the first 0.24 in, then 10% more.
# Placement (Evan, 9 Oct): the number sits directly above its dot (or above the
# halo), and both are ringed by 2 mm of cleared streets, so a road can't read
# into the number. It moves only when that spot is taken by another marker,
# the halo, the frame or the city label.
MARK_NUM_IN = 0.29       # number font size (0.24 in, then 10% up twice per Evan, 9 Oct)
MARK_DOT_IN = 0.06       # dot radius
MARK_CLEAR_IN = 2 * MM   # 2 mm of streets cleared around the dot and the number (Evan)
MARK_KO_IN = MARK_DOT_IN + MARK_CLEAR_IN   # streets cleared around the dot
MARK_PAD_IN = MARK_CLEAR_IN   # knocked-out padding around the number
MARK_GAP_IN = 0.03       # space between the top of the dot and the bottom of the number
HALO_KO_IN = 0.32        # the halo's own cleared radius (see halo())
HALO_RING_OUT_IN = 0.25  # just outside the halo's 0.22 in ring: where a temple's number patch may start
MARKERS_DIR = HERE / "history"


def markers_for(name):
    """The place's marker list, or None when it has none."""
    f = MARKERS_DIR / f"{name}-markers.json"
    if not f.exists():
        return None
    return json.loads(f.read_text())["markers"]


def _label_box(mask, label, px_per_in):
    """The knocked-out patch frame_and_label() will draw, so numbers keep off it."""
    d = ImageDraw.Draw(mask)
    f = ImageFont.truetype(str(OSWALD), round(LABEL_IN * px_per_in))
    f.set_variation_by_axes([COORD_WEIGHT])
    track = LABEL_TRACK * LABEL_IN * px_per_in
    text_w = sum(d.textlength(ch, font=f) for ch in label) + track * (len(label) - 1)
    _, top, _, _ = d.textbbox((0, 0), "A", font=f, anchor="ls")
    fw = round(FRAME_MM * MM * px_per_in)
    inset, pad = LABEL_INSET_IN * px_per_in, LABEL_PAD_IN * px_per_in
    W, H = mask.size
    base = H - fw - inset
    return (W - fw - inset - text_w - 2 * pad, base + top - 2 * pad, W, H)


def _overlap(a, b):
    return max(0, min(a[2], b[2]) - max(a[0], b[0])) * max(0, min(a[3], b[3]) - max(a[1], b[1]))


def draw_markers(mask, markers, to_px, px_per_in, temple_xy=None, label=None):
    """Draw every marker; returns the placed number boxes (for checks)."""
    d = ImageDraw.Draw(mask)
    W, H = mask.size
    f = ImageFont.truetype(str(OSWALD), round(MARK_NUM_IN * px_per_in))
    f.set_variation_by_axes([COORD_WEIGHT])
    fw = round(FRAME_MM * MM * px_per_in)
    pad = MARK_PAD_IN * px_per_in
    keep_off = []            # (box, owner): a number may overlap only its own dot's clearing
    pts = []
    for m in markers:
        temple = m.get("kind") == "temple" and temple_xy
        x, y = temple_xy if temple else to_px(*merc(m["lon"], m["lat"]))
        if not (fw < x < W - fw and fw < y < H - fw):
            print(f"  marker {m['n']} ({m['name']}) is outside the frame; skipped")
            continue
        pts.append((m, x, y, bool(temple)))
        r = (HALO_KO_IN if temple else MARK_KO_IN) * px_per_in
        keep_off.append(((x - r, y - r, x + r, y + r), m["n"]))
    if temple_xy and not any(t for *_, t in pts):
        r = HALO_KO_IN * px_per_in
        keep_off.append(((temple_xy[0] - r, temple_xy[1] - r, temple_xy[0] + r, temple_xy[1] + r), None))
    if label:
        keep_off.append((_label_box(mask, label, px_per_in), None))
    placed = []              # (box, text, l, t)
    for m, x, y, temple in pts:
        text = str(m["n"])
        l, t, rt, bt = d.textbbox((0, 0), text, font=f, anchor="lt")
        tw, th = rt - l + 2 * pad, bt - t + 2 * pad
        # distance from the point to the near edge of the number's cleared patch:
        # a site's number sits just above its dot (the patch may overlap the
        # dot's own clearing; the dot is drawn last); a temple's number sits
        # just outside the halo ring
        near = (HALO_RING_OUT_IN * px_per_in if temple
                else (MARK_DOT_IN + MARK_GAP_IN) * px_per_in - pad)
        others = [o for o, owner in keep_off if owner != m["n"]] + [b for b, *_ in placed]
        best = None
        # directly above first, then the nearest turns either way, below last
        order = (90, 60, 120, 30, 150, 0, 180, 330, 210, 300, 240, 270)
        # a marker may name its side ("label_at": right/left/below/above), e.g.
        # when the spot above is a road the number would read into (Mendon 1)
        side = {"above": 90, "right": 0, "left": 180, "below": 270}.get(m.get("label_at"))
        if side is not None:
            order = (side,) + tuple(a for a in order if a != side)
        for ang_deg in order:
            ang = math.radians(ang_deg)
            c, s_ = math.cos(ang), -math.sin(ang)
            reach = near + min(tw / 2 / max(abs(c), 1e-6), th / 2 / max(abs(s_), 1e-6))
            bx, by = x + c * reach - tw / 2, y + s_ * reach - th / 2
            box = (bx, by, bx + tw, by + th)
            clash = sum(_overlap(box, o) for o in others)
            outside = (max(0, fw - box[0]) + max(0, box[2] - (W - fw))
                       + max(0, fw - box[1]) + max(0, box[3] - (H - fw)))
            score = clash + outside * th * 10
            if best is None or score < best[0]:
                best = (score, box)
            if score == 0:
                break
        placed.append((best[1], text, l, t))
    # clearings first, then the dots, then the numbers, so nothing erases a dot
    for m, x, y, temple in pts:
        if not temple:
            r = MARK_KO_IN * px_per_in
            d.ellipse((x - r, y - r, x + r, y + r), fill=0)
    for box, *_ in placed:
        d.rectangle(box, fill=0)
    for m, x, y, temple in pts:
        if not temple:
            r = MARK_DOT_IN * px_per_in
            d.ellipse((x - r, y - r, x + r, y + r), fill=255)
    for box, text, l, t in placed:
        d.text((box[0] + pad - l, box[1] + pad - t), text, font=f, fill=255, anchor="lt")
    return [b for b, *_ in placed]


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


def front(lat=None, lon=None):
    """Return the front artwork as an L mask at the logo's own resolution.

    With no temple in the frame the front is the plain box logo."""
    logo = Image.open(LOGO).getchannel("A")
    if lat is None:
        return logo.crop(logo.getbbox())
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


def fit(roads, p, max_fused):
    """Line weight by kind of place: busy cities ("busy": true in places.json) at
    0.5 mm, narrowed if their frame merges; every other place at 1.5 mm.

    The fused-ink measure picks the frame width for a busy city, but it cannot
    tell a town from busy countryside (rural Fayette scores higher at 1.5 mm than
    the city of Quincy), so it does not choose the weight."""
    if not p.get("busy"):
        p["line_mm"] = 1.5
    else:
        p["line_mm"] = 0.5
        if fused_pct(render(roads, p["centre"], p["width_km"], 0.5, 100), 0.5, 100) > max_fused:
            p["width_km"] = auto_width(roads, p, max_fused, hi=p["width_km"])
    print(f"  fitted: {p['width_km']} km at {p['line_mm']} mm")


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


# Thin lines where the streets crowd (Evan, 9 Oct 2026). In small towns at
# 1.5 mm, tight rows of streets (lakeside cottage lanes, a village core) run
# together into solid white. Those patches are found and drawn at 0.5 mm, and
# everything else stays 1.5 mm. How: render the map at full weight (100 ppi),
# close every gap narrower than DENSE_GAP_MM, and where the closed-up pixels
# are dense, that is a crowded patch. A smooth field over the page then scales
# each line's width from 1 (open country) down to thin/line inside a patch,
# easing over about 0.2 in so a road thins gradually instead of stepping.
DENSE_LINE_MM = 0.5      # line weight inside crowded patches
DENSE_GAP_MM = 1.5       # gaps narrower than this read as merged
DENSE_THRESHOLD = 0.06   # local share of closed-up gaps that marks a patch
DENSE_PPI = 100
DENSE_MIN_SQIN = 0.2    # smaller patches are lone knots and keep the full weight


class WidthField:
    def __init__(self, f, thin_ratio):
        self.f, self.k = f, 1 - thin_ratio
        self.h, self.w = f.shape

    def factor(self, x_in, y_in):
        i = min(self.h - 1, max(0, int(y_in * DENSE_PPI)))
        j = min(self.w - 1, max(0, int(x_in * DENSE_PPI)))
        return 1 - self.k * self.f[i, j]

    def share(self):
        return float((self.f > 0.5).mean())


def dense_field(roads, p):
    """The width field for a place, or None when nothing crowds (or the place
    is already drawn thin)."""
    thin = p.get("dense_line_mm", DENSE_LINE_MM)
    if p.get("busy") or p["line_mm"] <= thin or p.get("dense_line_mm") == 0:
        return None
    import numpy as np
    from scipy import ndimage as ndi
    m = render(roads, p["centre"], p["width_km"], p["line_mm"], DENSE_PPI, p.get("temple"), hand=True)
    m = m.resize((m.width // SS, m.height // SS), Image.LANCZOS)
    ink = np.asarray(m) > 127
    r = DENSE_GAP_MM * MM * DENSE_PPI / 2
    n = int(r) + 1
    yy, xx = np.mgrid[-n:n + 1, -n:n + 1]
    closed = ndi.binary_closing(ink, structure=xx ** 2 + yy ** 2 <= r * r + 0.25)
    dens = ndi.gaussian_filter((closed & ~ink).astype(float), 0.12 * DENSE_PPI)
    zone = ndi.binary_opening(dens > DENSE_THRESHOLD, iterations=3)
    if not zone.any():
        return None
    zone = ndi.binary_dilation(zone, iterations=round(0.1 * DENSE_PPI))
    f = np.clip(ndi.gaussian_filter(zone.astype(float), 0.06 * DENSE_PPI) * 1.6, 0, 1)
    # A patch smaller than DENSE_MIN_SQIN is a lone knot on an ordinary road;
    # thinning it reads as a glitch, so it keeps the full weight.
    lab, n = ndi.label(f > 0.5)
    sizes = ndi.sum(np.ones_like(lab), lab, range(1, n + 1)) / DENSE_PPI ** 2
    small = np.isin(lab, 1 + np.nonzero(sizes < DENSE_MIN_SQIN)[0])
    keep = np.isin(lab, 1 + np.nonzero(sizes >= DENSE_MIN_SQIN)[0])
    ramp = round(0.25 * DENSE_PPI)
    f[ndi.binary_dilation(small, iterations=ramp) & ~ndi.binary_dilation(keep, iterations=ramp)] = 0
    if not keep.any():
        return None
    return WidthField(f, thin / p["line_mm"])


def build(name, p, args):
    print(f"{name}: {p['label']}")
    roads = load_roads(p["counties"])
    if args.auto:
        p["width_km"] = auto_width(roads, p, args.max_fused)
        print(f"  widest frame that holds: {p['width_km']} km")
    if args.fit:
        fit(roads, p, args.max_fused)
    outdir = OUT / name
    outdir.mkdir(parents=True, exist_ok=True)
    global HAND_SWING
    hand = not args.plain and p.get("style", "hand") == "hand"
    HAND_SWING = args.swing if args.swing is not None else swing_for(p)
    tag = f"{name}-{p['width_km']:g}km-{p['line_mm']:g}mm" + (f"-hand{round(HAND_SWING * 100)}" if hand else "")
    markers = markers_for(name)
    if markers:
        print(f"  {len(markers)} numbered markers")
    field = dense_field(roads, p) if hand and not args.no_thin else None
    if field:
        print(f"  crowded patches drawn at {p.get('dense_line_mm', DENSE_LINE_MM):g} mm: "
              f"{100 * field.share():.1f}% of the map")
    preview = render(roads, p["centre"], p["width_km"], p["line_mm"], 100, p.get("temple"), hand=hand,
                     markers=markers, marker_label=p["label"], field=field)
    fused = fused_pct(preview, p["line_mm"], 100)
    frame_and_label(preview, p["label"], 100 * SS)
    print(f"  {p['width_km']:g} km at {p['line_mm']:g} mm: "
          f"{fused:.1f}% fused")
    save(preview, outdir / f"{tag}-preview.png", 100)
    if not args.preview_only:
        save(render(roads, p["centre"], p["width_km"], p["line_mm"], 300, p.get("temple"), p["label"], hand,
                    markers=markers, field=field),
             outdir / f"{tag}-print-300dpi.png", 300)
    if p.get("temple"):
        save_front(front(*p["temple"]), outdir / f"{name}-front-6in-300dpi.png")
    else:
        save_front(front(), outdir / f"{name}-front-plain-6in-300dpi.png")
    print(f"  -> {outdir.relative_to(ROOT)}/")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("places", nargs="*", help="keys in places.json")
    ap.add_argument("--auto", action="store_true", help="find the widest frame that holds")
    ap.add_argument("--max-fused", type=float, default=6.0)
    ap.add_argument("--fit", action="store_true",
                    help="1.5 mm, or 0.5 mm for busy places (narrowed if needed); saves to places.json")
    ap.add_argument("--all", action="store_true", help="every place in places.json")
    ap.add_argument("--swing", type=float,
                    help="override the hand-drawn width swing (default 0.4 small towns, 0.1 busy cities)")
    ap.add_argument("--no-thin", action="store_true",
                    help="keep every line at the place's weight (no 0.5 mm in crowded patches)")
    ap.add_argument("--plain", action="store_true",
                    help="even-width lines with round ends instead of the hand-drawn style")
    ap.add_argument("--preview-only", action="store_true", help="skip the 300 ppi print file")
    args = ap.parse_args()
    places = {k: v for k, v in json.loads(PLACES.read_text()).items() if not k.startswith("_")}
    names = list(places) if args.all else args.places
    if not names:
        ap.error("name at least one place, or use --all")
    for name in names:
        if name not in places:
            sys.exit(f"unknown place {name!r}; known: {', '.join(places)}")
        build(name, places[name], args)
    if args.fit or args.auto:
        raw = json.loads(PLACES.read_text())
        for name in names:
            raw[name].update(width_km=places[name]["width_km"], line_mm=places[name]["line_mm"])
        PLACES.write_text(json.dumps(raw, indent=2) + "\n")


if __name__ == "__main__":
    main()
