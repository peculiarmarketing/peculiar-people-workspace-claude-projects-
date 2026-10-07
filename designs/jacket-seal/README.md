# Jacket back seal

Vector rebuild of the seal audited in
`research/design-audit/audits/seal_audit/REPORT.md`, built to its rebuild spec
at 12 in (D, the outer ring's outer diameter, = 304.8 mm).

    python3 build_seal.py --font zilla        # or --font montserrat
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

## Fonts (both SIL OFL, licences in `fonts/`)

- Zilla Slab Bold: slab serif, thinnest stroke 0.169 of cap height. Uses its lining
  figures for 2023.
- Montserrat Bold (static instance of the variable font at wght 700): the
  storefront's heading face, thinnest stroke 0.174 of cap height.

Classical serifs (Cinzel, Marcellus, Cormorant) measured 0.04 to 0.07 and cannot
reach the DTG floor at this size; the small text needs about 0.155.

## Audit of the rebuild at 12 in (`research/design-audit/audits/seal_rebuild_<font>/`)

- 4 rings found, centre offsets under 0.03 px; all ring widths pass every method
  (thin rings 1.22 mm, heavy 2.34 to 2.44 mm).
- Type hairlines 0.86 mm (Zilla) / 0.97 mm (Montserrat): pass the DTG floor
  (0.71), WARN under the 1.06 mm production margin.
- Band text centred (outer to inner clearance ratio 1.00 to 1.04); arcs on the axis
  within 0.1 degrees; diamonds at 90.0 / 180.0 / 270.0 on their band centre lines;
  caption offset 0.0.
- Still FAILS: the temple's lightest lines (0.24 mm) on every method. Brand call,
  see REPORT.md finding 3.
