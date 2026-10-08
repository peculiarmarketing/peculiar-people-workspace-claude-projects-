Source URL: https://shopify.dev/docs/storefronts/themes/architecture/blocks/theme-blocks
Fetched: 2026-10-03 via curl https://shopify.dev/docs/storefronts/themes/architecture/blocks/theme-blocks.md (HTTP 200, markdown)

---
title: Quick Start
description: >-
  Learn about theme blocks, a way to create reusable modules for structuring
  content within sections.
source_url:
  html: >-
    https://shopify.dev/docs/storefronts/themes/architecture/blocks/theme-blocks/quick-start?framework=liquid
  md: >-
    https://shopify.dev/docs/storefronts/themes/architecture/blocks/theme-blocks/quick-start.md?framework=liquid
api_name: liquid
---

# Quick Start

Learn how to build a basic theme block and add it to a section and another block file.

Theme blocks are blocks that are defined at the theme level. You can reuse theme blocks across different sections of the theme, unlike [section-defined blocks](https://shopify.dev/docs/storefronts/themes/architecture/blocks/section-blocks) that can only be used within the section where they're defined. Additionally, theme blocks can be nested within other theme blocks to create hierarchy.

## Requirements

[Understand Blocks at Shopify](https://shopify.dev/docs/storefronts/themes/architecture/blocks)

[Create a Theme](https://shopify.dev/docs/storefronts/themes/getting-started/create)

## Project

## Create a theme block

At the end of this tutorial, you should have a text block that can be reused across different sections and blocks of the theme. You will add it to a Custom Section and a Group block.

### Add a blocks folder

Theme blocks are Liquid files that are defined in the `blocks` directory of the theme. To create a theme block, add a Liquid file in the `/blocks` folder of your theme.

If your theme doesn't have a `/blocks` folder yet, then add one at the root of your theme. Add a `text.liquid` file to the `/blocks` folder.

### Write the markup

Theme block files contain markup.

The markup is any HTML or Liquid content that you want to include in the block.

## /blocks/text.liquid

```liquid
<div class="text-block text-{{ block.settings.alignment }}">
  {{ block.settings.text }}
</div>


{% stylesheet %}
  .text-left {
    text-align: left;
  }


  .text-center {
    text-align: center;
  }


  .text-right {
    text-align: right;
  }
{% endstylesheet %}


{% schema %}
{
  "name": "Text",
  "settings": [
    {
      "type": "richtext",
      "id": "text",
      "label": "Text"
    },
    {
      "type": "text_alignment",
      "id": "alignment",
      "label": "Alignment"
    },
  ],
  "presets": [
    { "name": "Text" },
    {
      "name": "Content",
      "settings": {
        "text": "<p>Hello, world!</p>"
      }
    }
  ]
}
{% endschema %}
```

### Write the schema

Theme block files contain a schema.

The schema is the `{% schema %}` Liquid tag, which is used to configure settings and attributes of the block. [Learn how to write block schema](https://shopify.dev/docs/storefronts/themes/architecture/blocks/theme-blocks/schema).

**Tip:** At this step, you'll be able to reference the theme block in a section file with [block targeting](https://shopify.dev/docs/storefronts/themes/architecture/blocks/theme-blocks/targeting). To make this block display in the theme editor's block picker, you need to [add a block preset](https://shopify.dev/docs/storefronts/themes/architecture/blocks/theme-blocks?extension=liquid#add-a-block-preset).

## /blocks/text.liquid

```liquid
<div class="text-block text-{{ block.settings.alignment }}">
  {{ block.settings.text }}
</div>


{% stylesheet %}
  .text-left {
    text-align: left;
  }


  .text-center {
    text-align: center;
  }


  .text-right {
    text-align: right;
  }
{% endstylesheet %}


{% schema %}
{
  "name": "Text",
  "settings": [
    {
      "type": "richtext",
      "id": "text",
      "label": "Text"
    },
    {
      "type": "text_alignment",
      "id": "alignment",
      "label": "Alignment"
    },
  ],
  "presets": [
    { "name": "Text" },
    {
      "name": "Content",
      "settings": {
        "text": "<p>Hello, world!</p>"
      }
    }
  ]
}
{% endschema %}
```

### Use Liquid objects in blocks

Blocks use a few key liquid objects:

* Theme blocks reference a [`block`](https://shopify.dev/docs/api/liquid/objects/block) object, which contains the properties and setting values of the block.
* Theme blocks can reference the [`section`](https://shopify.dev/docs/api/liquid/objects/section) object of the section that rendered the theme block.
* Theme blocks have access to [global objects](https://shopify.dev/docs/api/liquid/objects).

In this Text block example, this block references the settings attribute of the block object.

Theme blocks cannot access variables created outside the block and cannot be passed variables like when using a [snippet](https://shopify.dev/docs/storefronts/themes/architecture/snippets).

## /blocks/text.liquid

```liquid
<div class="text-block text-{{ block.settings.alignment }}">
  {{ block.settings.text }}
</div>


{% stylesheet %}
  .text-left {
    text-align: left;
  }


  .text-center {
    text-align: center;
  }


  .text-right {
    text-align: right;
  }
{% endstylesheet %}


{% schema %}
{
  "name": "Text",
  "settings": [
    {
      "type": "richtext",
      "id": "text",
      "label": "Text"
    },
    {
      "type": "text_alignment",
      "id": "alignment",
      "label": "Alignment"
    },
  ],
  "presets": [
    { "name": "Text" },
    {
      "name": "Content",
      "settings": {
        "text": "<p>Hello, world!</p>"
      }
    }
  ]
}
{% endschema %}
```

### Add a block preset

[Presets](https://shopify.dev/docs/storefronts/themes/architecture/blocks/theme-blocks/schema#presets) need to be defined in order for the theme block to be available for merchants in the theme editor block picker. You can author multiple presets for the same theme block.

In this example, the text theme blocks has two presets called Text and Content.

## Block presets

```json
"presets": [
  { "name": "Text" },
  {
    "name": "Content",
    "settings": {
      "text": "Hello, World!"
    }
  }
]
```

## /blocks/text.liquid

```liquid
<div class="text-block text-{{ block.settings.alignment }}">
  {{ block.settings.text }}
</div>


{% stylesheet %}
  .text-left {
    text-align: left;
  }


  .text-center {
    text-align: center;
  }


  .text-right {
    text-align: right;
  }
{% endstylesheet %}


{% schema %}
{
  "name": "Text",
  "settings": [
    {
      "type": "richtext",
      "id": "text",
      "label": "Text"
    },
    {
      "type": "text_alignment",
      "id": "alignment",
      "label": "Alignment"
    },
  ],
  "presets": [
    { "name": "Text" },
    {
      "name": "Content",
      "settings": {
        "text": "<p>Hello, world!</p>"
      }
    }
  ]
}
{% endschema %}
```

## Use theme blocks in sections

After theme blocks are defined in your theme, you need to update the theme's sections to render blocks.

**Tip:** Sections can either [define blocks locally](https://shopify.dev/docs/storefronts/themes/architecture/blocks/section-blocks) or opt-in to supporting theme blocks, but they can't support both simultaneously.

### Render the blocks in Liquid

Render the blocks in Liquid using

## Render blocks in liquid

```javascript
{% content_for 'blocks' %}
```

## /sections/custom-section.liquid

```liquid
<div class="custom-section color-{{ section.settings.color_scheme }}">
  {% content_for 'blocks' %}
</div>


{% schema %}
{
  "name": "Custom section",
  "blocks": [{ "type": "@theme" }, { "type": "@app" }],
  "settings": [
    {
      "type": "header",
      "content": "Color"
    },
    {
      "type": "color_scheme",
      "id": "color_scheme",
      "label": "Color scheme",
      "default": "scheme-1"
    }
  ],
  "presets": [
    {
      "name": "Custom section"
    },
    {
      "name": "Heading and text",
      "blocks": [
        {
          "type": "group",
          "settings": {
            "color_scheme": "scheme-3"
          },
          "blocks": [
            {
              "type": "text",
              "settings": {
                "text": "<h1>Image with text</h1>"
              }
            },
            {
              "type": "text",
              "settings": {
                "text": "<p>Pair text with an image to focus on your chosen product, collection, or blog post.</p>"
              }
            }
          ]
        }
      ]
    }
  ]
}
{% endschema %}
```

### Update the section schema

To accept all theme blocks in a section, add the type `@theme` to the [blocks attribute](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema#blocks) of the [schema](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema) of that section. To be more restrictive about which blocks can be use in specific sections, use [block targeting](https://shopify.dev/docs/storefronts/themes/architecture/blocks/theme-blocks/targeting).

## blocks attribute

```json
"blocks": [{ "type": "@theme" }, { "type": "@app" }],
```

## /sections/custom-section.liquid

```liquid
<div class="custom-section color-{{ section.settings.color_scheme }}">
  {% content_for 'blocks' %}
</div>


{% schema %}
{
  "name": "Custom section",
  "blocks": [{ "type": "@theme" }, { "type": "@app" }],
  "settings": [
    {
      "type": "header",
      "content": "Color"
    },
    {
      "type": "color_scheme",
      "id": "color_scheme",
      "label": "Color scheme",
      "default": "scheme-1"
    }
  ],
  "presets": [
    {
      "name": "Custom section"
    },
    {
      "name": "Heading and text",
      "blocks": [
        {
          "type": "group",
          "settings": {
            "color_scheme": "scheme-3"
          },
          "blocks": [
            {
              "type": "text",
              "settings": {
                "text": "<h1>Image with text</h1>"
              }
            },
            {
              "type": "text",
              "settings": {
                "text": "<p>Pair text with an image to focus on your chosen product, collection, or blog post.</p>"
              }
            }
          ]
        }
      ]
    }
  ]
}
{% endschema %}
```

## Nest blocks in theme blocks

Theme blocks can accept other theme and app blocks as children.

![Theme blocks can contain multiple levels of nested blocks](https://shopify.dev/assets/assets/themes/architecture/nested-blocks-example-B9HZ849r.png)

Theme blocks use the [`blocks` attribute](https://shopify.dev/docs/storefronts/themes/architecture/blocks/theme-blocks/schema#blocks) of their schema and assemble different configurations of these child blocks using the [`presets` attribute](https://shopify.dev/docs/storefronts/themes/architecture/blocks/theme-blocks/schema#presets).

In this example, the Group block has a preset called Column which is nesting the Text block using the `presets` attribute.

## Group block's Column preset nests Text blocks

```json
{
  "name": "Column",
  "settings": {
    "color_scheme": "scheme-3"
  },
  "blocks": [
    {
      "type": "text",
      "settings": {
        "text": "<h3>Hello, world!</h3>"
      }
    },
    {
      "type": "text",
      "settings": {
        "text": "<p>How's it going?<\/p>"
      }
    }
  ]
}
```

## /blocks/group.liquid

```liquid
<div
  class="group-block color-{{ block.settings.color_scheme }}"
>
  {% content_for 'blocks' %}
</div>


{% schema %}
{
  "name": "Group",
  "blocks": [{ "type": "@theme" }, { "type": "@app" }],
  "settings": [
    {
      "type": "header",
      "content": "Color"
    },
    {
      "type": "color_scheme",
      "id": "color_scheme",
      "label": "Color scheme",
      "default": "scheme-1"
    }
  ],
  "presets": [
    {
      "name": "Group"
    },
    {
      "name": "Column",
      "settings": {
        "color_scheme": "scheme-3"
      },
      "blocks": [
        {
          "type": "text",
          "settings": {
            "text": "<h3>Hello, world!</h3>"
          }
        },
        {
          "type": "text",
          "settings": {
            "text": "<p>How's it going?<\/p>"
          }
        }
      ]
    }
  ]
}
{% endschema %}
```

Each block's content is rendered by the liquid tag

## Render blocks in liquid

```javascript
{% content_for 'blocks' %}
```

The content is rendered in the order that's stored in the [JSON template](https://shopify.dev/docs/storefronts/themes/architecture/templates/json-templates). This is the same rendering mechanism sections use for blocks.

## /blocks/group.liquid

```liquid
<div
  class="group-block color-{{ block.settings.color_scheme }}"
>
  {% content_for 'blocks' %}
</div>


{% schema %}
{
  "name": "Group",
  "blocks": [{ "type": "@theme" }, { "type": "@app" }],
  "settings": [
    {
      "type": "header",
      "content": "Color"
    },
    {
      "type": "color_scheme",
      "id": "color_scheme",
      "label": "Color scheme",
      "default": "scheme-1"
    }
  ],
  "presets": [
    {
      "name": "Group"
    },
    {
      "name": "Column",
      "settings": {
        "color_scheme": "scheme-3"
      },
      "blocks": [
        {
          "type": "text",
          "settings": {
            "text": "<h3>Hello, world!</h3>"
          }
        },
        {
          "type": "text",
          "settings": {
            "text": "<p>How's it going?<\/p>"
          }
        }
      ]
    }
  ]
}
{% endschema %}
```

**Tip:** Block presets can refer to other theme blocks within the theme. This example refers to the `/blocks/text.liquid` Liquid file created earlier in this tutorial. Learn more about [theme block presets](https://shopify.dev/docs/storefronts/themes/architecture/blocks/theme-blocks/schema).

## /blocks/text.liquid

```liquid
<div class="text-block text-{{ block.settings.alignment }}">
  {{ block.settings.text }}
</div>


{% stylesheet %}
  .text-left {
    text-align: left;
  }


  .text-center {
    text-align: center;
  }


  .text-right {
    text-align: right;
  }
{% endstylesheet %}


{% schema %}
{
  "name": "Text",
  "settings": [
    {
      "type": "richtext",
      "id": "text",
      "label": "Text"
    },
    {
      "type": "text_alignment",
      "id": "alignment",
      "label": "Alignment"
    },
  ],
  "presets": [
    { "name": "Text" },
    {
      "name": "Content",
      "settings": {
        "text": "<p>Hello, world!</p>"
      }
    }
  ]
}
{% endschema %}
```

## /sections/custom-section.liquid

```liquid
<div class="custom-section color-{{ section.settings.color_scheme }}">
  {% content_for 'blocks' %}
</div>


{% schema %}
{
  "name": "Custom section",
  "blocks": [{ "type": "@theme" }, { "type": "@app" }],
  "settings": [
    {
      "type": "header",
      "content": "Color"
    },
    {
      "type": "color_scheme",
      "id": "color_scheme",
      "label": "Color scheme",
      "default": "scheme-1"
    }
  ],
  "presets": [
    {
      "name": "Custom section"
    },
    {
      "name": "Heading and text",
      "blocks": [
        {
          "type": "group",
          "settings": {
            "color_scheme": "scheme-3"
          },
          "blocks": [
            {
              "type": "text",
              "settings": {
                "text": "<h1>Image with text</h1>"
              }
            },
            {
              "type": "text",
              "settings": {
                "text": "<p>Pair text with an image to focus on your chosen product, collection, or blog post.</p>"
              }
            }
          ]
        }
      ]
    }
  ]
}
{% endschema %}
```

## /blocks/group.liquid

```liquid
<div
  class="group-block color-{{ block.settings.color_scheme }}"
>
  {% content_for 'blocks' %}
</div>


{% schema %}
{
  "name": "Group",
  "blocks": [{ "type": "@theme" }, { "type": "@app" }],
  "settings": [
    {
      "type": "header",
      "content": "Color"
    },
    {
      "type": "color_scheme",
      "id": "color_scheme",
      "label": "Color scheme",
      "default": "scheme-1"
    }
  ],
  "presets": [
    {
      "name": "Group"
    },
    {
      "name": "Column",
      "settings": {
        "color_scheme": "scheme-3"
      },
      "blocks": [
        {
          "type": "text",
          "settings": {
            "text": "<h3>Hello, world!</h3>"
          }
        },
        {
          "type": "text",
          "settings": {
            "text": "<p>How's it going?<\/p>"
          }
        }
      ]
    }
  ]
}
{% endschema %}
```

## Next Steps

The examples above demonstrate basic theme blocks usage. Theme blocks support several more advanced features to enhance the merchant experience as well as provide flexibility to theme developers.

[Theme block schema\
\
](https://shopify.dev/docs/storefronts/themes/architecture/blocks/theme-blocks/schema)

[Learn how to configure theme block settings and attributes through their schema.](https://shopify.dev/docs/storefronts/themes/architecture/blocks/theme-blocks/schema)

[Theme block availability with targeting\
\
](https://shopify.dev/docs/storefronts/themes/architecture/blocks/theme-blocks/targeting)

[Learn how to use targeting in order to restrict which theme blocks can be added by merchants to sections and blocks that accept nested blocks.](https://shopify.dev/docs/storefronts/themes/architecture/blocks/theme-blocks/targeting)

[Layout control with static blocks\
\
](https://shopify.dev/docs/storefronts/themes/architecture/blocks/theme-blocks/static-blocks)

[Learn how to have stricter control over the layout of theme blocks and sections using static blocks.](https://shopify.dev/docs/storefronts/themes/architecture/blocks/theme-blocks/static-blocks)

[Dynamic sources\
\
](https://shopify.dev/docs/storefronts/themes/architecture/blocks/theme-blocks/dynamic-sources)

[Learn how to enable more flexibility for merchants by connecting theme blocks to dynamic sources.](https://shopify.dev/docs/storefronts/themes/architecture/blocks/theme-blocks/dynamic-sources)
