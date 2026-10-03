Source URL: https://shopify.dev/docs/storefronts/themes/architecture/blocks/ai-generated-theme-blocks
Fetched: 2026-10-03 via curl https://shopify.dev/docs/storefronts/themes/architecture/blocks/ai-generated-theme-blocks.md (HTTP 200, markdown)

---
title: AI generated theme blocks
description: Learn how AI generated theme blocks interact in your theme
source_url:
  html: >-
    https://shopify.dev/docs/storefronts/themes/architecture/blocks/ai-generated-theme-blocks
  md: >-
    https://shopify.dev/docs/storefronts/themes/architecture/blocks/ai-generated-theme-blocks.md
api_name: liquid
---

# AI generated theme blocks

In the theme editor, merchants can generate theme blocks in existing sections that support theme blocks. In order for theme developers to create themes that enable merchants to use this feature effectively, there are a few key concepts to understand.

***

## Theme blocks

To make it possible for a section to accept AI generated blocks, it must accept [theme blocks](https://shopify.dev/docs/storefronts/themes/architecture/blocks/theme-blocks). To accept all theme blocks in a section, add the type `@theme` to the [blocks attribute](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema#blocks) of the [schema](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema) of that section.

***

## Wrapper Section

Generated blocks aren't sections themselves. Therefore Shopify wraps these generated blocks in a platform-generated section by default such as when merchants choose to use [Sidekick](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/sidekick) to generate a block in a new section.

Shopify automatically wraps the generated block in a wrapper section called `_blocks.liquid`. You can override and customize this wrapper section by adding your own `_blocks.liquid` section to your theme.

**Note:**

The `_blocks.liquid section` isn't a standard theme section. It can't be manually rendered, meaning you can't include it with `{% section '_blocks' %}`, and it won't show up in the theme editor for merchants to add to pages.

### Custom `_blocks.liquid` section

The `_blocks.liquid` section schema needs the following to be true:

1. Define `@theme` and `@app` as block types
2. Define `presets`
3. Define `{% content_for blocks %}`
4. Does not define the `templates` attribute, including within `disabled_on` and `enabled_on`

If any of these cases is not met, then an error is returned in the code editor and merchants aren't able to use the section.

Additionally, you can enable merchants to control how the block looks inside the \_blocks.liquid wrapper using settings. This ensures the wrapper is visually consistent with your theme's layout.

## \_blocks.liquid

```liquid
{% content_for 'blocks' %}


{% schema %}
{
  "name": "Section",
  "blocks": [{ "type": "@theme" }, { "type": "@app" }],
  "settings": [
    {
      "type": "range",
      "id": "section-margin",
      "label": "",
      "min": 0,
      "max": 50,
      "default": 0,
      "unit": "px"
    },
  ],
  "presets": [
    {
      "name": "Section"
    }
  ]
}
{% endschema %}
```

***
