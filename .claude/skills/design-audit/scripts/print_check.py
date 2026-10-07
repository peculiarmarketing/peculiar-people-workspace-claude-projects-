#!/usr/bin/env python3
"""Convert the measured geometry to physical sizes at one or more print widths and
compare it with the print minimums in references/print_thresholds.json.

Two kinds of check:
  1. Element checks: each ring, each text arc's stems and hairlines, the centre
     art's lightest weight, letter gaps, ring gaps, all converted to in / mm / pt.
  2. Whole-image morphology: every stroke thinner than the minimum line and every
     gap narrower than the minimum gap, found by opening and closing the ink mask
     at that size. Writes overlays (red = stroke too thin, yellow = gap that will
     close) so the failure can be seen, not just counted.

usage: print_check.py <image> <measurements.json> --width 12 --width 10
                      [--method dtf] [--outdir audit_out]
"""
import argparse
import json
import math
import os

import numpy as np
from PIL import Image

import common as C

HERE = os.path.dirname(os.path.abspath(__file__))
SPECK_MM = 1.0  # flagged regions shorter than this are corner and tip noise
THRESH = os.path.join(HERE, "..", "references", "print_thresholds.json")


def load_thresholds(path=THRESH):
    with open(path) as f:
        return json.load(f)


def morph_flags(mask, min_line_px, min_gap_px):
    """Strokes thinner than min_line: ink that does not survive an opening.
    Gaps narrower than min_gap: background that a closing fills in."""
    r_line = max(1, int(math.ceil(min_line_px / 2 - 0.5)))
    r_gap = max(1, int(math.ceil(min_gap_px / 2 - 0.5)))
    er = mask.copy()
    for k in range(r_line):
        er = C._shift_min(er, cross=(k % 2 == 0))
    opened = C.dilate(er, r_line)
    thin = mask & ~opened
    closed = C.dilate(mask, r_gap)
    for k in range(r_gap):
        closed = C._shift_min(closed, cross=(k % 2 == 0))
    gaps = closed & ~mask
    return thin, gaps, r_line, r_gap


def blob_summary(flag, min_len_px, units):
    """Count flagged regions long enough to matter. Tips of tapered strokes and the
    corners of shapes always show a pixel or two; a region shorter than min_len is
    reported in `specks` and not counted as a failure."""
    comps = C.components(flag)
    big, specks = [], 0
    for c in comps:
        x0, y0, x1, y1 = c["bbox"]
        if max(x1 - x0, y1 - y0) + 1 < min_len_px:
            specks += 1
            continue
        big.append({"bbox": c["bbox"], "length_mm": units.conv(max(x1 - x0, y1 - y0) + 1)["mm"],
                    "area_mm2": round(c["area"] / units.ppi ** 2 * 645.16, 3)})
    big.sort(key=lambda b: -b["area_mm2"])
    return {"regions": len(big), "specks_ignored": specks, "largest": big[:12],
            "total_area_mm2": round(sum(b["area_mm2"] for b in big), 2)}


def cap_to_pt(cap_px, units, cap_ratio):
    """Estimate the font size from cap height. Most text faces have a cap height
    between 0.65 and 0.72 of the em; thresholds give the ratio they assume."""
    return round(units.conv(cap_px)["pt"] / cap_ratio, 1)


