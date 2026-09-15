---
name: temple-ref-finder
description: Find reference photos for temple line drawings. Use when Evan asks to run the refs sweep, find reference images for a temple, fill a temple's refs folder, or drops new folders into Temples TO DO. Triggers include "run the refs sweep", "find refs for [temple]", "reference images", "check the TO DO folder".
---

# Temple Ref Finder

Project repo: `Claude Projects/temple-ref-finder/`. Read `docs/decisions.md` before changing behavior; those decisions are settled. Voice: no em dashes in anything Evan-facing, explain a failure's mechanism before fixing it.

All commands run from the repo root with `./.venv.nosync/bin/python`.

Pipeline: sweep `Temples TO DO` folders, find 5-10 good reference photos per temple (site galleries first, web fallback), Claude judges each at full size, clean passes land in the folder's `refs/`, images needing cleanup go flat into `refs/edits/` (no edit prompts; Evan dropped them 25 Aug 2026), folder moves to `Temples READY` for Evan's review. Scale the count by clarity (Evan, 20 Aug 2026): 5 is enough only when the passes are clean, unobstructed views; when the best passes are marginal (edits, partial screening, soft light), keep hunting toward 10.

## Folder name markers

- (no marker) = built temple with real photos; top up to 5-10 refs.
- `*` = under construction or announced WITH an official render; the render is the only ref, no top-up.
- `**` = announced with NO official render released; nothing usable exists yet. Recheck the site's Official section whenever the folder is swept; when a render appears, pull it and downgrade the marker to `*`.

The sweep sets and updates these markers itself via the `mark` field in selection.json (place.py renames the folder as it moves to READY). Markers are the ONLY part of a folder name the pipeline may ever change.

## Commands

| Task | Command |
|---|---|
| Queue report | `scan.py` (`--json` for machine-readable) |
| List a temple's gallery | `gallery.py list --temple "Cedar City" [--json]` |
| Contact sheets for triage | `gallery.py sheet --temple X [--section Gallery\|Official\|Construction\|all] [--max 60]` |
| Pull full-size candidates | `gallery.py pull --temple X --ids 123,456 [--min-long 1200 --min-short 800] [--report-only]` |
| Pull from a web URL | `gallery.py pull --temple X --url https://... --name web-1-hillside` |
| Wipe a temple's staging | `gallery.py clean --temple X` |
| Place refs and move to READY | `place.py --temple X [--report-only]` |

## The sweep workflow

1. Run `scan.py` and report the queue in chat. If a folder is unmapped, research its official name and slug on churchofjesuschristtemples.org, verify the slug with a live `gallery.py list`, add the entry to temples.json, and rerun scan. Slugs keep periods from the official name (`st.-paul-minnesota-temple`), and the site soft-404s unknown slugs with HTTP 200, so only a content check (list finding images) proves a slug right.
2. Branch per folder by scan's action column:
   - **top-up** (normal folder under 5 refs): steps 3-6.
   - **render-only** (starred, empty refs): `gallery.py list`, look at the Official section only, verify per the render rules below, pull the best 1-2 renders (`--min-long 1000` is acceptable, note when used). If no render exists, set `"mark": "**"`, write the shortfall note saying so, and proceed to step 6.
   - **render-recheck** (`**` folder, still empty): check the Official section again. Render released: verify it, pull the best 1-2, set `"mark": "*"`. Still nothing: keep the shortfall note and finalize; the marker stays `**`.
   - **starred-complete** (starred, has its render): check the existing render's resolution, write a note, go straight to step 6 with empty clean/edits. If the folder is `**` but now holds a render, set `"mark": "*"`.
   - **already-complete** (normal folder, 5+ refs): write a note and finalize like starred-complete.
   - **Unstarred but not built** (discovered at the gallery, not by scan): if an unstarred folder's temple turns out to be announced or under construction (Gallery section empty or only site-prep shots, real photos absent), do NOT hunt the web for photos that do not exist. Switch to the starred branch and set the marker: verified official render exists = pull the best 1-2 and set `"mark": "*"`; no render released = shortfall note and `"mark": "**"`. State plainly in the report and the chat summary that the temple is not built yet and that the folder was renamed.
