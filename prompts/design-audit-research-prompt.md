# Prompt: research logo and graphic design rules, build a design-audit skill

Paste everything below the line into a fresh Claude Code chat on the Mac (the
youtube-to-agent stack, the /watch plugin, yt-dlp, ffmpeg and GEMINI_API_KEY
live there, not in cloud sessions). Open the chat in the Claude Projects
workspace so the skill lands in `.claude/skills/`.

---

I want a reusable `design-audit` skill for Peculiar People, built from real research, that I can run against any logo, seal or garment graphic and get back specific, measured fixes. The first thing it will be run on is a circular seal for the back of a jacket (described at the bottom). Use the youtube-to-agent tool stack for the video research, back it with written sources, and build the skill with skill-creator.

Read these first: `CLAUDE.md`, `project-sync/BRAND.md` (especially the print and artwork sections), and the youtube-to-agent `SKILL.md` plus its two prompts in `references/`.

## What to research

Cover each of these, aiming for rules specific enough to check against an image, with numbers wherever the sources give them:

1. Logo and emblem design: simplicity, scalability, the small-size test, the one-colour test, distinctiveness, how emblem and badge logos are built.
2. Composition and spacing: hierarchy, optical versus mathematical centring, visual weight and balance, negative space, consistent spacing systems (modular or ratio-based gaps), breathing room between elements.
3. Ratios and proportion: golden ratio, rule of thirds, modular scales for type and spacing. Be sceptical here. Much of what is said online about the golden ratio in logos is retrofitted or myth. Record what designers actually use versus what is claimed after the fact, and say which is which.
4. Typography: hierarchy between type sizes, tracking for all-caps text, type on a circular path (baseline and centre alignment, which way the bottom text reads, start and end points, kerning around curves), minimum legible size.
5. Line work: stroke-weight consistency, how many weights to use, the ratio between them, how ring and border weights relate to the art inside.
6. Circular seals and badges specifically: ring proportions, band widths, spacing between rings, how text sits inside a band, divider glyphs (dots, diamonds, stars), how the centre art relates to the frame.
7. Screen-printing and garment constraints: minimum line weight and gap at print size, ink spread closing small counters and gaps, one-colour white ink on dark fabric, sizing a back print, what fails when a dense design is printed.
8. Other golden rules working designers repeat: the squint or blur test, black-and-white first, the five-second test, consistency, removing until it breaks.

## How to research

**Find the videos.** The youtube-to-agent skill needs a URL, so search first: run `yt-dlp "ytsearch8:<query>" --flat-playlist --print "%(title)s | %(channel)s | %(duration_string)s | %(view_count)s | %(webpage_url)s"` for queries covering the topics above (for example "logo design principles", "badge logo design tutorial", "seal emblem logo design", "optical alignment graphic design", "type on a circle illustrator", "screen printing design mistakes minimum line weight", "golden ratio logo myth"). Prefer working designers and studios with a track record (agency principals, type designers, print shops explaining their own production), recent uploads, and videos that show the work, not listicles. Show me the shortlist of 6 to 10 videos with one line on why each made it, then continue without waiting unless something looks off.

**Run each video through youtube-to-agent steps 1 to 4 only**, one work folder per video under `research/design-audit/<video-slug>/`. Do not build a skill per video. These are mostly lecture and demo videos, not build tutorials, so adapt the step 2 spec: keep the two-reader method, the "describe only what is in this video" rule and the UNREADABLE rule, but replace the six build sections with:
- PRINCIPLES: each rule stated in the video, as close to verbatim as possible.
- NUMBERS: every concrete value (ratios, sizes, weights, spacings, percentages), quoted exactly.
- DEMONSTRATED: what the video actually shows being done, versus only asserted.
- CAVEATS: exceptions, warnings, and "this is a guideline, not a law" asides.
- NOT SHOWN: claims made without evidence or demonstration.
Keep the reconcile step's CONFIRMED / SINGLE SOURCE / CONFLICT labels. Scope anything over about 20 minutes to the relevant section. Pass `--no-whisper` to /watch as the skill says.

