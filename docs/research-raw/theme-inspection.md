# Live theme inspection (read only), 2026-10-03

Tool: Shopify connector `graphql_query` (Admin API, read only). No write calls were made.

## Themes on the store
| Name | Role | ID |
|---|---|---|
| Claude code original | MAIN (live) | gid://shopify/OnlineStoreTheme/193770258804 |
| Claude Code V2 | UNPUBLISHED | gid://shopify/OnlineStoreTheme/194242150772 |
| Original | UNPUBLISHED | gid://shopify/OnlineStoreTheme/192015073652 |

## theme_info (config/settings_schema.json of the MAIN theme)
```
"theme_name": "Shrine PRO",
"theme_version": "1.9.0",
"theme_author": "Shrine",
"theme_documentation_url": "https://app.shrine.io/customer/help-center"
```
Local files: no full theme is in the repos. `temple-product-generator/theme/` holds only Peculiar People's own custom files (pp-* sections, assets, snippets, templates/index.json).

## Structure found
- 89 files in `sections/` on the live theme, 103 files in `blocks/` (Shrine uses theme blocks heavily).
- No `.theme-check.yml` in the live theme.
- Shrine already ships sections that overlap common "custom section" requests: collapsible-content, content-tabs, bundle-deals, testimonials, comparison-table, comparison-slider, featured-product, image-with-text, multicolumn, multirow, shoppable-image, trustpilot-reviews, tiktok-videos, insta-stories, sticky-cta, related-products, custom-liquid, custom-columns-new (V2). Blocks include product_sizing-chart, product_tabs, collapsible-row, product_bundle-offer, product_complementary, product_upsell-block--product-info, reviews, review-avatars.
- `sections/main-product.liquid` renders two STATIC theme blocks: `{% content_for 'block', type: 'main-product_gallery', id: 'Gallery' %}` and `{% content_for 'block', type: 'main-product_details', id: 'Details' %}`. Its schema `blocks` array is empty and it has no presets.
- `blocks/main-product_details.liquid` renders `{% content_for 'blocks' %}` inside a `<product-info>` custom element with `data-section="{{ section.id }}"`; the product form id is `'product-form-' | append: section.id`. Its schema accepts an explicit list of 49 block types beginning with `@app` (so app blocks such as Kiwi Size Chart and Easify can be placed there). It does NOT accept `@theme`, so a new custom theme block or a Shopify Magic generated block cannot be added to the product info column until its type is added to this list (which means editing a Shrine file).
- `blocks/container--product.liquid` accepts `@app` and a fixed list; no `@theme`.
- `sections/apps.liquid` accepts `@app` and has presets (a general place to drop app blocks).
- `sections/custom-liquid.liquid` exists with presets (Shopify's standard "Custom Liquid" section).
- Shrine's own block code uses `visible_if`, scoped selectors like `#ContentContainer-{{ block.id }}`, inline `<style>` with Liquid, and `!important` in places. Shrine's block schemas use plain English labels in some files and `t:` keys in others.
- The live theme does NOT contain `pp-garment-anatomy`, `pp-temple-marquee` or `pp-founder`; those are on the unpublished "Claude Code V2" theme per temple-product-generator/theme/README.md.