3. `gallery.py list` then `gallery.py sheet`. Read the contact sheets and shortlist 10-16 ids favoring 3/4 two-point-perspective views. Count existing refs toward the 5-10 target and avoid near-duplicate angles of them.
4. `gallery.py pull --ids ...`, then Read each full-size image and judge it against the quality bar below. Record a verdict and one-phrase reason per image. When a base line or a crown edge is too small to call at full-frame size, crop a zoom with the project venv (`./.venv.nosync/bin/python`, which has Pillow) and Read the crop. The system `/usr/bin/python3` has no Pillow, and `sips --cropOffset` returned wrong regions in testing, so do not use either for this.
5. If fewer than 5 pass, or the passes are not clean unobstructed views, WebSearch for more (skip churchofjesuschristtemples.org results, already exhausted), download with `gallery.py pull --url`, judge identically. Still short: write the shortfall note.
6. Write `staging/{slug}/selection.json` (shape documented in the README; `edits` is a plain list of image filenames), run `place.py --temple X --report-only`, check the printed plan, then run it for real.
7. After all folders: summarize the run in chat with per-temple counts (clean and edits/), shortfalls, and anything Evan should eyeball first.

## Quality bar

- **Resolution** (script-enforced): long edge >= 1200 px, short edge >= 800 px. Prefer >= 1600 long when the gallery allows; note in the report when settling for less.
- **Framing**: the whole temple must be in frame; fail any image where part of the building (a wing end, the spire tip, the base) is cut off by the frame edge (Evan's rule, 20 Aug 2026).
- **Angle**: two visible wall planes with converging horizontals (two-point perspective), spire visible top to bottom, eye level to slight elevation. Fail front elevations, extreme telephoto flattening, worm's-eye tilts that distort proportions, and drone top-downs.
- **Obstruction tiers** (tightened by Evan, 20 Aug 2026, second sweep):
  - Minor (PASS clean, stays in `refs/` top level): ONLY objects that do not overlap the building fabric at all — fences, hedges, and plantings that stay below the building line; lampposts and flagpoles against sky; tree crowns fully beside the silhouette; plus at most a single thin pole crossing the facade. The line-art prompt works around these.
  - Moderate (PASS+EDIT, goes flat into `refs/edits/`): ANY foliage or object overlapping the building itself — a tree crown crossing the base line, branches in front of a wall or corner, shrubs covering lower-story stone. "It's only the lower story" does not excuse it. Requires the hidden architecture to be recoverable from visible repetition or symmetry in the same photo. No prompt file is written; the verdict reason in the report records what needs removing.
  - Heavy (backfill would be guesswork): FAIL and find other images. Only when the gallery has nothing better AND other pulled images clearly show the occluded parts, keep it as PASS+EDIT and name those covering images in the verdict reason.

## Render verification (announced and under-construction temples)

Websites mislabel renders; a page can caption another temple's rendering with this temple's name. Before any render becomes a ref:

1. **Default source**: the Official fancybox section on the temple's OWN page at churchofjesuschristtemples.org (captioned Intellectual Reserve). That section is per-temple and is trusted.
2. **Web-sourced renders** (only when the Official section is empty): require corroboration before accepting. The image must appear attached to THIS temple's name on an official Church source (Church Newsroom announcement, temple details page on churchofjesuschristtemples.org) and match any published description of the design. One random blog or news thumbnail is not enough.
3. **Cross-check the design**: temples announced around the same time share render styles. If anything about the render conflicts with what is known about this temple (location terrain, announced size, spire count), or the same image appears on another temple's page, reject it.
4. **When in doubt, leave it out.** A `**` marker and a shortfall note beat a wrong render, because a wrong render becomes a wrong drawing.

Record the corroborating source URLs in the report for any web-sourced render.

## Corrections after placement

A rule change can force re-judging refs already in READY. Never rewrite that folder's `report (auto).md`; it records what the first pass decided and the no-overwrite rule stands. Move each reclassified image into or out of `refs/edits/`, then write `report correction (auto).md` beside the original naming every change and why. The correction file supersedes the original wherever they disagree. (Folders processed before 25 Aug 2026 were migrated from the old per-image `edits/{stem}/` prompt layout; each carries a `layout migration (auto).md` recording that move.)

Name every working file with the temple slug, images and scripts alike, inside a per-temple subdirectory. Generic scratchpad names have already caused one temple's crops to be read as another's, and two parallel audits to overwrite each other's mover script. This bites hardest when several temples are handled at once.

## Hard rules

- Never overwrite existing files in a temple folder. Never rename Evan's folders or files, with exactly one exception: the trailing asterisk markers, which place.py sets via the selection's `mark` field per the marker rules above. Billings-style `References/` dirs are used as-is.
- Existing markers stay through the move to READY unless the marker rules say to update them.
- All file operations happen inside the Python scripts via pathlib (folder names contain spaces and literal `*`); never move or copy these folders with shell commands.
- Images are private drawing references. Never publish or redistribute them; reports keep the photographer credit lines.
- Rejected images never leave staging. `gallery.py clean` wipes a temple's staging after its folder is safely in READY.
- Do not touch Lease End files or projects, ever.
