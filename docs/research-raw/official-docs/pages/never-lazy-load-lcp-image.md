Source URL: https://shopify.dev/docs/storefronts/themes/best-practices/performance/never-lazy-load-lcp-image
Fetched: 2026-10-03 via curl https://shopify.dev/docs/storefronts/themes/best-practices/performance/never-lazy-load-lcp-image.md (HTTP 200, markdown)

---
title: Never lazy-load the LCP image
description: >-
  Eagerly load images visible in the initial viewport. Never apply
  `loading="lazy"` or use a JavaScript-based lazy loader on the primary LCP
  target or other critical image in the initial viewport.
source_url:
  html: >-
    https://shopify.dev/docs/storefronts/themes/best-practices/performance/never-lazy-load-lcp-image
  md: >-
    https://shopify.dev/docs/storefronts/themes/best-practices/performance/never-lazy-load-lcp-image.md
api_name: liquid
---

# Never lazy-load the LCP image

Eagerly load images visible in the initial viewport. Never apply `loading="lazy"` or use a JavaScript-based lazy loader on the primary LCP target or other critical image in the initial viewport.

***

## Why

Lazy-loading the LCP image is one of the most common and damaging performance anti-patterns in Shopify themes. Server-side rendering with `image_tag` gives the browser maximum lead time on the LCP image, but only when the image is loaded eagerly.

When Liquid renders an `img` tag with a `src` attribute into the HTML, the browser's preload scanner discovers the image URL while parsing the HTML, before any CSS has been parsed, any JavaScript has run, or layout has begun. This gives the browser a head start on downloading the image as early as possible in the page load.

There are two related anti-patterns. First, `loading="lazy"` on the LCP candidate deprioritizes it and defers the download until after the browser processes a hidden `IntersectionObserver` event. Second, JavaScript lazy loading libraries like lazysizes replace the `src` attribute with a non-standard `data-src`, which hides the URL from the preload scanner entirely until JavaScript executes. Both practices are common, but they negate the benefits of the preload scanner and add latency.

***

## How

### Remove `loading="lazy"` from the LCP image

Change `loading="lazy"` to `loading="eager"`, or remove the attribute. Eager loading is the default browser behavior.

```liquid
{{ section.settings.image | image_url: width: 1000 | image_tag: loading: 'eager' }}
```

### Remove Java​Script lazy loading libraries

Libraries like lazysizes, lozad, and vanilla-lazyload replace `src` with `data-src`, hiding the image URL from the preload scanner until JavaScript executes.

To migrate:

1. Replace `data-src` with `src` on all images.
2. Add `loading="lazy"` to images outside the initial viewport.
3. Remove the library script tag.

### Use `section.index` for conditional loading

