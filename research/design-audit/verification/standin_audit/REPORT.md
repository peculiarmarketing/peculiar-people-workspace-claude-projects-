<!-- Iteration 1 verification run of the design-audit skill on the stand-in seal, 7 Oct 2026. Written by a fresh subagent following SKILL.md; saved by the parent session. Script fixes made after this run are listed in ../verification/FIXES.md. -->

# Design audit: Peculiar People jacket back seal (stand-in)

**File:** `.claude/skills/design-audit/tests/fixtures/standin_seal.png` (3000 x 3000 px, analysed at 3000 x 3000 px, `image.analysis_scale` 1.0)
**Ink / ground:** white `#FFFFFF` on navy `#001A58`, ink_mode `colour`
**Audited at:** 12 in and 10 in wide, ink to ink. Outer diameter D = 2880.84 px, which is 304.8 mm at 12 in and 254.0 mm at 10 in.
**Print method assumed:** all four (screen, screen transfer, DTF, DTG). The jacket's method is unknown, so per PRINT-08 the strictest rule that could apply is binding: DTG on dark for lines (fail 0.71 mm, warn 1.06 mm) and screen transfer for gaps (fail 1.02 mm). If Tapstitch confirms DTF, the line floor drops to 0.50 mm (warn 1.00 mm) and the gap rule becomes a 1.0 mm warn.
**Scripts:** run_audit.py output in `research/design-audit/verification/standin_audit/`
**Detection check:**
- **Rings:** 3 found, matching the image.
  - ring1 (outer) is 47.88 px, ring2 (thin) 8.9 px, ring3 (heavier inner) 29.9 px.
  - ring3's centre is (1514.0, 1505.99), 15.23 px off the outer centre. I confirmed this on four rays: the ring2 to ring3 gap is 287 px at top, 267 right, 275 bottom, 295 left.
- **Outer band:** the scripts report 2 arcs.
  - The bottom diamond is correctly an ornament at 180.02 deg.
  - The top text arc (65 components) has the left and right diamonds and the three round bullets merged into it. Bullets are dropped from the letter statistics, but the side diamonds are counted as letters, so `letter_gap_cv_pct` 29.1 is inflated.
  - Recomputed without the diamonds (my own pass with `common.components`): letter gap mean 12.59 px, CV 14.9 percent, min 7.94, max 16.16.
- **Inner zone:** 'PECULIAR PEOPLE' (top, 14 glyphs) and 'EST. 2023' (bottom, 7 glyphs) are detected correctly. The period in EST. is dropped as a speck.
- **Centre:** art and caption split correctly. The caption bbox [1310, 2185, 1690, 2228] is 'UTAH, USA'.
- **Corrected numbers:** two kinds of number use the wrong centre, and I corrected both below.
  - Every `centre.*` offset is measured from ring3's displaced centre, not the outer ring's.
  - Each arc's `gap_to_inner_ring_px` uses ring3's radius without its offset. EST shows 158.84 px; the true gap at 6 o'clock is about 153 px.
- **Stand-in art:** the temple is a 3/4 view crop from an old mockup, with perspective construction lines running past the building. Every number that depends on the art will change with the real front elevation: art line weights, mass centre, art bbox, and therefore caption spacing and block centring. Audited as given.

## Verdict

Not ready to print at either width. At both 12 in and 10 in the small serif type breaks print under every method except plain screen print. Its stems and hairlines fall below the line minimum, and the band's tightest letter gaps are under the gap minimum.

The change that does the most is to rebuild all the small type in one low-contrast (monoline) face at one cap height of 0.0177 D, and settle the print size at 12 in. At 10 in the band text has to grow by about 15 degrees of arc to hold both the line and gap floors, which pushes into the side diamonds. At 12 in it grows about 4 degrees and fits.

The temple art is approved, so its sub-minimum lines are a brand call. The layout can give it about 4 percent more room, not more.

## Findings, ranked

### 1. Small type is too light to hold ink: band text, EST. 2023 and UTAH, USA  (breaks print)

