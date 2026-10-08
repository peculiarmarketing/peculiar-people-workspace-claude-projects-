# City map back print

Started 8 October 2026. A street map of a church history site, mission city or any city, printed on the back of the garment inside a bolder frame, with `CITY, STATE` (or `CITY, COUNTRY`) small in the bottom right corner. Front carries the box logo or a map-inspired mark (not decided). Exploration only: nothing is on Tapstitch or the store.

Mockups live on the design canvas "City Map Back Prints" on claude.ai (private to Evan): https://claude.ai/artifact/G2aUish7Jaz8CngTkvGkAF

## Decided so far (Evan, 8 October 2026)

- **Full-bleed crop.** Streets fill a fixed rectangle and are cut at the frame. Every design has the same frame; each place gets its own centre and zoom.
- **Frame size 13.5 x 18 in.** Fits the back print area of the tee (14.62 x 18.39), crew (13.74 x 18.38) and hoodie (13.78 x 18.47) with one file.
- **Temple marker: the halo.** Streets cleared in a 0.32 in radius circle, a 1 mm ring at 0.22 in, a 0.06 in centre dot. No marker when no temple is in frame. Dot, dot-with-name and no-marker versions were rejected.
- **Line weight by place size.**
  - Big or busy cities: every street at 0.5 mm, with the frame as wide as it can go before streets merge. San Antonio holds to about 35 km across, Salt Lake to about 22 km.
  - Small towns (Nauvoo, Kirtland and the like): 1.5 mm.
- **The more streets the better**, as long as the frame does not pull in a whole other city. Kirtland went from 3.5 km to 6 km and Nauvoo from 3 km to 4 km for that reason.
- **Crop for streets, keep some blank.** Empty ground (lake, desert, mountains) is good contrast in moderation. Salt Lake's frame moved about 3 km south and 1 km east so the empty lake and airport corner at the top left mostly drops out and more of the valley comes in, with the mountains on the right kept.
  - Highway-only maps and the tight 4 to 5 km city crops were rejected. 0.3 mm was tried and rejected because it is below every print method's minimum.
- **Front: box logo with the temple's coordinates set into the box ("3A closed").** The box around PECULIAR stays whole except for two breaks: latitude in the top edge at the left, longitude in the bottom edge at the right, each with about 2 mm of clear space to the line ends. Decimal degrees to four places (about 11 m). Lettering is the original logo, untouched. Coordinates are Oswald 500, 0.8 mm strokes at the 6 in front size; weight 400 measured 0.45 mm and would not print on the tee. At chest size (3.75 in) the strokes drop to about 0.5 mm, so a chest version needs bolder coordinates. Rejected along the way: streets inside the box (too thin to print, and the street lines read as extra strokes in the thin PECULIAR letters), and corner-mark, tick, dashed, halo and scale-bar versions of the box.
- **Every street, not highways.** The look Evan wants is intricate: individual streets readable, not white blobs.

## How "as wide as it holds" is measured

Fused ink is the share of the ink that has merged into solid patches wider than a single road line (a morphological opening on the 100 ppi preview). Round 1's whole-city San Antonio map was about 50 percent fused and read as large white sections. The limit is about 6 percent: San Antonio at 35 km is 5.8, at 40 km it is 8.4 and visibly hazing.

`--auto` bisects for the widest frame at or under 6 percent. Treat it as a starting point and look at the result: around mountains, lakes or a county edge the measure plateaus. Salt Lake's auto answer is 27.7 km, but past about 22 km the frame runs into Davis County, which is not loaded.

## Print risk at 0.5 mm

The design-audit rule library puts the line minimum at 0.71 mm for DTG on dark garments (the tee) and 0.5 mm absolute for DTF (crew and hoodie). 0.5 mm is under the tee's guideline and exactly at the fleece floor. Order a sample tee and hoodie of one 0.5 mm design and wash them before committing a line to it.

## Data

Road files are the Census Bureau's TIGER/Line 2024 roads: public domain, with road classes. That is what drops sidewalks, service drives and alleys, which in OpenStreetMap data doubled every Salt Lake street and filled in the blocks. TIGER only covers the US. Abroad (Preston) still needs OpenStreetMap through `city-maps/fetch_map.py`, which brings the ODbL credit requirement with it.

Kept road classes (MTFCC): S1100 interstates, S1200 US and state highways, S1630 ramps, S1400 local streets.

## Running it

```bash
python3 designs/city-map-back/build_map_back.py san-antonio nauvoo
python3 designs/city-map-back/build_map_back.py san-antonio --auto --preview-only
```

Places are in `places.json` (counties by FIPS code, centre, width, line weight, temple). County road files download once to `city-maps/data/tiger/`, which is gitignored. Output goes to `out/<place>/`, also gitignored: a 100 ppi preview, a 300 ppi back print PNG (4050 x 5400) and a 300 ppi front PNG (the logo with coordinates, 6 in wide), white ink on transparent with every pixel's colour set to white. The frame border and city label are drawn on the canvas for now and get baked into the print file once the layout is final.

## Still open

- **San Antonio mission boundaries.** The area is now split into Texas San Antonio North and South missions (new missions effective 1 July 2026). The boundaries are not public. The canvas mission boards use county lines as a clearly labelled stand-in until Evan supplies the real line (a stake list or a map screenshot).

- **Label placement:** inside the frame (knockout) or outside, below the corner. Not picked.
- **Temple positions** in `places.json` are from OpenStreetMap or approximate; verify before shipping.
- Which places become products, and whether this becomes its own line in BRAND.md.
