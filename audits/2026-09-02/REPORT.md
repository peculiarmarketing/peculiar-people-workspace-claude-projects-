# Storefront audit: peculiarpeopleco.com

Run 2 September 2026 by the `store-cro-audit` skill. 53 screenshots in `shots/`, capture
log in `manifest.json`.

## What was checked

Desktop (1440x900) and mobile (iPhone 13 emulation, reloaded so load-time device logic
re-runs), both walked end to end:

home, nav opened, search for "temple", the All Products collection, desktop card hover,
three product pages, a colour change, a size change, the page scrolled to test for a sticky
add-to-cart, add to cart, the cart drawer, the cart page, the checkout entry screen, and the
footer.

Products were taken live from Shopify, not guessed: `essential-temple-tee-west-jordan`,
`essential-temple-tee-with-personalizable-date-west-jordan`, and
`pillar-temple-hoodie-boise`. Theme is Shrine Pro. Collection shows 164 products.

**No order was placed.** The journey stops at the checkout entry screen. Nothing was typed
into a payment field and nothing was submitted.

**Where the rules come from.** Twelve YouTube videos, synthesised in
`research/CRO-FINDINGS.md`. Ten of the twelve are made by people selling a service. Only one
source shows actual usability research. Lines marked SINGLE below rest on **one unverified
opinion** and are labelled as such. No conversion statistic appears anywhere in this report,
because none survived the two-source test in the research.

**Not assessed:** payment field styling inside checkout (K7), because reaching it means
entering a real address, which this audit does not do.

---

# Part 1: Makes the store look established

Ranked by impact against effort. The visitor decides whether this is a real business in
about two seconds, and never reaches Part 2 if the answer is no.

### E1. The product page shows a price you cannot actually pay
**Rule:** T11 (nothing asserts something untrue). **Evidence:** `desktop__10-pdp1-fold.png`,
`desktop__14-pdp1-scrolled-sticky.png`, `mobile__20-cart-drawer.png`

The product page headline reads **$35.55**. The DOM labels it "Regular price $35.55". But
the Single Tee option in the same screenshot is **$44.99**, the sticky bar lower down the
same page says **$44.99**, the cart says **$44.99**, and checkout charges **$44.99**.

$35.55 is the per-unit price of the "Buy 1, Get 1 25% OFF" bundle ($71.10 for two), which is
preselected. So the largest number on the page is a price no single-item buyer pays.

This is the highest-impact item in the audit. A shopper who notices the price change between
the product page and the cart has been given a concrete reason to distrust the store, at the
exact moment they were deciding. It also undercuts a deliberately premium price by
advertising a lower one.

**Fix:** make the headline price show the price of the currently selected configuration, or
default the bundle selector to Single Tee so the headline and the default purchase agree.
Effort: theme setting or a small template change. Impact: high.

### E2. The checkout claims an award the brand has not won
**Rule:** T11. **Evidence:** `desktop__30-checkout-entry.png`

The checkout footer reads: "Your order includes free returns and 24/7 access to our
award-winning customer service."

The store has never had an order. There is no award, there is no 24/7 support desk, and
"free returns" needs checking against the actual returns policy, because print-on-demand
returns usually are not free. This is boilerplate that shipped with a theme or app and was
never edited.

This sits on the single most trust-sensitive screen in the store. It is also the precise
pattern the research names as the dropshipper tell: unearned claims stated flatly.

**Fix:** delete the sentence, or replace it with something true. Draft, needs the humanizer
and structural-humanizer passes before it ships:

> DRAFT COPY - needs humanizer + structural-humanizer before it ships
> "Secure checkout. Questions before you order? Email evan@peculiarmarketing.com."

Effort: minutes. Impact: high.

### E3. The best writing on the site is set at 13.5px
**Rule:** T8, T9, M6 (SINGLE source, Kurt Elster). **Evidence:**
`desktop__14-pdp1-scrolled-sticky.png`, `mobile__14-pdp1-scrolled-sticky.png`

