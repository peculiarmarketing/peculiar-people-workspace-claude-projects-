# Design audit rule library

61 rules in eight groups. Built 7 October 2026 from the research in
`research/design-audit/` (project root):

- `written-sources.md`: 71 written sources, cited here as **W1 to W71**.
- Ten video folders, each with `SPEC.md`, cited here as **V:folder-name**
  (for example V:spoon-vintage-badge-logo). The videos were read from captions and
  storyboard thumbnails by one reader (no Gemini pass, no full frames; see
  `METHOD.md`), so a video alone never makes a rule ESTABLISHED.

**Confidence labels**

- **ESTABLISHED**: at least two independent sources agree (a vendor's blog and the
  same vendor's video count as one).
- **SINGLE SOURCE**: one source, or several that trace to one origin. Use it, label it
  in the report, and never rank a finding as "breaks print" on it alone.
- **FOLKLORE**: widely repeated, not supported, or contradicted by evidence. The audit
  never fails a design for breaking a FOLKLORE rule; it may note that a claim about
  the design rests on one.
- Some rules carry **CONFLICT** on the number: the direction is established, and
  sources disagree on the value. The audit uses a fail level and a warn level.

**Audit tolerances** (marked *tolerance*) are this skill's own pass bands for
measured values where no source gives a number. They are settings, not research,
and live in this file so they can be changed.

**Fields** for every rule: statement; why; check (script key or visual step);
threshold; sources; confidence.

## Contents

1. LOGO: logo and emblem fundamentals (LOGO-01 to LOGO-06)
2. COMP: composition and spacing (COMP-01 to COMP-07)
3. RATIO: ratios and proportion (RATIO-01 to RATIO-05)
4. TYPE: typography (TYPE-01 to TYPE-11)
5. LINE: line work (LINE-01 to LINE-05)
6. SEAL: circular seals and badges (SEAL-01 to SEAL-08)
7. PRINT: screen print, DTF and DTG constraints (PRINT-01 to PRINT-12)
8. TEST: golden rules and tests (TEST-01 to TEST-07)

Confidence count: 44 ESTABLISHED (5 of them derived arithmetic or geometry from ESTABLISHED rules: SEAL-02, SEAL-04, SEAL-07, PRINT-08, PRINT-09), 14 SINGLE SOURCE, 3 FOLKLORE. Tally at the end.

---

## 1. LOGO: logo and emblem fundamentals

### LOGO-01 Simplicity: every element earns its place
- **Statement:** Each element must help identify or read the mark; complexity is a cost.
- **Why:** "A design that is complex, like a fussy illustration or an arcane abstraction, harbors a self-destruct mechanism" (Rand). Detail that cannot be seen at viewing distance or print size adds noise and print risk.
- **Check:** Visual. List every element (rings, band text, dividers, arcs, art, caption) and say what each contributes. Pair with TEST-05.
- **Threshold:** None (judgement).
- **Sources:** W18, W20, W22; V:futur-legibility-hierarchy-contrast, V:satori-13-golden-rules.
- **Confidence:** ESTABLISHED.

### LOGO-02 Small-size test at about 1 inch
- **Statement:** A mark should stay recognisable at about 1 in wide; if the full version cannot, make a simplified small version (drop outer text first).
- **Why:** Marks are reused small (neck labels, hats, favicons). Encircling text is the first thing to become illegible.
- **Check:** Look at `small_1in.png` and `small_2in.png`. Can you read the largest word? Is the art still a recognisable building silhouette?
- **Threshold:** Largest word legible at 2 in; silhouette recognisable at 1 in. For a back-print seal that will never be used small, a failure here is **polish** plus a recommendation for a small version, not a print failure.
- **Sources:** W19, W20, W21, W22.
- **Confidence:** ESTABLISHED.

### LOGO-03 One colour, no tints
- **Statement:** The mark must reproduce in one solid colour, with no tints, gradients or semi-transparent pixels.
- **Why:** One-colour reproduction is the baseline test of a logo, and on DTG a semi-transparent pixel gets a solid white underbase and prints as a chalky halo.
- **Check:** `measurements.json` `tones.tint_pixels` and `tones.tint_pct_of_ink`; look at `onecolour.png`.
- **Threshold:** 0 tint pixels in a print file. Anti-aliased edge pixels in a raster preview are normal. In a final print PNG every pixel must be fully ink or fully clear (BRAND.md section 8 flatten rule).
- **Sources:** W18, W20, W59 (halo mechanism, SINGLE SOURCE); V:futur-legibility-hierarchy-contrast, V:satori-13-golden-rules.
- **Confidence:** ESTABLISHED (one colour); the DTG halo mechanism is SINGLE SOURCE.

### LOGO-04 One distinctive feature
- **Statement:** Strong marks have one feature that makes them recognisable from the silhouette alone.
- **Why:** Recognition happens on shape before detail.
- **Check:** `blur_2pct.png`: is one feature (for the seal, the temple silhouette or the top word) clearly the thing you notice?
- **Threshold:** None.
- **Sources:** W19 and W20 (both Airey). Rand (W18) supports "muddled is less memorable", not the single-feature claim.
- **Confidence:** SINGLE SOURCE.

### LOGO-05 Graphic elements reinforce legibility, never just decorate
- **Statement:** Graphic devices should make the mark read better; cutting into letters or swapping terminals can change what a word says.
- **Why:** An ornament that turns a letter into a symbol changes the reading (The Futur's HUDLUM example).
- **Check:** Visual. Do dividers, rules or flourishes collide with letters or read as letters?
- **Threshold:** None.
- **Sources:** V:futur-legibility-hierarchy-contrast.
- **Confidence:** SINGLE SOURCE.

### LOGO-06 Mark and type share one character
- **Statement:** The illustration and the typefaces should feel like one design (no soft mark with a rigid serif, no terminal from another family).
- **Why:** Mismatched character reads as assembled from parts.
- **Check:** Visual. Compare the art's line quality with the type's stroke contrast and serif style.
- **Threshold:** None.
- **Sources:** V:satori-13-golden-rules, V:futur-legibility-hierarchy-contrast.
- **Confidence:** SINGLE SOURCE (two videos, both asserted rather than demonstrated).

## 2. COMP: composition and spacing

### COMP-01 Centred in the canvas
- **Statement:** The design's ink is centred in the file, horizontally and vertically.
- **Why:** BRAND.md section 8: designs are centred in the print area, and every size is measured ink to ink. An off-centre file prints off-centre.
- **Check:** `centring.bbox_offset_from_canvas` (px); for a seal also `centring.outer_ring_offset_from_canvas`.
- **Threshold:** *tolerance* within 0.25 percent of the ink width on each axis.
- **Sources:** BRAND.md section 8 (house rule); W16, W17.
- **Confidence:** ESTABLISHED (as house rule plus badge practice).

### COMP-02 Optical centre sits slightly above geometric centre
- **Statement:** A block centred in a field should sit slightly above the mathematical centre; it must never sit below it.
- **Why:** The eye places the centre of a field above its geometric middle, so a block that is mathematically centred looks low, and one with a heavy base looks lower still.
- **Check:** `centre.art_plus_caption.bbox_center_offset[1]` and `centre.art.mass_center_offset[1]` (positive is below centre), against `centre.inner_diameter_px`.
- **Threshold:** FAIL (polish) if the art-plus-caption block's centre is below the ring centre by more than 1 percent of the inner diameter. Target: 0 to 5 percent of the field height above centre. The 5 percent figure is SINGLE SOURCE (W27, a framers' forum); the direction is ESTABLISHED.
- **Sources:** W23, W24, W25, W26; W27 for the number; V:draper-golden-ratio (asserted only).
- **Confidence:** ESTABLISHED (direction), SINGLE SOURCE (number).

### COMP-03 Optical size: round and pointed shapes overshoot
- **Statement:** Round and pointed shapes must be drawn slightly larger than flat ones to look equal (O, C, S overshoot the cap line; a diamond looks smaller than a square of the same height).
- **Why:** Optical weight is not pixel size; at equal size a square looks biggest, a triangle next, a circle smallest.
- **Check:** Visual crop of round letters next to flat ones, and of divider glyphs next to cap letters.
- **Threshold:** None given by any source (the commonly quoted 1 to 3 percent of cap height is FOLKLORE here).
- **Sources:** W23; V:graftalks-optical-sizing (demonstrated on slides).
- **Confidence:** ESTABLISHED.

### COMP-04 Repeated spacing is consistent
- **Statement:** Gaps that play the same role (ring to text, text to ring, art to ring) are equal or follow one deliberate ratio.
- **Why:** Unequal gaps that should match read as mistakes; consistent gaps read as built.
- **Check:** `ring_gaps[*].mean_px`, each arc's `gap_to_outer_ring_px` and `gap_to_inner_ring_px`, `centre.art.clearance_px`. Compare gaps that serve the same role.
- **Threshold:** *tolerance* gaps meant to match within 10 percent of each other.
- **Sources:** V:spoon-vintage-logo-typography ("roughly the same" spacing, demonstrated); W7 (consistent ratio as a tool, for type sizes).
- **Confidence:** SINGLE SOURCE (as a spacing rule).

### COMP-05 Isolation and density add visual weight
- **Statement:** An element with more surrounding space, or denser detail, reads heavier.
- **Why:** This decides what the eye lands on first. A dense drawing in a small field outweighs larger but sparse type.
- **Check:** Compare `centre.art` coverage and size with the arcs; confirm with the blur test (TEST-01).
- **Threshold:** None.
- **Sources:** W28.
- **Confidence:** SINGLE SOURCE.

### COMP-06 Hierarchy is the order things are seen
- **Statement:** The intended reading order (for the seal: outer ring frame, top word, temple, band text, small text) must match the visual order.
- **Why:** If the hierarchy is wrong, the mark says something other than what was intended.
- **Check:** `blur_1pct.png` and `blur_2pct.png`; TEST-01.
- **Threshold:** The two most important elements remain distinct blobs at 2 percent blur.
- **Sources:** W65, W66; W3 (levels).
- **Confidence:** ESTABLISHED.

### COMP-07 One vertical axis
- **Statement:** In a symmetric layout every element shares one vertical axis.
- **Why:** A few pixels of axis drift between the art, the caption and the arcs is visible because the eye compares them directly.
- **Check:** `centre.art.bbox_center_offset[0]`, `centre.caption.center_x_offset`, the arcs' `mid_offset_from_axis_deg`.
- **Threshold:** *tolerance* within 0.5 percent of the inner diameter horizontally. Asymmetric art (a temple drawn in 3/4 view) is judged on its visual mass, not its bounding box: report both.
- **Sources:** V:spoon-vintage-logo-typography (key object centring, demonstrated); W17.
- **Confidence:** ESTABLISHED.

## 3. RATIO: ratios and proportion

### RATIO-01 The golden ratio is not a quality test
- **Statement:** Never fail or praise a design for matching or missing 1.618; golden-circle overlays prove nothing.
- **Why:** Devlin's experiments found preferred rectangles "always random"; the aesthetic claim traces to a misattribution of Pacioli and to Zeising. Measurements of the Apple logo, the classic example, range from 1.53 to 1.73 depending on how they are taken, and its designer says he worked freehand. "Literally any shape" can be built from golden shapes at some scale.
- **Check:** If anyone (a brief, an AI generator, a mockup) claims the design uses the golden ratio, note that the claim is decorative.
- **Threshold:** None. A golden-ratio claim is never evidence.
- **Sources:** W29, W30, W31, W32, W33, W34; V:draper-golden-ratio.
- **Confidence:** FOLKLORE (the beauty claim). Designers who use it do so as one arbitrary proportion among many, chosen before or after the fact.

### RATIO-02 Rule of thirds as a law
- **Statement:** Not applied. It is irrelevant to a centred circular seal and weakly supported in general.
- **Why:** In large sets of rated images it "seems to play only a minor, if any, role".
- **Check:** None.
- **Threshold:** None.
- **Sources:** W35.
- **Confidence:** FOLKLORE.

### RATIO-03 Type sizes come from one consistent ratio
- **Statement:** Pick the sizes of the text levels from one scale (any ratio), and use the smallest step that is visibly different.
- **Why:** A consistent scale makes sizes look related. Steps that are too close look like errors.
- **Check:** Ratios of `cap_height_px` between arcs and the caption.
- **Threshold:** Adjacent levels at least 1.15x apart (one step of the classic 2^(1/5) printer's scale, derived from W6). Steps between levels should be similar (*tolerance*: within 25 percent of each other).
- **Sources:** W6, W7, W3; Bringhurst via W6 and W7.
- **Confidence:** ESTABLISHED (as a tool).

### RATIO-04 Any specific ratio is "correct"
- **Statement:** Not applied. 1.25, 1.333, 1.5 and 1.618 are all tools; none is better.
- **Why:** No designer source argues one ratio wins; Tim Brown: "modular scales are a tool, they're not magic".
- **Check:** None.
- **Threshold:** None.
- **Sources:** W6, W7.
- **Confidence:** FOLKLORE.

### RATIO-05 Seal field proportion (reference only)
- **Statement:** Regulated two-ring seals put the inner field at 0.63 to 0.67 of the outer diameter, with a text band 17 to 19 percent of the diameter.
- **Why:** It is the only published numeric seal convention. It is a reference, not a rule: a seal with two text zones will have a smaller field.
- **Check:** `centre.inner_diameter_px` / (2 x `rings[0].r_outer`).
- **Threshold:** Report only. Never FAIL on it.
- **Sources:** W68, W69 (four US states).
- **Confidence:** ESTABLISHED (for regulated seals).

## 4. TYPE: typography

### TYPE-01 Track all caps 5 to 10 percent of the type size
- **Statement:** Text in capitals gets 5 to 10 percent of the point size in extra letterspacing (up to 12 percent); smaller sizes get more, display sizes less.
- **Why:** Capitals are designed to sit next to lower case; set together they crowd and lose word shape.
- **Check:** Tracking cannot be read from pixels (side bearings are unknown). Instead compare `letter_gap_to_cap` between arcs: the smaller text must have the larger ratio. Visual crop for crowding.
- **Threshold:** The smallest text's `letter_gap_to_cap` must be at least that of the largest text. For the rebuild: 50 to 100 tracking units (Illustrator, 1/1000 em) on the small caps, 0 to 50 on the large bold caps, then adjust for the curve (TYPE-08).
- **Sources:** W1, W2, W5, W8, W12; V:spoon-vintage-logo-typography (tracking 400 on one small line: one value, not a rule).
- **Confidence:** ESTABLISHED.

### TYPE-02 At most three text levels
- **Statement:** Use no more than three type sizes (two is better), each a visible step apart.
- **Why:** More levels blur the hierarchy.
- **Check:** Count distinct cap heights among arcs and caption (cluster within 15 percent).
- **Threshold:** FAIL (hurts legibility) at four or more levels.
- **Sources:** W3, W6, W7; V:spoon-vintage-logo-typography (three-level hierarchy demonstrated).
- **Confidence:** ESTABLISHED.

### TYPE-03 Even spacing along each arc
- **Statement:** One tracking value per arc, then manual kerning: font kerning tables are built for straight lines and go wrong on curves.
- **Why:** Uneven gaps on a curve read as mistakes, and the curve magnifies pairs like LA, RA, T and E.
- **Check:** Each arc's `letter_gap_cv_pct`; crop the widest and narrowest gaps with `crop.py --polar`.
- **Threshold:** *tolerance* above 25 percent: look closely. Letter shapes (A, L, T, Y) vary the bounding-box gap even when spacing is optically right, so confirm by eye before calling it.
- **Sources:** W10, W11 (need for manual kerning); W9.
- **Confidence:** ESTABLISHED (the need); the tolerance is the skill's own.

### TYPE-04 The bottom arc reads left to right, upright
- **Statement:** Text on the bottom of a circle is flipped so it reads left to right, the right way up, with glyph tops toward the centre.
- **Why:** Continuing the top text around the circle puts the bottom words upside down.
- **Check:** Visual: `crop.py --polar <cx> <cy> 180 <r> <half>`.
- **Threshold:** Binary.
- **Sources:** W15, W16; V:pixelbracket-type-around-circle, V:spoon-vintage-badge-logo (both demonstrated).
- **Confidence:** ESTABLISHED.

### TYPE-05 Arcs are centred on the vertical axis
- **Statement:** The top arc's midpoint sits at 12 o'clock and the bottom arc's at 6 o'clock.
- **Why:** An arc rotated even a degree reads as tilted against the symmetric frame.
- **Check:** Each arc's `mid_deg` and `mid_offset_from_axis_deg`.
- **Threshold:** *tolerance* within 0.5 degrees, or within half a letter gap of arc length, whichever is larger. An optical nudge for a word ending in a wide letter is allowed (COMP-03).
- **Sources:** W15, CreativePro (via W summary); V:pixelbracket-type-around-circle.
- **Confidence:** ESTABLISHED.

### TYPE-06 Centre-align type to its path
- **Statement:** Align curved text to the centre of the path. Top and bottom arcs that share a band sit on one centre-line radius.
- **Why:** Baseline-aligned text bunches its tops on concave curves and spreads them on convex ones; centre alignment gives the most even spacing. Arcs on two different radii make the band look lopsided.
- **Check:** `targets.json` row "radial centre of both arcs"; each arc's `r_glyph_min` and `r_glyph_max`.
- **Threshold:** *tolerance* the two arcs' radial centres within 2 percent of the band width.
- **Sources:** W11, CreativePro (via summary); V:pixelbracket-type-around-circle.
- **Confidence:** ESTABLISHED.

### TYPE-07 Small type needs a sturdy, low-contrast face
- **Statement:** Small caps in a seal need a face with low stroke contrast and sturdy serifs: every hairline must clear the print minimum (PRINT-02).
- **Why:** Small optical sizes are drawn with less contrast for a reason. Thin hairlines vanish or break in print.
- **Check:** Each arc's `stroke_px.hairline_px` against `stroke_px.stem_px`; `print_check.json` hairline rows.
- **Threshold:** Hairline at or above the method's line minimum (PRINT-01). A stem-to-hairline ratio above 3:1 in the smallest text is a warning sign.
- **Sources:** W13, W14, W50; V:transferexpress-dtf-art-guidelines ("font stems count as lines").
- **Confidence:** ESTABLISHED.

### TYPE-08 Inside text crowds, outside text fans out
- **Statement:** Text set inside a circle (concave) crowds, so it needs looser tracking; text set outside (convex) fans out and may need tighter tracking.
- **Why:** The letter tops sit on a shorter or longer arc than the baseline.
- **Check:** Compare `letter_gap_to_cap` of the bottom arc with the top arc of similar size.
- **Threshold:** Direction only. Peters' example (-75 outside, +50 inside) is for one face (SINGLE SOURCE).
- **Sources:** W9, W11.
- **Confidence:** ESTABLISHED.

### TYPE-09 Fill an arc with tracking, not distortion
- **Statement:** Make text fill its arc by tracking; never stretch, warp or squash the letters to fit.
- **Why:** Distorted letterforms read as cheap and break stroke consistency.
- **Check:** Visual crop. Are letters a consistent width-to-height?
- **Threshold:** Binary.
- **Sources:** V:spoon-vintage-badge-logo (rejected a distorting warp on screen).
- **Confidence:** SINGLE SOURCE.

### TYPE-10 Paired top and bottom text match
- **Statement:** When the top and bottom arcs are a pair (same role), use the same size and style.
- **Why:** Pairs that differ look like a mistake. This does not apply when the bottom line is deliberately subordinate (a date under a name).
- **Check:** Compare cap heights of the top and bottom arcs in the same band.
- **Threshold:** Applies only when the brief says the arcs are a pair.
- **Sources:** V:pixelbracket-type-around-circle.
- **Confidence:** SINGLE SOURCE.

### TYPE-11 Legibility comes first
- **Statement:** Legibility supersedes every other consideration in a logo.
- **Why:** A mark that cannot be read cannot be remembered or said aloud.
- **Check:** Combine TYPE-07, PRINT-05 and LOGO-02.
- **Threshold:** None of its own.
- **Sources:** V:futur-legibility-hierarchy-contrast (verbatim); W18 (simplicity, in spirit).
- **Confidence:** SINGLE SOURCE (as stated).

## 5. LINE: line work

### LINE-01 Consistent stroke weight within an element class
- **Statement:** Every ring keeps one width all the way round; all lines of one role share one weight.
- **Why:** Weight wobble reads as hand error or a bad trace, not intent.
- **Check:** `rings[*].width_cv_pct`; `rings[*].width` (min to max).
- **Threshold:** *tolerance* `width_cv_pct` at or under 3 percent, or under `width_cv_noise_floor_pct` (whichever is larger: thin rings cannot be measured more finely than about half a pixel). A true vector ring is 0. Above 5 percent, and above the noise floor, is visible.
- **Sources:** W39, W16, W17; V:spoon-vintage-badge-logo.
- **Confidence:** ESTABLISHED.

### LINE-02 Few weights, roughly doubling (1:2:4)
- **Statement:** Use three weights (four at most), each step about double the last; adjacent weights closer than about 1.4x do not read as different.
- **Why:** It is the technical-drawing hierarchy (ISO pens 0.18, 0.35, 0.70 mm). Weights that are nearly equal look like errors.
- **Check:** The ring widths (`rings[*].width_mean`) and the art clusters (`centre.art.weights`) together: list the distinct weights and the ratios between neighbours.
- **Threshold:** Neighbours at least 1.4x apart; no more than four distinct weights across rings and art. Target for a rebuild: 1:2:4 (`targets.py`).
- **Sources:** W36, W37, W38. Applying it to logos is an analogy, not a sourced logo rule.
- **Confidence:** ESTABLISHED (in technical drawing).

### LINE-03 The border outweighs the interior
- **Statement:** The outer frame is the heaviest line; interior detail is lighter; the finest art line is the thinnest thing in the mark and still above the print minimum.
- **Why:** The heavy profile line holds the shape together and stops the edge dissolving.
- **Check:** `rings[0].width_mean` against the other rings and `centre.art.weights[-1]`.
- **Threshold:** Outer ring heaviest; ring order matches the design's intent.
- **Sources:** W38, W17.
- **Confidence:** ESTABLISHED (weakly: one technical summary, one tutorial).

### LINE-04 Rings relate to the art's own weights
- **Statement:** When the art is fixed, rings take their weights from it: the thinnest ring about equal to the art's heaviest line, the others in the LINE-02 steps above it.
- **Why:** A ring lighter than the art's lines looks like an afterthought; one far heavier swamps it. Anchoring the rings on the art keeps one system.
- **Check:** `targets.json` `anchor`.
- **Threshold:** Thinnest ring between 1x and 2x the art's heaviest weight (*tolerance*), and never under the print floor.
- **Sources:** Derived from LINE-02 and LINE-03 (W36, W37, W38).
- **Confidence:** SINGLE SOURCE (derived).

### LINE-05 Expand strokes before scaling and before print
- **Statement:** Convert strokes and type to filled outlines before scaling or sending to print.
- **Why:** A live stroke keeps its weight while the shape scales, so a ring's proportion changes when the art is resized (demonstrated at 10 in by Golden Press).
- **Check:** For a vector rebuild, a step in the fix list. Not measurable on a raster.
- **Threshold:** Binary.
- **Sources:** W58; V:goldenpress-designing-for-screenprint (demonstrated).
- **Confidence:** ESTABLISHED.

## 6. SEAL: circular seals and badges

### SEAL-01 Rings are concentric
- **Statement:** Every ring shares the outer ring's centre.
- **Why:** An off-centre ring makes the gap beside it change around the circle, and the eye picks up a gap change of a few percent.
- **Check:** `rings[*].offset_from_outer_px`; the min and max in `ring_gaps`.
- **Threshold:** FAIL (polish) if the offset is at least 1 analysis px and makes the neighbouring gap vary by more than 3 percent (*tolerance*). Target in a rebuild: 0.
- **Sources:** W16, W17; V:spoon-vintage-badge-logo (centring checked in outline mode).
- **Confidence:** ESTABLISHED.

### SEAL-02 Ring gaps are uniform around the circle
- **Statement:** The gap between two rings is the same width all the way round.
- **Why:** This is the visible symptom of SEAL-01 and LINE-01 failures.
- **Check:** `ring_gaps[*].min_px` and `max_px`.
- **Threshold:** *tolerance* (max - min) / mean at or under 3 percent.
- **Sources:** Derived from SEAL-01.
- **Confidence:** ESTABLISHED (derived from an ESTABLISHED rule).

### SEAL-03 Ring weights rank as intended
- **Statement:** The ring weights follow a clear, intended order (here: outer thick, inner heavier, thin ring lightest), with the steps in LINE-02.
- **Why:** If two rings are close in weight, the eye cannot tell which is meant to dominate.
- **Check:** `rings[*].width_mean` ratios.
- **Threshold:** As LINE-02.
- **Sources:** W38, W17; V:spoon-vintage-badge-logo ("a much broader stroke" on the outer ring).
- **Confidence:** ESTABLISHED.

### SEAL-04 Band text is centred in its band
- **Statement:** Text in a band has equal clearance to the ring outside it and the ring inside it, measured on the cap height.
- **Why:** This follows from centre alignment (TYPE-06). Text that crowds one ring makes the band look lopsided.
- **Check:** Each arc's `gap_to_outer_ring_px`, `gap_to_inner_ring_px` and `outer_to_inner_gap_ratio`.
- **Threshold:** *tolerance* ratio between 0.9 and 1.1 for a band holding one text line. In a zone holding a top word and a bottom line, apply TYPE-06 instead.
- **Sources:** W11 (derived); no source gives cap height as a fraction of band width.
- **Confidence:** ESTABLISHED (derived).

### SEAL-05 Dividers are consistent and placed symmetrically
- **Statement:** Divider glyphs (dots, diamonds, stars) are one glyph at one size, centred on the text's centre line, and placed symmetrically (for example at 3, 9 and 6 o'clock).
- **Why:** Dividers are punctuation for the ring. Mismatched sizes or positions break the symmetry the circle sets up.
- **Check:** Arcs with `kind: "ornament"`: `mid_deg`, `offset_from_band_center_line_px`, and `radial_extent_px` against `tangential_extent_px` (the same shape should give the same pair at every position; swapped values mean an upright glyph that was not rotated to the path). Visual crop for glyph match.
- **Threshold:** *tolerance* positions within 0.5 degrees of their symmetric angle; radial centre within 5 percent of the band width of the text centre line.
- **Sources:** V:pixelbracket-type-around-circle (dots at 3 and 9 o'clock), V:spoon-vintage-badge-logo (stars mirrored about the centre).
- **Confidence:** SINGLE SOURCE (practice shown in videos).

### SEAL-06 Centre art has breathing room
- **Statement:** The art clears the inner ring by at least the clearance used elsewhere in the seal, and the art-plus-caption block sits optically centred (COMP-02).
- **Why:** Art that nearly touches the ring reads as cramped and fights the frame.
- **Check:** `centre.art.min_radial_clearance_px` and `centre.art.clearance_px`, against the band clearances in `zones`.
- **Threshold:** *tolerance* minimum art clearance at least equal to the smallest text-to-ring clearance in the seal.
- **Sources:** Derived from COMP-04; W28 (isolation).
- **Confidence:** SINGLE SOURCE (derived).

### SEAL-07 Centre art size in the field
- **Statement:** Report the art's width and height as a share of the inner diameter.
- **Why:** The art's size inside the seal sets its physical print size (PRINT-09).
- **Check:** `centre.art.width_pct_of_inner_diameter` and `height_pct_of_inner_diameter`.
- **Threshold:** Report only.
- **Sources:** Measurement.
- **Confidence:** ESTABLISHED (as measurement; no rule threshold).

### SEAL-08 A rebuild centres each arc on the ring's own centre
- **Statement:** Text paths are circles concentric with the rings, on a radius chosen for centre alignment; rotate ornaments about the same centre.
- **Why:** AI-generated or freehand arcs drift off the ring centre, so letters lean in and out.
- **Check:** For a rebuild, part of the spec. On a raster: does the arc's `r_glyph_min` vary around the arc in a crop? (Visual.)
- **Threshold:** Binary in the rebuild.
- **Sources:** V:spoon-vintage-badge-logo (text on a separate circle, stars rotated about the centre), V:pixelbracket-type-around-circle.
- **Confidence:** SINGLE SOURCE (two videos showing one practice, no written source).

## 7. PRINT: screen print, DTF and DTG constraints

Numbers live in `print_thresholds.json` (fail and warn per method), which the
scripts read. Tapstitch prints DTG on the tee and DTF on the fleece (BRAND.md section 7).
No public Tapstitch artwork spec was found, so the jacket method is unknown: audit
all methods and treat the strictest as binding until Tapstitch confirms.

### PRINT-01 Minimum positive line
- **Statement:** Every printed stroke is at least the method's minimum line.
- **Why:** Lines below it fill or break on the screen, lack adhesive mass on DTF and peel or crack in wash, or lose their white underbase on DTG and print translucent or ghosted. A thin line can look fine new and still fail after washing.
- **Check:** `print_check.json` element rows with rule PRINT-01, plus `morphology.fail.thin_strokes` and the red pixels in `print_flags_<w>in_<method>_fail.png`.
- **Threshold (fail / warn):** screen 0.35 / 0.50 mm; screen transfer 0.30 / 0.35 mm; DTF 0.50 / 1.00 mm; DTG on dark 0.71 / 1.06 mm.
- **Sources:** screen W40, W43, W45, W49; DTF W42, W52, W55, W50 (absolute) and W50, W51, W53 (production-safe); DTG W57, W44, W58; V:transferexpress-dtf-art-guidelines.
- **Confidence:** ESTABLISHED (each method's floor). The warn levels for screen are a margin, not a source.

### PRINT-02 Type hairlines and serifs count as lines
- **Statement:** The thinnest stroke inside a letter (hairline, serif, crossbar) must clear the line minimum, not just the stem.
- **Why:** Hairlines are what break first. Small serif caps usually fail here before they fail on size.
- **Check:** Hairline rows in `print_check.json`; red pixels on letters in the overlays.
- **Threshold:** As PRINT-01.
- **Sources:** V:transferexpress-dtf-art-guidelines ("font stems count as lines"); W50; W14.
- **Confidence:** ESTABLISHED.

### PRINT-03 Minimum gap, and gaps close outward on white-on-dark
- **Statement:** Open space between printed elements (counters, letter gaps, the gap between art lines) must be wider than the minimum gap, which is larger than the minimum line.
- **Why:** Ink spreads on fabric, and again under heat and pressure for transfers, so small counters and gaps close ("closure", the inside of an O). With white ink on navy the white is the ink, so it spreads outward into the navy. Thickening lines to pass PRINT-01 can make this worse.
- **Check:** Gap rows in `print_check.json`; `morphology.*.closing_gaps`; the yellow pixels in the overlays.
- **Threshold (fail / warn):** screen 0.53 / 0.71 mm (CONFLICT 1.5 to 2.9 pt across sources); screen transfer 1.02 / 1.02 mm; DTF none / 1.0 mm (CONFLICT); DTG none / 0.71 mm (no DTG source: borrowed from screen, ASSUMPTION).
- **Sources:** W40, W41, W44, W45, W50, W53; V:transferexpress-dtf-art-guidelines; W14 (spread direction).
- **Confidence:** ESTABLISHED (gap larger than line, and the mechanism); CONFLICT on the number.

### PRINT-04 Small isolated shapes lift on DTF
- **Statement:** Small separate shapes (divider dots, specks, detached serif tips, stray pixels) are the first parts of a DTF print to peel.
- **Why:** The adhesive bond of a small area is weaker than the peel force, and stretch concentrates stress on narrow parts.
- **Check:** `print_check.json` `smallest_shapes` (mm² and largest dimension at each width).
- **Threshold:** Any shape whose largest dimension is under the DTF line minimum (0.5 mm) is a FAIL: it is a speck that will not transfer. Shapes under 1 mm are a WARN. Specks in the art are trace noise to clean, not art changes.
- **Sources:** W50, W51, W55.
- **Confidence:** ESTABLISHED.

### PRINT-05 Minimum text size
- **Statement:** Text should be at least 10 pt (warn) and never under 7 pt (fail), estimated from cap height.
- **Why:** Below this, letters fill in or break, and the hairline rule fails first anyway.
- **Check:** Rows with rule PRINT-05 (`est_font_pt`, estimated as cap height / 0.68).
- **Threshold:** fail under 7 pt, warn under 10 pt. Reversed (knocked-out) text on screen-printed transfers needs 18 pt (V:transferexpress-dtf-art-guidelines), which does not apply to positive white type.
- **Sources:** W50, W53, W54, W56, W57 (CONFLICT, 4 to 18 pt).
- **Confidence:** ESTABLISHED that a floor exists; CONFLICT on the value.

### PRINT-06 No halftones, tints or soft edges in the print file
- **Statement:** A one-colour line print has only fully inked and fully clear pixels: no halftone, no tint, no feathered edge.
- **Why:** On DTG a part-transparent pixel gets a full white underbase (chalky halo). On DTF and screen, tints become halftone dots that need their own minimums (45 to 65 LPI on DTF). BRAND.md section 8 already flattens print files.
- **Check:** `tones.tint_pixels`; LOGO-03.
- **Threshold:** 0 tint pixels in the final print file.
- **Sources:** W59 (SINGLE SOURCE on the halo), W46, W47, W60, W61; BRAND.md section 8.
- **Confidence:** ESTABLISHED.

### PRINT-07 Back print width
- **Statement:** A full back print is 10 to 14 in wide, 12 in by default; it must also fit the garment's back print area height.
- **Why:** These are the industry placements; small garments may need the narrower size.
- **Check:** The audited widths; `design_height_in` in `print_check.json` against the garment's print area (BRAND.md section 8 lists back areas; the narrowest is 18.4 in tall).
- **Threshold:** Width 10 to 14 in; height inside the print area.
- **Sources:** W62, W63; BRAND.md section 8.
- **Confidence:** ESTABLISHED.

### PRINT-08 Audit at the smallest intended size
- **Statement:** When the print size is not settled, every print rule is judged at the smallest candidate width.
- **Why:** Every line and gap scales with the print. A design that passes at 12 in can fail at 10 in.
- **Check:** `print_check.json` `widths[]`. Rebuild targets use the smallest width (`targets.py`).
- **Threshold:** n/a.
- **Sources:** W (written-sources 7.11, calculation).
- **Confidence:** ESTABLISHED (arithmetic).

### PRINT-09 Art reduced into a seal loses detail in proportion
- **Statement:** Art that was drawn to print at one size and is placed smaller inside a seal has every line and gap reduced by the same factor. Check the art at its real printed width.
- **Why:** The temple art is approved at up to 12 in wide (BRAND.md section 8). Inside a 10 in seal it may print at 4 in, so its lines and window gaps are about a third as wide.
- **Check:** The art's width in inches = `centre.art.width_px` / `ppi`; the art rows and overlays in `print_check.json`.
- **Threshold:** The art's own lines and gaps must pass PRINT-01 and PRINT-03 at that size. If they do not, the fix is a seal layout or size change (or a simplified art variant, which is Evan's call), never a redraw by this audit.
- **Sources:** Derived from PRINT-01 and PRINT-03.
- **Confidence:** ESTABLISHED (derived).

### PRINT-10 Supply true vectors, expanded, without clipping masks
- **Statement:** Final art is a real vector file with type and strokes expanded and no clipping masks (rebuild shapes with Pathfinder instead). A raster placed inside a vector file does not count.
- **Why:** Hidden geometry and live effects print unpredictably.
- **Check:** A step in the rebuild spec.
- **Threshold:** Binary.
- **Sources:** V:goldenpress-designing-for-screenprint; W58.
- **Confidence:** ESTABLISHED.

### PRINT-11 Thin light lines on dark garments need a solid underbase
- **Statement:** On a dark garment, white needs an underbase (DTG) or a full white layer (DTF). Features too thin to carry it print translucent.
- **Why:** This is the mechanism behind DTG's high line minimum.
- **Check:** Covered by PRINT-01 at the DTG and DTF levels.
- **Threshold:** As PRINT-01.
- **Sources:** W44, W57, W59; V:transferexpress-dtf-art-guidelines (DTF white backing).
- **Confidence:** ESTABLISHED.

### PRINT-12 Fine detail that is not critical may drop out; text may not
- **Statement:** When something must give at print size, drop non-critical texture first. Text, rings and the silhouette must hold.
- **Why:** Vendors accept losing texture, never text.
- **Check:** In the overlays, separate flags on texture (acceptable loss, polish) from flags on text and rings (breaks print).
- **Threshold:** Judgement, recorded per finding.
- **Sources:** V:transferexpress-dtf-art-guidelines.
- **Confidence:** SINGLE SOURCE.

## 8. TEST: golden rules and tests

### TEST-01 Squint (blur) test
- **Statement:** Blurred, the design should still show its structure and hierarchy.
- **Why:** Blur removes detail and leaves weight, which is what is seen first and from a distance (a jacket back is read across a room).
- **Check:** `blur_0.5pct.png`, `blur_1pct.png`, `blur_2pct.png`. For the seal, the expected order is: outer ring, the band as a texture ring, the top word, the temple. Small dividers and the small bottom line should disappear first.
- **Threshold:** The top word remains a distinct shape at 1 percent blur; the temple silhouette at 2 percent.
- **Sources:** W65, W66.
- **Confidence:** ESTABLISHED.

### TEST-02 Black and white first
- **Statement:** Judge the design in one colour before anything else.
- **Why:** Colour hides structural problems.
- **Check:** `onecolour.png`.
- **Threshold:** None.
- **Sources:** W18, W20; V:futur-legibility-hierarchy-contrast, V:satori-13-golden-rules.
- **Confidence:** ESTABLISHED.

### TEST-03 Five-second test
- **Statement:** After five seconds, a viewer should be able to name the main message.
- **Why:** That is about how long a jacket back is looked at in passing.
- **Check:** The auditor's approximation: view `small_2in.png` for a moment and say what you would name first. Note that a real test needs people.
- **Threshold:** The brand name or the temple is named first.
- **Sources:** W67 (method) plus glossaries.
- **Confidence:** ESTABLISHED (as a method; the audit's version is only an approximation).

### TEST-04 Consistency
- **Statement:** One stroke system, one spacing logic, one tracking logic.
- **Why:** Consistency is what makes a mark look designed rather than assembled.
- **Check:** Rolled up from LINE-01, COMP-04 and TYPE-03.
- **Threshold:** As those rules.
- **Sources:** W1, W39, W7.
- **Confidence:** ESTABLISHED.

### TEST-05 Remove until it breaks
- **Statement:** For each element, ask whether removing it would lose meaning or recognition; if not, propose removing it.
- **Why:** Perfection is reached "when there is no longer anything to take away".
- **Check:** Element inventory (LOGO-01). For the seal, the candidates are the dividers, the thin ring and the caption.
- **Threshold:** Propose only. Removing an element is Evan's call.
- **Sources:** W70, W18.
- **Confidence:** ESTABLISHED (as a heuristic).

### TEST-06 Look at it at real size
- **Statement:** View the design at its true print size (or a full-size print) before approving.
- **Why:** Screen zoom hides both crowding and print-scale thinness.
- **Check:** Recommend a 1:1 paper print at the chosen width as the last step.
- **Threshold:** n/a.
- **Sources:** W42 (test the thinnest elements against a minimum-diameter circle at size); W41.
- **Confidence:** ESTABLISHED.

### TEST-07 Distance legibility
- **Statement:** Text on a jacket back should be readable at the distance people stand.
- **Why:** Sign makers size letters to viewing distance.
- **Check:** Cap heights in inches from `print_check.json`.
- **Threshold:** Report only. W71 gives sign-industry rules of thumb, not garment ones.
- **Sources:** W71.
- **Confidence:** SINGLE SOURCE.

---

## Tally

| Group | ESTABLISHED | SINGLE SOURCE | FOLKLORE |
|---|---|---|---|
| LOGO (6) | 3 (01, 02, 03) | 3 (04, 05, 06) | 0 |
| COMP (7) | 5 (01, 02, 03, 06, 07) | 2 (04, 05) | 0 |
| RATIO (5) | 2 (03, 05) | 0 | 3 (01, 02, 04) |
| TYPE (11) | 8 (01 to 08) | 3 (09, 10, 11) | 0 |
| LINE (5) | 4 (01, 02, 03, 05) | 1 (04) | 0 |
| SEAL (8) | 5 (01, 02, 03, 04, 07) | 3 (05, 06, 08) | 0 |
| PRINT (12) | 11 (01 to 11) | 1 (12) | 0 |
| TEST (7) | 6 (01 to 06) | 1 (07) | 0 |
| **Total (61)** | **44** | **14** | **3** |

Number-level conflicts (direction established, value disputed): PRINT-03 gap sizes,
PRINT-05 text size. Single-source numbers inside ESTABLISHED rules: COMP-02 (5 percent),
TYPE-08 (tracking values), LOGO-03 (DTG halo).

## What the research could not settle

- Cap height as a fraction of band width, ring band widths and spacing between rings:
  no designer source gives numbers. The audit reports them and checks consistency only.
- Tapstitch's own line, gap and text minimums for the jacket blank: not published.
- The DTG minimum gap: no source found.
- The optical-centre offset: direction only (one forum figure of 5 percent).
- A numeric stroke ratio specifically for logos: only the technical-drawing analogy (1:2:4).
- Every video is single reader (captions plus 160x90 storyboards). On-screen values
  in Spoon Graphics and Graftalks are UNREADABLE until the videos are re-run on the
  Mac with /watch and Gemini.
