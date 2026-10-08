# Read-only observations of the store theme (2026-10-03)

Method: Shopify MCP connector, Admin GraphQL `theme(id:"gid://shopify/OnlineStoreTheme/194242150772")`
(the unpublished "Claude Code V2" copy), files query, read only. Nothing was written.

- theme_info in config/settings_schema.json: Shrine PRO 1.9.0 by Shrine (same on all 3 themes).
- The theme has a `blocks/` folder with ~50+ theme block files (announcement, atc-button,
  collapsible-row, custom-liquid, main-product_details, main-product_gallery, ...). So Shrine PRO
  1.9.0 uses Shopify theme blocks, not only section blocks.
- `sections/main-product.liquid` schema lists no local block types; its content comes from
  theme blocks `main-product_gallery` and `main-product_details`.
- `blocks/main-product_details.liquid` renders `<product-info id="ProductInfo-{{ section.id }}">`
  and `{% content_for 'blocks' %}`. Its schema accepts: @app, custom-liquid, image,
  json-animation, divider, button, atc-button, heading, text, product_title, rating-stars,
  product_clickable-discount, product_price, product_subscription, product_quantity-selector,
  product_buy-buttons, product_product-variant-picker-block, product_sticky-atc,
  product_description, product_tabs, product_estimated-shipping, product_shipping-checkpoints,
  countdown-timer, product_inventory, collapsible-row, video, slider, container--product,
  media-slider, trustpilot-stars, product_sku, product_share-button, product_popup,
  product_sizing-chart, product_upsell-block--product-info, payment-badges, product_urgency,
  product_emoji-benefits, product_bundle-offer, product_quantity-gifts, product_scroll-buttons,
  review-avatars, icon-with-content, text-with-icon, icon-with-text, product_complementary,
  reviews, product-rating, product_custom-product-field, bestseller-badge.
- templates/product.json, section `main`, Details block order:
  product_title, product_price, product_product-variant-picker-block,
  shopify://apps/easify-options/blocks/easify-product-options/...  (APP BLOCK)
  shopify://apps/kiwi-size-chart-recommender/blocks/kiwiSizing/...  (APP BLOCK)
  product_buy-buttons, product_shipping-checkpoints, 4 x collapsible-row, product_sticky-atc,
  product_description.
  Other sections on the product template: pp-temple-drawing (custom), comparison-slider,
  collapsible-content, related-products, rich-text, contact-form, 3 x `apps` sections.
- `blocks/custom-liquid.liquid` exists (a "Custom Liquid" theme block, category Custom).
- layout/theme.liquid defines CSS custom properties with Dawn-style names, including
  --font-body-family, --font-heading-family, --font-body-scale, --color-base-text,
  --color-base-background-1, --color-base-accent-1, --color-base-solid-button-labels,
  --buttons-radius, --page-width, --spacing-sections-desktop, --spacing-sections-mobile.
  (Observation: the naming matches Dawn's pattern. Whether Shrine is built from Dawn is
  NOT confirmed by any Shrine doc.)
- layout/theme.liquid loads base.css via `stylesheet_tag: preload: true` and secondary.js.
- No .theme-check.yml in the theme.
- Existing custom sections (from temple-product-generator/theme): pp-founder, pp-garment-anatomy,
  pp-temple-marquee, pp-temple-showcase, pp-temple-drawing. Conventions: `pp-` file and class
  prefix, BEM classes (`pp-founder__img`), shared assets/pp-home.css and pp-home.js loaded with
  `defer`, `image_url | image_tag` with widths and sizes, a `presets` entry, reduced-motion
  respected.
