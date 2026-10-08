URL: https://community.shopify.com/t/code-is-not-being-applied-to-editor-or-preview-anymore/582682
JSON: https://community.shopify.com/t/582682.json
HTTP status: 200
Fetched: 2026-10-03 via curl (Discourse topic JSON)
Title: Code is not being applied to editor or preview anymore
Created: 2026-01-09T10:39:01.196Z
Last posted: 2026-01-10T07:52:12.938Z
Posts: 4  Views: 248
Category id: 211  Tags: [{'id': 4021, 'name': 'troubleshooting', 'slug': 'troubleshooting'}, {'id': 2068, 'name': 'customizations', 'slug': 'customizations'}, {'id': 3921, 'name': 'shopify-themes', 'slug': 'shopify-themes'}, {'id': 5030, 'name': 'shopify-theme', 'slug': 'shopify-theme'}]
Accepted answer: null

---

## Post 1 by gmuletr at 2026-01-09T10:39:01.396Z
Hello I’ll try to describe this as clear as possible because it is quite annoying me and I don’t know where this problem came from!

I’ve been making some changes on my theme over the past 2 weeks, mainly changing the mobile drawer menu design, this is how it ended up looking (luckily I took a screenshot so I can show you)

How it should look, and how it looked with all the changes, before the problem appeared.490×811 53 KB

However 2 days ago I opened the theme editor as usual and everything was strange. Many of the changes I had made to the menu disappeared. In fact, ALL of its changes disappeared and my menu was back to the original version from  2-3 weeks ago before I made any changes.

image1920×894 138 KB

Even a carousel I changed 1 or 2 months ago, which I managed to make it show 2 squares per page in mobile (it’s a custom carousel if I recall correctly, not the standard product one) was “sent back” to some kind of previous version, showing now only 1 image per page and I don’t understand why. Before(correct version)/After(happened because of this whole problem)

image492×542 86 KB

image483×587 73.8 KB

But here’s the surprise: I go into the code to check, and my changes ARE in still in the code. For example, very clearly, the code to remove the images on the menu and change the font style:

image1920×531 29.8 KB

@media (max-width: 768px) {
  /* Hide collection images in mobile menu */
  .mobile-menu .menu-item img, .header-menu .menu-item img, .mega-menu img.collection-image, nav img[class*="collection"],
  .menu-drawer img, .hdt-category-img img {
    display: none !important;
  }

  .hdt-menu-link-text * {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-size: 17px;
  }

And yes before anyone asks, I checked 10 times to see if I’m on the same theme for both the editor and the code.

All of this makes absolutely no sense and I can’t think of any reason why this would happen or how to fix it.

Any ideas?

## Post 2 by tim_tairli at 2026-01-09T11:59:27.085Z
If it were just theme settings I’d probably point at possibility of wrong market selected, but theme code is the same for all markets.

I’d suggest clearing cookies (this will require you to re-login though).

To confirm that you’re looking at the same theme, you can always open Developer tools and look at Shopify.theme variable in console:

Screenshot 2026-01-09 at 10.27.56 PM616×359 26.8 KB

Theme id should be part of the URL in “Edit theme” and “Edit theme code”

Try duplicating your theme and see if the code re-surfaces in new theme copy.

It is also possible that server-side cache went crazy – contact Shopify support and ask them to clear cache.

If this is the case, this can be related – Anyone else seeing wrong images in search engines (Google/Bing) since early December? - CDN cache incoherence

Also – if you have apps installed, Apps may change without you knowing about and add / remove some new CSS on your page.

## Post 3 by Michael-50 at 2026-01-09T12:00:08.311Z
If the code is correct but the editor is wrong, try these steps in order:

Step A: Force a CSS Recompile. Go into your main CSS file ( usually base.css or theme.css ) add a blank space at the bottom, and hit Save. This often forces the Shopify CDN to clear the cache for that theme.

Step B: Toggle a Setting. In the Theme Editor, find a checkbox or a margin slider for the broken section. Change it, hit Save, change it back, and hit Save again. This forces the JSON top “re-marry” the Liquid code.

Step C: Check for Duplicate Sections. Ensure you didn’t accidently create a header-backup.liquid and that the theme is still pointing to the correct file.

## Post 4 by Dan-From-Ryviu at 2026-01-10T07:52:12.938Z
Could you share the link to your store?