**Cross-check with written sources.** Use web search to check the video findings against reputable written material: books and long-form writing by working designers (for example Logo Design Love, Thinking with Type, Butterick's Practical Typography, Paul Rand's writing), type foundry and studio articles, and screen-print shop technical guides for the print numbers. A rule counts as established only if at least two independent sources agree. Mark single-source rules as such, and mark anything that looks like design folklore.

## What to build

A skill at `.claude/skills/design-audit/` containing:

1. `SKILL.md`: when to use it, and the audit procedure. Inputs: an image file, and optionally its intended print size and the garment colour. Output: a ranked report.
2. `references/rules.md`: the rule library. Each rule has an id, a one-line statement, why it matters, how to check it, a pass/fail threshold where one exists, its sources, and its confidence (ESTABLISHED, SINGLE SOURCE, or FOLKLORE). Group rules under the eight topics above.
3. `scripts/`: Pillow-based checks for every rule that can be measured from pixels. At minimum:
   - Centring: ink bounding box and visual centre of mass against the canvas and ring centre.
   - Concentricity: detect the rings and report each one's centre and radius.
   - Stroke weights: sample line thickness in the rings, the type and the centre art, and report the ratios between them.
   - Spacing: gaps between rings, between text and its ring edges, and between centre art and the inner ring, with the ratios between those gaps.
   - Print size: given the intended print width in inches, convert the thinnest strokes, the smallest gaps and the cap height of the smallest text to inches, millimetres and points, then compare them with the screen-print minimums from the research.
   - Small-size and blur tests: write downscaled (for example 1 inch and 2 inch) and blurred copies to look at.
   Scripts write their numbers to JSON, and the report quotes them.
4. A report template. Every finding gives the rule id, the measured evidence, severity (breaks print, hurts legibility, polish), the concrete fix with target numbers, and the tool that would make the fix (vector rebuild of rings and type, regenerating the art, or a layout nudge).

The audit proposes changes. It never edits the design, and it never overrides a settled decision in BRAND.md (white ink only, the established line-drawing style, approved art). When a rule conflicts with a brand decision, it reports the conflict and leaves the call to me.

## Verify it

Run the finished skill on the seal below and fix whatever breaks in the scripts. A skill that has never been run on a real input is only a summary of the research.

## The design it will first be run on

A circular seal for the back of a jacket, one colour: white ink on navy `#001A58`. From the outside in: a thick outer ring; a band of small serif capitals reading "A CHOSEN GENERATION • A ROYAL PRIESTHOOD • AN HOLY NATION • A PECULIAR PEOPLE", with small solid diamonds at left, right and bottom; a thin ring; "PECULIAR PEOPLE" in larger bold serif capitals arched across the top; "EST. 2023" small and arched along the bottom; a heavier inner ring; and inside it a front-elevation line drawing of the Salt Lake Temple in a loose architectural-sketch style (three weights of line, overrunning tails at the corners, a solid Moroni figure on top), with "UTAH, USA" in small spaced capitals under it. The temple drawing is approved art: the audit may comment on its size and placement in the seal, but not ask for it to be redrawn. The rings and type were AI-generated and will be rebuilt as true vectors, so findings about them should give the exact target numbers for that rebuild. Print size is not settled yet; audit at a 12 inch wide back print and at a 10 inch one.

I will attach the seal image when I run the skill, so build and test it on a stand-in if the image is not in the chat.

## Rules for the whole job

- No em dashes anywhere in the skill, the report, or chat with me.
- Explain the mechanism behind any failure before fixing it.
- Keep the research folders: the skill's provenance should point to them.
- When it's done, tell me what was built, how many rules are ESTABLISHED versus SINGLE SOURCE versus FOLKLORE, which videos were used, and anything the research could not settle. Then commit and push on a new branch.