Measured directly in the browser:

- Product description body copy: **13.5px Arial**
- Homepage hero subcopy: **12.6px Arial**, white at 90% opacity on blue
- Headings: 31 to 39px Montserrat

The founder intro is the strongest asset on the product page. It is the thing that makes
this a brand rather than a print shop, and it is rendered two to three points below the
readable minimum, in a fallback system font, while the headings around it are a chosen
typeface at three times the size.

Note the mismatch: headings are Montserrat, body copy is Arial. The body font was never set,
so it falls back.

This is the "subtle is sophisticated" trap named in the research: the intent reads as
restrained to the person who built it, and as hard to read to a visitor on a phone.

**Fix:** body copy to 16px minimum, and set the body font deliberately rather than letting
it fall back to Arial. Effort: two theme settings. Impact: high, and it touches every page.

### E4. A countdown timer and an unearned badge
**Rules:** P17, P18, T11. **Evidence:** `mobile__20-cart-drawer.png`,
`desktop__20-cart-drawer.png`, `desktop__10-pdp1-fold.png`

Two things assert urgency or popularity that the store has not earned:

- The cart drawer shows a black bar reading **"Cart reserved for 04:56"**, counting down.
- The bundle box carries a **"MOST POPULAR"** ribbon on the Buy 1 Get 1 option.

With zero orders ever, "most popular" is not a true statement. The reservation countdown is
manufactured urgency of exactly the kind BRAND.md rules out, and the research names it as
one of the signals that makes a visitor decide a store is not legitimate.

**Fix:** turn off the cart reservation timer in whichever app supplies it. Remove the "most
popular" ribbon or replace it with a neutral label. Effort: app settings. Impact: high on
credibility, and it removes a live brand-guardrail breach.

### E5. A homepage collection card is blank and leads nowhere
**Rules:** H11, L1. **Evidence:** `desktop__02-home-full.png`

The Collections row on the homepage has three cards. The third, "Sweatshirts & Hoodies", has
**no image at all**: it is an empty white box with a text label. Shopify confirms that
collection contains **0 products**, as does the "Bottoms" collection.

So the homepage advertises a category, renders it as a blank card, and sends anyone who
clicks to an empty page. On a store whose problem is looking unfinished, this is the most
literal possible version of that.

**Fix:** either populate the collection and give the card an image, or remove the card.
Effort: low. Impact: high relative to effort.

### E6. Two of the three collection cards use the same photograph
**Rule:** L1. **Evidence:** `desktop__02-home-full.png`

"All Products" and "Shirts" both show the identical grey Salt Lake tee. The one visual
system finding in the research that is specifically about higher-priced items is that
consistency reads as trust, but identical is not consistent, it is unfinished.

**Fix:** give each card a distinct image. Effort: minutes. Impact: moderate.

### E7. Checkout drops the logo for plain text
**Rule:** K1 (CONFIRMED across two sources). **Evidence:** `desktop__30-checkout-entry.png`,
`mobile__30-checkout-entry.png`

Every page of the store shows the boxed PECULIAR|PEOPLE wordmark. The checkout shows
"Peculiar People" set in plain black system text, with no brand colour anywhere.

The research names this as the most common single mistake, and puts the fix at about sixty
seconds in checkout settings. Given BRAND.md records four checkouts reached and zero
completed, the checkout deserves attention it has evidently not had.

**Fix:** upload the logo and set the accent colour in Shopify checkout settings. Effort:
minutes. Impact: moderate to high, on the screen where trust matters most.

### E8. Default theme wording and a thin footer
**Rules:** H10, H12. **Evidence:** `desktop__40-footer.png`

The footer heading is **"Quick links"**, a Shopify default that the research names as a
visible tell that nobody edited the theme. The footer contains Search, Privacy Policy,
Become an Ambassador, Returns refunds and exchanges, and Shipping Info.

