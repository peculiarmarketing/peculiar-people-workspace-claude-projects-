# Companion: uzi prints prompt docs (video YXamW3c_J-s)

- Source 1 (linked in video description): https://docs.google.com/document/d/1qhfIo5PYAFXK8V1duposk_VVAT_ASqlGUM5I5T7V4hk (exported as txt)
- Source 2 (linked inside Source 1, Prompt #2): https://docs.google.com/document/d/1ZVA-N2QSwSI1oEKwa9LWQJnwKSwPEt6Q_gYkOOuEr_g (exported as txt)
- Fetched: 2026-10-03 with curl
- Note: the paid prompt pack (whop.com link) was not fetched.

## Source 1: prompt doc

﻿PROMPT #1: USE CLAUDE
(PROVIDE SCREENSHOT OF YOUR PRODUCT PAGE FOR STYLE KNOWLEDGEMENT)
I have provided screenshots of my entire webpage, please analyze my webpage so you understand the type of design and style for future custom liquids to create custom website sections that look very clean and fitting to the web page. The goal of this is so that whenever I need you to create a custom liquid, you can make it fitting to this webpage. 


PROMPT #2: COPY AND PASTE DOC + SECTION DESCRIPTION


I have pasted a guideline in this prompt for you to go off of when creating this custom liquid section for Shopify. Please keep in mind that we are using the custom liquid blocks, meaning that it only accepts plain Liquid and HTML, it does not support {% schema %}, {% style %}, section settings, or presets. 

I want you to create a custom liquid regarding this:

[INSERT WHAT YOU WANT]


PASTE EVERYTHING IN THIS LINK INTO THE SAME PROMPT:  https://docs.google.com/document/d/1ZVA-N2QSwSI1oEKwa9LWQJnwKSwPEt6Q_gYkOOuEr_g/edit?tab=t.0 


PROMPT #3: SECTION CHANGES
I have pasted a photo of what the custom liquid has created, please make these changes:


[INSERT CHANGES/EDITS YOU WANT]

## Source 2: section guideline doc

﻿You are building a custom Shopify Liquid section for the store you have already been shown in this conversation. You already have the visual reference for the store, the existing typography, the color palette, the spacing rhythm, the button styles, the section padding, the heading sizes, the corner radius, the shadow language, and the overall design temperature. Treat that visual context as the source of truth. The new section must look like it was built by the same designer who built the rest of the site, not bolted on.


# OUTPUT FORMAT


Return ONE complete, production ready Liquid file that can be dropped into the /sections folder of a Shopify theme. The file must include three parts in this order:


1. The Liquid markup (HTML with Liquid tags, fully wired to the schema settings).
2. A scoped <style> block placed inside the section file.
3. A {% schema %} block at the bottom with full settings and presets.


If JavaScript is required, include it in a scoped <script> block inside the section file. Do not use external libraries or CDN imports. Vanilla JS only.


Do not output explanations, commentary, or notes. Only output the complete Liquid file.


# STYLE MATCHING RULES (NON NEGOTIABLE)


The section must visually match the store you have been shown. Specifically:


- Match the existing font families, font weights, font sizes, and line heights used elsewhere on the site. Do not introduce new fonts.
- Match the existing color palette exactly. Pull primary, accent, background, text, border, and button colors from what you have seen on the site. Do not invent new colors.
- Match the existing button shape, padding, hover state, and corner radius. If the site uses pill buttons, use pill buttons. If the site uses sharp rectangles, use sharp rectangles.
- Match the existing section padding rhythm (top and bottom space between sections).
- Match the existing corner radius language on cards, images, and containers.
- Match the existing shadow language. If the site uses flat design with no shadows, do not add shadows. If it uses soft shadows, use soft shadows of the same weight.
- Match the existing heading hierarchy and casing (sentence case vs title case vs all caps).
- Match the existing iconography style if icons are used elsewhere (line vs filled, weight, size).
- Match the existing mobile breakpoints and responsive behavior.


If you are uncertain about a specific value, default to the most conservative interpretation of the existing site style rather than introducing something new.


# LIQUID AND SHOPIFY REQUIREMENTS


- Use Shopify section schema settings for every piece of content that the merchant should be able to edit. Nothing should be hardcoded if it would reasonably be edited later (headings, subheadings, body copy, button labels, button links, image fields, colors that the merchant may want to override, toggle visibility for optional elements).
- Use `image_picker` for any images, with `{{ section.settings.image_name | image_url: width: 1600 | image_tag: loading: 'lazy' }}` style rendering. Always include responsive `srcset` and `sizes` attributes where appropriate.
- Use `url` settings for any CTA links and render with `{{ section.settings.button_link }}`.
- Use `richtext` for paragraph copy that may include formatting, and `text` for short single line fields.
- Use `range` or `select` for any numeric or option settings the merchant may want to control (padding, columns, alignment, etc.) where it adds real flexibility, not bloat.
- Use `header` schema entries to logically group settings in the theme editor so the merchant can navigate them easily.
- Wrap the section in a unique class name scoped to this section so styles do not leak. Use a pattern like `.section-{name}-{{ section.id }}` to scope CSS to the specific instance when needed.
- Include `{% schema %}` with `name`, `tag` (usually `section`), `class`, `settings`, and `presets` so the merchant can add this section from the theme editor.
- Use Shopify's standard `padding_top` and `padding_bottom` settings pattern with a range slider (0 to 100, step 4) so the merchant can fine tune vertical rhythm.
- For any color settings, use `color` type so the merchant can pick from their palette.
- Where useful, include a `color_scheme` or `color_background` setting and inline CSS variables so colors update live in the editor.


# RESPONSIVE AND ACCESSIBILITY


- The section must be fully responsive across mobile, tablet, and desktop with a logical breakpoint structure. Use the same breakpoints the rest of the theme uses if known. Default to 749px and 990px if not.
- Use semantic HTML. Headings should use the correct level (h2 for section titles in most cases, h3 for sub items, never skip levels).
- All images must have alt text pulled from a schema setting or from the image object itself.
- Buttons and links must have visible focus states for keyboard navigation.
- Maintain at least WCAG AA color contrast for text against backgrounds.
- All interactive elements must work without JavaScript where possible. If JS is used, it should enhance, not gate functionality.


# CODE QUALITY


- Clean, indented, readable Liquid and CSS.
- No inline styles except for dynamic values pulled from settings (colors, spacing).
- No `!important` unless absolutely required to override a theme conflict, and only with a comment explaining why.
- No external font imports, no external CSS, no external JS libraries.
- Use CSS custom properties scoped to the section for any value that comes from a setting, so the entire section can be themed from a few variables.
- Comment any non obvious logic.


# DEFAULTS AND PRESETS


- Include a `presets` block in the schema so the section can be added from the theme editor with one click.
- All schema settings must have sensible default values so the section looks finished the moment it is added, without requiring the merchant to fill in every field first.
- Default copy should be relevant placeholder text that hints at the purpose of each field (e.g. "Add your headline here" rather than "Lorem ipsum").


# FINAL CHECK BEFORE OUTPUT


Before returning the file, silently confirm:


1. Does this section visually match the store you have been shown? If not, adjust.
2. Are all merchant editable fields wired to schema settings?
3. Does it work at mobile, tablet, and desktop?
4. Does it follow the existing typography, color, button, spacing, and radius language of the site?
5. Will it render correctly the moment it is dropped into the /sections folder and added via the theme editor?


Only output the complete Liquid section file. No explanations.