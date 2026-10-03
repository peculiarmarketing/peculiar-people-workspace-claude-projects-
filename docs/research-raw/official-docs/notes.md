# Official Shopify docs: raw excerpts for custom OS 2.0 sections (research date 2026-10-03)

Method: shopify.dev, help.shopify.com, changelog.shopify.com and shrine.io are all blocked by the egress proxy (WebFetch returned EGRESS_BLOCKED; curl returned 000). shopify.dev text below comes verbatim from the Shopify MCP `search_docs_chunks` tool (indexed chunks of shopify.dev, read as excerpts, not full pages). help.shopify.com, changelog.shopify.com and Shrine items come only from WebSearch result summaries and are NOT verbatim; they are marked [SEARCH SUMMARY]. The Dev MCP and AI Toolkit items were read from primary artifacts: the npm registry metadata/README and the published 1.16.0 tarball of @shopify/dev-mcp (downloaded and extracted, not installed), and a shallow git clone of github.com/Shopify/shopify-ai-toolkit (HEAD commit 2026-10-01).

Page dates: shopify.dev reference pages in the chunk index show no "last updated" date. Changelog posts carry dates and are noted.

---

## 1. Sections

### https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema
- "{% schema %} tag for sections allows you to define the following section attributes and settings: name tag class limit settings blocks max_blocks presets default locales enabled_on disabled_on"
- "Note: The {% schema %} tag is a Liquid tag. However, it doesn't output its contents, or render any Liquid included inside it."
- "Each section can have only a single {% schema %} tag, which must contain only valid JSON using the attributes listed below. The tag can be placed anywhere within the section file, but it can't be nested inside another Liquid tag."
- "Caution: Having more than one {% schema %} tag, or placing it inside another Liquid tag, will result in a syntax error when editing your theme code."
- "name The name attribute determines the section title that is shown in the theme editor."
- Example schema includes `"limit": 1`, `"max_blocks": 5`, presets, locales, `"enabled_on": { "templates": ["*"], "groups": ["footer"] }`.
- presets: "Presets are predefined section configurations that merchants can select when adding sections to a JSON template." ... "Presets appear alphabetically based on their name attribute." ... "Presets can optionally be grouped into collapsible categories using the category attribute." ... "Uncategorized presets are always displayed first." ... "The theme editor automatically generates a preset preview." Preset attributes: name (Required: Yes), category, settings, blocks (No).
- "Tip: Sections with presets shouldn't be statically rendered. If you're going to statically render a section, then you should use default settings."
- enabled_on: "You can restrict a section to certain template page types and section group types by specifying them through the enabled_on attribute. enabled_on, along with disabled_on, replaces the templates attribute. Caution: You can use only one of enabled_on or disabled_on." Groups accepted values: "header, footer, aside, and custom types in the format custom.<NAME>." and `["*"]`.
- disabled_on: "When you use disabled_on, the section is available to all templates and section groups except the ones that you specified."
- Render blocks: "{% for block in section.blocks %} {% case block.type %} {% when 'slide' %} <div className=\"slide\" {{ block.shopify_attributes }}> ..." ; "Shopify's theme editor uses that attribute to identify blocks in its JavaScript API. If your block is a single element, then ensure that the element has this attribute."
- "Caution: Don't rely on the literal value of a block's ID when you iterate over blocks. The ID is dynamically generated and is subject to change."
- Recommended blocks: "include the @theme block type along with your recommended blocks in the blocks array."

### https://shopify.dev/docs/storefronts/themes/architecture/sections
- "Sections support the {% schema %} Liquid tag. This tag is used to define the following section attributes and settings:- name tag class limit settings blocks app blocks max_blocks presets defaults locales enabled_on disabled_on"

### https://shopify.dev/docs/storefronts/themes/architecture/templates/json-templates
- sections attribute: "This attribute needs to contain at least one section.Duplicate IDs within the template aren't allowed." ... "JSON templates can render up to 25 sections, and each section can have up to 50 blocks."
- "Tip: Section files must define presets in their schema to support being added to JSON templates using the theme editor. Section files without presets should be included in the JSON file manually, and can't be removed using the theme editor."
- layout: "Use the value false to render the template without a layout. Templates without a layout can't be customized in the theme editor."
- Section data: "each section must have an ID that's unique within the template." ... "If no enabled_on or disabled_on attribute is defined, then the section can be added to any template." ... "<SectionID> ... A unique ID for the section. Accepts only alphanumeric characters." "<SectionDisabled> Boolean No When true, the section isn't rendered but can still be customized in the theme editor."

