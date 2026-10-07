---
name: design-audit
description: Audit a logo, seal, badge, emblem or garment graphic against a researched rule library (61 rules on composition, typography, type on a circle, line weights, seal construction and screen-print, DTF and DTG limits) and return a ranked report of specific, measured fixes with target numbers. Pillow scripts measure centring, ring concentricity, stroke weights, spacing and print-size minimums from the pixels, and write small-size, blur and ink-spread previews. Use whenever Evan shares a design image and asks to audit, critique, check, review or "fix" it, asks whether a graphic will print, whether lines are too thin, whether a seal is centred or balanced, what the rebuild specs should be, or wants a design checked before it goes on a garment, even if he never says "audit". Proposes only; never edits the design or overrides a BRAND.md decision.
---

# design-audit

Measures a design, checks it against `references/rules.md`, and writes a ranked
report of fixes with target numbers. Built from the research in
`research/design-audit/` (see Provenance).

## Ground rules

1. **Propose, never edit.** Do not modify the design file, regenerate art, or touch the
   store. The output is a report.
2. **BRAND.md wins.** Read `project-sync/BRAND.md` sections 7 and 8 first. White ink
   only, the established line-drawing style and approved art are settled. When a rule
   conflicts with one of them (for example, PRINT-09 says the art is too dense at seal
   size), report the conflict in "Brand conflicts" with the trade-off and leave the call
   to Evan. Approved art may get findings about its size and placement in the layout,
   never a request to redraw it.
3. **Every finding is measured or seen.** Quote the number and the JSON key it came
   from, or name the crop or preview file that shows it. A finding with no evidence is
   left out.
4. **Mechanism before fix.** Each finding says why it fails (what happens to the ink,
   or to the eye) before it says what to change.
5. **Respect confidence.** A SINGLE SOURCE rule can produce a finding, labelled as such,
   but never a "breaks print" severity on its own. FOLKLORE rules never fail a design.
6. **No em dashes** anywhere in the report or chat. House rule.

## Inputs

- The image (PNG or JPG; a transparent PNG print file works too, ink is read from alpha).
- Intended print width or widths in inches, measured ink to ink. If not given: for a
  back print, audit at 12 in and 10 in (the industry default and the smaller
  candidate, PRINT-07); for anything else, ask.
- Garment colour (sets which colour is ink). Default: white ink on whatever the
  background is. Navy is `#001A58`.
- Print method, if known: tee is DTG, fleece is DTF (BRAND.md section 7). If unknown
  (for example a new blank), use `--method all` and treat the strictest method that
  could apply as binding (PRINT-08), saying so.

## Procedure

### 1. Run the scripts

Use any python3 with numpy and Pillow (the temple-product-generator venv has both).

    python3 .claude/skills/design-audit/scripts/run_audit.py <image> \
        --width 12 --width 10 --method all [--ink '#FFFFFF' --bg '#001A58'] \
        --outdir <scratch or project folder>/<design>_audit

This runs `measure.py` (geometry), `print_check.py` (physical sizes against
`references/print_thresholds.json`), `targets.py` (rebuild numbers, seals only) and
`previews.py`. About a minute for a 3000 px image. The output folder holds:

| File | What it is |
|---|---|
| `measurements.json` | rings, gaps, text arcs, centre art, caption, strokes, tints, smallest shapes (analysis px) |
| `print_check.json` | per width and method: PASS / WARN / FAIL rows, thin-stroke and closing-gap regions, smallest shapes in mm |
| `targets.json` | rebuild targets as a fraction of the outer diameter D and in mm / pt at each width |
| `print_flags_<w>in_<method>_<fail or warn>.png` | red = stroke under the line minimum, yellow = gap that will close |
| `small_1in.png`, `small_2in.png` | the design at 1 and 2 in on a 96 ppi screen, enlarged 4x |
| `blur_0.5pct.png`, `blur_1pct.png`, `blur_2pct.png` | squint test |
| `onecolour.png` | ink only, black on white |
| `spread_<w>in.png` | ink grown by an illustrative 0.1 mm (orange = growth) |

All pixel values are in analysis pixels (inputs over 3200 px are downscaled; the scale
is `image.analysis_scale`). Angles: 0 degrees is 12 o'clock, increasing clockwise.

### 2. Check what the scripts detected

Open `onecolour.png` and compare it with `measurements.json`:

- Number of `rings` and their order (ring1 is outermost).
- `zones[*].arcs`: one entry per text line or ornament, with `position` (top, bottom,
  side) and `kind` (text or ornament). Does it match the lines you can see?
- `centre.art` and `centre.caption`: is the caption split from the art correctly?

If ink detection is wrong (wrong colours, or a textured background), rerun with `--ink`
and `--bg`. If a ring was missed because text or art breaks it, say so in the report's
detection check and treat the numbers that depend on it as unavailable. Never report
a number from a misdetected element.

### 3. Look at every preview

