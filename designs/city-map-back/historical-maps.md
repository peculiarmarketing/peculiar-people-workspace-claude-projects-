# Historical maps of the Church history sites

Research for map backs drawn from period maps instead of today's TIGER roads. Done 9 October 2026. Nothing here is a decision; see "Questions for Evan" at the end. Samples and their license manifest are in `historical/samples/`.

## Summary

**What is realistic.** No source gives us vector streets for these places as they were in the Church era, except Salt Lake City in OpenHistoricalMap. What does exist is scanned period maps, and the Library of Congress (LoC) holds good ones for about half the places: an 1847 plat of Salt Lake City, and 1850s county wall maps whose town insets draw Nauvoo, Palmyra, Carthage, Hiram and Sharon street by street. These can be traced by hand or semi-automatically into our line style. A traced historical map would have far fewer lines than our current maps (Nauvoo 1859 is about 150 blocks; Palmyra 1853 is about 15 streets), so it reads as a plat, not the dense web Evan picked. That is a design question, not a data one.

The era gap matters. Most "period" maps are 15 to 30 years after the Saints left (1850s county maps for New York and Ohio towns settled in the 1820s and 1830s). For Nauvoo and Salt Lake City the gap is harmless because the grid was laid out by the Saints and did not change. For Palmyra, Kirtland and Hiram the main streets and roads existed in the Saints' time, but some buildings and side streets on the 1850s map came later. The Missouri sites, the Iowa camps, Winter Quarters and Martin's Cove have almost nothing usable: either the map is of a plan that was never built, or it is held by the Church with rights reserved, or it simply was not found.

**Best opportunities, ranked**

1. **Salt Lake City, 1847 Sherwood plat (LoC).** The first map of the city, drawn in August 1847 on sheepskin: 135 numbered square blocks with the temple block marked. Public domain scan, 4328 x 6503 px. Perfect for tracing: a clean grid. Matches the Saints' era exactly. OHM also has 38 dated Salt Lake streets in our frame, enough to cross-check.
2. **Nauvoo, 1859 Hancock County map "City of Nauvoo" inset (LoC).** Every block of the flats and the bluff, street names, "Temple Ruins", the Mansion, Seventies Hall, Joseph Smith's homestead. Public domain, the inset is about 2300 x 1700 px at full resolution. The grid is the one the Saints platted, so it is era-true. The 1842 Gustavus Hills "Map of the City of Nauvoo" is the real period map (NYPL calls it public domain), but NYPL's site blocked our requests (see Failed requests).
3. **Palmyra, 1853 Wayne County map "Plan of Palmyra" inset (LoC).** Main, Canal, Church, Jackson, Canandaigua, Vienna streets, the Erie Canal, the cemetery. Public domain. Village-scale only; the Smith farm, Sacred Grove and Hill Cumorah are outside the inset (the county map shows them only as rural roads and owner names).
4. **Kirtland, 1857 Geauga and Lake counties map (LoC).** Kirtland township with its roads, the flats, "Kirtland P.O." and the river, at about 1.3 in per mile on the original. Public domain. Rural roads trace well. The 1833 Kirtland plat (Church History Library, via the Joseph Smith Papers) is more famous but is a city plan that was largely not built, and its scan is "All rights reserved".
5. **Independence, the 1833 Plat of the City of Zion.** The most recognisable Latter-day Saint city plan: 49 square blocks, a mile square, 132 ft streets, temple blocks in the centre. The scan is © Intellectual Reserve (needs Church permission), but the plan is simple geometry described in words on the plat itself; we could draw our own version from the stated dimensions without copying the scan. It was never built, so it is a "the city that was planned" design, not a map of a place. Needs Evan's call (and probably a quick IP check).
6. **Carthage, 1859 Hancock County map, Carthage inset (LoC).** Same map as Nauvoo; the town of the jail, 15 years after 1844. Small inset. Public domain.
7. **Sharon, 1855 Windsor County map, Sharon inset (LoC).** Public domain. Note the Smith birthplace is in the hills south of the village, so the county map's rural roads are more relevant than the inset.
8. **Bird's-eye views: Salt Lake City 1870 and 1875, Independence 1868, Council Bluffs 1868, Omaha 1868 (LoC).** Public domain, large (up to 10784 x 8978). Perspective drawings, not to scale: usable only as an image (a print or a different product), not traceable into our frame.

