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
- Temple E is the approved art, scaled 1.6 percent with the field. The seal uses a
  DTG-thickened version (`trace/Salt Lake E DTG white.svg`, see below); the
  untouched trace is `trace/Salt Lake E white.svg` (`--original-temple`).

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

## Chosen: Arvo Bold (Evan, 7 October 2026)

`Peculiar People Seal/` holds the finished files for `Other designs/`:

| File | What it is |
|---|---|
| `Peculiar People Seal white.png` | print file, white ink, 3600 x 3600 px at 300 ppi (12 in), transparent |
| `Peculiar People Seal black.png` | the same in black ink |
| `Peculiar People Seal white.svg` / `black.svg` | vector sources |

The PNGs follow the BRAND.md section 8 file rules: every pixel, visible or not,
carries the ink colour, and alpha is fully ink or fully clear (no tints). Rebuild
with `python3 build_seal.py --print-png` (Arvo is now the default).

## Temple thickened for DTG (Evan, 7 October 2026)

Inside the seal, temple E prints at about half its stand-alone size, so its
lightest lines were 0.24 mm at 12 in, under every print method's minimum (DTG
0.71 mm). `dtg/thicken.py` fixes that on the source drawing, upscaled 4x:

1. Every line grows 0.30 mm per side, so all three weights move up together and
   keep their order.
2. Every line gets a minimum width of 0.95 mm along its centre line, which
   catches the faint construction strokes that started under 0.11 mm.

The result is retraced with the temple-svg-tracer skill (`--upscale 1`, it is
already 8192 px). At 0.84 mm the floor still measured within one pixel of the DTG
limit after tracing and rasterising, so it was raised to 0.95.

Audit of the final print file (`research/design-audit/audits/seal_final_arvo_dtg/`):
0 FAIL on every method. Temple lightest lines 0.90 mm (DTG floor 0.71), no thin
regions left on the DTG overlay. Everything sits under the 1.06 mm DTG production
margin, so it reports WARN, the same as the type.

What it costs: the drawing reads heavier. Ink coverage went from 10.6 to 22.3
percent of the temple's frame, and 522 of 877 small enclosed gaps closed. The
rows of tiny square panels under the battlements are now solid bands, and the
spires' inner double lines fused. The windows, doors, round windows, battlements,
tails and the Moroni all still read.
