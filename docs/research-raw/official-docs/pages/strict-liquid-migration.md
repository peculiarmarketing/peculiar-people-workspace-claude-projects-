Source URL: https://shopify.dev/docs/storefronts/themes/tools/strict-liquid-migration
Fetched: 2026-10-03 via curl https://shopify.dev/docs/storefronts/themes/tools/strict-liquid-migration.md

---
title: Migrate to Liquid's strictest parser
description: >-
  Tips on migrating your theme or theme app extension to Liquid's strictest
  error mode.
source_url:
  html: 'https://shopify.dev/docs/storefronts/themes/tools/strict-liquid-migration'
  md: 'https://shopify.dev/docs/storefronts/themes/tools/strict-liquid-migration.md'
api_name: liquid
---

# Migrate to Liquid's strictest parser

Liquid now ships with a stricter error mode. Previously, Liquid would allow certain code patterns which appear to be well formed, but which the language doesn't yet support. Liquid's parser would accept this code, but evaluate it incorrectly.

To develop the Liquid language so that these types of code patterns can be supported in the future, we’ve updated the parser to be stricter about the code it accepts.

For example, instead of accepting `assign x = false or true` and evaluating `x` to be false, the new stricter error mode reports that this code can’t be parsed. This change means that we’ll be able to update Liquid in the future so it can accept `assign x = false or true` and correctly evaluate the expression to `true`.

In the following example, the previous parser would suppress the syntax error caused by trying to assign a logical expression to a variable and would never render Important content.

## snippets/example.liquid

```liquid
{% assign x = false or true %}
{% if x %}
  Important content
{% endif %}
```

We've put together a list of common errors we've seen across themes and theme app extensions to help the transition:

***

## Expected end\_​of\_​string but found pipe

### Filters in render tags

Using filters outside of variable output, assign and the echo tag throws a syntax error:

## snippets/example.liquid

```liquid
{% render 'image', image: image, alt: image.alt | escape %}
```

Fix by pulling the filter outside of the render tag and into its own variable:

## snippets/example.liquid

```liquid
{% assign alt_text = image.alt | escape %}
{% render 'image', image: image, alt: alt_text %}
```

***

## Expected end\_​of\_​string but found comparison

### Conditional expressions in render tags

Using conditional expressions as a value for a render argument throws a syntax error:

## snippets/example.liquid

```liquid
{%
  render 'product-card',
  product: product,
  show_description: settings.x or settings.y,
%}
```

Fix by wrapping the render tag with the conditional expression:

## snippets/example.liquid

```liquid
{% if settings.x or settings.y %}
  {%
    render 'product-card',
    product: product,
    show_description: true,
  %}
{% endif %}
```

***

## Expected end\_​of\_​string but found colon

### Using `with` with key value pairs

You can pass a single object to a snippet using the `with` parameter but also including a key value pair causes a syntax error:

## snippets/example.liquid

```liquid
{% render 'icon' with style: 'lock' %}
```

Fix by removing `with`:

## snippets/example.liquid

```liquid
{% render 'icon', style: 'lock' %}
```

Another version of this error you might see is raised as `[:colon, ":"] is not a valid expression` which you'll see if you use a colon immediately after `with`. Similarly to above, fix by removing `with:`:

## snippets/example.liquid

```diff
- {% render 'icon', with: style: 'lock' %}
+ {% render 'icon', style: 'lock' %}
```

