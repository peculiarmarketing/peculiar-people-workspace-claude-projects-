Source URL: https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/valid-schema
Fetched: 2026-10-03 via curl https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/valid-schema.md (HTTP 200, markdown)

---
title: ValidSchema
description: Identifies invalid JSON in schema tags.
source_url:
  html: >-
    https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/valid-schema
  md: >-
    https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/valid-schema.md
api_name: liquid
---

# Valid​Schema

Identifies invalid JSON in `{% schema %}` tags.

***

## Examples

The following examples contain code snippets that either fail or pass this check.

### ✗ Fail

```liquid
{% schema %}
{
  "comma": "trailing",
}
{% endschema %}
```

### ✓ Pass

```liquid
{% schema %}
{
  "comma": "not trailing"
}
{% endschema %}
```

***

## Options

```yaml
ValidSchema:
  enabled: true
  severity: error
```

| Parameter | Description |
| - | - |
| `enabled` | Whether this check is enabled. |
| `severity` | The [severity](https://shopify.dev/themes/tools/theme-check/configuration#check-severity) of the check. |

***

## Disabling this check

Disabling this check isn't recommended.

***
