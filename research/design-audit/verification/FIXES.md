# Fixes after the iteration 1 verification run

The first full run of the skill (a fresh agent following SKILL.md on the stand-in
seal) is in `standin_audit/` with its `REPORT.md`; its feedback is in
`skill_feedback.md`. The scripts did not crash, and the sanity values matched
(ring3 offset 15.23 px, ring2 width 8.9 px). These changes followed. The rerun is in
`standin_audit_after_fixes/` (JSON plus two overlays).

| Feedback item | Mechanism | Fix |
|---|---|---|
| Side diamonds merged into the band text, letter-gap CV 29.1 percent | Text grouping split arcs only on large angular gaps, and the diamonds sat within 3 cap heights of the text ends, so they joined the arc and were counted as letters | Ornaments are classified before grouping (solid convex shape, solidity above 0.88, at least 0.45 cap heights, not a narrow bar) and listed as `kind: ornament` with angle, radial and tangential extent, and offset from the band centre line. Band CV is now 14.9 percent, matching the agent's hand count |
| Centre offsets measured from the off-centre inner ring | `centre_zone` used the inner ring's centre for both membership and offsets | Offsets now use the outer ring centre; `_vs_inner_ring` versions sit alongside. The block offset now reads 81.5 px, as the agent measured |
| Text-to-ring gaps ignore the ring's own centre | Gaps used radii from the outer centre | Gaps are computed from each ring's own fitted centre per glyph pixel (EST to ring3: 151.2 px, against the agent's ~153 px on one ray) |
| Wrong rule labels in targets.json; TYPE-06 target averaged the arcs | Hand-written labels; the target was the mean of the current radii | targets.py rewritten: rules relabelled, both inner arcs target the zone centre line |
| Hairline target unreachable (1.06 mm in a 4.5 mm cap) | Only the warn level was used | Every stroke target now gives a floor (fail level) and a margin (warn level), plus a stroke-to-cap ratio check with a reading, an E/B fit check and an arc-room check |
| Missing targets (caption, block centring, art clearance, dividers, radii) | Not implemented | Added, including `geometry_now` (current radii outside in) and divider orientation (side diamonds 31x44 vs bottom 44x31 px: not rotated to the path) |
| "pt" on cap-height rows read as a font size | Key name | Renamed `cap_height_pt`; `est_font_pt` is the font size |
| Ring CV tolerance below measurement resolution | Run lengths are whole pixels | `width_cv_noise_floor_pct` added; LINE-01 uses the larger of 3 percent and the floor |
| Bright spots in blur previews | The blur smeared the canvas edge where the ring touches it | Previews pad with the ground colour before blurring |
| crop.py filled with black past the edge | No clamp | Crops pad with the ground colour |
| No locations for widest and narrowest letter gaps | Only stats were kept | `narrowest_letter_gap` and `widest_letter_gap` with angle in degrees |
| Acute joins flagged as closing gaps | Any acute notch fills a little under closing | SKILL.md tells the auditor not to count them |
| Gap radius printed when no gap level exists | Cosmetic | `null` now |
| SKILL.md: wrong venv, redundant copy step, undefined "binding", overlay scale, off-centre inner ring, resolution severity, print-size recommendation, interacting fixes | Gaps in the instructions | All addressed in SKILL.md |

Not changed: the art's construction lines still set its bounding box (no reliable
way to separate a building from overrunning lines in pixels); SKILL.md now says so.
