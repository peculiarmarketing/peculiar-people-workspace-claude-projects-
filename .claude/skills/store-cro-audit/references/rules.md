# Checkable rules

## Where these came from, and what that means

Derived from `research/CRO-FINDINGS.md` in this project, which synthesises **twelve YouTube
videos** watched in September 2026. Ten of the twelve are made by people selling a service:
an agency, an app, a template, a course, or a page builder.

**This is not research.** One source (Baymard Institute, presented at a 2014 VWO webinar)
shows usability studies with stated sample sizes. Everything else is a practitioner's
opinion, delivered on a marketing channel.

**No statistic survived.** The synthesis discarded any number not repeated by a second
independent source. Not one number qualified across twelve videos. Never quote a conversion
percentage in an audit report. If a finding needs a number to be persuasive, it is not
strong enough to ship.

Basis labels on every rule below:

- **CONFIRMED**: two or more independent sources agreed. Still opinion, just repeated opinion.
- **SINGLE**: one source. **Unverified.** Say so in the report whenever one of these drives
  a finding. Name the source in brackets.
- **RESOLVED CONFLICT**: sources disagreed and CRO-FINDINGS section 8 picked a side with
  stated reasoning.

Two sources (A3 and B4) are the same person, Kurt Elster. Rules marked "(Kurt)" rest on one
voice even though he appears in two videos.

## Brand constraints that override any rule here

Read `BRAND.md` before writing findings. These are settled and not up for re-derivation:

- **No em dashes anywhere.** Absolute.
- No fabricated urgency, scarcity, countdowns, or "N sold" counters. Ruled out on brand
  grounds, and at zero orders they would also be false statements.
- No jokes, memes, or politics.
- Premium pricing is held deliberately. Never recommend a discount as the fix for a trust
  problem.
- The store is print-on-demand: no volume cost break, no shipping-speed control. Free
  shipping thresholds, gift thresholds and bundle discounts all come straight out of margin.
- Zero orders ever. Any rule needing reviews, ratings, customer photos or press coverage is
  **N/A - blocked**, not FAIL. Scoring blocked rules as failures produces a report that
  reads as damning and is not actionable.

---

## Home page

| # | Rule | Basis |
|---|---|---|
| H1 | The hero image shows the product worn or in use, not floating on a blank background | CONFIRMED |
| H2 | Exactly one primary call to action is visible above the fold | CONFIRMED |
| H3 | The hero is a single image, not a rotating carousel | SINGLE (Kurt) |
| H4 | The announcement bar is one line carrying one message | CONFIRMED |
| H5 | The homepage communicates what the brand is, not only what it sells | CONFIRMED |
| H6 | Shipping and returns terms appear as readable text, not only as badges | CONFIRMED |
| H7 | The main menu has roughly five top-level items | SINGLE (Kurt) |
| H8 | The main menu contains no "Home" entry | SINGLE (Kurt) |
| H9 | Every main-menu item leads toward buying something | SINGLE (Kurt) |
| H10 | The footer contains company pages and policy pages | CONFIRMED |
| H11 | Every image on the homepage links somewhere | SINGLE (Kurt) |
| H12 | No section heading is left at the theme's default wording | SINGLE (C1) |
| H13 | The country or region selector lists only regions actually shipped to | SINGLE (B2) |
| H14 | Nothing above the fold auto-scrolls, rotates or animates | SINGLE (B2) |

## Collection page

| # | Rule | Basis |
|---|---|---|
| L1 | Every product image in the grid uses the same angle, crop, background and lighting | CONFIRMED |
| L2 | Product edges are clearly visible against the background | CONFIRMED |
| L3 | Filters exist and match how this catalogue would be browsed | CONFIRMED |
| L4 | Product cards show a hover state on desktop | CONFIRMED |
| L5 | The default card image is the clearest available image of the product | SINGLE (C1) |
| L6 | Product cards show colour options | SINGLE (A1) |
| L7 | The filter or header states how many products are in view | SINGLE (A1) |

## Product detail page