### https://shopify.dev/docs/storefronts/themes/architecture/limits
- "JSON templates per theme 1,000 / Sections per JSON template 25 / Section groups per theme 20 / Sections per section group 25 / Blocks per section 50 (you can reduce this limit with max_blocks) / Blocks per JSON template or section group 1,250 / Theme block nesting depth 8 levels, excluding the section level / Theme block files (blocks/ folder) per theme 300"
- "Attempting to exceed a limit results in an error, either in the theme editor or when the theme is saved, uploaded, or synced with the Shopify CLI."

### https://shopify.dev/docs/storefronts/themes/architecture/section-groups
- "A section group is a JSON data file that stores a list of sections and app blocks to be rendered, and their associated settings." ... "Section groups can render up to 25 sections, and each section can have up to 50 blocks." ... "Tip: In most themes, you should use section groups for only the header and footer." Files: sections/header-group.json, sections/footer-group.json.

### https://shopify.dev/docs/storefronts/themes/best-practices/performance/use-section-rendering-api
- "section.id outputs the unique section ID" ... "Static sections use their filename as the ID ... Sections in JSON templates and section groups get a dynamic ID instead, such as template--123__product-info." ... "Read the ID from {{ section.id }} or from the section wrapper instead of hardcoding it."

### https://shopify.dev/docs/storefronts/themes/best-practices/javascript-and-stylesheet-tags
- "You can bundle JavaScript and stylesheet assets with section, block and, snippet files using the following Liquid tags: {% javascript %} {% stylesheet %}"
- "Caution: Liquid isn't rendered in {% javascript %} or {% stylesheet %} tags. Including Liquid code in these tags can cause syntax errors, or prevent styles from being applied to the theme."
- "Caution: Each file can only have one {% javascript %} tag." / "Caution: Each file can only have one {% stylesheet %} tag. Having more than one will result in a syntax error when editing your theme code."
- JS: "Shopify concatenates the content from {% javascript %} tags across all section, block and snippet files into one file per file type: sections: scripts.js blocks: block-scripts.js snippets: snippet-scripts.js" ... "asynchronously loaded through a <script> tag with the defer attribute" ... "wrapped in a self-executing anonymous function"
- CSS: "Shopify collects the content from {% stylesheet %} tags across sections, blocks, and snippets into a single styles.css file." ... "Shopify subsets this CSS so that each page only loads the styles from files in its render tree"
- "Bundled assets are only injected once for each section, block or snippet file, not for each instance of that file. If you need instance-specific CSS, then use an inline <style> tag." / "If you need instance-specific JavaScript, then add data attributes to your section markup"

### https://shopify.dev/docs/api/liquid/tags/stylesheet
- "Each section, block or snippet can have only one {% stylesheet %} tag." "Caution: Liquid isn't rendered inside of {% stylesheet %} tags."

### https://shopify.dev/docs/api/liquid/tags/include
- "Deprecated: Deprecated because the way that variables are handled reduces performance and makes code harder to both read and maintain. The include tag has been replaced by render."

### https://shopify.dev/docs/storefronts/themes/best-practices/performance/avoid-nested-renders
- "Don't use include: include is deprecated, and you shouldn't use it anywhere in a theme. Unlike render, include gives the snippet access to the entire parent scope and lets it modify the caller's variables."

### https://shopify.dev/docs/storefronts/themes/architecture (directory structure)
- "Themes must use the following directory structure: assets blocks config layout locales sections snippets templates (customers, metaobject)" "Subdirectories, other than the ones listed, aren't supported." "Note: Only a layout directory containing a theme.liquid file is required for the theme to be uploaded to Shopify."

## 2. Blocks

