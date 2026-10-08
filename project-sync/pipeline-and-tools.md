# Peculiar People: Pipeline, Tools and Current State

Mirror of the Claude Code workspace, as of 8 October 2026. The source of truth lives on Evan's Mac in `1. Peculiar People/Claude Projects/`. BRAND.md (also in this project) covers the brand itself; this doc covers how the work gets built and where it stands.

## Where the work happens

- **Claude Code**, run from `1. Peculiar People/Claude Projects/`, does all building: art, print files, products, descriptions, Shopify and Tapstitch changes. It reads `CLAUDE.md`, `project-sync/BRAND.md`, and each project's `README.md`, `docs/decisions.md` and `HANDOFF.md`.
- **This Claude project** is for strategy, marketing, copy and creative, and it keeps a copy of the brand and pipeline state so chat answers match what is live. If this doc and the workspace disagree, the workspace wins.

## Folder map (`1. Peculiar People/`)

- `Temples/`: art source of truth. 45 temple folders with black and white SVGs, references and facts fragments.
- `Temples READY/`: 99 temples with verified reference photos, waiting for art.
- `Temples TO DO/`: queue for the ref finder.
- `Important Elements/`: logos (black, white, square, Spanish), Evan's signature, size guide videos.
- `Other designs/`: Be Peculiar wordmarks (English and Spanish), Dot the earth, Angel Moroni (flag before use), Peculiar People Seal (jacket back seal, white and black ink; source and build script in `Claude Projects/designs/jacket-seal/`).
- `Website : Social assets/`: slider images, product photography, temple collage.
- `Posts/`: CapCut ad drafts, Kirtland recordings, story audio.
- `Claude Projects/`: all automation, skills and research. `city-maps/` holds the street map tool and every saved town.

## The pipeline, end to end

1. **References.** The `temple-ref-finder` skill moves temples from `Temples TO DO` to `Temples READY` with verified photos. Its value is the trap list: mislabeled Newsroom files, pre-renovation photos (Columbus, Mesa, Oklahoma City), the demolished Kona temple, superseded renders, fan-made 3D, same-state search bleed.
2. **Line art.** Generated mainly on kie.ai with GPT Image 2.5, using the esquisse prompt (`prompts/temple-sketch-prompt.md`) plus the reference photo. When trees, poles or shrubs block the temple, the reference photo is cleaned up with GPT Image 2.5 first. The prompt's rules: proportions come only from the photo, peaks close cleanly, junctions overrun, bold felt-tip line weight.
3. **Products.** Saying "run a sweep" does a new temple end to end. Evan drops a folder in `Temples/` holding only the design PNG. The `temple-product-generator` skill researches the location and the temple facts (both humanizer passes), then `scripts/sweep.py` builds, publishes, tags, builds the on-model gallery, uploads the homepage drawing and city line to the live theme, copies the download file, adds the temple to the Temple Art File as a sold-out option, syncs the Easify CSV, and verifies everything on the live site. The proof gate is automatic. The only stop is a location the sources leave unclear. Two steps stay manual because no API reaches them: the Easify CSV import, and attaching the Art File download. In more detail, the skill traces the art, computes layout, builds flattened PNG print files, creates Tapstitch products from Python (`tapstitch_api.py`, since the Tapstitch editor is a JSON API underneath), publishes to Shopify, sets product type, tags and colour order, assembles and writes the description, pushes art close-up cards, and syncs the Easify Temple dropdown. Tapstitch is the only fulfillment channel. Back prints sit one quarter of the spare height above the design and three quarters below, so short wide temples no longer sit mid-back. The on-model photos fold the print into the shirt's creases, and each product's first photo (the collection thumbnail) is the on-model shot in the flat-lay colour: maroon tee, black sweatshirt, navy hoodie. A design change can be pushed to live products in place with `scripts/relift_rollout.py`, with no new listings.
4. **Descriptions.** Three fixed blocks plus one variable: the founder intro for each garment (signed "- Evan"), the temple facts (the only researched part, stored per temple, shown as collapsed rows), and the size guide video. The Kiwi Size Chart app sits next to the size selector. Stored blocks are copied in byte-identical and never edited.
5. **Copy passes.** Any new customer-facing prose gets `humanizer` (word-level tells) and then `structural-humanizer` (shape-level tells, one or two interventions per piece).
6. **Audit.** The `store-cro-audit` skill screenshots the live storefront on desktop and mobile and scores it against 68 rules. It is read-only. No audit has been run since the Tapstitch migration. The `design-audit` skill does the same for a single graphic (logo, seal, garment print): scripts measure centring, ring concentricity, stroke weights, spacing and print-size minimums from the image, and it scores 61 researched rules and returns ranked fixes with target numbers. It proposes only and never overrides a BRAND.md decision. Its print minimums are vendor guidance (screen, DTF, DTG); Tapstitch publishes no artwork spec.
7. **Idea inbox.** Evan texts himself reel links, screenshots and notes in iMessage through the day. A Mac mini collects them at 1:15 AM (`idea-inbox/collector/nightly.py`), turns videos into transcripts and still frames, and pushes them to `idea-inbox/inbox/`. Around 2 AM a Claude Code routine runs the `idea-triage` skill, which gives each item a verdict (useful, beneficial, plausible, waste) and a first deliverable: a plan, a copy draft, a mockup, or a one-line reason. The digest lands in `ideas/YYYY-MM-DD/DIGEST.md`. `ideas/STATUS.md` tracks what happened to each idea (new, approved, done, tested, dropped); any session that acts on one updates its row, and the triage reads it so it never re-plans finished work. It plans and drafts only; it never changes the store, posts, or replies to anyone.
8. **Street maps.** `city-maps/fetch_map.py` takes town names and writes black and white SVG and PNG street maps (transparent, 6000 px) to `city-maps/out/`. Each town is downloaded once from OpenStreetMap and saved in `city-maps/data/`. `city-maps/city-roads/` is a local copy of anvaka's city-roads web app for exploring by eye, fixed so small towns load: the public site only caches big cities and its fallback asks Overpass for more than a busy server will give. Raw material only; the designs come later. 29 Church history sites are saved, from Sharon, Vermont to Salt Lake City plus Preston, England; the list is `city-maps/church-history-sites.md`. `designs/city-map-back/build_map_back.py` turns a place into back-print art for the city map design line (in exploration): US roads from the Census TIGER files (public domain, with road classes, so sidewalks and service drives drop out), a halo marking the temple, and a 13.5 x 18 in frame. Big cities use 0.5 mm lines with the frame as wide as it holds before streets merge (about 6 percent fused ink; `--auto` finds it); small towns use 1.5 mm, and every frame takes in as many streets as it can without pulling in a neighbouring city.

