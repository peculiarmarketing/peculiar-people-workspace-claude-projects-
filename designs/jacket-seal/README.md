# Jacket back seal

Vector rebuild of the seal audited in
`research/design-audit/audits/seal_audit/REPORT.md`, built to its rebuild spec
at 12 in (D, the outer ring's outer diameter, = 304.8 mm).

    python3 build_seal.py --font zilla        # or montserrat, arvo, rokkitt, josefin, raleway
    python3 build_seal.py --font zilla --width-in 10

Needs `fonttools` and `cairosvg` (pip). Writes to `out/`:

| File | What it is |
|---|---|
| `seal-<font>.svg` | print file: white on transparent, 304.8 mm square, everything vector |
| `seal-<font>-navy.svg` / `.png` | preview on navy `#001A58` |
| `seal-<font>.png` | white on transparent render, 2048 px |

## How it is built

- Rings are filled annuli on one centre (strokes already expanded).
- Every letter is the font's own outline placed on its arc, centre-aligned to the
  band's centre line; no live text. Bottom line reads left to right, upright.
- Motto tracking is solved so the motto covers 290 degrees, as in the draft; EST.
  2023 and UTAH, USA use the same tracking (one spacing logic). PECULIAR PEOPLE is
  at 50.
- Temple E is the approved art, traced with the temple-svg-tracer skill
  (`trace/Salt Lake E white.svg`; black twin alongside) and scaled 1.6 percent with
  the field. Its line weights are untouched.

## Fonts (all SIL OFL, licences in `fonts/`)

The small text needs a face whose thinnest stroke is at least about 0.155 of its
cap height to clear the DTG floor at 12 in. Measured ratios (3rd percentile of
stroke width over cap height), and the six that are built:

| Key | Face | Ratio | Character |
|---|---|---|---|
| `josefin` | Josefin Sans Bold (wght 700 instance) | 0.166 | art deco geometric sans |
| `raleway` | Raleway ExtraBold (wght 800 instance) | 0.172 | elegant sans |
| `montserrat` | Montserrat Bold (wght 700 instance) | 0.174 | the storefront heading face |
| `zilla` | Zilla Slab Bold | 0.169 | slab serif |
| `arvo` | Arvo Bold | 0.181 | geometric slab, vintage |
| `rokkitt` | Rokkitt ExtraBold (wght 800 instance) | 0.182 | narrower slab, badge feel |

Too thin for this size: Roboto Slab ExtraBold 0.138, Bree Serif 0.129, Crete Round
0.115, Josefin Slab 0.114, Domine Bold 0.091, Cinzel Black 0.071, Marcellus 0.060,
Belleza 0.057, Old Standard Bold 0.045, Source Serif ExtraBold 0.043, Cormorant SC
Bold 0.035, Playfair Display SC Black 0.034. Poppins Bold passes (0.188) but is
close to Montserrat, so it is not built.

Figures always use each face's lining set (its `lnum` feature): Zilla, Rokkitt
and Raleway default to old-style figures.

`out/font-comparison.png` shows all six side by side.

## Audit of the rebuild at 12 in (`research/design-audit/audits/seal_rebuild_<font>/`, all six faces)

- 4 rings found, centre offsets under 0.03 px; all ring widths pass every method
  (thin rings 1.22 mm, heavy 2.34 to 2.44 mm).
- Type hairlines 0.86 mm (Zilla) to 0.97 mm (the others): pass the DTG floor
  (0.71), WARN under the 1.06 mm production margin.
- Band text centred (outer to inner clearance ratio 1.00 to 1.04); arcs on the axis
  within 0.1 degrees; diamonds at 90.0 / 180.0 / 270.0 on their band centre lines;
  caption offset 0.0.
- Still FAILS: the temple's lightest lines (0.24 mm) on every method. Brand call,
  see REPORT.md finding 3.