- **Rule:** PRINT-01 / PRINT-02: every stroke, including hairlines and serifs, clears the method's line minimum (ESTABLISHED). TYPE-07: small type needs a sturdy, low-contrast face (ESTABLISHED).
- **Mechanism:** on a dark garment the white needs an underbase (DTG) or a full adhesive layer (DTF). A stroke narrower than the minimum cannot carry it. On DTG it prints translucent; on DTF it lacks adhesive mass and peels or cracks in the wash. Serif hairlines go first, so the letters lose their thin parts and read broken.
- **Evidence** (`print_check.json` `widths[].methods.*.element_checks`; in overlay `print_flags_10in_dtg_fail.png` all three lines are solid red):

  | Text | Measure | px | 12 in | 10 in | Binding (DTG fail 0.71 mm) |
  |---|---|---|---|---|---|
  | Band | stem | 6.5 | 0.688 mm | 0.573 mm | FAIL both widths |
  | Band | hairline | 2.5 | 0.264 mm | 0.220 mm | FAIL both; also fails screen (0.35) and DTF (0.50) |
  | EST. 2023 | stem | 5.5 | 0.582 mm | 0.485 mm | FAIL both; DTF FAIL at 10 in |
  | EST. 2023 | hairline | 2.5 | 0.264 mm | 0.220 mm | FAIL both, every method |
  | UTAH, USA | stem | 4.5 | 0.476 mm | 0.397 mm | FAIL both; DTF FAIL both |
  | UTAH, USA | hairline | 1.5 | 0.159 mm | 0.132 mm | FAIL both, every method |

  - Stem to hairline ratios: band 2.6:1, EST 2.2:1, caption 3:1.
  - Hairlines are percentile estimates, but crop_caption.png and crop_band_narrowest_gap.png show the thin serifs directly.
  - Text size passes PRINT-05: estimated 13.2 to 18.8 pt at 10 in.
- **Fix:**
  - Set the band text, EST. 2023 and UTAH, USA in one monoline or very low-contrast face: hairline equal to stem, no thin serifs.
  - Thinnest stroke if 10 in stays a candidate: at least 0.00280 D. That is 0.71 mm / 2.02 pt at 10 in and 0.85 mm / 2.42 pt at 12 in.
  - Thinnest stroke if the print is settled at 12 in: at least 0.00233 D, which is 0.71 mm at 12 in.
  - For margin, aim at 0.00417 D (1.06 mm at 10 in, 1.27 mm at 12 in) where the cap height allows.
  - Cap height for all three: 0.0177 D, which is 4.50 mm / 12.74 pt at 10 in and 5.39 mm / 15.29 pt at 12 in. This raises the caption from 0.0125 D and EST from 0.0160 D.
  - At that cap height the minimum stroke is 0.158 of the cap height at 10 in (a bold monoline) or 0.132 at 12 in (a medium one).
  - E and B check: 3 strokes plus 2 counters must fit the cap height. 3 x 0.0028 + 2 x 0.00402 = 0.0164 D, which fits inside 0.0177 D.
- **Tool:** vector rebuild of rings and type.

### 2. Band letter gaps will close on transfer methods  (breaks print at the binding method; CONFLICT on the number)

- **Rule:** PRINT-03: open space must be wider than the minimum gap, and white on navy spreads outward into the gaps (ESTABLISHED direction; CONFLICT on the value).
- **Mechanism:** white ink is the ink here, so it spreads into the navy, and transfers spread again under heat and pressure. Tight pairs merge into one shape, and thickening the strokes for finding 1 removes more of the gap.
- **Evidence** (screen_transfer rows):
  - Band letter gap (5th pct) 9.47 px: 1.002 mm at 12 in, FAIL by 0.018 mm (a judgement call at 0.106 mm per px). At 10 in it is 0.835 mm, FAIL, and DTF WARN.
  - Caption letter gap 1.014 mm at 10 in, FAIL by 0.006 mm (judgement call).
  - The band minimum gap of 7.94 px (0.70 mm at 10 in) is the R to A pair in crop_band_narrowest_gap.png.
  - In print_flags_10in_screen_transfer_fail.png, most of the yellow on the band text sits in the notches where the strokes of A, N and Y meet. Any sharp angle fills there, so I did not count those.
