# A4. 8 Checkout Optimization Lessons from 5+ Years of Testing at the Baymard Institute

## Source
- Channel: VWO. Presenter is Christian Holst, co-founder of the Baymard Institute.
- Length 1:08:24, published 17 Nov 2014
- https://www.youtube.com/watch?v=6wwKZDzJEnM
- Watched: 04:33 to 46:26, the eight lessons. Native captions.
- Frame note: the watch script's scene detection found only 9 slide changes across the 42
  minutes, because the deck cross-fades. I re-extracted at one frame per 60 seconds
  directly with ffmpeg and read 42 slides. Every claim below is read off a slide, not
  inferred from the audio.

**Age warning, restated.** This is from 2014. It is on the list because it is the only
substantial free recording of Baymard's checkout research, and because BRAND.md puts
"verify checkout works" as priority one after four checkouts reached and zero completed.
Findings about form behaviour and human error recovery have held up. Anything about
specific payment methods or mobile is twelve years stale and is not recorded below.

## Testable claims, each read from a slide

**1. Number of checkout steps.** The slide's own caption: "It's *not* about the number of
checkout steps, but what you ask users to do at each step (and how you ask them)." The
chart plots a checkout usability score against step count and does not fall monotonically:
2 steps scores highest, but 6 steps scores higher than 4. Only 8 and 9 steps collapse.
Average across the top 100 US ecommerce sites was 5.08 steps from cart to order review.
- Rule: do not count steps. Audit what each step asks for.

**2. Form field attention.** Users give disproportionate attention to *empty* form fields.
The specific consequence named: a visible coupon code field makes users feel they are
overpaying, and sends them off-site hunting for a code.
- Rule: no open coupon field in checkout. Put it behind a link.
- Evidence shown: eye-tracking heatmaps, 32 participants, on L.L.Bean and REI.

**3. Seemingly unnecessary information.** Subjects were "very forgiving if the site
explained *why* phone was required." 61% of sites require a phone number without
explaining what it is for. The same applies to gender, date of birth, and similar.
- Rule: every field is either optional or carries a one-line reason. The worked example on
  the slide is Williams-Sonoma, which labels its phone field "(for delivery questions only)".

**4. Do not ask for the same information twice.** 50% of sites ask for the same information
multiple times during checkout. It rarely happens on the same page, so it is easy to miss.
- Rule: pre-fill anything already typed, in particular cardholder name, email, zip, and any
  address entered earlier.
- Sharper rule from the slide: for most B2C sites the billing address can default to the
  shipping address, and the right move is to hide the billing fields entirely rather than
  pre-fill them.

**5. Avoid inline labels.** Labels placed inside the field look visually simple, but the
fields become hard to interact with, and "each field loses its context the second the user
starts typing." Called out as especially damaging during error recovery.
- Rule: labels sit above or beside fields, never as placeholder text inside them.

**6. Placement of guest checkout.** 60% of users overlook the guest checkout option, and
the checkout is then perceived as forced account creation.
- Rule: guest checkout sits top-left, following the western reading pattern.
- Second rule from the same slide: postpone account creation to after the order. The
  Crate&Barrel example shown offers account creation on the order confirmation page, where
  it is perceived as only two fields because the rest is already known.

**7. Perceived level of security.** Subjects described specific *areas* of a checkout page
as secure or insecure, and were primarily concerned about their credit card details.
Visual devices, specifically a border, a background colour, and a security icon, raise the
perceived security of the area they enclose. 89% of sites do not visually encapsulate their
credit card fields.
- Rule: the payment fields sit in a visually distinct enclosed block.
- Note: this is about perceived security, an aesthetic property, not actual security.

**8. Validation errors.** The slide states 100% abandonment on unresolved errors. Four
sub-rules, all printed:
   1. Persist all typed data. Retyping is infuriating and causes repeat errors.
   2. Highlight the field and put the error description next to it. Never only at the top
      of the page.
   3. The error message states the rule that was actually broken. Do not write "invalid
      phone number"; write "+ character not allowed" or "10 digits required."
   4. Prefer non-blocking warnings over hard validators. Only 36% of sites use address
      warnings rather than blocks.

## Apparel-specific

None. Checkout is category-neutral and this deck treats it that way.

## What was shown that contradicts what was said, and cross-source conflict

**Within this source:** nothing. The slides and the narration agree, and every quantitative
claim is printed on the slide with the sample described. This is the most disciplined source
on the watchlist by a distance.

**Against A1, a real conflict.** Shopify's own video says "minimize steps, maximize
conversions" and recommends a progress indicator showing checkout steps. Baymard's data
says step count is not the variable and shows a six-step checkout outscoring a four-step
one. These cannot both be treated as rules. My read, for the synthesis: Baymard wins, because
it shows the distribution and names the sample, while A1 asserts. The progress indicator is
not in conflict, only the "fewer steps" claim is.

**Against A2, a partial conflict.** A2 removed the reassurance icons under the button as
"generic" and expects shoppers to discount them. A4's lesson 7 finds that visual security
devices measurably change perceived security. These are reconcilable: A4 is about
enclosing the payment fields inside checkout, A2 is about badge clutter on a product page.
Different pages, different claims. Not a true conflict, and worth saying so rather than
listing it as one.

## Statistics stated

All of these are printed on slides with the research described, which is a much stronger
footing than a presenter's spoken number. Still single-source for the purposes of the
two-source rule, so they stay labelled:
- 5.08 average checkout steps, top 100 US ecommerce sites.
- 61% of sites require phone with no explanation.
- 50% of sites ask for the same information more than once.
- 60% of users overlook guest checkout.
- 89% of sites do not encapsulate credit card fields.
- 36% of sites use non-blocking address warnings.
- 100% abandonment on unresolved validation errors.

## Relevance to Peculiar People

The important qualifier: **most of this is not Evan's to change.** Shopify's checkout is
largely locked on the Basic plan, and Shopify already does guest checkout by default,
persists typed data, uses labels above fields, and offers address autocomplete. Lessons 1,
4, 5, 6 and 8 are mostly already handled by the platform.

What remains genuinely actionable and in Evan's control:
- Whether the checkout carries the brand logo and colours. This overlaps exactly with A3's
  first claim and is now confirmed by two independent sources.
- Whether the phone field is required, and whether it explains itself. Shopify lets you set
  this, and it is a live candidate explanation for four abandoned checkouts.
- Whether a discount code field sits open in the checkout. Lesson 2 says an empty coupon
  box is a cost, and a store with zero orders and no active promotions has nothing to gain
  from showing one.
- Whether payment fields read as an enclosed, secure-looking block in the current theme.

Given BRAND.md priority one is "verify checkout works with a real test purchase," lessons 3
and 8 are the two most likely explanations for a silent drop-off that this deck offers.
Neither can be confirmed without walking the checkout, which is exactly what the phase 2
skill is for.
