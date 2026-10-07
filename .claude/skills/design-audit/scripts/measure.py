#!/usr/bin/env python3
"""Pixel geometry of a logo, seal or garment graphic.

Measures, in pixels (print_check.py converts to inches, mm and points):
  - ink bounding box, centre of mass, and their offsets from the canvas centre
  - rings: each ring's own fitted centre, inner and outer radius, and width
    (mean, min, max) around the circle; concentricity against the outer ring
  - zones between rings, the text arcs in each zone (cap height, stroke width,
    letter gaps, clearance to the rings above and below, how centred the arc is)
  - the centre art inside the innermost ring and any caption line under it
    (size, clearance to the ring, offset from the ring centre, stroke weights)
  - global stroke and gap distributions

usage: measure.py <image> [--ink #FFFFFF] [--bg #001A58] [--out measurements.json]
"""
import argparse
import math

import numpy as np

import common as C

N_ANG = 1440  # quarter-degree polar sampling


# ----------------------------------------------------------------- rings ---

def polar(mask, cx, cy, rmax):
    """Sample the mask on (angle, radius) rays from (cx, cy). Angle 0 is 12 o'clock,
    increasing clockwise, so the numbers read like a clock face."""
    th = np.linspace(0, 2 * np.pi, N_ANG, endpoint=False)
    r = np.arange(0, int(rmax))
    xs = cx + np.outer(np.sin(th), r)
    ys = cy - np.outer(np.cos(th), r)
    h, w = mask.shape
    xi = np.clip(np.round(xs).astype(int), 0, w - 1)
    yi = np.clip(np.round(ys).astype(int), 0, h - 1)
    inside = (xs >= 0) & (xs < w) & (ys >= 0) & (ys < h)
    return mask[yi, xi] & inside, th, r


def find_rings(mask, cx, cy, rmax, min_cov=0.6):
    """A ring is a radius band where at least `min_cov` of all rays hit ink.
    Text bands peak far lower (letters cover well under half the circle), so the
    threshold separates them. Each candidate is then fitted on its own, because an
    off-centre ring smears across radii when sampled from the wrong centre."""
    P, th, r = polar(mask, cx, cy, rmax)
    cov = P.mean(axis=0)
    covs = np.maximum.reduce([np.roll(cov, k) for k in (-3, -2, -1, 0, 1, 2, 3)])
    is_ring = covs >= min_cov
    bands = []
    i = 0
    while i < len(r):
        if is_ring[i]:
            j = i
            while j + 1 < len(r) and is_ring[j + 1]:
                j += 1
            bands.append((int(r[i]), int(r[j])))
            i = j + 1
        else:
            i += 1
    rings = []
    for (r0, r1) in bands:
        ring = fit_ring(P, th, r, cx, cy, r0, r1)
        if ring:
            rings.append(ring)
    rings.sort(key=lambda g: -g["r_outer"])
    return rings, cov


