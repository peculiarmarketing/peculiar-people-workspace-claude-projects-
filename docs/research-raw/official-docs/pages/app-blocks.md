Source URL: https://shopify.dev/docs/storefronts/themes/architecture/blocks/app-blocks
Fetched: 2026-10-03 via curl https://shopify.dev/docs/storefronts/themes/architecture/blocks/app-blocks.md (HTTP 200, markdown)

---
title: App blocks for themes
description: Learn how to support app blocks in your theme sections and theme blocks.
source_url:
  html: 'https://shopify.dev/docs/storefronts/themes/architecture/blocks/app-blocks'
  md: >-
    https://shopify.dev/docs/storefronts/themes/architecture/blocks/app-blocks.md
api_name: liquid
---

# App blocks for themes

If your section is part of a [JSON template](https://shopify.dev/docs/storefronts/themes/architecture/templates/json-templates), then you should support blocks of type `@app`. These blocks enable app developers to create blocks for merchants to add app content to their theme without having to directly edit theme code. You can build app blocks using [theme app extensions](https://shopify.dev/docs/apps/build/online-store/theme-app-extensions).

**Note:**

Blocks of type `@app` aren't supported in [statically rendered sections](https://shopify.dev/docs/storefronts/themes/architecture/sections#statically-render-a-section).

In the theme editor, merchants can choose to add app blocks to existing sections, or in a new section.

When merchants choose to add the app to a new section, Shopify automatically wraps the app block in a [wrapper section](#app-block-wrapper) called `Apps`. You can customize this wrapper section by your own `apps.liquid` section.

To add support for app blocks to your sections and theme blocks, you need take the following steps:

* [Add support for app blocks to the schema](#supporting-app-blocks)
* [Render the block content](#render-app-blocks)
* [Ensure that you have valid section settings](#app-blocks-and-section-settings)

Refer to Dawn's [main product section](https://github.com/Shopify/dawn/blob/main/sections/main-product.liquid) for an example implementation of an existing theme section that opts-in to accepting app blocks.

**Tip:**

For framework information about app blocks, including the valid schema for app blocks, refer to the [theme app extensions framework](https://shopify.dev/docs/apps/build/online-store/theme-app-extensions/configuration) documentation.

***

## Supporting app blocks

To allow merchants to add app blocks to a [section](https://shopify.dev/docs/storefronts/themes/architecture/sections) or a [theme block](https://shopify.dev/docs/storefronts/themes/architecture/blocks/theme-blocks), you need to include a generic block of type `@app` in the section or block schema.

For example:

```json
"blocks": [
  {
    "type": "@app"
  }
]
```

**Caution:**

Blocks of type `@app` don't accept the `limit` parameter. Including this will result in an error.

***

## Render app blocks

To render app blocks, the theme block must use the `{% content_for 'blocks' %}` Liquid tag. This tag handles block rendering, including app blocks.

For example:

```liquid
<div className="group">
  {% content_for 'blocks' %}
</div>
```

### Render app blocks alongside section-defined blocks

To render an app block alongside [section-defined blocks](https://shopify.dev/docs/storefronts/themes/architecture/blocks/section-blocks), you need to check for the appropriate type, and use the following code:

```liquid
{% render block %}
```

For example:

```liquid
{% for block in section.blocks %}
  {% case block.type %}
    {% when '@app' %}
      {% render block %}
    ...
  {% endcase %}
{% endfor %}
```

***

## App blocks and section settings

To prevent ambiguity with [autofill settings](https://shopify.dev/docs/apps/build/online-store/theme-app-extensions/configuration#autofill), sections that support app blocks can include only one resource setting of each type as a section setting. For example, a section might include only one product setting and only one collection setting.

***

## App block wrapper

Merchants can add app blocks to a page in the following ways:

* As a block within the confines of the section that's rendering the block
* In a similar manner to sections, giving them the full width of the page to render content

Because app blocks aren't sections themselves, Shopify wraps these top-level app blocks in a platform-generated `apps.liquid` wrapper section by default. However, you can override this default wrapper section by creating your own.

### Shopify wrapper logic

Shopify determines which wrapper to use for these top-level app blocks based on the following logic:

#### Theme-provided `apps.liquid` section

* If your theme includes a section file named `apps.liquid`, Shopify uses this section to wrap any top-level app block added by the merchant.
* This provides theme developers specific control over how only app blocks are rendered when added directly to a template.
* The `apps.liquid` section schema needs to support blocks of type `@app` and must include a preset. If either of these is missing, then an `Apps not supported` or `Apps section is invalid` error is returned in the theme editor and merchants aren't able to use the section.

#### Theme-provided `_blocks.liquid` section

* If `apps.liquid` does not exist, Shopify looks for a section file named `_blocks.liquid`.
* This section acts as a more generic wrapper, designed to handle both `@app` blocks and `@theme` blocks when added directly to a template.
* The `_blocks.liquid` section schema needs to support block types `@theme` and `@app`, and must include a preset. If either of these is missing, then an error is returned in the theme editor and merchants aren't able to use the section

#### Platform-generated `apps.liquid` section

* If neither `apps.liquid` nor `_blocks.liquid` exists in the theme, Shopify falls back to using a default, platform-generated `apps.liquid` wrapper to render the top-level app block.

### App Wrapper Examples

**Caution:**

The `apps.liquid` section schema can't contain the `templates` schema attribute. This also includes the `templates` attribute within the `enabled_on/disabled_on` schema attributes. It's expected that the `apps.liquid` section is available on all templates.

For example:

## /sections/apps.liquid

```liquid
{% for block in section.blocks %}
  {% render block %}
{% endfor %}


{% schema %}
  {
    "name": "App wrapper",
    "settings": [],
    "blocks": [
      {
        "type": "@app"
      }
    ],
    "presets": [
      {
        "name": "App wrapper"
      }
    ]
  }
{% endschema %}
```

To enable merchants to control how the app looks inside of an app section, you can add a setting that lets merchants add margins around the app blocks. This helps make the app section margins consistent with your theme's layout.

## /sections/apps.liquid

```liquid
<div className="{% if section.settings.include_padding %}padded{% endif %}">
  {% for block in section.blocks %}
    {% render block %}
  {% endfor %}
</div>


{% schema %}
  {
    "name": "App wrapper",
    "settings": [
      {
        "type": "checkbox",
        "id": "include_padding",
        "default": true,
        "label": "Make section margins the same as theme"
      }
    ],
    "blocks": [
      {
        "type": "@app"
      }
    ],
    "presets": [
      {
        "name": "App wrapper"
      }
    ]
  }
{% endschema %}
```

**Note:**

The `apps.liquid` section isn't a standard theme section. It can't be manually rendered, meaning you can't include it with `{% section 'apps' %}`, and it won't show up in the theme editor for merchants to add to pages.

***
