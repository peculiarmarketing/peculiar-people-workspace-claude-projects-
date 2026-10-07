# Design audit: jacket back seal (Salt Lake temple E)

**File:** `seal.png` (2048 x 2048 px, analysed at 2048 x 2048 px, `image.analysis_scale` 1.0)
**Ink / ground:** white `#FFFFFF` on navy `#001A58`, colour mode
**Audited at:** 12 in and 10 in wide, ink to ink (ink box 1759 px, so 0.173 mm per px at 12 in and 0.144 mm per px at 10 in, `print_check.json` `px_resolution_mm`)
**Print method assumed:** all four methods, because the jacket blank and its method are unknown (BRAND.md section 7 covers only the tee and fleece). Binding line rule is DTG (0.71 mm fail, 1.06 mm warn); binding gap rule is screen (0.53 mm fail) and DTF (1.0 mm warn) (`targets.json` `binding`).
**Scripts:** run_audit.py output in `research/design-audit/audits/seal_audit/`
**Detection check:** The seal has four rings: a heavy outer ring, a thin ring under the motto band, then a close pair at the inner field (a thin ring outside a heavy ring). The scripts found only the two heavy rings (`measurements.json` `rings`: ring1 outer, ring2 inner heavy). The two thin rings (about 5 px wide and up to 6 px off centre) were missed, so the scripts treated everything between the heavy rings as one band. That merged the motto and the PECULIAR PEOPLE title into fragmented arcs and made every zone, band-clearance, arc-room and `ring_gaps` number wrong. I did not use those numbers. Instead I fitted all four rings by hand with the skill's own circle fit (`rings_manual.json`) and measured band gaps and text extents per ray from the outer ring centre. Unaffected and used as is: ring1 and ring2 widths, the centre art, the caption, per-arc cap heights, stems and hairlines, the ornaments, tones and all print_check element rows. Centre art and caption split correctly (`centre.art`, `centre.caption`).

## Verdict

Not ready to print at either size. On DTG, the binding method while the jacket's method is unknown, it fails three ways: every line of type has hairlines under the floor, the two thin rings fall under the floor at 10 in, and most of the temple's lines fall under every method's floor at both sizes. The rings and type are fixed in the planned vector rebuild (spec below). The temple's line weight is a brand call: no layout change can fix it, because its lightest lines would need to be 3.3 times thicker. Settle on **12 in**: more passes at 12 than at 10, and none of the rules prefers 10. Ask Tapstitch which method the jacket uses before anything else. If it is screen print, the floor drops to 0.35 mm and most of these failures shrink to near misses.

## Findings, ranked

### 1. Type hairlines are under the print floor on every text line  (breaks print)

- **Rule:** PRINT-02 Type hairlines and serifs count as lines (ESTABLISHED); TYPE-07 Small type needs a sturdy, low-contrast face (ESTABLISHED).
- **Mechanism:** The type is a high-contrast serif. Its thin strokes (crossbars, serifs, the thin side of each letter) are what break first. On DTG a stroke this thin cannot carry its white underbase, so it prints translucent or ghosted on navy. On DTF it lacks the adhesive mass to stay put through washes.
- **Evidence** (`print_check.json`, rule PRINT-02 rows; red letter edges in `print_flags_10in_dtg_fail.png`):
  - Motto, EST. 2023 and UTAH, USA: hairline 2.5 px. That is 0.43 mm at 12 in and 0.36 mm at 10 in. It fails DTG (0.71) at both sizes and DTF (0.50) at both; the DTF miss at 12 in is at measurement resolution (0.07 mm under, one px is 0.17 mm). It warns on screen print (0.50).
  - PECULIAR PEOPLE: hairline 3.5 px. That is 0.61 mm at 12 in and 0.51 mm at 10 in. It fails DTG at both sizes.
  - Motto and bottom-arc stems: 5.5 px, 0.95 / 0.79 mm. They warn on DTG and DTF.
