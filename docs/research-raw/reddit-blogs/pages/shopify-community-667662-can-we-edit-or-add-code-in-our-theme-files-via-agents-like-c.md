URL: https://community.shopify.com/t/can-we-edit-or-add-code-in-our-theme-files-via-agents-like-cursor-or-claude/667662
JSON: https://community.shopify.com/t/667662.json
HTTP status: 200
Fetched: 2026-10-03 via curl (Discourse topic JSON)
Title: Can we edit or add code in our theme files via agents like Cursor or Claude?
Created: 2026-08-17T21:50:23.526Z
Last posted: 2026-09-19T13:22:10.391Z
Posts: 10  Views: 306
Category id: 133  Tags: [{'id': 1893, 'name': 'design', 'slug': 'design'}, {'id': 2995, 'name': 'css', 'slug': 'css'}, {'id': 2068, 'name': 'customizations', 'slug': 'customizations'}, {'id': 3921, 'name': 'shopify-themes', 'slug': 'shopify-themes'}]
Accepted answer: null

---

## Post 1 by WestStyle-HQ at 2026-08-17T21:50:23.691Z
Hey Community,

Hope everyone is doing well. We just wanna ask if it is possible to edit your website features with Claude or Cursor code. Now, if we want to add or update a filter section to make it cleaner and cooler, can I use Cursor to do it? If yes, then how? Has anyone tried?

Thank You..

## Post 2 by Maximus3 at 2026-08-17T22:14:50.257Z
Yes you can use Cursor to edit a theme. You just need to export, download, and unzip the folder. Then in Cursor open the folder and begin your chat. Then when you’re done, zip the folder and import back into Shopify.

If you don’t want the effort of having to import and check after every edit, you’d have to do something like Nodes.js, Git, and Shopify CLI, but for the normal merchant that is a bit much. I’d just do some editing in Cursor, then import and preview in Shopify.

## Post 3 by New_Dev at 2026-08-17T22:42:39.947Z
Yes, definitely. Cursor or Claude can be very useful for Shopify theme work,

## Post 4 by Ecom_swift_LLC at 2026-08-18T01:39:32.256Z
Hey @WestStyle-HQ! Yes, this works well. Export your theme (Online Store > Themes > Download), unzip it, and open the folder in Cursor or point Claude at it, both can edit the Liquid/CSS/JS directly. A couple tips: duplicate your live theme first so you’re always editing a copy, use Shopify CLI (shopify theme dev) for a live preview while you edit, and run Theme Check before uploading, it catches broken Liquid fast. Once you’re happy, zip it and upload as a new theme (or push via CLI/Git). Way faster than hand-coding a filter section from scratch!

## Post 5 by Khanh-Linh2 at 2026-08-18T08:17:57.671Z
WestStyle-HQ:

Hey Community,

Hope everyone is doing well. We just wanna ask if it is possible to edit your website features with Claude or Cursor code. Now, if we want to add or update a filter section to make it cleaner and cooler, can I use Cursor to do it? If yes, then how? Has anyone tried?

Thank You..

Cursor or Claude definitely can help you to edit your theme code but they don’t do it live on the theme, you need to export zip file in Shopify Admin → Online Store → Themes, then give this to Cursor and provide your requirements, then again, publish the editted theme to Shopify again.

## Post 6 by gotinker at 2026-08-18T15:03:43.437Z
The zip export and re-upload works, but you don’t have to work that way. Pulling the theme locally is a much tighter loop with an agent.

Shopify CLI needs Node 22.12 or newer first. Then shopify theme pull puts the theme in a local folder, and you open that in Cursor or point Claude at it. Run shopify theme dev alongside it: you get a preview at 127.0.0.1:9292 running on your real store data, and it hot reloads CSS and section edits as you save, so you can watch the filter section change while the agent works. It uploads as a development theme, so your live one is untouched.

Two things I’d do before pushing. Run shopify theme check, it catches broken Liquid fast. And push to an unpublished duplicate rather than straight to live: shopify theme push overwrites JSON templates and settings_data.json too, so if anyone has touched the theme editor since you pulled, you’ll quietly revert their work.

One split worth knowing though: which filters exist and what values show up is the Search and Discovery app, driven by your product data. How the filter section actually looks is theme code, so the “cleaner and cooler” part is the bit you’d be doing locally.

## Post 7 by One-Sun1995 at 2026-08-20T06:11:54.530Z
Hey @WestStyle-HQ, yeah, this works fine, you just need the theme on your machine first. Shopify CLI is the bit people miss: run shopify theme pull and it drops the whole theme into a local folder, at which point Cursor or Claude treats it like any other repo. Then shopify theme dev serves a local preview running against your real products and collections, so you can watch the filter change as you edit. When you’re happy, shopify theme push --unpublished puts it on a separate theme you can preview before it goes live, so the published one never gets touched. For filters on Dawn, the files you want are snippets/facets.liquid and assets/component-facets.css.

## Post 8 by Ian_Chechin at 2026-08-23T13:05:46.256Z
Worth adding the other half to this thread: how you get back if the agent breaks something. The editing advice above is solid, the recovery part is where people get hurt.

The fastest rollback is not in the code editor at all: keep the previous theme in your theme list and publish it again. That is seconds, and it takes the whole storefront back at once. Which is also the argument for duplicating before you start, as mentioned above - a duplicate is the only thing that gives you a whole theme to go back to.

Inside the code editor, the Timeline is narrower than people expect: it restores one file at a time, it does not restore a whole theme, it does not bring back files that were deleted, there is no history at all for the assets folder, and the history is finite. So it is a good tool for “this one Liquid file was fine yesterday” and a bad tool for “the agent rewrote fifteen files”.

One more thing that catches people after a correct rollback: sections can come back empty. App blocks and metaobject content do not live in theme files, so restoring the file restores the layout, not what was rendered inside it.

Disclosure: I work on StoreVault, a backup app for Shopify, and those Timeline limits are exactly why we version theme files separately.

## Post 9 by Tim57 at 2026-08-25T00:15:29.155Z
Tim from Sonder Sites in Melbourne. Yes, we do this a lot.

Duplicate the live theme first so you always have a one-click rollback. Pull a copy with Shopify CLI (shopify theme pull), open that folder in Cursor, and run shopify theme dev so you preview against real products before anything goes live. Run Theme Check before you upload. Zip import works for a one-off, but the CLI loop is safer because you see the break before customers do.

If the agent has already published a bad filter or cart change, publish the previous theme immediately, then fix on the copy. That recovery path is the part most Cursor-on-Shopify jobs miss. If you get stuck, happy to help.

## Post 10 by CommerceGov at 2026-09-19T13:22:10.391Z
The unpublished-theme workflow is a good safety boundary, but I think the baseline matters too.

If someone changes the live theme after the agent pulled its copy, an otherwise valid push can quietly overwrite newer production state. So I’d want the reviewed change bound not only to the files being published, but also to the production baseline they were reviewed against.

If that baseline changes before publish, rebase/review before execution.
