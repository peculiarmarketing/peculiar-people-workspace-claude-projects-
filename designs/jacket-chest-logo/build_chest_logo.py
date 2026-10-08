"""Build the A2 chest logo (framed stacked lockup) as vectors.

PECULIAR and PEOPLE are traced from the original logo PNG, not set in a font:
the PECULIAR letters were drawn by an image model and exist in no font file, so
the logo itself is the only source that keeps them identical. PEOPLE is traced
too so both words keep the logo's exact shapes and spacing. EST. 2023 is new
text and is set in Oswald, the face PEOPLE matches (97 percent pixel overlap).

Layout follows the Higgsfield draft higgsfield/A2-stacked-badge.png: a frame
around PECULIAR, a rule, PEOPLE, a rule, EST. 2023. Both words are scaled to the
same width without distortion. Units are thousandths of an inch.

    python3 build_chest_logo.py --width-in 3.5

Writes out/chest-logo-a2-{white,black}.svg, a white-ink print PNG at 300 dpi,
navy and black previews, and proof-letterforms.png (traced words over the
original logo) so the match can be checked by eye.
"""
import argparse
import os

import cairosvg
import numpy as np
import potrace
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
LOGO = os.path.join(HERE, "source", "Peculiar_People_Logo_-_Square_-_Black.png")
OSWALD = os.path.join(HERE, "fonts", "Oswald[wght].ttf")
NAVY = "#001A58"

# Word regions in the 1000 px source logo (PECULIAR is inside the box strokes).
PECULIAR_BOX = (36, 420, 594, 582)
PEOPLE_BOX = (615, 395, 995, 605)
UPSAMPLE = 8            # trace at 8x so curves come out smooth

# ---- layout, thousandths of an inch at 3.5 in frame width ----------------
FRAME_W = 3500
FRAME_STROKE = 63       # 1.6 mm
SIDE = 200              # frame outer edge to the words
RULE = 48               # 1.2 mm
GAP = 180               # every gap between frame, words and rules
EST_CAP = 250           # EST. 2023 cap height
EST_WIDTH = 0.60        # EST. 2023 width as a fraction of the word width
EST_WGHT = 400


def ink_gray():
    im = Image.open(LOGO).convert("RGBA")
    bg = Image.new("RGBA", im.size, "white")
    return Image.alpha_composite(bg, im).convert("L")


def trace_word(gray, box):
    """Trace one word. Returns (svg path d in source px, bbox in source px)."""
    crop = gray.crop(box)
    big = crop.resize((crop.width * UPSAMPLE, crop.height * UPSAMPLE), Image.LANCZOS)
    mask = np.array(big) < 128
    ys, xs = np.where(mask)
    bbox = (xs.min() / UPSAMPLE, ys.min() / UPSAMPLE,
            (xs.max() + 1) / UPSAMPLE, (ys.max() + 1) / UPSAMPLE)
    # potracer treats falsy pixels as ink, so pass the inverse.
    plist = potrace.Bitmap(~mask).trace(turdsize=4, alphamax=1.0,
                                       opticurve=True, opttolerance=0.2)
    s = 1.0 / UPSAMPLE
    f = lambda p: "%.3f %.3f" % (p.x * s, p.y * s)
    d = []
    for curve in plist:
        d.append("M" + f(curve.start_point))
        for seg in curve.segments:
            if seg.is_corner:
                d.append("L" + f(seg.c) + "L" + f(seg.end_point))
            else:
                d.append("C" + f(seg.c1) + " " + f(seg.c2) + " " + f(seg.end_point))
        d.append("Z")
    return "".join(d), bbox


def placed(d, bbox, x, y, width):
    """Wrap a traced path so its ink bbox lands at (x, y) with the given width."""
    k = width / (bbox[2] - bbox[0])
    return ('<path fill-rule="evenodd" transform="translate(%.2f %.2f) scale(%.5f) '
            'translate(%.4f %.4f)" d="%s"/>' % (x, y, k, -bbox[0], -bbox[1], d)), k


def oswald_line(text, cap, width, cx, top):
    """EST. 2023 as Oswald outlines, tracked out to the given width."""
    font = instantiateVariableFont(TTFont(OSWALD), {"wght": EST_WGHT})
    gs, cmap = font.getGlyphSet(), font.getBestCmap()
    bp = BoundsPen(gs)
    gs[cmap[ord("E")]].draw(bp)
    k = cap / (bp.bounds[3] - bp.bounds[1])
    names = [cmap[ord(c)] for c in text]
    advance = sum(gs[n].width for n in names) * k
    gaps = len(text) - 1
    track = (width - advance) / gaps
    # Ink width differs from advance width; centre on the measured ink below.
    out, x = [], 0.0
    for n in names:
        pen = SVGPathPen(gs)
        gs[n].draw(TransformPen(pen, (k, 0, 0, -k, x, cap)))
        if pen.getCommands():
            out.append(pen.getCommands())
        x += gs[n].width * k + track
    total = x - track
    return '<path transform="translate(%.2f %.2f)" d="%s"/>' % (cx - total / 2, top, " ".join(out))


