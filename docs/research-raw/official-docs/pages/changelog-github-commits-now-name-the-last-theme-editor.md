Source URL: https://shopify.dev/changelog/github-commits-now-name-the-last-theme-editor
Fetched: 2026-10-03 via curl https://shopify.dev/changelog/github-commits-now-name-the-last-theme-editor.md

---
title: GitHub commits now name the last theme editor - Shopify developer changelog
description: >-
  Shopify’s developer changelog documents all changes to Shopify’s platform.
  Find the latest news and learn about new platform opportunities.
source_url:
  html: >-
    https://shopify.dev/changelog/posts/github-commits-now-name-the-last-theme-editor
  md: >-
    https://shopify.dev/changelog/posts/github-commits-now-name-the-last-theme-editor.md
metadata:
  effectiveApiVersion: ''
  affectedApi: []
  primaryTag:
    displayName: Themes
    handle: dev_themes
  secondaryTag:
    displayName: Update
    handle: update
  indicatesActionRequired: false
  createdAt: '2026-08-25T13:07:00-04:00'
  postedAt: '2026-08-26T12:00:00-04:00'
  updatedAt: '2026-08-25T19:54:42-04:00'
  effectiveAt: '2026-08-26T12:00:00-04:00'
---

August 26, 2026

# GitHub commits now name the last theme editor

DateAugust 26, 2026

FlagsUpdate

SurfacesThemes

When you edit a theme in the Shopify admin, the commit Shopify pushes to your connected branch now includes the editor's name in the body:

```
Update from Shopify for theme Dawn

Committed from shop: Snowdevil
Theme last edited by: Bob Bobsen
```

The name is plain text in the commit body. The commit author is still the shopify bot, so `git blame` and the commit avatar don't change.

Edits saved within about 10 seconds of each other are batched into one commit, and the body names whoever saved last. If the theme has no recorded editor, the body lists only the shop name, as before.

Learn more about the Shopify GitHub app in our [developer documentation](https://shopify.dev/docs/storefronts/themes/tools/github).