def element_checks(m, units, th, method):
    t = th["methods"][method]
    min_line = t["min_line_mm"]
    min_gap = t["min_gap_mm"]
    min_text = th["text"]["min_positive_text_pt"]
    min_rev = th["text"]["min_reversed_text_pt"]
    cap_ratio = th["text"]["cap_height_to_em"]
    rows = []

    def add(element, what, px, limit_mm, rule, kind="min"):
        if px is None:
            return
        v = units.conv(px)
        ok = v["mm"] >= limit_mm
        rows.append({"element": element, "measure": what, **{k: v[k] for k in ("px", "in", "mm", "pt")},
                     "limit_mm": limit_mm, "pass": bool(ok),
                     "margin_pct": round((v["mm"] / limit_mm - 1) * 100, 1), "rule": rule})

    for g in m.get("rings", []):
        add(g["id"], "ring width (thinnest point)", g["width"]["p05"], min_line, "PRINT-01")
    for gap in m.get("ring_gaps", []):
        add("/".join(gap["between"]), "gap between rings (narrowest)", gap["min_px"], min_gap, "PRINT-02")
    for z in m.get("zones", []):
        for a in z["arcs"]:
            if a.get("kind") != "text":
                continue
            name = f"{a['position']} arc in {'/'.join(z['between'])}"
            s = a.get("stroke_px") or {}
            add(name, "type stem", s.get("stem_px"), min_line, "PRINT-01")
            add(name, "type hairline", s.get("hairline_px"), min_line, "PRINT-01")
            lg = a.get("letter_gap_px")
            if lg:
                add(name, "letter gap (5th pct)", lg["p05"], min_gap, "PRINT-02")
            pt = cap_to_pt(a["cap_height_px"], units, cap_ratio)
            v = units.conv(a["cap_height_px"])
            rows.append({"element": name, "measure": "cap height / est. font size", **{k: v[k] for k in ("px", "in", "mm", "pt")},
                         "est_font_pt": pt, "limit_pt": min_text, "pass": pt >= min_text,
                         "margin_pct": round((pt / min_text - 1) * 100, 1), "rule": "PRINT-04"})
    c = m.get("centre")
    if c:
        art = c["art"]
        if art.get("weights"):
            add("centre art", "lightest line weight", art["weights"][0]["weight_px"], min_line, "PRINT-01")
        add("centre art", "line width (10th pct)", art["stroke_px"]["p10"], min_line, "PRINT-01")
        cap = c.get("caption")
        if cap:
            s = cap.get("stroke_px") or {}
            add("caption", "type stem", s.get("stem_px"), min_line, "PRINT-01")
            add("caption", "type hairline", s.get("hairline_px"), min_line, "PRINT-01")
            if cap.get("letter_gap_px"):
                add("caption", "letter gap (5th pct)", cap["letter_gap_px"]["p05"], min_gap, "PRINT-02")
            pt = cap_to_pt(cap["cap_height_px"], units, cap_ratio)
            v = units.conv(cap["cap_height_px"])
            rows.append({"element": "caption", "measure": "cap height / est. font size", **{k: v[k] for k in ("px", "in", "mm", "pt")},
                         "est_font_pt": pt, "limit_pt": min_text, "pass": pt >= min_text,
                         "margin_pct": round((pt / min_text - 1) * 100, 1), "rule": "PRINT-04"})
    return rows, {"min_line_mm": min_line, "min_gap_mm": min_gap, "min_text_pt": min_text,
                  "min_reversed_text_pt": min_rev}


def overlay(mask, thin, gaps, path, shrink_to=1600):
    h, w = mask.shape
    img = np.zeros((h, w, 3), np.uint8)
    img[...] = (0, 26, 88)
    img[mask] = (200, 205, 220)
    img[thin] = (255, 40, 40)
    img[gaps] = (255, 210, 0)
    im = Image.fromarray(img)
    if max(w, h) > shrink_to:
        # max-filter style shrink so one-pixel flags stay visible
        im = im.resize((shrink_to * w // max(w, h), shrink_to * h // max(w, h)), Image.BOX)
    im.save(path)


def run(image, mpath, widths, method, outdir, basis="ink"):
    m = json.load(open(mpath))
    th = load_thresholds()
    rgb, mask, info = C.load(image)
    basis_px = m["ink"]["width_px"] if basis == "ink" else m["canvas"]["width"]
    os.makedirs(outdir, exist_ok=True)
    methods = [method] if method != "all" else list(th["methods"])
    res = {"thresholds_file": os.path.relpath(THRESH, outdir), "basis": basis,
           "basis_px": basis_px, "widths": []}
    for wi in widths:
        u = C.Units(wi, basis_px)
        entry = {"print_width_in": wi, "ppi": round(u.ppi, 2), "px_per_mm": round(u.ppi / 25.4, 3),
                 "px_resolution_mm": round(25.4 / u.ppi, 3),
                 "design_height_in": round(m["ink"]["height_px"] / u.ppi, 3), "methods": {}}
        for meth in methods:
            rows, lim = element_checks(m, u, th, meth)
            line_px = lim["min_line_mm"] / 25.4 * u.ppi
            gap_px = lim["min_gap_mm"] / 25.4 * u.ppi
            thin, gaps, rl, rg = morph_flags(mask, line_px, gap_px)
            tag = f"{wi:g}in_{meth}"
            ov = os.path.join(outdir, f"print_flags_{tag}.png")
            overlay(mask, thin, gaps, ov)
            entry["methods"][meth] = {
                "limits": lim, "element_checks": rows,
                "failures": [r for r in rows if not r["pass"]],
                "thin_strokes": blob_summary(thin, SPECK_MM / 25.4 * u.ppi, u),
                "closing_gaps": blob_summary(gaps, SPECK_MM / 25.4 * u.ppi, u),
                "morph_radius_px": {"line": rl, "gap": rg},
                "overlay": os.path.basename(ov)}
        res["widths"].append(entry)
    return res


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("image")
    ap.add_argument("measurements")
    ap.add_argument("--width", type=float, action="append", required=True,
                    help="intended print width in inches, measured ink to ink (repeatable)")
    ap.add_argument("--method", default="all", help="screen, dtf, dtg, or all")
    ap.add_argument("--basis", default="ink", choices=["ink", "canvas"],
                    help="what the print width refers to (default: the ink, per house rule)")
    ap.add_argument("--outdir", default="audit_out")
    a = ap.parse_args()
    res = run(a.image, a.measurements, a.width, a.method, a.outdir, a.basis)
    p = os.path.join(a.outdir, "print_check.json")
    C.dump(res, p)
    print(p)


if __name__ == "__main__":
    main()