If you want to keep the behavior of `with` (which in the error example above assigns the value of `style` to `icon`, [see documentation](https://shopify.dev/docs/api/liquid/tags/render#render-with) for more details) then you can specify it like this:

## snippets/example.liquid

```liquid
{% assign style = 'lock' %}
{% render 'icon' with style %}
```

### Malformed arguments in render tag

Missing a value for the `responsive` attribute:

## snippets/example.liquid

```liquid
{% render 'image', lazyload: lazyload, responsive: width: 500 %}
```

Fix by adding a value for `responsive`:

## snippets/example.liquid

```liquid
{% render 'image', lazyload: lazyload, responsive: true, width: 500 %}
```

***

## Expected end\_​of\_​string but found id

### Logical operators in variable assignments

Logical operators can only be used in `if` statements. The following throws a syntax error:

## snippets/example.liquid

```liquid
{% liquid
  assign x = settings.y or settings.z


  if x
    # logic
  endif
%}
```

Fix by moving the conditional expression into the `if` statement:

## snippets/example.liquid

```liquid
{% liquid
  if settings.y or settings.z
    # logic
  endif
%}
```

### Logical operators in case statements

Just like variables, case statements can't use logical operators:

## snippets/example.liquid

```liquid
{% liquid
case template.name
when 'product'
  # product logic
when 'collection' and settings.x
  # collection logic
else
  # all other templates
endcase %}
```

Depending on the scenario you might need to rework your business logic but the example above could be refactored to be like this:

## snippets/example.liquid

```liquid
{% liquid
case template.name
when 'product'
  # product logic
when 'collection'
  if settings.x
    # collection logic
  endif
else
  # all other templates
endcase %}
```

***

## Expected colon but found end\_​of\_​string

### Malformed arguments passed to render tag

## snippets/example.liquid

```liquid
{% render 'image', lazyload: lazyload, responsive %}
```

Fix by adding a value for `responsive`:

## snippets/example.liquid

```liquid
{% render 'image', lazyload: lazyload, responsive: true %}
```

***

## Expected colon but found comma

### Malformed arguments passed to render tag

## snippets/example.liquid

```liquid
{% render 'related-products', product, collection %}
```

Variables passed to a snippet need to be formatted as key value pairs:

## snippets/example.liquid

```liquid
{% render 'related-products', product: product, collection: collection %}
```

***

## Unexpected characters

This is an all encompassing error that can sometimes be hard to parse where the exact issue is. In most cases the problem is a typo but the line number on the error should help point you to the exact spot. Provided are some common examples we've seen but this isn't an exhaustive list:

### Conditional expressions using `&&` and `||` instead of `and` and `or`

Conditional expressions in Liquid use `and` and `or`. Using `&&` and `||` throws a syntax error:

## snippets/example.liquid

```liquid
{% liquid
  if responsive && settings.x || settings.y
    render 'responsive-image', image: image
  endif
%}
```

Fix by using Liquid's boolean operators:

## snippets/example.liquid

```liquid
{% liquid
  if responsive and settings.x or settings.y
    render 'responsive-image', image: image
  endif
%}
```

### Conditional expressions using parentheses

Using parentheses to group conditional expressions throws a syntax error:

## snippets/example.liquid

```liquid
{% liquid
  if responsive and (settings.x or settings.y)
    render 'responsive-image', image: image
  endif
%}
```

Fix by removing the parentheses (and read the [documentation](https://shopify.dev/docs/api/liquid/basics#order-of-operations) on the order in which Liquid parses conditional expressions):

## snippets/example.liquid

```liquid
{% liquid
  if responsive and settings.x or settings.y
    render 'responsive-image', image: image
  endif
%}
```

### Invalid expressions used in case statement

The following results in `Liquid syntax error (line 3): Unexpected character =`:

## snippets/example.liquid

```liquid
{% liquid
  case media.preview_image.width
    when => 550
      assign media_largest = media.preview_image | image_url: width: 550 | append: '550w'
    when => 1100
      assign media_largest = media.preview_image | image_url: width: 1100 | append: '1100w'
    # etc...
  endcase
%}
```

To fix this remove the `=>`:

## snippets/example.liquid

```liquid
{% liquid
  case media.preview_image.width
    when 550
      assign media_largest = media.preview_image | image_url: width: 550 | append: '550w'
    when 1100
      assign media_largest = media.preview_image | image_url: width: 1100 | append: '1100w'
    # etc...
  endcase
%}
```

### Comments must be written on their own line

The following results in `Liquid syntax error (line 5): Unexpected character #`:

## snippets/example.liquid

```liquid
{% liquid
  case media.preview_image.width
    when 550
      assign media_largest = media.preview_image | image_url: width: 550 | append: '550w'
    when 1100 # this is a comment about this size
      assign media_largest = media.preview_image | image_url: width: 1100 | append: '1100w'
    # etc...
  endcase
%}
```

To fix this, move the comment to its own line:

## snippets/example.liquid

```liquid
{% liquid
  case media.preview_image.width
    when 550
      assign media_largest = media.preview_image | image_url: width: 550 | append: '550w'
    when 1100
      # this is a comment about this size
      assign media_largest = media.preview_image | image_url: width: 1100 | append: '1100w'
    # etc...
  endcase
%}
```

***

## `[:end_of_string]` is not a valid expression

### Malformed arguments passed to render tag

## snippets/example.liquid

```liquid
{% render 'icon', style: %}
```

Fix by adding a value for `style:`:

## snippets/example.liquid

```liquid
{% render 'icon', style: 'lock' %}
```

***

## Bare bracket access is not allowed

### Global lookups using bare brackets

In the previous parser, an expression could start with a square bracket, and Liquid looked the key inside it up in the current scope. We're reserving square brackets for array literal syntax, so the stricter parser rejects an expression that starts with one:

## snippets/example.liquid

```liquid
{% assign key = 'product' %}
{% assign global_lookup = [key] %}
```

Fix by putting `self` in front of the bracket. The `self` object resolves the key through the same variable lookup chain that the bare bracket used, so the behavior doesn't change:

## snippets/example.liquid

```liquid
{% assign key = 'product' %}
{% assign global_lookup = self[key] %}
```

This applies to literal keys too, so `{{ ['product'] }}` becomes `{{ self['product'] }}`.

Bracket access that already has an object in front of it, such as `product['title']` or `products[key]`, is unaffected.

Depending on which version of the parser reported it, you might see this error as `Bare bracket access is not allowed. Use self['...'] instead` or as `Bare bracket access is not allowed in strict2 mode`.

***
