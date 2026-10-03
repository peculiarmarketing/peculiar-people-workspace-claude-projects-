URL: https://community.shopify.com/t/not-been-to-center-the-section-which-i-created-using-sidekick/583083
JSON: https://community.shopify.com/t/583083.json
HTTP status: 200
Fetched: 2026-10-03 via curl (Discourse topic JSON)
Title: Not been to center the section which I created using Sidekick
Created: 2026-01-12T13:25:15.999Z
Last posted: 2026-01-14T08:47:19.691Z
Posts: 5  Views: 77
Category id: 133  Tags: [{'id': 1893, 'name': 'design', 'slug': 'design'}, {'id': 2995, 'name': 'css', 'slug': 'css'}, {'id': 3921, 'name': 'shopify-themes', 'slug': 'shopify-themes'}]
Accepted answer: null

---

## Post 1 by raridesign at 2026-01-12T13:25:16.181Z
Screenshot 2026-01-12 1854291917×1031 46.2 KB

why is the section not taking the full width of the page, kindly help me, this is created using side kick

## Post 2 by suyash1 at 2026-01-12T13:27:09.740Z
@raridesign it must be having fixed width and margin set to it, can you please share this page link?

## Post 3 by topnewyork at 2026-01-12T13:31:33.733Z
Hi @raridesign,

Go to Online Store → Theme → Edit code.

2. Open your theme.css / based.css / style.css file and paste the code in the bottom of the file.

.ai-product-reviews__container-awhhhshloohnpm29fsaigenblock45ae8f87qn6bk {
    max-width: 1600px !important;
}

image1587×665 52.9 KB

Thanks!

## Post 5 by Moeed at 2026-01-12T13:33:07.931Z
Hey @raridesign

Follow these Steps:

- Go to Online Store

- Edit Code

- Find theme.liquid file

- Add the following code in the bottom of the file above </ body> tag

<style>
.ai-product-reviews__header-awhhhshloohnpm29fsaigenblock45ae8f87qn6bk {
    text-align: -webkit-center !important;
    justify-items: center !important;
}
</style>

RESULT:

image1049×802 18.3 KB

If I managed to help you then a Like would be truly appreciated.

Best,

Moeed

## Post 6 by AnneLuo at 2026-01-14T08:47:19.691Z
Hi @raridesign

You can try this code by following these steps:

Step 1: Go to the online store ->Theme ->Edit Code.

Step 2: Find the theme.liquid file and add the following code before the </head> tag

<style>
.ai-product-reviews__container-awhhhshloohnpm29fsaigenblock45ae8f87qn6bk {
    max-width: 100% !important; 
    padding: 0 !important; 
}
</style>

Results:

image1410×623 18.8 KB

Hope this helps!  If yes then Please don’t forget hit Like and Mark it as solution!