Missing: Our Story, Contact Us, Terms of Service. "Our Story" and "Contact Us" exist but
live only in the hamburger menu. The research finds that the presence of company and policy
pages in the footer is itself a trust signal, independent of anyone reading them.

**Fix:** rename the heading, and add Our Story, Contact Us and Terms. The recommended layout
from the research is logo left, then three columns: catalogue, customer care, about.
Effort: low. Impact: moderate.

### E9. No call to action above the fold on desktop
**Rules:** H2, H3, H14. **Evidence:** `desktop__01-home-fold.png`

On desktop the hero image fills the entire first screen. There is no headline, no text and
no button until the visitor scrolls. The headline and the "FIND YOUR TEMPLE" button sit
below the fold.

The hero is also a **carousel** with two slides, arrows, dots and autoplay, and the
announcement bar above it is a **scrolling marquee**. Two moving elements above the fold.

The research is consistent that a hero should be one still image doing one job, and that a
carousel usually exists to settle internal debates rather than to communicate. That last
point is a SINGLE source (Kurt Elster) and unverified.

**Fix:** overlay the headline and the button on the hero image so the first screen says what
this is and offers one way in. Stop the marquee and the carousel autoplay. Effort: moderate.
Impact: moderate.

### E10. Flagged for Evan, outside the rule set: the reference photograph
**Evidence:** `desktop__02-home-full.png`

The "Carefully made designs" section publishes a photograph of a temple labelled
**REFERENCE** beside the derived line drawing labelled **FINAL DRAWING**.

This is not a conversion finding, and I am raising it because it appears to conflict with two
standing rules in BRAND.md: publish only material Evan owns outright and never display a
third-party photograph, and do not publish a record of reference-sourcing practice. Section
15 also notes the real legal exposure sits in the source photograph rather than the building.

I cannot tell from a screenshot who took that photograph. If Evan took it, there is no
issue. If it came from a third party, this section is showing both the source and the
derivation, side by side, on the homepage. Worth a look before anything else changes.

---

# Part 2: Removes friction

Different problem, different fixes. These matter for a visitor who has already decided the
store is real.

### F1. There is no size guide anywhere on the product page
**Rule:** P2 (CONFIRMED, three sources). **Evidence:** `desktop__10-pdp1-fold.png`

I queried the live page for any link, button or summary matching "size guide", "size chart"
or "sizing". **Zero matches.** There is no size guide on the product page at all, above or
below the fold.

