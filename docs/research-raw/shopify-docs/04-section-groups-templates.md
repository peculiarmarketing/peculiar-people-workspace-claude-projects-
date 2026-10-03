# 04. Section groups, JSON templates, making a section addable

## https://shopify.dev/docs/storefronts/themes/architecture/templates/json-templates
> "You can't share section data across JSON theme templates, so each section must have an ID that's unique within the template. JSON templates can render up to 25 sections, and each section can have up to 50 blocks."
> "The sections that are available to be added to a template in the theme editor might be limited by the enabled_on or disabled_on attribute of the section schema. If no enabled_on or disabled_on attribute is defined, then the section can be added to any template."
> Section data: "<SectionID> ... Accepts only alphanumeric characters. <SectionType> String Yes The filename of the section file to render, without the extension. <SectionDisabled> Boolean No When true, the section isn't rendered but can still be customized in the theme editor."

## https://shopify.dev/docs/storefronts/themes/architecture/section-groups
> "A section group is a JSON data file that stores a list of sections and app blocks to be rendered, and their associated settings. Merchants can add sections to the section group, as well as remove and reorder them, in the theme editor."
> "Section groups can render up to 25 sections, and each section can have up to 50 blocks."
> "Tip: In most themes, you should use section groups for only the header and footer."
> Location: "Section group files are located in the sections directory of the theme" (e.g. sections/header-group.json, sections/footer-group.json)

## How a section becomes addable
https://shopify.dev/docs/storefronts/themes/best-practices/editor/integrate-sections-and-blocks
> "Tip: Section and block files must define presets in their schema to support being added to JSON templates using the theme editor. Files without presets should be included in the JSON file manually, and can't be removed using the theme editor."
https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema
> "Presets appear alphabetically based on their name attribute ... Presets can optionally be grouped into collapsible categories using the category attribute ... Uncategorized presets are always displayed first ... The theme editor automatically generates a preset preview."

## JSON comments
https://shopify.dev/docs/storefronts/themes/architecture
> "Files that users typically don't edit won't persist comments or trailing commas. This includes the following: templates/*.json sections/*.json (section groups) config/settings_data.json locales/*.json"

## Metaobject templates
https://shopify.dev/docs/storefronts/themes/architecture/templates/metaobject
> "Metaobject theme templates enable the rendering of metaobject webpages per metaobject definition. To create a metaobject template for an Online Store, you must enable the onlineStore capability." Location: templates/metaobject/{type}.json

## Best practice
https://shopify.dev/docs/storefronts/themes/best-practices/templates-sections-blocks
> "These guidelines apply to Online Store 2.0 themes, which use JSON templates and section groups. You can't add or remove static sections from Liquid templates or layouts."
> "Avoid providing blocks that are too granular."
