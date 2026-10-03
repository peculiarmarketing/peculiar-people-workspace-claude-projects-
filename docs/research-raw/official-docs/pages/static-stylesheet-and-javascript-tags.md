Source URL: https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/static-stylesheet-and-javascript-tags
Fetched: 2026-10-03 via curl https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/static-stylesheet-and-javascript-tags.md (HTTP 200, markdown)

---
title: StaticStylesheetAndJavascriptTags
description: >-
  Warns if Liquid code is used inside a `{% stylesheet %}` or `{% javascript %}`
  tag.
source_url:
  html: >-
    https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/static-stylesheet-and-javascript-tags
  md: >-
    https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/static-stylesheet-and-javascript-tags.md
api_name: liquid
---

# Static​Stylesheet​And​Javascript​Tags

Warns if Liquid code is used inside a `{% stylesheet %}` or `{% javascript %}` tag. Liquid code isn't supported within these tags, and this check helps you quickly spot and avoid potential issues.

***

## Examples

The following examples show code that fails or passes this check.

### ✗ Fail

In the following example, Liquid code is used inside a `{% stylesheet %}` tag, which is not allowed:

```liquid
{% stylesheet %}
.button {
  background-color: {{ settings.button_color }};
  color: white;
}
{% endstylesheet %}
```

### ✗ Fail

In the following example, Liquid code is used inside a `{% javascript %}` tag, which is also not allowed:

```liquid
{% javascript %}
var themeColor = "{{ settings.theme_color }}";
{% endjavascript %}
```

### ✓ Pass

In the following example, no Liquid code is present inside the `{% stylesheet %}` tag, which is the correct usage:

```liquid
{% stylesheet %}
.button {
  background-color: #333;
  color: white;
}
{% endstylesheet %}
```

### ✓ Pass

Similarly, in this example, no Liquid code appears in the `{% javascript %}` tag:

```liquid
{% javascript %}
var themeColor = "#333333";
{% endjavascript %}
```

***

## Options

The following example shows the default configuration for this check:

```yaml
StaticStylesheetAndJavascriptTags:
  enabled: true
  severity: error
```

| Parameter | Description |
| - | - |
| `enabled` | Whether this check is enabled. |
| `severity` | The [severity](https://shopify.dev/docs/storefronts/themes/tools/theme-check/configuration#check-severity) of the check. |

***

## Disabling this check

Disabling this check is not recommended, as using Liquid inside `{% stylesheet %}` or `{% javascript %}` tags can lead to errors in your theme.

***
