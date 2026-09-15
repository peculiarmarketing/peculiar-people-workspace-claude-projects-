# B4. Website Teardowns: The Future of eCommerce for Fashion and Apparel

## Source
- Channel: eCommerce Tech. Presenter is Kurt Elster of Ethercycle, live at a conference.
- Length 38:10, published 27 Jul 2020
- https://www.youtube.com/watch?v=qDNzLcoZdOc
- Watched: 02:54 to 21:30, balanced detail, 45 scene-selected frames, native captions.
- Skipped: Bold Bundles and exit-intent popups, both app segments.

Live teardowns of apparel stores submitted by the audience, chiefly **Sicko Clothing**, plus
QuikCamo and Asutra. He states he has not seen any of them before opening them.

**Independence warning.** This is the same presenter as A3. For the two-source CONFIRMED
rule, A3 and B4 are **one source, not two.** Where they agree, that is consistency, not
corroboration. This matters most on the main-menu findings, which appear in both.

## Testable claims

Typography and readability, the core argument
1. Body text is black on white.
2. Body text is at least 16px. His words: "make sure all your text is black on white and is
   at least 16 points so everybody can read it... that really truly is one of the easiest
   layout and design CRO hacks you can use, is make stuff easier to read."
3. "The web is 90% typography."
4. He names a specific design trap: "in design there's this idea that subtle is
   sophisticated, and the problem is subtle is not great when you're just trying to read it
   on your phone." Low-contrast, small, elegant type is the failure mode of a brand trying
   to look premium.
5. Content is not hidden behind accordions and tabs by default. He lists this among the
   things "ugly" high-converting sites do right: "not hiding all the content behind
   accordion menus and tabs."
6. Headline size and content width are set in relation to each other. He uses
   grtcalculator.com, plugs in the font and size, and gets the appropriate content width.
   His live example: a 48px headline should sit in about a 1600px width, and the site he
   was auditing had a narrow width set that made the headline look broken on desktop.

The "ugly converts" argument, stated carefully
7. He explicitly rejects the crude version. "I don't think it's that ugly necessarily
   converts better. I think it's that what we think of as ugly sites are often very
   functional, very usable sites." The mechanism he names is readability, plain copy, and
   not hiding content, not ugliness itself.
8. He reports that the three highest-revenue sites he has worked on were "ugly as sin," one
   to the point where he wondered if it was broken.
9. Craigslist and Wikipedia are his worked examples: almost all text, load fast, work on
   every device, work with screen readers, and score well on page speed.

Hero and homepage
10. The hero is a single image, not a carousel. His stated reason: "the big advantage of a
    carousel is settling debates internally in an organisation, as opposed to communicating
    something."
11. For apparel specifically, the hero is an aspirational lifestyle or action image. His
    test for whether it works: "you either look at this and go I love it, or you look at it
    and go not for me. One of the two." A hero that does not provoke either reaction is not
    doing its job.
12. Every image shown on the homepage is clickable through to the product. He marks Sicko
    down because some gallery images link and some do not: "if you're going to show it to
    me, let me click and go straight to that product."

Menus
13. A menu holds about five items. His reasoning is short-term memory, by analogy to a
    seven-digit phone number.
14. "Home" is removed. "Everybody knows they can click the logo."
15. "Shop All" is removed, as too intimidating a starting point.
16. "About Us" moves to the footer unless it is genuinely strong.
17. For apparel, the menu is organised by audience first (men, women, kids), then by type
    within each. His reasoning: think about how a physical store works and how people
    actually shop.
18. A plain, sensible main menu beats a badly built mega menu. "I'd rather have someone just
    have a straightforward, sensible main menu than ham-fist a mega menu."
19. On desktop, important links are not hidden behind a hamburger. "What's the advantage
    there? Spread that stuff out."

Footer
20. A specific layout: logo on the left, then three columns of link lists, being catalogue,
    customer care, and about the company, then a newsletter signup and social icons. He
    calls the newsletter there "a safety net."

