"""Trim the black-on-white seal files from a white square to a white disc that
stops MARGIN_MM past the outer ring (radius 152.4 mm, 1800 px at 300 ppi).
Outside the disc is transparent. Rewrites the files in place, so it is safe to
run again after make_ink_files.py."""
import glob
import os
import re

import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "Peculiar People Seal")
R_MM, MARGIN_MM = 152.4, 2.0
R_PX, M_PX = 1800, round(MARGIN_MM / 25.4 * 300)  # 24 px

for path in glob.glob(os.path.join(OUT, "*black on white*.svg")):
    svg = open(path).read()
    body = svg[svg.index("<g "):]
    h = R_MM + MARGIN_MM
    head = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{2*h:.3f}mm" height="{2*h:.3f}mm" '
            f'viewBox="{-h:.4f} {-h:.4f} {2*h:.4f} {2*h:.4f}">'
            f'<circle cx="0" cy="0" r="{h:.4f}" fill="#FFFFFF"/>')
    open(path, "w").write(head + body)
    print("svg", os.path.basename(path))

for path in glob.glob(os.path.join(OUT, "*black on white*.png")):
    g = np.asarray(Image.open(path).convert("L"))
    n = g.shape[0]
    c = n // 2
    ink = g < 128
    ys, xs = np.nonzero(ink)
    reach = np.sqrt((ys + 0.5 - n / 2) ** 2 + (xs + 0.5 - n / 2) ** 2).max()
    assert reach <= R_PX + 1, (path, reach)
    k = 2 * (R_PX + M_PX)
    crop = ink[c - k // 2:c + k // 2, c - k // 2:c + k // 2]
    yy, xx = np.mgrid[:k, :k] + 0.5 - k / 2
    disc = xx ** 2 + yy ** 2 <= (R_PX + M_PX) ** 2
    level = np.where(crop, 0, 255).astype(np.uint8)
    alpha = np.where(disc | crop, 255, 0).astype(np.uint8)
    Image.fromarray(np.dstack([level] * 3 + [alpha]), "RGBA").save(path, dpi=(300, 300))
    print("png", os.path.basename(path), n, "->", k, "ink reach", round(reach, 1))
