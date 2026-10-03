# 08. Theme app extensions vs custom sections vs metaobjects

## Theme app extensions
https://shopify.dev/docs/apps/build/online-store/theme-app-extensions
> "Theme app extensions allow merchants to easily add dynamic elements to their themes without having to interact with Liquid templates or code." ; "Apps built in the theme app extension framework don't edit theme code, which decreases the risk of introducing breaking changes to the theme"
> Resources: "Blocks ... App blocks App embed blocks ; Assets ... ; Snippets"
https://shopify.dev/docs/apps/build/online-store/theme-app-extensions/configuration
> "For app blocks to function, a theme must contain the following: JSON templates. Sections that support and render blocks of type @app."
> Limits: "All files in a theme app extension 10 MB Enforced / Number of blocks 30 Enforced / ... Size of Liquid across all files 100 KB Enforced / Size of CSS (compressed) referenced directly by the schema 100 KB Suggested / Size of JS (compressed) referenced directly by the schema 10 KB Suggested"
> "Theme app extensions don't have access to the following Liquid objects or properties: The content_for_header object The content_for_index object The content_for_layout object Any properties of the parent section object, other than id."
> "Theme app extension app blocks and app embed blocks can't be rendered on checkout pages."
https://shopify.dev/docs/apps/build/online-store/theme-app-extensions/migrate
> "App embed blocks are inactive until an app user turns them on in the theme editor"
> "Note: Use app blocks if you want apps to automatically point to dynamic sources. App embed blocks only have access to the Global Liquid scope for the page on which they're rendered."
https://shopify.dev/docs/storefronts/themes/os20
> "When an app is uninstalled by a merchant, the app code is removed with it."
Inference (not a Shopify quote): a theme app extension requires building and deploying an app; for a single store's own section, a theme section/theme block is the direct route.

## Dynamic sources and metaobjects
https://shopify.dev/docs/storefronts/themes/architecture/settings/dynamic-sources
> "Dynamic data sources ... allow merchants to connect input settings to data coming from resources such as products, collections, blogs, and pages as well as metafields and metaobjects. Dynamic sources are connected using section and block settings." ; "Note: Dynamic sources aren't available for general theme settings."
https://shopify.dev/docs/storefronts/themes/architecture/blocks/theme-blocks/dynamic-sources
> Theme block sources: "Template ... Section ... Block ... Liquid A resource drop passed to blocks explicitly in Liquid to the content_for tag."
https://shopify.dev/docs/api/liquid/objects/metaobject
> "{{ metaobjects.type.handle }}" ; "When the publishable capability is enabled, a metaobject can only be accessed if its status is active. If its status is draft, then the return value is nil."
https://shopify.dev/docs/storefronts/themes/architecture/settings/input-settings (metaobject_list): custom metaobject definitions "require the metaobject definition to already exist" and are "not allowed in themes listed on the Theme Store".
https://shopify.dev/docs/storefronts/themes/architecture/templates/metaobject: metaobject templates need the "onlineStore capability"; "Any sections that are available for any template or section group are included in metaobject templates by default."