def build(width_in):
    gray = ink_gray()
    pec_d, pec_bb = trace_word(gray, PECULIAR_BOX)
    peo_d, peo_bb = trace_word(gray, PEOPLE_BOX)

    W = FRAME_W - 2 * SIDE
    pec_h = W * (pec_bb[3] - pec_bb[1]) / (pec_bb[2] - pec_bb[0])
    peo_h = W * (peo_bb[3] - peo_bb[1]) / (peo_bb[2] - peo_bb[0])
    y = FRAME_STROKE + GAP
    pec_y = y; y += pec_h + GAP
    rule1 = y; y += RULE + GAP
    peo_y = y; y += peo_h + GAP
    rule2 = y; y += RULE + GAP
    est_y = y; y += EST_CAP + GAP
    H = y + FRAME_STROKE

    pec, k_pec = placed(pec_d, pec_bb, SIDE, pec_y, W)
    peo, _ = placed(peo_d, peo_bb, SIDE, peo_y, W)
    est = oswald_line("EST. 2023", EST_CAP, W * EST_WIDTH, FRAME_W / 2, est_y)
    fs = FRAME_STROKE
    frame = ('<path fill-rule="evenodd" d="M0 0H%d V%.2f H0Z M%d %d V%.2f H%d V%dZ"/>'
             % (FRAME_W, H, fs, fs, H - fs, FRAME_W - fs, fs))
    rules = "".join('<rect x="%d" y="%.2f" width="%d" height="%d"/>' % (SIDE, r, W, RULE)
                    for r in (rule1, rule2))
    body = frame + rules + pec + peo + est

    # Thinnest stroke: the I in PECULIAR, measured in the source and scaled.
    m = np.array(gray.crop(PECULIAR_BOX)) < 128
    cols = m.any(0)
    runs, s = [], None
    for x in range(len(cols)):
        if cols[x] and s is None:
            s = x
        if not cols[x] and s is not None:
            runs.append(x - s); s = None
    i_px = sorted(runs)[0]
    scale = width_in / 3.5
    stats = {
        "size_in": (round(width_in, 2), round(H / 1000 * scale, 2)),
        "peculiar_stroke_mm": round(i_px * k_pec * scale * 0.0254, 2),
        "frame_mm": round(fs * scale * 0.0254, 2),
        "rule_mm": round(RULE * scale * 0.0254, 2),
        "est_cap_in": round(EST_CAP / 1000 * scale, 3),
    }

    def svg(fill, bg=None):
        pad = 300 if bg else 0
        vw, vh = FRAME_W + 2 * pad, H + 2 * pad
        rect = ('<rect x="%d" y="%d" width="%.2f" height="%.2f" fill="%s"/>'
                % (-pad, -pad, vw, vh, bg)) if bg else ""
        return ('<svg xmlns="http://www.w3.org/2000/svg" width="%.3fin" height="%.3fin" '
                'viewBox="%d %d %.2f %.2f">%s<g fill="%s">%s</g></svg>'
                % (vw / 1000 * scale, vh / 1000 * scale, -pad, -pad, vw, vh, rect, fill, body))

    os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
    o = lambda n: os.path.join(HERE, "out", n)
    files = {"chest-logo-a2-white.svg": svg("#FFFFFF"), "chest-logo-a2-black.svg": svg("#000000"),
             "preview-navy.svg": svg("#FFFFFF", NAVY), "preview-black.svg": svg("#FFFFFF", "#111111")}
    for n, t in files.items():
        with open(o(n), "w") as fh:
            fh.write(t)
    cairosvg.svg2png(bytestring=files["preview-navy.svg"].encode(), write_to=o("preview-navy.png"), dpi=150)
    cairosvg.svg2png(bytestring=files["preview-black.svg"].encode(), write_to=o("preview-black.png"), dpi=150)

    # Print PNG: 300 dpi, white ink, every pixel's colour set to white (BRAND.md s8).
    cairosvg.svg2png(bytestring=files["chest-logo-a2-white.svg"].encode(),
                     write_to=o("tmp.png"), dpi=300)
    a = Image.open(o("tmp.png")).getchannel("A")
    ink = Image.new("RGBA", a.size, (255, 255, 255, 0)); ink.putalpha(a)
    ink.save(o("chest-logo-a2-white-%gin-300dpi.png" % width_in), dpi=(300, 300))
    os.remove(o("tmp.png"))

    proof(gray, pec_d, pec_bb, peo_d, peo_bb, o("proof-letterforms.png"))
    return stats


def proof(gray, pec_d, pec_bb, peo_d, peo_bb, out):
    """Traced words in red over the original logo at 4x, plus overlap scores."""
    S = 4
    def render(d, box):
        w, h = box[2] - box[0], box[3] - box[1]
        t = ('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="%d %d %d %d">'
             '<path fill-rule="evenodd" d="%s"/></svg>' % (w * S, h * S, 0, 0, w, h, d))
        im = Image.open(__import__("io").BytesIO(cairosvg.svg2png(bytestring=t.encode())))
        return np.array(im.getchannel("A")) > 128
    rows = []
    for d, box in ((pec_d, PECULIAR_BOX), (peo_d, PEOPLE_BOX)):
        traced = render(d, box)
        orig = np.array(gray.crop(box).resize((traced.shape[1], traced.shape[0]), Image.LANCZOS)) < 128
        iou = (traced & orig).sum() / (traced | orig).sum()
        print("trace overlap %.3f" % iou)
        rgb = np.full(orig.shape + (3,), 255, np.uint8)
        rgb[orig] = (0, 0, 0)
        rgb[traced & ~orig] = (230, 0, 0)
        rgb[orig & ~traced] = (0, 140, 255)
        rows.append(Image.fromarray(rgb))
    W = max(r.width for r in rows)
    sheet = Image.new("RGB", (W, sum(r.height for r in rows) + 20), "white")
    sheet.paste(rows[0], (0, 0)); sheet.paste(rows[1], (0, rows[0].height + 20))
    sheet.save(out)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--width-in", type=float, default=3.5)
    print(build(ap.parse_args().width_in))
