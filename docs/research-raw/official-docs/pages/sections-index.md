Source URL: https://shopify.dev/docs/storefronts/themes/architecture/sections
Fetched: 2026-10-03 via curl https://shopify.dev/docs/storefronts/themes/architecture/sections.md (HTTP 200, markdown)

---
title: Sections
description: >-
  Learn about sections, a way to create reusable modules of content for your
  theme.
source_url:
  html: 'https://shopify.dev/docs/storefronts/themes/architecture/sections'
  md: 'https://shopify.dev/docs/storefronts/themes/architecture/sections.md'
api_name: liquid
---

# Sections

Sections are Liquid files that allow you to create reusable modules of content that can be customized by merchants. They can also include [blocks](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema#blocks) which allow merchants to add, remove, and reorder content within a section.

For example, you can create an **Image with text** section that displays an image and text side-by-side with options for merchants to choose the image, set the text, and select the display order.

Sections can be dynamically added to pages using [JSON templates](https://shopify.dev/docs/storefronts/themes/architecture/templates/json-templates) or [section groups](https://shopify.dev/docs/storefronts/themes/architecture/section-groups), giving merchants flexibility to easily customize page layouts. Sections that are included in JSON templates or section groups can support [app blocks](https://shopify.dev/docs/storefronts/themes/architecture/blocks/app-blocks), which give merchants the option to include app content within a section without having to edit theme code. JSON templates and section groups can render up to 25 sections, and each section can have up to 50 [blocks](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema#blocks).

Sections can also be [included statically](#statically-render-a-section), which can provide merchants with in-context customization options for static content.

By default, sections are available for any template or section group. You can limit which templates and section groups have access in the [section schema](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema).

The following diagram shows the main theme architecture components with sections highlighted in blue and blocks highlighted in red:

![Diagram of theme architecture components with sections highlighted in blue and blocks highlighted in red.](https://shopify.dev/assets/assets/images/themes/architecture/section-and-block-BGj5HnqS.png)

***

## Location

Section files are located in the `sections` directory of the theme:

```text
└── theme
  ...
  ├── templates
  ├── sections
  ...
```

***

## Content

Sections can contain three main types of content:

| Type | Description | Required |
| - | - | - |
| **Main content** | Any HTML or Liquid content you might want to include in the section.Sections have the same access to [global objects](https://shopify.dev/docs/api/liquid/objects), [tags](https://shopify.dev/docs/api/liquid/tags), and [filters](https://shopify.dev/docs/api/liquid/filters) as other Liquid theme files, as well as the following section-specific objects:- **The [`section` object](https://shopify.dev/docs/api/liquid/objects/section)** - Contains the section's properties and setting values.
- **The [`block` object](https://shopify.dev/docs/api/liquid/objects/block)** - Contains the properties and setting values of a single section block.Aside from global objects, variables created outside of sections aren't accessible within sections.The section and block objects, as well as variables created within sections, aren't available outside of their respective section. The only exception is when you reference section and block objects within a snippet that's rendered inside the section you're referencing. | No |
| **Assets** | Sections can bundle their own JavaScript and stylesheet assets with the following section-specific Liquid tags:- [`{% javascript %}`](https://shopify.dev/docs/storefronts/themes/best-practices/javascript-and-stylesheet-tags#javascript)
- [`{% stylesheet %}`](https://shopify.dev/docs/storefronts/themes/best-practices/javascript-and-stylesheet-tags#stylesheet)To learn more, refer to [Section assets](https://shopify.dev/docs/storefronts/themes/best-practices/javascript-and-stylesheet-tags). | No |
| **Schema** | Sections support the `{% schema %}` Liquid tag. This tag is used to define the following section attributes and settings:- [name](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema#name)
- [tag](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema#tag)
- [class](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema#class)
- [limit](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema#limit)
- [settings](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema#settings)
- [blocks](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema#blocks)
- [app blocks](https://shopify.dev/docs/storefronts/themes/architecture/blocks/app-blocks)
- [max\_blocks](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema#max_blocks)
- [presets](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema#presets)
- [defaults](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema#default)
- [locales](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema#locales)
- [enabled\_on](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema#enabled_on)
- [disabled\_on](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema#disabled_on)To learn more, refer to [Section schema](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema). | Yes |

***

## Usage

When working with sections, you should familiarize yourself with the following:

* [How to render a section](#render-a-section)
* [How to integrate sections with the theme editor](#integrate-sections-with-the-theme-editor)
* [Support app blocks](#support-app-blocks)

### Render a section

You can render sections in one of the following ways:

* Reference the section in a [JSON template](https://shopify.dev/docs/storefronts/themes/architecture/templates/json-templates), or a [section group](https://shopify.dev/docs/storefronts/themes/architecture/section-groups) in a [layout](https://shopify.dev/docs/storefronts/themes/architecture/layouts) file.
* [Statically render](#statically-render-a-section) the section with the `section` Liquid tag.
* Use the [Section Rendering API](https://shopify.dev/docs/api/ajax/section-rendering).

**Tip:**

If you want to render sections inside a template, then use a JSON template. JSON templates provide more extensive customization options for merchants, and improve the theme editor's performance.

#### Statically render a section

**Caution:**

Whenever possible, you should avoid statically rendering sections. Instead, you should reference them in a JSON template or section group. Statically rendered sections can't be removed or reordered by merchants.

You can statically render a section using the Liquid [section tag](https://shopify.dev/docs/api/liquid/tags/section).

For example, to include a section in a [Liquid template](https://shopify.dev/docs/storefronts/themes/architecture/templates/liquid-templates), you can include it with a section tag:

## /templates/customers/register.liquid

```liquid
{% section 'featured-product' %}
```

**Note:**

You can include a statically rendered section in multiple theme files. However, only one instance of the section exists. If you change section settings in one location, then the change will be applied to all locations where the section is rendered.

### Integrate sections with the theme editor

When users customize sections and blocks through the theme editor, their HTML is dynamically added, removed, or re-rendered directly onto the existing DOM, without reloading the entire page. However, any associated JavaScript that runs when the page loads won't run again.

Additionally, you must make sure that when a section or block is selected, that section or block becomes, and remains, visible while it’s selected. For example, a slideshow section should scroll into view when the section is selected, slide to a selected block (slide), and pause while that block is selected.

To help identify theme editor actions like section and block selection or reordering, you can use the [JavaScript events](https://shopify.dev/docs/storefronts/themes/best-practices/editor/integrate-sections-and-blocks#javascript-events) emitted by the theme editor.

You might also want to prevent specific code from running in the theme editor. To do so, you can use Liquid and JavaScript variables for [detecting the theme editor](https://shopify.dev/docs/storefronts/themes/best-practices/editor/integrate-sections-and-blocks#detect-the-theme-editor).

**Tip:**

Section and block files must define [presets](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema#presets) in their schema to support being added to JSON templates using the theme editor. Files without presets should be included in the JSON file manually, and can't be removed using the theme editor.

### Support app blocks

App blocks allow app developers to create blocks for merchants to add app content to their theme without having to directly edit theme code.

To learn more about how to make your theme compatible with app blocks, refer to [App blocks](https://shopify.dev/docs/storefronts/themes/architecture/blocks/app-blocks).

***