- **Fix:** Rebuild all type in a face whose thinnest stroke is at least 0.0028 D, aiming for 0.0042 D. That is 0.86 mm (2.4 pt) floor and 1.29 mm (3.6 pt) margin at 12 in, or 0.71 mm (2.0 pt) and 1.07 mm (3.0 pt) at 10 in. At the motto's cap height (0.0181 D), the floor means the thinnest stroke must be about 15 percent of cap height. In practice that needs a monoline or slab serif, not a classical high-contrast serif. If the classical look matters more, the alternatives are a larger motto, or confirming that the jacket is not DTG. The title at 0.0306 D needs a thinnest stroke of about 9 percent of cap height, which a bold, low-contrast serif can reach.
- **Tool:** vector rebuild of rings and type.

### 2. The two thin rings are at or under the DTG floor  (breaks print at 10 in; at measurement resolution)

- **Rule:** PRINT-01 Minimum positive line (ESTABLISHED); LINE-03 the finest line still clears the print minimum (ESTABLISHED).
- **Mechanism:** Same as finding 1. Long thin white lines on a dark garment are the first features to lose their underbase, and a ring that fades in patches reads as a print fault.
- **Evidence** (`rings_manual.json`; red arcs on both thin rings in `print_flags_10in_dtg_fail.png`):
  - Both rings average 5.1 px wide, 0.0029 D. At 12 in that is 0.88 mm mean and 0.69 mm at the thinnest 5 percent (4 px). At 10 in it is 0.73 mm mean and 0.58 mm thinnest.
  - Against DTG's 0.71 mm floor, the rings fail at 10 in and sit on the line at 12 in. They are under the 1.06 mm production margin at both sizes, and under DTF's 1.0 mm production margin.
- **Fix:** Rebuild both thin rings at 0.0042 D (1.29 mm at 12 in, 1.07 mm at 10 in). Never go below 0.0028 D. See the Rebuild spec.
- **Tool:** vector rebuild of rings and type.

### 3. The temple's lines are under every method's floor at seal size  (breaks print; brand call)

- **Rule:** PRINT-09 Art reduced into a seal loses detail in proportion (ESTABLISHED, derived); PRINT-01 (ESTABLISHED); PRINT-12 texture may drop, text may not (SINGLE SOURCE).
- **Mechanism:** Temple E was drawn to fill a square on its own. Inside the seal it prints at 5.1 x 6.4 in at a 12 in seal, and 4.3 x 5.3 in at 10 in. That is about half its stand-alone size, and every line shrinks by the same factor. The lightest lines are interior detail (windows, bands, battlement notches), so they go first. On screen print, the gaps inside the battlements and windows also close.
- **Evidence** (`centre.art.weights`; `print_check.json` centre art rows; nearly the whole drawing is red in `print_flags_10in_dtg_fail.png`):
  - The art has three line weights, measured in px:
    - 1.5 px, 55 percent of the art's ink: 0.26 mm at 12 in, 0.22 mm at 10 in.
    - 2.5 px, 13 percent: 0.43 / 0.36 mm.
    - 4.72 px, 32 percent: 0.82 / 0.68 mm.
  - The lightest weight fails every method, including screen print (0.35 mm).
  - At 10 in on DTG, only the heaviest weight comes close, and it still fails (0.68 vs 0.71, at measurement resolution).
  - Screen print would also close 336 gap regions at 10 in, all inside the art: battlement notches and window interiors (`morphology.fail.closing_gaps`).
- **Fix:** None of the layout options is enough.
  - The largest standard back print (14 in, PRINT-07) gives a factor of only 1.17.
  - Shrinking the bands to enlarge the field gains about 10 percent.
  - Reaching 0.0028 D needs the lightest line to grow 3.3 times.
  - So the options are Evan's: see Brand conflicts.
- **Tool:** no change: brand call.

### 4. Rings are not concentric, not round, and not even in weight  (polish; one fix covers it)

