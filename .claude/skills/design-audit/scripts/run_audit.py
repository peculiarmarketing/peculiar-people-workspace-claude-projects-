#!/usr/bin/env python3
"""Run every measurement for one design and write everything to one folder.

usage: run_audit.py <image> --width 12 --width 10 [--method all|screen|dtf|dtg]
                    [--ink #FFFFFF --bg #001A58] [--outdir <dir>]

Writes <outdir>/measurements.json, print_check.json, the print-flag overlays and
the preview images, then prints a short summary the report can quote.
"""
import argparse
import json
import os
import subprocess
import sys

import common as C
import measure
import print_check

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("image")
    ap.add_argument("--width", type=float, action="append", required=True)
    ap.add_argument("--method", default="all")
    ap.add_argument("--ink")
    ap.add_argument("--bg")
    ap.add_argument("--outdir")
    a = ap.parse_args()
    out = a.outdir or os.path.splitext(a.image)[0] + "_audit"
    os.makedirs(out, exist_ok=True)
    m, _ = measure.measure(a.image, a.ink, a.bg)
    mp = os.path.join(out, "measurements.json")
    C.dump(m, mp)
    pc = print_check.run(a.image, mp, a.width, a.method, out)
    C.dump(pc, os.path.join(out, "print_check.json"))
    if m["rings"]:
        cmd = [sys.executable, os.path.join(HERE, "targets.py"), mp, "--method", a.method,
               "--out", os.path.join(out, "targets.json")]
        for w in a.width:
            cmd += ["--width", str(w)]
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL)
    cmd = [sys.executable, os.path.join(HERE, "previews.py"), a.image, "--outdir", out]
    for w in a.width:
        cmd += ["--width", str(w)]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL)
    # summary
    print(f"output: {out}")
    print(f"ink {m['ink']['width_px']}x{m['ink']['height_px']} px, {len(m['rings'])} rings")
    for g in m["rings"]:
        print(f"  {g['id']}: r_out {g['r_outer']} width {g['width_mean']} px (cv {g['width_cv_pct']}%), "
              f"centre offset {g['offset_from_outer_px']} px")
    for w in pc["widths"]:
        for meth, r in w["methods"].items():
            mf = r["morphology"]["fail"]
            cg = mf["closing_gaps"]["regions"] if mf["closing_gaps"] else "n/a"
            print(f"  {w['print_width_in']:g} in, {meth}: {len(r['fail'])} FAIL, {len(r['warn'])} WARN elements; "
                  f"at fail level {mf['thin_strokes']['regions']} thin-stroke and {cg} closing-gap regions")


if __name__ == "__main__":
    main()
