Source URL: https://shopify.dev/changelog/liquid-is-getting-faster-and-ready-to-evolve
Fetched: 2026-10-03 via curl https://shopify.dev/changelog/liquid-is-getting-faster-and-ready-to-evolve.md

---
title: >-
  Stricter Liquid parsing for themes and theme app extensions - Shopify
  developer changelog
description: >-
  Shopify’s developer changelog documents all changes to Shopify’s platform.
  Find the latest news and learn about new platform opportunities.
source_url:
  html: >-
    https://shopify.dev/changelog/posts/liquid-is-getting-faster-and-ready-to-evolve
  md: >-
    https://shopify.dev/changelog/posts/liquid-is-getting-faster-and-ready-to-evolve.md
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
  createdAt: '2026-01-08T13:31:45-05:00'
  postedAt: '2026-01-13T15:00:00-05:00'
  updatedAt: '2026-01-13T17:13:28-05:00'
  effectiveAt: '2026-01-13T15:00:00-05:00'
---

January 13, 2026

# Stricter Liquid parsing for themes and theme app extensions

DateJanuary 13, 2026

FlagsUpdate

SurfacesThemes

Starting January 13, 2026, Shopify is enforcing stricter Liquid parsing for all themes. This improves code quality, prevents syntax errors, and enables future Liquid enhancements.

If your theme contains Liquid code that doesn't meet the stricter parsing requirements, we'll automatically rewrite those files to be compatible. Updated files will include a comment explaining what changed. The rewrite process preserves your theme's functionality and appearance while fixing syntax issues that could cause problems in the future.

If you're developing new themes or theme app extensions, all new submissions to the Theme Store and App Store already require strict-parsable Liquid code. This ensures new code meets the higher quality standards from the start.

View the [migration guide](https://shopify.dev/docs/storefronts/themes/tools/strict-liquid-migration) for detailed information on updating your code.
