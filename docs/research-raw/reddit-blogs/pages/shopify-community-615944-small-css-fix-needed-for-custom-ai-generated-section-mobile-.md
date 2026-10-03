URL: https://community.shopify.com/t/small-css-fix-needed-for-custom-ai-generated-section-mobile-clipping-carousel-dots/615944
JSON: https://community.shopify.com/t/615944.json
HTTP status: 200
Fetched: 2026-10-03 via curl (Discourse topic JSON)
Title: Small CSS fix needed for custom AI-generated section, mobile clipping + carousel dots
Created: 2026-05-04T14:38:03.647Z
Last posted: 2026-05-05T05:21:48.104Z
Posts: 9  Views: 106
Category id: 133  Tags: [{'id': 4021, 'name': 'troubleshooting', 'slug': 'troubleshooting'}, {'id': 1893, 'name': 'design', 'slug': 'design'}, {'id': 2995, 'name': 'css', 'slug': 'css'}, {'id': 2068, 'name': 'customizations', 'slug': 'customizations'}, {'id': 4694, 'name': 'html', 'slug': 'html'}]
Accepted answer: null

---

## Post 1 by whimandwise at 2026-05-04T14:38:03.851Z
**Bug 1, Left panel cut off at top on mobile:**The left panel content is clipped at the top on mobile. Likely caused by max-height or overflow: hidden on the section wrapper or left panel. Fix: at max-width: 749px, remove/override max-height and overflow: hidden on both the outer wrapper and left panel so all content is fully visible.

Bug 2, Carousel dots obscuring product title on right panel: The navigation dots are positioned on top of the product title instead of below it. Fix: dots must be in normal document flow (not position: absolute), placed below the product title in this order: image → product title → dots. Add a minimum 8px gap between the title and dots.

## Post 2 by Laza_Binaery at 2026-05-04T14:51:20.216Z
HI @whimandwise

Welcome to the community.

And we are real people  not AI so we do not know what your store is, what page, and what sections you have issues with. So could you clear that out?

And also not sure you already have a fix, probably from ChatGPT or somewhere else, but it does not have an exact CSS selector, the element that you need to target.  So I should not even guess, but here it is

@media screen and (max-width: 749px) {
    .left-panel-selector {
         max-height: none;
         overflow: unset;
    }
}

.dots {
    padding-top: 8px;
    position: relative;
}

Note “.left-panel-selector” and  .dots" selectors you need to replace and find by yourself. Right click in your browser > Click on Inspect and see what sounds like a panel or dots

## Post 3 by Moeed at 2026-05-04T16:29:57.114Z
Hey @whimandwise

Welcome to the community! Like @Laza_Binaery said, we’d need to see your store URL so we can give you something that actually works. Without it, we’d just be guessing and the code probably won’t do what you need.

Drop your store link and we’ll get you sorted!

Best,

Moeed

## Post 4 by Custom-Cursor at 2026-05-04T19:17:39.915Z
Seems like the Post written by Ai. But if you could share your store url and the password as well, then this helps a lot to us, so that we can provide you the solution.

## Post 5 by whimandwise at 2026-05-04T20:33:21.951Z
Whim and Wise
  

  
    

Whim and Wise

  Whim and Wise

  

  
    
    
  

  

PW: loverboy

## Post 6 by whimandwise at 2026-05-04T20:33:51.837Z
I only see the left panel issue happening on mobile view.

## Post 7 by lumine at 2026-05-05T00:26:58.241Z
Pulled up the live store. The section uses hashed class names, for example .ai-top-hits-left-panel-auxpmd0juwhpzzfdxoaigenblockdba7094lqfyx7 (the suffix is unique per block).

The mobile cutoff is from justify-content: center on the left panel. On mobile that centers content vertically, but if the content stack is taller than the panel can size to (with the absolute bg image fighting for height), the headline gets pushed above the top edge.

Try this in your theme’s custom CSS:

@media screen and (max-width: 749px) {
  .ai-top-hits-left-panel-auxpmd0juwhpzzfdxoaigenblockdba7094lqfyx7 {
    justify-content: flex-start;
    min-height: 360px;
  }
}

One caveat: hashed class suffixes like that regenerate when the block is edited, so custom CSS targeting them can break later without warning. If you can, give the wrapper a stable class.

Was this added through Shopify Magic or pasted from somewhere?

## Post 8 by whimandwise at 2026-05-05T02:22:01.387Z
I have been using sidekick to help design the website. Most of it has been pretty smooth, but this one section has been tricky. I will try your fix and see if it solves the issue. Everything else works great except this one bug is something that sidekick could not solve.

## Post 9 by tim_tairli at 2026-05-05T05:21:48.104Z
For the left part you can use this code, ideally in this sections “Custom CSS” setting

@media (max-width:749px) {
  [class^=ai-top-hits-left-panel] {
    padding-top: 35vw;
  }

  [class^=ai-top-hits-left-panel] img {
    object-position: top;
  }
}

Same for the right panel:

[class^=ai-top-hits-product-name] {
  padding-bottom: 20px;
}

Will produce this result:

Screenshot 2026-05-05 at 2.55.39 PM754×563 45.4 KB   and  Screenshot 2026-05-05 at 2.50.37 PM435×861 54.5 KB

if my post is helpful, please like it via ♡ button and mark as a solution -- this will help others find it