def fit_ring(P, th, r, cx, cy, r0, r1):
    tol = max(4, (r1 - r0))
    lo, hi = max(0, r0 - tol), min(len(r) - 1, r1 + tol)
    inner_pts, outer_pts, widths = [], [], []
    for a in range(len(th)):
        seg = P[a, lo:hi + 1].astype(np.int8)
        if not seg.any():
            continue
        d = np.diff(np.concatenate([[0], seg, [0]]))
        s = np.flatnonzero(d == 1) + lo
        e = np.flatnonzero(d == -1) - 1 + lo
        mid = (r0 + r1) / 2
        k = int(np.argmin(np.abs((s + e) / 2 - mid)))
        if s[k] > r1 + 2 or e[k] < r0 - 2:
            continue
        inner_pts.append((th[a], s[k] - 0.5))
        outer_pts.append((th[a], e[k] + 0.5))
        widths.append(e[k] - s[k] + 1)
    if len(widths) < 0.5 * len(th):
        return None
    widths = np.array(widths, float)
    med = np.median(widths)
    mad = np.median(np.abs(widths - med)) + 0.5
    keep = np.abs(widths - med) <= 4 * mad  # drop rays where text or a glyph touches the ring
    ip = np.array(inner_pts)[keep]
    op = np.array(outer_pts)[keep]
    ix, iy = cx + ip[:, 1] * np.sin(ip[:, 0]), cy - ip[:, 1] * np.cos(ip[:, 0])
    ox, oy = cx + op[:, 1] * np.sin(op[:, 0]), cy - op[:, 1] * np.cos(op[:, 0])
    icx, icy, ir, ires = C.fit_circle(ix, iy)
    ocx, ocy, orr, ores = C.fit_circle(ox, oy)
    rcx, rcy = (icx + ocx) / 2, (icy + ocy) / 2
    # width measured from the ring's own centre, so an off-centre ring is not
    # reported as uneven just because it was sampled from the wrong point
    w_own = np.hypot(ox - rcx, oy - rcy) - np.hypot(ix - rcx, iy - rcy)
    # thickness variation around the ring: outer minus inner radius per ray
    return {"center": [round(rcx, 2), round(rcy, 2)],
            "r_inner": round(ir, 2), "r_outer": round(orr, 2),
            "r_mid": round((ir + orr) / 2, 2),
            "width": C.stats(w_own),
            "width_mean": round(float(np.mean(w_own)), 2),
            "width_cv_pct": round(float(np.std(w_own) / max(np.mean(w_own), 1e-6) * 100), 1),
            "inner_outer_center_gap": round(math.hypot(icx - ocx, icy - ocy), 2),
            "fit_rms": [round(ires, 2), round(ores, 2)],
            "coverage": round(len(widths) / len(th), 3),
            "rays_used": int(keep.sum())}


# ------------------------------------------------------------- text arcs ---

def comp_polar(c, cx, cy):
    dx = c["xs"] - cx
    dy = cy - c["ys"]
    rr = np.hypot(dx, dy)
    ang = np.arctan2(dx, dy) % (2 * np.pi)
    a0 = math.atan2(dx.mean(), dy.mean()) % (2 * np.pi)
    rel = (ang - a0 + np.pi) % (2 * np.pi) - np.pi
    return rr, a0, rel


def text_arcs(comps, cx, cy, r_lo, r_hi):
    """Group the components of one annulus into arcs of type. Components are sorted
    by angle; a new arc starts wherever the angular gap is far larger than a word
    space (more than 3 cap heights of arc length)."""
    items = []
    for c in comps:
        rr, a0, rel = comp_polar(c, cx, cy)
        if rr.min() < r_lo - 1 or rr.max() > r_hi + 1 or c["area"] < 6:
            continue
        items.append({"c": c, "a0": a0, "amin": a0 + rel.min(), "amax": a0 + rel.max(),
                      "rmin": float(rr.min()), "rmax": float(rr.max()),
                      "rmean": float(rr.mean())})
    if not items:
        return []
    items.sort(key=lambda t: t["a0"])
    hts = np.array([t["rmax"] - t["rmin"] for t in items])
    cap = float(np.median(hts))
    rmean = float(np.median([t["rmean"] for t in items]))
    split = 3 * cap / max(rmean, 1)
    # rotate the list so it starts after the largest gap (an arc may cross 12 o'clock)
    n = len(items)
    gaps = [((items[(i + 1) % n]["amin"] - items[i]["amax"]) % (2 * np.pi)) for i in range(n)]
    start = (int(np.argmax(gaps)) + 1) % n
    ordered = items[start:] + items[:start]
    arcs, cur = [], [ordered[0]]
    for prev, nxt in zip(ordered, ordered[1:]):
        g = (nxt["amin"] - prev["amax"]) % (2 * np.pi)
        if g > split:
            arcs.append(cur)
            cur = [nxt]
        else:
            cur.append(nxt)
    arcs.append(cur)
    return [summarise_arc(a, cx, cy) for a in arcs]