The `image_tag` filter automatically applies `loading="eager"` for sections 1 through 3, and `loading="lazy"` for sections 4 and later. It also applies `loading="eager"` whenever `section.index0` is `nil`, which is the case in the online store editor, in static sections, and in the [Section Rendering API](https://shopify.dev/docs/api/section-rendering). Don't set the `loading` attribute when relying on this default.

When you override the default with [`section.index`](https://shopify.dev/docs/api/liquid/objects/section#section-index), match that `nil` handling. Comparisons against `nil` are falsey in Liquid, so `{% if section.index <= 3 %}` sends the LCP image to the `else` branch in exactly the contexts where the built-in default keeps it eager. Test the lazy case as a positive `section.index > 3` comparison instead, and let everything else, including `nil`, fall through to eager. For the full explanation, refer to [Load above-the-fold and below-the-fold sections differently with `section.index`](https://shopify.dev/docs/storefronts/themes/best-practices/performance/use-section-index):

```liquid
{% if section.index == 1 %}
  {%- comment -%} First section: eager, and the LCP candidate {%- endcomment -%}
  {{ image
    | image_url: width: 1000
    | image_tag:
        loading: 'eager',
        fetchpriority: 'high'
  }}
{% elsif section.index > 3 %}
  {%- comment -%} Sections 4 and later {%- endcomment -%}
  {{ image
    | image_url: width: 1000
    | image_tag: loading: 'lazy'
  }}
{% else %}
  {%- comment -%} Sections 2 and 3, and any context where section.index is nil {%- endcomment -%}
  {{ image
    | image_url: width: 1000
    | image_tag: loading: 'eager'
  }}
{% endif %}
```

### Use `forloop.index` for image-dense sections

A collection section might render up to 50 products at a time, all within the first section. `section.index` alone isn't sufficient here, because only the first few images are visible in the viewport and are LCP candidates. Use `forloop.index` to enable eager loading for just those cards, and leave the rest to be lazy loaded:

```liquid
{% for product in collection.products %}
  {%- liquid
    if forloop.index <= 4
      assign image_loading = 'eager'
    else
      assign image_loading = 'lazy'
    endif
  -%}
  {{ product.featured_image
    | image_url: width: 400
    | image_tag:
        loading: image_loading,
        widths: '200, 300, 400',
        sizes: '(min-width: 1200px) calc(25vw - 2rem), (min-width: 768px) calc(33vw - 2rem), calc(50vw - 2rem)'
  }}
{% endfor %}
```

### Avoid auto-sizes on LCP images

Calculating `sizes` with JavaScript, as some lazy loading libraries do, delays image download because the browser can't select the correct source until after JavaScript runs. Always provide an explicit `sizes` attribute for images visible in the initial viewport:

```liquid
{{ image
  | image_url: width: 1000
  | image_tag:
      loading: 'eager',
      widths: '400, 600, 800, 1000',
      sizes: '(min-width: 1000px) 900px, calc(100vw - 2rem)'
}}
```

***

## Examples

### Example 1.​Hero or banner sections

```liquid
{%- comment -%} Before: always lazy loads, even when this section is at the top of the page {%- endcomment -%}
{{ section.settings.image
  | image_url: width: 1600
  | image_tag:
      loading: 'lazy',
      widths: '600, 900, 1200, 1600',
      sizes: '100vw'
}}


{%- comment -%} After: section.index determines loading at render time, and nil stays eager {%- endcomment -%}
{%- liquid
  assign hero_loading = 'eager'
  assign hero_priority = 'auto'
  if section.index == 1
    assign hero_priority = 'high'
  elsif section.index > 3
    assign hero_loading = 'lazy'
  endif
-%}
{{ section.settings.image
  | image_url: width: 1600
  | image_tag:
      loading: hero_loading,
      fetchpriority: hero_priority,
      widths: '600, 900, 1200, 1600',
      sizes: '100vw'
}}
```

### Example 2.​Migrate from lazysizes

Before, with lazysizes:

```html
<script src="{{ 'lazysizes.min.js' | asset_url }}" async></script>
<img
  data-src="{{ section.settings.image | image_url: width: 1200 }}"
  data-srcset="{{ section.settings.image | image_url: width: 400 }} 400w,
               {{ section.settings.image | image_url: width: 800 }} 800w,
               {{ section.settings.image | image_url: width: 1200 }} 1200w"
  data-sizes="auto"
  class="lazyload"
  alt="{{ section.settings.image.alt | escape }}"
/>
```

After, with `image_tag`. Remove the script tag from your layout file and provide an explicit `sizes` attribute, because you can no longer use `data-sizes="auto"`:

```liquid
{{ section.settings.image
  | image_url: width: 1200
  | image_tag:
      loading: 'eager',
      fetchpriority: 'high',
      widths: '400, 800, 1200',
      sizes: '(min-width: 1000px) 900px, calc(100vw - 2rem)'
}}
```

### Example 3. Product card grid with `forloop.index`

```liquid
{% for product in collection.products %}
  {%- comment -%} Eagerly load only the first few items {%- endcomment -%}
  {%- liquid
    if forloop.index <= 4
      assign image_loading = 'eager'
    else
      assign image_loading = 'lazy'
    endif
  -%}
  {{ product.featured_image
    | image_url: width: 400
    | image_tag:
        loading: image_loading,
        widths: '200, 300, 400',
        sizes: '(min-width: 1200px) calc(25vw - 2rem), (min-width: 768px) calc(33vw - 2rem), calc(50vw - 2rem)'
  }}
{% endfor %}
```

***

## Testing

* Use the **Insights** tab in the **Performance** panel to identify whether the LCP image is being lazy loaded.
* Use the **Network** panel to check when the LCP image request starts. It should appear early in the waterfall, discovered by the preload scanner, not after JavaScript executes.
* Compare **Performance** panel runs with `loading="lazy"` and `loading="eager"` on the LCP image to see the LCP difference.

***

## References

* [`forloop.index`](https://shopify.dev/docs/api/liquid/objects/forloop#forloop-index)
* [`section.index`](https://shopify.dev/docs/api/liquid/objects/section#section-index)
* [`image_tag`](https://shopify.dev/docs/api/liquid/filters/image_tag) filter
* [Lazy load images for performance](https://performance.shopify.com/blogs/blog/lazy-load-images-for-performance)
* [How layout position impacts three big web performance levers](https://performance.shopify.com/blogs/blog/how-layout-position-impacts-three-big-web-performance-levers)
* [Announcing new Liquid features for better web performance](https://performance.shopify.com/blogs/blog/announcing-new-liquid-features-for-better-web-performance)
* [Use `section.index` for position-aware loading](https://shopify.dev/docs/storefronts/themes/best-practices/performance/use-section-index)
* [Mark the LCP image with `fetchpriority="high"`](https://shopify.dev/docs/storefronts/themes/best-practices/performance/set-fetchpriority-high-on-lcp-image)
* [Prevent image layout shift](https://shopify.dev/docs/storefronts/themes/best-practices/performance/prevent-image-layout-shift)
* [Use responsive images](https://shopify.dev/docs/storefronts/themes/best-practices/performance/use-responsive-images)

***