### https://shopify.dev/docs/storefronts/themes/architecture/blocks
- "There are three types of blocks: Theme blocks: Created as their own Liquid files in the /blocks folder, and re-usable across multiple sections with the theme. Section blocks: Created within a section's Liquid file and are limited to use within that section. App blocks: Provided by apps installed on a merchant's shop."
- "Note: A theme can contain at most 300 theme blocks. Every .liquid file in the theme's /blocks folder counts toward this limit, including AI-generated theme blocks"
- Section block limits: "They only work in the section they're defined within ... They only support a single level of hierarchy, and cannot be nested. They can not currently be used in the same section as Theme blocks."
- "App blocks can be added to any section (or Theme Block) within a theme that has added support in it's schema file." `"blocks": [{ "type": "@theme" }, { "type": "@app" }]`
- AI blocks: "Shopify themes can be extended with custom blocks generated using Sidekick, directly within the theme editor (for eligible merchants)." ... "these AI-generated blocks are theme blocks. They are stored in the /blocks folder"

### https://shopify.dev/docs/storefronts/themes/architecture/blocks/theme-blocks/schema
- "Theme blocks support the {% schema %} Liquid tag ... name settings blocks presets tag class"
- "Each block can have only a single {% schema %} tag, which must contain only valid JSON and can only use the attributes listed below."
- "The \"@app\" type denotes that this block accepts app blocks." "The \"@theme\" type denotes that this block is compatible with other theme-defined blocks that live in the /blocks folder of the theme."
- "Theme blocks can't define local blocks in the blocks attribute of their schema." "Tip: Theme blocks can be nested up to 8 levels deep, excluding the section level."
- "For blocks to be compatible with the theme editor, the top level HTML element must be tagged with the {{ block.shopify_attributes }} Liquid tag." "Note: Shopify automatically adds this attribute for you when it renders the wrapper around blocks, but when the tag attribute is set to null, you must ensure that the top level HTML element of your block has this attribute"

### https://shopify.dev/docs/storefronts/themes/architecture/blocks/app-blocks
- "If your section is part of a JSON template, then you should support blocks of type @app." "Note: Blocks of type @app aren't supported in statically rendered sections."
- "When merchants choose to add the app to a new section, Shopify automatically wraps the app block in a wrapper section called Apps. You can customize this wrapper section by your own apps.liquid section."
- "Caution: Blocks of type @app don't accept the limit parameter. Including this will result in an error."

### https://shopify.dev/docs/apps/build/online-store/theme-app-extensions/configuration
- "For app blocks to function, a theme must contain the following: JSON templates. Sections that support and render blocks of type @app."

### https://shopify.dev/docs/apps/build/online-store/verify-support
- "To verify whether a theme supports app blocks, you need to determine the following: Whether the template where your app is injected supports JSON. The main section in the template. Whether the section where your app is injected has a block of type @app in its schema."

### https://shopify.dev/docs/apps/build/online-store/theme-app-extensions/migrate
- "App embed blocks are inactive until an app user turns them on in the theme editor, and your app can't activate them on the app user's behalf."

### https://shopify.dev/docs/storefronts/themes/architecture/blocks/section-blocks
- "{% for block in section.blocks %} {%- case block.type -%} {%- when \"heading\" -%} <h1>{{ block.settings.heading }}</h1> {% endcase %} {% endfor %}"

## 3. Input settings

### https://shopify.dev/docs/storefronts/themes/architecture/settings/input-settings
- Standard attributes: "type ... Yes / id ... Yes / label ... Yes / default ... No / info ... No"
- "Basic input settings: checkbox number radio range select text textarea"
- "Specialized input settings: article article_list blog collection collection_list color color_background color_palette color_scheme color_scheme_group font_picker html image_picker inline_richtext link_list liquid metaobject metaobject_list page product product_list richtext text_alignment url video video_url"
- checkbox: "If default is unspecified, then the value is false by default."
- number: "Caution: The default attribute is optional. However, the value must be a number and not a string."
- radio: "If default is unspecified, then the first option is selected by default."
- range: "min ... Yes / max ... Yes / step The increment size between steps of the slider. Defaults to 1 when omitted. No / unit ... No" ... "If you enter a value that doesn't respect the step definition, then the value rounds to the closest step." ... "Caution: The default attribute is required. The min, max, step, and default attributes can't be string values. Failing to adhere results in an error."
- select: options "Yes"; rendered as SegmentedControl when "Two to five options are provided" and no group.
- text: "Tip: Settings of type text are not updated when switching presets." placeholder "only appear for settings defined in settings_schema.json. They don't appear for settings defined in a section's schema."
- font_picker: "Caution: The default attribute is required. Failing to include it will result in an error."
- html: "The following HTML tags will be automatically removed: <html> <head> <body>"
- link_list: "Accepted values for the default attribute are main-menu and footer."
- liquid: "outputs a multi-line text field that accepts HTML and limited Liquid markup." ... "Note: The default attribute is optional. However, if you use it, then its value can't be an empty string." ... "Settings of type liquid don't have access to the following liquid objects/tags: layout content_for_header content_for_layout content_for_index section javascript stylesheet schema settings"
- richtext: "if it's used, then only <p> or <ul> tags are supported as top-level elements." "Caution: Failing to wrap the default content in <p> or <ul> tags will result in an error."
- text_alignment: "Can be one of left, right, center."
- Localization note: "Text-bearing settings (text, textarea, richtext, inline_richtext, and html): merchants can translate their content with Translate & Adapt."

