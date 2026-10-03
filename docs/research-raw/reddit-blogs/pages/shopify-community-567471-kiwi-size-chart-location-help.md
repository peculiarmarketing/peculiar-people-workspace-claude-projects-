URL: https://community.shopify.com/t/kiwi-size-chart-location-help/567471
JSON: https://community.shopify.com/t/567471.json
HTTP status: 200
Fetched: 2026-10-03 via curl (Discourse topic JSON)
Title: Kiwi Size Chart Location Help
Created: 2025-09-25T00:12:06.195Z
Last posted: 2025-09-25T00:51:51.661Z
Posts: 3  Views: 117
Category id: 133  Tags: [{'id': 4021, 'name': 'troubleshooting', 'slug': 'troubleshooting'}, {'id': 1893, 'name': 'design', 'slug': 'design'}, {'id': 2995, 'name': 'css', 'slug': 'css'}, {'id': 2068, 'name': 'customizations', 'slug': 'customizations'}, {'id': 4694, 'name': 'html', 'slug': 'html'}]
Accepted answer: null

---

## Post 1 by lev123 at 2025-09-25T00:12:06.316Z
I have followed all the kiwi sizing instructions to position my size chart above my size variant selector and now matter what I do I can’t get it there. Can anyone help?

I’m using Horizon theme.

  
      

      The Snouts Collective
  

  
    

The Snouts Collective

  The Snouts Collective

  

  
    
    
  

  

Password: Bonnie123

## Post 2 by The_ScriptFlow at 2025-09-25T00:41:26.273Z
lev123:

Bonnie123

Many of the Merchants face the same issue.

But I help them to relocate it. See here: VEDORE Regular Fit Linen Loose Pants – Vedore Lifestyle

  
      

      Linda Utrecht
  

  
    

Matteo - Casual heren-fleecejacket

  Matteo – Casual heren-fleecejacket Blijf stijlvol en comfortabel met het Matteo fleecejack. Perfect voor dagelijkse casual looks, met zacht materiaal dat warmte biedt zonder zwaar aan te voelen. Ideaal voor werk, vrije tijd of buitenactiviteiten....

  
    Price: EUR 59,95
  

  

  
    
    
  

  

If you want to get it fixed check your p/m.

## Post 3 by The_ScriptFlow at 2025-09-25T00:51:51.661Z  [ACCEPTED ANSWER]
Or You can paste the following code in the Custom Css of theme settings.

.ks-chart-container.sizing-chart-container.ks-container-with-modal {
  transform: translate(0px, -113px) !important;
  height: 0 !important;
}
.group-block.group-block--height-fit.group-block--width-fill.border-style.spacing-style.size-style {
  padding: 0px 0px 16px 0px;
}
@media only screen and (max-width: 767px) {
.ks-chart-container.sizing-chart-container.ks-container-with-modal {
  transform: translate(0px, -123px) !important;
  height: 0 !important;
}
}

Results:

image1549×504 111 KB
