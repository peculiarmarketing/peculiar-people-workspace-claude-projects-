URL: https://community.shopify.com/t/how-to-update-your-shopify-theme-without-losing-your-custom-code/686447
JSON: https://community.shopify.com/t/686447.json
HTTP status: 200
Fetched: 2026-10-03 via curl (Discourse topic JSON)
Title: How to update your Shopify theme without losing your custom code
Created: 2026-09-22T19:59:54.682Z
Last posted: 2026-09-28T12:20:46.424Z
Posts: 10  Views: 218
Category id: 133  Tags: [{'id': 4021, 'name': 'troubleshooting', 'slug': 'troubleshooting'}, {'id': 1893, 'name': 'design', 'slug': 'design'}, {'id': 2068, 'name': 'customizations', 'slug': 'customizations'}, {'id': 3921, 'name': 'shopify-themes', 'slug': 'shopify-themes'}, {'id': 4770, 'name': 'shop-performance', 'slug': 'shop-performance'}]
Accepted answer: null

---

## Post 1 by Moeed at 2026-09-22T19:59:54.880Z
This one comes up constantly. Dawn user here, same thing again, someone stuck on Sense 2.0. Two of those never got an answer.

The situation is always the same. There is an update sitting there, and you know somebody put custom code in your theme at some point. Maybe you did it, maybe a developer did two years ago, maybe an app did it without telling you. So you never press the button. I still open stores running versions from three years back for exactly this reason.

Most of what you are scared of losing is not actually at risk.

What survives, guaranteed

Everything you did in the theme editor comes across. Shopify lists it out: theme settings, page layouts, sections and blocks you added or reordered or hid, all their settings and images and text, templates you created, app embeds and their settings, and wording changed in the content editor.

Two code folders are protected too: Templates, and settings_data.json in Config.

That covers most of what most stores have. If nobody has ever opened your code editor, go take the update.

What is at risk

Only manual edits to theme code files. theme.liquid, a section or snippet the theme shipped with, the theme’s own CSS and JS.

Plus anything an app pasted into those files on your behalf, which is what catches people out. You know you never edited anything, and you have forgotten that Loox or Judge_me went in there at install.

Shopify tells you whether your code made it

This is missing from nearly every guide on this topic.

The update goes into your Draft themes, not your live site. Then a message appears on that theme card saying one of two things:

- “Theme added: code edits successfully included”

- “Theme added: code edits could not be included”

No guessing. Shopify checks whether your edits conflicted and just tells you, before anything goes live.

A conflict means you and the theme developer both changed the same file. If you edited the product section and their update also rewrote it, that is a conflict. If they left it alone, your edit rides along.

Finding what is actually customised

Old threads will tell you Shopify marks every edited file with a dot. That used to be true, and it is not anymore. In the new code editor a dot means unsaved changes on that tab, nothing else. If you find that tip somewhere, ignore it.

What actually works now:

Timeline. Open a file in the code editor and check the Timeline panel on the left. A file nobody has touched shows only its original entry. Good for checking a file you suspect, painful for scanning a whole theme.

Diff against the official version. Download your theme (Themes, three dots, Download theme file) and compare it against a clean copy of the same theme. Dawn and Horizon are both published on GitHub, so for free themes this costs nothing and gives you an exact list.

Diff apps. Apps in the App Store do the comparison for you and list what changed. Usually the realistic route on a paid theme.

Whichever you use, copy the custom bits into a text file first, with a note on which file each came from.

The process

- Duplicate your live theme. Three dots, Duplicate. That is your rollback.

- Find your customisations with the dot trick, copy them out.

- Read the release notes. If they rewrote the product section and your code is in the product section, you already know what is coming.

- Click the update notification, then Add to draft themes. Older threads call this “Add to theme library”, same thing, Shopify renamed it.

- Check the message on the new card. It will be prefixed “Updated copy of”.

- Preview properly. Product page, collection, cart, and whatever custom thing you paid someone to build. Then check it on a phone.

- Paste back anything dropped, preview again, publish.

image829×150 15 KB

Stop this happening next time

The more of your code lives in files the theme does not ship, the less there is to conflict with. A file that only exists in your theme has nothing to disagree with it.

So: a section called custom-size-chart.liquid instead of editing theirs. A custom.css in Assets with one line in theme.liquid to load it:

{{ 'custom.css' | asset_url | stylesheet_tag }}

Now your styles sit somewhere an update cannot touch, and the only thing inside a theme file is that one line.

Two things to avoid. Adding custom settings to config/settings_schema.json, because those collide with new theme settings. And app code pasted into theme files, when the app offers an app block or app embed instead, which lives outside your theme entirely.

One catch Shopify flags: if your custom CSS targets the theme’s class names, check those still exist after the update. Your file survived, but what it was pointing at may have been renamed.

A few cases where none of this applies

- Uploaded themes get no updates. Theme Store installs only. A theme you bought for a different store is unlicensed here and has to be re-purchased.

- No “Add to draft themes” option means the standard path is closed. Install fresh from the Theme Store and reapply manually.

- Vintage themes are sunset. That is a migration conversation, not an update one.

- Automated updates are bug and security fixes only. Shopify states they do not change your look and feel, content or settings.

If you already lost it

Your old version is almost certainly still in your theme library, because the update is added as a new theme rather than replacing the old one. Open it, pull the files you need, copy your code back out.

