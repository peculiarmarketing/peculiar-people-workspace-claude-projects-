Source URL: https://shopify.dev/docs/storefronts/themes/best-practices/javascript-and-stylesheet-tags
Fetched: 2026-10-03 via curl https://shopify.dev/docs/storefronts/themes/best-practices/javascript-and-stylesheet-tags.md (HTTP 200, markdown)

---
title: JavaScript and stylesheet tags
description: 'Bundling JavaScript and stylesheet assets with sections, blocks and snippets.'
source_url:
  html: >-
    https://shopify.dev/docs/storefronts/themes/best-practices/javascript-and-stylesheet-tags
  md: >-
    https://shopify.dev/docs/storefronts/themes/best-practices/javascript-and-stylesheet-tags.md
api_name: liquid
---

# Java​Script and stylesheet tags

You can bundle JavaScript and stylesheet assets with [`section`](https://shopify.dev/docs/storefronts/themes/architecture/sections), [`block`](https://shopify.dev/docs/storefronts/themes/architecture/blocks) and, [`snippet`](https://shopify.dev/docs/storefronts/themes/architecture/snippets) files using the following Liquid tags:

* [`{% javascript %}`](#javascript)
* [`{% stylesheet %}`](#stylesheet)

Including assets with the relevant files can help you keep the theme modular, making the files portable across different themes and shops without losing their functionality or styling.

If reusability isn't a concern, then you can place the JavaScript or CSS styles that your file needs in your theme's [`assets`](https://shopify.dev/docs/storefronts/themes/architecture#assets) directory and include them using the [`asset_url` filter](https://shopify.dev/docs/api/liquid/filters/asset_url) with either the [`script_tag` filter](https://shopify.dev/docs/api/liquid/filters/script_tag) or [`stylesheet_tag` filter](https://shopify.dev/docs/api/liquid/filters/stylesheet_tag). If an asset has already been included in a parent layout or template, then you don't need to include it again.

**Caution:**

Liquid isn't rendered in `{% javascript %}` or `{% stylesheet %}` tags. Including Liquid code in these tags can cause syntax errors, or prevent styles from being applied to the theme.

***

## javascript

To include JavaScript, use the [`{% javascript %}`](https://shopify.dev/docs/api/liquid/tags/javascript) tag:

```liquid
{% javascript %}
  document.querySelector('.slideshow').slideshow();
{% endjavascript %}
```

**Caution:**

Each file can only have one `{% javascript %}` tag. Having more than one will result in a syntax error when editing your theme code.

Shopify concatenates the content from `{% javascript %}` tags across all section, block and snippet files into one file per file type:

* **sections**: `scripts.js`
* **blocks**: `block-scripts.js`
* **snippets**: `snippet-scripts.js`

These files are then injected into the theme through the `content_for_header` [Liquid object](https://shopify.dev/docs/api/liquid/objects/content_for_header) and asynchronously loaded through a `<script>` tag with the `defer` attribute.

The content from each `{% javascript %}` tag is wrapped in a self-executing anonymous function so that any variables are defined within a closure, and runtime exceptions won't affect other sections.

### Instance specific Java​Script

Bundled assets are only injected once for each section, block or snippet file, not for each instance of that file. If you need instance-specific JavaScript, then add data attributes to your section markup and reference those attributes in your JavaScript. For example:

## /sections/slideshow\.liquid

```liquid
<div className="slideshow-wrapper" data-slide-speed="{{ section.settings.speed }}">
  <!-- slideshow content -->
</div>


{% javascript %}
  var slideshowSpeed = parseInt(document.querySelector('.slideshow-wrapper').dataset.slideSpeed);
{% endjavascript %}
```

***

## stylesheet

The [`{% stylesheet %}`](https://shopify.dev/docs/api/liquid/tags/stylesheet) tag can be used to include CSS styles:

```liquid
<div className="slideshow-wrapper" data-slide-speed="{{ section.settings.speed }}">
  <!-- slideshow content -->
</div>


{% stylesheet %}
.slideshow-wrapper {
  // your styles
}
{% endstylesheet %}
```

**Caution:**

Each file can only have one `{% stylesheet %}` tag. Having more than one will result in a syntax error when editing your theme code.

Shopify collects the content from `{% stylesheet %}` tags across sections, blocks, and snippets into a single `styles.css` file. A link to this generated file is automatically injected into the theme through the `content_for_header` [global Liquid object](https://shopify.dev/docs/api/liquid/objects/content_for_header). To optimize performance, Shopify [subsets this CSS](https://shopify.dev/docs/storefronts/themes/best-practices/performance/stylesheet-subsetting) so that each page only loads the styles from files in its render tree, rather than bundling all `{% stylesheet %}` CSS on every page.

### Instance specific styles

Bundled assets are only injected once for each section, block or snippet file, not for each instance of that file. If you need instance-specific CSS, then use an inline `<style>` tag.

***
