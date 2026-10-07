# SPEC: Designing for Screenprinting (5 Common Mistakes)

- Title: Designing for Screenprinting (5 Common Mistakes)
- Channel: Golden Press Studio
- URL: https://www.youtube.com/watch?v=-PBTivLnhEw
- Upload date: 2021-12-07
- Duration: 20:36
- Why this video: a working print-shop art director's file-prep rules; the stroke-scaling demo on a circle maps directly onto seal rings drawn as strokes.

Readers: one (reader A, transcript plus 160x90 storyboard). Gemini pass did not run, so every line is SINGLE SOURCE (reader A).

## Principles

- SINGLE SOURCE (reader A): Build print art in a vector program (Adobe Illustrator or similar) so it stays crisp at any size.
- SINGLE SOURCE (reader A): Expand fonts to shapes ("Object > Expand", "object and fill checked") so the printer does not hit missing fonts.
- SINGLE SOURCE (reader A): Expand strokes before scaling. A stroked circle scaled to a new size changes proportion ("it's kind of changed its shape"); the expanded copy "is going to maintain its width" relative to the circle. "we want to maintain exactly its shape."
- SINGLE SOURCE (reader A): Final art should be "solid shape" because "strokes and those kind of things can get hairy at times".
- SINGLE SOURCE (reader A): Variable-width strokes need "expand appearance" (plain Expand is greyed out); unexpanded they "get all fat and weird" when scaled down.
- SINGLE SOURCE (reader A): Avoid clipping masks in screen-print art (speaker's personal rule); rebuild with Pathfinder "minus front" so the result is one solid compound shape that recolours cleanly.
- SINGLE SOURCE (reader A): Ask the printer for its colour limit before designing; this shop's press maximum is six colours.
- SINGLE SOURCE (reader A): A 12-colour design was reduced to six colours using halftones for shadows and a colour reused as an underbase for hair.
- SINGLE SOURCE (reader A): Supply vector or high-resolution art; a JPEG placed in an .ai file is not "a proper illustrator file".
- SINGLE SOURCE (reader A): Ideal file: one clean shape the printer can "click on it make it black".

## Numbers

- SINGLE SOURCE (reader A): "10 inches wide" (circle size in the stroke-scaling demo).
- SINGLE SOURCE (reader A): "maximum color is six colors"; client art "around 12 colors"; result "a six color print".
- SINGLE SOURCE (reader A): Procreate canvas "5 000 by 5 000", "dpi is 500".
- SINGLE SOURCE (reader A): Image Trace preset: threshold "97", paths "97", corners "97", noise "1", "ignore white" selected.

## Demonstrated vs said

- SINGLE SOURCE (reader A), shown: font expansion; stroked vs expanded circle scaled with a visible ring-thickness difference (red overlay); variable stroke expanded with Expand Appearance; clipping mask release failure and Pathfinder rebuild; 12-to-6 colour reduction with halftones; leaf re-trace via Pen tool and via Procreate plus Image Trace.
- SINGLE SOURCE (reader A), said only: an Illustrator setting that keeps strokes proportional (speaker unsure, not shown); the 6-colour print matching the brown tone (no print shown).

## Caveats

- SINGLE SOURCE (reader A): Clipping-mask rule is explicitly personal and limited to screen printing.
- SINGLE SOURCE (reader A): The six-colour limit is this shop's press, not a universal number.

## Archetype trap flags

- Minimum line weights, gap sizes, mesh counts, ink spread, white underbase on dark garments: none of these are in this video. Do not attribute them here.
- The stroke-scaling point is about file behaviour in Illustrator (stroke weight not scaling with the object), not about how ink behaves on fabric.

## OPEN QUESTIONS

- Stroke weight values on the demo circle before and after scaling: UNREADABLE.
- Which direction the unexpanded stroke changed (thinner relative to a larger circle) is inferred from the overlay, not stated with numbers.
- Halftone LPI, angle, density used for the 6-colour reduction: not given.
- No guidance on minimum detail size at print size; would need another source.
