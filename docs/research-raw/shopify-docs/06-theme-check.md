# 06. Theme Check

## Checks reference: https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks
Liquid file checks (partial verbatim):
> "AppBlockValidTags Error ... AssetPreload Warning ... AssetSizeAppBlockCSS Error ... AssetSizeAppBlockJavascript Error ... AssetSizeCSS Error Prevents themes from using CSS files larger than the configured threshold. AssetSizeJavaScript Error ... BlockIdUsage Warning Warns against the use of block IDs in conditional statements and case statements. CdnPreconnect Warning ... ContentForHeaderModification Error Identifies code that tries to parse content_for_header."
> "DuplicateContentForArguments Warning ... DuplicateRenderSnippetArguments Warning ... EmptyBlockContent Warning Detects instances where the Liquid tag {% content_for 'blocks' %} is used when the associated schema blocks array is empty or undefined. ExcessiveSettingsCount Warning ... HardcodedRoutes Warning Encourages use of the routes object instead of hardcoding URLs. ImgWidthAndHeight Error Enforces setting the width and height attributes on img tags. LiquidComplexity Warning ... LiquidFreeSettings Warning ... LiquidHTMLSyntaxError Error Identifies Liquid and HTML syntax errors. LiquidNestingDepth Warning ..."
> "OrphanedSnippet Warning ... PaginationSize Warning ... ParserBlockingScript Error Identifies script tags that don't have defer or async attributes ... RemoteAsset Warning Discourages use of third party domains for hosting assets. RequiredLayoutThemeObject Error ... ReservedDocParamNames Error ... SchemaPresetsBlockOrder Warning ... SchemaPresetsStaticBlocks Error Warns if a preset static block doesn't have a {% content_for "block" ... %} tag in the Liquid code. StaticStylesheetAndJavascriptTags Error Warns if Liquid code is used inside a {% stylesheet %} or {% javascript %} tag."
JSON file checks:
> "JSONMissingBlock Error ... JSONMissingSection Error Identifies when a JSON template or section group file is referencing section types that don't exist. JSONSyntaxError Error ... MatchingTranslations Warning ... MaxFileSize Error ... ValidHTMLTranslation Warning"

## 1.x to 2.x mapping: https://shopify.dev/docs/storefronts/themes/tools/theme-check/migrate
Key renames/removals (verbatim pairs): "ImgLazyLoading | -" (removed in 2.x), "ParserBlockingJavaScript | ParserBlockingScript", "ParserBlockingScriptTag | ParserBlockingScript", "ValidJson | JSONSyntaxError", "SyntaxError | LiquidHTMLSyntaxError", "HtmlParsingError | LiquidHTMLSyntaxError", "AssetUrlFilters | RemoteAsset", "ConvertIncludeToRender | DeprecatedTag", "TemplateLength | -".
2.x-only checks include: ValidBlockTarget, ValidContentForArguments, ValidDocParamTypes, ValidLocalBlocks, ValidContentForArgumentTypes, ValidRenderSnippetArgumentTypes, ValidSchemaName, ValidSettingsKey, ValidStaticBlockType, UniqueStaticBlockId, UnclosedHTMLElement, UndefinedObject, UnknownFilter, UnusedAssign, ValidSchema, TranslationKeyExists, MissingTemplate, MissingAsset.

## Individual checks
- ValidSchema (https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/valid-schema): "Identifies invalid JSON in {% schema %} tags." Fail example: trailing comma. severity: error.
- ValidSchemaName (.../checks/valid-schema-name): 25 character limit. severity: error.
- ValidSchemaTranslations (.../checks/valid-schema-translations): "every translation key (t:) referenced inside a {% schema %} tag has a matching entry in the default schema locale file."
- ValidBlockTarget (.../checks/valid-block-target): "Ensures that block types reference valid files, and that nested blocks are declared in the root-level of the schema."
- JSONMissingBlock (.../checks/json-missing-block): "Ensures that a JSON template file includes block types that reference valid files and are declared at the root level of their associated schema."
- LiquidHTMLSyntaxError (.../checks/liquid-html-syntax-error): aliases "HtmlParsingError SyntaxError".
- ParserBlockingScript (.../checks/parser-blocking-javascript): "Theme Check only lints script tags that include the src attribute." Disable inline: `{% # theme-check-disable ParserBlockingScript %}` ... `{% # theme-check-enable ParserBlockingScript %}`
- DeprecateLazysizes (.../checks/deprecate-lazysizes): pass example `<img src="a.jpg" loading="lazy" />`
- AppBlockValidTags (.../checks/app-block-valid-tags): forbidden in app blocks: "{% javascript %} {% stylesheet %} [one item garbled in the returned chunk, likely {% include 'foo' %}] {% layout 'foo' %} {% section 'foo' %} {% sections 'foo' %}"

## Performance checks explained: https://shopify.dev/docs/storefronts/themes/best-practices/performance/theme-check-tool
> "AssetSizeCSS and AssetSizeJavaScript: ... The defaults are 100000 bytes for CSS and 10000 bytes for JavaScript ... They don't measure minified or compressed size"
> "Note: AssetSizeCSS and AssetSizeJavaScript aren't part of the recommended configuration, so they don't run unless you enable them."
> "ImgWidthAndHeight: Flags img tags that are missing width and height attributes, which causes layout shift. PaginationSize: ... The default is maxSize: 250."

## Config: https://shopify.dev/docs/storefronts/themes/tools/theme-check/configuration
```yaml
# .theme-check.yml
root: dist
extends:
  - theme-check:recommended # or theme-check:all, theme-check:theme-app-extension
require:
  - ./path/to/my_custom_check.js
ignore:
  - 'node_modules/**'
TemplateLength:
  enabled: false
  severity: warning
  ignore:
    - templates/index.liquid
  max_length: 300
```
> "By default, Theme Check fails, or returns an exit code of 1, when one or more issues with severity error are detected. You can configure the severity that causes a run of theme check to fail using the --fail-level flag." Severities: "error 0 warning 1 info 2".

## VS Code extension / language server: https://shopify.dev/docs/storefronts/themes/tools/shopify-liquid-vscode
> Completion of "Liquid tags, filters, objects, and object properties ... Theme, section and block settings ... Translation keys ... Snippet names ... Schema tags"; "Code formatting is powered by the Liquid Prettier plugin"; "Theme check is a linter for Shopify Themes. When it finds a problem with your code, it will add a red or yellow wavy line under it."
CLI: `theme language-server` "Starts the Language Server." (https://shopify.dev/docs/api/shopify-cli/theme)