**What is commercially safe.** LoC Geography and Map Division scans: yes. Every item checked says "free to use and reuse unless a Rights Advisory statement is present", and none of ours has one. USGS topo maps: yes (public domain), but the earliest editions are 1885 to 1954, far too late to be period maps. OpenHistoricalMap: yes (CC0 unless a feature says otherwise). NYPL's 1842 Nauvoo map: NYPL says public domain in the US, but we could not reach the image. Joseph Smith Papers and Church History Library images: not without permission (footer "© 2026 by Intellectual Reserve, Inc. All rights reserved."; the library's own guide routes Church-owned material to the Intellectual Property Office, about 45 days). David Rumsey: no (CC BY-NC-SA, non-commercial).

## Per place

"Traceable" means the map draws streets or roads as lines we could redraw in our style inside a frame. "Image only" means it could only be used as a picture. Every LoC item below has the rights text quoted under Licenses, at the item URL given.

### Sharon, Vermont (1805)

| Best map | Date | Holder | URL | License | Format | Traceable |
|---|---|---|---|---|---|---|
| Map of Windsor County, Vermont (Sharon inset plus township roads) | 1855 | LoC | https://www.loc.gov/item/2012586225/ | LoC free to use | JP2 13547 x 16471, IIIF | Yes (rural roads; 50 years late) |
| USGS Strafford quad, 1:62,500 | 1896 | USGS | topoView / TNM API | Public domain | GeoTIFF | Yes, but 90 years late |

### Whitingham, Vermont (1801)

| Best map | Date | Holder | URL | License | Format | Traceable |
|---|---|---|---|---|---|---|
| McClellan's map of Windham County, Vermont (no Whitingham inset listed; township roads) | 1856 | LoC | https://www.loc.gov/item/2012586226/ | LoC free to use | JP2 13408 x 16136 | Yes (rural roads) |
| USGS Wilmington quad, 1:62,500 | 1889 | USGS | topoView | Public domain | GeoTIFF | Yes, late |

### Palmyra village, Palmyra township, Manchester, Sacred Grove, Hill Cumorah, New York (1816 to 1831)

| Best map | Date | Holder | URL | License | Format | Traceable |
|---|---|---|---|---|---|---|
| Map of Wayne County, New York (H.F. Walling), "Plan of Palmyra" inset | 1853 | LoC | https://www.loc.gov/item/2009579478/ | LoC free to use | JP2 17182 x 11540; sample crop 2250 x 1300 | Yes (village streets) |
| Map of Ontario County, New York (Manchester, the Smith farm area, Cumorah) | 1852 | LoC | https://www.loc.gov/item/2006636780/ | LoC free to use | JP2 14487 x 11888 | Yes (rural roads) |
| Map of Ontario County, New York (28 village insets) | 1859 | LoC | https://www.loc.gov/item/2013593229/ | LoC free to use | JP2 17941 x 18470 | Yes |
| Gillette's map of Wayne Co. | 1858 | LoC | https://www.loc.gov/item/2009583838/ | LoC free to use | not measured | Yes |
| Sanborn, Palmyra | 1884, 1889 | LoC | https://www.loc.gov/item/sanborn06158_001/ | Public domain | Sheets | Building level, too late and too detailed |

### Fayette, New York (1829 to 1831)

| Best map | Date | Holder | URL | License | Format | Traceable |
|---|---|---|---|---|---|---|
| Topographical map of Seneca County, New York | 1852 | LoC | https://www.loc.gov/item/2013593233/ | LoC free to use | JP2 10901 x 16037 | Yes (rural roads; insets are Waterloo, Seneca Falls, Ovid, not Fayette) |
| Map of Seneca County, New York (with an inset of the 1838 Burr county map) | 1858 | LoC | https://www.loc.gov/item/2013593272/ | LoC free to use | JP2 11168 x 16189 | Yes |

### Mendon, New York (1829 to 1833)

