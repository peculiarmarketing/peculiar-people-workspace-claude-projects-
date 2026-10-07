"""Thicken temple E so every line clears the DTG floor inside the 12 in seal.

Two steps on the source drawing, upscaled 4x:
1. Grow every line by GROW_MM per side (keeps the heavy / medium / light
   hierarchy, every weight moves up by the same amount).
2. Enforce a minimum width of MIN_MM along each line's centre line, for the
   faint construction strokes that started too thin for step 1 to rescue.
Sizes are in mm at the seal's 12 in print size. Writes a black-on-white PNG for
the temple-svg-tracer skill.
"""
import numpy as np
from PIL import Image
from scipy import ndimage as nd
from skimage.morphology import skeletonize

Image.MAX_IMAGE_PIXELS = None
GROW_MM = 0.30
MIN_MM = 0.95
UP = 4
MM_PER_SRC_PX = 0.08131708400265811     # temple E source px at the 12 in seal

src = Image.open("temple-e.png").convert("L")
big = src.resize((src.width * UP, src.height * UP), Image.LANCZOS)
ink = np.asarray(big) < 128
mmpx = MM_PER_SRC_PX / UP
dist_out = nd.distance_transform_edt(~ink)
grown = dist_out <= GROW_MM / mmpx
skel = skeletonize(ink)
floor = nd.distance_transform_edt(~skel) <= (MIN_MM / 2) / mmpx
out = grown | floor
Image.fromarray(np.where(out, 0, 255).astype(np.uint8)).save("dtg/Salt Lake E DTG.png")
holes = lambda m: nd.label(~m)[1]
print(f"ink {ink.mean() * 100:.1f}% -> {out.mean() * 100:.1f}%, "
      f"enclosed white regions {holes(ink)} -> {holes(out)}")
