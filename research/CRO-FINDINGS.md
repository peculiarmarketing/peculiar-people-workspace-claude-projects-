# CRO Findings

Synthesised 2 September 2026 from twelve YouTube videos, watched in full or in named
sections. Per-video notes with timestamps live in `research/cro-videos/`.

## How to read this

**These are videos, not studies.** Ten of the twelve are made by people selling a service:
an agency, an app, a template, a course, a page builder. Every claim here is a
practitioner's opinion unless marked otherwise. One source (A4, Baymard) presents actual
usability research with stated sample sizes; it is also twelve years old.

Labels:

- **CONFIRMED**: two or more *independent* sources say it.
- **SINGLE SOURCE**: one source only. Kept, but unverified.
- **CONFLICT**: sources disagree. My read is given with reasoning.

**Independence note.** A3 and B4 are both Kurt Elster. Where they agree that is one source,
not two, and it is counted as one throughout. That leaves eleven independent voices.

**On statistics.** The rule was to discard any number unless two sources gave the same
figure. **No number survived.** Not one statistic was repeated by a second source anywhere
in twelve videos. Every percentage quoted in any of these videos is therefore excluded from
this document. The individual notes record what each source claimed, so nothing is lost, but
none of it should be used to justify a decision.

---

## 1. Home page

### CONFIRMED

**The hero shows the product in use on a person, not floating on a blank background.**
Six independent sources: A1, A2, B1, B4, C1, C2. B1 states it as apparel-specific reasoning.
A2 gives it a name, the "imagination gap": the shopper cannot pick the item up, so the image
has to close the distance between an object and the experience of owning it.

**There is exactly one primary call to action above the fold.** B1, C3.

**The homepage does more than list products.** B2 calls it a business card: a visitor should
be able to tell who you are and what you do from it. C2 calls it "a guided conversation, not
a gallery of images." C3 argues an alternating rhythm of sections reads as a brand campaign
where a repeating product grid reads as a catalogue. B2 explicitly rejects the excuse that a
small catalogue justifies a bare homepage.

**The announcement bar is one line carrying one message.** B1 shrank a three-line bar and
spent the space above the fold. B3 criticises a mobile header stack consuming 20 to 25% of
the screen.

**Navigation is organised the way customers shop, not the way the catalogue is filed.**
A1, C2, and Kurt (A3/B4). C2 supplies the most examples: by trade, by occasion, by activity,
by audience. Kurt's apparel version is audience first, then type.

**The footer carries company and policy pages, and their presence is itself the signal.**
B2 and Kurt (B4). Kurt gives a layout: logo left, three link columns (catalogue, customer
care, about), newsletter, social icons.

**Shipping and returns terms appear as prominent text near the top of the funnel.**
A1 (observed on Maguire, Kirrin Finch, Chubbies), B1 (a policy bar under the nav), B2, C2.

### SINGLE SOURCE

- **The hero is a single image, not a carousel.** Kurt (B4). His reason: "the big advantage
  of a carousel is settling debates internally in an organisation, as opposed to
  communicating something."
- **The hero image should provoke either "I love it" or "not for me."** Kurt (B4). An image
  that provokes neither is not working.
- **Menus hold about five items; remove "Home" and "Shop All"; move "About" to the footer.**
  Kurt (A3/B4).
- **Everything in the main menu should lead to money.** Kurt (A3).
- **Remove the country/shipping selector if you do not ship to those countries.** B2. His
  reasoning is credibility: a new store listing dozens of countries is pretending to be a
  worldwide company.
- **Every image on the homepage links through to something.** Kurt (B4).
- **Hero copy is not a description of the catalogue.** C1 rejects "browse our selection of
  X apparel" as generic; prefers openings like "Inspired by..." or "Representing..."
- **Section headings are not left as theme defaults.** C1 flags "Current Collection" as
  obviously stock text.
- **Press logos ("as seen in") above the fold.** B1.

---

## 2. Collection page

### CONFIRMED

**Product photography is consistent across the grid: same angle, background and lighting.**
C2 names the mechanism explicitly, on FRYE: "creates visual continuity, a huge trust builder
for higher priced items." C1 argues the same property from the failure side, telling a brand
its decorative backgrounds hide the garment's edges so quality cannot be judged.

**The background is plain enough that the product's edges are clearly visible.** C1, C2.

**Filters are present and match how the category is browsed.** A1 (size, colour, price on
Maguire and Allbirds), C2 (Fishwife).

