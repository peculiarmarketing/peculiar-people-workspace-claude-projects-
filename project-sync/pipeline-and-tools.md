# Peculiar People: Pipeline, Tools and Current State

Mirror of the Claude Code workspace, as of 23 September 2026. The source of truth lives on Evan's Mac in `1. Peculiar People/Claude Projects/`. BRAND.md (also in this project) covers the brand itself; this doc covers how the work gets built and where it stands.

## Where the work happens

- **Claude Code**, run from `1. Peculiar People/Claude Projects/`, does all building: art, print files, products, descriptions, Shopify and Tapstitch changes. It reads `CLAUDE.md`, `BRAND.md`, and each project's `README.md`, `docs/decisions.md` and `HANDOFF.md`.
- **This Claude project** is for strategy, marketing, copy and creative, and it keeps a copy of the brand and pipeline state so chat answers match what is live. If this doc and the workspace disagree, the workspace wins.

## Folder map (`1. Peculiar People/`)

- `Temples/`: art source of truth. 45 temple folders with black and white SVGs, references and facts fragments.
- `Temples READY/`: 99 temples with verified reference photos, waiting for art.
- `Temples TO DO/`: queue for the ref finder.
- `Important Elements/`: logos (black, white, square, Spanish), Evan's signature, size guide videos.
- `Other designs/`: Be Peculiar wordmarks (English and Spanish), Dot the earth, Angel Moroni (flag before use).
- `Website : Social assets/`: slider images, product photography, temple collage.
- `Posts/`: CapCut ad drafts, Kirtland recordings, story audio.
- `Claude Projects/`: all automation, skills and research.

## The pipeline, end to end

1. **References.** The `temple-ref-finder` skill moves temples from `Temples TO DO` to `Temples READY` with verified photos. Its value is the trap list: mislabeled Newsroom files, pre-renovation photos (Columbus, Mesa, Oklahoma City), the demolished Kona temple, superseded renders, fan-made 3D, same-state search bleed.
2. **Line art.** Generated mainly on kie.ai with GPT Image 2.5, using the esquisse prompt (`temple-sketch-prompt.md`) plus the reference photo. When trees, poles or shrubs block the temple, the reference photo is cleaned up with GPT Image 2.5 first. The prompt's rules: proportions come only from the photo, peaks close cleanly, junctions overrun, bold felt-tip line weight.
3. **Products.** The `temple-product-generator` skill traces the art, computes layout, builds flattened PNG print files, creates Tapstitch products from Python (`tapstitch_api.py`, since the Tapstitch editor is a JSON API underneath), publishes to Shopify, sets product type, tags and colour order, assembles and writes the description, pushes art close-up cards, and syncs the Easify Temple dropdown. The Printify path stays on disk as a fallback.
4. **Descriptions.** Three fixed blocks plus one variable: the founder intro for each garment (signed "- Evan"), the temple facts (the only researched part, stored per temple, shown as collapsed rows), and the size guide video. The Kiwi Size Chart app sits next to the size selector. Stored blocks are copied in byte-identical and never edited.
5. **Copy passes.** Any new customer-facing prose gets `humanizer` (word-level tells) and then `structural-humanizer` (shape-level tells, one or two interventions per piece).
6. **Audit.** The `store-cro-audit` skill screenshots the live storefront on desktop and mobile and scores it against 68 rules. It is read-only. The last full audit was 2 September 2026.

Skills in the workspace (`Claude Projects/.claude/skills/`): temple-ref-finder, temple-product-generator, humanizer, structural-humanizer, store-cro-audit.

Retired: the account-level cc1717, cc1566 and cc1567 temple description builders (written for Comfort Colors blanks that are gone), plus the old temple-prompt-assembler and temple-sketch-generator flow through Higgsfield.

## Tools and apps

- Store: Shopify (peculiarpeopleco.com). Store email evan@peculiarmarketing.com. Repos under the `peculiarmarketing` GitHub account.
- Fulfillment: Tapstitch, vendor `ODMPOD`, US-printed, 4 to 7 day delivery. Printify fulfils nothing and stays installed only until the first Tapstitch orders arrive fine. Printful is being uninstalled.
- Shopify apps: Kaching (bundles and upsells), Easify Product Options (Temple dropdown), Kiwi Size Chart, Digital Products (Temple Art File downloads), Track123 (order tracking, free tier).
- Email: a four-email Shopify Email post-purchase flow is drafted. Klaviyo will soon replace Shopify Email.
- Art: kie.ai with GPT Image 2.5 for line art and reference cleanup; Adobe Illustrator for SVG cleanup.
- Connectors in Claude: Shopify, Higgsfield, Google Drive, Figma.

## Current state (23 September 2026)

- 136 active products: 45 temples on the tee, sweatshirt and hoodie, plus the Temple Art File.
- Eden Green hoodie rollout finished: all 45 hoodies live in seven colours, verified. Each was a swap, and the old listings sit as drafts at `<address>-retired-<date>`.
- The personalized date tee is paused (40 drafts on the old Printify blank). Tapstitch has no buyer personalization.
- Zero orders. Distribution is the only constraint.

Still open for Evan:

- Re-import `artifacts/easify/option-sets.csv` in Easify. Every swapped hoodie is missing its Temple dropdown until then.
- Attach download files for the five new Art File designs (Albuquerque, Billings, Burley, Lehi, Provo Rock Canyon). They show as sold out until then.
- The storefront overhaul doc still says Boise is unfinished; its "State as of" section needs the completed rollout.
- Test purchase to verify checkout (first priority in BRAND.md section 17).
- Beachhead temples not yet picked.

## Working rules

- No em dashes, anywhere.
- Plain, direct language. Explain the mechanism of a failure before fixing it.
- Direct execution over proposal-and-confirm loops. Complete outputs, not partial edits.
- Never guess company-specific facts. Flag uncertainty.
- Temple facts clear the source hierarchy in BRAND.md section 12 or they do not ship.
- Anything touching the live store gets Evan's explicit confirmation.
- Never touch Lease End files or projects from Peculiar People work.
