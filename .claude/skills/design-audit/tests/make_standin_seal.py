#!/usr/bin/env python3
"""Build a stand-in for the jacket seal so the audit scripts can be tested
before the real image is attached.

It is deliberately imperfect in the ways an AI-generated seal usually is, so the
checks have something to find: the inner ring is nudged off centre, the gaps
between rings are uneven, the thin ring is very thin, and the temple sits low.

--thin-ring adds a 5 px ring 6 px off centre between the title and the inner ring,
the case that seal.png exposed: sampled from the outer ring's centre it smears
across about 12 px of radius and no single radius reaches ring coverage. The
default output is unchanged, so the expectations in SKILL.md still apply to it.

usage: make_standin_seal.py <temple_crop_png_white_on_dark> <out.png> [--size 3000] [--thin-ring]
The temple input is any white-on-dark line drawing; it is thresholded to ink.
"""
import argparse
import math

from PIL import Image, ImageDraw, ImageFont

NAVY = (0, 26, 88)
WHITE = (255, 255, 255)
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SERIF_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"


def ring(d, c, r_out, w, fill=WHITE):
    d.ellipse([c[0] - r_out, c[1] - r_out, c[0] + r_out, c[1] + r_out], outline=fill, width=int(round(w)))


def arc_text(img, text, font, c, r, center_deg, outside_reading=True, tracking=0.0):
    """Set text on a circle. center_deg: 0 = top, 180 = bottom, clockwise.
    Top text: baseline on radius r, glyphs upright reading clockwise.
    Bottom text (outside_reading=False): reads left to right, glyph tops toward centre,
    r is the cap-top radius."""
    widths = [font.getlength(ch) for ch in text]
    track = tracking * font.size
    total = sum(widths) + track * (len(text) - 1)
    ang_total = math.degrees(total / r)
    a = center_deg - ang_total / 2 if outside_reading else center_deg + ang_total / 2
    asc = font.getbbox("H")[1]
    for ch, wch in zip(text, widths):
        step = math.degrees((wch + track) / r)
        mid = a + (math.degrees(wch / r) / 2) * (1 if outside_reading else -1)
        if ch != " ":
            gw = gh = font.size * 3
            g = Image.new("L", (gw, gh), 0)
            gd = ImageDraw.Draw(g)
            gd.text((gw // 2, gh // 2), ch, font=font, fill=255, anchor="ms" if outside_reading else "mt")
            rot = -mid if outside_reading else 180 - mid
            g = g.rotate(rot, resample=Image.BICUBIC, expand=True)
            th = math.radians(mid)
            px = c[0] + r * math.sin(th)
            py = c[1] - r * math.cos(th)
            img.paste(WHITE, (int(round(px - g.width / 2)), int(round(py - g.height / 2))), g)
        a += step if outside_reading else -step


def diamond(d, c, r, deg, size):
    th = math.radians(deg)
    x, y = c[0] + r * math.sin(th), c[1] - r * math.cos(th)
    d.polygon([(x, y - size), (x + size * 0.7, y), (x, y + size), (x - size * 0.7, y)], fill=WHITE)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("temple")
    ap.add_argument("out")
    ap.add_argument("--size", type=int, default=3000)
    ap.add_argument("--thin-ring", action="store_true")
    a = ap.parse_args()
    S = a.size
    k = S / 3000
    img = Image.new("RGB", (S, S), NAVY)
    d = ImageDraw.Draw(img)
    c = (S / 2, S / 2)
    R = 1440 * k
    ring(d, c, R, 48 * k)                         # thick outer ring
    band_out, band_in = R - 48 * k, 1190 * k
    ring(d, c, band_in, 9 * k)                    # thin ring (deliberately very thin)
    small = ImageFont.truetype(SERIF, int(78 * k))
    text = "A CHOSEN GENERATION • A ROYAL PRIESTHOOD • AN HOLY NATION • A PECULIAR PEOPLE"
    # outer band text set around the full circle, starting at the left diamond
    mid_r = (band_out + band_in) / 2
    cap = small.getbbox("H")[3] - small.getbbox("H")[1]
    arc_text(img, text, small, c, mid_r - cap / 2 - 6 * k, 0, tracking=0.08)
    for deg in (90, 180, 270):
        diamond(d, c, mid_r, deg, 22 * k)
    big = ImageFont.truetype(SERIF_BOLD, int(150 * k))
    arc_text(img, "PECULIAR PEOPLE", big, c, 990 * k, 0, tracking=0.04)
    est = ImageFont.truetype(SERIF, int(70 * k))
    arc_text(img, "EST. 2023", est, c, 1060 * k, 180, outside_reading=False, tracking=0.15)
    ci = (c[0] + 14 * k, c[1] + 6 * k)            # inner ring nudged off centre
    ring(d, ci, 900 * k, 30 * k)                  # heavier inner ring
    if a.thin_ring:
        ring(d, (c[0] - 6 * k, c[1]), 945 * k, 5 * k)  # thin ring, 6 px off centre
    t = Image.open(a.temple).convert("L")
    t = t.point(lambda v: 255 if v > 128 else 0)
    bb = t.getbbox()
    t = t.crop(bb)
    tw = int(1060 * k)
    th = int(t.height * tw / t.width)
    t = t.resize((tw, th), Image.LANCZOS)
    tx, ty = int(c[0] - tw / 2), int(c[1] - th / 2 + 40 * k)
    img.paste(WHITE, (tx, ty), t)
    loc = ImageFont.truetype(SERIF, int(54 * k))
    s = "UTAH, USA"
    spaced = " ".join(s)
    d.text((c[0], ty + th + 40 * k), spaced, font=loc, fill=WHITE, anchor="mt")
    img.save(a.out)


if __name__ == "__main__":
    main()