Animation
21. Use animation sparingly. He is blunt: "I'm very anti-animation at this point... it's not
    entirely unusual that animations one out of 100 times get weird."

Social proof
22. Customer photos are labelled as what they are. He dislikes both "testimonials" and "user
    generated content" as headings and suggests "customer action shots."
23. Limit the customer photo wall to about five of the most striking images rather than
    showing everything.

## What was shown that contradicts what was said, and a real cross-source conflict

**Payment icons: three-way conflict.** Kurt says to remove them: "I would kill the payment
method icons at this point. Like 30 years ago that made sense, it's 2020, everybody knows
how online shopping works." B1 (Oliver Kenyon) adds payment seals under the cart checkout
button as an improvement. B2 (Christian Pon) tells a store to put payment icons under the
add-to-cart. So two sources say add them, one says remove them. Notably Kurt immediately
hedges: "that's also a thing you could split test, see if it makes a difference or not.
Probably won't." A4 (Baymard) is adjacent but not the same claim: its finding is about
visually enclosing the credit card fields inside checkout, not about icons on a product
page. My read for the synthesis: this is a genuine CONFLICT, and Kurt's own hedge suggests
low stakes either way.

**He could not test mobile.** At 19:20 he tries to demo the site on his phone, cannot
remember the name of his screen-mirroring app, and gives up: "otherwise I would do this on
mobile. All right, next time." An apparel teardown at a conference where mobile is the
dominant device, conducted entirely on desktop. The single biggest gap in this source.

**Two sites failed to load properly on camera and he attributed it to himself.** YouTube
embeds and social content did not render, and he says "I apologise that those don't work, I
promise these work, this is entirely me," because he blocks social media on his machine.
Fair, but it means he assessed those sections without seeing them.

**He is auditing on first impression with no data.** He says so openly at the start, and
frames the whole exercise as "a subjective outsider look." He also volunteers that his
colleague's split tests only succeed about one in eight times, and that he has personally
been wrong about a mega menu he loved that lost to "the old crappy one." That is unusually
honest about the limits of this kind of review, and it is the right lens for the entire
watchlist.

**2020.** Five years before the newest source here. The typography, menu and footer findings
are structural and have not dated. His "it's 2020, everybody knows how online shopping
works" argument against payment icons is the one claim where the date matters.

## Statistics stated

- One in eight split tests succeed (attributed to another speaker, Nick).
- Menus of about five items, from short-term memory research he does not cite.
Neither is carried forward.

## Relevance to Peculiar People

This source is unusually well aimed at Evan's actual problem, because it attacks the
assumption behind it.

- Claims 1 to 4 are the most important thing found so far about looking premium. A brand
  positioned as "premium, reverent, understated" is at direct risk of the failure Kurt
  names: subtle grey type at small sizes, low contrast, reading as elegant to its designer
  and as unreadable to a visitor on a phone. Worth checking body text colour and size on
  the live site before anything else.
- Claim 5 conflicts with a decision already made. BRAND.md records that the temple facts
  render as collapsed rows because the block had grown to about six phone screens. Kurt
  argues against hiding content behind accordions. This is a real tension and it should be
  flagged rather than resolved from a video: the collapse was a deliberate response to a
  measured problem (six screens of scroll), which is exactly the kind of local knowledge a
  general rule does not have.
- Claims 13 to 17 are checkable. BRAND.md says navigation runs through an Easify "Temple"
  dropdown on product pages rather than Shopify collections. Kurt's audience-then-type
  structure does not map cleanly onto a catalogue organised by building, which is a genuine
  open question for this store rather than a defect.
- Claim 20 gives a concrete footer specification, which pairs with B2's finding that the
  presence of company and policy pages is itself a trust signal.
- Claim 11 is the mockup problem stated a fourth time, and stated most sharply: an image
  that provokes neither "I love it" nor "not for me" is not working. A floating garment on
  a blank background provokes neither.
- Claim 10 is directly checkable. BRAND.md mentions slider images in the assets folder,
  so a homepage carousel may well exist.