### https://shopify.dev/docs/storefronts/themes/architecture/settings
- "Most setting types may be conditionally set using the visible_if attribute."

### NOT FOUND: a "range may have at most 101 steps" rule. Searched; current input-settings chunks don't contain it.

## 4. Liquid reference: images and assets

### https://shopify.dev/docs/api/liquid/filters/image_url
- "Caution: You need to specify either a width or height parameter. If neither are specified, then an error is returned." "Note: Regardless of the specified dimensions, an image can never be resized to be larger than its original dimensions." width/height "up to a maximum of 5760px."

### https://shopify.dev/docs/api/liquid/filters/image_tag
- widths: "By default, Shopify generates a srcset with a smart set of default widths up to the maximum defined in the image URL."
- alt: "By default, the alt attribute of the <img> tag is set to the media alt text, or the resource title"
- preload: "When preload is set to true, a resource hint is sent as a Link HTTP header with a rel value of preload." "You should use the preload parameter sparingly."

### https://shopify.dev/docs/storefronts/themes/best-practices/performance/never-lazy-load-lcp-image
- "The image_tag filter automatically applies loading=\"eager\" for sections 1 through 3, and loading=\"lazy\" for sections 4 and later. It also applies loading=\"eager\" whenever section.index0 is nil, which is the case in the online store editor, in static sections, and in the Section Rendering API. Don't set the loading attribute when relying on this default."

### https://shopify.dev/docs/storefronts/themes/best-practices/performance/use-filter-chains
- "The candidate widths start from the defaults 352, 832, 1200, and 1920." ... "Format negotiation: The CDN automatically serves WebP or AVIF when the browser supports them"

### https://shopify.dev/docs/storefronts/themes/best-practices/performance/use-responsive-images
- "{{ product.featured_image | image_url: width: 1000 | image_tag: widths: '400, 600, 800, 1000', sizes: '(min-width: 1000px) 900px, calc(100vw - 2rem)' }}" "Four to six widths are usually sufficient." "No sizes attribute: The browser defaults to downloading the largest image."

### https://shopify.dev/docs/api/liquid/filters/stylesheet_tag
- "{{ 'base.css' | asset_url | stylesheet_tag }}" -> `<link href="..." rel="stylesheet" type="text/css" media="all" />`; "preload ... resource hint is sent as a Link header"

### Verifying objects/filters exist
- https://shopify.dev/docs/api/liquid is the reference ("Liquid Cheat Sheet ... Theme Check ...").
- Theme Check UnknownFilter: "Identifies references to unknown Liquid filters." UndefinedObject check exists (name confirmed in 2.x table).

## 5. Shopify CLI

### https://shopify.dev/docs/api/shopify-cli
- "Requirements Node.js: 22.12 or higher A Node.js package manager: npm, Yarn 1.x, or pnpm. Git: 2.28.0 or higher" ; "npm install -g @shopify/cli@latest" ; "brew tap shopify/shopify brew install shopify-cli" ; "Starting with Shopify CLI 4.0, Shopify CLI upgrades itself automatically" ; "shopify config autoupgrade off"

