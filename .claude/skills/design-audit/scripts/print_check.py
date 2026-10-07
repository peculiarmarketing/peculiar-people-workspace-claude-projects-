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
    min_gap_px = max(min_gap_px, 1)
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
        big.append({"bbox_in_crop": c["bbox"], "length_mm": units.conv(max(x1 - x0, y1 - y0) + 1)["mm"],
                    "area_mm2": round(c["area"] / units.ppi ** 2 * 645.16, 3)})
    big.sort(key=lambda b: -b["area_mm2"])
    return {"regions": len(big), "specks_ignored": specks, "largest": big[:12],
            "total_area_mm2": round(sum(b["area_mm2"] for b in big), 2)}


def cap_to_pt(cap_px, units, cap_ratio):
    """Estimate the font size from cap height. Most text faces have a cap height
    between 0.65 and 0.72 of the em; thresholds give the ratio they assume."""
    return round(units.conv(cap_px)["pt"] / cap_ratio, 1)


def status(v, fail, warn):
    if fail and v < fail:
        return "FAIL"
    if warn and v < warn:
        return "WARN"
    return "PASS"


def element_checks(m, units, th, method):
    t = th["methods"][method]
    tx = th["text"]
    cap_ratio = tx["cap_height_to_em"]
    rows = []

    def add(element, what, px, kind, rule):
        if px is None:
            return
        v = units.conv(px)
        fail, warn = t[f"{kind}_fail_mm"], t[f"{kind}_warn_mm"]
        rows.append({"element": element, "measure": what, **{k: v[k] for k in ("px", "in", "mm", "pt")},
                     "fail_mm": fail, "warn_mm": warn, "status": status(v["mm"], fail, warn), "rule": rule})

    def add_text(element, cap_px):
        v = units.conv(cap_px)
        pt = round(v["pt"] / cap_ratio, 1)
        rows.append({"element": element, "measure": "cap height / est. font size",
                     "px": v["px"], "in": v["in"], "mm": v["mm"], "cap_height_pt": v["pt"], "est_font_pt": pt,
                     "fail_pt": tx["fail_pt"], "warn_pt": tx["warn_pt"],
                     "status": status(pt, tx["fail_pt"], tx["warn_pt"]), "rule": "PRINT-05"})

    for g in m.get("rings", []):
        add(g["id"], "ring width (5th pct around the ring)", g["width"]["p05"], "line", "PRINT-01")
    for gap in m.get("ring_gaps", []):
        add("/".join(gap["between"]), "gap between rings (narrowest)", gap["min_px"], "gap", "PRINT-03")
    for z in m.get("zones", []):
        for a in z["arcs"]:
            if a.get("kind") != "text":
                continue
            name = f"{a['position']} arc in {'/'.join(z['between'])}"
            s = a.get("stroke_px") or {}
            add(name, "type stem", s.get("stem_px"), "line", "PRINT-01")
            add(name, "type hairline", s.get("hairline_px"), "line", "PRINT-02")
            lg = a.get("letter_gap_px")
            if lg:
                add(name, "letter gap (5th pct)", lg["p05"], "gap", "PRINT-03")
            add_text(name, a["cap_height_px"])
    c = m.get("centre")
    if c:
        art = c["art"]
        if art.get("weights"):
            add("centre art", "lightest line weight (cluster centre)", art["weights"][0]["weight_px"], "line", "PRINT-01")
        add("centre art", "line width (10th pct)", art["stroke_px"]["p10"], "line", "PRINT-01")
        cap = c.get("caption")
        if cap:
            s = cap.get("stroke_px") or {}
            add("caption", "type stem", s.get("stem_px"), "line", "PRINT-01")
            add("caption", "type hairline", s.get("hairline_px"), "line", "PRINT-02")
            if cap.get("letter_gap_px"):
                add("caption", "letter gap (5th pct)", cap["letter_gap_px"]["p05"], "gap", "PRINT-03")
            add_text("caption", cap["cap_height_px"])
    if not m.get("rings"):
        if m.get("strokes_weights"):
            add("whole design", "lightest line weight (cluster centre)", m["strokes_weights"][0]["weight_px"], "line", "PRINT-01")
        if m.get("strokes_all"):
            add("whole design", "line width (10th pct)", m["strokes_all"]["p10"], "line", "PRINT-01")
    return rows, t