- **Fix:**
  - Minimum letter gap, after the stroke change: 0.00402 D for 10 in (1.02 mm at 10 in, 1.23 mm at 12 in), or 0.00335 D if settled at 12 in (1.02 mm at 12 in).
  - Arc budget at 10 in: about +5.3 px per letter gap and +1.6 px per letter, so the band text grows about 350 px, or 15.5 degrees. Today only 28.0 px (left) and 31.6 px (right) separate the text from the side diamonds.
  - Arc budget at 12 in: the text grows about 4 degrees. That fits if word spaces drop to about 0.0111 D (32 px) and the phrase gaps around the bullets to about 0.0306 D (88 px).
  - Recommendation: settle the print at 12 in. If 10 in must stay, either move the side diamonds down symmetrically to about 97 and 263 deg or shorten the band text. Evan's call.
- **Tool:** vector rebuild of rings and type.

### 3. Rebuild the rings and text paths as concentric vectors  (breaks print on ring2 at 10 in DTG; the rest is polish)

- **Rules:** this one rebuild resolves:
  - PRINT-01: ring2 below the line floor (ESTABLISHED).
  - SEAL-01 / SEAL-02: rings concentric, gaps uniform (ESTABLISHED).
  - LINE-01: one weight per ring (ESTABLISHED).
  - SEAL-04: band text centred in its band (ESTABLISHED).
  - TYPE-06: top and bottom arcs share one centre-line radius (ESTABLISHED).
  - COMP-04: gaps that play the same role match (SINGLE SOURCE).
  - SEAL-08: text paths and ornaments built on the ring centre (SINGLE SOURCE).
- **Mechanism:**
  - An off-centre ring makes the gap beside it change around the circle.
  - Text closer to one ring than the other makes the band look lopsided.
  - Two arcs on different radii make the inner zone look tipped.
  - The thin ring sits on the DTG floor and will print patchy.
- **Evidence:**
  - ring2 (5th pct): 8.0 px = 0.705 mm at 10 in, DTG FAIL by 0.005 mm (judgement call). At 12 in it is 0.846 mm, DTG and DTF WARN. It shows as broken red along ring2 in print_flags_10in_dtg_fail.png.
  - ring3 is offset 15.23 px (1.61 mm at 12 in, 1.34 mm at 10 in). The ring2 to ring3 gap runs from 265.86 to 296.32 px around a mean of 281.09: 10.8 percent variation against a 3 percent tolerance.
  - ring2 width varies 4.1 percent (tolerance 3). An 8.9 px line measured to 0.5 px cannot resolve better than about 5 percent, so this is at the limit of measurement.
  - Outer band text: 80.09 px to ring1 vs 67.51 px to ring2, ratio 1.186 (tolerance 0.9 to 1.1).
  - Inner zone: PECULIAR PEOPLE's radial centre is 1039.5 px and EST's is 1083.4 px. They are 43.9 px apart, 15.6 percent of the band against a 2 percent tolerance. EST sits 74 px from ring2 and about 153 px from ring3 (crop_bottom_arc_est.png).
  - Text-to-ring clearances that play the same role are 67.5, 73.97, 80.1, 88.8 and 91.8 px, a 1.36x spread against a 10 percent tolerance.
  - The side diamonds are upright rather than rotated to the circle. Their radial extent is 31 px at the sides vs 44 px at the bottom (crop_divider_left.png vs crop_divider_bottom.png).
- **Fix:**
  - Build all circles on the outer ring centre.
  - Ring weights at 1:2:4 from the print floor: ring1 0.01669 D, ring3 0.00835 D, ring2 0.00417 D.
  - Band text centre line on a 0.44854 D radius, with 0.02592 D clearance each side.
  - Both inner-zone arcs on one centre line at 0.36654 D.
  - Move ring3 out so PECULIAR PEOPLE has the same 0.0259 D clearance as the band text. This widens the inner field from 0.604 D to 0.630 D.
  - Rotate all diamonds so each one's long axis points at the centre.
  - Expand strokes and type to outlines (LINE-05, PRINT-10). All mm values are in the Rebuild spec.