### https://shopify.dev/docs/storefronts/themes/tools/cli
- "Development themes are temporary, hidden themes that are connected to the Shopify store that you're using for development." "Development themes don't count toward your theme limit, and are deleted from the store after seven days of inactivity. Your development theme is deleted when you run shopify auth logout."
- "Anonymous usage statistics are collected by default. To opt out, you can use the environment variable SHOPIFY_CLI_NO_ANALYTICS=1."

### https://shopify.dev/docs/api/shopify-cli/theme/theme-dev
- "Uploads the current theme as the specified theme, or a development theme, to a store so you can preview it." "If you already have a development theme for your current environment, then this command replaces the development theme with your local theme. You can override this using the --theme-editor-sync flag." "You can run this command only in a directory that matches the default Shopify theme folder structure."
- Flags quoted: --host ("The default value is 127.0.0.1"), --live-reload (hot-reload default / full-page / off), --theme-editor-sync ("Synchronize Theme Editor updates in the local theme files."), -a/--allow-live ("Allow development on a live theme."), -n/--nodelete, -o/--only ("Hot reload only files that match the specified pattern."), -s/--store, -t/--theme, -x/--ignore, --store-password, --error-overlay, --listing, --notify, --open.

### https://shopify.dev/docs/storefronts/themes/getting-started/create
- "The command returns a URL that hot reloads local changes to CSS and sections ... This preview is only available in Google Chrome." "You need to pass the --store flag the first time you preview your theme."

### https://shopify.dev/docs/api/shopify-cli/theme/theme-push
- "-n, --nodelete ... Prevent deleting remote files that don't exist locally." "-o, --only ... Upload only the specified files (Multiple flags allowed)." "-p, --publish Publish as the live theme after uploading." "-u, --unpublished Create a new unpublished theme and push to it." "-l, --live" ; "-x, --ignore" ; example "shopify theme push --unpublished --json"

### https://shopify.dev/docs/api/shopify-cli/theme/theme-pull
- "-n, --nodelete Prevent deleting local files that don't exist remotely." "-o, --only Download only the specified files" "-l, --live Pull theme files from your remote live theme."

### https://shopify.dev/docs/api/shopify-cli/theme/theme-share
- "Uploads your theme as a new, unpublished theme in your theme library. The theme is given a randomized name. This command returns a preview link that you can share with others."

### https://shopify.dev/docs/api/shopify-cli/theme/theme-package
- "Packages your local theme files into a ZIP file that can be uploaded to Shopify. Only folders that match the default Shopify theme folder structure are included" ; "theme_name-theme_version.zip, based on parameters in your settings_schema.json file."

### https://shopify.dev/docs/api/shopify-cli/theme/theme-check
- "Calls and runs Theme Check to analyze your theme code for errors" ; flags --fail-level, --init ("Generate a .theme-check.yml file"), --list, --print, -a/--auto-correct, -C/--config ("theme-check:theme-app-extension, theme-check:recommended, theme-check:all"), -o/--output.

### https://shopify.dev/docs/api/shopify-cli/theme (command list)
- theme init, language-server, list, metafields pull, open, package, preview ("Applies a JSON overrides file to a theme and creates or updates a preview."), profile, publish, pull, push, rename, share.

### https://shopify.dev/docs/storefronts/themes/getting-started/customize
- "The development theme is destroyed when you run shopify auth logout." ; "Caution: This tutorial describes customizing themes that don't use the Shopify GitHub integration."

## 6. Theme Check

### https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks (table)
- "ImgWidthAndHeight | Error | Enforces setting the width and height attributes on img tags."
- "LiquidHTMLSyntaxError | Error | Identifies Liquid and HTML syntax errors."
- "MissingTemplate | Warning | Identifies when a resource is referenced using a render, section, or include tag, but doesn't exist. | Yes"
- "ParserBlockingScript | Error | Identifies script tags that don't have defer or async attributes"
- "RemoteAsset | Warning | Discourages use of third party domains for hosting assets."
- "StaticStylesheetAndJavascriptTags | Error | Warns if Liquid code is used inside a {% stylesheet %} or {% javascript %} tag."
- "ValidSchema | Warning | Identifies invalid JSON in {% schema %} tags." (the ValidSchema check page shows "ValidSchema: enabled: true severity: error")
- "ValidSchemaName | Error", "ValidSettingsKey | Error", "ValidLocalBlocks | Error", "ValidStaticBlockType | Error", "ValidScopedCSSClass | Warning", "ExcessiveSettingsCount | Warning", "AssetSizeCSS | Error | Prevents themes from using CSS files larger than the configured threshold."
- ValidBlockTarget page: "Ensures that block types reference valid files, and that nested blocks are declared in the root-level of the schema."
- UnknownFilter page: "Identifies references to unknown Liquid filters." severity error.