def overlay(mask, thin, gaps, path, shrink_to=1600):
    """Overlay of the ink bounding box (plus 8 px). Large images are shrunk to
    shrink_to px wide: multiply overlay coordinates by (crop width / overlay width)
    to get back to analysis pixels."""
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
    rgb, mask, info, soft = C.load(image, want_soft=True)
    bb = m["ink"]["bbox"]
    pad = 8
    box = (max(0, bb[0] - pad), max(0, bb[1] - pad), min(mask.shape[1] - 1, bb[2] + pad), min(mask.shape[0] - 1, bb[3] + pad))
    basis_px = m["ink"]["width_px"] if basis == "ink" else m["canvas"]["width"]
    os.makedirs(outdir, exist_ok=True)
    methods = [method] if method != "all" else list(th["methods"])
    cache = {}
    res = {"thresholds_file": os.path.relpath(THRESH, outdir), "basis": basis,
           "basis_px": basis_px, "widths": []}
    for wi in widths:
        u = C.Units(wi, basis_px)
        smalls = [{"bbox": c["bbox"], "area_mm2": round(c["area_px"] / u.ppi ** 2 * 645.16, 3),
                   "max_dim_mm": u.conv(c["max_dim_px"])["mm"]} for c in m.get("smallest_components", [])]
        entry = {"print_width_in": wi, "smallest_shapes": smalls[:15], "ppi": round(u.ppi, 2), "px_per_mm": round(u.ppi / 25.4, 3),
                 "px_resolution_mm": round(25.4 / u.ppi, 3),
                 "design_height_in": round(m["ink"]["height_px"] / u.ppi, 3), "methods": {}}
        for meth in methods:
            rows, lim = element_checks(m, u, th, meth)
            r = {"limits": {k: v for k, v in lim.items() if k != "sources"}, "element_checks": rows,
                 "fail": [x for x in rows if x["status"] == "FAIL"],
                 "warn": [x for x in rows if x["status"] == "WARN"], "morphology": {}}
            for level in ("fail", "warn"):
                line_px = lim[f"line_{level}_mm"] / 25.4 * u.ppi
                gap_px = lim[f"gap_{level}_mm"] / 25.4 * u.ppi
                k = C.pick_k(min(line_px, gap_px) if gap_px else line_px)
                mk = C.upsample(soft, k, box)
                key = (k, round(line_px * k, 3), round(gap_px * k, 3))
                if key not in cache:
                    cache[key] = morph_flags(mk, line_px * k, gap_px * k)
                thin, gaps, rl, rg = (x.copy() if hasattr(x, "copy") else x for x in cache[key])
                if k > 1:  # back to analysis pixels for counting and the overlay
                    thin = thin.reshape(thin.shape[0] // k, k, thin.shape[1] // k, k).any(axis=(1, 3))
                    gaps = gaps.reshape(gaps.shape[0] // k, k, gaps.shape[1] // k, k).any(axis=(1, 3))
                mcrop = mask[box[1]:box[3] + 1, box[0]:box[2] + 1]
                if not lim[f"gap_{level}_mm"]:
                    gaps[:] = False
                tag = f"{wi:g}in_{meth}_{level}"
                ov = os.path.join(outdir, f"print_flags_{tag}.png")
                overlay(mcrop, thin, gaps, ov)
                speck = SPECK_MM / 25.4 * u.ppi
                r["morphology"][level] = {
                    "line_mm": lim[f"line_{level}_mm"], "gap_mm": lim[f"gap_{level}_mm"],
                    "thin_strokes": blob_summary(thin, speck, u),
                    "closing_gaps": blob_summary(gaps, speck, u) if lim[f"gap_{level}_mm"] else None,
                    "upsample": k, "morph_radius_px": {"line": round(rl / k, 2),
                                                       "gap": round(rg / k, 2) if lim[f"gap_{level}_mm"] else None},
                    "overlay": os.path.basename(ov)}
            entry["methods"][meth] = r
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