- **Tool:** vector rebuild of rings and type.

### 4. 'PECULIAR PEOPLE' hairlines are borderline at 10 in  (breaks print at 10 in DTG; WARN at 12 in)

- **Rule:** PRINT-02 (ESTABLISHED).
- **Mechanism:** as in finding 1; the bold serif's thin strokes lose their underbase first.
- **Evidence:**
  - Hairline 7.5 px: 0.661 mm at 10 in (DTG FAIL, DTF WARN), 0.793 mm at 12 in (WARN).
  - The stem (20.5 px) and minimum letter gap (12.42 px = 1.09 mm at 10 in) both pass.
  - Red shows on the serifs only in print_flags_10in_dtg_fail.png.
- **Fix:**
  - Keep the cap height at 0.03428 D: 8.71 mm / 24.68 pt at 10 in, 10.45 mm / 29.62 pt at 12 in.
  - If 10 in stays a candidate, use a weight whose hairline is at least 0.00280 D (0.71 mm at 10 in).
  - At 12 in the current hairline already clears the 0.71 mm floor.
- **Tool:** vector rebuild of rings and type.

### 5. Temple lines and gaps are below every method's minimum at seal size  (breaks print on texture; sorted last per PRINT-12)

- **Rule:** PRINT-09 (ESTABLISHED, derived); PRINT-04 (ESTABLISHED); PRINT-12 (SINGLE SOURCE).
- **Mechanism:** the art prints at about a third of its approved 12 in width, so every line and window gap shrinks by the same factor.
- **Evidence:**
  - Art width 1060 px: 4.42 in at 12 in, 3.68 in at 10 in.
  - Art weight clusters are 2.47, 4.48 and 8.47 px. The lightest is 0.261 mm at 12 in and 0.218 mm at 10 in, failing screen, DTF and DTG.
  - At 10 in: 545 thin-stroke regions for DTG (worst at box [1334, 1561, 1400, 1745], crop_red_art_dtg10.png) and 605 closing-gap regions for screen transfer (worst at [1730, 1362, 1742, 1697], crop_yellow_art_st10.png).
  - Three specks with a 3 px maximum dimension (0.264 mm at 10 in, 0.317 mm at 12 in) at [1552, 1240], [1285, 1292] and [1670, 1730]. That fails PRINT-04's 0.5 mm limit.
- **Fix:** layout only, plus clean-up.
  - Print at 12 in.
  - Use the wider field to scale the art from 0.3679 D to at most 0.3838 D wide: 93.5 to 97.5 mm at 10 in, 112.1 to 117.0 mm at 12 in.
  - Neither change brings the 2.47 px lines up to the floor (see Brand conflicts).
  - Clean the three specks as trace noise. That is not an art change.
- **Tool:** layout nudge; no change to the art: brand call.

### 6. The period in 'EST. 2023' sits at cap height  (hurts legibility)

- **Rule:** seen in crop; PRINT-04 (ESTABLISHED).
- **Mechanism:** the period sits at radius 1060.3 to 1067.4 px while the letters span 1059.3 to 1107.6. On the bottom arc that is the cap line, so it reads 'EST˙'. It is also only 8 px across.
- **Evidence:**
  - Seen in crop_bottom_arc_est.png.
  - Smallest-shape entry [1469, 2560, 1476, 2567]: 0.705 mm at 10 in, 0.846 mm at 12 in (PRINT-04 WARN under 1 mm).
- **Fix:** put the period on the baseline. Its smallest dimension should be at least 1.0 mm: 0.00394 D at 10 in, or 0.00328 D if settled at 12 in.
- **Tool:** vector rebuild of rings and type.

### 7. Text sizes step unevenly  (polish)

- **Rule:** RATIO-03 (ESTABLISHED); TYPE-02 passes with 3 levels.
- **Mechanism:** two sizes 10 percent apart read as a mistake, not a hierarchy.
- **Evidence:**
  - Cap heights: 98.76 (PECULIAR PEOPLE), 51.03 (band), 46.05 (EST), 36.0 px (caption).
  - Steps are 1.94x, 1.108x and 1.28x. The 1.108x step is under the 1.15x minimum, and the steps are not within 25 percent of each other.
