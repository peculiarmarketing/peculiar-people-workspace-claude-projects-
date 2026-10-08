URL: https://community.shopify.com/t/generate-blocks-in-any-theme/417074
JSON: https://community.shopify.com/t/417074.json
HTTP status: 200
Fetched: 2026-10-03 via curl (Discourse topic JSON)
Title: Generate Blocks in Any Theme
Created: 2025-05-30T19:06:03.000Z
Last posted: 2025-05-31T04:05:11.000Z
Posts: 3  Views: 283
Category id: 95  Tags: [{'id': 4021, 'name': 'troubleshooting', 'slug': 'troubleshooting'}]
Accepted answer: null

---

## Post 1 by DrewOswald at 2025-05-30T19:06:03.000Z
Generate Blocks in Any Theme

I made a section that allows any theme to access the new Generate Blocks functionality introduced in the recent Shopify Editions Summer '25 shown here: https://www.shopify.com/editions/summer2025#generate-theme-blocks-with-ai

It is basically just a section that uses theme blocks i.e. “@theme” as a block type in the section’s schema and then outputs the theme blocks with {% content_for ‘blocks’ %}

For example:

{% content_for 'blocks' %}

{% schema %}
...
"blocks": [
    {
      "type": "@theme"
    }
  ],
...
{% endschema %}

Note: You can’t use “@theme” blocks and blocks defined the schema in a section at the same time.

Instructions:### 1. Add the ai-powered-section.liquid file to the “sections” folder in your theme files

001.png883×987 95.6 KB

002.png770×1064 85.3 KB

Ai-powered-section.liquid:

{% content_for 'blocks' %}

{% schema %}
{
  "name": "AI-Powered Section",
  "blocks": [
    {
      "type": "@theme"
    }
  ],
  "settings": [
    {
      "type": "header",
      "content": "Instructions",
      "info": "Add a block to this section, then select Generate."
    },
    {
      "type": "header",
      "content": "Settings",
      "info": "There are no settings for this section. Try checking the generated blocks."
    }
  ],
  "presets": [
    {
      "name": "AI-Powered Section"
    }
  ]
}
{% endschema %}

2. Add the section to your theme and start generating custom blocks with A.I.

003.png922×567 92.1 KB

004.png563×653 51 KB

Bonus Tips

Bonus tip 1: If your custom blocks aren’t aligning with the layout of the rest of your content then ask the A.I. to add a setting that allows you to align the block.

Note: Follow up instructions are only available before saving the block to the theme files.

006.png632×319 36.7 KB

Ex follow up prompt 1: Could you add a page width setting.

Ex follow up prompt 2: Could you add a setting that let’s me align the content in the center.

Bonus tip 2: If you know how to code and want to try editing the code for the generated block directly you can navigate to the file quickly by right clicking the block and selecting “Edit code”

Note: “Edit code” is only available after the generated block has been saved to the theme files by clicking “Save”

005.png427×469 45.3 KB

## Post 2 by BiDeal-Discount at 2025-05-31T01:38:43.000Z
It’s useful. Thank @DrewOswald

## Post 3 by DrewOswald at 2025-05-31T04:05:11.000Z
Sorry about the broken link. Here’s the correct one: https://www.shopify.com/editions/summer2025#generate-theme-blocks-with-ai
