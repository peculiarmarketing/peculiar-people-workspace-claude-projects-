Source URL: https://shopify.dev/docs/apps/build/online-store/theme-app-extensions
Fetched: 2026-10-03 via curl https://shopify.dev/docs/apps/build/online-store/theme-app-extensions.md (HTTP 200, markdown)

---
title: About theme app extensions
description: Create theme extensions for apps that integrate with online stores.
source_url:
  html: 'https://shopify.dev/docs/apps/build/online-store/theme-app-extensions'
  md: 'https://shopify.dev/docs/apps/build/online-store/theme-app-extensions.md'
---

# About theme app extensions

Theme app extensions allow merchants to easily add dynamic elements to their themes without having to interact with Liquid templates or code. For example, dynamic elements can include product reviews, prices, ratings, or interactive 3D models of products. Theme app extensions can integrate with Online Store 2.0 themes.

***

## Benefits of using theme app extensions

* Theme app extensions automatically expose your app in the theme editor. You can leverage the editor’s visual editing capabilities without needing to replicate them in your app.
* You can deploy your app at the same time to all online stores that use it. You also have access to [versioning](https://shopify.dev/docs/apps/build/app-extensions#versioning-and-deployment), and [asset hosting on the Shopify CDN](https://shopify.dev/docs/apps/build/online-store/theme-app-extensions/configuration#performance).
* A single set of integration logic and instructions works for all themes.
* Merchants won't need to manually edit their theme code.

***

## Theme app extensions resources

Theme app extensions contain the following resources:

* Blocks - Liquid files that act as the entry point for what you want to inject in a theme. The following block types are supported:

  * [App blocks](https://shopify.dev/docs/apps/build/online-store/theme-app-extensions/configuration#app-blocks-for-themes)
  * [App embed blocks](https://shopify.dev/docs/apps/build/online-store/theme-app-extensions/configuration#app-embed-blocks)

* Assets - CSS, JavaScript, and other static app content that gets injected into themes.

* Snippets - Reusable Liquid snippets that can be used across multiple blocks.

  Learn more about the [theme app extensions framework](https://shopify.dev/docs/apps/build/online-store/theme-app-extensions/configuration).

***

## Designing for the best merchant experience

Apps built in the theme app extension framework don't edit theme code, which decreases the risk of introducing breaking changes to the theme, makes it easier to iterate on the content of the integration, and provides for a better merchant experience.

Merchants can use the [theme editor](https://shopify.dev/docs/storefronts/themes/tools/online-editor) to configure exposed settings and add app blocks in theme sections for precise positioning in a page's layout.

***

## Resources

[Dawn\
\
](https://github.com/Shopify/dawn)

[Explore Shopify's Online Store 2.0 reference theme, built to support app blocks.](https://github.com/Shopify/dawn)

[Shopify CLI\
\
](https://shopify.dev/docs/apps/build/cli-for-apps)

[Learn about Shopify CLI, which is used for creating and registering theme app extensions and for version control.](https://shopify.dev/docs/apps/build/cli-for-apps)

***

## Next steps

* [Get started with theme app extensions](https://shopify.dev/docs/apps/build/online-store/theme-app-extensions/build)
* [Review the theme app extensions framework](https://shopify.dev/docs/apps/build/online-store/theme-app-extensions/configuration)
* [Understand the UX guidelines for theme app extensions](https://shopify.dev/docs/apps/build/online-store/theme-app-extensions/ux)

***