| Best map | Date | Holder | URL | License | Format | Traceable |
|---|---|---|---|---|---|---|
| Map of Monroe County, New York | 1852 | LoC | https://www.loc.gov/item/2013593227/ | LoC free to use | not measured (item JSON came back truncated) | Yes (rural roads) |
| Gillette's map of Monroe Co. | 1858 | LoC | https://www.loc.gov/item/2015585062/ | LoC free to use | not measured | Yes |

### Colesville and Afton (South Bainbridge), New York (1826 to 1831)

| Best map | Date | Holder | URL | License | Format | Traceable |
|---|---|---|---|---|---|---|
| Map of Broome County, New York (Colesville) | 1855 | LoC | https://www.loc.gov/item/2013593069/ | LoC free to use | JP2 17873 x 12407 | Yes (rural roads) |
| Map of Chenango County, New York (Afton, then Bainbridge) | 1855 | LoC | https://www.loc.gov/item/2012593650/ | LoC free to use | JP2 15959 x 16942 | Yes |

### Harmony, Pennsylvania (1827 to 1830)

| Best map | Date | Holder | URL | License | Format | Traceable |
|---|---|---|---|---|---|---|
| Map of Susquehanna Co., Pennsylvania (19 borough insets) | 1858 | LoC | https://www.loc.gov/item/2012592185/ | LoC free to use | JP2 17604 x 16851 | Yes (rural roads along the river) |

### Kirtland, Ohio (1831 to 1838)

| Best map | Date | Holder | URL | License | Format | Traceable |
|---|---|---|---|---|---|---|
| Map of Geauga and Lake counties, Ohio (township and a Kirtland inset) | 1857 | LoC | https://www.loc.gov/item/2012591126/ | LoC free to use | JP2 13251 x 17982; sample crop 2250 x 2200 | Yes |
| Plat of Kirtland, Ohio (F.G. Williams; 49 blocks, 974 lots; a plan) | 1833 | Church History Library, via Joseph Smith Papers | https://www.josephsmithpapers.org/paper-summary/plat-of-kirtland-ohio-not-before-2-august-1833/1 | "© 2026 by Intellectual Reserve, Inc. All rights reserved." | JPG on JSP | Yes, but a plan, and needs permission |
| Plat of Kirtland, about 1837 (Beals plat), CHL MS 2569 | c. 1837 | Church History Library | https://catalog.churchofjesuschrist.org/assets?id=5bd72cdd-20c5-48f2-af9e-5323710142ae&crate=0&index=0 | Rights field not read (catalog is a JavaScript app) | not checked | Probably yes |
| JSP modern maps "Portion of Kirtland Township" 1833 and 1838 | modern | Joseph Smith Papers | PDFs linked from the plat page | © Intellectual Reserve | PDF | Reference only |

### Hiram, Ohio (1831 to 1832)

| Best map | Date | Holder | URL | License | Format | Traceable |
|---|---|---|---|---|---|---|
| Map of Portage Co., Ohio (P.J. Browne), "Hiram" inset | 1857 | LoC | https://www.loc.gov/item/2012592242/ | LoC free to use | JP2 15659 x 17112; sample crop 1450 x 1500 | Yes, but only 2 or 3 roads; the township roads on the main map trace better |

### Independence, Missouri (1831 to 1833)

| Best map | Date | Holder | URL | License | Format | Traceable |
|---|---|---|---|---|---|---|
| Plat of the City of Zion (49 blocks, 132 ft streets; never built) | 1833 | Church History Library, via Joseph Smith Papers | https://www.josephsmithpapers.org/paper-summary/plat-of-the-city-of-zion-circa-early-june-25-june-1833/1 | "© 2026 by Intellectual Reserve, Inc. All rights reserved." | JPG 1579 x 2000, 1.0 MB (measured, not kept) | Yes (simple geometry; could be redrawn from its stated dimensions) |
| Revised Plat of the City of Zion | Aug 1833 | Church History Library, via JSP | https://www.josephsmithpapers.org/paper-summary/revised-plat-of-the-city-of-zion-circa-early-august-1833 | © Intellectual Reserve | JPG | Same |
| Bird's eye view of Independence (A. Ruger) | 1868 | LoC | https://www.loc.gov/item/73693478/ | LoC free to use | JP2 8704 x 6976 | Image only |
| Edwards' map of Jackson Co. | 1887 | LoC | https://www.loc.gov/item/2012593037/ | LoC free to use | not measured | Yes, but 55 years late |