- **Rule:** SEAL-01 Rings are concentric (ESTABLISHED); SEAL-02 Ring gaps are uniform (ESTABLISHED); LINE-01 Consistent stroke weight (ESTABLISHED).
- **Mechanism:** The rings were generated as an image, not drawn as circles. Each one drifts off the outer ring's centre and wobbles. The eye compares neighbouring rings directly, so a gap that changes width around the circle reads as a mistake. This is most visible in the tight inner pair, where a 2.5 px drift is a third of the gap.
- **Evidence** (`rings_manual.json`; per-ray gaps; crops `crop_double_ring_narrow_194deg.png`, `crop_double_ring_wide_340deg.png`):
  - Centre offsets from the outer ring: thin ring 4.5 px, inner thin ring 6.4 px, inner heavy ring 7.5 px. The 7.5 px offset is 1.30 mm at 12 in and 1.08 mm at 10 in; the inner rings sit low.
  - Gap variation around the circle (tolerance 3 percent):

    | Gap | Width now | Variation |
    |---|---|---|
    | Motto band | 79 to 91 px | 14 percent |
    | Title zone | 119 to 130 px | 9 percent |
    | Inner pair | 11 to 16 px | 36 percent |

  - Width variation (CV) against the noise floor: outer ring 7.0 against 3.8 percent, inner heavy ring 5.4 against 4.2 percent, thin rings 13.4 to 13.6 against about 10 percent.
  - The outer ring is out of round: circle-fit RMS 2.5 to 2.8 px.
- **Fix:** Rebuild every ring as a true circle with one shared centre (offset 0), at the widths and gaps in the Rebuild spec. This one change also clears LINE-01, SEAL-02 and the uneven inner pair.
- **Tool:** vector rebuild of rings and type.

### 5. Band text sits off its centre line  (polish)

- **Rule:** SEAL-04 Band text is centred in its band (ESTABLISHED, derived); TYPE-06 Arcs that share a band sit on one centre-line radius (ESTABLISHED).
- **Mechanism:**
  - The motto hugs the outer ring, so the band looks lopsided.
  - PECULIAR PEOPLE hugs the thin ring above it, while EST. 2023 sits on a different, lower radius. The pair looks like two separate bands rather than one.
- **Evidence** (per-ray text extents from the outer ring centre; `crop_top_title_and_motto.png`):
  - Motto (caps from radius 817 to 853 px): 17 px of clearance to the outer ring against 32 px to the thin ring. The outer-to-inner ratio is 0.54, where the tolerance is 0.9 to 1.1.
  - PECULIAR PEOPLE (709 to 763 px): 17 px of clearance above, 52 px below.
  - Radial centres: PECULIAR PEOPLE at 736 px, EST. 2023 at 707.5 px (`zones` arc r_min and r_max). The 28.5 px difference is 23 percent of the 124 px zone, where the tolerance is 2 percent.
- **Fix:** Centre the motto at radius 0.4677 D, with equal clearance of 0.0150 D each side (4.6 mm at 12 in, 3.8 mm at 10 in). Put PECULIAR PEOPLE and EST. 2023 on one shared centre line at 0.4044 D. Both radii come from the rebuilt ring positions in the spec.
- **Tool:** vector rebuild of rings and type.

### 6. Four type sizes where two would do; the small steps barely differ  (polish)

- **Rule:** RATIO-03 Type sizes come from one consistent ratio (ESTABLISHED); TYPE-02 At most three text levels (ESTABLISHED).
- **Mechanism:** The motto, the date and the caption are all small supporting text, but they are three sizes only 16 to 19 percent apart. A step that small reads as an accident, not a hierarchy.
- **Evidence** (cap heights from `zones` arcs and `centre.caption`):
  - PECULIAR PEOPLE: 54 px.
  - UTAH, USA: 38 px.
  - EST. 2023: 37.4 px.
  - Motto: 32 px.
  - That makes three clusters (54, 37.5 and 32) with steps of 1.44 and 1.17. The steps are not within 25 percent of each other, so it fails the RATIO-03 tolerance. It passes TYPE-02, but only just.
- **Fix:** Set the motto, EST. 2023 and UTAH, USA at one cap height of 0.0181 D (5.5 mm, about 23 pt type, at 12 in; 4.6 mm, about 19 pt type, at 10 in). PECULIAR PEOPLE stays at 0.0306 D. That gives two levels, 1.69 apart. The small text stays far above the 10 pt warning (PRINT-05).
- **Tool:** vector rebuild of rings and type.

### 7. The three diamonds are two sizes, in two different bands  (polish; SINGLE SOURCE rule)

