"""Write the finished Peculiar People Seal files for Other designs/ from
out/seal-arvo.svg (run build_seal.py first): white and black ink, each as an SVG
source and a 300 ppi transparent print PNG. Every PNG pixel carries the ink
colour and alpha is fully ink or fully clear (BRAND.md section 8, PRINT-06)."""
import io
import os

import cairosvg
import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "out", "seal-arvo.svg")
OUT = os.path.join(HERE, "Peculiar People Seal")
PX = 3600  # 12 in at 300 ppi

os.makedirs(OUT, exist_ok=True)
src = open(SRC).read()
for name, hexv, level in [("white", "#FFFFFF", 255), ("black", "#000000", 0)]:
    svg = src.replace('fill="#FFFFFF"', f'fill="{hexv}"').replace('fill="#ffffff"', f'fill="{hexv}"')
    open(os.path.join(OUT, f"Peculiar People Seal {name}.svg"), "w").write(svg)
    buf = cairosvg.svg2png(bytestring=svg.encode(), output_width=PX, output_height=PX)
    a = np.asarray(Image.open(io.BytesIO(buf)).convert("RGBA"))[:, :, 3]
    alpha = np.where(a >= 128, 255, 0).astype(np.uint8)
    rgba = np.dstack([np.full_like(alpha, level)] * 3 + [alpha])
    Image.fromarray(rgba, "RGBA").save(os.path.join(OUT, f"Peculiar People Seal {name}.png"), dpi=(300, 300))
    print(name, "ink values", np.unique(rgba[:, :, :3]), "alpha values", np.unique(alpha))
    if name == "black":
        # Black on a white tile. The seal runs edge to edge, so add a margin equal to
        # the clear space inside the outer ring (149.87 to 135.24 mm radius, 173 px)
        # so crops and rounded thumbnails don't clip the outer ring.
        m_px = 173
        m = m_px * 25.4 / 300
        s, h = 304.8 + 2 * m, 152.4 + m
        head = svg[:svg.index(">") + 1]
        tile = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{s:.3f}mm" height="{s:.3f}mm" '
                f'viewBox="{-h:.4f} {-h:.4f} {s:.4f} {s:.4f}">'
                f'<rect x="{-h:.4f}" y="{-h:.4f}" width="{s:.4f}" height="{s:.4f}" fill="#FFFFFF"/>')
        open(os.path.join(OUT, "Peculiar People Seal black on white.svg"), "w").write(tile + svg[len(head):])
        flat = np.full((PX + 2 * m_px,) * 2, 255, np.uint8)
        flat[m_px:m_px + PX, m_px:m_px + PX][alpha == 255] = 0
        Image.fromarray(flat).convert("RGB").save(
            os.path.join(OUT, "Peculiar People Seal black on white.png"), dpi=(300, 300))
