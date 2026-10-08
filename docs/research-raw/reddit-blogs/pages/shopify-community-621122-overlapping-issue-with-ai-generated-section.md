URL: https://community.shopify.com/t/overlapping-issue-with-ai-generated-section/621122
JSON: https://community.shopify.com/t/621122.json
HTTP status: 200
Fetched: 2026-10-03 via curl (Discourse topic JSON)
Title: Overlapping issue with AI-generated section
Created: 2026-05-05T05:38:57.288Z
Last posted: 2026-05-05T06:33:10.020Z
Posts: 6  Views: 78
Category id: 133  Tags: [{'id': 2995, 'name': 'css', 'slug': 'css'}, {'id': 2068, 'name': 'customizations', 'slug': 'customizations'}]
Accepted answer: null

---

## Post 1 by FLMBZ at 2026-05-05T05:38:57.482Z
Hi, I’m using the Shopify Horizon theme and using a custom sticky header (AI-generated section, not the native theme header). I’m running into a stacking issue that I can’t resolve.

When I scroll, page content e(product images, text blocks, sections) are  above the sticky header. Instead of staying behind the header, everything visually overlaps on top of it.

If anyone can help with this I’d really appreciate guidance! Thanks.

## Post 2 by tim_tairli at 2026-05-05T05:40:24.527Z
It’s an AI generated section, how we supposed to diagnose it without slightest idea what it does?

No URL – no help

## Post 3 by FLMBZ at 2026-05-05T05:43:38.119Z
dropped you a message!

## Post 4 by Mustafa_Ali at 2026-05-05T05:52:56.775Z
Hey @FLMBZ Welcome to Shopify Community can you please share the Website URL

## Post 5 by tim_tairli at 2026-05-05T06:00:33.289Z  [ACCEPTED ANSWER]
On your sticky header section in “Theme Edit” go to “Custom CSS” and paste this:

{ z-index: 3; }

The code will apply z-index to entire section.

It’s invalid code outside sections “Custom CSS”, but Shopify will add proper selector automatically if used in sections Custom CSS.

Otherwise, you can use code like this in Theme Settings-> Custom CSS or in your stylesheet:

.shopify-section:has([class^="ai-sticky-header"]) {
  z-index:3;
}

if my post is helpful, please like it via ♡ button and mark as a solution -- this will help others find it

## Post 6 by FLMBZ at 2026-05-05T06:33:10.020Z
tim_tairli:

{ z-index: 3; }

This worked! Thank you for your help!