def summarise_arc(items, cx, cy):
    hts = np.array([t["rmax"] - t["rmin"] for t in items])
    cap = float(np.median(hts))
    # glyphs: drop specks (periods, dots, divider bullets) from the letter statistics
    glyph = [t for t, h in zip(items, hts) if h >= 0.6 * cap]
    rmean = float(np.median([t["rmean"] for t in glyph])) if glyph else float(np.median([t["rmean"] for t in items]))
    lgaps = []
    for a, b in zip(items, items[1:]):
        g = ((b["amin"] - a["amax"]) % (2 * np.pi)) * rmean
        lgaps.append(g)
    # specks (dots, bullets) sit between letters and would halve the gaps; measure
    # letter gaps between glyphs only
    gl = [t for t, h in zip(items, hts) if h >= 0.6 * cap]
    lg = np.array([((b["amin"] - a["amax"]) % (2 * np.pi)) * rmean for a, b in zip(gl, gl[1:])])
    letter, words = split_gaps(lg)
    a_start = items[0]["amin"] % (2 * np.pi)
    a_end = items[-1]["amax"] % (2 * np.pi)
    span = (a_end - a_start) % (2 * np.pi)
    mid = (a_start + span / 2) % (2 * np.pi)
    mid_deg = math.degrees(mid)
    ys = np.concatenate([t["c"]["ys"] for t in items])
    xs = np.concatenate([t["c"]["xs"] for t in items])
    return {"n_components": len(items), "n_glyphs": len(glyph),
            "start_deg": round(math.degrees(a_start), 2), "end_deg": round(math.degrees(a_end), 2),
            "span_deg": round(math.degrees(span), 2), "mid_deg": round(mid_deg, 2),
            "cap_height_px": round(cap, 2), "glyph_height": C.stats([h for h in hts if h >= 0.6 * cap]),
            "r_min": round(min(t["rmin"] for t in items), 2),
            "r_max": round(max(t["rmax"] for t in items), 2),
            "r_glyph_min": round(min(t["rmin"] for t in glyph), 2) if glyph else None,
            "r_glyph_max": round(max(t["rmax"] for t in glyph), 2) if glyph else None,
            "letter_gap_px": C.stats(letter),
            "word_gap_px": C.stats(words),
            "letter_gap_to_cap": round(float(np.median(letter)) / cap, 3) if letter.size else None,
            "kind": "text" if len(glyph) >= 3 else "ornament",
            "letter_gap_cv_pct": round(float(np.std(letter) / max(np.mean(letter), 1e-6) * 100), 1) if letter.size > 2 else None,
            "_pix": (ys, xs)}


# ---------------------------------------------------------- centre zone ----

