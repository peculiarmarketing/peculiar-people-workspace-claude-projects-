URL: https://community.shopify.com/t/invalid-json-in-tag-schema-error-for-whole-code/169273
JSON: https://community.shopify.com/t/169273.json
HTTP status: 200
Fetched: 2026-10-03 via curl (Discourse topic JSON)
Title: Invalid JSON in Tag 'schema' error for whole code
Created: 2022-11-19T17:30:35.000Z
Last posted: 2022-11-20T12:47:44.000Z
Posts: 7  Views: 177
Category id: 211  Tags: []
Accepted answer: null

---

## Post 1 by anand_choudhary at 2022-11-19T17:30:35.000Z
Can someone help me with where I am going wrong?

<style>
.content-block-b1-button {background-color: #232323; color: #ffffff; cursor: pointer; border: solid #232323; border-radius: {{ section.settings.border-radius }}; }
.content-block-b1-title {font-family: Poppins; font-weight: 600;}
@media only screen and (max-width: 680px) {
  /* For mobile phones: */
    .d1 {display: flex; gap: 1%; overflow-x: scroll; overflow-y: hidden; }
    .image-banner-c1 { min-width: 70%; aspect-ratio: auto 3/5 ; border-radius: {{ section.settings.border-radius }}; display: flex; flex-direction: column;}
    .content-image-a1 {height: 65%; width: 100%; border-radius: {{ section.settings.border-radius }} {{ section.settings.border-radius }} 0 0; object-fit: cover;}
    .content-block-b1 {height: auto; width: 100%; background-color: #fafcfc; border-radius: 0 0 {{ section.settings.border-radius }} {{ section.settings.border-radius }}; }
    .content-block-b1-brand { margin: 10px 15px 0; font-size: 1em;}
    .content-block-b1-title { margin: 0 15px; font-size: 2em;}
    .content-block-b1-button { margin: 5px 15px 20px; width: calc(100% - 30px); height: 50px; font-size: 1.3em; }
}
@media only screen and (min-width: 681px) {
    .d1 {display: flex; gap: 1%; }
    .image-banner-c1 { width: 49.5%; aspect-ratio: auto 4/2; border-radius: {{ section.settings.border-radius }}; display: flex;}
    .content-image-a1 {height: 100%; width: 50%; border-radius: {{ section.settings.border-radius }} 0 0 {{ section.settings.border-radius }}; object-fit: cover;}
    .content-block-b1 {height: 100%; width: 50%; background-color: #fafcfc; border-radius: 0 0 {{ section.settings.border-radius }} {{ section.settings.border-radius }}; position: relative;}
    .content-block-b1-brand { margin: 20px 20px 0; font-size: 1em;margin-top: 20px !important;}
    .content-block-b1-title { margin: 0 20px; margin-top: 10px !important; font-size: 2em;}
    .content-block-b1-button { margin: 10px 20px 10px; width: calc(100% - 40px); height: 50px; font-size: 1.3em; right: 0px; position:absolute; bottom: 10px; }
}

@media only screen and (max-width: 682px) {
  /* For mobile phones: */
    .d1 {display: flex; gap: 1%; overflow-x: scroll; overflow-y: hidden; }
    .image-banner-c1 { min-width: 70%; aspect-ratio: auto 3/5 ; border-radius: {{ section.settings.border-radius }}; display: flex; flex-direction: column;}
    .content-image-a1 {height: 65%; width: 100%; border-radius: {{ section.settings.border-radius }} {{ section.settings.border-radius }} 0 0; object-fit: cover; }
    .content-block-b1{height: auto; width: 100%; background-color: #fafafa !important; border-radius: 0 0 {{ section.settings.border-radius }} {{ section.settings.border-radius }}; }
    .content-block-b1-brand { margin: 10px 15px 0; font-size: 1em;}
    .content-block-b1-title { margin: 0 15px; font-size: 1.5em; }
    .content-block-b1-button { margin: 10px 15px 20px; width: calc(100% - 30px); height: 50px; font-size: 1.3em; }
}

</style>

{%- if section.blocks.size > 0 -%}
	<div class="d1">
		<div class="image-banner-c1">
			<img class="content-image-a1" src="{{ block.settings.first_image|img_url:'600x600', crop: 'center' }} loading="lazy"">
			<div class="content-block-b1">
        		<div class="content-block-b1-brand">{{ block.settings.b1_brand }}</div>
                <div class="content-block-b1-title">{{ block.settings.b1_title }}</div>
                <a href="{{ block.settings.b1_button_link }} "><button class="content-block-b1-button">{{ block.settings.b1_button_option }}</button>
          </div>
       </div>
{% endif %}
{% schema %}
{
  "name": "Image Banner Custom",
  "class": "image-banner-c1",
  "max_blocks": "2"
}
  "blocks": [
  {
   "type": "image_picker",
   "id": "first_image",
   "label": "Image"
   },
    {
     "type": "select",
     "id": "border-radius",
     "label": "Border Radius",
     "options": [
    {
     "label": "5px",
     "value": "5px"
     }, 
    {
     "label": "10px",
     "value": "10px"
     },
    {
     "label": "15px",
     "value": "15px"
     }
    ],
     "default": "10px",
    },
 {
  "type": "text",
  "id": "b1_brand",
  "label": "Brand - Sub Title"
 },
 {
  "type": "text",
  "id": "b1_title",
  "label": "Title - Product Category"
 },
{
  "type": "url",
  "id": "b1_button_link",
  "label": "Card Link"
},
  {
  "type": "select",
  "id": "b1_button_option",
  "label": "Visit Now - Shop Now",
  "default": "Visit Now",
  "options": [
    {
     "label": "Visit Now",
     "value": "Visit Now"
     }, 
    {
     "label": "Shop Now",
     "value": "Shop Now"
     }
    ]
    }
]
{% endschema %}

## Post 2 by kaalTechGeeks at 2022-11-19T17:50:46.000Z
Hi @anand_choudhary ,

Just replace the above code with the below code:

{%- if section.blocks.size > 0 -%}
	
		

			
			

        		
{{ block.settings.b1_brand }}

                {{ block.settings.b1_title }}

                
          

       

{% endif %}
{% schema %}
{
   "name":"Image Banner Custom",
   "class":"image-banner-c1",
   "max_blocks":"2",
   "blocks":[
      {
         "type":"image_picker",
         "id":"first_image",
         "label":"Image"
      },
      {
         "type":"select",
         "id":"border-radius",
         "label":"Border Radius",
         "options":[
            {
               "label":"5px",
               "value":"5px"
            },
            {
               "label":"10px",
               "value":"10px"
            },
            {
               "label":"15px",
               "value":"15px"
            }
         ],
         "default":"10px"
      },
      {
         "type":"text",
         "id":"b1_brand",
         "label":"Brand - Sub Title"
      },
      {
         "type":"text",
         "id":"b1_title",
         "label":"Title - Product Category"
      },
      {
         "type":"url",
         "id":"b1_button_link",
         "label":"Card Link"
      },
      {
         "type":"select",
         "id":"b1_button_option",
         "label":"Visit Now - Shop Now",
         "default":"Visit Now",
         "options":[
            {
               "label":"Visit Now",
               "value":"Visit Now"
            },
            {
               "label":"Shop Now",
               "value":"Shop Now"
            }
         ]
      }
   ]
}
{% endschema %}

Thanks

## Post 3 by anand_choudhary at 2022-11-19T18:07:46.000Z
Hi @kaalTechGeeks it still shows the same error.

## Post 4 by anand_choudhary at 2022-11-19T18:17:46.000Z
These are the errors I’m receiving

Invalid block ‘image_picker’: name is required

Invalid block ‘image_picker’: ‘id’ is not a valid attribute

Invalid block ‘image_picker’: ‘label’ is not a valid attribute

Invalid block ‘select’: name is required

Invalid block ‘select’: name is already taken

Invalid block ‘select’: ‘id’ is not a valid attribute

Invalid block ‘select’: ‘label’ is not a valid attribute

Invalid block ‘select’: ‘options’ is not a valid attribute

Invalid block ‘select’: ‘default’ is not a valid attribute

Invalid block ‘text’: name is required

Invalid block ‘text’: name is already taken

Invalid block ‘text’: ‘id’ is not a valid attribute

Invalid block ‘text’: ‘label’ is not a valid attribute

Invalid block ‘text’: type is already taken

Invalid block ‘url’: name is required

Invalid block ‘url’: name is already taken

Invalid block ‘url’: ‘id’ is not a valid attribute

Invalid block ‘url’: ‘label’ is not a valid attribute

Invalid block ‘select’: type is already taken

## Post 5 by kaalTechGeeks at 2022-11-19T18:22:36.000Z
Hi @anand_choudhary ,

There was a lot of bugs in the code not just the schema,

I have fixed all of them please use the below code:

{%- if section.blocks.size > 0 -%}
  {% for block in section.blocks %}
	
		

			
			

        		
{{ block.settings.b1_brand }}

                {{ block.settings.b1_title }}

                
          

       

  {% endfor %}
{% endif %}
{% schema %}
{
   "name":"Image Banner Custom",
   "class":"image-banner-c1",
   "max_blocks":2,
   "blocks":[
      {
         "type":"image_picker",
         "name":"Image Picker",
         "settings":[
            {
               "type":"image_picker",
               "id":"first_image",
               "label":"Image"
            },
            {
               "type":"select",
               "id":"border-radius",
               "label":"Border Radius",
               "options":[
                  {
                     "label":"5px",
                     "value":"5px"
                  },
                  {
                     "label":"10px",
                     "value":"10px"
                  },
                  {
                     "label":"15px",
                     "value":"15px"
                  }
               ],
               "default":"10px"
            },
            {
               "type":"text",
               "id":"b1_brand",
               "label":"Brand - Sub Title"
            },
            {
               "type":"text",
               "id":"b1_title",
               "label":"Title - Product Category"
            },
            {
               "type":"url",
               "id":"b1_button_link",
               "label":"Card Link"
            },
            {
               "type":"select",
               "id":"b1_button_option",
               "label":"Visit Now - Shop Now",
               "default":"Visit Now",
               "options":[
                  {
                     "label":"Visit Now",
                     "value":"Visit Now"
                  },
                  {
                     "label":"Shop Now",
                     "value":"Shop Now"
                  }
               ]
            }
         ]
      }
   ]
}
{% endschema %}

## Post 6 by anand_choudhary at 2022-11-20T09:44:06.000Z
It still shows a error,

New schema is incompatible with the current setting value. Invalid value for type in block ‘d5306451-36c3-49b6-8884-856944b3648a-16688487846e27311c-0’. Type must be defined in schema..New schema is incompatible with the current setting value. Invalid value for type in block ‘d5306451-36c3-49b6-8884-856944b3648a-16688487846e27311c-1’. Type must be defined in schema..New schema is incompatible with the current setting value. Invalid value for type in block ‘d5306451-36c3-49b6-8884-856944b3648a-16688487846e27311c-2’. Type must be defined in schema..New schema is incompatible with the current setting value. Invalid value for type in block ‘d5306451-36c3-49b6-8884-856944b3648a-16688487846e27311c-3’. Type must be defined in schema.

## Post 7 by kaalTechGeeks at 2022-11-20T12:47:44.000Z
So to make it compatible you have to first remove this specific section from the customization settings and then add this section back using the customize settings then it will be fixed.

The reason it shows the error is because you have already added values as per your previous schema which had errors, and what I have sent you is new schema with different block.

If you still face any issue then do let me know and we can get over a shot meeting to fix this.

Thanks
