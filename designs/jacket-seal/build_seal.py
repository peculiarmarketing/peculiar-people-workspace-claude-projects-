"""Build the jacket back seal as vectors, per the rebuild spec in
research/design-audit/audits/seal_audit/REPORT.md.

Rings, type and diamonds are true geometry: every ring is a filled annulus on
one shared centre, and every letter is the font's own outline placed on its arc
(type is expanded to outlines, no live text). Sizes are fractions of D, the
outer diameter of the outer ring, so the same script builds any print size.

    python3 build_seal.py --font zilla --width-in 12 --out out/

Writes seal-<font>.svg (print file, white on transparent), seal-<font>-navy.svg
(preview on #001A58) and PNG renders of both. The temple goes in as the traced
SVG from trace/Salt Lake E white.svg when it exists, otherwise as the raster
temple-e-white.png (preview only: a raster is not a print file, PRINT-10).
"""
import argparse
import base64
import io
import math
import os

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen
from fontTools.ttLib import TTFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = {
    "zilla": os.path.join(HERE, "fonts", "ZillaSlab-Bold.ttf"),
    "montserrat": os.path.join(HERE, "fonts", "Montserrat-Bold-static.ttf"),
}
NAVY = "#001A58"

# ---- geometry, fractions of D (REPORT.md rebuild spec) --------------------
HEAVY = 0.0083          # outer ring and inner heavy ring
THIN = 0.0042           # both thin rings (DTG margin; floor 0.0028)
MOTTO_BAND = 0.0480     # outer ring to thin ring, edge to edge
TITLE_ZONE = 0.0702     # thin ring to inner thin ring, edge to edge
PAIR_GAP = 0.0078       # inner thin ring to inner heavy ring
CAP_SMALL = 0.0181      # motto, EST. 2023, UTAH, USA
CAP_TITLE = 0.0306      # PECULIAR PEOPLE
DIAMOND = 0.0232        # tip to tip, all three

R1o = 0.5
R1i = R1o - HEAVY
R2o = R1i - MOTTO_BAND
R2i = R2o - THIN
R3o = R2i - TITLE_ZONE
R3i = R3o - THIN
R4o = R3i - PAIR_GAP
R4i = R4o - HEAVY
R_MOTTO = (R1i + R2o) / 2
R_TITLE = (R2i + R3o) / 2

# Temple E placement, carried over from seal.png and scaled with the field.
# In seal.png (2048 px) the temple layer was 935 px tall with its top at
# y 452, centred on x 1024, and the inner heavy ring's inner edge sat at
# 626.6 px from the ring centre (1021.6, 1023.1); D was 1766.2 px.
OLD_D = 1766.2
OLD_CENTRE = (1021.6, 1023.1)
OLD_FIELD_R = 626.6
ART_TOP, ART_H, ART_CX = 452, 935, 1024
CAPTION_CENTRE_DY = 1448.5 - 1023.1      # old caption cap centre below ring centre
CROP_ORIGIN = (246, 39)                  # temple-e-white.png = temple-e.png cropped here
FULL_SRC = 2048


def ring(cx, cy, ro, ri):
    """Filled annulus: two circles, even-odd."""
    def circ(r):
        return (f"M{cx - r:.4f},{cy:.4f}a{r:.4f},{r:.4f} 0 1,0 {2 * r:.4f},0"
                f"a{r:.4f},{r:.4f} 0 1,0 {-2 * r:.4f},0Z")
    return f'<path fill-rule="evenodd" d="{circ(ro)}{circ(ri)}"/>'


class Face:
    def __init__(self, path):
        self.f = TTFont(path)
        self.gs = self.f.getGlyphSet()
        self.cmap = self.f.getBestCmap()
        self.upm = self.f["head"].unitsPerEm
        self.cap = self.f["OS/2"].sCapHeight
        self.hmtx = self.f["hmtx"]

    def glyph(self, ch):
        name = self.cmap[ord(ch)]
        if ch.isdigit() and name + ".pnum_lnum" in self.gs:
            name = name + ".pnum_lnum"   # lining figures beside capitals (Zilla defaults to old-style)
        pen = SVGPathPen(self.gs)
        self.gs[name].draw(pen)
        bp = BoundsPen(self.gs)
        self.gs[name].draw(bp)
        return name, pen.getCommands(), self.hmtx[name][0], bp.bounds