- **Fix:** finding 1 sets all small type to 0.0177 D. That leaves two levels, a 1.94x step apart.
- **Tool:** vector rebuild of rings and type.

### 8. The temple and caption block sits low  (polish)

- **Rule:** COMP-02 (ESTABLISHED direction; the 5 percent figure is SINGLE SOURCE).
- **Mechanism:** the eye places a field's centre above its middle, so a block below centre looks like it is sliding out.
- **Evidence:**
  - The block bbox [970, 935, 2029, 2228] centres at y 1581.5. That is 81.5 px below the outer ring centre, 4.7 percent of the 1741 px inner diameter. The JSON shows 75.51 px against ring3's centre. The fail threshold is 1 percent below centre.
  - The art's mass centre is 53 px below the outer centre.
  - The stand-in's construction lines run about 200 px below the building base (crop_art_base_lines.png).
- **Fix:**
  - Centre the block 0.012 D above the ring centre: 3.66 mm at 12 in, 3.05 mm at 10 in. On the present art that is a move up of about 0.0403 D (12.3 mm at 12 in, 10.2 mm at 10 in).
  - Keep the art-to-caption gap at 0.0139 D (4.24 mm at 12 in, 3.53 mm at 10 in).
  - Recheck with the real art.
- **Tool:** layout nudge.

### 9. Two divider glyphs  (polish; SINGLE SOURCE)

- **Rule:** SEAL-05.
- **Mechanism:** two shapes and two sizes in one ring read as two systems.
- **Evidence:**
  - Positions pass: diamonds at 90.00, 180.01 and 270.00 deg, with radial centres 5 to 6 px off the text centre line (3 percent of the band, tolerance 5).
  - Round bullets (18.5 px) sit at 8.31, 46.50 and 320.72 deg; the diamonds are 44 x 31 px (crop_band_315.png).
  - The brief asks for both, so this may be deliberate.
- **Fix (optional):**
  - Between phrases, use a small diamond about 0.0064 D tall (1.6 mm at 10 in, 1.96 mm at 12 in).
  - At 3, 6 and 9 o'clock, keep diamonds at 0.01527 D (3.88 mm at 10 in, 4.65 mm at 12 in).
  - Put all of them on the 0.44854 D centre line. Evan's call.
- **Tool:** vector rebuild of rings and type.

### 10. Too many distinct line weights  (polish)

- **Rule:** LINE-02 (ESTABLISHED by analogy).
- **Evidence:**
  - Art 2.47, 4.48 and 8.47 px plus rings 8.9, 29.9 and 47.88 px make five distinct weights.
  - After the 1:2:4 rebuild there are six (rings 12.0, 24.1, 48.1 px).
  - LINE-04 passes: thinnest ring is 1.05x the art's heaviest line now, 1.42x after the rebuild.
- **Fix:** none while the approved art keeps three weights under the ring floor. Brand call.
- **Tool:** no change: brand call.

### 11. The 3/4 view temple's mass sits left of the axis  (polish)

- **Rule:** COMP-07 (ESTABLISHED).
- **Evidence:**
  - Measured from the outer ring axis: art bbox centre -0.5 px and caption 0 px pass, but the art's mass centre is -19.0 px, 1.1 percent against a 0.5 percent tolerance.
  - The JSON's -14.5 and -14.0 px are measured from ring3.
- **Fix:** none for the stand-in. The symmetric front elevation should pass; recheck after the swap.
- **Tool:** no change: brand call.

## Brand conflicts

- **PRINT-09 / PRINT-01 vs the approved temple art (BRAND.md section 8).**
  - At 3.68 to 4.42 in wide, the art's lightest lines (0.22 to 0.26 mm) and many window gaps fail every method. The layout fixes here do not reach the floor.
  - Option 1: accept loss of fine texture (PRINT-12 allows texture, never text, to drop out).
  - Option 2: commission a simplified seal-size variant with no line under 0.0028 D.
  - A seal larger than the 12 in back maximum is not available.
  - The choice is Evan's.
