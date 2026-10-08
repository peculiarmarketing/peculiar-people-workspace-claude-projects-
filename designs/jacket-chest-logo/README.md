# Jacket chest logo (left or right chest, 3 to 5 in)

Started 8 October 2026. Companion to the back seal in `../jacket-seal/`. Read with `project-sync/BRAND.md`.

## Direction

The chest mark is a smaller version of the existing identity, not a new symbol.
No temple, no invented ornament (star, sunburst, wheel). Clean lines; the
sketch style stays with the temple art on the back.

## Sources

- `source/Peculiar_People_Logo_-_Square_-_Black.png`: the current logo (Evan, 8 Oct).
- `source/Peculiar People Seal thin black (Other designs).png`: the thin seal Evan
  actually uses, from `Other designs/`. Use this one as the reference, not the
  heavier version in `../jacket-seal/Peculiar People Seal/`.

## Round 1 drafts (Higgsfield, GPT Image 2.5, high, 2k)

| File | Direction | Notes |
|---|---|---|
| `higgsfield/A1-stacked.png` | A, stacked logo | Model thickened PECULIAR too far; thin/bold contrast lost |
| `higgsfield/A2-stacked-badge.png` | A, framed stacked logo with EST. 2023 | Clean; rules are thin for 3 in |
| `higgsfield/B1-seal-chosen-generation.png` | B, mini seal | Top text crowds the band |
| `higgsfield/B2-seal-utah.png` | B, mini seal | Shorter text, most air |
| `higgsfield/C-wordmark-print.png` | C, one-line wordmark | Same contrast loss as A1 |
| `higgsfield/A3-pp-box.png` | Extra: boxed PP | Type-only PP, check against the rejected monogram note |

`previews/chest-previews-3.5in.jpg` shows each one as white ink on navy and
black at 3.5 in wide.

Round 1 drafts are raster AI images, not print files. Whichever direction wins gets
rebuilt as vectors from the real logo, with stroke weights checked by the
`design-audit` skill, before any Tapstitch upload.

## Round 2: A2 picked, rebuilt as vectors (8 October 2026)

Evan picked A2. A rectangle inside a circle (B) felt off. Requirement: the
lettering must be identical to the original logo.

- The PECULIAR letters were drawn by an image model about two years ago and are
  in no font file (the closest free font, Outfit, overlaps only 77 percent). So
  `build_chest_logo.py` traces both words straight from the logo PNG. Trace
  overlap with the original: PECULIAR 98.5 percent, PEOPLE 99.5 percent
  (`out/proof-letterforms.png`).
- PEOPLE matches Oswald Regular (97 percent overlap), so the new text, EST. 2023,
  is set in Oswald 400 (`fonts/`, OFL).
- Both words are scaled to the same width with no stretching. Original letter
  spacing is kept.

At 3.5 x 3.12 in: frame 1.6 mm, rules 1.2 mm, EST. 2023 cap height 0.25 in,
thinnest PECULIAR stroke 0.93 mm. That stroke is just under the 1 mm DTG rule of
thumb. It reaches 1 mm at 3.75 in wide. DTF holds it at 3.5 in.

Outputs in `out/`: `chest-logo-a2-white.svg` / `-black.svg` (vector masters),
`chest-logo-a2-white-3.5in-300dpi.png` (white ink, every pixel's colour set to
white per BRAND.md section 8), navy and black previews.

**Final size: 3.75 in wide (Evan, 8 October 2026).** 3.75 x 3.34 in: frame
1.71 mm, rules 1.31 mm, EST. 2023 cap height 0.27 in, thinnest PECULIAR stroke
0.99 mm. Print files: `out/chest-logo-a2-white-3.75in-300dpi.png` and `-black-` (transparent, 1125 x 1003 px). Solid `-white-on-black` and `-black-on-white` versions (SVG and PNG) carry a margin equal to the clear space inside the frame, 0.147 in at 3.75 in (1213 x 1091 px). Flush to the frame was rejected: crops, rounded thumbnails and resampling eat the outer frame line.
Evan places it on the garment himself.
