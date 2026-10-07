#!/usr/bin/env python3
"""Ring detection checks on the stand-in seals in fixtures/.

standin_seal.png: the expectations in SKILL.md (three rings, ring3 about 15.2 px
off the outer ring's centre, ring2 about 8.9 px wide).

standin_seal_thin_ring.png (make_standin_seal.py --thin-ring): the same seal plus
a 5 px ring 6 px off centre at r 940.5 to 945.5. Sampled from the outer ring's
centre it smears into two coverage peaks of about 0.42 with a trough between, the
failure seen on seal.png, where two 5 px rings 4.5 and 6.4 px off centre were
missed and every band and clearance number came out wrong.

usage: python3 tests/test_rings.py   (or pytest tests/test_rings.py)
"""
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "scripts"))

import common as C  # noqa: E402
import measure as M  # noqa: E402


def rings_of(name):
    mask = C.load(os.path.join(HERE, "fixtures", name))[1]
    ys, xs = np.nonzero(mask)
    rings = M.detect_rings(mask, [int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max())])
    cx, cy = rings[0]["center"]
    for g in rings:
        g["offset"] = float(np.hypot(g["center"][0] - cx, g["center"][1] - cy))
    return rings


def near(a, b, tol):
    return abs(a - b) <= tol


def test_standin_expectations():
    rings = rings_of("standin_seal.png")
    assert len(rings) == 3, [(g["r_inner"], g["r_outer"]) for g in rings]
    assert near(rings[1]["width_mean"], 8.9, 0.3), rings[1]["width_mean"]
    assert near(rings[2]["offset"], 15.2, 0.3), rings[2]["offset"]


def test_thin_offset_ring():
    rings = rings_of("standin_seal_thin_ring.png")
    assert len(rings) == 4, [(g["r_inner"], g["r_outer"]) for g in rings]
    thin = rings[2]
    assert near(thin["r_inner"], 940.5, 1) and near(thin["r_outer"], 945.5, 1), (thin["r_inner"], thin["r_outer"])
    assert near(thin["width_mean"], 5, 0.5), thin["width_mean"]
    assert near(thin["offset"], 6, 1), thin["offset"]
    # the rings that were already found must not move
    assert near(rings[1]["width_mean"], 8.9, 0.3), rings[1]["width_mean"]
    assert near(rings[3]["offset"], 15.2, 0.3), rings[3]["offset"]


if __name__ == "__main__":
    for t in (test_standin_expectations, test_thin_offset_ring):
        t()
        print("ok", t.__name__)