The information partly exists. Further down the page there is a fit block ("Fit: Relaxed,
true to size", plus a ladder from Tighter fit through Oversize fit), and the FAQ accordion
contains an entry beginning "It says unisex. How do I s...". But a shopper looking at the
Size dropdown gets no link to any of it.

Size is the blocking question in apparel. Everything stalls until it is answered, and this
store answers it in a collapsed FAQ several screens below the control that raises it.

**Fix:** put a size guide link immediately beside the Size control, opening the fit content
that already exists. Effort: low, because the content is already written. Impact: highest
in Part 2.

### F2. Colour and size are dropdown menus
**Rules:** P3, P4 (both CONFIRMED, three sources each). **Evidence:**
`desktop__10-pdp1-fold.png`, `desktop__12-pdp1-colour-changed.png`

Confirmed in the DOM: every variant control on the product page is a `<select>`. There are
no swatches and no buttons.

For sizes this costs a click and hides the range. For colour it costs more. This store sells
one design across dozens of colourways where the art renders white on dark garments and
black on light ones. The colour **is** the product's appearance, and a dropdown reading
"Moss" cannot convey that.

Credit where due: changing the dropdown does update the main image correctly, and the
gallery reorders to that colourway. The information is there. The control is the problem.

**Fix:** sizes become buttons. Colours become image swatches showing the garment in that
colour, which the store already has, since the gallery holds 13 images. Effort: moderate,
theme work. Impact: high.

### F3. Nothing reassures the shopper at the moment of doubt
**Rule:** P16 (SINGLE source, uxpeak, unverified). **Evidence:** `desktop__10-pdp1-fold.png`

Related to F1 but distinct. Even without a full size guide, one line of text beside the Size
control would defuse the objection where it occurs rather than five screens later.

**Fix:** a single line under the size control. Draft, needs the humanizer and
structural-humanizer passes before it ships:

> DRAFT COPY - needs humanizer + structural-humanizer before it ships
> "Relaxed fit, true to size. Size down for a closer fit."

That is drawn from the fit block already on the page. Effort: minutes. Impact: moderate.

### F4. The catalogue cannot be filtered by temple
**Rule:** L3 (CONFIRMED). **Evidence:** `desktop__05-collection-fold.png`,
`mobile__05-collection-fold.png`

The All Products page offers exactly two filters: Availability and Price. With 164 products
that differ almost entirely by which temple is printed on them, and secondarily by garment,
neither filter helps anyone.

There is no filter for temple, garment type, colour or size.

**Note, and this is deliberate restraint:** BRAND.md records that navigation runs through
the Easify dropdown rather than Shopify collections, and that this is what keeps links alive
across renames. Whether people arrive wanting "a temple shirt" or "the Logan temple" is an
open question in BRAND.md section 19, and nobody has ever bought anything, so I am not going
to settle it from a screenshot. What is checkable is narrower: the filters that exist do not
match the catalogue.

**Fix:** add garment type and colour filters at minimum. Effort: moderate. Impact: moderate,
and it depends on the open navigation question.

### F5. Searching "temple" returns 164 near-identical results
**Rule:** L3-adjacent. **Evidence:** `desktop__04-search-results.png`

Searching the most obvious word on a temple store returns essentially the whole catalogue,
across seven pages. The first twenty-two results are all "Essential Temple Tee with
personalizable date", every one shown in the same green colourway, distinguished only by a
place name in brackets at the end of a wrapped title.

Two content pages ("Our Story", "Have a design suggestion?") are mixed into the product grid
with no image.

**Fix:** this is really the same problem as F4. The store needs a way to get to a temple,
whether by filter, by a searchable temple index, or by making the search return temples
rather than products. Effort: moderate to high. Impact: moderate.

### F6. Product cards do not show colour options
**Rule:** L6 (SINGLE source, observed on established stores in A1). **Evidence:**
`desktop__05-collection-fold.png`

Cards show image, title, price and a "Choose options" button. No colour swatches, so the
grid gives no sense of the range without clicking into every product.

"Choose options" is also the Shopify default button label.

**Fix:** add colour swatches to cards. Effort: moderate. Impact: low to moderate.

### F7. On mobile, colour and size are below the fold
**Rules:** P1, M1. **Evidence:** `mobile__10-pdp1-fold.png`

The mobile product page shows image, image counter, title, price and the Shop Pay
instalments line. Colour, size, and the buy button all sit below the fold.

Genuine credit: the sticky add-to-cart bar works well on both viewports, appears on scroll,
and carries the thumbnail, title, correct price and a variant selector. That is a CONFIRMED
rule passing cleanly.

**Fix:** tighten the space above the variant controls. Effort: moderate. Impact: moderate.

### F8. The announcement bar is unreadable on mobile
**Rules:** H4, M1, M6. **Evidence:** `mobile__01-home-fold.png`,
`mobile__05-collection-fold.png`

The bar scrolls two alternating messages. On a phone the viewport is narrower than one
message, so at any moment the visitor sees a fragment: "ND 25% OFF" and "FREE SHIPPING ON
ORDERS OV". Neither message is ever fully visible, and because it moves, reading it means
waiting for it.

**Fix:** one message, static, short enough to fit a phone. Effort: low. Impact: moderate.

### F9. The page never says what size is shown in the picture
**Rule:** P5 (CONFIRMED, three independent sources). **Evidence:**
`desktop__10-pdp1-fold.png`

Nothing states which size garment appears in the product image.

This is the one part of the apparel fit research that needs no customers, no reviews and no
models. It is a line of text. Three separate sources arrived at it independently, and it is
the cheapest unblocked win in this report.

**Fix:** state the size shown, in the image caption or beside the fit block. If the mockup
is generated at a fixed size, the generator already knows which. Effort: low. Impact:
moderate.

---

# Part 3: Blocked, and what would unblock it

Not failures. The store has never had an order, so these cannot be done honestly yet.

| Rule | What it needs |
|---|---|
| Star ratings and review counts on cards, product pages, cart | First orders, then a review request. BRAND.md puts this on the order insert. |
| Customer photographs and user-generated content | Orders, plus the customer feature programme in BRAND.md section 17. |
| Reviews carrying fit data and size purchased | Enough reviews to aggregate. The strongest apparel finding in the research, entirely blocked. |
| "As seen in" press logos | Press coverage. |
| Best seller and top rated badges | Real sales data. Currently asserted anyway, see E4. |

Two structural constraints, recorded so they are not re-raised as fixes:

- **Free shipping thresholds, gift thresholds and bundle discounts** all appear in the
  research and all come straight out of margin under print-on-demand, which gives no volume
  cost break. The store already runs a free shipping threshold and a BOGO bundle. That is
  Evan's call and it is priced against nothing.
- **Lifestyle photography** showing garments worn by people is blocked behind the Tapstitch
  garment decision, per BRAND.md. The unblocked half is C1's suggestion: a flat lay of a
  sample Evan already owns, on a plain background.

---

# Part 4: What the store does well

Worth stating, because a report that lists only failures misrepresents the site.

- **The hero photograph is real.** It is a genuine flat lay of actual garments, not a
  floating mockup on white. Five separate sources in the research identify generic mockups
  as the thing that destroys credibility for small apparel brands. This store already
  avoids the worst version of that problem on its homepage.
- **The product grid is visually consistent.** Same angle, same crop, same white background,
  garment centred, across 164 products. This is the finding the research ties most directly
  to trust at a premium price, and the generator pipeline is already enforcing it.
- **The founder intro is on every product page and it is signed.** A named human standing
  behind the brand is a rule most stores fail. This one passes, and only the type size
  undermines it.
- **The fit content is genuinely good.** Weight, fabric, "Fit: Relaxed, true to size", and a
  five-step fit ladder. Better than most apparel stores. It is only in the wrong place.
- **The sticky add-to-cart works properly on both viewports.**
- **Add to cart correctly outranks Buy It Now.** The research flags the Shopify default of a
  solid express-wallet button above a plain outlined add-to-cart. This store has it the
  right way round.
- **Persuasive copy is visible and reference detail is collapsed**, which is the right side
  of the one real disagreement between sources in the research.

---

# Full scorecard

68 rules. **PASS 38, FAIL 27, N/A 3.**

The nine blocked items listed after the tables are not separate numbered rules. They are the
social-proof patterns the research recommends that this store cannot implement honestly at
zero orders, recorded so they are not mistaken for oversights.

## Home
| # | Rule | Result | Evidence |
|---|---|---|---|
| H1 | Hero shows product worn or in use | FAIL | `desktop__01-home-fold.png` (real flat lay, but not worn) |
| H2 | Exactly one CTA above the fold | FAIL | `desktop__01-home-fold.png` (zero on desktop) |
| H3 | Hero is a single image, not a carousel | FAIL (SINGLE) | `desktop__01-home-fold.png` |
| H4 | Announcement bar is one line, one message | FAIL | `mobile__01-home-fold.png` |
| H5 | Homepage says what the brand is | PASS | `desktop__02-home-full.png` |
| H6 | Shipping and returns as readable text | PASS | `desktop__02-home-full.png` |
| H7 | Menu has roughly five items | PASS (6) | `desktop__03-nav-open.png` |
| H8 | No "Home" entry in the menu | FAIL (SINGLE) | `desktop__03-nav-open.png` |
| H9 | Every menu item leads toward buying | FAIL (SINGLE) | `desktop__03-nav-open.png` (1 of 6) |
| H10 | Footer has company and policy pages | FAIL | `desktop__40-footer.png` |
| H11 | Every homepage image links somewhere | FAIL | `desktop__02-home-full.png` |
| H12 | No default theme wording | FAIL (SINGLE) | `desktop__40-footer.png` ("Quick links") |
| H13 | Country selector lists only shipped regions | N/A | no selector on storefront |
| H14 | Nothing above the fold animates | FAIL (SINGLE) | `desktop__01-home-fold.png` |

## Collection
| # | Rule | Result | Evidence |
|---|---|---|---|
| L1 | Consistent angle, crop, background, lighting | PASS | `desktop__05-collection-fold.png` |
| L2 | Product edges clearly visible | PASS | `desktop__05-collection-fold.png` |
| L3 | Filters match how the catalogue is browsed | FAIL | `desktop__05-collection-fold.png` |
| L4 | Cards have a desktop hover state | PASS | `desktop__07-collection-hover.png` |
| L5 | Default card image is the clearest | PASS | `desktop__05-collection-fold.png` |
| L6 | Cards show colour options | FAIL (SINGLE) | `desktop__05-collection-fold.png` |
| L7 | Product count stated | PASS | "164 products" |

## Product detail page
| # | Rule | Result | Evidence |
|---|---|---|---|
| P1 | All decision info without scrolling | FAIL | `mobile__10-pdp1-fold.png` |
| P2 | Size guide reachable above the fold | FAIL | `desktop__10-pdp1-fold.png` (none exists) |
| P3 | Sizes are buttons, not a dropdown | FAIL | `desktop__10-pdp1-fold.png` |
| P4 | Colours are images, not plain dots | FAIL | `desktop__12-pdp1-colour-changed.png` |
| P5 | States the size shown in the image | FAIL | `desktop__10-pdp1-fold.png` |
| P6 | Add to cart is most dominant | PASS (SINGLE) | `desktop__20-cart-drawer.png` |
| P7 | Add to cart outranks express wallet | PASS (SINGLE) | `desktop__20-cart-drawer.png` |
| P8 | Sticky add-to-cart on scroll | PASS | `desktop__14-pdp1-scrolled-sticky.png` |
| P9 | Gallery shows more images exist | PASS | `mobile__10-pdp1-fold.png` ("1/13") |
| P10 | Shipping and returns near add-to-cart | PASS | `desktop__20-cart-drawer.png` |
| P11 | Sections answer fabric, care, fit, origin | PASS | `desktop__14-pdp1-scrolled-sticky.png` |
| P12 | Benefit-led copy, scannable | PASS | `desktop__14-pdp1-scrolled-sticky.png` |
| P13 | Selling copy visible, reference collapsed | PASS | `mobile__14-pdp1-scrolled-sticky.png` |
| P14 | Emotional before technical | PASS (SINGLE) | `desktop__14-pdp1-scrolled-sticky.png` |
| P15 | Would work as a landing page | PASS | `desktop__11-pdp1-full.png` |
| P16 | Reassurance beside the doubt | FAIL (SINGLE) | `desktop__10-pdp1-fold.png` |
| P17 | No fabricated scarcity or countdown | FAIL | `mobile__20-cart-drawer.png` |
| P18 | No unearned badge | FAIL | `desktop__10-pdp1-fold.png` ("MOST POPULAR") |

## Cart
| # | Rule | Result | Evidence |
|---|---|---|---|
| C1 | Drawer opens without a page load | PASS | `desktop__20-cart-drawer.png` |
| C2 | Checkout button reachable on mobile | PASS | `mobile__20-cart-drawer.png` |
| C3 | Discount field not dominant | PASS | `desktop__21-cart-page.png` (absent) |
| C4 | Cart cross-sell buttons have contrast | N/A | no cross-sell buttons in drawer |

## Checkout entry
| # | Rule | Result | Evidence |
|---|---|---|---|
| K1 | Checkout shows logo and brand colours | FAIL | `desktop__30-checkout-entry.png` |
| K2 | Guest checkout available and visible | PASS | `desktop__30-checkout-entry.png` |
| K3 | Express wallets present | PASS | `mobile__30-checkout-entry.png` |
| K4 | No unexplained required field | PASS | `desktop__30-checkout-entry.png` |
| K5 | Labels outside the fields | PASS | `desktop__30-checkout-entry.png` |
| K6 | No information requested twice | PASS | `desktop__31-checkout-entry-full.png` |
| K7 | Payment fields visually enclosed | N/A | not reached; requires entering an address |
| K8 | No open discount box | PASS | `desktop__30-checkout-entry.png` |

## Trust and credibility
| # | Rule | Result | Evidence |
|---|---|---|---|
| T1 | Typeface is not the theme default | PASS | Montserrat, Shrine Pro theme |
| T2 | A real logo, not default type | PASS | `desktop__01-home-fold.png` |
| T3 | Deliberate colour palette | PASS | `desktop__02-home-full.png` |
| T4 | App widgets styled to match | FAIL (SINGLE) | `mobile__20-cart-drawer.png` |
| T5 | A named human behind the brand | PASS (SINGLE) | `desktop__14-pdp1-scrolled-sticky.png` |
| T6 | Contact details findable | FAIL (SINGLE) | `desktop__40-footer.png` (no address or phone) |
| T7 | Policy pages exist and are linked | PASS | `desktop__40-footer.png` |
| T8 | Body text at least 16px | FAIL (SINGLE) | measured 13.5px / 12.6px |
| T9 | Body text has strong contrast | PASS | measured |
| T10 | Photography looks made by this brand | PASS | `desktop__01-home-fold.png` |
| T11 | Nothing asserts an untruth | FAIL | `desktop__30-checkout-entry.png` |

## Mobile
| # | Rule | Result | Evidence |
|---|---|---|---|
| M1 | Rules pass on mobile too | FAIL | `mobile__01-home-fold.png` |
| M2 | Primary buttons full width | PASS (SINGLE) | `mobile__20-cart-drawer.png` |
| M3 | Floating widgets do not overlap | PASS (SINGLE) | `mobile__14-pdp1-scrolled-sticky.png` |
| M4 | No simultaneous cookie banner and popup | PASS (SINGLE) | neither appeared |
| M5 | Sticky action bar at the bottom | PASS (SINGLE) | `mobile__14-pdp1-scrolled-sticky.png` |
| M6 | Text readable without zooming | FAIL (SINGLE) | measured 13.5px |

## Blocked (all N/A)
Ratings on cards, ratings on product pages, review counts, review text, customer photos,
UGC in the gallery, fit scales from reviews, size-purchased on reviews, press logos.

---

# One thing this audit cannot tell you

BRAND.md records 558 sessions in a year, 4 checkouts reached, 0 completed, and states that
distribution is the only constraint.

Every fix above removes a reason not to buy. None of them creates a visitor. Fixing E1
through F9 on a store nobody visits changes nothing until the traffic problem is addressed
separately. The one real read on this from the underlying research is a video reviewing two
small clothing brands with finished products and active social accounts, making $400 and
$650 a month after a year of trading.

The checkout question is the exception worth acting on regardless. Zero of four completed
checkouts is unexplained, and E1 (a price that changes between the product page and the
cart), E2 (a false claim on the checkout screen) and E7 (an unbranded checkout) are three
plausible contributors that cost very little to remove.
