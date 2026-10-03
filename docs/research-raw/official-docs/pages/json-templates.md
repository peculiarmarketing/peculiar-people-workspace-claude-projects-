Source URL: https://shopify.dev/docs/storefronts/themes/architecture/templates/json-templates
Fetched: 2026-10-03 via curl https://shopify.dev/docs/storefronts/themes/architecture/templates/json-templates.md (HTTP 200, markdown)

---
title: JSON templates
description: >-
  Learn how to use JSON templates to build pages with sections that can be
  customized in the theme editor.
source_url:
  html: >-
    https://shopify.dev/docs/storefronts/themes/architecture/templates/json-templates
  md: >-
    https://shopify.dev/docs/storefronts/themes/architecture/templates/json-templates.md
api_name: liquid
---

# JSON templates

JSON templates allow you to control the look and feel of different pages of the online store using [sections](https://shopify.dev/docs/storefronts/themes/architecture/sections).

JSON templates are data files that store a list of sections to be rendered, and their associated settings. Merchants can add, remove, and reorder these sections using the theme editor.

When a page is rendered with a JSON template, the sections are rendered in the order specified by the [order attribute](#schema), with no markup between the sections. JSON templates can render up to 25 sections, and each section can have up to 50 blocks.

***

## Supported features

Although JSON templates differ from Liquid templates in their contents, they are still template files that support the following Shopify theme features:

* All template types, except for [gift\_card](https://shopify.dev/docs/storefronts/themes/architecture/templates/gift-card-liquid), [robots.txt](https://shopify.dev/docs/storefronts/themes/architecture/templates/robots-txt-liquid), [agents.md](https://shopify.dev/docs/storefronts/themes/architecture/templates/agents-md-liquid), [llms.txt](https://shopify.dev/docs/storefronts/themes/architecture/templates/llms-txt-liquid), and [llms-full.txt](https://shopify.dev/docs/storefronts/themes/architecture/templates/llms-full-txt-liquid).

* [Alternate templates](https://shopify.dev/docs/storefronts/themes/architecture/templates/alternate-templates).

  When you build a JSON template, you should also build a section that contains the core functionality for the template. For example, when you're building a [list-collections](https://shopify.dev/docs/storefronts/themes/architecture/templates/list-collections) JSON template, it should reference a section that uses the [collections object](https://shopify.dev/docs/api/liquid/objects/collections).

  A theme can contain up to 1,000 JSON templates. After the limit is reached, you can't create new JSON templates.

***

## Schema

A JSON template accepts only a JSON file with a fixed schema and list of accepted attributes. The root should be an object with the following attributes:

| Attribute | Type | Required | Description |
| - | - | - | - |
| `layout` | String or `false` | No | The filename of the [layout](https://shopify.dev/docs/storefronts/themes/architecture/layouts) to use when rendering the template. For example, specify `"full-width"` to render `layout/full-width.liquid`.The default layout is `theme.liquid`.Use the value `false` to render the template without a layout. Templates without a layout can't be customized in the theme editor. |
| `wrapper` | String | No | The HTML wrapper element for the template's sections. To learn more, refer to [The wrapper property](https://shopify.dev/docs/storefronts/themes/architecture/templates/json-templates#the-wrapper-property). |
| `sections` | Object | Yes | An object that uses section IDs as keys, and section data as values. This attribute needs to contain at least one section.Duplicate IDs within the template aren't allowed.The format of the section data is the same as section data in [settings\_data.json](https://shopify.dev/docs/storefronts/themes/architecture/config/settings-data-json). To learn more, refer to [Section data](https://shopify.dev/docs/storefronts/themes/architecture/templates/json-templates#section-data). JSON templates can render up to 25 sections, and each section can have up to 50 blocks. |
| `order` | Array | Yes | An array of section IDs, listed in the order that they should be rendered. The IDs must exist in the `sections` object. Duplicates are not allowed. |

**Tip:**

Section files must define [presets](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema#presets) in their schema to support being added to JSON templates using the theme editor. Section files without presets should be included in the JSON file manually, and can't be removed using the theme editor.

### Naming JSON templates

The filename must be a valid [theme template type](https://shopify.dev/docs/storefronts/themes/architecture/templates#template-types), with an optional suffix for an alternate template. For example, a product template can be named `product.json` or `product.alternate.json`.

A template can only exist as a JSON or Liquid template, not both. For example, if `product.liquid` already exists, then you can't create `product.json`.

### The wrapper property

The `wrapper` property makes it possible to insert HTML tags around all of the sections in a JSON template. You can use the following HTML tags:

* `<div>`

* `<main>`

* `<section>`

  For example, a JSON file with the following `wrapper` property produces the following output:

## product.json

```json
{
  "wrapper": "div#div_id.div_class[attribute-one=value]",
  "sections": {
    "main": {
      "type": "product"
    }
  },
  "order": [
    "main"
  ]
}
```

## Output

```html
<div id="div_id" className="div_class" attribute-one="value">
    <!-- product.json sections -->
</div>
```

### Section data

The `sections` attribute of JSON templates holds the data for the sections to be rendered by the template. These can be either [theme sections](https://shopify.dev/docs/storefronts/themes/architecture/sections) or [app sections](https://shopify.dev/docs/storefronts/themes/architecture/blocks/app-blocks#app-block-wrapper). You can't share section data across JSON theme templates, so each section must have an ID that's unique within the template.

JSON templates can render up to 25 sections, and each section can have up to 50 blocks.

You can add sections to a template in code, or through the theme editor. The sections that are available to be added to a template in the theme editor might be limited by the [`enabled_on`](https://shopify.dev/docs/themes/architecture/sections/section-schema#enabled_on) or [`disabled_on`](https://shopify.dev/docs/themes/architecture/sections/section-schema#disabled_on) attribute of the section schema. If no `enabled_on` or `disabled_on` attribute is defined, then the section can be added to any template.

The following table outlines the format of section data:

| Value | Type | Required | Description |
| - | - | - | - |
| `<SectionID>` | String | - | A unique ID for the section. Accepts only alphanumeric characters. |
| `<SectionType>` | String | Yes | The filename of the section file to render, without the extension. |
| `<SectionDisabled>` | Boolean | No | When `true`, the section isn't rendered but can still be customized in the theme editor. Is `false` by default. |
| `<BlockID>` | String | - | A unique ID for the block. Accepts only alphanumeric characters. |
| `<BlockType>` | String | Yes | The type of block to render, as defined in the schema of the section file. |
| `<BlockOrder>` | Array | No | An array of block IDs, ordered as they should be rendered. The IDs must exist in the `blocks` object, and duplicate IDs aren't allowed. |
| `<SettingID>` | String | - | The ID of a setting as defined in the schema of the section or the block. |
| `<SettingValue>` | (multiple) | - | A valid value for the setting. |

For example:

```json
sections: {
<SectionID>: {
  "type": <SectionType>,
  "disabled": <SectionDisabled>,
  "settings": {
    <SettingID>: <SettingValue>
  },
  "blocks": {
    <BlockID>: {
      "type": <BlockType>,
      "settings": {
        <SettingID>: <SettingValue>
      }
    }
  },
  "block_order": <BlockOrder>
}
}
```

For example, the following template renders the `product.liquid` and `product-recommendations.liquid` section files on product pages:

## templates/product.json

```json
{
  "sections": {
    "main": {
      "type": "product",
      "settings": {
        "show_vendor": true
      }
    },
    "recommendations": {
      "type": "product-recommendations"
    }
  },
  "order": [
    "main",
    "recommendations"
  ]
}
```

**Caution:**

Any sections that are included in a template, and aren't app sections, must exist in the theme. If they don't, then this will result in an error.

### Platform-controlled settings

In the theme editor, Shopify exposes a [custom CSS setting](https://help.shopify.com/manual/online-store/themes/theme-structure/extend/add-css) at the theme and section level. Any custom CSS that merchants add to a section instance is stored in a `custom_css` attribute in the section data.

This setting is intended to enable users to customize the look and feel of their storefront without editing theme code. As a theme developer, you shouldn't add this setting, or edit the value of this setting after it's set. Instead, you should use dedicated [CSS assets](https://shopify.dev/docs/storefronts/themes/architecture#assets) and [`stylesheet` Liquid tags](https://shopify.dev/docs/storefronts/themes/best-practices/javascript-and-stylesheet-tags#stylesheet), and introduce customization options for CSS in these areas using [theme settings](https://shopify.dev/docs/storefronts/themes/architecture/settings).

***

## Content

A JSON template accepts only JSON with a fixed schema and list of accepted attributes. For more information, refer to [JSON templates](https://shopify.dev/docs/storefronts/themes/architecture/templates/json-templates).

***
