#!/usr/bin/env python3
"""Add the Church history sites (city-maps/church-history-sites.md) to places.json.

    python designs/city-map-back/add_sites.py

Frames come from each place's saved extent in city-maps/data/index.json: a town
is framed to its own boundary (3:4, a little margin), so the map takes in the
whole town and not the next one; a site with no town is framed on its 6 km
square. Counties are every county whose outline box touches the frame, so roads
run to the frame edge instead of stopping at a county line. A temple is marked
when one of TEMPLES falls inside the frame. Line weight is 1.5 mm, or 0.5 mm for the
cities listed in BUSY.

Entries already in places.json are left alone, so hand-tuned frames (Nauvoo,
Kirtland, Salt Lake City) are kept.
"""

import json
import math
import struct
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
INDEX = ROOT / "city-maps" / "data" / "index.json"
COUNTY_SHP = ROOT / "city-maps" / "data" / "tiger" / "ref" / "cb_2023_us_county_20m.shp"
PLACES = HERE / "places.json"

# LDS temples near the sites, from OpenStreetMap (Nominatim, 8 Oct 2026).
TEMPLES = {
    "Nauvoo Illinois": (40.5504848, -91.3843815),
    "Kirtland": (41.6252883, -81.3621488),
    "Palmyra New York": (43.0389988, -77.2370607),
    "Kansas City Missouri": (39.2202404, -94.5013296),
    "Winter Quarters Nebraska": (41.3340799, -95.9661780),
    "Salt Lake": (40.7704367, -111.8919131),
}

# index.json key -> (places.json key, label). Garden Grove uses its 6 km square,
# as church-history-sites.md says; Preston is abroad and TIGER covers the US only.
SITES = {
    "sharon-windsor-county-vermont": ("sharon", "SHARON, VERMONT"),
    "whitingham-vermont": ("whitingham", "WHITINGHAM, VERMONT"),
    "palmyra-new-york": ("palmyra-village", "PALMYRA, NEW YORK"),
    "town-of-palmyra-new-york": ("palmyra-township", "PALMYRA, NEW YORK"),
    "town-of-manchester-ontario-county-new-york": ("manchester", "MANCHESTER, NEW YORK"),
    "sacred-grove-manchester-3km": ("sacred-grove", "SACRED GROVE, NEW YORK"),
    "town-of-fayette-new-york": ("fayette", "FAYETTE, NEW YORK"),
    "town-of-mendon-new-york": ("mendon", "MENDON, NEW YORK"),
    "town-of-colesville-new-york": ("colesville", "COLESVILLE, NEW YORK"),
    "town-of-afton-new-york": ("afton", "AFTON, NEW YORK"),
    "oakland-township-susquehanna-county-pennsylvania": ("harmony", "HARMONY, PENNSYLVANIA"),
    "kirtland-ohio": ("kirtland", "KIRTLAND, OHIO"),
    "hiram-township-portage-county-ohio": ("hiram", "HIRAM, OHIO"),
    "independence-missouri": ("independence", "INDEPENDENCE, MISSOURI"),
    "liberty-missouri": ("liberty", "LIBERTY, MISSOURI"),
    "richmond-missouri": ("richmond", "RICHMOND, MISSOURI"),
    "far-west-missouri-3km": ("far-west", "FAR WEST, MISSOURI"),
    "adam-ondi-ahman-3km": ("adam-ondi-ahman", "ADAM-ONDI-AHMAN, MISSOURI"),
    "hawn-s-mill-3km": ("hauns-mill", "HAUN'S MILL, MISSOURI"),
    "quincy-illinois": ("quincy", "QUINCY, ILLINOIS"),
    "nauvoo-illinois": ("nauvoo", "NAUVOO, ILLINOIS"),
    "carthage-illinois": ("carthage", "CARTHAGE, ILLINOIS"),
    "garden-grove-iowa-3km": ("garden-grove", "GARDEN GROVE, IOWA"),
    "mount-pisgah-park-union-county-iowa-3km": ("mount-pisgah", "MOUNT PISGAH, IOWA"),
    "council-bluffs-iowa": ("council-bluffs", "COUNCIL BLUFFS, IOWA"),
    "mormon-trail-center-at-winter-quarters-3km": ("winter-quarters", "WINTER QUARTERS, NEBRASKA"),
    "martin-s-cove-natrona-county-wyoming-3km": ("martins-cove", "MARTIN'S COVE, WYOMING"),
    "salt-lake-city-utah": ("salt-lake-city", "SALT LAKE CITY, UTAH"),
}
# River towns on a state line: leave the far bank out so the map ends at the
# river instead of pulling in the next city (Omaha, West Quincy).
ACROSS_RIVER = {"council-bluffs": "31", "quincy": "29", "carthage": "19"}
# Cities busy enough that 1.5 mm streets clump; they print at 0.5 mm.
BUSY = {"independence", "council-bluffs", "liberty", "quincy"}
MARGIN = 0.05
MIN_KM = 3.0