- **Rule:** SEAL-05 Dividers are consistent and placed symmetrically (SINGLE SOURCE).
- **Mechanism:** The side diamonds flank the title zone, while the bottom one closes the motto band. Different bands can be a deliberate choice, since the two sets play different roles. Different sizes read as a mismatch either way.
- **Evidence** (`zones` ornament rows; `crop_left_diamond.png`, `crop_bottom_diamond.png`):
  - The side diamonds are 51 px (0.0289 D), centred at radius 716 to 718 px, at 90.6 and 269.4 degrees. That is 0.6 degrees off the 3 and 9 o'clock positions; the tolerance is 0.5.
  - The bottom diamond is 41 px (0.0232 D), at radius 830 px and 179.9 degrees.
- **Fix:** Make all three diamonds one size, 0.0232 D (7.1 mm at 12 in, 5.9 mm at 10 in). Put them exactly at 90, 270 and 180 degrees about the shared centre. Each sits on its own band's centre line: 0.4044 D for the sides, 0.4677 D for the bottom. Whether the bottom one should move to the title zone is a design choice, not a rule.
- **Tool:** vector rebuild of rings and type.

### 8. The caption sits right of the vertical axis  (polish)

- **Rule:** COMP-07 One vertical axis (ESTABLISHED).
- **Mechanism:** UTAH, USA sits directly under a symmetrical temple, so even a small sideways shift shows.
- **Evidence:** `centre.caption.center_x_offset` is 9.9 px (1.7 mm at 12 in). That is 0.79 percent of the inner diameter, against a 0.5 percent tolerance. The art is on axis (`centre.art.bbox_center_offset` x 1.9 px).
- **Fix:** Centre the caption on the seal's axis, optically: the comma makes the bounding box slightly wider on the left.
- **Tool:** vector rebuild of rings and type.

### 9. Print-file hygiene  (polish)

- **Rule:** PRINT-06 No tints in the print file (ESTABLISHED); PRINT-10 Supply true vectors (ESTABLISHED); PRINT-04 Small isolated shapes lift on DTF (ESTABLISHED); COMP-01 Centred in the canvas (ESTABLISHED).
- **Mechanism:** This file is a raster mockup. It has semi-transparent pixels, which DTG prints as a chalky halo. It has one-pixel specks from the trace, which will not transfer on DTF. Its ink is also off the canvas centre.
- **Evidence:**
  - `tones.tint_pixels`: 147.
  - `smallest_shapes`: specks at 0.17 mm, under DTF's 0.5 mm.
  - `centring.bbox_offset_from_canvas`: (-2, -9) px. The -9 px is 0.51 percent of the ink width, against a 0.25 percent tolerance.
- **Fix:** Deliver the final file as expanded vectors, with no tints and specks cleaned out in the trace. Crop it to the ink box; BRAND.md section 8 centres the ink block, so the canvas offset then disappears.
- **Tool:** vector rebuild of rings and type (plus the temple trace).

## Brand conflicts

- **Temple E's line weights (finding 3).** PRINT-09 says the art's lines must clear the print floor at their printed size. BRAND.md treats the line-drawing style as settled, and E is approved art. The layout cannot close a 3.3 times gap. Evan's options:
  1. **Thicken the lines during the vector trace.** Add a uniform stroke so the lightest weight reaches 0.0028 D (0.86 mm at 12 in). This changes the 5 : 2.5 : 1 weight hierarchy into something closer to 3 : 2 : 1.5, and makes the drawing read heavier.
  2. **Make a seal variant of E.** Draw it fresh at seal size, with fewer interior lines and the house prompt's weights set for a 5 in print.
  3. **Confirm the jacket's method first.** If it is screen print (0.35 mm floor), only the lightest weight fails, by about 0.1 mm at 12 in. A smaller thickening would then do.
- **Caption wording.** BRAND.md section 8 sets the back-print location line as the temple's physical city and state ("SALT LAKE CITY, UTAH" style). The seal says "UTAH, USA", from Evan's draft. This audit does not judge copy, but the two differ. Evan's call whether the seal follows the location-line rule.
- **White ink only:** no conflict. The seal is one colour.

