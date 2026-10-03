# 11. Shopify AI features for themes; 12. Online Store editor, previews, versions

## AI generated theme blocks: https://shopify.dev/docs/storefronts/themes/architecture/blocks/ai-generated-theme-blocks
> "In the theme editor, merchants can generate theme blocks in existing sections that support theme blocks."
> "To make it possible for a section to accept AI generated blocks, it must accept theme blocks. To accept all theme blocks in a section, add the type @theme to the blocks attribute"
> "Shopify automatically wraps the generated block in a wrapper section called _blocks.liquid. You can override and customize this wrapper section by adding your own _blocks.liquid section to your theme."
> "The _blocks.liquid section isn't a standard theme section. It can't be manually rendered ... and it won't show up in the theme editor for merchants to add to pages."
> Custom _blocks.liquid must: "Define @theme and @app as block types Define presets Define {% content_for blocks %} Does not define the templates attribute, including within disabled_on and enabled_on"
https://shopify.dev/docs/storefronts/themes/architecture/blocks
> "Shopify themes can be extended with custom blocks generated using Sidekick, directly within the theme editor (for eligible merchants). ... Sidekick generates the corresponding Liquid code, including the necessary HTML structure, potential CSS/JavaScript, and the JSON schema definition. From a developer perspective, these AI-generated blocks are theme blocks. They are stored in the /blocks folder"
> 300 theme block file cap includes AI-generated blocks.
Changelog (WebSearch snippet, not fetched): https://changelog.shopify.com/posts/ai-block-generation-for-all-theme-store-themes : "AI block generation, powered by Sidekick, now works with every theme from the Shopify Theme Store, not just Horizon themes." Also https://changelog.shopify.com/posts/generate-theme-blocks-with-shopify-magic (title only).
Help Center (WebSearch snippet, not fetched): https://help.shopify.com/en/manual/online-store/themes/customizing-themes/theme-editor/shopify-magic/generate-blocks : "click Add block and then Generate ... Prompts should be a minimum of five words long".
Third-party claims (NOT official, unverified): generated blocks may hardcode values instead of exposing schema settings and may not match brand styling (gempages.net blog).

## Theme editor / versions / previews
- Development themes: see 05-cli.md ("don't count toward your theme limit ... deleted ... after seven days of inactivity").
- `shopify theme share`: new unpublished theme with randomized name and preview link.
- `shopify theme push --unpublished`: new unpublished theme.
- Theme limit (WebSearch snippet of https://help.shopify.com/en/manual/online-store/themes/adding-themes, not fetched): "Stores and organizations on the Basic, Grow, and Advanced plans can add up to 20 themes ... Shopify Plus plan can add up to 100 themes."
- File rollback (WebSearch snippet of https://help.shopify.com/en/manual/online-store/extend/theme-code, not fetched): code editor, click "Older versions" next to a .liquid file name and pick a datestamp to roll back that file. Per-file only. No whole-theme version history was confirmed in official docs; whole-theme rollback = duplicate before editing, or GitHub integration history.
- Theme editor live text preview rules: https://shopify.dev/docs/storefronts/themes/tools/online-editor (see 02).