### https://shopify.dev/docs/storefronts/themes/tools/theme-check/migrate
- 1.x to 2.x table: "ImgLazyLoading | -" (no 2.x equivalent), "HtmlParsingError -> LiquidHTMLSyntaxError", "SyntaxError -> LiquidHTMLSyntaxError", "AssetSizeCSSStylesheetTag -> AssetSizeCSS", "ConvertIncludeToRender -> DeprecatedTag", "ParserBlockingJavaScript -> ParserBlockingScript", "ValidJson -> JSONSyntaxError", "UndefinedObject -> UndefinedObject", "UnknownFilter -> UnknownFilter", "MissingTemplate -> MissingTemplate".

### https://shopify.dev/docs/storefronts/themes/best-practices/performance/theme-check-tool
- "AssetSizeCSS and AssetSizeJavaScript ... The defaults are 100000 bytes for CSS and 10000 bytes for JavaScript." "Note: AssetSizeCSS and AssetSizeJavaScript aren't part of the recommended configuration, so they don't run unless you enable them."

### https://shopify.dev/docs/storefronts/themes/tools/theme-check/configuration
- Example .theme-check.yml with root, extends (theme-check:recommended / theme-check:all / theme-check:theme-app-extension), require, ignore, per-check enabled/severity/ignore. "By default, Theme Check fails, or returns an exit code of 1, when one or more issues with severity error are detected." Severities "error 0 warning 1 info 2".

## 7. GitHub integration

### https://shopify.dev/docs/storefronts/themes/tools/github
- "The GitHub theme integration updates your theme in the Shopify admin whenever the connected branch is updated. It also commits changes made through the Shopify admin to the branch" ; "Note: Files are updated in GitHub whenever changes are made to a connected theme. This can't be disabled."
- "Edits saved within about 10 seconds of each other are batched into one commit"
- "There are currently no conflict alerts in the code editor. The version of the file in the code editor overwrites the GitHub version of the file." ; "the commit coming from Shopify might be viewed as outdated and rejected by GitHub." ; "View logs beside the Last saved timestamp" ; "Actions > Reset to last commit."
- "You can connect only branches that match the default Shopify theme folder structure. This structure represents a buildless theme" ; "Folders in the repository that don't match the default theme structure are ignored."
- Limitations: "GitHub outside collaborators can't connect branches."

## 8. Theme app extensions vs sections vs dynamic sources

### https://shopify.dev/docs/apps/build/online-store/theme-app-extensions
- "Theme app extensions allow merchants to easily add dynamic elements to their themes without having to interact with Liquid templates or code." "Theme app extensions can integrate with Online Store 2.0 themes." "Apps built in the theme app extension framework don't edit theme code"
### https://shopify.dev/docs/storefronts/themes/os20
- "When an app is uninstalled by a merchant, the app code is removed with it."
### https://shopify.dev/docs/storefronts/themes/architecture/settings/dynamic-sources
- "Dynamic data sources ... allow merchants to connect input settings to data coming from resources such as products, collections, blogs, and pages as well as metafields and metaobjects. Dynamic sources are connected using section and block settings." "Note: Dynamic sources aren't available for general theme settings." "Metaobjects with storefront visibility will be available as dynamic sources for any theme setting"
### https://shopify.dev/docs/storefronts/themes/store/requirements
- "Introduce Custom Liquid blocks into certain sections. Add a Custom Liquid block anywhere you'd consider adding an app block ... This block should include a setting of type liquid." ; "Themes must support app blocks (blocks of type @app) in the main product section and featured product section."

## 9. AI tooling

