"""Shared helpers for the design-audit scripts: loading, ink masks, distance maps,
connected components and unit conversion. Pillow + numpy only, so it runs on the
temple-product-generator venv (numpy 2.x, pillow 12.x) with nothing extra.
"""
import json
import math

import numpy as np
from PIL import Image

MM_PER_IN = 25.4
PT_PER_IN = 72.0
MAX_SIDE = 3200  # larger inputs are downscaled for speed; the scale is recorded


def load(path, ink=None, bg=None, max_side=MAX_SIDE):
    """Return (rgb uint8 array, ink bool mask, info dict).

    Ink detection, in order:
    1. Transparent PNG: alpha > 127 is ink (how the print files are delivered).
    2. Otherwise the background colour is the median of a 2 percent border, and a
       pixel is ink when it sits closer to the ink colour than to the background.
       The ink colour is --ink if given, else the colour farthest from the
       background among the brightest/darkest 1 percent of pixels.
    """
    im = Image.open(path)
    info = {"source": str(path), "source_size": list(im.size)}
    scale = 1.0
    if max(im.size) > max_side:
        scale = max_side / max(im.size)
        im = im.resize((round(im.width * scale), round(im.height * scale)), Image.LANCZOS)
    info["analysis_scale"] = scale
    info["size"] = list(im.size)
    has_alpha = im.mode in ("RGBA", "LA") or (im.mode == "P" and "transparency" in im.info)
    rgba = np.asarray(im.convert("RGBA")).astype(np.float32)
    rgb = rgba[..., :3]
    if has_alpha and (rgba[..., 3] < 128).mean() > 0.05 and ink is None and bg is None:
        mask = rgba[..., 3] > 127
        info["ink_mode"] = "alpha"
        return rgb.astype(np.uint8), mask, info
    h, w = rgb.shape[:2]
    b = max(2, int(0.02 * min(h, w)))
    border = np.concatenate([rgb[:b].reshape(-1, 3), rgb[-b:].reshape(-1, 3),
                             rgb[:, :b].reshape(-1, 3), rgb[:, -b:].reshape(-1, 3)])
    bgc = np.array(parse_color(bg), np.float32) if bg else np.median(border, axis=0)
    if ink:
        inkc = np.array(parse_color(ink), np.float32)
    else:
        d = np.linalg.norm(rgb - bgc, axis=2)
        far = d >= np.quantile(d, 0.99)
        inkc = np.median(rgb[far], axis=0)
    d_bg = np.linalg.norm(rgb - bgc, axis=2)
    d_ink = np.linalg.norm(rgb - inkc, axis=2)
    mask = d_ink < d_bg
    info.update(ink_mode="colour", background_rgb=[round(float(x)) for x in bgc],
                ink_rgb=[round(float(x)) for x in inkc])
    return rgb.astype(np.uint8), mask, info


def parse_color(s):
    s = s.strip().lstrip("#")
    return [int(s[i:i + 2], 16) for i in (0, 2, 4)]


def _shift_min(a, cross, outside=False):
    """One erosion step of a uint mask (as bool). cross=True uses the 4-neighbour
    cross, else the 3x3 square. Alternating the two gives an octagonal metric that
    stays within about 8 percent of true Euclidean distance at any stroke angle."""
    p = np.pad(a, 1, constant_values=outside)
    out = a.copy()
    out &= p[:-2, 1:-1] & p[2:, 1:-1] & p[1:-1, :-2] & p[1:-1, 2:]
    if not cross:
        out &= p[:-2, :-2] & p[:-2, 2:] & p[2:, :-2] & p[2:, 2:]
    return out


def erosion_depth(mask, limit=None):
    """Distance map by repeated erosion: depth 1 = removed by the first erosion.
    A stroke of width w pixels has a centre-line depth of about (w + 1) / 2, so
    width = 2 * depth - 1. Pixels still standing after `limit` steps get limit + 1."""
    depth = np.zeros(mask.shape, np.int32)
    cur = mask.copy()
    k = 0
    while cur.any():
        k += 1
        depth[cur] = k
        if limit and k > limit:
            break
        cur = _shift_min(cur, cross=(k % 2 == 1))
    return depth


def ridge_widths(mask, region=None, limit=None):
    """Stroke widths in pixels, sampled along each stroke's centre line (local maxima
    of the erosion depth). Returns (widths array, ridge bool mask)."""
    d = erosion_depth(mask, limit=limit)
    p = np.pad(d, 1)
    nb = np.max(np.stack([p[:-2, :-2], p[:-2, 1:-1], p[:-2, 2:], p[1:-1, :-2],
                          p[1:-1, 2:], p[2:, :-2], p[2:, 1:-1], p[2:, 2:]]), axis=0)
    ridge = (d > 0) & (d >= nb)
    if region is not None:
        ridge &= region
    if limit:
        ridge &= d <= limit
    return (2 * d[ridge] - 1).astype(np.float32), ridge


