URL: https://intercom.help/kiwi-sizing-chart/en/articles/10290960-can-i-use-code-snippets-instead-of-injection-selectors
Final URL: https://intercom.help/kiwi-sizing-chart/en/articles/10290960-can-i-use-code-snippets-instead-of-injection-selectors
HTTP status: 200
Fetched: 2026-10-03 via curl
Meta: {"og:title": "Can I Use Code Snippets Instead of Injection Selectors? | Kiwi Size Chart & Recommender", "og:description": "Learn how to add Kiwi’s size chart using manual snippets or Liquid code, pass product data when the product object isn’t available, and override display settings like link text, modal headers, or display mode.", "twitter:description": "Learn how to add Kiwi’s size chart using manual snippets or Liquid code, pass product data when the product object isn’t available, and override display settings like link text, modal headers, or display mode.", "description": "Learn how to add Kiwi’s size chart using manual snippets or Liquid code, pass product data when the product object isn’t available, and override display settings like link text, modal headers, or display mode."}
Schema dates: 2026-07-02T14:23:28Z

---

Skip to main content

Search for articles...

- All Collections

- FAQs

- Settings

- Can I Use Code Snippets Instead of Injection Selectors?

# Can I Use Code Snippets Instead of Injection Selectors?

Learn how to add Kiwi’s size chart using manual snippets or Liquid code, pass product data when the product object isn’t available, and override display settings like link text, modal headers, or display mode.

July 2, 2026

Table of contents

If you are more familiar with adding code snippets to your theme, Kiwi also supports this option. There are two main ways to do this, depending on your needs.

## 1. Adding Snippet on the Product Page

Because product pages already have the Kiwi snippet installed, our app can identify which size chart belongs to this product. You can simply add the following snippet, and Kiwi will inject the size chart here:

<div id="KiwiSizingChart"></div>

## 2. Adding Snippet with Product Info (Using Liquid)

If you are inserting the snippet in a place where the product info may not be available, for example, on the home page, you need to add the following snippet with Liquid so KiwiSizing knows what the product is and can find the relevant size charts:

<!-- START KiwiSizing code !--> 

 <div id="KiwiSizingChart" 

 data-collections="{{ product.collections | map: 'id' | join: ','}}"

 data-tags="{{ product.tags | join: ',' | escape}}" 

 data-product="{{product.id}}" 

 data-vendor="{{product.vendor | escape}}" 

 data-product-name="{{product.title}}" 

 data-product-images="{{product.images | json| escape}}" 

 data-type="{{product.type | escape}}"> 

</div> 

<!-- END KiwiSizing code !-->

# Q. Can I customize the display settings?

By default, the size chart will be displayed according to the settings in the app. In certain situations, you may want to override these settings. For example, you may want a link above the Add to Cart button but show the size chart inline within the description.

Here are all the options you can pass in to override the settings:

key

Possible values

data-display-mode

0 is inline, 1 is link modal, 2 is button modal

data-link-text

any string

data-modal-header-text

any string

data-modal-sub-header-text

any string

data-layout-type

0 is display both, 1 is display recommender only, 2 is display layout only

data-recommender-display-mode

0 is inline, 1 is link modal, 2 is button modal

data-recommender-has-result-text

any string (use{result} to reference recommended size)

data-recommender-no-result-text

any string

data-recommender-no-input-text

any string

For example, if you want to hardcode the display type, you can pass in data-display-mode:

- 

0 is inline

- 

1 is link modal

- 

2 is button modal

<!-- START KiwiSizing code !--><div id="KiwiSizingChart" data-display-mode="0"></div><!-- END KiwiSizing code !-->

If you want to have different modal header text, subtext, or just the link text, you can pass in data-modal-header-text, data-modal-sub-header-text, and data-link-text, respectively:

<!-- START KiwiSizing code !--><div id="KiwiSizingChart" data-modal-header-text="THIS IS A NEW MODAL HEADER" data-modal-sub-header-text="THIS IS A NEW MODAL SUB HEADER" data-link-text="THIS IS A NEW LINK TEXST"></div><!-- END KiwiSizing code !-->

## Q: Is there a limit to how many snippets I can use per page?

You can put the snippet in as many places as you want on your page; the app will inject size charts into all of them.

## Q: Can I automatically display ALL my size charts on a non-product page (home / collection page)?

No. Kiwi has no setting that auto-loads every published size chart on a page, data-display-mode only controls how a chart displays, not which charts load. On a non-product page you must add the embed snippet (the Liquid version in section 2 above) for each individual size chart you want to show, one snippet per chart/placement.

## Q: My original size chart disappeared after I added a snippet. How do I keep both?

Note that by adding a snippet like this, KiwiSizing will automatically ignore the injection selector and only inject within this snippet container. If you want to keep the regular injection selector and also use a separate snippet to inject the size chart, add the class kiwiAllowRegularInjectionSelector like this:

<div id="KiwiSizingChart" class="kiwiAllowRegularInjectionSelector"></div>

This same class can be added to the liquid snippet as well.

Related Articles

- 
What Is the Difference Between an Ordinary Snippet and an Embedded Snippet?

- 
Can I Display Size Charts on Non-Product Pages?

- 
[Advanced] Dynamically passing product name from Shopify to sizing chart link/button text

- 
Understanding Size Chart Layout and Display Settings in the Kiwi App

- 
My size chart is not showing where I expect. What should I check?

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