def set_arc(face, text, cap_frac, r_frac, D, track, mid_deg, bottom=False):
    """Centre-aligned text on a circle. Each glyph's cap-height centre sits on
    radius r; advance is measured along that centre line. Top text reads
    clockwise with tops outward; bottom text reads left to right with tops
    toward the centre. `track` is in 1/1000 em. Returns (svg, span_deg)."""
    s = cap_frac * D / face.cap                      # font units -> mm
    r = r_frac * D
    adv = []
    for i, ch in enumerate(text):
        _, _, aw, _ = face.glyph(ch)
        a = aw * s + (track / 1000.0 * face.upm * s if i < len(text) - 1 else 0)
        adv.append(a)
    total = sum(adv)
    span = math.degrees(total / r)
    out = []
    pos = -total / 2
    for ch, a in zip(text, adv):
        _, d, aw, _ = face.glyph(ch)
        centre = pos + aw * s / 2
        pos += a
        if ch == " " or not d:
            continue
        ang = math.degrees(centre / r)
        if not bottom:
            th = mid_deg + ang
            tf = (f"rotate({th:.4f}) translate(0,{-r:.4f}) scale({s:.6f},{-s:.6f}) "
                  f"translate({-aw / 2:.2f},{-face.cap / 2:.2f})")
        else:
            th = mid_deg - ang                     # left to right = decreasing angle
            tf = (f"rotate({th - 180:.4f}) translate(0,{r:.4f}) scale({s:.6f},{-s:.6f}) "
                  f"translate({-aw / 2:.2f},{-face.cap / 2:.2f})")
        out.append(f'<path transform="{tf}" d="{d}"/>')
    return "\n".join(out), span


def set_line(face, text, cap_frac, D, track, cy):
    """Straight centred line; cap-height centre on cy (relative to seal centre).
    Centred on the ink bounds, not the advance box (COMP-07)."""
    s = cap_frac * D / face.cap
    x = 0.0
    glyphs = []
    xmin, xmax = None, None
    for i, ch in enumerate(text):
        _, d, aw, b = face.glyph(ch)
        if d and b:
            lo, hi = x + b[0], x + b[2]
            xmin = lo if xmin is None else min(xmin, lo)
            xmax = hi if xmax is None else max(xmax, hi)
            glyphs.append((x, d))
        x += aw + (track / 1000.0 * face.upm if i < len(text) - 1 else 0)
    off = (xmin + xmax) / 2
    out = []
    for gx, d in glyphs:
        out.append(f'<path transform="translate({-off * s + gx * s:.4f},{cy:.4f}) '
                   f'scale({s:.6f},{-s:.6f}) translate(0,{-face.cap / 2:.2f})" d="{d}"/>')
    return "\n".join(out)


def diamond(deg, r, size):
    h = size / 2
    return (f'<path transform="rotate({deg:.4f}) translate(0,{-r:.4f})" '
            f'd="M0,{-h:.4f}L{h:.4f},0L0,{h:.4f}L{-h:.4f},0Z"/>')


def temple(D, field_r_new):
    """Temple layer, scaled with the field. Returns an SVG fragment in seal
    coordinates (origin at the seal centre)."""
    k = field_r_new / OLD_FIELD_R                      # old px -> mm, scaled with the field
    # temple layer box in old px, relative to the old ring centre
    from PIL import Image
    png = os.path.join(HERE, "temple-e-white.png")
    w, h = Image.open(png).size
    scale_px = ART_H / h
    bw, bh = w * scale_px, ART_H
    x0 = (ART_CX - bw / 2) - OLD_CENTRE[0]
    y0 = ART_TOP - OLD_CENTRE[1]
    # Traced vector (temple-svg-tracer, white variant) of the full 2048 px
    # temple-e.png; temple-e-white.png is that image cropped to its ink box.
    svg_trace = os.path.join(HERE, "trace", "Salt Lake E white.svg")
    if os.path.exists(svg_trace):
        body = open(svg_trace).read()
        vb = body.split('viewBox="')[1].split('"')[0]
        inner = body[body.index(">", body.index("<svg")) + 1: body.rindex("</svg>")]
        fx = x0 - CROP_ORIGIN[0] * scale_px
        fy = y0 - CROP_ORIGIN[1] * scale_px
        fw = FULL_SRC * scale_px
        return (f'<svg x="{fx * k:.4f}" y="{fy * k:.4f}" width="{fw * k:.4f}" '
                f'height="{fw * k:.4f}" viewBox="{vb}">{inner}</svg>'), "vector"
    b64 = base64.b64encode(open(png, "rb").read()).decode()
    return (f'<image x="{x0 * k:.4f}" y="{y0 * k:.4f}" width="{bw * k:.4f}" '
            f'height="{bh * k:.4f}" href="data:image/png;base64,{b64}"/>'), "raster"


