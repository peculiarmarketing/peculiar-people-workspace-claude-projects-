URL: https://community.shopify.com/t/urgent-matter-sahara-theme-collection-code-went-wrong/417178
JSON: https://community.shopify.com/t/417178.json
HTTP status: 200
Fetched: 2026-10-03 via curl (Discourse topic JSON)
Title: Urgent matter! Sahara theme collection code went wrong
Created: 2025-05-31T13:30:08.000Z
Last posted: 2025-05-31T16:32:42.000Z
Posts: 8  Views: 96
Category id: 133  Tags: [{'id': 4021, 'name': 'troubleshooting', 'slug': 'troubleshooting'}, {'id': 1893, 'name': 'design', 'slug': 'design'}, {'id': 2068, 'name': 'customizations', 'slug': 'customizations'}, {'id': 3921, 'name': 'shopify-themes', 'slug': 'shopify-themes'}, {'id': 1775, 'name': 'liquid', 'slug': 'liquid'}, {'id': 3015, 'name': 'third-party-themes', 'slug': 'third-party-themes'}]
Accepted answer: null

---

## Post 1 by MicalJoseph at 2025-05-31T13:30:08.000Z
I wanted to create a Klaviyo mailing to let customers know that a restock of one of the pants is coming.

I had added a button in the email, so that when customers clicked it, they would automatically be added to a segment. The button linked to a thank-you page on my website that said: "Thank you. We’ll let you know when the pants are back in stock.

However, I had built that thank-you page as a “standard page” in Shopify, and it turns out I had previously linked the Our Story page as my default page template.

So when I removed the content from the thank-you page, it also automatically deleted the content from the Our Story page, because they were using the same default page template.

Unfortunately, I had already clicked save before I realized this, so the original content on the Our Story page was lost. Luckily, I still had the original Our Story page open in another tab. So I asked ChatGPT how I could restore it in the Shopify page builder.

ChatGPT told me to press Option + CMD + U on my Mac to access the source code, and to paste that into the backend of the default page. I did that, but after saving it, my entire Shop All collection page (which is also my main product listing page) was gone and displaying incorrectly… It now looks like the attached screenshot.

Does anyone know what to do?

## Post 2 by suyash1 at 2025-05-31T14:38:16.000Z
@MicalJoseph so you can create a separate template for our story page, say our_story.liquid, copy paste code in this template and then set this template for your page

Will need multiple changes to it to make it work like before but you can have the content

## Post 3 by MicalJoseph at 2025-05-31T14:56:44.000Z
Hi Suyash, thank you for your reply. The thing is that the problem turned into the problem that the collection page is gone due to coding in that section. So I need to have the collection code back - of let’s, say yesterday. Is it possible to reset the website back to how it was this morning or yesterday? We tried to change that in the codes/liquids, but it’s not working.

## Post 4 by suyash1 at 2025-05-31T15:32:14.000Z
@MicalJoseph you can restore the previous versions of the file, please check this link and check if it works for you

## Post 5 by MicalJoseph at 2025-05-31T15:35:24.000Z
Thanks again Suyash, we already tried that, but that’s not working unfortunately..

## Post 6 by suyash1 at 2025-05-31T15:37:36.000Z
@MicalJoseph - can you download other copy of sahara theme? we can make this newly downloaded theme live and customize it carefully

## Post 7 by MicalJoseph at 2025-05-31T16:30:41.000Z
Hi Suyash, yes I downloaden the default theme. But does that mean I need to rebuild everything again?

## Post 8 by suyash1 at 2025-05-31T16:32:42.000Z
@MicalJoseph - you can copy the code from this new theme collection page to previous theme, or make this theme live. But yes, you will need to make changes for collection page
