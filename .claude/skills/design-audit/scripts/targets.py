#!/usr/bin/env python3
"""Propose target numbers for rebuilding a seal's rings and type as vectors.

It keeps what the design already decided (how many rings, their order of weight,
where the text sits, the art) and corrects the numbers against the rules: every
stroke at or above the print minimum at the SMALLEST audited width, ring weights in
a clear ratio anchored on the art's own line weight, the band text centred
optically between its rings, equal gaps where the design uses repeated gaps, and
the inner ring concentric.

Values are given as a fraction of the outer diameter D, and in mm and pt at each
audited width, so a designer can build at any size. The proportions it uses come
from the "rebuild" block of references/print_thresholds.json; each has a rule id.

usage: targets.py <measurements.json> --width 12 --width 10 [--method dtf] [--out targets.json]
"""
import argparse
import json
import os

import common as C

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("measurements")
    ap.add_argument("--width", type=float, action="append", required=True)
    ap.add_argument("--method", default="dtf")
    ap.add_argument("--out", default="targets.json")
    a = ap.parse_args()
    m = json.load(open(a.measurements))
    th = json.load(open(os.path.join(HERE, "..", "references", "print_thresholds.json")))
    rb = th["rebuild"]
    meth = th["methods"][a.method] if a.method != "all" else {
        "min_line_mm": max(v["min_line_mm"] for v in th["methods"].values()),
        "min_gap_mm": max(v["min_gap_mm"] for v in th["methods"].values())}
    rings = m["rings"]
    if not rings:
        raise SystemExit("no rings detected; targets.py is for seals and badges")
    D = 2 * rings[0]["r_outer"]
    wmin = min(a.width)
    D_mm_small = wmin * 25.4  # the ink width is the outer diameter for a seal
    safety = rb["line_safety_factor"]
    floor_frac = meth["min_line_mm"] * safety / D_mm_small  # thinnest allowed stroke, as a fraction of D
    gap_floor_frac = meth["min_gap_mm"] * safety / D_mm_small

    # anchor: the art's heaviest weight (approved art is not redrawn, so rings tune to it)
    art_w = None
    c = m.get("centre")
    if c and c["art"].get("weights"):
        art_w = c["art"]["weights"][-1]["weight_px"] / D
    base = max(floor_frac, art_w or 0)
    order = sorted(range(len(rings)), key=lambda i: rings[i]["width_mean"])  # thinnest first
    ratio = rb["ring_weight_ratios"]  # e.g. [1, 2, 3] thinnest to heaviest
    targets = []
    for rank, i in enumerate(order):
        k = ratio[min(rank, len(ratio) - 1)]
        targets.append((i, base * k))
    targets.sort()
    out = {"D_px": D, "method": a.method, "min_line_mm": meth["min_line_mm"], "safety": safety,
           "anchor": {"art_heaviest_weight_frac": art_w, "print_floor_frac": round(floor_frac, 5),
                      "base_frac": round(base, 5),
                      "note": "base = max(print floor at the smallest width x safety, art heaviest line)"},
           "elements": []}

    def row(name, frac, current_frac, rule, note=""):
        e = {"element": name, "target_frac_D": round(frac, 5),
             "current_frac_D": round(current_frac, 5) if current_frac is not None else None,
             "rule": rule, "note": note, "at": {}}
        for w in a.width:
            mm = frac * w * 25.4
            e["at"][f"{w:g}in"] = {"mm": round(mm, 3), "pt": round(mm / 25.4 * 72, 2), "in": round(mm / 25.4, 4)}
        out["elements"].append(e)

    for (i, f) in targets:
        g = rings[i]
        row(f"{g['id']} stroke", f, g["width_mean"] / D, "LINE-02 / PRINT-01",
            f"rank {order.index(i) + 1} of {len(rings)} by weight; ratio {ratio}")
        if g.get("offset_from_outer_px", 0) > 0:
            row(f"{g['id']} centre offset", 0.0, g["offset_from_outer_px"] / D, "SEAL-01",
                "rebuild concentric on the outer ring centre")
    # gaps between rings: keep the current mean radius layout but enforce the gap floor
    for gap in m.get("ring_gaps", []):
        row(f"gap {gap['between'][0]} to {gap['between'][1]}", max(gap["mean_px"] / D, gap_floor_frac),
            gap["mean_px"] / D, "PRINT-02", "edge to edge; equalise the min and max around the circle")
    # band text: cap height and its optical centring between the rings
    for z in m.get("zones", []):
        band = z["band_width_px"]
        for arc in z["arcs"]:
            if arc.get("kind") != "text":
                continue
            name = f"{arc['position']} text in {z['between'][0]}/{z['between'][1]}"
            cap = arc["cap_height_px"]
            lo, hi = rb["band_cap_fraction"]
            if len([x for x in z["arcs"] if x.get("kind") == "text"]) == 1 or arc["position"] != "bottom":
                tgt = min(max(cap / band, lo), hi)
                row(f"{name} cap height", tgt * band / D, cap / D, "SEAL-03",
                    f"cap height {lo:.0%} to {hi:.0%} of the band it sits in")
            go, gi = arc.get("gap_to_outer_ring_px"), arc.get("gap_to_inner_ring_px")
            if go is not None and gi is not None and len([x for x in z["arcs"] if x.get("kind") == "text"]) == 1:
                eq = (go + gi) / 2
                row(f"{name} clearance to each ring", eq / D, None, "SEAL-04",
                    f"now {go:.1f} px outside vs {gi:.1f} px inside; set equal")
            lg = arc.get("letter_gap_to_cap")
            if lg is not None:
                row(f"{name} letter gap", arc["cap_height_px"] * lg / D, arc["cap_height_px"] * lg / D, "TYPE-03",
                    f"keep one tracking value for the whole arc; measured gap varies {arc.get('letter_gap_cv_pct')}% (cv)")
    C.dump(out, a.out)
    print(a.out)


if __name__ == "__main__":
    main()