If you are sitting on an update you have been avoiding, reply with your theme and what has been customized, and I will tell you what to watch for.

Cheers,

Moeed

## Post 2 by Rohail_Ali_12 at 2026-09-23T00:17:25.323Z
Hi @Moeed ,

I hope you are having a great day, and thank you so much for sharing such a detailed guide on this.

You’re absolutely right that importing custom code into a new version of a theme can take quite a bit of time. I have experienced this myself, and in some cases, it has taken me several hours to migrate custom code for a client.

However, adding custom code is sometimes necessary to fulfill the store’s specific requirements. That’s why I make sure to properly document all custom code that I add. This makes it much easier for future developers to locate the code and make updates or adjustments as needed.

Best Regards,

Rohail

## Post 3 by vividusdesigns at 2026-09-23T09:23:34.483Z
A safe update flow is: duplicate the live theme first, then use the update banner in Online Store > Themes to add the new version to your theme library. Compare the old and new code, and reapply only documented edits in files such as `theme.liquid`, section files, snippets, and `assets/custom.css`; avoid changing `config/settings_schema.json` unless you know why. App blocks and app embeds usually reconnect, but pasted app code may need to be added again. Test the preview, cart, checkout, and key app flows before publishing, and keep the old theme as a rollback.

## Post 4 by optima-tiktok-shop1 at 2026-09-23T10:05:30.149Z
One more way to get an exact list of custom files: connect the theme to a private GitHub repo (Online Store > Themes > Add theme > Connect from GitHub) before you run the update. Shopify then commits each code-editor save, so the commit history shows precisely which files were hand-edited. Use that as your migration list.

Also keep the old theme in Theme library after publishing the draft rather than deleting it. It can be republished in two clicks if the update breaks something, which is faster than restoring a downloaded zip.

App embeds and app blocks carry over with settings_data.json, but code an app pasted into theme.liquid or a snippet has to be re-added if that file conflicted.

## Post 5 by IFGeCommerce at 2026-09-23T10:58:14.638Z
My name is Francesco Guiducci and I’m the founder of IFG eCommerce.

One correction I’d make to the process because it could otherwise confuse someone following the guide step by step.

Earlier in the post you correctly explain that the old “dot trick” no longer identifies files that were historically edited. In Shopify’s current code editor, that dot is not a reliable way to inventory previous customizations.

So I would change step 2 from “find your customisations with the dot trick” to something closer to: identify suspected custom files through Timeline where history is available, and compare the current theme against a clean copy of the same theme/version when you need a complete inventory.

There is another distinction I think is worth making clear.

The “code edits successfully included” message tells you that Shopify was able to carry those edits into the updated theme. It does not guarantee that the customization still behaves correctly with the new version.

A CSS file can transfer perfectly while the selector it targets has changed. The same applies to JavaScript that depends on markup the theme developer modified, or Liquid logic that interacts with a section whose schema or surrounding structure changed.

So I treat the update status as the merge check, and the preview as the regression check.

After the update I would specifically test the product page, collection page, cart, navigation, variant selection, app blocks and every custom component that matters to the store, on both desktop and mobile.

That small distinction is important because “the code survived the update” and “the customization survived the update” are not necessarily the same thing.

## Post 6 by ahsandoesntcare at 2026-09-24T11:02:54.513Z
One thing worth adding to the survivor list: app embeds are enabled per theme copy, so if one gets toggled on in the old theme after the update draft is created, it may not carry over. Open the draft’s Theme settings > App embeds and compare against the live theme before publishing.

For the pasted-code case, use the code editor search for the app’s domain (loox, judge.me, klaviyo) or for `<script src` inside theme.liquid, header/footer snippets, and the cart templates. That produces your re-add list in minutes. Many apps now offer an app embed instead, so switching removes the paste permanently. Save a copy of anything you strip out and retest that app after publishing.

## Post 7 by One-Sun1995 at 2026-09-24T11:21:03.581Z
Hey @Moeed, one thing missing from that list: the update button only exists for themes you got from the Shopify Theme Store. Vintage ones like Debut, Brooklyn, Supply and Motion, plus anything bought outside the store or uploaded as a copy, have no update path at all, so those are a fresh install with the code re-applied by hand. If a theme card in Online Store > Themes shows no update prompt, that’s usually why. And yes, the new version lands in Draft themes as “Updated copy of …”, so preview it there and read the code-edits line on that card before you hit publish.

## Post 8 by Moeed at 2026-09-24T11:33:03.254Z
Moeed:

- Uploaded themes get no updates. Theme Store installs only. A theme you bought for a different store is unlicensed here and has to be re-purchased.

@One-Sun1995 Maybe read the post properly first?

## Post 9 by One-Sun1995 at 2026-09-25T07:48:45.666Z
Hey @Moeed, the vintage themes are the gap. Debut, Brooklyn, Supply and Motion were all Theme Store installs and they still get no update button, because Shopify retired that generation and stopped publishing new versions of them. So being a Theme Store theme on its own tells you nothing about whether an update exists. Check the theme card in Online Store > Themes: no update prompt there means a retired theme, and moving off it is a fresh install with the custom code re-applied by hand.

## Post 10 by LiquifyAI at 2026-09-28T12:20:46.424Z
This post was flagged by the community and is temporarily hidden.
