# Report template

Fill every bracket. Every number in the report is quoted from `measurements.json` or
`print_check.json` (name the file and key once per section), or from a crop you
made with `crop.py` (name the crop file). No em dashes anywhere.

---

# Design audit: [design name]

**File:** [path] ([source size] px, analysed at [size] px)
**Ink / ground:** [ink colour] on [background colour], [ink_mode]
**Audited at:** [print widths, e.g. 12 in and 10 in wide, ink to ink]
**Print method assumed:** [DTF / DTG / screen / all three, and why: garment line from BRAND.md section 7, or unknown]
**Scripts:** run_audit.py output in [outdir]
**Detection check:** [what the scripts found (N rings, N text arcs, centre art, caption) and whether that matches what you see in the image. If anything was misdetected, say what and how it affects the numbers below.]

## Verdict

[Two or three sentences. Is it ready to print at each size? What single change would
do the most? Which brand-locked items limit what can change?]

## Findings, ranked

Rank by severity first (breaks print, then hurts legibility, then polish), then by
how many other findings the fix resolves. One block per finding:

### [n]. [Short title]  ([severity])

- **Rule:** [rule id] [one-line statement] ([confidence: ESTABLISHED / SINGLE SOURCE / FOLKLORE])
- **Mechanism:** [why this fails: what happens physically or perceptually, before any fix]
- **Evidence:** [the measured values with units at each print width, and the file/key
  they came from; an overlay or crop file name for anything visual]
- **Fix:** [the concrete change, with target numbers: in mm and pt at each audited
  width AND as a fraction of the outer diameter, so the rebuild works at any size]
- **Tool:** [vector rebuild of rings and type / regenerate the art / layout nudge / no change: brand call]

Severity definitions:
- **breaks print**: at the audited size and method, ink will not hold (lines under the
  minimum, gaps that close, text below the minimum size). It fails regardless of taste.
- **hurts legibility**: it prints, but a reader at normal viewing distance will
  struggle (small-size, blur or hierarchy failures, crowding, reading direction).
- **polish**: visible to a trained eye (off-centre by a few pixels, uneven gaps,
  inconsistent tracking, stroke ratios that do not relate).

## Brand conflicts

[Every place a rule pushes against a settled BRAND.md decision (white ink only, the
established line-drawing style, approved art). State the rule, the decision, the
trade-off, and leave the call to Evan. If none, say "None".]

## Rebuild spec

Only when rings or type will be rebuilt as vectors. A table Evan or a designer can
build from directly. Give every value as a fraction of the outer diameter D and in mm
at each audited print width.

| Element | Target | Fraction of D | At [12] in | At [10] in | Rule |
|---|---|---|---|---|---|
| Outer ring stroke | | | | | |
| Gap outer ring to band | | | | | |
| Band text cap height | | | | | |
| ... | | | | | |

## Passed

[Rule ids that passed, one line each with the number that passed. Keep it short.]

## Not checked

[Rules that could not be measured on this input and why (for example, no rings
detected, no caption, raster too small to resolve the minimum line at this size).]

## Previews looked at

[List the preview files you viewed (small_1in, small_2in, blur_*, onecolour, spread_*,
print_flags_*) and one line on what each showed.]
