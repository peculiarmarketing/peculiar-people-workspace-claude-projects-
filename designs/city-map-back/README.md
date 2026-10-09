# City map back print

Started 8 October 2026. A street map of a Church history site or any city, printed on the back of the garment inside a bolder frame, with `CITY, STATE` (or `CITY, COUNTRY`) small in the bottom right corner. The front is the box logo with the temple's coordinates. Cities only for now; mission-boundary designs are set aside. Nauvoo and Salt Lake City are live (8 October 2026); see Publishing below.

Mockups live on the design canvas "City Map Back Prints" on claude.ai (private to Evan): https://claude.ai/artifact/G2aUish7Jaz8CngTkvGkAF

## Decided so far (Evan, 8 October 2026)

- **Full-bleed crop.** Streets fill a fixed rectangle and are cut at the frame. Every design has the same frame; each place gets its own centre and zoom.
- **Frame size 13.5 x 18 in.** Fits the back print area of the tee (14.62 x 18.39), crew (13.74 x 18.38) and hoodie (13.78 x 18.47) with one file. The frame border is 2.5 mm, drawn on the map's outer edge.
- **City label inside the frame**, bottom right, on a knocked-out patch: Oswald 500, 0.25 in type with 0.16 em letter spacing, 0.25 in in from the frame.
- **Temple marker: the halo.** Streets cleared in a 0.32 in radius circle, a 1 mm ring at 0.22 in, a 0.06 in centre dot. No marker when no temple is in frame. Dot, dot-with-name and no-marker versions were rejected.
- **Line weight by place size.**
  - Big or busy cities: every street at 0.5 mm, with the frame as wide as it can go before streets merge. San Antonio holds to about 35 km across, Salt Lake to about 22 km (widened to 24.5 km on 9 October 2026, with Davis County loaded, so the Temple Quarry marker clears the city label; 5.3 percent fused).
  - Small towns, townships and rural sites: 1.5 mm.
  - Which is which is set by hand (`"busy": true` in `places.json`): the fused-ink measure picks a busy city's width but cannot tell a town from busy countryside (rural Fayette scores higher at 1.5 mm than the city of Quincy). Busy so far: San Antonio, Salt Lake City, Independence, Council Bluffs, Liberty, Quincy.
- **The more streets the better**, as long as the frame does not pull in a whole other city. Kirtland went from 3.5 km to 6 km and Nauvoo from 3 km to 4 km for that reason.
- **Crop for streets, keep some blank.** Empty ground (lake, desert, mountains) is good contrast in moderation. Salt Lake's frame moved about 3 km south and 1 km east so the empty lake and airport corner at the top left mostly drops out and more of the valley comes in, with the mountains on the right kept.
  - Highway-only maps and the tight 4 to 5 km city crops were rejected. 0.3 mm was tried and rejected because it is below every print method's minimum.
- **Front: box logo with the temple's coordinates set into the box ("3A closed"), 6 in wide, centred.** The box around PECULIAR stays whole except for two breaks: latitude in the top edge at the left, longitude in the bottom edge at the right, each with about 2 mm of clear space to the line ends. Decimal degrees to four places (about 11 m). Lettering is the original logo, untouched. Coordinates are Oswald 500, 0.8 mm strokes at the 6 in front size; weight 400 measured 0.45 mm and would not print on the tee. Rejected along the way: streets inside the box (too thin to print, and the street lines read as extra strokes in the thin PECULIAR letters), and corner-mark, tick, dashed, halo and scale-bar versions of the box.
- **Every street, not highways.** The look Evan wants is intricate: individual streets readable, not white blobs.

## Numbered landmark markers (9 October 2026)

Church history maps carry numbered markers that match the numbered On the Map list on the product page. The list of places lives in `history/<place>-markers.json` and is drawn by `draw_markers()` in `build_map_back.py`: a dot (0.06 in radius) with the number (Oswald 500, 0.29 in, about 1 mm strokes, 6 mm tall) directly above it, about 1.8 mm above the dot (Evan asked for 1 mm more space), both ringed by 2 mm of cleared streets (Evan, 9 October 2026: 10 percent bigger twice over the first 0.24 in, numbers directly above the dot). A temple keeps its halo and gets its number above the ring. A number moves only when the spot above is taken by another marker, the halo, the frame or the label, or when its marker names a side (`"label_at": "right"`, used for Mendon 1, whose spot above is a road). Places closer than 0.35 in on the print share one number. A place whose spot is uncertain is graded approximate or traditional in the file and says so in its list item. Plain city maps have no markers.

