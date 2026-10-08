Source URL: https://shopify.dev/docs/api/liquid/tags/stylesheet
Fetched: 2026-10-03 via curl https://shopify.dev/docs/api/liquid/tags/stylesheet.md (HTTP 200, markdown)

---
title: 'Liquid tags: stylesheet'
description: >-
  CSS styles included in
  [section](/docs/storefronts/themes/architecture/sections),
  [block](/docs/storefronts/themes/architecture/blocks), and
  [snippet](/docs/storefronts/themes/architecture/snippets) files.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/tags/stylesheet'
  md: 'https://shopify.dev/docs/api/liquid/tags/stylesheet.md'
api_name: liquid
---

# stylesheet

CSS styles included in [section](https://shopify.dev/docs/storefronts/themes/architecture/sections), [block](https://shopify.dev/docs/storefronts/themes/architecture/blocks), and [snippet](https://shopify.dev/docs/storefronts/themes/architecture/snippets) files.

Each section, block or snippet can have only one `{% stylesheet %}` tag.

To learn more about how CSS that's defined between the `stylesheet` tags is loaded and run, refer to the documentation for [stylesheet tags](https://shopify.dev/docs/storefronts/themes/best-practices/javascript-and-stylesheet-tags#stylesheet).

***

**Caution:** Liquid isn\&#39;t rendered inside of \<code>{% stylesheet %}\</code> tags. Including Liquid code can cause syntax errors.

***

## Syntax

```oobleckTag
{% stylesheet %}
  css_styles
{% endstylesheet %}
```

### css\_styles

The CSS styles for the section, block or snippet.
