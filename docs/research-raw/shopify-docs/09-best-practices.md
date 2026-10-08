# 09. Best practices: performance, accessibility, CSS/JS scoping, theme editor JS, Theme Store

## Images
https://shopify.dev/docs/storefronts/themes/best-practices/performance/use-filter-chains
> "Responsive images: Automatically generates a srcset. The candidate widths start from the defaults 352, 832, 1200, and 1920. If you pass width to image_url, then that width is added to the set ... If you pass widths to image_tag, then your list replaces the defaults entirely."
> "width and height attributes: Automatically generates correct dimensions based on aspect ratio, preventing CLS"
> "Focal point positioning: Automatically applies an object-position style if a focal point is set" ; "Format negotiation: The CDN automatically serves WebP or AVIF" ; "Use the preload: true parameter to trigger HTTP 103 Early Hints"
> Anti-pattern: `<img src="{{ product.featured_image.src | replace: '.jpg', '_x800.jpg' }}" />` ; Recommended: `{{ product.featured_image | image_url: width: 800 | image_tag }}`
https://shopify.dev/docs/storefronts/themes/best-practices/performance/use-responsive-images
> `{{ product.featured_image | image_url: width: 1000 | image_tag: widths: '400, 600, 800, 1000', sizes: '(min-width: 1000px) 900px, calc(100vw - 2rem)' }}` ; "Four to six widths are usually sufficient." ; "No sizes attribute: The browser defaults to downloading the largest image."
https://shopify.dev/docs/storefronts/themes/best-practices/performance/never-lazy-load-lcp-image
> forloop pattern: `if forloop.index <= 4 assign image_loading = 'eager' else assign image_loading = 'lazy'` ; "Always provide an explicit sizes attribute for images visible in the initial viewport"
https://shopify.dev/docs/storefronts/themes/best-practices/performance/set-fetchpriority-high-on-lcp-image (title: "Mark the LCP image with fetchpriority="high""; references image_tag fetchpriority parameter and section.index for position-aware loading)
https://shopify.dev/docs/api/liquid/filters/image_tag : "This filter automatically applies a focal point to the image using the object-position CSS style"

## JavaScript
https://shopify.dev/docs/storefronts/themes/best-practices/performance
> "The goal is to load only what's needed, only when it's needed: defer non-critical scripts, import modules on interaction instead of at page load, and avoid heavyweight frameworks when Liquid and CSS can do the same job."
ParserBlockingScript check: "Use the defer or async attribute." RemoteAsset: "Self-host on the Shopify CDN using the asset_url filter."

## {% stylesheet %} / {% javascript %}
https://shopify.dev/docs/storefronts/themes/best-practices/javascript-and-stylesheet-tags
> "You can bundle JavaScript and stylesheet assets with section, block and, snippet files"
> "Caution: Liquid isn't rendered in {% javascript %} or {% stylesheet %} tags."
> "Caution: Each file can only have one {% javascript %} tag." / "Each file can only have one {% stylesheet %} tag."
> JS: "Shopify concatenates the content from {% javascript %} tags across all section, block and snippet files into one file per file type: sections: scripts.js blocks: block-scripts.js snippets: snippet-scripts.js ... asynchronously loaded through a <script> tag with the defer attribute. The content from each {% javascript %} tag is wrapped in a self-executing anonymous function"
> "Bundled assets are only injected once for each section, block or snippet file, not for each instance of that file. If you need instance-specific JavaScript, then add data attributes to your section markup"
> CSS: "Shopify collects the content from {% stylesheet %} tags across sections, blocks, and snippets into a single styles.css file ... Shopify subsets this CSS so that each page only loads the styles from files in its render tree" ; "If you need instance-specific CSS, then use an inline <style> tag."
Section wrapper id: `<div id="shopify-section-[id]" class="shopify-section">` (section-schema page). NOT CONFIRMED: a specific shopify.dev passage prescribing `#shopify-section-{{ section.id }}` CSS scoping; the inline-style guidance above is the confirmed rule.

## Theme editor integration
https://shopify.dev/docs/storefronts/themes/best-practices/editor/integrate-sections-and-blocks
> "When users customize sections and blocks through the theme editor, their HTML is dynamically added, removed, or re-rendered directly onto the existing DOM, without reloading the entire page. However, any associated JavaScript that runs when the page loads won't run again."
> "blocks need to have the attribute added manually using the shopify_attributes property of the block object."
> "The theme editor emits section and block JavaScript events that bubble, and are not cancellable."
Events: shopify:inspector:activate, shopify:inspector:deactivate, shopify:section:load ("Re-execute any JavaScript needed for the section to work"), shopify:section:unload ("Clean up any event listeners, variables, etc."), shopify:section:select, shopify:section:deselect, shopify:section:reorder, shopify:block:select (detail {blockId, sectionId, load}), shopify:block:deselect.
> Liquid: `{% if request.design_mode %}` ; JS: "the global variable Shopify.designMode will return true if you're in the theme editor, and undefined if not."

## Accessibility
https://shopify.dev/docs/storefronts/themes/best-practices/accessibility
> "Text that is less than 24 pixels (regular) or 18.5 pixels (bold) has a contrast ratio of 4.5:1 ... Icons have a contrast ratio of 3.0:1"
> "The keyboard focus order must match the DOM order." ; "Your theme doesn't rely on a mouse hover action" ; "Your themes uses no tabindex attributes values other than 0 or -1 and no autofocus attribute." ; "The viewport zoom is enabled." ; "Content that plays automatically in a slideshow can be paused or stopped."
https://shopify.dev/docs/storefronts/themes/store/requirements (Theme Store, section 12)
> "All parts of a page must be keyboard accessible ... focusable elements must feature a visible focus state. All images require the alt attribute. Themes must use image.alt or image_url | image_tag: alt: string for product images. Form inputs must have a unique ID, and labels with for attributes ... Themes must be built with valid HTML ... The size of the touch target for pointer inputs must be at least 24 by 24 CSS pixels."

## Theme Store requirements (useful as a quality bar)
https://shopify.dev/docs/storefronts/themes/store/requirements
> "Themes must have a minimum average Lighthouse performance score of 60 across the theme's product, collection, and home page, for both desktop and mobile." ; "minimum average Lighthouse accessibility score of 90"
> "Themes must support app blocks (blocks of type @app) in the main product section and featured product section." ; "Add a Custom Liquid block anywhere you'd consider adding an app block"
> "14. Settings ... Avoid unnecessarily deep nesting of blocks or complicated configuration structures"