**Product cards have a hover state on desktop.** B3 (quick-add appearing on hover, and he
notes a mobile-first design ported to desktop loses this), C3.

**Product cards carry ratings and review counts.** A1 (observed on Tentree, Allbirds), C2
(Flag & Anthem). *Blocked, see section 8.*

### SINGLE SOURCE

- **Product cards carry colour swatches.** A1, observed on Tentree and Allbirds.
- **The filter control states the product count.** A1, observed on Allbirds ("31 products").
- **The default card image is the clearest one.** C1 caught a store whose clean product shot
  was the *hover* image and whose decorative shot was the default. The good photograph
  existed and was hidden behind an interaction.

---

## 3. Product detail page

This is where the sources converge hardest, and where apparel diverges from everything else.

### CONFIRMED

**Everything needed to decide is visible without scrolling.** B3 enumerates it: imagery,
price, reviews, colour, size, size guide, add to cart. C2 says it of FRYE and states it as
the takeaway for BRUNT. B1 and A1 agree.

**The size guide is reachable above the fold.** B1 (says he is "amazed" a major menswear
brand does not do this), B2, B3.

**The size selector is buttons, not a dropdown.** B2 (argues from click count), A2
(calls dropdowns "lazy design" because they force a click just to learn the options), B1
(size options pulled above the fold as buttons).

**Colour options are shown as photographs of the product in that colour, not as plain
colour dots.** B1 states it directly for apparel: "it allows people to visualise what colour
is actually changing on the product." A2 makes the same move with imaged swatches.

