URL: https://community.shopify.com/t/not-been-to-center-the-section-which-i-created-using-sidekick/580094
JSON: https://community.shopify.com/t/580094.json
HTTP status: 200
Fetched: 2026-10-03 via curl (Discourse topic JSON)
Title: Not been to center the section which I created using Sidekick
Created: 2025-12-18T05:34:19.710Z
Last posted: 2025-12-18T06:03:25.843Z
Posts: 5  Views: 82
Category id: 133  Tags: [{'id': 4021, 'name': 'troubleshooting', 'slug': 'troubleshooting'}, {'id': 1893, 'name': 'design', 'slug': 'design'}, {'id': 2995, 'name': 'css', 'slug': 'css'}, {'id': 2068, 'name': 'customizations', 'slug': 'customizations'}]
Accepted answer: null

---

## Post 1 by raridesign at 2025-12-18T05:34:19.853Z
I had created this section of about us using Shopify Sidekick AI by giving prompt - in the preview beside the prompt it is showing perfect layout but when I save the section and see the output on live website then it is showing up like this (image attached below). How to fix this? My theme is Atelier 2.1.6

121915×1030 224 KB

## Post 3 by tim_tairli at 2025-12-18T05:55:13.221Z
You can always ask it to improve the design, however, there is a chance your lose something else 

You can’t see it in “Edit theme” because the site width is limited there and your section cover it entirely.

This can be fixed with this code added to the “Custom CSS” setting of this section:

.layout-panel-flex.layout-panel-flex--column {
  align-items: center;
}

Or this,

if want to add it elsewhere
(In “theme settings”=>“custom css”, or your stylesheet asset file)

.layout-panel-flex:has([class^="ai-about"]) {
  align-items: center;
}

Screenshot 2025-12-18 at 4.25.31 PM1510×593 81.4 KB

## Post 4 by Moeed at 2025-12-18T05:55:54.823Z
Hey @raridesign

Follow these Steps:

- Go to Online Store

- Edit Code

- Find theme.liquid file

- Add the following code in the bottom of the file above </ body> tag

<style>
div#shopify-block-AVDBGZnpabGFLaGxZd__ai_gen_block_c6006e7_BmFycP {
    width: 100% !important;
}
</style>

RESULT:

image1910×919 216 KB

If you require any other help, feel free to reach out to me. If I managed to help you then a Like would be truly appreciated.

Best,

Moeed

## Post 5 by raridesign at 2025-12-18T06:01:50.606Z
Thank you for the solution

## Post 6 by Moeed at 2025-12-18T06:03:25.843Z
Thank you for your reply. I’m glad to hear that the solution worked well for you. If you require any more help, please don’t hesitate to reach out. If you find this information useful, a Like would be greatly appreciated.

Cheers,

Moeed