| # | Rule | Basis |
|---|---|---|
| P1 | Image, price, colour, size, size guide and add-to-cart are all visible without scrolling | CONFIRMED |
| P2 | A size guide is reachable from above the fold | CONFIRMED |
| P3 | Sizes are selectable buttons, not a dropdown | CONFIRMED |
| P4 | Colour options are shown as images of the product in that colour, not plain colour dots | CONFIRMED |
| P5 | The page states what size garment is shown in the image | CONFIRMED |
| P6 | Add to cart is the most visually dominant button on the page | SINGLE (B2) |
| P7 | Add to cart is not visually subordinate to an express-wallet button | SINGLE (B2) |
| P8 | A sticky add-to-cart appears once the main one scrolls out of view | CONFIRMED |
| P9 | The gallery makes it obvious that more images exist | CONFIRMED (form contested) |
| P10 | Shipping and returns terms appear near the add-to-cart button | CONFIRMED |
| P11 | Below the fold, named sections answer fabric, care, fit and origin questions | CONFIRMED |
| P12 | Description copy leads with benefit and uses bullets or short blocks | CONFIRMED |
| P13 | The persuasive copy is visible; only reference tables are collapsed | RESOLVED CONFLICT |
| P14 | Emotional content appears before technical detail | SINGLE (C2) |
| P15 | The page would work as a paid-traffic landing page | CONFIRMED |
| P16 | Reassurance text sits next to the control that triggers the doubt | SINGLE (A2) |
| P17 | No fabricated scarcity, countdown or "N sold" counter is present | RESOLVED CONFLICT |
| P18 | No badge asserts something unearned (best seller, top rated) | RESOLVED CONFLICT |

## Cart

| # | Rule | Basis |
|---|---|---|
| C1 | The cart opens as a drawer without a full page load | CONFIRMED |
| C2 | The checkout button is reachable without scrolling on mobile | CONFIRMED |
| C3 | The discount code field is not visually dominant, and ideally is behind a link | CONFIRMED |
| C4 | Cart cross-sell buttons have real contrast against their background | SINGLE (B1) |

## Checkout entry

| # | Rule | Basis |
|---|---|---|
| K1 | The checkout shows the brand's logo and colours | CONFIRMED |
| K2 | Guest checkout is available and visibly offered | CONFIRMED |
| K3 | Express wallet buttons are present | CONFIRMED |
| K4 | No field is required without an explanation of why | SINGLE (A4, research-grade) |
| K5 | Field labels are outside the fields, not placeholder text | SINGLE (A4, research-grade) |
| K6 | No information is requested twice | CONFIRMED |
| K7 | Payment fields sit in a visually enclosed block | SINGLE (A4, research-grade) |
| K8 | No open discount code box invites coupon hunting | CONFIRMED |

## Trust and credibility

| # | Rule | Basis |
|---|---|---|
| T1 | The typeface is not the theme's default | CONFIRMED |
| T2 | A real logo is present, not a wordmark in the theme's default type | CONFIRMED |
| T3 | Colours form a deliberate palette; no colour appears once and nowhere else | CONFIRMED |
| T4 | Third-party app widgets are styled to match the site | SINGLE (C3) |
| T5 | A named human appears somewhere as the person behind the brand | SINGLE (Kurt) |
| T6 | Contact details exist and are findable | SINGLE (Kurt) |
| T7 | Policy pages exist and are linked | CONFIRMED |
| T8 | Body text is at least 16px | SINGLE (Kurt) |
| T9 | Body text has strong contrast against its background | SINGLE (Kurt) |
| T10 | The product photography looks like it was made by this brand, not bought | CONFIRMED |
| T11 | Nothing on the page asserts a fact that is not true | RESOLVED CONFLICT |

## Mobile

| # | Rule | Basis |
|---|---|---|
| M1 | Every rule above passes on a mobile viewport as well as desktop | CONFIRMED |
| M2 | Primary buttons are full width on mobile | SINGLE (B1) |
| M3 | Floating widgets do not overlap each other or the cart | SINGLE (B2) |
| M4 | A cookie banner and an email popup do not appear simultaneously | SINGLE (B2) |
| M5 | A sticky action bar sits at the bottom of the screen | SINGLE (B3, hedged by its own source) |
| M6 | Text is readable without zooming | SINGLE (Kurt) |

---

## Rules that are usually blocked for this store

Mark **N/A - blocked** and say what would unblock them, rather than FAIL:

- Anything requiring reviews, ratings, review counts, or customer photographs.
- "As seen in" press logos.
- Best-seller or top-rated badges.
- Fit scales and per-review size data.

The one part of the fit finding that is **not** blocked is P5: stating what size is shown in
the image needs no customers at all. Three independent sources support it. If it fails,
report it as a live opportunity, not as blocked.