View each preview file, and the `print_flags` overlays for the binding method at the
smallest width. Make zoomed crops for anything visual you will cite:

    python3 .claude/skills/design-audit/scripts/crop.py <image> --polar <cx> <cy> <deg> <r> <half> --out crop_x.png
    python3 .claude/skills/design-audit/scripts/crop.py <image> --box x0 y0 x1 y1 --out crop_y.png

(cx and cy are `centring.outer_ring_center`; r is an arc's `(r_min + r_max) / 2`.)
Always crop the bottom arc (TYPE-04), the widest and narrowest letter gaps of each
arc (TYPE-03), each divider (SEAL-05), and the worst red and yellow regions in the
overlays (their `bbox_in_crop` coordinates are relative to the ink bounding box
`ink.bbox`, so add `ink.bbox[0]` and `ink.bbox[1]` minus the 8 px pad).

### 4. Score the rules

Read `references/rules.md` and go group by group. For each rule: PASS, FAIL, or NOT
CHECKED (with the reason), using the check and threshold it states. Rules marked
*tolerance* use the skill's own pass bands; say so when one decides a finding.

What the scripts cannot see, you check by eye: reading direction, glyph distortion,
divider glyph match, kerning pairs, style match between type and art, hierarchy under
blur.

### 5. Severity and ranking

- **breaks print**: an ESTABLISHED PRINT rule FAILs at the binding method and the
  smallest width (ink will not hold, gaps close, text under the floor). Flags on texture
  inside approved art count, but sort after flags on text and rings (PRINT-12).
- **hurts legibility**: it prints, but a reader will struggle (small-size, blur,
  hierarchy, reading direction, crowding, WARN-level print results on text).
- **polish**: visible to a trained eye (centring by a few px, uneven gaps, ring wobble,
  tracking inconsistency, stroke ratios that do not relate).

Rank by severity, then by how many other findings one fix resolves (a vector rebuild of
the rings fixes concentricity, ring wobble and gap uniformity at once: list it once
and name what it covers).

### 6. Fixes with numbers

Every fix gives target numbers in mm and pt at each audited width, and as a fraction of
the outer diameter D, so a rebuild at any size works. Take them from `targets.json`
where it has them, and check that they make sense together: a thicker line must not
push a gap under PRINT-03. Name the tool for each fix:

- **vector rebuild of rings and type**: rings, text paths, tracking, dividers, centring.
- **regenerate the art**: only when Evan decides to (never as this audit's instruction
  for approved art); otherwise "brand call".
- **layout nudge**: move or scale an element without redrawing it.

When a rule pushes against the approved art (PRINT-09: the art's lines or gaps fail at
its size inside the seal), the options are layout changes: a larger seal, a larger
inner field with thinner bands, or fewer elements. A simplified art variant goes under
Brand conflicts as Evan's call.

### 7. Write the report

Use `references/report-template.md` exactly. Save it next to the audit output as
`REPORT.md`, and give Evan the verdict, the top findings and the file path in chat. Copy
the preview files you cite into the same folder, so the report travels with its
evidence.

## Known limits

- Stroke widths are measured to about half a pixel (`stroke_resolution_px`). At a
  12 in seal from a 3000 px file one pixel is about 0.1 mm, so a line within 0.05 mm of
  a limit is a judgement call. Say so, and ask for a higher-resolution or vector file.
- Hairline and stem values for type are percentiles of centre-line samples, not
  per-letter measurements. Confirm a hairline failure in a crop before calling it.
- Letter gaps are bounding-box gaps, so letter shapes (A, L, T, Y) add natural
  variation. TYPE-03 needs a visual check.
- Ring detection needs a ring to cover most of its circle. A ring broken by text or
  art for more than 40 percent of its length is not detected; say so.
- Non-circular logos get centring, strokes, print checks and previews; the SEAL and arc
  rules report NOT CHECKED.
- The print numbers are vendor guidance, not Tapstitch's spec (none is published). When
  Tapstitch confirms the jacket's method and minimums, update
  `references/print_thresholds.json`.

## Provenance

Built 7 October 2026 with skill-creator from:

- `research/design-audit/METHOD.md`: how the research ran, and what could not run in
  the cloud session (no /watch frames, no Gemini pass).
- `research/design-audit/<video>/SPEC.md` and `notes/claude-pass.md` for ten videos:
  The Futur, Satori Graphics, Spoon Graphics (two), Graftalks, Pixel & Bracket,
  We Are Draper, Golden Press Studio, Transfer Express, Ryonet.
- `research/design-audit/written-sources.md`: 71 written sources with quotes and verdicts.

`tests/make_standin_seal.py` builds a stand-in seal with known defects (inner ring
15 px off centre, a 9 px thin ring, a low centre block) for checking the scripts after
a change: the run should report ring3 `offset_from_outer_px` near 15.2 and ring2
`width_mean` near 8.9.
