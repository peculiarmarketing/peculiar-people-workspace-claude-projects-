"""Export the finished seal and chest logo to Other designs/ at 600 ppi, with
short names that lead with what differs (the folder already says which design).

Renders every PNG from its SVG, so the two formats match. Seal PNGs keep the
BRAND.md section 8 rule (alpha fully ink or fully clear); the chest logo keeps
its anti-aliased alpha, as build_chest_logo.py does.

Needs resvg-py, Pillow and numpy:  python export_other_designs.py
"""
import io
import os
import re

import numpy as np
import resvg_py
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
DEST = os.path.join(HERE, "..", "..", "Other designs")
SEAL = os.path.join(HERE, "jacket-seal", "Peculiar People Seal")
CHEST = os.path.join(HERE, "jacket-chest-logo", "final")
PPI = 600


def render(svg):
    png = resvg_py.svg_to_bytes(svg_string=svg, dpi=PPI)
    return np.asarray(Image.open(io.BytesIO(bytes(png))).convert("RGBA"))


def save(arr, mode, path):
    Image.fromarray(arr, mode).save(path, dpi=(PPI, PPI), optimize=True)
    print(os.path.relpath(path, DEST), arr.shape[1], "x", arr.shape[0])


def seal_variants():
    """(new name, svg text) for every seal version, thick and thin."""
    out = []
    for weight, suffix in (("", ""), (" thin", " (thin)")):
        on_white = open(os.path.join(SEAL, f"Peculiar People Seal black on white{suffix}.svg")).read()
        # Plain ink versions: the on-white file minus its white disc, sized to the ring.
        bare = re.sub(r'<circle[^>]*fill="#FFFFFF"/>', "", on_white, count=1)
        bare = re.sub(r'width="[\d.]+mm" height="[\d.]+mm" viewBox="[^"]*"',
                      'width="304.800mm" height="304.800mm" viewBox="-152.4000 -152.4000 304.8000 304.8000"',
                      bare, count=1)
        out.append((f"black{weight}", bare))
        # Every fill, not just the outer group: the temple carries its own fills.
        out.append((f"white{weight}", bare.replace('fill="#000000"', 'fill="#FFFFFF"')))
        out.append((f"black on white{weight}", on_white))
    return out


def export_seal():
    d = os.path.join(DEST, "jacket-seal")
    for f in os.listdir(d):
        if f.startswith("Peculiar People Seal"):
            os.remove(os.path.join(d, f))
    for name, svg in seal_variants():
        open(os.path.join(d, name + ".svg"), "w").write(svg)
        a = render(svg)
        alpha = np.where(a[:, :, 3] >= 128, 255, 0).astype(np.uint8)
        if "on white" in name:
            # White disc with black ink: colour from luminance, hard edges.
            ink = (a[:, :, :3].mean(axis=2) < 128) & (alpha == 255)
            level = np.where(ink, 0, 255).astype(np.uint8)
        else:
            level = np.full_like(alpha, 255 if name.startswith("white") else 0)
        save(np.dstack([level] * 3 + [alpha]), "RGBA", os.path.join(d, name + ".png"))


def export_chest():
    d = os.path.join(DEST, "jacket-chest-logo")
    for f in os.listdir(d):
        if f.startswith("chest-logo-a2-"):
            os.remove(os.path.join(d, f))
    for v in ("black", "white", "black-on-white", "white-on-black"):
        svg = open(os.path.join(CHEST, f"chest-logo-a2-{v}.svg")).read()
        name = v.replace("-", " ")
        open(os.path.join(d, name + ".svg"), "w").write(svg)
        a = render(svg)
        if "on" in v:
            save(np.ascontiguousarray(a[:, :, :3]), "RGB", os.path.join(d, name + ".png"))
        else:
            rgb = 255 if v == "white" else 0
            save(np.dstack([np.full_like(a[:, :, 3], rgb)] * 3 + [a[:, :, 3]]), "RGBA",
                 os.path.join(d, name + ".png"))


def export_traced(src_dir, dest_dir, names, scale):
    """Logos that only existed as PNGs, traced to SVG (temple-svg-tracer,
    --upscale 3 --threshold 128 --no-label-group, sources in <design>/source/).
    The SVGs are sized in source pixels, so PNGs render at `scale` times that.
    Anti-aliased alpha, like the originals."""
    for src_name, new_name in names:
        svg = open(os.path.join(src_dir, src_name + ".svg")).read()
        open(os.path.join(dest_dir, new_name + ".svg"), "w").write(svg)
        w, h = (float(v) for v in re.search(r'width="([\d.]+)" height="([\d.]+)"', svg).groups())
        png = resvg_py.svg_to_bytes(svg_string=svg, width=round(w * scale), height=round(h * scale))
        a = np.asarray(Image.open(io.BytesIO(bytes(png))).convert("RGBA"))[:, :, 3]
        level = 255 if new_name.endswith("white") else 0
        save(np.dstack([np.full_like(a, level)] * 3 + [a]), "RGBA", os.path.join(dest_dir, new_name + ".png"))


def export_be_peculiar():
    d = os.path.join(DEST, "Be Peculiar")
    src = os.path.join(HERE, "be-peculiar", "trace")
    pairs = [(f"{k} {c}", f"{k} {c}") for k in ("english", "spanish") for c in ("black", "white")]
    export_traced(src, d, pairs, 4)  # 1920 x 600 source, 7680 x 2400 out
    export_traced(src, os.path.join(d, "alts"), [("alt 1 black", "alt 1 black"), ("alt 1 white", "alt 1 white")], 4)
    old = os.path.join(d, "alts", "alt 1.png")
    if os.path.exists(old):
        os.remove(old)


def export_logo():
    d = os.path.join(DEST, "Logo")
    for f in os.listdir(d):
        if f.startswith("Peculiar People Logo"):
            os.remove(os.path.join(d, f))
    export_traced(os.path.join(HERE, "logo", "trace"), d, [("black", "black"), ("white", "white")], 2)  # 3125 x 625 at 300 dpi -> 600 dpi


export_seal()
export_chest()
export_be_peculiar()
export_logo()