## Rebuild spec

D is the outer diameter of the outer ring (outer edge to outer edge). At a 12 in print D is 306 mm; at 10 in it is 255 mm. Radii are measured from the shared centre, and every ring is concentric (offset 0). Strokes follow 1 : 2 (thin rings : heavy rings). The thin-ring weight is the DTG production margin; the floor values in brackets are the absolute minimum.

| Element | Target | Fraction of D | At 12 in | At 10 in | Rule |
|---|---|---|---|---|---|
| Outer ring stroke | heavy, equal to the inner heavy ring (now 0.0073 D) | 0.0083 | 2.54 mm / 7.2 pt | 2.12 mm / 6.0 pt | LINE-02, LINE-03, SEAL-03 |
| Outer ring, outer radius | edge of seal | 0.5000 | 153.0 mm | 127.5 mm | |
| Motto band (outer ring to thin ring, edge to edge) | uniform, keep current width | 0.0480 | 14.69 mm | 12.24 mm | SEAL-02, COMP-04 |
| Motto cap height | keep | 0.0181 | 5.54 mm (about 23 pt type) | 4.62 mm (about 19 pt type) | PRINT-05, RATIO-03 |
| Motto centre-line radius | centred in band, 0.0150 D clear each side | 0.4677 | 143.1 mm | 119.3 mm | SEAL-04, TYPE-06 |
| Thin ring stroke (under motto) | margin (floor 0.0028 D) | 0.0042 | 1.29 mm / 3.6 pt (floor 0.86) | 1.07 mm / 3.0 pt (floor 0.71) | PRINT-01, LINE-02 |
| Title zone (thin ring to inner thin ring, edge to edge) | uniform, keep current width | 0.0702 | 21.48 mm | 17.90 mm | SEAL-02 |
| PECULIAR PEOPLE cap height | keep | 0.0306 | 9.36 mm | 7.80 mm | RATIO-03 |
| EST. 2023 cap height | match motto | 0.0181 | 5.54 mm | 4.62 mm | RATIO-03, TYPE-02 |
| Title and EST centre-line radius | one shared line, centred in zone | 0.4044 | 123.7 mm | 103.1 mm | TYPE-06, SEAL-04 |
| Side diamonds (90 and 270 degrees) | on 0.4044 D | 0.0232 size | 7.10 mm | 5.92 mm | SEAL-05 |
| Bottom diamond (180 degrees) | on 0.4677 D | 0.0232 size | 7.10 mm | 5.92 mm | SEAL-05 |
| Inner thin ring stroke | margin (floor 0.0028 D) | 0.0042 | 1.29 mm | 1.07 mm | PRINT-01 |
| Gap inner thin ring to inner heavy ring | uniform, keep | 0.0078 | 2.39 mm | 1.99 mm | SEAL-02, PRINT-03 (over 1.0 mm DTF margin) |
| Inner heavy ring stroke | equal to outer ring | 0.0083 | 2.54 mm | 2.12 mm | LINE-02 |
| Field diameter (inside inner heavy ring) | result of the above (now 0.709 D) | 0.698 | 213.6 mm | 178.0 mm | RATIO-05 (report only) |
| UTAH, USA cap height | match motto | 0.0181 | 5.54 mm | 4.62 mm | RATIO-03 |
| Thinnest stroke in any letter | margin (floor 0.0028 D) | 0.0042 | 1.29 mm | 1.07 mm | PRINT-02, TYPE-07 |
| Temple art | keep placement: block centre 4.9 percent of field above centre | | | | COMP-02 |

Working outside in, the ring radii are: outer ring 0.5000 to 0.4917, thin ring 0.4437 to 0.4395, inner thin ring 0.3693 to 0.3651, inner heavy ring 0.3573 to 0.3490. Heavier rings shrink the field by about 1.6 percent. Either scale the temple down 1.6 percent, or keep it at its size and let the top clearance fall from about 55 px (0.031 D) to about 35 px (0.020 D). That is still more than the band text clearances, so SEAL-06 holds either way. If Evan wants the border to lead, the outer ring can step up to 0.0117 D (1.4 times the inner heavy ring); the radii inside it then move in by 0.0034 D. Expand all strokes and type to outlines before export (LINE-05, PRINT-10).