### Liberty, Richmond, Far West, Adam-ondi-Ahman, Haun's Mill, Missouri (1833 to 1839)

| Place | Best map | Date | Holder | URL | License | Traceable |
|---|---|---|---|---|---|---|
| Liberty | Map of Clay County, Missouri (G.M. Hopkins) | 1887 | LoC | https://www.loc.gov/item/2012593074/ | LoC free to use; JP2 12986 x 16345 | Yes, 50 years late |
| Richmond | Nothing period found at LoC. USGS Lexington 1:125,000, 1889 | 1889 | USGS | topoView | Public domain | Poorly (small scale) |
| Far West | Original sheepskin plat "Original Platte of Far West" (privately owned per a 1990 Church News report); JSP "Plat of Far West, Missouri, 1838" is a modern reconstruction | 1838 (modern) | JSP | https://www.josephsmithpapers.org/bc-jsp/content/jsp/images/content/library/pdf/D6_Map7_Plat_of_Far_West_MO_1838.pdf (PDF, 214 KB) | © Intellectual Reserve | Yes as a reference; not ours to reproduce |
| Adam-ondi-Ahman | Original plat map, University of Utah Marriott Library (photocopy in the folder, original in reserve, by appointment) | 1838? | U of Utah | https://archivespace.lib.utah.edu/repositories/3/top_containers/19315 | Not stated | Unknown; not digitised |
| Haun's Mill | Nothing found. USGS Braymer quad 1924 | 1924 | USGS | topoView | Public domain | Late |

### Quincy and Carthage, Illinois (1839, 1844); Nauvoo (1839 to 1846)

| Place | Best map | Date | Holder | URL | License | Format | Traceable |
|---|---|---|---|---|---|---|---|
| Nauvoo | Map of Hancock County, Illinois (Holmes & Arnold), "City of Nauvoo" inset | 1859 | LoC | https://www.loc.gov/item/2013593101/ | LoC free to use | JP2 17770 x 16773; sample crop 2300 x 1700 | Yes, excellent |
| Nauvoo | Map of the city of Nauvoo (Gustavus Hills, lith. J. Childs), 1:9,900, streets, block and lot numbers | 1842 | NYPL (Lionel Pincus and Princess Firyal Map Division), listed on DPLA | https://dp.la/item/8cb9dd75353e97817d7e0463800210cf | NYPL: believed public domain in the US (as reported on the DPLA record; we could not open it) | Not reached | Yes, best possible |
| Carthage | Same 1859 Hancock County map, Carthage inset | 1859 | LoC | https://www.loc.gov/item/2013593101/ | LoC free to use | small inset | Yes |
| Quincy | Edwards' map of Adams Co., Illinois | 1889 | LoC | https://www.loc.gov/item/2013593085/ | LoC free to use | JP2 16940 x 16673 | Yes, 50 years late |

### Garden Grove, Mount Pisgah, Council Bluffs (Kanesville), Iowa (1846 to 1852)

| Place | Best map | Date | Holder | URL | License | Traceable |
|---|---|---|---|---|---|---|
| Council Bluffs | Bird's eye view of Council Bluffs | 1868 | LoC | https://www.loc.gov/item/73693392/ | LoC free to use; JP2 8864 x 7056 | Image only |
| Council Bluffs | A.T. Andreas' illustrated historical atlas of Iowa (includes a "Plan of Council Bluffs"; page not checked) | 1875 | LoC | https://www.loc.gov/item/70654676/ | LoC free to use | Probably yes, but 25 years late and Kanesville was replatted |
| Garden Grove, Mount Pisgah | Nothing period found. Camps had no street plan to speak of. OHM has the Mormon Trail line through each. | | | | | No |

### Winter Quarters, Nebraska (1846 to 1848)