def centre_zone(mask, comps, cx, cy, r_in):
    """Split the inner disc into art and an optional caption line under it. The
    caption is found as the lowest band of rows separated from the art by a clear
    horizontal gap and made only of small components."""
    inside = [c for c in comps if np.hypot(c["xs"] - cx, c["ys"] - cy).max() < r_in - 0.5]
    if not inside:
        return None
    ys = np.concatenate([c["ys"] for c in inside])
    y0, y1 = int(ys.min()), int(ys.max())
    prof = np.zeros(y1 - y0 + 1, int)
    for c in inside:
        np.add.at(prof, c["ys"] - y0, 1)
    empty = prof == 0
    caption, art = [], inside
    best = None
    i = 0
    while i < len(empty):
        if empty[i]:
            j = i
            while j + 1 < len(empty) and empty[j + 1]:
                j += 1
            if y0 + i > cy:  # only gaps in the lower half separate a caption
                best = (y0 + i, y0 + j)
            i = j + 1
        else:
            i += 1
    if best:
        below = [c for c in inside if c["bbox"][1] > best[1]]
        above = [c for c in inside if c["bbox"][3] < best[0]]
        if below and above:
            bh = max(c["bbox"][3] - c["bbox"][1] for c in below)
            ah = max(c["bbox"][3] for c in above) - min(c["bbox"][1] for c in above)
            if bh < 0.2 * ah:
                caption, art = below, above
    out = {}
    ax = np.concatenate([c["xs"] for c in art])
    ay = np.concatenate([c["ys"] for c in art])
    bb = [int(ax.min()), int(ay.min()), int(ax.max()), int(ay.max())]
    rr = np.hypot(ax - cx, ay - cy)
    out["art"] = {"bbox": bb, "width_px": bb[2] - bb[0] + 1, "height_px": bb[3] - bb[1] + 1,
                  "width_pct_of_inner_diameter": round((bb[2] - bb[0] + 1) / (2 * r_in) * 100, 1),
                  "height_pct_of_inner_diameter": round((bb[3] - bb[1] + 1) / (2 * r_in) * 100, 1),
                  "bbox_center_offset": [round((bb[0] + bb[2]) / 2 - cx, 2), round((bb[1] + bb[3]) / 2 - cy, 2)],
                  "mass_center_offset": [round(float(ax.mean()) - cx, 2), round(float(ay.mean()) - cy, 2)],
                  "min_radial_clearance_px": round(r_in - float(rr.max()), 2),
                  "clearance_px": {"top": round(bb[1] - (cy - r_in), 2), "bottom": round((cy + r_in) - bb[3], 2),
                                   "left": round(bb[0] - (cx - r_in), 2), "right": round((cx + r_in) - bb[2], 2)}}
    art_mask = np.zeros(mask.shape, bool)
    art_mask[ay, ax] = True
    out["_art_mask"] = art_mask
    if caption:
        cxs = np.concatenate([c["xs"] for c in caption])
        cys = np.concatenate([c["ys"] for c in caption])
        cb = [int(cxs.min()), int(cys.min()), int(cxs.max()), int(cys.max())]
        hts = [c["bbox"][3] - c["bbox"][1] + 1 for c in caption]
        cap = float(np.median(hts))
        caption.sort(key=lambda c: c["bbox"][0])
        g = np.array([b["bbox"][0] - a["bbox"][2] - 1 for a, b in zip(caption, caption[1:])], float)
        letter, words = split_gaps(g)
        crr = np.hypot(cxs - cx, cys - cy)
        out["caption"] = {"bbox": cb, "cap_height_px": round(cap, 2),
                          "width_px": cb[2] - cb[0] + 1,
                          "center_x_offset": round((cb[0] + cb[2]) / 2 - cx, 2),
                          "gap_to_art_px": cb[1] - bb[3] - 1,
                          "min_radial_clearance_px": round(r_in - float(crr.max()), 2),
                          "letter_gap_px": C.stats(letter), "word_gap_px": C.stats(words),
                          "letter_gap_to_cap": round(float(np.median(letter)) / cap, 3) if letter.size else None}
        blk = [min(bb[0], cb[0]), bb[1], max(bb[2], cb[2]), cb[3]]
        out["art_plus_caption"] = {"bbox": blk,
                                   "bbox_center_offset": [round((blk[0] + blk[2]) / 2 - cx, 2), round((blk[1] + blk[3]) / 2 - cy, 2)],
                                   "clearance_px": {"top": round(blk[1] - (cy - r_in), 2), "bottom": round((cy + r_in) - blk[3], 2)}}
        cm = np.zeros(mask.shape, bool)
        cm[cys, cxs] = True
        out["_caption_mask"] = cm
    return out


def split_gaps(g):
    """Separate letter gaps from word gaps. Word spaces form a second, wider cluster;
    2-means on the gaps finds it when the two centres differ by more than 1.6x."""
    g = np.asarray(g, float)
    if g.size < 4:
        return g, np.array([])
    c = np.quantile(g, [0.25, 0.9])
    for _ in range(20):
        lab = np.abs(g - c[0]) > np.abs(g - c[1])
        if lab.all() or (~lab).all():
            return g, np.array([])
        c = np.array([g[~lab].mean(), g[lab].mean()])
    if c[1] / max(c[0], 1e-6) < 1.6:
        return g, np.array([])
    return g[~lab], g[lab]