Skills in the workspace (`Claude Projects/.claude/skills/`): temple-ref-finder, temple-product-generator, humanizer, structural-humanizer, store-cro-audit, design-audit, idea-triage.

Retired: the account-level cc1717, cc1566 and cc1567 temple description builders (written for blanks that are gone), plus the old temple-prompt-assembler and temple-sketch-generator flow through Higgsfield.

## Tools and apps

- Store: Shopify (peculiarpeopleco.com). Store email evan@peculiarmarketing.com. Repos under the `peculiarmarketing` GitHub account.
- Fulfillment: Tapstitch, vendor `ODMPOD`, US-printed, 4 to 7 day delivery. The only fulfillment channel. Printful is being uninstalled.
- Shopify apps: Kaching (bundles and upsells), Easify Product Options (Temple dropdown), Kiwi Size Chart, Digital Products (Temple Art File downloads), Track123 (order tracking, free tier).
- Email: a four-email Shopify Email post-purchase flow is drafted. Klaviyo will soon replace Shopify Email.
- Art: kie.ai with GPT Image 2.5 for line art and reference cleanup; Adobe Illustrator for SVG cleanup.
- Maps: OpenStreetMap data through Nominatim (search) and Overpass (download). Free; ODbL licence, credit needed on anything sold. US Census TIGER/Line road files for the city map designs: public domain, no credit needed.
- Connectors in Claude: Shopify, Higgsfield, Google Drive, Figma.

## Current state (8 October 2026)

