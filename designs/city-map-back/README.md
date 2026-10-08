# City map back print

Started 8 October 2026. A street map of a Church history site or any city, printed on the back of the garment inside a bolder frame, with `CITY, STATE` (or `CITY, COUNTRY`) small in the bottom right corner. The front is the box logo with the temple's coordinates. Cities only for now; mission-boundary designs are set aside. Nothing is on Tapstitch or the store yet.

Mockups live on the design canvas "City Map Back Prints" on claude.ai (private to Evan): https://claude.ai/artifact/G2aUish7Jaz8CngTkvGkAF

## Decided so far (Evan, 8 October 2026)

- **Full-bleed crop.** Streets fill a fixed rectangle and are cut at the frame. Every design has the same frame; each place gets its own centre and zoom.
- **Frame size 13.5 x 18 in.** Fits the back print area of the tee (14.62 x 18.39), crew (13.74 x 18.38) and hoodie (13.78 x 18.47) with one file. The frame border is 2.5 mm, drawn on the map's outer edge.
- **City label inside the frame**, bottom right, on a knocked-out patch: Oswald 500, 0.25 in type with 0.16 em letter spacing, 0.25 in in from the frame.
- **Temple marker: the halo.** Streets cleared in a 0.32 in radius circle, a 1 mm ring at 0.22 in, a 0.06 in centre dot. No marker when no temple is in frame. Dot, dot-with-name and no-marker versions were rejected.
- **Line weight by place size.**
  - Big or busy cities: every street at 0.5 mm, with the frame as wide as it can go before streets merge. San Antonio holds to about 35 km across, Salt Lake to about 22 km.
  - Small towns, townships and rural sites: 1.5 mm.
  - Which is which is set by hand (`"busy": true` in `places.json`): the fused-ink measure picks a busy city's width but cannot tell a town from busy countryside (rural Fayette scores higher at 1.5 mm than the city of Quincy). Busy so far: San Antonio, Salt Lake City, Independence, Council Bluffs, Liberty, Quincy.
- **The more streets the better**, as long as the frame does not pull in a whole other city. Kirtland went from 3.5 km to 6 km and Nauvoo from 3 km to 4 km for that reason.
- **Crop for streets, keep some blank.** Empty ground (lake, desert, mountains) is good contrast in moderation. Salt Lake's frame moved about 3 km south and 1 km east so the empty lake and airport corner at the top left mostly drops out and more of the valley comes in, with the mountains on the right kept.
  - Highway-only maps and the tight 4 to 5 km city crops were rejected. 0.3 mm was tried and rejected because it is below every print method's minimum.
- **Front: box logo with the temple's coordinates set into the box ("3A closed"), 6 in wide, centred.** The box around PECULIAR stays whole except for two breaks: latitude in the top edge at the left, longitude in the bottom edge at the right, each with about 2 mm of clear space to the line ends. Decimal degrees to four places (about 11 m). Lettering is the original logo, untouched. Coordinates are Oswald 500, 0.8 mm strokes at the 6 in front size; weight 400 measured 0.45 mm and would not print on the tee. Rejected along the way: streets inside the box (too thin to print, and the street lines read as extra strokes in the thin PECULIAR letters), and corner-mark, tick, dashed, halo and scale-bar versions of the box.
- **Every street, not highways.** The look Evan wants is intricate: individual streets readable, not white blobs.

## How "as wide as it holds" is measured

Fused ink is the share of the ink that has merged into solid patches wider than a single road line (a morphological opening on the 100 ppi preview). Round 1's whole-city San Antonio map was about 50 percent fused and read as large white sections. The limit is about 6 percent: San Antonio at 35 km is 5.8, at 40 km it is 8.4 and visibly hazing.

`--auto` bisects for the widest frame at or under 6 percent. Treat it as a starting point and look at the result: around mountains, lakes or a county edge the measure plateaus. Salt Lake's auto answer is 27.7 km, but past about 22 km the frame runs into Davis County, which is not loaded.

## Data

Road files are the Census Bureau's TIGER/Line 2024 roads: public domain, with road classes. That is what drops sidewalks, service drives and alleys, which in OpenStreetMap data doubled every Salt Lake street and filled in the blocks. TIGER only covers the US. Abroad (Preston) still needs OpenStreetMap through `city-maps/fetch_map.py`, which brings the ODbL credit requirement with it.

Kept road classes (MTFCC): S1100 interstates, S1200 US and state highways, S1630 ramps, S1400 local streets.

## Church history sites

`add_sites.py` adds every site in `city-maps/church-history-sites.md` to `places.json`. Each town is framed to its own boundary (3:4, 5 percent margin), so the map takes in the whole town and not the next one; sites with no town use their 6 km square. Every county the frame touches is loaded, so roads run to the frame edge. River towns on a state line leave out the far bank (Council Bluffs drops Omaha, Quincy drops Missouri, Carthage drops Iowa), so the map ends at the river. A temple in frame gets the halo and the coordinates front; with no temple the front is the plain box logo. Temples in frame: Nauvoo, Kirtland, Palmyra (Palmyra township, Manchester, Sacred Grove), Winter Quarters, Salt Lake. Preston, England is not built: TIGER is US only, and the OpenStreetMap download servers were unreachable on 8 October.

## When these become products

Each map publishes on the tee, crewneck and hoodie like the temple products. Each product description gets a Church history section about the place on the map (what happened there and when), researched and fact-checked to the same source hierarchy as the temple facts section (BRAND.md section 12, the temple-fact-checker skill's standard: no fact ships without a source that clears it, and folklore is checked against the known-myths list). It is new prose, so it gets the humanizer and structural-humanizer passes before it ships (CLAUDE.md). The one-line notes in `city-maps/church-history-sites.md` are for orientation only and are not a source.

## Running it

```bash
python3 designs/city-map-back/build_map_back.py san-antonio nauvoo
python3 designs/city-map-back/build_map_back.py san-antonio --auto --preview-only
python3 designs/city-map-back/build_map_back.py --all
```

Places are in `places.json` (counties by FIPS code, centre, width, line weight, temple). County road files download once to `city-maps/data/tiger/`, which is gitignored. Output goes to `out/<place>/`, also gitignored: a 100 ppi preview, a 300 ppi back print PNG (4050 x 5400) and a 300 ppi front PNG (the logo with coordinates, 6 in wide), white ink on transparent with every pixel's colour set to white. The back print includes the frame and the city label.

## Still open

- Which places become products, and whether this becomes its own line in BRAND.md.