def type_strokes(widths):
    """Stem and hairline estimates for type. Ridge samples include serif tips and
    corners, which drag the median down, so the stem is the 75th percentile and the
    hairline the 10th. Widths are quantised to about 1 px."""
    st = C.stats(widths)
    if st:
        w = np.asarray(widths, float)
        st["stem_px"] = round(float(np.quantile(w, 0.75)), 2)
        # one-pixel ridges are mostly anti-aliased corners and stroke tips; leave
        # them out unless the type is genuinely that thin (median under 3 px)
        wh = w[w > 1] if np.median(w) >= 3 and (w > 1).sum() > 10 else w
        st["hairline_px"] = round(float(np.quantile(wh, 0.20)), 2)
    return st


def weight_clusters(widths, kmax=3):
    """Group stroke widths into up to `kmax` weights with 1D k-means on log width.
    A cluster must hold at least 8 percent of samples to count as a weight."""
    w = np.asarray(widths, float)
    w = w[w >= 1]
    if w.size < 20:
        return []
    lw = np.log(w)
    best = None
    for k in range(1, kmax + 1):
        cent = np.quantile(lw, np.linspace(0.15, 0.85, k))
        for _ in range(30):
            lab = np.argmin(np.abs(lw[:, None] - cent[None, :]), axis=1)
            cent = np.array([lw[lab == j].mean() if (lab == j).any() else cent[j] for j in range(k)])
        sizes = np.bincount(lab, minlength=k) / lw.size
        sep = np.diff(np.sort(cent)).min() if k > 1 else 1
        if k > 1 and (sizes.min() < 0.08 or sep < math.log(1.35)):
            break
        best = (np.exp(cent), sizes)
    order = np.argsort(best[0])
    return [{"weight_px": round(float(best[0][i]), 2), "share": round(float(best[1][i]), 3)} for i in order]


# ------------------------------------------------------------------ main ---