## Thin lines in crowded patches (9 October 2026)

Evan: where 1.5 mm streets crowd together into solid white (tight lakeside rows, a village core), draw those patches at 0.5 mm and keep everything else at 1.5 mm. `dense_field()` in `build_map_back.py` renders the map at full weight, closes every gap narrower than 1.5 mm, and marks the places where those closed-up gaps are dense as crowded patches. A smooth field then scales each line's width from 1.5 mm in open country down to 0.5 mm inside a patch, easing over about 0.2 in, so a road thins gradually. Patches under 0.2 sq in are lone knots on an ordinary road and keep the full weight, since thinning them reads as a glitch. Busy cities are already at 0.5 mm and are skipped. A place can set `"dense_line_mm"` (0 turns it off), and `--no-thin` turns it off for a run. Fayette: 7 percent of the map thinned, fused ink 16.8 to 8.8 percent. The thin patches print at 0.5 mm, under the 0.71 mm DTG minimum for the tee, the same as Salt Lake City (see HANDOFF, sample tee).

## Hand-drawn lines

Every map is drawn in the hand-drawn style (Evan, 8 October 2026; `--plain` gives the old even lines). Each street's width wanders either way like pen pressure: 40 percent for small towns, 10 percent for busy cities (a place can set its own `"swing"`, and `--swing` overrides it). Dead ends taper to a point over about seven line widths, in the spirit of the temple line art. The wobble is a smooth field over the page, so two streets meeting at a junction agree on width there. An end only tapers when no other street touches it: in the road data a side street often meets a main road partway along without sharing a point, and tapering those ends would leave gaps at junctions. Polygon fill adds about half a pixel per side, so each half-width is reduced by that much to keep the average weight where it was. Product copy must not call the art hand drawn (BRAND.md section 17); it is drawn by code.

## How "as wide as it holds" is measured

Fused ink is the share of the ink that has merged into solid patches wider than a single road line (a morphological opening on the 100 ppi preview). Round 1's whole-city San Antonio map was about 50 percent fused and read as large white sections. The limit is about 6 percent: San Antonio at 35 km is 5.8, at 40 km it is 8.4 and visibly hazing.

`--auto` bisects for the widest frame at or under 6 percent. Treat it as a starting point and look at the result: around mountains, lakes or a county edge the measure plateaus. Salt Lake's auto answer is 27.7 km, but past about 22 km the frame runs into Davis County, which is not loaded.

## Data

Road files are the Census Bureau's TIGER/Line 2024 roads: public domain, with road classes. That is what drops sidewalks, service drives and alleys, which in OpenStreetMap data doubled every Salt Lake street and filled in the blocks. TIGER only covers the US. Abroad (Preston) still needs OpenStreetMap through `city-maps/fetch_map.py`, which brings the ODbL credit requirement with it.

Kept road classes (MTFCC): S1100 interstates, S1200 US and state highways, S1630 ramps, S1400 local streets.

## Church history sites

`add_sites.py` adds every site in `city-maps/church-history-sites.md` to `places.json`. Each town is framed to its own boundary (3:4, 5 percent margin), so the map takes in the whole town and not the next one; sites with no town use their 6 km square. Every county the frame touches is loaded, so roads run to the frame edge. River towns on a state line leave out the far bank (Council Bluffs drops Omaha, Quincy drops Missouri, Carthage drops Iowa), so the map ends at the river. A temple in frame gets the halo and the coordinates front; with no temple the front is the plain box logo. Temples in frame: Nauvoo, Kirtland, Palmyra (Palmyra township, Manchester, Sacred Grove), Winter Quarters, Salt Lake. Preston, England is not built: TIGER is US only, and the OpenStreetMap download servers were unreachable on 8 October.

## Product stages

Every place in `places.json` has a `status`: **designed** (art built, not reviewed), **review** (the full product package is made: print files per garment, gallery cards, history section; waiting on Evan), **ready** (Evan confirmed; it may go on products), **live** (on the store). `map_run.py <place> --review` builds the package and a review sheet, `--confirm` marks it ready once Evan approves, `--apply` refuses anything below ready, and a full publish marks it live. 9 October 2026: Nauvoo and Salt Lake City live, Kirtland and Sharon ready (confirmed by Evan), the rest in review (packages built; history sections still to write, see HANDOFF.md).

## Publishing (product page)

Each map publishes on the tee, crewneck and hoodie through `temple-product-generator/scripts/map_run.py`, which runs the temple pipeline's own Tapstitch and Shopify calls with the map art. Nauvoo is the first, as a live test (8 October 2026).

