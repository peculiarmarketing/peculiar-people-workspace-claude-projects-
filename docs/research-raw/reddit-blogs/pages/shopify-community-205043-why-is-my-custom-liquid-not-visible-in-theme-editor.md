URL: https://community.shopify.com/t/why-is-my-custom-liquid-not-visible-in-theme-editor/205043
JSON: https://community.shopify.com/t/205043.json
HTTP status: 200
Fetched: 2026-10-03 via curl (Discourse topic JSON)
Title: Why is my custom liquid not visible in Theme Editor?
Created: 2023-04-02T18:56:59.000Z
Last posted: 2023-04-02T18:56:59.000Z
Posts: 1  Views: 59
Category id: 211  Tags: []
Accepted answer: null

---

## Post 1 by supperluety at 2023-04-02T18:56:59.000Z
Hello there,

I’ve tried to create a custom liquid with help of ChatGPT but the liquid is not showing up in the Theme Editor. Does anyone know what the problem is?

Cheers!

{%- render 'custom-colors',
  id: section.id,
  background: section.settings.custom_background,
  text: section.settings.custom_text
-%}

<div class="custom-split-container">
  <div class="custom-split-left">
    <h2>{{ section.settings.heading }}</h2>
    <p>{{ section.settings.paragraph }}</p>
    <a href="{{ section.settings.button_url }}">{{ section.settings.button_text }}</a>
  </div>
  <div class="custom-split-right">
    <img src="{{ section.settings.image | img_url: '400x' }}" alt="{{ section.settings.image.alt }}">
    <p class="caption">{{ section.settings.image.caption }}</p>
  </div>
</div>

{% schema %}
{
  "name": "Custom Split Section",
  "settings": [
    {
      "type": "text",
      "id": "heading",
      "label": "Heading",
      "default": "Insert your heading here"
    },
    {
      "type": "richtext",
      "id": "paragraph",
      "label": "Paragraph",
      "default": "<p>Insert your paragraph text here</p>"
    },
    {
      "type": "url",
      "id": "button_url",
      "label": "Button URL"
    },
    {
      "type": "text",
      "id": "button_text",
      "label": "Button Text"
    },
    {
      "type": "image_picker",
      "id": "image",
      "label": "Image"
    }
  ]
}
{% endschema %}

{% stylesheet %}
  .custom-split-container {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: center;
    gap: 2rem;
  }

  .custom-split-left {
    flex: 0 0 50%;
    text-align: center;
  }

  .custom-split-right {
    flex: 0 0 50%;
    text-align: center;
  }

  .custom-split-right img {
    max-width: 100%;
  }

  .caption {
    font-size: 0.875rem;
    color: #666;
    margin-top: 0.5rem;
  }
{% endstylesheet %}

{% javascript %}
{% endjavascript %}
