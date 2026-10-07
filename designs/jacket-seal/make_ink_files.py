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
