URL: https://intercom.help/kiwi-sizing-chart/en/articles/13342634-size-chart-placement-why-the-app-block-is-ignored-and-what-to-do-when-the-chart-is-in-the-wrong-spot
Final URL: https://intercom.help/kiwi-sizing-chart/en/articles/13342634-size-chart-placement-why-the-app-block-is-ignored-and-what-to-do-when-the-chart-is-in-the-wrong-spot
HTTP status: 200
Fetched: 2026-10-03 via curl
Meta: {"og:title": "Size chart placement: why the app block is ignored, and what to do when the chart is in the wrong spot | Kiwi Size Chart & Recommender", "og:description": "Why the Kiwi app block gets ignored, and what to do when the size chart appears in the wrong place on your product page.", "twitter:description": "Why the Kiwi app block gets ignored, and what to do when the size chart appears in the wrong place on your product page.", "description": "Why the Kiwi app block gets ignored, and what to do when the size chart appears in the wrong place on your product page."}
Schema dates: 2026-09-29T03:46:42Z

---

Skip to main content

Search for articles...

- All Collections

- Troubleshooting

- Size Charts

- Size chart placement: why the app block is ignored, and what to do when the chart is in the wrong spot

# Size chart placement: why the app block is ignored, and what to do when the chart is in the wrong spot

Why the Kiwi app block gets ignored, and what to do when the size chart appears in the wrong place on your product page.

Updated this week

Table of contents

This article fixes the two most common size chart placement problems in Kiwi Size Chart & Recommender: the Kiwi Size Chart app block appearing to be ignored, and the chart landing somewhere other than where you want it. By the end you will know which placement method your store is using and how to switch back to the app block.

Who this is for: merchants who have already added the Kiwi Size Chart app block to a product page in the Shopify theme editor and can open Styles & Settings in the Kiwi app.

Custom injection does not depend on your plan; the Sizing Injection Selector is available on every Kiwi plan, including Free.

On theme type: app blocks arrived with Shopify's Online Store 2.0 themes, and the app block is the placement route Kiwi recommends over editing theme code. Online Store 2.0 is the starting indicator, not the confirmation, because Shopify decides app block support per section. The test is in the theme editor: open Online Store → Edit theme, go to the product section you want the chart in, click Add block, and see whether an Apps section appears in the block picker. If it does, that section supports app blocks.

The app block itself isn't plan-gated: it works on every Kiwi plan, and it only needs a Shopify Online Store 2.0 theme. In the block picker, it is called Kiwi Sizing, on the Apps tab, under Kiwi Size Chart & Recommender.

## Why is my Kiwi size chart app block being ignored?

If you have added the Kiwi Size Chart app block to your product page but the size chart does not appear where you placed it, check whether custom injection is set in the Kiwi Dashboard at Styles & Settings → General Settings → Display.

When custom injection is turned on, it takes priority over the app block, and Kiwi will try to place the chart using the selector entered in the Sizing Injection Selector instead of using the app block position.

## How do I switch back to the app block placement?

To make Kiwi use the app block position instead of custom injection, empty the injection selector so no selector is set:

- 

Open the Kiwi app.

- 

Go to Styles & Settings in the left-hand navigation, then the General Settings tab and its Display tab. This is the first page the app lands on.

- 

Under Display Settings, clear the Selector value field of the Sizing Injection Selector, leave it blank.

- 

Save changes.

With no selector in that field, the size chart appears based on where you placed the Kiwi Size Chart app block in the Shopify theme editor.

On that screen, the group is labeled Sizing Injection Selector and sits under Display Settings on the Display tab, below the Enable the app toggle. It has three fields: Position, Selector type, and Selector value. Selector value is the one to read at a glance; a selector in it means custom injection is in play and will take priority over the app block, and an empty field means it is not.

Clear your browser cache and reload the product page after saving; a cached page can keep showing the old placement. With the Selector value empty, the size chart appears as a pop-up link at the position of the Kiwi Size Chart app block; if you haven't moved the block, that is directly above the Add to Cart button. Kiwi resolves placement by custom injection first, then the app block; if neither works, the chart falls back to appearing near the first Add to Cart form on the page.

If the chart still does not appear at the app block position, check that the app block is enabled in the product template you are viewing, that the chart is assigned to that product and template in Kiwi, and that the block or selector targets an element that is actually visible on the page.

## My size chart still isn't in the right spot. What should I do?

If neither the Kiwi Size Chart app block nor custom injection gives you the placement you want, contact the Kiwi support team.

Kiwi support can:

- 

Review your store's theme

- 

Recommend the best placement method

- 

Help adjust settings for your specific layout

Send your theme name and version, plus the product page URL where the chart is landing in the wrong place. Those two are what a placement review starts from.

To reach the team, open the Kiwi Sizing app in your Shopify admin and use the in-app messenger, then choose Send us a message. The full routes are in How to get help from Kiwi Sizing Support.

​

​

Related Articles

- 
How to Move the Size Chart with an Injection Selector (Advanced)

- 
How to Move the Size Chart on Your Product Page (Beginner-Friendly: App Block Method)

- 
My size chart is not showing where I expect. What should I check?

- 
How Kiwi Decides Where to Place the Size Chart (App Block)

- 
Custom Size Chart Placement - Dawn Theme

Did this answer your question?
Disappointed Reaction😞Neutral Reaction😐Smiley Reaction😃

Table of contents

Kiwi Size Chart & Recommender

by Staytuned Digital

Resources

- Community Hub

- More Apps

- Refer & Earn

- Blog
