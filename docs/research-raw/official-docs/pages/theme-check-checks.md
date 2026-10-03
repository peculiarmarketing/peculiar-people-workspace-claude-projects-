Source URL: https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks
Fetched: 2026-10-03 via curl https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks.md (HTTP 200, markdown)

---
title: Checks reference
description: 'Learn about the checks that you can run in Theme Check, and what they mean.'
source_url:
  html: 'https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks'
  md: 'https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks.md'
api_name: liquid
---

# Checks reference

You can run the following checks as part of Theme Check. Each check identifies a specific error or a place in your code where a best practice is not being followed.

To learn more about the check and its options, click on the name of the check.

***

## Liquid file checks

These checks analyze the style and validity of Liquid code. Some of these checks support auto-correction using the `--auto-correct` flag.

| Check | Severity | Purpose | Auto-correction |
| - | - | - | - |
| [AppBlockValidTags](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/app-block-valid-tags) | Error | Identifies forbidden Liquid tags in theme app extension app block and app embed block code. | |
| [AssetPreload](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/asset-preload) | Warning | Encourages preloading of assets using Liquid filters, rather than HTML attributes. | |
| [AssetSizeAppBlockCSS](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/app-block-valid-tags) | Error | Prevents theme app extensions from using CSS files larger than the configured threshold. | |
| [AssetSizeAppBlockJavascript](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/app-block-valid-tags) | Error | Prevents theme app extensions from using JavaScript files and external scripts with a compressed size larger than the configured threshold. | |
| [AssetSizeCSS](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/asset-size-css) | Error | Prevents themes from using CSS files larger than the configured threshold. | |
| [AssetSizeJavaScript](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/asset-size-javascript) | Error | Prevents using theme JavaScript files and external scripts with a compressed size greater than the configured threshold. | |
| [BlockIdUsage](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/block-id-usage) | Warning | Warns against the use of block IDs in conditional statements and case statements. | |
| [CdnPreconnect](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/cdn-preconnect) | Warning | This check is aimed at signaling the redundant preconnect to Shopify's CDN. | |
| [ContentForHeaderModification](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/cdn-preconnect) | Error | Identifies code that tries to parse `content_for_header` . | |
| [DeprecateBgsizes](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/deprecate-bgsizes) | Warning | Discourages use of the bgset extension instead of the image-set attribute for loading background images. | |
| [DeprecateLazysizes](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/deprecate-lazysizes) | Warning | Discourages use of the lazysizes library for lazy loading images, iframes, and scripts. | |
| [DeprecatedFilter](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/deprecated-filter) | Warning | Discourages using deprecated filters in themes. | Yes |
| [DeprecatedFontsOnSectionsAndBlocks](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/deprecated-fonts-on-sections-and-blocks) | Warning | Discourages using deprecated fonts in section and block schemas. | |
| [DeprecatedFontsOnSettingsData](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/deprecated-fonts-on-settings-data) | Warning | Discourages using deprecated fonts in the `config/settings_data.json` file. | |
| [DeprecatedFontsOnSettingsSchema](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/deprecated-fonts-on-settings-schema) | Warning | Discourages using deprecated fonts in the `settings_schema.json` file. | |
| [DeprecatedTag](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/deprecated-tag) | Error | Discourages using deprecated tags in themes. | |
| [DuplicateContentForArguments](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/duplicate-content-for-arguments) | Warning | Identifies when argument names provided for the `content_for` tag are not unique. | |
| [DuplicateRenderSnippetArguments](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/duplicate-render-snippet-arguments) | Warning | Identifies when argument names provided for the `render` tag are not unique. | |
| [EmptyBlockContent](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/empty-block-content) | Warning | Detects instances where the Liquid tag `{% content_for 'blocks' %}` is used when the associated schema `blocks` array is empty or undefined. | |
| [ExcessiveSettingsCount](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/excessive-settings-count) | Warning | Identifies section or block schemas that declare more top-level settings than the configured maximum. | |
| [HardcodedRoutes](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/hardcoded-routes) | Warning | Encourages use of the routes object instead of hardcoding URLs. | |
| [ImgWidthAndHeight](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/img-lazy-loading) | Error | Enforces setting the `width` and `height` attributes on `img` tags. | |
| [LiquidComplexity](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/liquid-complexity) | Warning | Identifies Liquid files with high cyclomatic complexity. | |
| [LiquidFreeSettings](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/liquid-free-settings) | Warning | Identifies when a theme is using the `{% liquid %}` tag within `Settings` values. | |
| [LiquidHTMLSyntaxError](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/liquid-html-syntax-error) | Error | Identifies Liquid and HTML syntax errors. | |
| [LiquidNestingDepth](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/liquid-nesting-depth) | Warning | Identifies Liquid files with deeply nested control-flow structures. | |
| [LiquidSyntaxError](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/liquid-syntax-error) | Error | Identifies Liquid syntax errors. | |
| [MaxFileSize](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/max-file-size) | Error | Identifies theme files that exceed Shopify's maximum file size. | |
| [MissingAsset](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/missing-asset) | Error | Makes sure that all asset files referenced by the `asset_url` filter exist. | |
| [AppBlockMissingSchema](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/app-block-missing-schema) | Error | Ensures schema is present in app blocks in theme app extensions. | |
| [MissingContentForArguments](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/missing-content-for-arguments) | Warning | Identifies when required arguments are not provided when using a `content_for` tag. | |
| [MissingRenderSnippetArguments](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/missing-render-snippet-arguments) | Warning | Identifies when required arguments are not provided when using a `render` tag. | |
| [MissingTemplate](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/missing-asset) | Warning | Identifies when a resource is referenced using a `render` , `section` , or `include` tag, but doesn't exist. | Yes |
| [OrphanedSnippet](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/orphaned-snippet) | Warning | Identifies snippets that exist but are never referenced or rendered in the theme. | |
| [PaginationSize](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/pagination-size) | Warning | Ensures that objects are paginated with performant sizes so too many objects are not loaded at once. | |
| [ParserBlockingScript](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/parser-blocking-javascript) | Error | Identifies script tags that don't have defer or async attributes, avoiding parser-blocking JavaScript. | |
| [RemoteAsset](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/remote-asset) | Warning | Discourages use of third party domains for hosting assets. | |
| [RequiredLayoutThemeObject](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/required-layout-theme-object) | Error | Makes sure that the theme.liquid layout file contains the required `{{ content_for_header }}` and `{{ content_for_layout }}` objects. | Yes |
| [ReservedDocParamNames](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/reserved-doc-param-names) | Error | Identifies when a LiquidDoc parameter in a block file reuses a name reserved for the `content_for` tag. | |
| [SchemaPresetsBlockOrder](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/schema-presets-block-order) | Warning | Makes sure that the section and block schema presets are correctly used in the `block_order`. | |
| [SchemaPresetsStaticBlocks](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/schema-presets-static-blocks) | Error | Warns if a preset static block doesn't have a `{% content_for "block" ... %}` tag in the Liquid code. | |
| [StaticStylesheetAndJavascriptTags](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/static-stylesheet-and-javascript-tags) | Error | Warns if Liquid code is used inside a `{% stylesheet %}` or `{% javascript %}` tag. | |
| [TranslationKeyExists](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/translation-key-exists) | Error | Identifies references to translations that don't exist. | |
| [UnclosedHTMLElement](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/unclosed-html-element) | Error | Identifies instances of unclosed HTML elements in branching code. | |
| [UndefinedObject](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/undefined-object) | Error | Identifies references to undefined Liquid objects. | |
| [UniqueStaticBlockId](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/unique-static-block-id) | Error | Identifies when two static blocks are using the same ID. | |
| [UnknownFilter](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/unknown-filter) | Error | Identifies references to unknown Liquid filters. | |
| [UnusedAssign](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/unused-assign) | Warning | Identifies variable definitions that aren't used. | |
| [UniqueDocParamNames](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/unique-doc-param-names) | Error | Identifies when parameter names in LiquidDoc are not unique. | |
| [UnrecognizedContentForArguments](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/unrecognized-content-for-arguments) | Warning | Identifies when unknown arguments for a static block are provided when using a `content_for` tag. | |
| [UnrecognizedRenderSnippetArguments](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/unrecognized-render-snippet-arguments) | Warning | Identifies when unknown arguments for a snippet are provided when using a `render` tag. | |
| [UnsupportedDocTag](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/unsupported-doc-tag) | Error | Identifies when LiquidDoc tag is used outside of snippets. | |
| [UnsupportedFilterArguments](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/unsupported-filter-arguments) | Error | Identifies when Liquid filters are applied to arguments passed to a `render`, `include`, or `content_for` tag. | |
| [UnusedDocParam](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/unused-doc-param) | Warning | Identifies when parameters are defined within LiquidDoc, but are not used within the snippet. | |
| [ValidBlockTarget](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/valid-block-target) | Error | Identifies when a block is using an invalid target. | |
| [ValidContentForArguments](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/valid-content-for-arguments) | Error | Identifies invalid arguments passed to the `{% content_for %}` tag | |
| [ValidContentForArgumentTypes](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/valid-content-for-argument-types) | Warning | Identifies when arguments are provided when using a `content_for` tag, but the types of the arguments don't match the type defined in the block's LiquidDoc. | |
| [ValidDocParamTypes](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/valid-doc-param-types) | Error | Identifies when invalid parameter types exist in LiquidDoc. | |
| [ValidLocalBlocks](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/valid-local-blocks) | Error | Identifies when a local block is used incorrectly. | |
| [ValidRenderSnippetArgumentTypes](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/valid-render-snippet-argument-types) | Warning | Identifies when arguments are provided when using a `render` tag, but the types of the arguments don't match the type defined in the snippet's LiquidDoc. | |
| [ValidSchema](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/valid-schema) | Warning | Identifies invalid JSON in `{% schema %}` tags. | |
| [ValidSchemaName](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/valid-schema-name) | Error | Identifies invalid values for the schema name property. | |
| [ValidSchemaTranslations](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/valid-schema-translations) | Error | Identifies translation keys in schema tags that don't have a matching entry in the default schema locale file. | |
| [ValidScopedCSSClass](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/valid-scoped-css-class) | Warning | Warns when a CSS class used in an HTML class attribute might be defined outside the current file's scope. | |
| [ValidSettingsKey](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/valid-settings-key) | Error | Identifies when preset settings key, default settings key, or referenced block setting key is defined in their respective schema. | |
| [ValidStaticBlockType](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/valid-static-block-type) | Error | Identifies when a static block is using an invalid type. | |
| [VariableName](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/variable-name) | Warning | Identifies variable names that don't adhere to a selected naming convention. | |

***

## JSON file checks

These checks analyze the syntax, content and structure of JSON files.

| Check | Severity | Purpose | Auto-correction |
| - | - | - | - |
| [JSONMissingBlock](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/json-missing-block) | Error | Identifies when a JSON template file is referencing block types that don't exist. | |
| [JSONMissingSection](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/json-missing-section) | Error | Identifies when a JSON template or section group file is referencing section types that don't exist. | |
| [JSONSyntaxError](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/json-syntax-error) | Error | Identifies invalid JSON files in themes. | |
| [MatchingTranslations](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/matching-translations) | Warning | Identifies missing or additional translations in locale files. | Yes |
| [MaxFileSize](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/max-file-size) | Error | Identifies JSON and asset files that exceed Shopify's maximum file size. Also listed under Liquid file checks. | |
| [ValidHTMLTranslation](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/valid-html-translation) | Warning | Identifies invalid HTML inside translations. | |

***