def build(font_key, width_in, out_dir, motto_track, title_track, small_track, motto_span=None):
    face = Face(FONTS[font_key])
    D = width_in * 25.4
    c = D / 2
    parts = []
    for ro, ri in [(R1o, R1i), (R2o, R2i), (R3o, R3i), (R4o, R4i)]:
        parts.append(ring(0, 0, ro * D, ri * D))
    motto = "A CHOSEN GENERATION • A ROYAL PRIESTHOOD • AN HOLY NATION • A PECULIAR PEOPLE"
    if motto_span:
        # tracking that makes the motto cover motto_span degrees (span is linear in tracking)
        _, s0 = set_arc(face, motto, CAP_SMALL, R_MOTTO, D, 0, 0)
        _, s1 = set_arc(face, motto, CAP_SMALL, R_MOTTO, D, 1000, 0)
        motto_track = round((motto_span - s0) / (s1 - s0) * 1000)
    m_svg, m_span = set_arc(face, motto, CAP_SMALL, R_MOTTO, D, motto_track, 0)
    if small_track is None:
        small_track = motto_track      # one tracking value for all small text (TEST-04)
    t_svg, t_span = set_arc(face, "PECULIAR PEOPLE", CAP_TITLE, R_TITLE, D, title_track, 0)
    e_svg, e_span = set_arc(face, "EST. 2023", CAP_SMALL, R_TITLE, D, small_track, 180, bottom=True)
    parts += [m_svg, t_svg, e_svg]
    parts.append(diamond(90, R_TITLE * D, DIAMOND * D))
    parts.append(diamond(270, R_TITLE * D, DIAMOND * D))
    parts.append(diamond(180, R_MOTTO * D, DIAMOND * D))
    k = (R4i / (OLD_FIELD_R / OLD_D))
    cap_cy = CAPTION_CENTRE_DY / OLD_D * k * D
    parts.append(set_line(face, "UTAH, USA", CAP_SMALL, D, small_track, cap_cy))
    art, art_kind = temple(D, R4i * D)

    def doc(bg):
        rect = f'<rect x="{-c}" y="{-c}" width="{D}" height="{D}" fill="{bg}"/>' if bg else ""
        return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{D:.3f}mm" height="{D:.3f}mm" '
                f'viewBox="{-c:.4f} {-c:.4f} {D:.4f} {D:.4f}">{rect}'
                f'<g fill="#FFFFFF">{"".join(parts)}</g>{art}</svg>')

    os.makedirs(out_dir, exist_ok=True)
    base = os.path.join(out_dir, f"seal-{font_key}")
    open(base + ".svg", "w").write(doc(None))
    open(base + "-navy.svg", "w").write(doc(NAVY))
    import cairosvg
    px = 2048
    cairosvg.svg2png(url=base + "-navy.svg", write_to=base + "-navy.png", output_width=px, output_height=px)
    cairosvg.svg2png(url=base + ".svg", write_to=base + ".png", output_width=px, output_height=px)
    print(f"{font_key}: D {D:.1f} mm, motto span {m_span:.1f} deg (track {motto_track}), "
          f"title span {t_span:.1f} deg (track {title_track}), EST span {e_span:.1f} deg (track {small_track}), "
          f"temple {art_kind}")
    print(f"  radii (frac D): R1 {R1o:.4f}-{R1i:.4f}  R2 {R2o:.4f}-{R2i:.4f}  "
          f"R3 {R3o:.4f}-{R3i:.4f}  R4 {R4o:.4f}-{R4i:.4f}  motto line {R_MOTTO:.4f}  title line {R_TITLE:.4f}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--font", choices=sorted(FONTS), default="zilla")
    ap.add_argument("--width-in", type=float, default=12.0)
    ap.add_argument("--out", default=os.path.join(HERE, "out"))
    ap.add_argument("--motto-track", type=float, default=200)
    ap.add_argument("--title-track", type=float, default=50)
    ap.add_argument("--small-track", type=float, default=None,
                    help="tracking for EST. 2023 and UTAH, USA; default matches the motto")
    ap.add_argument("--motto-span", type=float, default=290,
                    help="degrees the motto covers, centred on 12 o'clock; 0 uses --motto-track")
    a = ap.parse_args()
    build(a.font, a.width_in, a.out, a.motto_track, a.title_track, a.small_track, a.motto_span or None)