def county_boxes():
    """(fips, (minlon, minlat, maxlon, maxlat)) for every US county."""
    b = COUNTY_SHP.with_suffix(".dbf").read_bytes()
    n, hlen, rlen = struct.unpack("<IHH", b[4:12])
    off, pos, cols = 32, 1, {}
    while b[off] != 0x0D:
        name, size = b[off:off + 11].split(b"\0")[0].decode(), b[off + 16]
        cols[name] = (pos, size)
        pos += size
        off += 32
    def field(i, name):
        p, s = cols[name]
        return b[hlen + i * rlen + p:hlen + i * rlen + p + s].decode().strip()
    fips = [field(i, "STATEFP") + field(i, "COUNTYFP") for i in range(n)]
    s, off, boxes = COUNTY_SHP.read_bytes(), 100, []
    while off < len(s):
        clen = struct.unpack(">i", s[off + 4:off + 8])[0] * 2
        boxes.append(struct.unpack("<4d", s[off + 12:off + 44]))
        off += 8 + clen
    return list(zip(fips, boxes))


def frame(bbox, radius):
    """Centre and width (km) of a 3:4 portrait frame around the saved extent."""
    s, w, n, e = bbox
    lat, lon = (s + n) / 2, (w + e) / 2
    kx = 111.32 * math.cos(math.radians(lat))
    wkm, hkm = (e - w) * kx, (n - s) * 111.32
    if radius:  # a 6 km square around a site: keep its width, the frame runs taller
        return (lat, lon), round(wkm, 1)
    return (lat, lon), round(max(MIN_KM, max(wkm, hkm * 0.75) * (1 + 2 * MARGIN)), 1)


def frame_box(centre, width_km):
    lat, lon = centre
    dlon = width_km / 2 / (111.32 * math.cos(math.radians(lat)))
    dlat = width_km * 4 / 3 / 2 / 111.32
    return lon - dlon, lat - dlat, lon + dlon, lat + dlat


def main():
    index = json.loads(INDEX.read_text())
    places = json.loads(PLACES.read_text())
    counties = county_boxes()
    for key, (name, label) in SITES.items():
        if name in places:
            print(f"{name}: kept as is")
            continue
        centre, width = frame(index[key]["bbox"], index[key].get("radius_km"))
        x0, y0, x1, y1 = frame_box(centre, width)
        codes = [f for f, (a, b, c, d) in counties if a < x1 and c > x0 and b < y1 and d > y0]
        temple = next(([lat, lon] for lat, lon in TEMPLES.values()
                       if y0 < lat < y1 and x0 < lon < x1), None)
        if name in ACROSS_RIVER:  # the far bank is another state and another city
            codes = [c for c in codes if not c.startswith(ACROSS_RIVER[name])]
        places[name] = {"label": label, "counties": codes,
                        "centre": [round(centre[0], 5), round(centre[1], 5)],
                        "width_km": width, "line_mm": 0.5 if name in BUSY else 1.5,
                        "temple": temple}
        if name in BUSY:
            places[name]["busy"] = True
        print(f"{name}: {width} km, counties {codes}, temple {'yes' if temple else 'no'}")
    PLACES.write_text(json.dumps(places, indent=2) + "\n")


if __name__ == "__main__":
    main()
