<!-- Iteration 1 verification run of the design-audit skill on the stand-in seal, 7 Oct 2026. Written by a fresh subagent following SKILL.md; saved by the parent session. Script fixes made after this run are listed in ../verification/FIXES.md. -->

# design-audit skill feedback (stand-in seal run, 7 Oct 2026)

## Script errors or crashes

- **None.** run_audit.py finished in 56 s with system python3 (numpy 2.5.3, Pillow 12.3.0).
- **Sanity check matched:** ring3 offset_from_outer_px 15.23, ring2 width_mean 8.9.

## Script bugs and wrong-looking numbers

1. **Side diamonds merged into the band text arc.**
   - text_arcs groups by angular gap, and the diamonds at 90 and 270 deg are within 3 cap heights of the text ends, so they join the text arc.
   - summarise_arc then counts them as glyphs because their height is at least 0.6 cap.
   - Result: band letter_gap_cv_pct is 29.1, which trips the TYPE-03 "look closely" flag. With the diamonds excluded it is 14.9.
   - The side diamonds also never appear as `kind: ornament`, so SEAL-05 cannot be checked from the JSON. I had to write my own component pass.
   - Fix: classify components by shape (aspect ratio, solidity, lack of counters) or by the absolute angle positions 90/180/270, before grouping.
2. **centre.* offsets use the inner ring's centre, not the outer ring's.**
   - When the inner ring is the defect (as here), every centre number points at the wrong thing. Art bbox -14.5 and caption -14.0 look like art/caption problems; relative to the outer axis they are -0.5 and 0.
   - Block centre is 75.51 px against ring3 vs 81.5 px against the outer centre.
   - Fix: report against the outer ring centre, or both.
3. **gap_to_inner_ring_px ignores the ring's own centre offset.** It uses r_outer from the outer centre. EST shows 158.84 px; the real gap at 6 o'clock is about 153 px.
4. **targets.json labels two rows with the wrong rule.**
   - "gap ring1 to ring2" and "gap ring2 to ring3" say PRINT-02; they should be SEAL-02 (or PRINT-03).
   - "radial centre of both arcs" says TYPE-05; it should be TYPE-06.
5. **targets.json TYPE-06 target is wrong in kind.**
   - It averages the two arcs' current radii (0.36845 D). That moves PECULIAR PEOPLE off its centred position (ratio 1.034 now) toward ring2.
   - The target should be the centre line of the zone between the two rings, here 0.36654 D after the rebuild.
6. **targets.json hairline target cannot be met.**
   - It sets every text hairline to 0.00417 D (the DTG warn level, 1.06 mm at 10 in) while keeping the 4.5 mm cap height. That is a stroke of 0.236 of the cap height, heavier than nearly any book face.
   - It also never checks whether thicker strokes plus the gap floor still fit in the cap height or along the arc. SKILL.md step 6 says to check this, but the script does not help.
   - At 10 in the band text grows about 15 deg of arc, so the targets do not work together, and the script cannot tell.
   - Fix: give a floor (method fail level) and a margin target separately, and compute the arc-length budget.
7. **targets.json missing rows.** It has no targets for:
   - the ornaments,
   - caption cap height,
   - art clearance,
   - block centring (COMP-02),
   - EST clearance,
   - the inner zone clearance.

   I computed all of these by hand.
8. **The "pt" value on cap-height rows is cap height, not font size.** In print_check element rows and targets.json it reads "12.75 pt" next to est_font_pt 18.8. That invites a wrong reading. Rename the key (cap_pt) or drop it.
9. **Ring CV tolerance is below measurement resolution for thin rings.** ring2 at 8.9 px measured to 0.5 px gives a CV of about 4 percent from quantisation alone, so LINE-01's 3 percent tolerance fails any ring under about 15 px. Scale the tolerance by stroke_resolution_px / width.
10. **Blur previews show bright spots at 12, 3, 6 and 9 o'clock.** The ring touches the preview edge, which looks like an edge-padding artefact in the blur. Pad the canvas before blurring.
11. **crop.py does not clamp to the image.** A polar crop past the edge fills with black (crop_top_word.png). Clamp, or pad with the background colour.
12. **No positions for the widest and narrowest letter gaps.** Step 3 says to crop the widest and narrowest gaps of each arc, but the JSON only gives stats. I wrote my own pass to find their angles.
13. **Morphological closing flags every acute join (A, N, Y apex notches) as a closing gap.** Physically true but noisy; it dominates the yellow on type. Worth a note in SKILL.md, or masking corners whose gap is under the spread distance.
14. **The PRINT-03 letter-gap row only appears for some methods.** It shows at screen_transfer and DTF but not at screen or DTG, so a reader cannot see the pass values. List it for every method.
15. **DTF and DTG morphology "fail" entries carry gap_mm 0.0 and closing_gaps null.** Correct (there is no fail level), but morph_radius_px gap 0.5 / 1.0 is then meaningless noise.

## SKILL.md unclear or wrong

1. **It points to "the temple-product-generator venv".** That folder does not exist in this workspace. System python3 worked.
2. **"Copy the preview files you cite into the same folder" is redundant** when --outdir is already the report folder.
3. **It does not say what "binding" means when --method all mixes methods.** Lines and gaps come from different methods (DTG for lines, screen transfer for gaps). I had to decide this myself.
   - It also does not say whether targets should use the fail or the warn level. targets.py uses DTG warn (1.06 mm) without saying so in the JSON beyond min_line_mm.
4. **The bbox_in_crop note works, but the overlay PNGs are downscaled.** Their 1600 px width does not equal the crop size, so you cannot map overlay pixels back to coordinates. Say so.
5. **No instruction for an off-centre inner ring.** It does not say to re-reference centring numbers to the outer ring.
6. **COMP-04 tolerance (10 percent) vs SEAL-04 vs RATIO-05 interact, and no guidance is given.** Equalising clearances changed the field size here, which helped PRINT-09. The skill should say to check this.
7. **The severity rules are silent on a FAIL that is within measurement resolution.** Examples: ring2 at 0.705 vs 0.71, band gap 1.002 vs 1.02, caption gap 1.014 vs 1.02. Known limits says "judgement call", but not which severity it gets.
8. **It does not say which print size to recommend** when the brief leaves it open and the rules only pass at one width. This is the most useful output of the audit here.

## Things I had to work out myself

- **Rebuild geometry:** the outside-in radii (ring edges, band centre lines, the zone centre line, field diameter). targets.json gives strokes and gaps but never the radii a designer needs.
- **Stroke-to-cap ratio and the E/B counter check:** whether a monoline face at the floor stroke still fits 3 strokes plus 2 gaps in the cap height.
- **Arc-length budget:** whether the type fits at each width after the stroke and gap changes. This decided the 12 in recommendation.
- **The diamond orientation problem:** side diamonds are upright, not rotated to the path. No metric covers it.
- **The misplaced EST period:** found only because the speck list showed an 8 px shape at cap-line radius.
- **The art's construction lines:** they set the art bbox and so distort the caption gap and block centring. The skill has no way to separate the building from stray lines.
