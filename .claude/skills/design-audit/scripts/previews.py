#!/usr/bin/env python3
"""Write the look-at-it copies: small-size test, blur (squint) test, one-colour
check and ink-spread preview. These are for the auditor's eyes; the numbers come
from measure.py and print_check.py.

  small_<n>in.png     the design at n inches wide on a 96 ppi screen, then
                      enlarged 4x with nearest neighbour so the pixel loss shows
  blur_<pct>.png      Gaussian blur at pct of the design width (squint test)
  onecolour.png       ink mask alone, black on white (one-colour / silhouette test)
  spread_<w>in.png    ink grown by the spread in print_thresholds.json at w inches

usage: previews.py <image> [--sizes 1 2] [--blur 0.5 1 2] [--width 12] [--outdir audit_out]
"""
import argparse
import json
import os

import numpy as np
from PIL import Image, ImageFilter

import common as C

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("image")
    ap.add_argument("--sizes", type=float, nargs="*", default=[1, 2])
    ap.add_argument("--blur", type=float, nargs="*", default=[0.5, 1, 2])
    ap.add_argument("--width", type=float, action="append", default=[])
    ap.add_argument("--screen-ppi", type=float, default=96)
    ap.add_argument("--outdir", default="audit_out")
    a = ap.parse_args()
    os.makedirs(a.outdir, exist_ok=True)
    rgb, mask, info = C.load(a.image)
    ys, xs = np.nonzero(mask)
    x0, y0, x1, y1 = xs.min(), ys.min(), xs.max(), ys.max()
    im = Image.fromarray(rgb).crop((x0, y0, x1 + 1, y1 + 1))
    crop_mask = mask[y0:y1 + 1, x0:x1 + 1]
    W = im.width
    written = []
    for s in a.sizes:
        px = max(8, int(round(s * a.screen_ppi)))
        small = im.resize((px, round(im.height * px / W)), Image.LANCZOS)
        big = small.resize((small.width * 4, small.height * 4), Image.NEAREST)
        p = os.path.join(a.outdir, f"small_{s:g}in.png")
        big.save(p)
        written.append(p)
    view = im.resize((1200, round(im.height * 1200 / W)), Image.LANCZOS) if W > 1200 else im
    for b in a.blur:
        rad = b / 100 * view.width
        p = os.path.join(a.outdir, f"blur_{b:g}pct.png")
        view.filter(ImageFilter.GaussianBlur(rad)).save(p)
        written.append(p)
    one = Image.fromarray(np.where(crop_mask, 0, 255).astype(np.uint8))
    p = os.path.join(a.outdir, "onecolour.png")
    one.resize((1200, round(one.height * 1200 / one.width)), Image.LANCZOS).save(p)
    written.append(p)
    th = json.load(open(os.path.join(HERE, "..", "references", "print_thresholds.json")))
    spread_mm = th.get("spread_preview_mm", 0.1)
    for w in a.width:
        ppi = W / w
        steps = max(1, int(round(spread_mm / 25.4 * ppi)))
        grown = C.dilate(crop_mask, steps)
        out = np.zeros(grown.shape + (3,), np.uint8)
        out[...] = (0, 26, 88)
        out[grown] = (255, 255, 255)
        out[grown & ~crop_mask] = (255, 120, 0)
        p = os.path.join(a.outdir, f"spread_{w:g}in.png")
        Image.fromarray(out).save(p)
        written.append(p)
    print("\n".join(written))


if __name__ == "__main__":
    main()
