# 02. Input setting types

Source: https://shopify.dev/docs/storefronts/themes/architecture/settings/input-settings (via Shopify MCP search_docs_chunks, 2026-10-03)

Standard attributes:
> "type ... Yes / id The setting ID, which is used to access the setting value. Yes / label ... Yes / default ... No / info ... No"

Basic input settings (verbatim list):
> "The following are the basic input setting types: checkbox number radio range select text textarea"

Specialized input settings (verbatim list):
> "article article_list blog collection collection_list color color_background color_palette color_scheme color_scheme_group font_picker html image_picker inline_richtext link_list liquid metaobject metaobject_list page product product_list richtext text_alignment url video video_url"

Sidebar settings (https://shopify.dev/docs/storefronts/themes/architecture/settings/sidebar-settings):
> "The following are the types of sidebar settings: header paragraph" ; standard attributes `type` and `content` (required).

## Per-type rules quoted

checkbox: "If default is unspecified, then the value is false by default."

number: "Caution: The default attribute is optional. However, the value must be a number and not a string." placeholder: "These values only appear for settings defined in settings_schema.json. They don't appear for settings defined in a section's schema."

radio: "required options attribute that accepts an array of value and label definitions" ; "If default is unspecified, then the first option is selected by default."

range:
> "min The minimum value of the input Yes / max The maximum value of the input Yes / step The increment size between steps of the slider. Defaults to 1 when omitted. No / unit The unit for the input. For example, you can set px ... No"
> "If you enter a value that doesn't respect the step definition, then the value rounds to the closest step. If you enter a value outside of the given min and max, then the value reverts to the min or max value accordingly."
> "Caution: The default attribute is required. The min, max, step, and default attributes can't be string values. Failing to adhere results in an error."
NOT CONFIRMED: an older rule that a range may have at most 101 steps. Current chunk returned did not mention it. Treat as unverified.

text: "Tip: Settings of type text are not updated when switching presets."

image_picker:
> "outputs an image picker field that's automatically populated with the available images from the Files section of Shopify admin ... Merchants also have an opportunity to enter alt text and select a focal point"
> returns "An image object. nil, if either no selection has been made or the selection no longer exists."
> "Note: Settings of type image_picker are not updated when switching presets. image_picker settings also don't support the default attribute."
> Focal points: "Render your images using the image_tag filter. Consider positioning images within containers using object-fit: cover."

richtext: "outputs a multi-line text field with the following basic formatting options: Bold Italic Underline Link Paragraph Unordered list"; returns "A string ... An empty object, if nothing has been entered."
inline_richtext: "outputs HTML markup that isn't wrapped in paragraph tags (<p>) ... Bold Italic Link" ; "doesn't support ... Line breaks (<br />)"

url: picker for "Articles Blogs Collections Pages Products"; "Note: Accepted values for the default attribute are /collections and /collections/all."

video: "video picker that's automatically populated with the available videos from the Files section"; "also accepts metafields of type file_reference as a dynamic source"; "video settings don't support the default attribute."

video_url: "accept Takes an array of accepted video providers. Valid values are youtube, vimeo, or both. Yes"

link_list: "Accepted values for the default attribute are main-menu and footer."

liquid: "outputs a multi-line text field that accepts HTML and limited Liquid markup." (Theme limits page: "Content in a single liquid setting 50 KB")

product / article etc.: "Settings of type product are not updated when switching presets. product settings also don't support the default attribute."
product_list / article_list: "limit ... The default limit, and the maximum limit you can set, is 50." product_list: "You can only choose from products that are published to the online store and have an active status."

color_scheme: "Shopify returns the selected color_scheme object from color_scheme_group ... If the theme doesn't have color_scheme_group data in settings_data.json, then nil is returned."
color_scheme_group: "Color schemes can be added only in settings_schema.json."

metaobject_list:
> "metaobject_type The metaobject type allowed by the picker. Yes" ; "limit ... default limit, and the maximum limit you can set, is 50."
> "Custom metaobject definitions: These are designed for custom themes and require the metaobject definition to already exist. Note that custom metaobject definitions are not allowed in themes listed on the Theme Store."
> "When referencing a custom or app created metaobject_type, the definition must exist on the shop and be available to the storefront. If either condition isn't met, the setting will show an error in the theme editor."
> Example: `{ "type": "metaobject_list", "id": "my_material_list_setting", "label": "Materials", "metaobject_type": "shopify--material", "limit": 12 }`

Localization:
> "Text-bearing settings (text, textarea, richtext, inline_richtext, and html): merchants can translate their content with Translate & Adapt. liquid settings: the stored value isn't available in Translate & Adapt"

Conditional settings (https://shopify.dev/docs/storefronts/themes/architecture/settings):
> "The following settings support conditional settings: All basic input settings All sidebar settings These specialized input settings: color color_background color_scheme font_picker html image_picker inline_richtext ..." (list truncated in returned chunk)

Theme editor live preview of text (https://shopify.dev/docs/storefronts/themes/tools/online-editor):
> "The setting value must be the only child of its parent HTML element" ; "There must be no Liquid filters applied to the setting value, other than the escape filter"