- **Title:** the garment's line name with Map for Temple, place in brackets: "Essential Heavyweight Map Tee (Nauvoo)", "Ultra-soft Map Sweatshirt (Nauvoo)", "Ultra-soft Oversized Map Hoodie (Nauvoo)". The product page shows it the way a temple page does: the theme cuts the title at the bracket and puts the place line underneath ("Nauvoo, Illinois", from the `peculiar.temple_city` and `temple_state` metafields; no temple name, no dedication date).
- **No temple information section.** The temple facts block is temple-specific and does not appear.
- **Product details section: the same** as the temple products (the fixed sections copied in byte-identical, as those stored blocks always are).
- **Church history section, only for Church history sites** (`"history": true` in `places.json`; plain cities such as San Antonio do not get one). It lives in `history/<place>.html` as a `<section class="site-history">` fragment and renders as collapsed rows like the temple facts. It is researched and fact-checked to the same source hierarchy as the temple facts (BRAND.md section 12, the temple-fact-checker skill's standard; sources and dropped claims in `history/<place>-sources.md`), and as new prose it gets the humanizer and structural-humanizer passes (CLAUDE.md). The one-line notes in `church-history-sites.md` are orientation only, not a source. `map_run.py` refuses to publish a history site without its fragment.
- **A band that draws the map**, the way temple product pages draw the temple. `web_map_drawing.py` writes each map in the temple band's own format (`pp-map-<place>.json` strokes in pen order plus `pp-map-<place>.webp` finished art), so the existing `pp-pen-draw.js` player runs it. The theme's `pp-temple-drawing` section reads a `map:<place>` tag as well as `temple:`, and `map_run.py` uploads the section and the two files with a checksum read-back. Every map fits the temple budget of 250,000 bytes gzipped (San Antonio 244 KB, most small towns under 100 KB).
- **One card per garment, a dropdown for the rest:** Salt Lake City is the map line's parent (published with `--parent`, tag `listing:parent`), so it is the map card in the Tees, Sweatshirts and Hoodies collections; every other map is reached through the Easify Map dropdown on it (sets Map Tee, Map Sweatshirt, Map Hoodie, written by `easify_options.py sync --maps-only`, imported by hand).
- **Tags and collection:** `map:<place>`, `line:map` and `apparel:<garment>`, and none of the temple tags. The temple collections are smart collections on `garment:` and `country:` tags, and the homepage marquee reads the temple tee collection, so a temple tag would put a map in the temple marquee. Map products collect in their own smart collection, Church History Maps (`church-history-maps`, rule: tag `line:map`).
- **Print size:** the 13.5 x 18 in map is scaled per garment to the largest size that keeps the pipeline's 0.25 in safe margin (tee 13.4 in wide, crew 13.2, hoodie 13.3), a quarter of the spare height above. The front is the coordinates logo placed like the plain logo: 6.0 in of ink wide, 3.0 in down.
- **Design cards:** the map, and the coordinates logo when the front has temple coordinates, in black on white like the temple line-art card, at gallery positions 2 and 3 (alt text "City map art close-up - <City>" and "Coordinates logo close-up - <City>").
- **Page template:** `product.map` (in the temple repo's `theme/templates/`), the product template without the temple Reference / Final drawing slider, with the suggestion row reading "Don't see your city?" and the suggestion section asking for "a map of a city or Church history site we haven't made yet".
- **Not done for maps:** the on-model gallery (it composites onto blank garment photos kept only on the Mac; until it runs there, the products show Tapstitch's mockups), and the temple-only steps (art card, Temple Art File option, Easify row, marquee).

## Running it

```bash
python3 designs/city-map-back/build_map_back.py san-antonio nauvoo
python3 designs/city-map-back/build_map_back.py san-antonio --auto --preview-only
python3 designs/city-map-back/build_map_back.py --all
```

Places are in `places.json` (counties by FIPS code, centre, width, line weight, temple). County road files download once to `city-maps/data/tiger/`, which is gitignored. Output goes to `out/<place>/`, also gitignored: a 100 ppi preview, a 300 ppi back print PNG (4050 x 5400) and a 300 ppi front PNG (the logo with coordinates, 6 in wide), white ink on transparent with every pixel's colour set to white. The back print includes the frame and the city label.

## Still open

- Decided 9 October 2026: two kinds of map, Church history sites (with a history section) and plain city maps (none). San Antonio is a plain city product, and every city with a temple product will get one. Historical period maps were tested and declined; maps stay on today's TIGER roads. Recorded in BRAND.md.