### https://shopify.dev/docs/apps/build/ai-toolkit
- "Shopify AI Toolkit gives your AI coding tool a Shopify-aware starting point." "Code validation: validate GraphQL queries, Liquid templates, and Shopify Extensions against Shopify schemas"
- "Requirements ... Node.js 18 or higher"
- Claude Code plugin: "claude plugin install shopify-ai-toolkit@claude-plugins-official"
- Skills: "npx skills add Shopify/shopify-ai-toolkit"
- Dev MCP: "The server runs locally and doesn't require authentication." "claude mcp add --transport stdio shopify-dev-mcp -- npx -y @shopify/dev-mcp@latest"
### https://shopify.dev/changelog/blog/shopify-ai-toolkit-connect-your-ai-tools-to-the-shopify-platform (April 9, 2026)
- "Shopify AI Toolkit connects supported AI coding tools to Shopify documentation, API schemas, code validation, store-management workflows, and migration guidance." "If you're editing Liquid or UI extension code, it can validate the generated work against Shopify-specific expectations."
### https://shopify.dev/changelog/posts/ai-toolkit-skills-have-been-consolidated (September 25, 2026)
- "all existing shopify- skills are consolidated into a single shopify skill." "Users of the ucp skill and Dev MCP are unaffected."
### https://shopify.dev/changelog/posts/dev-mcp-now-supports-liquid (October 1, 2025)
- "The Shopify Dev MCP server can now search for Liquid docs, and validate Liquid" ; "The built-in theme-check integration identifies syntax errors and best practice violations"
### npm @shopify/dev-mcp README (registry, latest 1.16.0 published 2026-09-25T19:57:15Z)
- "It lets AI agents search Shopify's documentation and API schemas, validate GraphQL operations, Liquid and theme files, and UI-extension code, and resolve supported API versions."
- "The server requires Node.js 18 or later and runs locally over standard input/output without authentication"
- "LIQUID_VALIDATION_MODE defaults to full, which exposes validate_theme for validating entire theme directories. Set it to partial to validate individual code blocks instead: validate_theme is not registered, and liquid joins the api enum of the merged validate tool."
- Telemetry: "Published release builds send usage events to https://shopify.dev/mcp/usage." Opt out: "~/.config/shopify-ai-toolkit/opt-out" or "OPT_OUT_INSTRUMENTATION=true or DO_NOT_TRACK=1".
### dev-mcp 1.16.0 dist (tool registry `_v`): feedback, learn_shopify_api, search_docs_chunks, validate, validate_theme
- validate_theme description: "This tool validates Liquid codeblocks, Liquid files, and supporting Theme files (e.g. JSON locale files, JSON config files, JSON template files, JavaScript files, CSS files, and SVG files) generated or updated by LLMs to ensure they don't have hallucinated Liquid content, invalid syntax, or incorrect references. Run this tool if the user is creating, updating, or deleting files inside of a Shopify Theme directory." Inputs: absoluteThemePath, filesCreatedOrUpdated.
- learn_shopify_api: code comment "This tool is the entrypoint for our MCP server ... It generates and returns a conversationId that should be passed to all subsequent tool calls"
- search_docs_chunks: "This tool will take in the user prompt, search shopify.dev, and return relevant documentation and code examples"
- Older names validate_theme_codeblocks / validate_graphql_codeblocks / validate_component_codeblocks still appear as strings; merged into `validate`.
### github.com/Shopify/shopify-ai-toolkit (clone, HEAD 2026-10-01; plugin 2.1.0)
- CHANGELOG 2.0.0: "Publish every Shopify topic as a single shopify skill" ; 2.1.0: "The Cursor plugin ... now connects to Shopify's remote MCP at setup.shopify.com/mcp."
- skills/shopify/references/liquid.md: "Write per-component CSS/JS using {% stylesheet %} and {% javascript %} tags" "These tags are only supported in snippets/, blocks/, and sections/" "Liquid is NOT rendered inside {% stylesheet %} or {% javascript %} tags" ; "Use {{ block.shopify_attributes }} on block wrapper elements" ; "for loops limited to 50 iterations"; validate: "--api liquid --theme-path <absolute-path-to-theme> --files <rel1,rel2,...>"
- README telemetry: "Telemetry is on by default." Claude Code hook can attach "the user's most recent prompt verbatim (truncated to 2000 chars)".

