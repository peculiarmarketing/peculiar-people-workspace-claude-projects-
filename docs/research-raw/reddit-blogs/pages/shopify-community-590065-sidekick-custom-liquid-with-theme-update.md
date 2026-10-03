URL: https://community.shopify.com/t/sidekick-custom-liquid-with-theme-update/590065
JSON: https://community.shopify.com/t/590065.json
HTTP status: 200
Fetched: 2026-10-03 via curl (Discourse topic JSON)
Title: Sidekick & custom liquid with theme update
Created: 2026-02-27T00:20:44.706Z
Last posted: 2026-09-17T09:12:07.519Z
Posts: 4  Views: 352
Category id: 317  Tags: []
Accepted answer: null

---

## Post 1 by Brad_Goldberg at 2026-02-27T00:20:44.818Z
Can sidekick track liquid file edits and maintain the custom liquid after a theme update?

## Post 2 by mkoenig at 2026-03-03T18:21:05.751Z
Hi Brad! Quick clarifying question here - you mean for AI blocks generated with Sidekick, can Sidekick update these after a theme update? If that’s the question then yes, blocks generated with Sidekick don’t take you off the upgrade path for your theme.

## Post 3 by Brad_Goldberg at 2026-03-05T00:07:57.000Z
Hi. I’m looking for a better way of tracking and maintaining liquid changes to existing theme sections (not sidekick created) and was wondering if sidekick can assist with this.

Thank you,

Brad

## Post 4 by Ian_Chechin at 2026-09-17T09:12:07.519Z
Sidekick will not do that for edits it did not make, and nothing else in the admin does either. The code editor marks changed templates with a dot, but not assets, and the marks do not survive duplicating the theme, which most people do right before an update.

What works is boring: a versioned copy of the theme files, taken on a schedule, so any two versions can be compared file by file. Then “which liquid did we change” is a list, not a memory exercise, and after an update you re-apply exactly those files instead of hunting through three hundred.

Keep custom code in its own snippets and sections wherever you can, since those carry across updates untouched. Edits inside the theme’s own files are the ones that need the list.

StoreVault, which I build, keeps daily versions of every theme file and shows what changed between any two. Since 8 September it also writes files back into the same theme when an update or an app breaks something, with a plan naming each file before anything is written. It never creates or publishes a theme; that part stays yours.
