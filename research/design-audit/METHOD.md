# design-audit research: method

Research behind `.claude/skills/design-audit/`. Run 7 October 2026 in a claude.ai
cloud session, not on the Mac, which changed how the youtube-to-agent steps ran.

## What ran and what could not

| youtube-to-agent step | What happened here |
|---|---|
| 1. Scope | Done. Videos found with `yt-dlp "ytsearch8:<query>" --flat-playlist`. Nothing over 20 minutes was used in full except Golden Press (20:36), which is entirely on topic. |
| 2. Claude pass | Done, but **without /watch**. YouTube's bot check blocks video downloads from cloud IPs, so no full-resolution frames. What did download: the caption track (`--write-auto-subs`, `player_client=web_embedded`) and YouTube's storyboard thumbnails (`-f sb0`, 160x90 px, one every ~5 s). Storyboards show what is being done on screen but cannot be read for on-screen numbers, so any value that was only shown on screen is UNREADABLE. |
| 3. Gemini pass | **Did not run.** No GEMINI_API_KEY in the cloud session. Per the skill's failure-mode rule, every video SPEC.md is SINGLE SOURCE (reader A only). |
| 4. Reconcile | Done as a one-reader SPEC.md per video. The CONFIRMED / SINGLE SOURCE / CONFLICT labels are kept; with one reader everything is SINGLE SOURCE at the video level. Cross-source confidence for the rule library comes from the written-source check instead (`written-sources.md`). |

To upgrade a video to two readers later, on the Mac: run /watch and
`gemini_review.py` on the same URL and re-reconcile into that folder's SPEC.md.

## Adapted pass spec (replaces the six build sections)

Keep the two-reader method, the "describe only what is in this video" rule and the
UNREADABLE rule. Sections:

- PRINCIPLES: each rule stated in the video, as close to verbatim as possible.
- NUMBERS: every concrete value (ratios, sizes, weights, spacings, percentages), quoted exactly.
- DEMONSTRATED: what the video actually shows being done, versus only asserted.
- CAVEATS: exceptions, warnings, and "this is a guideline, not a law" asides.
- NOT SHOWN: claims made without evidence or demonstration.

## Folder layout

    <video-slug>/
      source/transcript.txt   cleaned caption track, ~30 s paragraphs with start times
      source/*.vtt            raw caption track(s)
      source/*.info.json      yt-dlp metadata (title, channel, duration, upload date)
      frames/sheet_NN.jpg     storyboard contact sheets, labelled m:ss
      notes/claude-pass.md    reader A, the five sections above
      SPEC.md                 reconciled spec, every line labelled

`written-sources.md` holds the cross-check against books, foundry and studio
writing, and print vendor technical guides.