### https://shopify.dev/docs/storefronts/themes/architecture/blocks/ai-generated-theme-blocks
- "In the theme editor, merchants can generate theme blocks in existing sections that support theme blocks." "To make it possible for a section to accept AI generated blocks, it must accept theme blocks." "Shopify automatically wraps the generated block in a wrapper section called _blocks.liquid." Custom _blocks.liquid must: "Define @theme and @app as block types Define presets Define {% content_for blocks %} Does not define the templates attribute"

### Changelog/help [SEARCH SUMMARY, not verbatim]
- changelog.shopify.com/posts/ai-block-generation-for-all-theme-store-themes: AI block generation powered by Sidekick works with every Theme Store theme, not just Horizon; dated December 10, 2025 per search summary.
- help.shopify.com/.../theme-editor/shopify-magic/generate-blocks: Add block > Generate; prompts minimum five words; merchant responsible for reviewing generated code.

### Other dated dev changelog (verbatim)
- May 21, 2025 "Block previews are now available in theme editor"; May 21, 2025 "Recommend theme blocks in the block picker"; May 21, 2025 "Passing parameters to static blocks".
- July 21, 2026 "Liquid templates can now compose pages with blocks and partials": "The Liquid July '26 developer preview ... adds two Liquid tags: {% block %} ... {% partial %}" "Existing themes continue to work with sections, theme settings, and JSON templates."

## 10. Performance / accessibility

### https://shopify.dev/docs/storefronts/themes/store/requirements
- "Themes must have a minimum average Lighthouse performance score of 60 across the theme's product, collection, and home page, for both desktop and mobile." "Themes must have a minimum average Lighthouse accessibility score of 90"
- Accessibility list: keyboard accessible, visible focus, alt attribute, "Text color contrast ratio must be 4.5:1", "touch target ... at least 24 by 24 CSS pixels".
### https://shopify.dev/docs/storefronts/themes/best-practices/performance
- Essential: "Never lazy-load the LCP image", "Mark the LCP image with fetchpriority=\"high\"", "Use defer and async on non-critical scripts".
### https://shopify.dev/docs/storefronts/themes/best-practices/performance/testing-for-performance
- weights "Home page: 17 percent. Product page: 40 percent. Collection page: 43 percent." ; "Append pb=0 (preview bar off)"
### https://shopify.dev/docs/storefronts/themes/best-practices/accessibility
- "Following only the best practices on this page doesn't guarantee that your theme is completely accessible." Tools: Accessibility Insights, Lighthouse, WAVE, Shopify Lighthouse CI GitHub action.
### Custom Liquid [SEARCH SUMMARY] help.shopify.com/.../theme-editor/customizing-sections and /extend/
- "Not all themes support Custom Liquid blocks." Liquid settings "only allow you to access limited Liquid objects and tags."

## 11. Theme updates and Shrine [SEARCH SUMMARY]
- help.shopify.com/en/manual/online-store/themes/managing-themes/updating-themes: theme editor customizations are copied to the updated theme; code edits included only if they don't conflict; incompatible code changes are removed from the updated copy; save a copy of customized code first.
- Same page / adding-themes: updates are for Theme Store themes; "If you purchased a theme from a third-party theme designer outside of the Shopify Theme Store, then contact the designer for updates."
- Shrine: sold at shrine.io (not Theme Store). Update = upload new ZIP via Add theme > Upload zip file (community/third-party summary). Shrine site claims settings carry over between versions; no official Shrine statement found about custom code/custom sections surviving updates. Shrine PRO 1.9.0 change summary (vendor-adjacent search summary): Swatch Pills picker, quantity-break gifts/upsells, infinite collection loading, etc. A separate summary mentions "Shrine 2.1.0 (December 11, 2025)"; unclear whether that is Shrine or Shrine PRO numbering.
- app.shrine.io and shrine.io unreachable (EGRESS_BLOCKED).

## 12. Preview / duplicate / history [SEARCH SUMMARY]
- help.shopify.com/.../edit-code/edit-theme-code: per-file "Timeline view" ... "doesn't restore an entire theme, and it can't recover deleted theme files" ; "Asset files ... don't have Timeline history."
- help.shopify.com/.../adding-themes: Basic/Grow/Advanced up to 20 themes, Plus up to 100; "only one theme can be published at any time"; unpublished themes have Draft status.
- help.shopify.com/.../duplicating-themes: duplicate needs a free slot under the 20 limit.