| Best map | Date | Holder | URL | License | Traceable |
|---|---|---|---|---|---|
| Thomas Bullock's plan of Winter Quarters (shown in DPLA's Mormon migration source set; holder not confirmed, likely Church History Library) | Dec 1846 | Unconfirmed | https://www.dp.la/primary-source-sets/mormon-migration/sources/1595 | Not read (403) | Probably yes, if obtainable |
| Bird's eye view of Omaha (Florence is off the edge) | 1868 | LoC | https://www.loc.gov/item/73693495/ | LoC free to use | Image only |

### Martin's Cove, Wyoming (1856)

No streets ever existed. The only period-relevant line is the trail itself (OHM has the Mormon Trail and one other dated way here). Not a candidate for a street design.

### Salt Lake City, Utah (1847 to about 1870)

| Best map | Date | Holder | URL | License | Format | Traceable |
|---|---|---|---|---|---|---|
| [Plat of the Great City of the Valley of the Great Salt Lake], H.G. Sherwood, manuscript on sheepskin | 1847 | LoC | https://www.loc.gov/item/2017587026/ | LoC free to use | JP2 4328 x 6503 (5.6 MB); TIFF 169 MB; IIIF info.json saved | Yes, excellent |
| Bird's eye view of Salt Lake City, Utah Territory | 1870 | LoC | https://www.loc.gov/item/75696611/ | LoC free to use | JP2 10784 x 8978 | Image only |
| Birds-eye view of Salt Lake City | 1875 | LoC | https://www.loc.gov/item/75696614/ | LoC free to use | JP2 9881 x 7312 | Image only |
| OpenHistoricalMap streets | 1847 on | OHM | see below | CC0 | Vector | Yes (38 era streets) |
| Sanborn, Salt Lake City | 1884, 1889 | LoC | https://www.loc.gov/item/sanborn08891_001/ | Public domain | Sheets | Too late and too detailed |

## Licenses, word for word