def dilate(mask, steps):
    """Grow ink by `steps` pixels (octagonal), used for the ink-spread simulation."""
    inv = ~mask
    for k in range(steps):
        inv = _shift_min(inv, cross=(k % 2 == 0), outside=True)  # beyond the canvas is background
    return ~inv


def components(mask):
    """Connected components (8-connected) by run-length union-find. Returns a list
    of dicts with area, bbox, centroid, and the pixel coordinates (ys, xs)."""
    h, w = mask.shape
    runs = []  # (row, x0, x1)
    row_runs = []
    for y in range(h):
        row = mask[y]
        if not row.any():
            row_runs.append((len(runs), len(runs)))
            continue
        dr = np.diff(np.concatenate([[0], row.view(np.int8), [0]]))
        starts = np.flatnonzero(dr == 1)
        ends = np.flatnonzero(dr == -1) - 1
        a = len(runs)
        runs.extend((y, int(s), int(e)) for s, e in zip(starts, ends))
        row_runs.append((a, len(runs)))
    parent = list(range(len(runs)))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    for y in range(1, h):
        a0, a1 = row_runs[y - 1]
        b0, b1 = row_runs[y]
        i, j = a0, b0
        while i < a1 and j < b1:
            _, s1, e1 = runs[i]
            _, s2, e2 = runs[j]
            if s1 <= e2 + 1 and s2 <= e1 + 1:
                ri, rj = find(i), find(j)
                if ri != rj:
                    parent[ri] = rj
            if e1 < e2:
                i += 1
            else:
                j += 1
    groups = {}
    for i in range(len(runs)):
        groups.setdefault(find(i), []).append(runs[i])
    out = []
    for rl in groups.values():
        ys = np.concatenate([np.full(e - s + 1, y) for y, s, e in rl])
        xs = np.concatenate([np.arange(s, e + 1) for y, s, e in rl])
        out.append({"area": int(ys.size), "ys": ys, "xs": xs,
                    "bbox": [int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max())],
                    "centroid": [float(xs.mean()), float(ys.mean())]})
    return out


def fit_circle(xs, ys):
    """Least-squares (Kasa) circle fit. Returns (cx, cy, r, rms residual)."""
    xs = np.asarray(xs, float)
    ys = np.asarray(ys, float)
    A = np.column_stack([xs, ys, np.ones_like(xs)])
    b = -(xs ** 2 + ys ** 2)
    (D, E, F), *_ = np.linalg.lstsq(A, b, rcond=None)
    cx, cy = -D / 2, -E / 2
    r = math.sqrt(max(cx * cx + cy * cy - F, 0))
    res = np.hypot(xs - cx, ys - cy) - r
    return float(cx), float(cy), float(r), float(np.sqrt(np.mean(res ** 2)))


class Units:
    """Pixel to physical conversion for one intended print width. `basis_px` is the
    pixel width that the print width refers to (the design's ink width by default,
    matching the house rule that print sizes are measured ink to ink)."""

    def __init__(self, print_width_in, basis_px):
        self.width_in = float(print_width_in)
        self.ppi = basis_px / self.width_in

    def conv(self, px):
        if px is None:
            return None
        inch = px / self.ppi
        return {"px": round(float(px), 2), "in": round(inch, 4),
                "mm": round(inch * MM_PER_IN, 3), "pt": round(inch * PT_PER_IN, 2)}


def stats(a):
    a = np.asarray(a, float)
    if a.size == 0:
        return None
    return {"n": int(a.size), "min": round(float(a.min()), 2),
            "p05": round(float(np.quantile(a, 0.05)), 2),
            "p10": round(float(np.quantile(a, 0.10)), 2),
            "median": round(float(np.median(a)), 2),
            "p90": round(float(np.quantile(a, 0.90)), 2),
            "max": round(float(a.max()), 2)}


def dump(obj, path):
    def default(o):
        if isinstance(o, (np.integer,)):
            return int(o)
        if isinstance(o, (np.floating,)):
            return float(o)
        if isinstance(o, np.ndarray):
            return o.tolist()
        raise TypeError(type(o))
    with open(path, "w") as f:
        json.dump(obj, f, indent=2, default=default)