- 139 active products: 45 temples on the tee, sweatshirt and hoodie, the Temple Art File, and the Nauvoo city map test on all three garments.
- One-quarter lift finished 7 October: all 135 garment products re-saved in place with the higher print, folded model photos and on-model thumbnails, and verified. Orders print the new design; no listing was swapped, so the Easify dropdowns are untouched.
- Eden Green hoodie rollout finished: all 45 hoodies live in seven colours, verified. Each was a swap, and the old listings sit as drafts at `<address>-retired-<date>`.
- The personalized date tee is paused (40 drafts on a retired blank). Tapstitch has no buyer personalization, so bringing it back means building it from scratch.
- Zero orders. Distribution is the only constraint.
- The sweep (`scripts/sweep.py`) was built 7 October and has not yet run on a real new temple. The first run should be watched: its tag, Art File and theme-upload writes have not touched the store yet.
- Tapstitch now works from cloud sessions (8 October): the scripts read the login cookies from a `TAPSTITCH_COOKIES` environment secret when there is no Chrome profile. `scripts/tapstitch_designs.py` lists the Designs tab, including designs never published. The secret is a full login and expires after a few days.
- Street map tool built 7 October (`city-maps/`). Small towns that fail on the public city-roads site now download in seconds.
- City map back print in design exploration (8 October). Mockups on the claude.ai canvas "City Map Back Prints". Decided: full-bleed 13.5 x 18 in frame, halo temple marker, 0.5 mm lines for big cities at the widest frame that holds (San Antonio about 35 km, Salt Lake about 22 km), 1.5 mm for small towns. City label inside the frame, bottom right. Front: the box logo, 6 in and centred, with the temple's coordinates set into breaks in the box edge (latitude top left, longitude bottom right); the build script writes both prints per place. Cities only for now; mission-boundary designs are set aside. Built for every US Church history site in `city-maps/church-history-sites.md` (Preston, England waits on OpenStreetMap, which was unreachable). Busy cities print at 0.5 mm, everything else at 1.5 mm, all in a hand-drawn style (width swings 40 percent in small towns, 10 percent in busy cities; dead ends taper to a point); a site with no temple in frame gets the plain box-logo front. Product page: no temple section, the same product details, a fact-checked Church history section only for Church history sites (held to the temple facts standard), and a band that draws the map from the temple out like the temple pen drawing (`designs/city-map-back/web_map_drawing.py` writes the drawings in the temple band's format). Nauvoo published live as the test on 8 October through `temple-product-generator/scripts/map_run.py`: titles "Essential Heavyweight Map Tee (Nauvoo)" and so on, shown on the page as the garment name with "Nauvoo, Illinois" underneath; tags `map:nauvoo` and `line:map` only, so maps stay out of the temple collections and the homepage marquee; a new smart collection, Church History Maps. The history section lives in `designs/city-map-back/history/`. Not yet done for maps: the on-model gallery (needs the blank garment photos on the Mac).
- Idea inbox is live on this Mac from 6 October, iMessage only: notes, screenshots and reel links texted to self get transcripts and frames nightly. Reel links are downloaded logged out, so no account is tied to it; an occasional reel may fail. The Instagram API route was tried and removed (Meta returned no conversations with every setting correct), and nothing in the pipeline logs in to any account.

Still open for Evan:

- Church History Maps collection: tick Online Store (and any other channels) in the admin. The app token cannot publish collections, so it was created unpublished and its page 404s until then. Add it to the menu if wanted.
- Nauvoo map products: run the on-model gallery from the Mac when convenient. Map products use their own page template (`product.map`): no Reference / Final drawing slider, and the design-suggestion copy asks for cities and Church history sites.

- Add the `TAPSTITCH_COOKIES` secret to the cloud environment (copy the Cookie header from DevTools on tapstitch.com while logged in). Refresh it when a cloud run says "Not logged in".
- Re-import `artifacts/easify/option-sets.csv` in Easify. Every swapped hoodie is missing its Temple dropdown until then.
- Attach download files for the five new Art File designs (Albuquerque, Billings, Burley, Lehi, Provo Rock Canyon). They show as sold out until then.
- Test purchase to verify checkout (first priority in BRAND.md section 17).
- Before any street map design ships: decide where the "© OpenStreetMap contributors" credit goes (product page is the usual place). The ODbL requires it. US designs built from Census TIGER data do not need it.
- Optional: the Meta developer app "Message Reader" (Peculiar Marketing LLC) is no longer used by anything. Delete it in the Meta dashboard, and remove it under Instagram Settings > Apps and websites on both accounts, if you want no app holding access.

## Working rules

- No em dashes, anywhere.
- Plain, direct language. Explain the mechanism of a failure before fixing it.
- Direct execution over proposal-and-confirm loops. Complete outputs, not partial edits.
- Never guess company-specific facts. Flag uncertainty.
- Temple facts clear the source hierarchy in BRAND.md section 12 or they do not ship.
- Anything touching the live store gets Evan's explicit confirmation.
- Never touch Lease End files or projects from Peculiar People work.
