#!/usr/bin/env python3
"""Cut a magnified evidence crop out of the design, for findings that need a
close look (kerning on the arc, a divider glyph, where a text arc starts).

Coordinates are analysis pixels as written in measurements.json (bboxes), or a
polar window around the outer ring centre.

usage: crop.py <image> --box x0 y0 x1 y1 [--zoom 4] --out crop.png
       crop.py <image> --polar <cx> <cy> <deg> <r> <half_size> [--zoom 4] --out crop.png
       (deg: 0 = 12 o'clock, clockwise; r: radius in px)
"""
import argparse
import math

from PIL import Image

import common as C


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("image")
    ap.add_argument("--box", type=float, nargs=4)
    ap.add_argument("--polar", type=float, nargs=5)
    ap.add_argument("--zoom", type=float, default=4)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    rgb, mask, info = C.load(a.image)
    im = Image.fromarray(rgb)
    if a.polar:
        cx, cy, deg, r, hs = a.polar
        x = cx + r * math.sin(math.radians(deg))
        y = cy - r * math.cos(math.radians(deg))
        box = (x - hs, y - hs, x + hs, y + hs)
    else:
        box = a.box
    box = tuple(int(round(v)) for v in box)
    # crop on a canvas padded with the ground colour, so a window past the edge
    # shows background rather than black
    bgc = tuple(info.get("background_rgb", (0, 0, 0)))
    c = Image.new("RGB", (box[2] - box[0], box[3] - box[1]), bgc)
    c.paste(im.crop((max(box[0], 0), max(box[1], 0), min(box[2], im.width), min(box[3], im.height))),
            (max(-box[0], 0), max(-box[1], 0)))
    c = c.resize((int(c.width * a.zoom), int(c.height * a.zoom)), Image.NEAREST)
    c.save(a.out)
    print(a.out)


if __name__ == "__main__":
    main()
