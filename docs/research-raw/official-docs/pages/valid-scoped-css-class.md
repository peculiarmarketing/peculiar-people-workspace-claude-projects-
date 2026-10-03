Source URL: https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/valid-scoped-css-class
Fetched: 2026-10-03 via curl https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/valid-scoped-css-class.md (HTTP 200, markdown)

---
title: ValidScopedCSSClass
description: >-
  Warns when a CSS class used in an HTML class attribute might be defined
  outside the current file's scope.
source_url:
  html: >-
    https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/valid-scoped-css-class
  md: >-
    https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/valid-scoped-css-class.md
api_name: liquid
---

# Valid​Scoped​CSSClass

Warns when a CSS class used in an HTML `class` attribute is defined in the theme, but isn't reachable from the current file's scope.

A CSS class is in scope for a file when it's defined in any of the following:

* The file's own `{% stylesheet %}` tag.
* The `{% stylesheet %}` tag of any ancestor file that directly renders this file (through `{% render %}`, `{% section %}`, and so on). The full ancestor chain is traversed, but only `direct` references count-`indirect` and `preset` references don't.
* The `{% stylesheet %}` tag of any snippet that this file (or any of its ancestors) renders through `{% render %}`, including nested snippet descendants.
* Any `.css` file in the theme's `assets/` directory. These are always in scope.

The check doesn't report classes that aren't defined anywhere in the theme, because those might come from external sources, such as CDNs or utility frameworks. It also doesn't report dynamic class attributes that contain Liquid output tags (for example, `class="{{ some_class }}"`), because they can't be analyzed statically.

***

## Examples

The following examples contain code snippets that either fail or pass this check.

### ✗ Fail

In the following example, `other-class` is defined in `snippets/other.liquid`, but that snippet isn't rendered from `sections/section.liquid`, so the class is out of scope:

## sections/section.liquid

```liquid
{% stylesheet %}
  .local-class { color: red; }
{% endstylesheet %}


<div class="other-class">Hello</div>
```

## snippets/other.liquid

```liquid
{% stylesheet %}
  .other-class { color: blue; }
{% endstylesheet %}
```

### ✓ Pass

In the following example, `my-class` is defined in the same file's `{% stylesheet %}` tag:

## sections/section.liquid

```liquid
{% stylesheet %}
  .my-class { color: red; }
{% endstylesheet %}


<div class="my-class">Hello</div>
```

### ✓ Pass

In the following example, `parent-class` is defined in an ancestor file that directly renders the block, so it's in scope for the block:

## sections/section.liquid

```liquid
{% stylesheet %}
  .parent-class { color: red; }
{% endstylesheet %}


{% content_for 'block', type: 'child', id: 'child' %}
```

## blocks/child.liquid

```liquid
<div class="parent-class">Hello</div>
```

### ✓ Pass

In the following example, `asset-class` is defined in a CSS asset file, and in a section file. No warning is displayed in `sections/section1.liquid` because `asset-class` is assumed globally in scope by being defined in the assets folder:

## assets/theme.css

```css
.asset-class { color: red; }
```

## sections/section1.liquid

```liquid
<div class="asset-class">Hello</div>
```

## sections/section2.liquid

```liquid
{% stylesheet %}
  .asset-class { color: blue; }
{% endstylesheet %}


<div class="asset-class">Goodbye</div>
```

### ✓ Pass

In the following example, `shared-style` is defined in a snippet being imported by a parent file, but used the child file `blocks/child.liquid`:

## sections/section.liquid

```liquid
{% render 'shared-styles' %}


{% content_for 'block', type: 'child', id: 'child' %}
```

## blocks/child.liquid

```liquid
<div class="shared-style">Hello</div>
```

## snippets/shared-styles.liquid

```liquid
{% stylesheet %}
  .shared-style { color: red; }
{% endstylesheet %}
```

***

## Options

The following example contains the default configuration for this check:

```yaml
ValidScopedCSSClass:
  enabled: true
  severity: warning
```

| Parameter | Description |
| - | - |
| `enabled` | Whether this check is enabled. |
| `severity` | The [severity](https://shopify.dev/docs/storefronts/themes/tools/theme-check/configuration#check-severity) of the check. |

***

## Disabling this check

You can disable this check if your theme relies heavily on class names that are defined in external stylesheets, inline scripts, or build-time CSS pipelines that the check can't analyze.

***
