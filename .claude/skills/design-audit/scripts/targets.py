#!/usr/bin/env python3
"""Propose target numbers for rebuilding a seal's rings and type as vectors.

Keeps what the design already decided (how many rings, their order of weight, which
text sits where, the art) and corrects the numbers against the rules:

  - strokes: a FLOOR (the binding method's fail level at the smallest width) and a
    MARGIN target (its warn level), reported separately, because the margin is
    often unreachable inside a small cap height
  - ring weights in the 1:2:4 steps of LINE-02, anchored on max(floor, art's
    heaviest line) (LINE-04)
  - every ring and text path concentric on the outer ring (SEAL-01, SEAL-08)
  - a band holding one text line: equal clearance to both rings (SEAL-04)
  - a zone holding a top word and a bottom line: both on the zone's centre line (TYPE-06)
  - the art-plus-caption block slightly above the field centre (COMP-02)
  - fit checks: stroke-to-cap ratio (can a real face do it?), three strokes plus two
    gaps inside the cap height (E, B), and the arc room each text line has left

"Binding" with --method all: the strictest line rule and the strictest gap rule
across the methods that could apply, which may come from different methods; both
are named in the output. Every value is a fraction of the outer diameter D plus mm
and pt at each audited width; "pt" is a length, never a font size.

usage: targets.py <measurements.json> --width 12 --width 10 [--method all|dtf|dtg|screen] [--out targets.json]
"""
import argparse
import json
import os

import common as C

HERE = os.path.dirname(os.path.abspath(__file__))


