Source URL: https://shopify.dev/docs/storefronts/themes/best-practices/performance/use-section-rendering-api
Fetched: 2026-10-03 via curl https://shopify.dev/docs/storefronts/themes/best-practices/performance/use-section-rendering-api.md (HTTP 200, markdown)

---
title: Use the Section Rendering API for dynamic updates
description: >-
  Fetch and replace specific theme sections through Ajax using the Section
  Rendering API instead of triggering full page reloads when content needs to
  update.
source_url:
  html: >-
    https://shopify.dev/docs/storefronts/themes/best-practices/performance/use-section-rendering-api
  md: >-
    https://shopify.dev/docs/storefronts/themes/best-practices/performance/use-section-rendering-api.md
api_name: liquid
---

# Use the Section Rendering API for dynamic updates

Use the [Section Rendering API](https://shopify.dev/docs/api/ajax/section-rendering) to fetch and update specific theme sections through Ajax without a full page reload.

***

## Why

Without the Section Rendering API, updating page content requires a full page reload, which redownloads and re-renders the entire page. This wastes bandwidth and creates slow, jerky user experiences. The Section Rendering API requests only the sections that changed, allowing targeted updates that feel instant and improving metrics for subsequent pages.

***

## How

### Basic usage

Request sections using the `sections` query parameter on any page URL:

```javascript
// Request up to 5 sections at once. Static sections use their filename as the ID,
// and sections in JSON templates or section groups use their dynamic ID.
fetch("/?sections=header,template--123__product-info,cart-drawer")
  .then((response) => response.json())
  .then((data) => {
    // data.header contains rendered HTML for the header section
    // data["template--123__product-info"] contains rendered HTML for the product-info section
    // and so on
  });
```

Requesting more than five sections returns `400 Bad Request` and renders nothing.

Response format:

```json
{
  "header": "<div id=\"shopify-section-header\" class=\"shopify-section\"><!-- HTML content --></div>",
  "template--123__product-info": "<div id=\"shopify-section-template--123__product-info\" class=\"shopify-section\"><!-- HTML content --></div>",
  "cart-drawer": "<div id=\"shopify-section-cart-drawer\" class=\"shopify-section\"><!-- HTML content --></div>"
}
```

### Find section IDs

You can find section IDs in two ways.

Using Liquid:

```liquid
<div data-section-id="{{ section.id }}">
  {%- comment -%} section.id outputs the unique section ID {%- endcomment -%}
</div>
```

From the section wrapper in HTML:

```html
<div id="shopify-section-template--123__product-info" class="shopify-section">
  <!-- The ID is: template--123__product-info -->
</div>
```

Static sections use their filename as the ID: `header.liquid` maps to `header`, and `footer.liquid` maps to `footer`.

Sections in JSON templates and section groups get a dynamic ID instead, such as `template--123__product-info`. Requesting one of those by filename doesn't return the configured section. If a section file with that name exists, then the server renders it statically with default settings, and if it doesn't, then the request fails. On a typical Online Store 2.0 product or collection template, that means a filename-style ID replaces configured page content with default markup or nothing at all. Read the ID from `{{ section.id }}` or from the section wrapper instead of hardcoding it.

### Render sections in different contexts

Sections render in the context of the page URL. You can specify any page context. Read the rendered section ID from the section element rather than hardcoding a filename. Each of the following examples runs on a page that already renders the section it requests:

```javascript
// On a product page: render a different product through the same section
const productSectionId =
  document.querySelector(".product-info").dataset.sectionId;
fetch(`/products/my-product?sections=${productSectionId}`).then((response) =>
  response.json()
);


// On a collection page: render the next page of results
const gridSectionId = document.querySelector(".product-grid").dataset.sectionId;
fetch(`/collections/all?page=2&sections=${gridSectionId}`).then((response) =>
  response.json()
);


// On a search page: render results for a new query
const resultsSectionId =
  document.querySelector(".search-results").dataset.sectionId;
fetch(`/search?q=shoes&sections=${resultsSectionId}`).then((response) =>
  response.json()
);
```

The section ID must exist in the template that renders for the URL you request. A product section ID works for another product that uses the same template, but it doesn't work against a collection or search URL.

### Optimistic cart rendering

When a customer adds a product to the cart, the cart drawer typically opens but shows nothing until the server responds with the Section Rendering API result. You can make add-to-cart feel instant by rendering the cart drawer optimistically with data already available on the product page.

The approach: immediately insert the added item into the cart drawer using product data from the PDP (title, variant, price, image, quantity), then reconcile when the server response arrives. This decouples perceived UI responsiveness from server processing time.

```javascript
function addToCart(variantId, quantity) {
  const product = getProductDataFromPage();


  // Immediately render optimistic cart item
  renderOptimisticCartItem({
    title: product.title,
    variant: product.selectedVariant,
    price: product.price,
    image: product.featuredImage,
    quantity: quantity,
  });
  openCartDrawer();


  // Fetch the real server-rendered cart sections
  fetch("/cart/add.js", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      items: [{ id: variantId, quantity }],
      sections: "cart-drawer,cart-icon-bubble",
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      // Replace optimistic content with server-rendered HTML
      replaceCartSections(data.sections);
    });
}
```

The server response reconciles any differences, such as discount pricing, stock changes, or cart-level promotions that only the server knows about.

### Bundled section rendering with the Cart API

The Cart API supports bundled section rendering, so that you can update multiple sections after cart modifications:

```javascript
fetch("/cart/add.js", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    items: [{ id: 39072856, quantity: 1 }],
    sections: "cart-drawer,cart-icon-bubble,cart-footer",
  }),
})
  .then((response) => response.json())
  .then((data) => {
    // data.items contains the cart data
    // data.sections["cart-drawer"] contains rendered cart drawer HTML
    // data.sections["cart-icon-bubble"] contains rendered cart icon HTML
    // and so on
  });
```

### Use locale-aware URLs

When building Section Rendering API requests, use locale-aware URLs to maintain the customer's selected language and region:

```javascript
// Good: use window.Shopify.routes.root for locale awareness
fetch(window.Shopify.routes.root + "?sections=header").then((response) =>
  response.json()
);


// Good: or use the current page context
fetch(window.location.pathname + "?sections=product-info").then((response) =>
  response.json()
);
```

### Single section request (alternative)

For a single section, you can use the `section_id` parameter. It returns HTML directly instead of JSON:

```javascript
// Returns HTML directly, not JSON. `routes.root` keeps the request locale-aware.
fetch(`${window.Shopify.routes.root}?section_id=header`)
  .then((response) => response.text())
  .then((html) => {
    document.querySelector("#header").innerHTML = html;
  });
```

This returns a `404` if the section doesn't exist. The `404` applies only to the `section_id` path. A nonexistent section ID inside `?sections=` is `null` in an otherwise successful `200` response, so requesting several sections at once never fails outright because of one bad ID.

**Caution:**

`<script>` tags in the returned HTML don't execute when you insert them with `innerHTML`, `DOMParser`, or `replaceWith`. You must bind any behavior that the section needs outside the replaced markup, either by delegating events from an ancestor that's never replaced, or by wrapping the section in a custom element and re-initializing in `connectedCallback()`.

***

## Examples

### Variant selection

Update product details when a customer selects a different variant:

## sections/product-info.liquid

```liquid
<div class="product-info" data-section-id="{{ section.id }}">
  <h1>{{ product.title }}</h1>
  <div class="price">{{ product.selected_or_first_available_variant.price | money }}</div>
  <div class="inventory">
    {% if product.selected_or_first_available_variant.available %}
      In stock
    {% else %}
      Out of stock
    {% endif %}
  </div>


  {%- comment -%} Option picker {%- endcomment -%}
  {%- for option in product.options_with_values -%}
    <fieldset>
      <legend>{{ option.name }}</legend>
      {%- for option_value in option.values -%}
        <label>
          {%- comment -%}
            Emit `checked` from `option_value.selected`. The JS rebuilds `option_values`
            from the checked inputs, so a picker that comes back with nothing checked
            would drop every option the customer didn't just click.
          {%- endcomment -%}
          <input
            type="radio"
            name="{{ option.name }}"
            value="{{ option_value | escape }}"
            data-option-value-id="{{ option_value.id }}"
            {% if option_value.selected %}checked{% endif %}
          />
          {{ option_value }}
        </label>
      {%- endfor -%}
    </fieldset>
  {%- endfor -%}
</div>


<script>
  {%- comment -%}
    Delegate from `document`, which is never replaced. Listeners bound directly
    to the inputs would be lost the first time `.product-info` is swapped out,
    and the script in the fetched section doesn't execute to rebind them.
  {%- endcomment -%}
  document.addEventListener('change', (event) => {
    if (!event.target.matches('.product-info input[data-option-value-id]')) return;
    updateProduct(event.target.closest('.product-info'));
  });


  function updateProduct(container) {
    const sectionId = container.dataset.sectionId;
    const selectedOptions = Array.from(
      container.querySelectorAll('input[data-option-value-id]:checked')
    ).map(input => input.dataset.optionValueId);


    const params = `section_id=${sectionId}&option_values=${selectedOptions.join(',')}`;


    fetch(`${window.location.pathname}?${params}`)
      .then(response => response.text())
      .then(html => {
        const parser = new DOMParser();
        const doc = parser.parseFromString(html, 'text/html');
        const newContent = doc.querySelector('.product-info');


        container.replaceWith(newContent);
      });
  }
</script>
```

Scope every query to the section container. A bare `document.querySelectorAll('input[name]')` also matches search, newsletter, and quantity inputs elsewhere on the page.

For a component-based alternative, see how Dawn's `variant-selects` custom element binds its `change` listener in `connectedCallback()`, so the listener re-attaches automatically each time the element is replaced.

### Error handling

In a `?sections=` request, sections that fail to render or don't exist come back as `null` inside a `200` response. Always account for this:

```javascript
fetch("/?sections=header,footer,missing-section")
  .then((response) => response.json())
  .then((data) => {
    if (data.header) {
      // Update header
    }
    if (data.footer) {
      // Update footer
    }
    if (!data["missing-section"]) {
      console.error("Section failed to render or doesn't exist");
    }
  });
```

***

## Testing

* **Browser DevTools Network tab**: Verify that only sections are fetched, not full pages.
* **Compare sizes**: Check the network payload. The section response should be smaller than a full page.
* **User experience**: Interactions should feel instant with no page flash.

***

## References

* [`section.id`](https://shopify.dev/docs/api/liquid/objects/section#section-id)
* [`product.title`](https://shopify.dev/docs/api/liquid/objects/product#product-title)
* [`product.selected_or_first_available_variant`](https://shopify.dev/docs/api/liquid/objects/product#product-selected_or_first_available_variant)
* [`product.options_with_values`](https://shopify.dev/docs/api/liquid/objects/product#product-options_with_values)
* [`product_option_value`](https://shopify.dev/docs/api/liquid/objects/product_option_value) object
* [`money`](https://shopify.dev/docs/api/liquid/filters/money) filter
* [`escape`](https://shopify.dev/docs/api/liquid/filters/escape) filter
* [`for`](https://shopify.dev/docs/api/liquid/tags/for) tag
* [`if`](https://shopify.dev/docs/api/liquid/tags/if) tag
* [Section Rendering API](https://shopify.dev/docs/api/ajax/section-rendering)
* [Ajax API](https://shopify.dev/docs/api/ajax)
* [Bundled section rendering with Cart API](https://shopify.dev/docs/api/ajax/reference/cart#bundled-section-rendering)
* [Avoid over-fetching product variants](https://shopify.dev/docs/storefronts/themes/best-practices/performance/avoid-variant-overfetching)
* [Defer child product loading in combined listings](https://shopify.dev/docs/storefronts/themes/best-practices/performance/defer-combined-listing-products)
* [Limit pagination depth](https://shopify.dev/docs/storefronts/themes/best-practices/performance/limit-pagination-depth)

***