def measure(path, ink=None, bg=None):
    rgb, mask, info = C.load(path, ink=ink, bg=bg)
    h, w = mask.shape
    ys, xs = np.nonzero(mask)
    if xs.size == 0:
        raise SystemExit("no ink found; pass --ink and --bg")
    bb = [int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max())]
    out = {"image": info, "canvas": {"width": w, "height": h},
           "ink": {"bbox": bb, "width_px": bb[2] - bb[0] + 1, "height_px": bb[3] - bb[1] + 1,
                   "coverage_pct_of_bbox": round(float(mask[bb[1]:bb[3] + 1, bb[0]:bb[2] + 1].mean() * 100), 2)}}
    bcx, bcy = (bb[0] + bb[2]) / 2, (bb[1] + bb[3]) / 2
    mcx, mcy = float(xs.mean()), float(ys.mean())
    out["centring"] = {"canvas_center": [w / 2, h / 2], "bbox_center": [bcx, bcy],
                       "mass_center": [round(mcx, 2), round(mcy, 2)],
                       "bbox_offset_from_canvas": [round(bcx - w / 2, 2), round(bcy - h / 2, 2)],
                       "mass_offset_from_bbox_center": [round(mcx - bcx, 2), round(mcy - bcy, 2)]}

    rings, cov = find_rings(mask, bcx, bcy, rmax=max(bb[2] - bcx, bcy - bb[1]) + 3)
    if rings:
        # refine: re-run from the outer ring's fitted centre
        ocx, ocy = rings[0]["center"]
        rings, cov = find_rings(mask, ocx, ocy, rmax=rings[0]["r_outer"] + 6)
    out["rings"] = rings
    comps = C.components(mask)
    out["n_components"] = len(comps)
    sw_all, _ = ridge_widths_cached(mask)
    out["strokes_all"] = C.stats(sw_all)

    if rings:
        cx, cy = rings[0]["center"]
        for i, g in enumerate(rings):
            g["id"] = f"ring{i + 1}"
            g["offset_from_outer"] = [round(g["center"][0] - cx, 2), round(g["center"][1] - cy, 2)]
            g["offset_from_outer_px"] = round(math.hypot(*g["offset_from_outer"]), 2)
        out["centring"]["outer_ring_center"] = [cx, cy]
        out["centring"]["outer_ring_offset_from_canvas"] = [round(cx - w / 2, 2), round(cy - h / 2, 2)]
        # gaps between consecutive rings, edge to edge, measured along the ring
        # centres (offset rings make the gap vary around the circle: min and max)
        gaps = []
        for a, b in zip(rings, rings[1:]):
            off = math.hypot(b["center"][0] - a["center"][0], b["center"][1] - a["center"][1])
            mean_gap = a["r_inner"] - b["r_outer"]
            gaps.append({"between": [a["id"], b["id"]], "mean_px": round(mean_gap, 2),
                         "min_px": round(mean_gap - off, 2), "max_px": round(mean_gap + off, 2)})
        out["ring_gaps"] = gaps
        # zones: the annuli between rings, and the disc inside the last ring
        zones = []
        for a, b in zip(rings, rings[1:]):
            arcs = text_arcs(comps, cx, cy, b["r_outer"], a["r_inner"])
            for arc in arcs:
                ys_, xs_ = arc.pop("_pix")
                m = np.zeros(mask.shape, bool)
                m[ys_, xs_] = True
                sw, _ = C.ridge_widths(m)
                arc["stroke_px"] = type_strokes(sw)
                arc["gap_to_outer_ring_px"] = round(a["r_inner"] - arc["r_glyph_max"], 2) if arc["r_glyph_max"] else None
                arc["gap_to_inner_ring_px"] = round(arc["r_glyph_min"] - b["r_outer"], 2) if arc["r_glyph_min"] else None
                if arc["gap_to_outer_ring_px"] is not None and arc["gap_to_inner_ring_px"]:
                    arc["outer_to_inner_gap_ratio"] = round(arc["gap_to_outer_ring_px"] / max(arc["gap_to_inner_ring_px"], 0.5), 3)
                arc["cap_height_pct_of_band"] = round(arc["cap_height_px"] / max(a["r_inner"] - b["r_outer"], 1) * 100, 1)
                arc["mid_offset_from_axis_deg"] = round(min(abs(arc["mid_deg"]), abs(arc["mid_deg"] - 360),
                                                            abs(arc["mid_deg"] - 180)), 2)
                arc["position"] = "top" if (arc["mid_deg"] < 60 or arc["mid_deg"] > 300) else (
                    "bottom" if 120 < arc["mid_deg"] < 240 else "side")
            zones.append({"between": [a["id"], b["id"]], "band_width_px": round(a["r_inner"] - b["r_outer"], 2),
                          "arcs": arcs})
        out["zones"] = zones
        last = rings[-1]
        cz = centre_zone(mask, comps, last["center"][0], last["center"][1], last["r_inner"])
        if cz:
            am = cz.pop("_art_mask")
            cm = cz.pop("_caption_mask", None)
            sw, _ = C.ridge_widths(am)
            cz["art"]["stroke_px"] = C.stats(sw)
            cz["art"]["weights"] = weight_clusters(sw)
            if cm is not None:
                sw, _ = C.ridge_widths(cm)
                cz["caption"]["stroke_px"] = type_strokes(sw)
            cz["inner_ring"] = last["id"]
            cz["inner_diameter_px"] = round(2 * last["r_inner"], 2)
        out["centre"] = cz
    else:
        out["ring_gaps"] = []
        out["zones"] = []
        out["centre"] = None
        out["strokes_weights"] = weight_clusters(sw_all)
    return out, mask


_cache = {}


def ridge_widths_cached(mask):
    k = id(mask)
    if k not in _cache:
        _cache[k] = C.ridge_widths(mask)
    return _cache[k]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("image")
    ap.add_argument("--ink")
    ap.add_argument("--bg")
    ap.add_argument("--out", default="measurements.json")
    a = ap.parse_args()
    out, _ = measure(a.image, a.ink, a.bg)
    C.dump(out, a.out)
    print(a.out)


if __name__ == "__main__":
    main()
