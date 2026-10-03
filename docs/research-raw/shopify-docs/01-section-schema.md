# 01. Section file structure and {% schema %} rules

Source tool: Shopify MCP `search_docs_chunks` (searches shopify.dev), queried 2026-10-03. Quotes are verbatim chunk text.

## https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema

> "{% schema %} tag for sections allows you to define the following section attributes and settings: name tag class limit settings blocks max_blocks presets default locales enabled_on disabled_on"

> "Note: The {% schema %} tag is a Liquid tag. However, it doesn't output its contents, or render any Liquid included inside it."

> "Each section can have only a single {% schema %} tag, which must contain only valid JSON using the attributes listed below. The tag can be placed anywhere within the section file, but it can't be nested inside another Liquid tag. Caution: Having more than one {% schema %} tag, or placing it inside another Liquid tag, will result in a syntax error when editing your theme code."

tag:
> "By default, when Shopify renders a section, it's wrapped in a <div> element with a unique id attribute: <div id="shopify-section-[id]" class="shopify-section"> ... The following are the accepted values: article aside div footer header section"

class:
> "When Shopify renders a section, it's wrapped in an HTML element with a class of shopify-section. You can add to that class with the class attribute"

limit:
> "By default, there's no limit to how many times a section can be added to a template or section group. You can specify a limit of 1 or 2 with the limit attribute"

settings:
> "Caution: All section setting IDs must be unique within each section. Having duplicate IDs within a section will result in an error."
> "Tip: If a section is statically rendered, then there's only one instance of the section across all static renderings, as a result they all share the same section setting values."

blocks (section blocks):
> "Attribute Description Required type The block type. This is a free-form string ... Yes name The block name, which will show as the block title in the theme editor. Yes limit The number of blocks of this type that can be used. No settings Any input or sidebar settings ... No"
> "Caution: All block names and types must be unique within each section, and all setting IDs must be unique within each block. Having duplicates will result in an error."

Dynamic block titles:
> "The theme editor uses settings with the following id values, in order of precedence: heading title text If a setting with a matching id value doesn't exist, then the block name is used as the title."

max_blocks:
> "There's a limit of 50 blocks per section. You can specify a lower limit with the max_blocks attribute. Note: Static blocks don't count toward this limit."

presets:
> "Presets are predefined section configurations that merchants can select when adding sections to a JSON template."
> "Section presets have the following attributes: name (Yes) ... category (No) Groups related presets together in the theme editor's Add section picker. settings (No) ... blocks (No) Default blocks included in the preset. Each block entry must include a type attribute matching the block type..."
> "Tip: Sections with presets shouldn't be statically rendered. If you're going to statically render a section, then you should use default settings."

default:
> "If you statically render a section, then you can define a default configuration with the default object, which has the same attributes as the preset object."
> "Tip: You should only use the section default attribute for sections that will be reused, or installed on multiple themes or shops."

locales:
> "Sections can provide their own set of translated strings through the locales object. This is separate from the locales directory of the theme"

enabled_on / disabled_on:
> "enabled_on, along with disabled_on, replaces the templates attribute. Caution: You can use only one of enabled_on or disabled_on."
> groups accepted values: "header, footer, aside, and custom types in the format custom.<NAME>. ["*"] (all section group types)"
> templates: "A list of page types ["*"] (all template page types)"

## https://shopify.dev/docs/storefronts/themes/architecture/settings
> "Most setting types may be conditionally set using the visible_if attribute." Example: `"visible_if": "{{ block.settings.layout_style == 'flex' }}"`

## https://shopify.dev/docs/storefronts/themes/architecture/limits (Theme limits)
> "JSON templates per theme 1,000 / Sections per JSON template 25 / Section groups per theme 20 / Sections per section group 25 / Blocks per section 50 (you can reduce this limit with max_blocks) / Blocks per JSON template or section group 1,250 / Theme block nesting depth 8 levels, excluding the section level / Theme block files (blocks/ folder) per theme 300"
> "Statically rendered blocks added with {% content_for %} don't count toward these limits."
> File sizes: "JSON template file 512 KB / Section group file 512 KB / settings_schema.json 512 KB / settings_data.json 1.5 MB / Locale files 1.5 MB / Other Liquid files (sections, snippets, layouts) 256 KB / Content in a single liquid setting 50 KB"
> Naming: "Theme name 50 characters / Section and block schema name attribute 25 characters / Custom section and block names (set by merchants in the theme editor) 100 characters"

## https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/valid-schema-name
> "Makes sure that the schema name property doesn't exceed the 25 character limit, including when the name is a translation key that resolves to a value in the default schema locale file." Default severity: error.

## https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/excessive-settings-count
> "Identifies section or block schemas with more top-level settings than the configured maxSettings. This check counts only top-level settings with an id; it doesn't count presentation-only header or paragraph entries, or settings nested inside blocks."
> Fail example: "the schema declares 41 top-level settings with an id, which is greater than the default maximum of 40"
NOTE: 40 is a Theme Check lint default (warning), not a confirmed platform hard limit. A hard platform cap on settings per section was NOT confirmed.