- **White ink only (BRAND.md section 7):** no conflict. `tones.tint_pixels` is 0. The final PNG still needs every pixel fully ink or fully clear, with transparent pixels set to the ink colour (section 8). The preview has 146,436 anti-aliased edge pixels.
- **TEST-05:** consider whether the ring needs both divider systems (finding 9). Removing anything is Evan's call.

## Rebuild spec

- D is the outer diameter of ring1, outer edge to outer edge. Radii are measured from the common centre.
- pt is the dimension in points, not a font size.
- Where the two widths differ, the 10 in value is binding while 10 in remains a candidate (PRINT-08).

| Element | Target | Fraction of D | At 12 in | At 10 in | Rule |
|---|---|---|---|---|---|
| Outer diameter D | ink to ink | 1 | 304.80 mm | 254.00 mm | PRINT-07 |
| All circles and paths | one centre | offset 0 | 0 | 0 | SEAL-01, SEAL-08 |
| ring1 stroke | 4 units | 0.01669 | 5.09 mm / 14.42 pt | 4.24 mm / 12.02 pt | LINE-02, SEAL-03 |
| ring1 inner edge radius | | 0.48331 | 147.31 mm | 122.76 mm | |
| Band clearance each side | equal | 0.02592 | 7.90 mm | 6.58 mm | SEAL-04, COMP-04 |
| Band text centre-line radius | | 0.44854 | 136.71 mm | 113.93 mm | TYPE-06 |
| Band cap height | | 0.01770 | 5.39 mm / 15.29 pt | 4.50 mm / 12.74 pt | PRINT-05, RATIO-03 |
| Small type thinnest stroke | monoline | 0.00280 (12 in only: 0.00233) | 0.85 mm (12 in only: 0.71) | 0.71 mm / 2.02 pt | PRINT-01/02, TYPE-07 |
| Small type min letter gap | one tracking per arc | 0.00402 (12 in only: 0.00335) | 1.23 mm (12 in only: 1.02) | 1.02 mm / 2.89 pt | PRINT-03, TYPE-03 |
| Band word space | | about 0.0111 | 3.38 mm | 2.82 mm | TYPE-03 |
| Diamonds at 90/180/270 deg | rotated to path, on band centre line | 0.01527 tall | 4.65 mm | 3.88 mm | SEAL-05/08 |
| ring2 stroke | 1 unit | 0.00417 | 1.27 mm / 3.60 pt | 1.06 mm / 3.00 pt | PRINT-01, LINE-02 |
| ring2 centre-line radius | unchanged | 0.41168 | 125.48 mm | 104.57 mm | |
| ring2 inner edge radius | | 0.40960 | 124.85 mm | 104.04 mm | |
| Inner arcs centre-line radius (both) | | 0.36654 | 111.72 mm | 93.10 mm | TYPE-06 |
| PECULIAR PEOPLE cap height | | 0.03428 | 10.45 mm / 29.62 pt | 8.71 mm / 24.68 pt | RATIO-03 |
| PECULIAR PEOPLE thinnest stroke | | 0.00280 (12 in only: 0.00233) | 0.85 mm (now 0.79) | 0.71 mm | PRINT-02 |
| PECULIAR PEOPLE clearance each ring | = band clearance | 0.02592 | 7.90 mm | 6.58 mm | COMP-04 |
| EST cap height | | 0.01770 | 5.39 mm | 4.50 mm | RATIO-03 |
| EST period, on baseline | min dimension | 0.00394 (12 in only: 0.00328) | 1.20 mm | 1.00 mm | PRINT-04 |
| ring3 outer edge radius | | 0.32348 | 98.60 mm | 82.16 mm | COMP-04 |
| ring3 stroke | 2 units | 0.00835 | 2.55 mm / 7.21 pt | 2.12 mm / 6.01 pt | LINE-02 |
| Inner field diameter | | 0.63026 | 192.10 mm | 160.09 mm | RATIO-05 ref |
| Temple art width | current, up to | 0.3679 to 0.3838 | 112.1 to 117.0 mm | 93.5 to 97.5 mm | SEAL-07, PRINT-09 |
| Art+caption block centre | above ring centre | 0.01200 | 3.66 mm | 3.05 mm | COMP-02 |
| Art to caption gap | | 0.01390 | 4.24 mm | 3.53 mm | COMP-04 |
| UTAH, USA cap height | | 0.01770 | 5.39 mm | 4.50 mm | PRINT-01, RATIO-03 |