- **Library of Congress, Geography and Map Division** (identical on every item above, read from each item's JSON on 9 Oct 2026, no Rights Advisory on any): "The content of the Library of Congress Geography and Map Division digitized collections is free to use and reuse unless a Rights Advisory statement is present that indicates otherwise. Credit Line: Library of Congress, Geography and Map Division." Linked to https://www.loc.gov/legal/.
- **Joseph Smith Papers** (page footer on the City of Zion and Kirtland plat pages): "© 2026 by Intellectual Reserve, Inc. All rights reserved." No separate image credit or terms of use found on those pages.
- **Church History Library**, "Preparing to Publish" (https://churchhistorylibrary.churchofjesuschrist.org/accessing-our-records/preparing-to-publish?lang=eng): each catalog record has one of five rights statements. "In Copyright – Owned by Intellectual Reserve, Inc." and "In Copyright – Licensed to Intellectual Reserve, Inc." go to the Intellectual Property Office through the Permission to Use Church-owned Content site (approval can take 45 days). "No known copyright" means "there are no restrictions on using the source in a publication", but "you bear the ultimate responsibility of ensuring that the material is not subject to copyright." The page defines publishing as "any physical or digital distribution of materials", including posting online. Selling a shirt would count.
- **USGS** (https://www.usgs.gov/information-policies-and-instructions/copyrights-and-credits): "USGS-authored or produced data and information are considered to be in the U.S. Public Domain." and "When using information from USGS information products, publications, or websites, we ask that proper credit be given." Nothing specific to historical topo maps.
- **OpenHistoricalMap**: CC0 unless a feature has its own `license=*` tag (from the brief; https://www.openhistoricalmap.org/copyright).
- **David Rumsey**: CC BY-NC-SA 3.0, non-commercial (from the brief).

## Earliest USGS topo per place (TNM API, Historical Topographic Maps)

All too late to be period maps; listed so nobody looks again. Salt Lake 1885 (1:250,000), Whitingham 1889, Richmond 1889 (1:125,000), Independence and Liberty 1894 (1:125,000), Winter Quarters 1893 (Omaha), Sharon 1896, Palmyra and Sacred Grove 1899, Mendon 1901, Manchester and Fayette 1902, Colesville, Afton, Kirtland and Hiram 1905, Adam-ondi-Ahman 1922, Far West and Haun's Mill 1924, Quincy 1925, Harmony 1932, Carthage 1933, Nauvoo 1936, Mount Pisgah 1951, Martin's Cove 1951, Garden Grove and Council Bluffs 1954 (1:250,000).

## OpenHistoricalMap findings

The raw Overpass endpoint (the brief's open question) is `https://overpass-api.openhistoricalmap.org/api/interpreter`, from the OSM wiki page "OpenHistoricalMap/Overpass". The wiki states no rate limits; I sent one small query per place, 2 seconds apart.

Query per place, using each map's own frame (centre and width from `places.json`, 3:4 portrait): `way["highway"](bbox); way["railway"](bbox); out tags;`. "In era" means `start_date` before the end of the era year and no `end_date` before the era start.

| Place | Highways in frame | In era | What the era ways are |
|---|---|---|---|
| Salt Lake City | 472 | 38 | The original grid: 100 South, 100 East/State Road, 200 East and so on |
| Hiram | 18 | 7 | Cleveland-Warren State Road, Windham Street |
| Winter Quarters | 135 | 5 | Mormon Trail |
| Council Bluffs | 489 | 3 | Mormon Trail |
| Colesville | 117 | 2 | Great Bend & Bath and Susquehanna & Bath turnpikes |
| Fayette | 56 | 2 | Seneca Turnpike, North Branch |
| Martin's Cove | 5 | 2 | Mormon Trail and one unnamed way |
| Afton | 43 | 1 | Susquehanna & Bath Turnpike |
| Mendon | 33 | 1 | Ontario & Genesee Turnpike |
| Nauvoo, Garden Grove, Mount Pisgah | 1 each | 1 | Mormon Trail only |
| Manchester | 17 | 0 | earliest 1954 |
| Kirtland | 7 | 0 | earliest 1926 |
| Independence | 151 | 0 | earliest 1886 |
| Liberty | 2 | 0 | |
| Sharon, Whitingham, Palmyra (both), Sacred Grove, Harmony, Richmond, Far West, Adam-ondi-Ahman, Haun's Mill, Quincy, Carthage | 0 | 0 | |

Verdict: OHM is only useful for Salt Lake City (38 streets, enough to cross-check a tracing of the Sherwood plat, not enough alone) and for the Mormon Trail line. Raw results are not saved in the repo.

## Failed requests and limits (reported, not worked around)

- **NYPL Digital Collections** (digitalcollections.nypl.org): returns an Incapsula bot-check page to scripted requests, so the 1842 Hills Nauvoo map's image, size and exact rights text were not read. Evan can open it in a browser from the DPLA link.
- **DPLA** (dp.la item and the Winter Quarters source page) and **civilwaronthewesternborder.org** (1877 Jackson County plat book page): HTTP 403 to WebFetch.
- **Allmaps annotation lookup** (annotations.allmaps.org with the LoC IIIF manifest URL): HTTP 403 for all six maps tried, so whether any is already georeferenced is unknown.
- **Church History Library catalog**: a JavaScript app; record rights fields were not read. Rights for the CHL plats are taken from the Joseph Smith Papers footer.
- **David Rumsey**: I ran 8 searches against `davidrumsey.com/luna/servlet/as/search` before reading its robots.txt, which disallows that path. I stopped there. Nothing was downloaded. What came back: an Andreas 1870s Illinois atlas page with Nauvoo, a "Plan of Council Bluffs" (likely the same Andreas 1875 Iowa atlas LoC holds), and Mormon Trail route maps. Rumsey is non-commercial in any case, and LoC holds public-domain copies of the useful items.
- **LoC**: one item JSON (Monroe County 1852) came back truncated and one (Windsor County 1856 variant) returned an error page; not retried.

## Samples saved

`historical/samples/` (all LoC, all listed in `manifest.json` with source URL, license text and license URL):

- `slc-1847-sherwood-plat_loc_pct25.jpg`, 1082 x 1626, 210 KB, plus `slc-1847-sherwood-plat_loc_info.json`
- `nauvoo-1859-hancock-county-inset_loc_crop.jpg`, 2300 x 1700, 533 KB
- `palmyra-1853-wayne-county-inset_loc_crop.jpg`, 2250 x 1300, 346 KB
- `kirtland-1857-geauga-lake-township_loc_crop.jpg`, 2250 x 2200, 801 KB
- `hiram-1857-portage-county-inset_loc_crop.jpg`, 1450 x 1500, 214 KB

Crops come straight from the LoC IIIF server (`.../{x},{y},{w},{h}/full/0/default.jpg`), so any other inset can be pulled the same way without downloading a whole map.

## Side-by-side test (9 October, second session)

`build_historical.py` draws two period plans in the map-back style, in the same 13.5 x 18 in frame, next to today's back. Run `python3 designs/city-map-back/build_historical.py` (about 25 seconds). Output in `out/historical/` (gitignored): `slc-1847-vs-today.png`, `nauvoo-1859-vs-today.png`, overlay checks and 100 ppi previews. The traced street lines are kept in `historical/traces/*.geojson` and listed in the samples manifest under "derived". No new files were downloaded.

- **Salt Lake City 1847.** The plat is a perfect grid, so it is not traced pixel by pixel: the script counts the blocks on the scan (9 x 15, square pitch to 1.7 percent) and lays that grid on the ground at the spacing measured from today's TIGER streets (241.5 m east-west, 243.5 m north-south; the 1847 survey's 660 ft block plus 132 ft street is 241.4 m), anchored at Main and South Temple. The overlay shows the 1847 grid sitting exactly on today's downtown streets, except the top two rows, which run onto Capitol Hill where today's streets bend with the slope. The plat draws its streets narrower than they are (0.13 of a block on the sheepskin, 0.20 on the ground). In the same box, the plat has 71 km of street and today has 147 km: the later mid-block streets are what the plat lacks.
- **Nauvoo 1859.** Traced from the inset: blocks are found as closed outlines, lettering and river hatching are filtered out, and the streets are the centre lines of the gaps. Fitted to the ground through 8 intersections whose 1859 names are still on TIGER (Main, Partridge and Wells with Young, Mulholland, White and Munson): 3 m mean error, 6 m worst. The Temple Ruins block lands on today's temple. In the same box the trace has about 39 km of street and today about 35 km: Nauvoo had a fuller grid on the flats in 1859 than survives today. The trace is automatic and unfinished: about 112 of the inset's blocks were found, a handful of street segments are missing where a block was missed, the rotated north-west addition is patchy, and the inset stops short of the east bluff, so the right side of the 4 km frame is empty. A product version would need about an hour of hand cleanup.
- **Labels** on the test read "SALT LAKE CITY, UTAH 1847" and "NAUVOO, ILLINOIS 1859" as placeholders; which year to show is question 4 below.

## Questions for Evan

1. **Sparse is the look you would get.** A traced 1847 Salt Lake or 1859 Nauvoo is a clean plat of blocks, not the dense street web you chose for the current line. Is that a separate "Historical" version of the map back, a replacement, or not wanted?
2. **Plans that were never built.** The City of Zion (1833) and Kirtland (1833) plats are the most iconic period plans, but they show what was planned, not a place as it was. Are planned-city designs in scope?
3. **Church-held plats.** The City of Zion, Kirtland and Far West material is © Intellectual Reserve. Do you want to (a) request permission through the Church's permissions site (about 45 days), (b) draw our own version of the City of Zion from its written dimensions, which avoids copying the scan but is worth a quick IP check, or (c) stay with LoC sources only?
4. **The era gap.** Is an 1850s map acceptable for a place the Saints left in the 1830s, if the label says the map's own year (for example "PALMYRA, NEW YORK 1853")? Or should the year shown be the Saints' year, which would only be honest for Nauvoo and Salt Lake City?
5. **Nauvoo 1842.** The Hills map is the true period map and NYPL calls it public domain. Can you open the DPLA link in a browser and confirm the NYPL page and its rights line, or should we just use the 1859 LoC inset?
6. **Missouri, Iowa, Winter Quarters, Martin's Cove.** Nothing usable was found. Keep those on today's TIGER maps?