def binding(th, method):
    names = [k for k in th["methods"] if k != "screen_transfer"] if method == "all" else [method]
    out = {}
    for lvl in ("fail", "warn"):
        for kind in ("line", "gap"):
            k = f"{kind}_{lvl}_mm"
            src = max(names, key=lambda n: th["methods"][n][k])
            out[k] = th["methods"][src][k]
            out[k + "_from"] = src
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("measurements")
    ap.add_argument("--width", type=float, action="append", required=True)
    ap.add_argument("--method", default="all")
    ap.add_argument("--out", default="targets.json")
    a = ap.parse_args()
    m = json.load(open(a.measurements))
    th = json.load(open(os.path.join(HERE, "..", "references", "print_thresholds.json")))
    rb, tx = th["rebuild"], th["text"]
    rings = m["rings"]
    if not rings:
        raise SystemExit("no rings detected; targets.py is for seals and badges")
    D = 2 * rings[0]["r_outer"]
    wmin = min(a.width)
    Dmm = wmin * 25.4  # for a seal the ink width is the outer diameter
    B = binding(th, a.method)

    def f(mm):  # mm at the smallest width -> fraction of D
        return mm / Dmm
    line_floor, line_margin = f(B["line_fail_mm"]), f(B["line_warn_mm"])
    gap_floor, gap_margin = f(B["gap_fail_mm"]), f(B["gap_warn_mm"])
    gap_use = gap_floor or gap_margin  # methods with no gap fail level use the warn level
    cap_floor = f(tx["warn_pt"] * tx["cap_height_to_em"] / 72 * 25.4)

    out = {"D_px": D, "method": a.method, "smallest_width_in": wmin, "binding": B,
           "floors_frac_D": {"line_floor": round(line_floor, 5), "line_margin": round(line_margin, 5),
                             "gap_floor": round(gap_floor, 5), "gap_margin": round(gap_margin, 5),
                             "cap_floor": round(cap_floor, 5)},
           "elements": [], "geometry_now": [], "checks": []}

    def at(frac):
        return {f"{w:g}in": {"mm": round(frac * w * 25.4, 3), "pt": round(frac * w * 72, 2)} for w in a.width}

    def row(name, target, current, rule, note="", margin=None):
        e = {"element": name, "target_frac_D": None if target is None else round(target, 5),
             "current_frac_D": None if current is None else round(current, 5), "rule": rule, "note": note}
        if target is not None:
            e["at"] = at(target)
        if margin is not None:
            e["margin_frac_D"] = round(margin, 5)
            e["margin_at"] = at(margin)
        out["elements"].append(e)

    def geo(name, frac):
        out["geometry_now"].append({"element": name, "frac_D": round(frac, 5), "at": at(frac)})

    # --- current geometry, outside in (radii from the outer centre) -------------
    for g in rings:
        geo(f"{g['id']} outer edge radius", g["r_outer"] / D)
        geo(f"{g['id']} inner edge radius", g["r_inner"] / D)
    for z in m.get("zones", []):
        for arc in z["arcs"]:
            if arc.get("kind") == "text":
                geo(f"{arc['position']} text centre-line radius in {'/'.join(z['between'])}", arc["r_center"] / D)
    c = m.get("centre")
    if c:
        geo("inner field diameter", c["inner_diameter_px"] / D)

    # --- rings ----------------------------------------------------------------
    art_w = c["art"]["weights"][-1]["weight_px"] / D if c and c["art"].get("weights") else 0
    base = max(line_floor, art_w)
    base_m = max(line_margin, art_w)
    out["anchor"] = {"art_heaviest_weight_frac": round(art_w, 5), "base_floor_frac": round(base, 5),
                     "base_margin_frac": round(base_m, 5),
                     "note": "thinnest ring = max(line floor or margin at the smallest width, art's heaviest line)"}
    order = sorted(range(len(rings)), key=lambda i: rings[i]["width_mean"])
    ratio = rb["ring_weight_ratios"]
    for rank, i in enumerate(order):
        k = ratio[min(rank, len(ratio) - 1)]
        g = rings[i]
        row(f"{g['id']} stroke", base * k, g["width_mean"] / D, "LINE-02, SEAL-03, PRINT-01",
            f"rank {rank + 1} of {len(rings)} by weight; steps {ratio}", margin=base_m * k)
        if g.get("offset_from_outer_px", 0) >= 1:
            row(f"{g['id']} centre offset", 0.0, g["offset_from_outer_px"] / D, "SEAL-01",
                "rebuild concentric on the outer ring centre")
    for gap in m.get("ring_gaps", []):
        row(f"gap {gap['between'][0]} to {gap['between'][1]}", max(gap["mean_px"] / D, gap_use),
            gap["mean_px"] / D, "SEAL-02, PRINT-03",
            f"edge to edge; now {gap['min_px']:.1f} to {gap['max_px']:.1f} px around the circle, make it uniform")

    # --- text -----------------------------------------------------------------
    for z in m.get("zones", []):
        texts = [x for x in z["arcs"] if x.get("kind") == "text"]
        orns = [x for x in z["arcs"] if x.get("kind") == "ornament"]
        zone = "/".join(z["between"])
        for arc in texts:
            name = f"{arc['position']} text in {zone}"
            cap = arc["cap_height_px"] / D
            capt = max(cap, cap_floor)
            row(f"{name} cap height", capt, cap, "PRINT-05",
                f"at least {tx['warn_pt']} pt type (cap {cap_floor * Dmm:.2f} mm) at {wmin:g} in; no source "
                "fixes cap height as a share of the band, so a clearing size is kept")
            st = arc.get("stroke_px") or {}
            if st.get("hairline_px") is not None:
                row(f"{name} thinnest stroke (hairline)", max(st["hairline_px"] / D, line_floor), st["hairline_px"] / D,
                    "PRINT-02, TYPE-07", "floor is the binding fail level; margin is the warn level",
                    margin=max(st["hairline_px"] / D, line_margin))
                out["checks"].append({
                    "check": f"{name}: stroke-to-cap ratio", "at_floor": round(line_floor / capt, 3),
                    "at_margin": round(line_margin / capt, 3),
                    "reading": "under 0.10 most text faces; 0.10 to 0.15 a medium monoline; 0.15 to 0.20 a bold "
                               "monoline; over 0.20 no ordinary face: grow the type or settle the larger print width"})
                need = 3 * line_floor + 2 * gap_use
                out["checks"].append({
                    "check": f"{name}: three strokes plus two counters fit the cap height (E, B)",
                    "needed_frac_D": round(need, 5), "cap_frac_D": round(capt, 5), "fits": need <= capt})
            lg = arc.get("letter_gap_px")
            if lg:
                row(f"{name} narrowest letter gap", max(lg["min"] / D, gap_use), lg["min"] / D,
                    "PRINT-03, TYPE-03", f"one tracking value per arc; spacing varies {arc.get('letter_gap_cv_pct')}% (cv)",
                    margin=max(lg["min"] / D, gap_margin))
            room = min(arc.get("room_before_px", 1e9), arc.get("room_after_px", 1e9))
            if room < 1e9:
                out["checks"].append({
                    "check": f"{name}: arc room before the next element", "px": room, "frac_D": round(room / D, 5),
                    "reading": "if heavier strokes or wider gaps lengthen the line by more than twice this, it no "
                               "longer fits between its neighbours: shorten it, move dividers, or settle the larger width"})
        if len(texts) == 1:
            arc = texts[0]
            go, gi = arc["gap_to_outer_ring_px"], arc["gap_to_inner_ring_px"]
            row(f"{arc['position']} text in {zone}: clearance to each ring", (go + gi) / 2 / D, None, "SEAL-04",
                f"now {go:.1f} px outside vs {gi:.1f} px inside; set equal")
            row(f"{arc['position']} text in {zone}: centre-line radius", arc["zone_center_line_r"] / D,
                arc["r_center"] / D, "SEAL-04, TYPE-06")
        elif len(texts) == 2:
            row(f"centre-line radius for both arcs in {zone}", texts[0]["zone_center_line_r"] / D, None, "TYPE-06",
                f"zone centre line between the rings; now {texts[0]['r_center']:.1f} px ({texts[0]['position']}) and "
                f"{texts[1]['r_center']:.1f} px ({texts[1]['position']})")
        if orns:
            shapes = [(o["radial_extent_px"], o["tangential_extent_px"]) for o in orns]
            same = max(abs(r - shapes[0][0]) + abs(t - shapes[0][1]) for r, t in shapes) <= 0.1 * max(shapes[0])
            desc = ", ".join(f"{r:.0f}x{t:.0f} px at {o['mid_deg']:.0f} deg" for (r, t), o in zip(shapes, orns))
            row(f"dividers in {zone}", max(max(s) for s in shapes) / D, max(max(s) for s in shapes) / D,
                "SEAL-05, SEAL-08",
                ("same orientation to the path at every position" if same else
                 f"orientation differs by position (radial x tangential: {desc}): rotate each so its long axis "
                 "points at the centre") + "; centre each on the text centre line")

    # --- centre block ---------------------------------------------------------
    if c:
        blk = c.get("art_plus_caption") or {"bbox_center_offset": c["art"]["bbox_center_offset"]}
        dy = blk["bbox_center_offset"][1]
        row("art-plus-caption block centre, above the ring centre", 0.012, -dy / D, "COMP-02",
            "target 0 to 5 percent of the field height above centre (0.012 D is a middle value); "
            "current: positive is above centre, negative below")
        row("art clearance to inner ring (minimum)", c["art"]["min_radial_clearance_px"] / D,
            c["art"]["min_radial_clearance_px"] / D, "SEAL-06", "keep at least the smallest text-to-ring clearance")
        if c.get("caption"):
            cap = c["caption"]["cap_height_px"] / D
            row("caption cap height", max(cap, cap_floor), cap, "PRINT-05, RATIO-03")
            st = c["caption"].get("stroke_px") or {}
            if st.get("hairline_px") is not None:
                row("caption thinnest stroke (hairline)", max(st["hairline_px"] / D, line_floor), st["hairline_px"] / D,
                    "PRINT-02, TYPE-07", "sturdier face or larger size", margin=max(st["hairline_px"] / D, line_margin))
            row("art to caption gap", c["caption"]["gap_to_art_px"] / D, c["caption"]["gap_to_art_px"] / D, "COMP-04")
    C.dump(out, a.out)
    print(a.out)


if __name__ == "__main__":
    main()