Build notes: expand all strokes and type, use no clipping masks, deliver a true vector, then flatten to the Tapstitch PNG with every pixel fully ink or fully clear.

## Passed

- **Layout and type:**
  - COMP-01: ink bbox and outer ring offsets are 0, 0.
  - TYPE-01: caption spacing 0.403 vs top word 0.175.
  - TYPE-02: 3 text levels.
  - TYPE-03: band CV is 14.9 percent with the diamonds excluded, and the crops look even. EST 7.1, PECULIAR PEOPLE 13.6.
  - TYPE-04: EST reads left to right, upright.
  - TYPE-05: arcs are off axis by only 0.0 / 0.17 / 0.08 / 0.02 deg.
  - TYPE-08: bottom text tracked looser (0.391 vs 0.25).
  - TYPE-09: no letters are distorted.
- **Seal and line weights:**
  - SEAL-03: weights rank 47.88 > 29.9 > 8.9, with steps of 1.60x and 3.36x.
  - SEAL-06: art clearance 217.83 px and caption clearance 130.72 px are both above the smallest text clearance (67.51 px).
  - LINE-03: outer ring is heaviest.
  - LINE-04: 1.05x.
- **Recognition:**
  - LOGO-02: the top word is readable at 2 in; the silhouette holds at 1 in.
  - LOGO-03 / PRINT-06: 0 tint pixels.
  - LOGO-04: the temple block is the shape that stands out.
  - LOGO-05: the dividers do not collide with the letters.
  - COMP-06 / TEST-01: the top word stays distinct at 1 percent blur and the temple at 2 percent.
  - TEST-03 (approximation): the top word and temple are what you name first.
- **Print:**
  - PRINT-05: minimum 13.2 pt.
  - PRINT-07: both widths are in range.
  - Ring gaps of 202 and 266 px are far above every gap floor.
  - Diamonds and bullets are at least 1.67 mm.
- **Report only:**
  - RATIO-05: 0.604 D now, 0.630 D after the rebuild.
  - SEAL-07: art is 60.9 percent of the field wide and 69.5 percent high.
  - TEST-07: cap heights at 10/12 in are 0.343/0.411, 0.177/0.213, 0.160/0.192 and 0.125/0.150 in.

## Not checked

- LOGO-06: art style is locked.
- COMP-03: no number given.
- TYPE-10: EST is subordinate, not a pair.
- PRINT-10, LINE-05: these are rebuild steps.
- PRINT-11: covered by PRINT-01.
- TEST-06: do a 1:1 paper print at the chosen width as the last step.
- RATIO-01/02/04: FOLKLORE.
- All art-dependent numbers are measured on the stand-in only.

## Previews looked at

- **onecolour:** clean; upright side diamonds and the raised period are visible.
- **small_2in / small_1in:** see LOGO-02.
- **blur_0.5/1/2pct:** expected hierarchy. Bright spots at 12, 3, 6 and 9 o'clock are a preview edge artefact.
- **print_flags_10in_dtg_fail:** all small type, ring2 and most of the art are red; PECULIAR PEOPLE only on its serifs.
- **print_flags_10in_screen_transfer_fail:** windows and the notches in A, N and Y are yellow.
- **Other overlays:** same pattern, smaller in extent.
- **spread_10in/12in:** barely visible except on the hatching.
- **Crops:** crop_bottom_arc_est, crop_divider_left/right/bottom, crop_band_315/045, crop_band_narrowest_gap, crop_band_widest_gap, crop_band_end_right, crop_top_word (the black strip is the crop running off the canvas), crop_caption, crop_art_base_lines, crop_red_art_dtg10, crop_yellow_art_st10, crop_gap_r2r3_left/right.