## Passed

- COMP-02: the art-plus-caption block sits 61 px above the inner ring centre, 4.9 percent of the field (target 0 to 5 percent above).
- COMP-06 and TEST-01: at 1 percent blur PECULIAR PEOPLE stays a distinct shape; at 2 percent the temple silhouette holds while the motto dissolves first, as it should.
- LOGO-02: the largest word is legible in `small_2in.png`; the temple is recognisable in `small_1in.png`.
- LOGO-03 and TEST-02: one colour; the only tints are 147 antialias pixels (handled in finding 9).
- LINE-02: four distinct weights in all, with each step at least 1.67 times the last (art 1.5, 2.5 and about 4.9 px; heavy rings about 12.2 px).
- LINE-03: the outer ring (12.8 px) is the heaviest line in the mark.
- LINE-04: the thinnest ring (5.1 px) is 1.07 times the art's heaviest weight (4.72 px). The tolerance is 1 to 2 times.
- SEAL-06: the art's closest approach to the ring is 54.8 px, more than the smallest text clearance (17 px).
- TYPE-01: the smallest text has the loosest spacing: the motto's gap-to-cap ratio is about 0.9, against 0.41 for the title.
- TYPE-04: EST. 2023 reads left to right, upright (`crop_bottom_arc_est.png`). The motto stops short of 6 o'clock, so no bottom text is upside down.
- TYPE-09: no distorted letterforms in the crops.
- PRINT-03: no gap failures on text or rings at any method; the gap flags are all inside the art (finding 3).
- PRINT-05: the smallest text estimates to 19 pt at 10 in (warning level 10 pt).
- PRINT-07: 10 and 12 in are both standard back widths; the design is 12.07 in tall at 12 in, inside the narrowest back print area (18.4 in).
- RATIO-01, RATIO-02, RATIO-04: FOLKLORE, never applied.

## Not checked

- TYPE-03, TYPE-05, TYPE-08: per-arc spacing variation, arc midpoint angles and the inside-versus-outside tracking comparison. The missed thin rings broke the arcs into fragments (see Detection check). In the crops the spacing looks even and the title looks centred at 12 o'clock, but there are no numbers to cite.
- RATIO-05: reported in the spec (field 0.709 D now, 0.698 D rebuilt). It is reference only, and a seal with two text zones is expected to sit below the 0.63 to 0.67 range of regulated seals.
- TEST-03, TEST-07: need real viewers and a viewing distance; not approximated beyond the small-size previews.
- TEST-06: a 1 to 1 paper print at 12 in is the last step after the rebuild.
- Whether the jacket is DTG, DTF or screen print. Tapstitch publishes no artwork spec. Ask them for the jacket's method and minimums, and update `references/print_thresholds.json`.

## Previews looked at

- `onecolour.png`: four rings visible; the scripts reported two (Detection check).
- `blur_1pct.png`, `blur_2pct.png`: hierarchy holds. The title and temple survive, the motto goes first.
- `small_1in.png`, `small_2in.png`: the temple reads at 1 in; PECULIAR PEOPLE reads at 2 in; the motto is texture at both, as expected for a back print.
- `print_flags_10in_dtg_fail.png`: red on both thin rings, on the type hairlines, and on almost all of the temple except its heavy outline.
- `print_flags_12in_dtg_fail.png` and the screen overlays: same pattern, smaller. On screen print the yellow closing gaps sit only inside the temple's battlements and windows.
- `spread_10in.png` (zoomed on the towers): 0.1 mm of spread nearly fills the rows of small square panels under the battlements, and thickens the window surrounds. This is the first detail to go if the ink spreads.
- Crops: `crop_top_title_and_motto.png`, `crop_bottom_arc_est.png`, `crop_left_diamond.png`, `crop_bottom_diamond.png`, `crop_double_ring_narrow_194deg.png`, `crop_double_ring_wide_340deg.png`, `crop_art_tower_detail.png`, `crop_caption.png` (all in this folder; `sheet_crops.png` and `sheet_previews.png` collect them).
