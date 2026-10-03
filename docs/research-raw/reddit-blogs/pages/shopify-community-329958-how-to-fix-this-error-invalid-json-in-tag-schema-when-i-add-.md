URL: https://community.shopify.com/t/how-to-fix-this-error-invalid-json-in-tag-schema-when-i-add-a-collapsible-section/329958
JSON: https://community.shopify.com/t/329958.json
HTTP status: 200
Fetched: 2026-10-03 via curl (Discourse topic JSON)
Title: How to fix this error " Invalid JSON in tag 'schema'" when i add a collapsible section?
Created: 2024-06-08T12:08:58.000Z
Last posted: 2024-06-09T03:06:41.000Z
Posts: 3  Views: 161
Category id: 133  Tags: [{'id': 4021, 'name': 'troubleshooting', 'slug': 'troubleshooting'}, {'id': 3921, 'name': 'shopify-themes', 'slug': 'shopify-themes'}, {'id': 4694, 'name': 'html', 'slug': 'html'}, {'id': 2856, 'name': 'landing-page', 'slug': 'landing-page'}]
Accepted answer: null

---

## Post 1 by abdelrahman298 at 2024-06-08T12:08:58.000Z
The Command send me this message and can’t find any error

Invalid JSON in tag ‘schema’

{% schema %}

{

“name”: “my-collapsible”,

“settings”: [

{

“type” : “text”,

“id” : “caption”,

“label” : “write your caption”

},

{

“type” : “article”,

“id” : “heading”,

“label” : “heading”

}

],

“blocks” : [

{

“name”:“add my block”,

“type”:“collapsible”,

“settings” : [

{

“type” : “text”,

“id” :“coll_heading”,

“label” :“write your collapse”

},

{

“type” : “article”,

“id” : “coll_body”,

“label” : “write your body”

}

],

},

],

“presets”: [

{“name”: “my-collapseible”}

]

}

{% endschema %}

## Post 2 by Columbus_Themes at 2024-06-08T12:45:06.000Z
Try this:

{% schema %}

{

“name”: “my-collapsible”,

“settings”: [

{

“type”: “text”,

“id”: “caption”,

“label”: “write your caption”

},

{

“type”: “richtext”, // Consider using “richtext” for heading content

“id”: “heading”,

“label”: “heading”

}

],

“blocks”: [

{

“name”: “add my block”,

“type”: “collapsible”,

“settings”: [

{

“type”: “text”,

“id”: “coll_heading”,

“label”: “write your collapse”

},

{

“type”: “richtext”, // Consider using “richtext” for body content

“id”: “coll_body”,

“label”: “write your body”

}

]

}

],

“presets”: [

{ “name”: “my-collapseible” }

]

}

{% endschema %}

## Post 3 by BSSCommerce-B2B at 2024-06-09T03:06:41.000Z
Hi @abdelrahman298

It seems that your issue has not been resolved yet, I suggest replacing the JSON snippet with

{% schema %}
{
  "name": "my-collapsible",
  "settings": [
    {
      "type" : "text",
      "id" : "caption",
      "label" : "write your caption"
    },
    {
      "type" : "article",
      "id" : "heading",
      "label" : "heading"
    }
  ],
  "blocks" : [
    {
      "name":"add my block",
      "type":"collapsible",
      "settings" : [
        {
          "type" : "text",
          "id" :"coll_heading",
          "label" :"write your collapse"
        },
        {
          "type" : "article",
          "id" : "coll_body",
          "label" : "write your body"
        }
      ]
   
    }
  ],
  "presets": [
    {"name": "my-collapseible"}
  ]
}
{% endschema %}

If it helps you, please like and mark it as the solution

Best regards.
