Source URL: https://shopify.dev/docs/storefronts/themes/architecture/limits
Fetched: 2026-10-03 via curl https://shopify.dev/docs/storefronts/themes/architecture/limits.md (HTTP 200, markdown)

---
title: Theme limits
description: >-
  A consolidated reference of the platform limits that apply to Online Store
  themes, including template, section, block, file, and naming limits.
source_url:
  html: 'https://shopify.dev/docs/storefronts/themes/architecture/limits'
  md: 'https://shopify.dev/docs/storefronts/themes/architecture/limits.md'
api_name: liquid
---

# Theme limits

Themes are subject to platform limits that control how many templates, sections, and blocks a theme can contain, and how large its files can be. This page consolidates those limits in one place. Individual limits are also documented on the relevant architecture pages, which are linked throughout.

Attempting to exceed a limit results in an error, either in the theme editor or when the theme is saved, uploaded, or synced with the [Shopify CLI](https://shopify.dev/docs/storefronts/themes/tools/cli).

***

## Templates

| Limit | Value |
| - | - |
| [JSON templates](https://shopify.dev/docs/storefronts/themes/architecture/templates/json-templates) per theme | 1,000 |
| Sections per JSON template | 25 |

***

## Section groups

| Limit | Value |
| - | - |
| [Section groups](https://shopify.dev/docs/storefronts/themes/architecture/section-groups) per theme | 20 |
| Sections per section group | 25 |

***

## Sections and blocks

For more information about how sections and blocks are structured, refer to [Sections](https://shopify.dev/docs/storefronts/themes/architecture/sections) and [Blocks](https://shopify.dev/docs/storefronts/themes/architecture/blocks).

| Limit | Value |
| - | - |
| Blocks per section | 50 (you can reduce this limit with [`max_blocks`](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema#max_blocks)) |
| Blocks per JSON template or section group | 1,250 |
| [Theme block](https://shopify.dev/docs/storefronts/themes/architecture/blocks/theme-blocks) nesting depth | 8 levels, excluding the section level |
| Theme block files (`blocks/` folder) per theme | 300 |

The per-section and per-template block limits apply to blocks that merchants can add, remove, or reorder, including [app blocks](https://shopify.dev/docs/storefronts/themes/architecture/blocks/app-blocks) and [theme blocks](https://shopify.dev/docs/storefronts/themes/architecture/blocks/theme-blocks). [Statically rendered blocks](https://shopify.dev/docs/storefronts/themes/architecture/blocks/theme-blocks/static-blocks) added with `{% content_for %}` don't count toward these limits.

***

## File and content size limits

The following limits apply to individual files within a theme:

| File | Maximum size |
| - | - |
| JSON template file | 512 KB |
| Section group file | 512 KB |
| [`settings_schema.json`](https://shopify.dev/docs/storefronts/themes/architecture/config/settings-schema-json) | 512 KB |
| [`settings_data.json`](https://shopify.dev/docs/storefronts/themes/architecture/config/settings-data-json) | 1.5 MB |
| [Locale files](https://shopify.dev/docs/storefronts/themes/architecture/locales) | 1.5 MB |
| Other Liquid files (sections, snippets, layouts) | 256 KB |
| Content in a single [`liquid` setting](https://shopify.dev/docs/storefronts/themes/architecture/settings/input-settings#liquid) | 50 KB |

The following limits apply to a theme as a whole:

| Limit | Value |
| - | - |
| Uploaded theme package (compressed) | 50 MB |
| Total code (all files except assets) | 250 MB |
| Files per theme | 100,000 |

***

## Naming

| Limit | Value |
| - | - |
| Theme name | 50 characters |
| Section and block schema `name` attribute | 25 characters |
| Custom section and block names (set by merchants in the theme editor) | 100 characters |

***

## Theme app extensions

Apps that extend themes through [theme app extensions](https://shopify.dev/docs/apps/build/online-store/theme-app-extensions) have their own separate file and content size limits. Refer to [Theme app extension configuration](https://shopify.dev/docs/apps/build/online-store/theme-app-extensions/configuration#file-and-content-size-limits) for details.

***
