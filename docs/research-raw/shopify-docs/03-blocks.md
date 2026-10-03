# 03. Blocks: section blocks, theme blocks, app blocks, content_for, render vs include

## https://shopify.dev/docs/storefronts/themes/architecture/blocks
> "There are three types of blocks: Theme blocks: Created as their own Liquid files in the /blocks folder, and re-usable across multiple sections with the theme. Section blocks: Created within a section's Liquid file and are limited to use within that section. App blocks: Provided by apps installed on a merchant's shop."
> "Note: A theme can contain at most 300 theme blocks. Every .liquid file in the theme's /blocks folder counts toward this limit, including AI-generated theme blocks and blocks that aren't currently referenced by any section or template."
> Section block limitations: "They only work in the section they're defined within ... They only support a single level of hierarchy, and cannot be nested. They can not currently be used in the same section as Theme blocks."
> Theme blocks vs snippets: "Theme blocks: Show settings in the theme editor ... Cannot receive variables from parent code. Snippets: ... Accept variables from their parent code Don't show in the theme editor"

## https://shopify.dev/docs/storefronts/themes/architecture/blocks/theme-blocks/schema
> "Theme blocks support the {% schema %} Liquid tag. This tag is used to define the following block attributes and settings: name settings blocks presets tag class"
> "Each block can have only a single {% schema %} tag, which must contain only valid JSON ..."
> "For blocks to be compatible with the theme editor, the top level HTML element must be tagged with the {{ block.shopify_attributes }} Liquid tag. ... Note: Shopify automatically adds this attribute for you when it renders the wrapper around blocks, but when the tag attribute is set to null, you must ensure that the top level HTML element of your block has this attribute"
> Wrapper: `<div id="shopify-block-[id]" class="shopify-block slide">`

## https://shopify.dev/docs/storefronts/themes/architecture/blocks/theme-blocks/quick-start?framework=liquid
> "To accept all theme blocks in a section, add the type @theme to the blocks attribute of the schema of that section." `"blocks": [{ "type": "@theme" }, { "type": "@app" }]`
> "Theme blocks are Liquid files that are defined in the blocks directory of the theme."

## https://shopify.dev/docs/api/liquid/tags/content_for
> "The content_for tag requires a type parameter to differentiate between rendering a number of theme blocks ('blocks') and a single static block ('block')."
> Syntax: `{% content_for 'blocks' %}` and `{% content_for 'block', type: "slide", id: "slide-1" %}`

## https://shopify.dev/docs/storefronts/themes/architecture/blocks/theme-blocks/static-blocks
> Static vs dynamic: static "Cannot be reordered", "Cannot be removed or duplicated", "Can be rendered conditionally or in a for-loop", "Don't count toward the max_blocks limit"; dynamic "Cannot be rendered conditionally or in a for-loop", "Count toward the max_blocks limit".
> "The static: true flag indicates which blocks are statically rendered. Static block IDs are not included in the block_order array"

## https://shopify.dev/docs/storefronts/themes/architecture/blocks/app-blocks
> "If your section is part of a JSON template, then you should support blocks of type @app."
> "Note: Blocks of type @app aren't supported in statically rendered sections."
> "Caution: Blocks of type @app don't accept the limit parameter. Including this will result in an error."
> "When merchants choose to add the app to a new section, Shopify automatically wraps the app block in a wrapper section called Apps. You can customize this wrapper section by your own apps.liquid section."

## render vs include
https://shopify.dev/docs/api/liquid/tags/include
> "Deprecated: Deprecated because the way that variables are handled reduces performance and makes code harder to both read and maintain. The include tag has been replaced by render."
https://shopify.dev/docs/storefronts/themes/best-practices/performance/avoid-nested-renders
> "Don't use include: include is deprecated, and you shouldn't use it anywhere in a theme. Unlike render, include gives the snippet access to the entire parent scope and lets it modify the caller's variables."
> "Inside a for loop, this multiplication becomes significant ... Flattening the nesting to a single level reduces it"

## Developer preview (not GA): {% block %} and {% partial %}
https://shopify.dev/docs/storefronts/themes/getting-started/developer-preview/block
> "Developer preview: To use the {% block %} tag, select Liquid July '26 changes from the available feature previews."
> "Use {% block %} the same way that {% render %} renders a snippet ... {% block 'container' %} renders blocks/container.liquid."
https://shopify.dev/changelog/posts/developer-preview-liquid-block-and-partial-tags (July 21, 2026)
> "{% partial %} defines a named region of server-rendered HTML that JavaScript can refresh without reloading the full page."
> "Existing themes continue to work with sections, theme settings, and JSON templates. This preview adds a Liquid-first composition model alongside the existing theme architecture."

## LiquidDoc (https://shopify.dev/docs/storefronts/themes/tools/liquid-doc)
> "LiquidDoc gives you a way to create a structured interface for Liquid snippets and blocks, allowing you to specify input parameters ..." Tags: "@description", "@param", "@example" inside `{% doc %} ... {% enddoc %}`.