**The page states what size the model or mockup is wearing.** B2, B3, C2. Three independent
sources. B3 goes furthest: state the model's height, the size worn, and where the garment
runs small or large ("this model is a size 10 but is wearing a 12 because it's very tight
fitting"). He claims it both raises conversion and lowers returns. **This is the single
strongest apparel-specific finding in the research.**

**Reviews carry a fit dimension, not only a star rating.** B3 (an aggregate fit scale, plus
size purchased and size normally worn on each review), C2 (Pepper's fit notes). *Blocked.*

**The product page is built like a landing page, not an order form.** Kurt (A3) gives the
test: "if your product page was a landing page, would it work?" A5 and C2 (Modern Mammals,
"make your product page your best salesperson") agree.

**Below the fold, named blocks answer the practical questions.** A5 (Graza: size, harvest,
uses, ingredients, recipes), Kurt (A3: layered description with subheading, pull quote,
narrative, bullets, then detail), B3 (fabric, fastening, washing, ironing), B2 (where it is
made, shipping and returns), C2 (ingredients, dimensions, materials).

**Copy leads with the benefit, not the feature, and uses bullets for skimmers.** A1 (his
example: "keeps your gear dry even if your feet get wet" rather than "waterproof"), A5.

**Shipping and returns terms sit near the add-to-cart button as plain text.** A1, B1, B2.

**There is a sticky add-to-cart once the main one scrolls away.** A1, B3. B3's reason: "you
only have that split second when someone might buy it."

**A gallery gives the shopper a way to know more images exist.** B1, B3. *See conflict 6 for
how.*

### SINGLE SOURCE

- **Add to cart is the most visually dominant button on the page.** B2. He points out that
  the Shopify default renders a solid "Buy with Shop Pay" above a plain outlined "Add to
  cart," so the theme's own default makes the wrong button dominant, and the dominant one
  carries someone else's brand. Seen unremarked on another store in C1.
- **Purchase options are side-by-side cards, not stacked radio buttons.** A2. His reason:
  radio buttons present two visually equal choices so users default to lowest risk.
- **The reassurance that defuses an objection sits inside the box where the decision is
  made,** not elsewhere on the page. A2.
- **Extra options appear after a click rather than cluttering the first view.** A2
  (progressive disclosure).
- **Reassurance icons are specific to what this buyer fears, not generic.** A2.
- **Emotional content first, rational content second.** C2 (Rumpl).
- **Customer photos are placed inside the image gallery,** so people who never scroll still
  see them. Kurt (A3). *Blocked.*
- **Product photos are annotated with callouts.** Kurt (A3).
- **Review counts are specific, not rounded.** A2. *See conflict 4.*
- **A status badge sits above the product title.** A2. *Blocked and would be dishonest here.*
- **The page states where the product is made.** B2.

---

## 4. Cart

### CONFIRMED

**The cart is a drawer that does not require a page load.** A5, B1, B2.

**The checkout button is reachable without scrolling on mobile.** B1, B3.

**The discount code field is not the most visually prominent element.** B3 questions a
green, dominant discount field. A4 goes further with actual research: users give
disproportionate attention to *empty* form fields, and a visible coupon box makes them feel
they are overpaying and sends them off-site hunting for a code. A4's remedy is to hide it
behind a link. Two independent sources, and one of them is the only research-grade source
in the set.

**A free shipping threshold is shown with a visual progress indicator.** B1, B2, B3.
*Conflicted on economics, see section 8.*

### SINGLE SOURCE

- **A second threshold above free shipping unlocks a gift.** B1.
- **Cart cross-sells use a high-contrast button.** B1 (criticising a white button on a white
  background: "it's just not going to get clicked").
- **A customer review appears inside the cart drawer.** B1. *Blocked.*
- **Cart cross-sells are pattern-based, not random** (matching designs, "complete your
  uniform"). C2.

---

## 5. Checkout entry

Most of this section is Baymard (A4), the only research-grade source, and most of it is
already handled by Shopify's own checkout. What remains is what a merchant can still get
wrong.

### CONFIRMED

**The checkout carries the brand's logo and colours.** Kurt (A3) calls an unstyled checkout
the single most common mistake he sees, describes stores that cost $100,000 to build
dropping to a plain text logo at checkout, and puts the fix at 60 seconds. A5 independently
criticises a checkout with no branding, no trust marks and no shipping information.

**Guest checkout is offered and visible.** A4 (research: 60% of users overlook the guest
checkout option and then perceive the checkout as forced account creation; it belongs
top-left, following the western reading pattern), A1.

**Information already given is not asked for again.** A4 (research: 50% of sites do this,
and it rarely happens on the same page so it is easy to miss; prefill name, email, zip, and
any address already typed), A1 (address autofill).

**Express wallets are supported.** A1, A5, B3.

### SINGLE SOURCE (all A4, all research-grade)

- **Every field is either optional or explains itself.** 61% of sites require a phone number
  without saying what it is for. Subjects were "very forgiving" when the reason was given.
- **Labels sit above or beside fields, never as placeholder text inside them.** Inline
  labels look clean but each field loses its context the moment typing starts, and they are
  worst during error recovery.
- **Typed data survives a validation error.**
- **Error messages appear next to the offending field, never only at the top of the page.**
- **Error messages state the rule that was broken.** Not "invalid phone number" but
  "+ character not allowed" or "10 digits required."
- **Payment fields sit in a visually enclosed block** (border, background tint, security
  icon). 89% of sites do not do this. This is about *perceived* security, not actual.
- **Account creation is offered after the order, on the confirmation page,** where it is
  perceived as only two fields.

---

## 6. Trust and credibility (cross-cutting)

This is the section that answers the brief.

### CONFIRMED

**A generic or stock-looking store destroys credibility, and visitors infer product quality
from it.** Four independent sources: C1, B2, C3, Kurt (A3). C1 states the mechanism most
precisely: "when you come across a brand where it just looks really generic, it hurts your
credibility, it just feels like it's not legit, like the product quality is not going to be
that good when they receive it in the mail." The visitor makes a judgment about the physical
garment from the quality of the image of it.

**The specific tells named by these sources:**
- Unmodified theme defaults. B2 identifies a store as untouched Shopify Dawn on sight, from
  the default font. C1 flags "Current Collection" as obvious stock heading text.
- No logo, or a wordmark set in the theme's default type. B2.
- Colours that appear once and nowhere else, with no palette. B2.
- Components that visibly come from different places. C3: "a lot of Shopify stores feel a
  little bit stitched together because we're using a ton of random different apps, one for
  reviews, one for videos, one for products."
- Copy that reads as generated. Kurt (A3): "I don't just want copy-pasted AI slop."
- Generic mockups. C1.

**The judgment is made in seconds.** Kurt (A3) lists the questions a visitor's brain runs
on landing: is this legit, are they real, should I be concerned, are they authentic. C1
frames his whole review as first impressions.

**Credibility signals are cumulative and there is no single threshold.** Kurt (A3) is
explicit that he does not know where the line sits and that it differs per person.

**Brand colours and typography are consistent across the site.** B2, C2, C3.

**Company and legal pages exist and are linked in the footer.** B2, Kurt (B4).

**Restraint reads as expensive.** C3: "expensive-looking premium ecommerce isn't about
adding more." C2 shows the same through fifteen examples. Kurt (B4) adds the essential
counterweight, below.

### SINGLE SOURCE, high value

- **Visual consistency across the catalogue is a trust builder specifically for
  higher-priced items.** C2, on FRYE. And the line that follows it: **"Clean visual systems
  build trust faster than discounts ever could."** One source, no evidence, and the most
  directly useful sentence in twelve videos for a premium brand with no reviews.
- **Show the founder as a person.** Kurt (A3): "I want the person, not the brand." Ideally
  video. His argument is that an About page is no longer table stakes now anyone can
  generate one, so the bar has moved to evidence of a real human.
- **A physical address and a phone number in the footer.** Kurt (A3).
- **Restraint executed badly reads as unreadable, not premium.** Kurt (B4) names the trap:
  "in design there's this idea that subtle is sophisticated, and the problem is subtle is
  not great when you're just trying to read it on your phone." His rule: body text black on
  white, at least 16px. "The web is 90% typography."
- **"Ugly" high-converting sites are actually just readable ones.** Kurt (B4) explicitly
  rejects the crude version of this claim. The properties he identifies are plain copy,
  strong typography, and not hiding content, not ugliness.
- **Self-shot photography beats better mockups.** C1: "just lay your products down on a
  table, get a nice white light, and take the pictures yourselves."
- **Lifestyle photography shows scale and real use rather than polished staging.** C2, on
  Gathre.

### Blocked but universally recommended

Reviews, star ratings, review counts, customer photographs, user-generated video, verified
buyer badges, "as seen in" press logos, and best-seller badges are recommended by nearly
every source. All of them require sales or coverage that do not exist. Section 8 covers this.

---

## 7. Mobile (cross-cutting)

### CONFIRMED

**Mobile is checked separately, not assumed from desktop.** A1 ("mobile first is
mandatory"), B2 (floating widgets that are tolerable on desktop overlap on mobile), B3
(reviews mobile first, then desktop, and finds most of the missed opportunities on desktop
precisely because the site was built mobile-first). Kurt (B4) demonstrates the failure by
accident: he tries to demo an apparel site on his phone, cannot get screen mirroring
working, and does the entire apparel teardown on desktop.

**A design built mobile-first and ported to desktop loses its hover states and feels
inert.** B3, C3.

### SINGLE SOURCE

- **Primary buttons are full width on mobile.** B1, who points out that the "before" button
  was a small square most viewers could not find.
- **A sticky bar belongs at the bottom on mobile, where the thumb is.** B3, who then honestly
  flags that the site he was reviewing puts it at the top, that top draws more attention,
  and that this is a thing to test rather than a rule.
- **Floating corner widgets must not overlap each other.** B2, who found a discount tab
  sitting on top of a cart bubble.
- **A cookie banner and an email popup must not fire together.** B2, who demonstrates it
  live: accepting the cookie banner dismissed the popup too.
- **Nothing above the fold moves or auto-scrolls.** B2.
- **Pages load in under two seconds on mobile.** A1.
- **Body text at least 16px.** Kurt (B4). Listed here as well as section 6 because it is
  a mobile-readability claim.

---

## 8. Conflicts

### Conflict 1: Payment method icons on the product page and in the cart

- **Add them:** B1 (payment seals under the cart checkout button), B2 (payment icons below
  the add-to-cart).
- **Remove them:** Kurt (B4): "I would kill the payment method icons. Like 30 years ago that
  made sense, it's 2020, everybody knows how online shopping works."

**My read:** low stakes either way, and Kurt himself immediately hedges ("that's also a thing
you could split test... probably won't" make a difference). Note that A4's research finding
is adjacent but not the same claim: it is about visually *enclosing the credit card fields
inside checkout*, which is a different element on a different page. Two-to-one in favour of
keeping them, with the dissenter conceding it probably does not matter. Not worth spending
attention on.

### Conflict 2: Trust badges

- **Add them:** A1 (secure payment icons, money-back guarantees, free shipping badges, via
  an app).
- **Remove them:** A2 ("generic badges like free shipping don't build deep trust anymore
  because shoppers expect them"), and he replaced them with claims specific to his category.
- **Split:** B2 calls free shipping and free returns badges "great" but singles out "secure
  payments" as weak "because everyone has secure payment nowadays."

**My read:** B2's split is the resolution, and A1's own screen evidence supports it. The
established apparel stores shown in A1 (Maguire, Kirrin Finch, Chubbies) display no badge
clusters at all; they display plain text stating an actual policy, such as free shipping
over $200 and a 60-day return policy. The rule that fits all three sources: **state a real
policy in text; do not display a badge asserting a universal minimum.** "Secure payments" is
not a policy. "Free returns for 60 days" is.

### Conflict 3: Number of checkout steps

- **Minimise steps:** A1 ("minimise steps, maximise conversions") plus a progress indicator.
- **Step count is not the variable:** A4, with a chart. The checkout usability score does not
  fall monotonically with step count; six steps outscores four in their data, and only eight
  and nine collapse. The slide's own caption: "It's *not* about the number of checkout
  steps, but what you ask users to do at each step (and how you ask them)."

**My read:** A4 wins clearly. It shows a distribution and names its sample (top 100 US
ecommerce sites, average 5.08 steps); A1 asserts. The progress indicator is not in conflict,
only the step-count claim. Practically this barely matters here, because Shopify's checkout
is not restructurable on Basic.

### Conflict 4: Specific versus vague social proof numbers

- **Specific:** A2 changed "200+ Reviews" to "4.9 stars, 221 reviews," arguing round numbers
  read as an estimate, a placeholder, or fake.
- **Vague:** B1's redesigned homepage reads "4.9/5 by Thousands of Happy Customers."

**My read:** A2 has the better argument, and B1's own product page undercuts his homepage,
because it uses the exact figure 78. Use real numbers. Note also that A2 contradicts himself
within thirty seconds by adding a "500+ sold this week" badge immediately after arguing that
500 is exactly the kind of round number that reads as fake. Academic for now: this store has
no reviews to count.

### Conflict 5: Accordions

- **Do not hide content behind them:** Kurt (B4) lists "not hiding all the content behind
  accordion menus and tabs" as a property of high-converting sites.
- **Use them:** C2 praises three brands for putting ingredients, nutrition, dimensions and
  materials into accordions so pages can be skimmed. A2's progressive disclosure is a
  version of the same idea.

**My read:** they are describing different content. Kurt is arguing against hiding the
*selling* copy, the part that persuades. C2 is describing *reference* detail that only some
shoppers want and that would otherwise bury the page. The rule that satisfies both: the
argument for buying is visible; the reference tables are collapsible.

This matters directly. BRAND.md records that the temple facts were collapsed into rows
because the block had grown to about six phone screens. Under this reading that decision was
correct, because temple facts are reference content. It would be wrong to collapse the
founder intro, which is the selling copy.

### Conflict 6: Gallery navigation affordances

- **Add visible thumbnails and arrows:** B1. "Don't leave things up to guesswork... treat
  people like they're 5 years old."
- **A clean edge-peek is enough:** B3 praises a gallery with no arrows because "it's very
  clear to the user just from the design that you should swipe."

**My read:** B3 names the resolving variable himself in the next breath: "if you have a
slightly older demographic they might think that this looks broken." The answer depends on
who is shopping. Given Peculiar People's buyers include grandmothers buying gifts (BRAND.md,
section 10), B1's explicit-affordance side is the safer default here.

### Conflict 7: Urgency and scarcity

- **Use it:** A2 adds "🔥 500+ sold this week" and calls it a trust anchor. A5 praises a page
  built on "86% off today" and a prize draw. A1 recommends CTA copy that "creates a sense of
  urgency."
- **It is the dropshipper tell:** Kurt (A3) names countdown timers, lightning bolt emojis,
  "sale ends in 10 minutes" and "only one left in stock" as the signals that make him
  distrust a store, and calls fake urgency and fake scarcity flatly illegal.

**My read:** Kurt is right on the merits for this brand, and it is not close. Three
considerations converge. Legally, fabricated urgency is a deceptive practice. Commercially,
the store has zero orders, so any "500+ sold" or "only one left" claim would be false rather
than merely aggressive. And on brand, BRAND.md's guardrails rule out this register entirely.
The sources recommending urgency are also the two weakest in the set by evidence (see the
individual notes for A2's and A5's problems). Excluded.

### Conflict 8: What to do about mockups

Not a disagreement between sources so much as one inside a source. C1 diagnoses generic
mockups as the credibility problem, then offers "buy better mockup files" as his first fix
and "photograph the real garments yourself" as an afterthought. His own diagnosis argues for
the second: a better mockup is still a mockup. A2, C2 and B1 all point the same way, toward
images that show the product in use at real scale.

**My read:** photograph real garments. It is also the cheaper option.

---

## 9. Checkable rules

Pass / fail / not applicable, judged from a screenshot or a short interaction. This is the
raw material for the phase 2 audit skill. Source labels carry the confidence forward.

### Home page

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

### Collection page

| # | Rule | Basis |
|---|---|---|
| L1 | Every product image in the grid uses the same angle, crop, background and lighting | CONFIRMED |
| L2 | Product edges are clearly visible against the background | CONFIRMED |
| L3 | Filters exist and match how this catalogue would be browsed | CONFIRMED |
| L4 | Product cards show a hover state on desktop | CONFIRMED |
| L5 | The default card image is the clearest available image of the product | SINGLE (C1) |
| L6 | Product cards show colour options | SINGLE (A1) |
| L7 | The filter or header states how many products are in view | SINGLE (A1) |

### Product detail page

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
| P13 | The persuasive copy is visible; only reference tables are collapsed | CONFLICT 5, resolved |
| P14 | Emotional content appears before technical detail | SINGLE (C2) |
| P15 | The page would work as a paid-traffic landing page | CONFIRMED |
| P16 | Reassurance text sits next to the control that triggers the doubt | SINGLE (A2) |
| P17 | No fabricated scarcity, countdown or "N sold" counter is present | CONFLICT 7, resolved |
| P18 | No badge asserts something unearned (best seller, top rated) | CONFLICT 7, resolved |

### Cart

| # | Rule | Basis |
|---|---|---|
| C1 | The cart opens as a drawer without a full page load | CONFIRMED |
| C2 | The checkout button is reachable without scrolling on mobile | CONFIRMED |
| C3 | The discount code field is not visually dominant, and ideally is behind a link | CONFIRMED |
| C4 | Cart cross-sell buttons have real contrast against their background | SINGLE (B1) |

### Checkout entry

| # | Rule | Basis |
|---|---|---|
| K1 | The checkout shows the brand's logo and colours | CONFIRMED |
| K2 | Guest checkout is available and visibly offered | CONFIRMED |
| K3 | Express wallet buttons are present | CONFIRMED |
| K4 | No field is required without an explanation of why | SINGLE (A4, research) |
| K5 | Field labels are outside the fields, not placeholder text | SINGLE (A4, research) |
| K6 | No information is requested twice | CONFIRMED |
| K7 | Payment fields sit in a visually enclosed block | SINGLE (A4, research) |
| K8 | No open discount code box invites coupon hunting | CONFIRMED |

### Trust and credibility

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
| T11 | Nothing on the page asserts a fact that is not true | CONFLICT 7, resolved |

### Mobile

| # | Rule | Basis |
|---|---|---|
| M1 | Every rule above passes on a mobile viewport as well as desktop | CONFIRMED |
| M2 | Primary buttons are full width on mobile | SINGLE (B1) |
| M3 | Floating widgets do not overlap each other or the cart | SINGLE (B2) |
| M4 | A cookie banner and an email popup do not appear simultaneously | SINGLE (B2) |
| M5 | A sticky action bar sits at the bottom of the screen | SINGLE (B3, hedged) |
| M6 | Text is readable without zooming | SINGLE (Kurt) |

---

## 10. Findings that conflict with BRAND.md or with print-on-demand

Set aside deliberately, not dropped. Each is a real finding that cannot be applied as stated.

### Blocked: needs sales or customers that do not exist

BRAND.md records zero orders, ever. The following are recommended by most sources and cannot
be implemented honestly today:

- Star ratings and review counts anywhere (home, collection, product, cart).
- Review text, pull quotes from reviews, verified-buyer badges.
- Fit scales derived from reviews, and per-review "size purchased / normally wears" data.
  This is the strongest apparel finding in the research and it is entirely blocked.
- Customer photographs and user-generated video, including in the image gallery.
- "Best seller", "top rated", "N sold this week" and any social-count badge.
- "As seen in" press logos.

**What is not blocked:** the *model size* half of the fit finding. B2 and B3's core point is
that a shopper needs to calibrate the garment against a body. Stating the size shown in the
image needs no customers at all. It should be treated as available now.

### Blocked: needs the garment decision

BRAND.md holds the blanks open pending Tapstitch samples and says not to build content
showing products that may be discontinued.

- Lifestyle and campaign photography (C3's alternating homepage rhythm, C2's Adanola-style
  tall image stacks on real bodies).
- Any substantial photo shoot.

**Partially available:** C1's flat-lay suggestion, photographing a delivered sample on a
plain white background, is small enough to survive a blank change and directly addresses
the mockup problem. Worth separating from the larger shoot.

### Conflicts with print-on-demand economics

Printify gives no volume cost break, so every one of these comes straight out of margin with
no cost relief behind it:

- Free shipping thresholds and the progress bar that drives them (B1, B2, B3).
- Gift-with-purchase thresholds (B1).
- Bundle tiers at 10% and 20% off (A2).
- Multi-buy discounts of any kind.

The *mechanic* of encouraging a larger order is still right, and BRAND.md already names
multi-temple orders as an AOV lever. What does not transfer is funding it with a discount.
C2's framing is the useful one: "complete your uniform" as a merchandising idea rather than
a price cut.

Also structurally unavailable: subscriptions (a temple tee is not a consumable), and control
of shipping speed.

### Conflicts with BRAND.md guardrails

- **Urgency and scarcity** (A1, A2, A5). Covered in conflict 7. Excluded on legal,
  factual and brand grounds simultaneously.
- **Discount-led page structure** (A5's Everyday Dose example, several of C2's discount
  heroes). BRAND.md holds premium pricing deliberately, and records that discounting before
  reviews exist trains buyers to wait and leaves the trust problem untouched. C2's own line
  is the counter-argument: clean visual systems build trust faster than discounts.
- **CTA copy that manufactures excitement.** A1 recommends urgency in button copy; A2
  recommends "Add to cart, start my journey." Both sit badly with a reverent, understated
  brand. The finding that survives is narrower: the button should say what happens next and
  be the dominant element, not that it should be enthusiastic.

### Conflicts with existing, deliberate decisions

These are places where a source's general rule collides with a specific choice already made
for a reason. Flagged for Evan, not resolved here.

- **Collapsed temple facts.** Kurt (B4) argues against hiding content in accordions. The
  facts were collapsed because the block ran to about six phone screens. Conflict 5's
  reading supports the existing decision: reference content may collapse, selling copy may
  not. Worth confirming that the founder intro is not also collapsed.
- **Navigation by temple rather than by shopper intent.** C2 and Kurt both argue navigation
  should mirror how people shop. Every example they give organises by audience, occasion,
  activity or trade. Peculiar People organises by building, through an Easify dropdown
  rather than Shopify collections, and BRAND.md notes that structure is what keeps the
  dropdown links alive across renames. Whether a buyer arrives wanting "a temple shirt" or
  "the Logan temple" is unknown, because nobody has ever bought anything. **Do not resolve
  this from a video.** It is a real open question and the beachhead decision touches it.
- **Homepage as product grid.** C3 argues an endless product grid reads as a catalogue
  rather than a brand. With roughly 167 near-identical products differing only by temple, a
  grid is the natural output of the catalogue, and the prescribed alternative needs imagery
  that is blocked on the garment decision.
- **Front-of-garment branding.** Several sources treat brand marks as a credibility signal.
  BRAND.md already identifies a front logo as a legitimacy fix and has it blocked behind the
  Tapstitch decision and the $4.90 second-print-location cost. Nothing here changes that
  analysis; it corroborates it.

---

## 11. What this research cannot tell us

Stated plainly so the phase 2 audit does not overclaim.

1. **No source reached a real checkout.** B1, B2, B3, C1 and Kurt all stop at the cart.
   A4 covers checkout properly and is from 2014, before Shopify's current checkout existed.
   Given BRAND.md's priority one is verifying that checkout works after four reached and
   zero completed, the videos are close to useless on the single most important question.
2. **Almost nothing here is measured.** One source shows research with sample sizes. The
   rest are opinions from people selling services. No statistic survived the two-source test.
3. **Nothing here addresses traffic.** BRAND.md is explicit that distribution is the only
   constraint. C1 is the one source that touches the reality: two real brands with finished
   products and active social accounts were making $400 and $650 a month after a year. A CRO
   audit can remove friction and raise credibility. It cannot manufacture visitors, and a
   perfect store with no traffic converts nothing.
4. **The sources skew to categories with repeat purchase.** Supplements, coffee, deodorant,
   olive oil, tinned fish. Much of the AOV and retention advice assumes economics a
   one-off apparel purchase does not have.
