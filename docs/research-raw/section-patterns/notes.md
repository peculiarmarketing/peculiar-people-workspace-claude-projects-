# Raw notes: custom Shopify sections research (2026-10-03)

## Method and big caveat
- WebFetch was EGRESS_BLOCKED for every domain tried: baymard.com, styleimprint.app, easifyapps.com, apps.shopify.com, help.shopify.com. Shell egress blocked too.
- So every item below comes from WebSearch result summaries (the search tool's own summary of the page). None of it is verbatim page text that I read myself. Treat all as PARAPHRASED (search summary). Page dates were mostly not visible; "date unknown" means exactly that.
- Nothing was installed.

## PART 1 Section patterns

### Accordions / collapsible detail blocks
- baymard.com/blog/avoid-horizontal-tabs (Baymard, official research; date unknown, Baymard tweet about it dates to 2018 so original likely OLDER THAN 12 MONTHS, page may be updated):
  - "Vertically Collapsed Sections" and "Expanded Sections" outperform "Horizontal Tabs".
  - 27% of users in a Sephora study never discovered content in unopened horizontal tabs.
  - Horizontal tabs still used by 29% of sites (tweet said 28%).
  - Collapsed sections: less likely to be overlooked than tabs, page less intimidating, headers scannable.
- Search summary also: hiding basic item/order details in collapsed sections performed as poorly as not providing them (attributed to Baymard; exact page not confirmed).
- styleimprint.app (practitioner/vendor blog, 2026, unverified): claims Baymard found 90% of apparel sites fail to let shoppers assess appearance, size or fit; deciding facts (fabric, fit, care, model, size) should be visible blocks near top, not buried in collapsed tabs.
- clariola.com (practitioner, 2026): cites Baymard 2026 benchmark: 52% desktop, 62% mobile, 64% apps have "mediocre or worse" product pages.
- shopify.com/blog/accordion-ui-design (Shopify blog, 2026 in title): pros/cons; a cited "bounce rate 73% to 51%" anecdote and "23% higher abandonment" when pricing hidden; sourcing of these numbers unclear (search summary may mix pages). Unverified.
- Shrine has built-in Collapsible content section (Pro has "Advanced" version) per shrine.io features pages.
- Delivery: built-in theme feature (Shrine) covers it.

### Collection filters
- baymard.com/blog/promoting-product-filters: 61% of sites don't promote filters.
- baymard filtering summary: 51% don't provide 5 essential filter types; 28% don't show applied-filters overview; 14% don't allow multi-select.
- Apparel: price, size, color most popular; size filter near top and expanded prompted 90% of participants to filter by size first (baymard.com/blog/apparel-put-size-filter-near-top-and-expand-for-sidebar-filtering).
- Mediocre product list usability: 67-90% abandonment vs 17-33% on optimized (older Baymard stat, OLDER THAN 12 MONTHS likely).
- Delivery: Shopify Search & Discovery app (free, Shopify) + OS 2.0 theme filters. help.shopify.com search-and-discovery-filters: filters on price, availability, type, vendor, tags, variant options, metafields; OS 2.0 only; collections > 5,000 products don't show filters.

### Reviews / UGC / photo walls
- baymard.com/blog/allow-reviewers-to-upload-images: 34% of sites don't allow image upload with review; image reviews well received in testing.
- baymard.com/blog/allow-navigation-across-reviews-from-reviewer-images: up to 95% of users consult reviews; 63% of sites don't let users navigate reviews via reviewer images.
- baymard.com/blog/integrate-social-media-visuals-on-product-page: 67% of product pages don't feature buyer social media images/videos.
- baymard 2026 apparel quant insights: 33% of sites don't aggregate "fit" info from reviews.
- Spiegel Research Center (Northwestern, 2017, OLDER THAN 12 MONTHS): 5 reviews -> 270% purchase likelihood vs 0; low-price +190%, high-price +380%; peak at 4.0-4.7 stars.
- storecensus.com, easyappsecom.com, eevy.ai (2026, vendor/practitioner aggregators, unverified): apparel UGC lifts 18-31%; UGC gallery +22% median; photo reviews 2.6x; photo pages +30-45%. Primary sources not shown.
- Delivery: review app (app block), not a hand-built theme section.

### Size guide embeds
- baymard.com/research-articles/apparel-size-information: size guide link must be adjacent to size selector or overlooked; tailor per product type; 82-83% of apparel sites insufficient sizing info; 43% provide no usable sizing info; metric + imperial.
- Size Finder recommended alongside charts (baymard size-finder examples).
- Practitioner claim (aggregator, unverified): apparel stores with sizing signals see ~22% CVR lift.
- Delivery: Kiwi app block (already installed).

### Brand story
- No rigorous quantified evidence found. Orbit Media (practitioner): top pages 1/3 to 1/2 "evidence". Baymard summary: users want supplementary info like brand history and manufacturing ethics (page not identified).
- Delivery: built-in theme sections (image with text / rich text) suffice.

### Bundles / FBT / upsells
- baymard.com/blog/product-recommendations-cart: 52% of desktop sites don't do enough for cart cross-sell relevance.
- baymard.com/blog/product-page-suggestions-information: 68% of desktop sites missing one or more list-item attributes in cross-sells.
- Baymard labels: "Frequently Bought Together" for co-purchase cross-sells, "Complete the Look" for apparel coordination.
- AOV lift 15-35% / 20-35% for orders with bundles: cartylabs.com, easyappsecom, etc. (2026 vendor blogs, unverified, no primary data).
- Fashion & apparel median AOV $73 (2025) -> $80 (2026): eevy.ai (vendor, unverified).
- Shopify native: Complementary products via Search & Discovery (manual pairing) + theme block; Shopify Bundles app (free, fixed bundles only, no mix-match / volume discounts per fudge.ai 2026).
- Shrine 1.9.0 notes mention quantity breaks and cart upsells built in.

## PART 2 Section libraries
- Section Store: Theme Sections (apps.shopify.com/section-factory): free install, most sections $0-$9 one-time, optional Section Store Plus $15/mo; 700-730+ sections; 4.9 from 2,300+ reviews; OS 2.0 compatible. Some reviews complain of price increases / push to $15/mo.
  - Installed sections use "ss-" prefix; claimed to persist into updated theme's sections folder (search summary, source unclear).
- Section Library: AI Sections: free 8 credits/mo; $9 (25), $19 (55), $29 (90).
- Flexi Sections: $5/$10/$30 per mo by Shopify plan.
- Pent Library: free up to 2 sections; $19 / $39 mo.
- Puco Sections: free 30+ sections; Pro $19/mo.
- AppSections (docs.appsections.com): clean uninstall removes all sections/templates; customizations lost.
- Note: section.store blog comparing apps is written by Section Store itself (vendor bias).
- Custom Liquid section (Shopify built-in in OS 2.0 themes): paste Liquid/HTML/CSS. Limit: 50 KB per liquid setting (shopify.dev theme limits). Max 50 blocks per section.
- Theme app extensions (shopify.dev): app blocks don't edit theme code; removed automatically on uninstall; survive theme updates. Old script-injection apps left "ghost code".

## PART 3 App compatibility
### Easify Product Options
- Developer support email support@tigren.com (so Easify is run by Tigren).
- Injection: App embed ("Product Options" in Theme Customize > App embeds) must be enabled AND saved; plus optional app block "Easify Product Options" in Product information section.
- Position: General Settings has 4 positions: above/below Add To Cart button, above/below (Shopify) product variants. Theme editor app block position overrides General Settings.
- Page builders: paste `<div class="easify-product-options">`.
- Troubleshooting when not visible: may be a theme conflict, multiple product-options apps enabled, or conflict with another app; contact support/live chat.
- Theme switch: must reactivate on new theme.
- Fully compatible with OS 2.0 (search summary).
- Pricing: Free Forever; Pro $9.99; Premium $19.99; Enterprise $99.99/mo; 4.9 stars 2,000+ reviews (inso.codes/search summary; verify).
- Third-party general: apps conflict when both modify add-to-cart button (easyappsecom guide, vendor).
### Kiwi Size Chart & Recommender
- App listing apps.shopify.com/kiwi-sizing. Developer appears as "Staytuned" in third-party listings, not "Kiwi Commerce". Launched 2018; 4.8 stars, ~1,039 reviews; ~42,977 installs (storeleads/taranker).
- Pricing: Free (2 charts, watermark); Premium $6.99/mo; Plus $12.49/mo; Ultimate $24.49/mo.
- Injection: "KiwiSizing" app block in Product information (OS 2.0) / "Kiwi Theme Helper" embed; or Custom Injection via "sizing injection selector" (CSS selector); or "Hijack" method (turn existing button into Kiwi trigger).
- Selectors: avoid ID selectors (Shopify generates per product); use class selectors.
- After theme update app blocks may be removed/overwritten: re-add block. Enable on every product template.
- Variant apps (Swatch King, Bold Options, custom scripts) rebuild variant DOM: chart may disappear, duplicate, jump, or script conflicts. Don't inject inside swatch/radio markup that reloads on variant change or into app-generated variant nodes; don't rely on dynamic IDs/classes.
- Dev docs: window.ks.loadSizing(); window.KiwiSizing liquid snippet data.

## PART 4 Shrine
- Official: shrine.io (Shrine Solutions Ltd, Cyprus). Also shrinetheme.io, shrinethemes.com, help.shrinetheme.com: relationship unclear.
- Etsy / gumroad / nulled forums sell or leak "Shrine Pro 1.9.0"; shrine.io blog warns about nulled copies. License: one store, license key.
- Updates: 1 year free updates; lifetime updates extra. Distribution as ZIP uploaded to Shopify (not via Shopify Theme Store, so no Shopify one-click update).
- Shopify: only Theme Store themes get Shopify's update flow; others contact developer.
- Claim (shrine.io blog, vendor): dedicated custom CSS/JS fields survive updates; settings carry over. Not verified how.
- General Shopify: edits to existing theme files are not carried to new version; separate new files copy across (ed.codes, practitioner).
- Version: 1.9.0 dated July 8, 2025 (OLDER THAN 12 MONTHS) with: custom color scheme per section, Store colors changer section, quantity breaks variant price, compare prices in cart drawer, cart progress bar by quantity, Image block and Rating stars block in Product information, Swatch Pills. Another summary: "Shrine Pro 2.1.0" Dec 11, 2025 with custom product field blocks, sticky ATC with variant picker; a third says latest "Shrine 2.1.0 and Shrine Pro 1.6.1". Version numbering conflicting; unverified.
- Built-ins (shrine.io features, vendor): Before & After slider, comparison tables, Collapsible content (Pro Advanced), content tabs, image/video sliders, FAQ blocks; Pro 44 or 52 sections (conflicting numbers), 49 product info blocks; Custom liquid block in Cart drawer.
