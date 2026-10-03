# Companion: Lookbook Gallery repo (video tXkpsim6sfI)

- Source: https://github.com/BeauchampAndrew/shopify-lookbook-gallery (README.md, AGENTS.md via raw.githubusercontent.com, main branch)
- Fetched: 2026-10-03 with curl
- Also inspected sections/lookbook-gallery.liquid (49.6 KB): schema parses as valid JSON; name 'Lookbook gallery'; 48 section settings grouped under headers; one block type 'look' (image_picker, product_list, title, subtitle, richtext, button label/link, custom anchor); presets present. File itself not saved here.

## README.md

# Lookbook Gallery for Shopify

A shoppable lookbook section for any Shopify theme. Shoppers click a look, see every product in it, pick a size and add to cart without leaving the page.

It's one file. No app, no monthly fee, no code knowledge needed to install it.

**Using Claude Code, Cursor or another AI coding tool?** Point it at this repo and tell it what you want, like "install this in my theme" or "make the popup image go on the right and add a quantity picker". [AGENTS.md](AGENTS.md) tells it how the section works and how to change it without breaking it in other themes.

## What it does

- Grid of look photos. Clicking one opens a popup with the photo and every product in that look.
- **Quick add:** shoppers choose a size and add to cart right in the popup, then keep browsing other looks. Out-of-stock sizes are crossed out.
- Arrows (and keyboard arrow keys) to move between looks.
- Every look has its own link, like `yourstore.com/pages/lookbook#look-3`. Use these in emails and ads to open a specific look.
- Matches your theme's fonts, colors and headings automatically.
- Works on mobile. The popup slides up from the bottom of the screen.
- Everything is adjustable in the theme editor: columns, image shape, spacing, popup size, colors, labels and more.

## Install it (about 5 minutes, no coding)

You need a Shopify theme that supports sections on every page ("Online Store 2.0"). Every free Shopify theme made since 2021 does, including Horizon and Dawn.

**Tip:** do this on a copy of your theme first. In **Online Store > Themes**, click **...** next to your theme and choose **Duplicate**. Try it there, then publish the copy when you're happy.

### Step 1: Add the section file

1. Open [`sections/lookbook-gallery.liquid`](sections/lookbook-gallery.liquid) here on GitHub and click the **Copy raw file** button (the two-squares icon at the top right of the file).
2. In your Shopify admin, go to **Online Store > Themes**. Next to your theme, click **...** then **Edit code**.
3. In the file list on the left, find the **Sections** folder and click **Add a new section**.
4. Name it `lookbook-gallery` and pick **Liquid** if it asks.
5. Delete everything in the new file, paste what you copied, and click **Save**.

### Step 2: Make a lookbook page

1. Go to **Online Store > Themes** and click **Customize**.
2. In the dropdown at the top of the screen, choose **Pages**, then **Create template**. Name it `lookbook` and click **Create template**.
3. In the left sidebar, click **Add section** and choose **Lookbook gallery**. You can remove the page's default sections if you don't want them.
4. Click **Save**.
5. Go to **Online Store > Pages > Add page**. Give it a title (like "Lookbook"), set **Theme template** to `lookbook`, and save.

Your lookbook is live at `yourstore.com/pages/lookbook` (or whatever you named the page).

### Step 3: Add your looks

In the theme editor, open the Lookbook gallery section. Each **Look** is a block. For each one:

- **Look photo:** upload the outfit photo.
- **Products in this look:** pick the products shoppers can buy.
- **Title, subtitle, description:** optional. Shown in the popup.

Click **Add Look** for more. Drag looks to reorder them. When you select a look in the editor, its popup opens so you can see what you're editing.

## Link straight to a look

Each look has a link that opens its popup when the page loads:

```
yourstore.com/pages/lookbook#look-1
yourstore.com/pages/lookbook#look-2
```

Great for "Look of the Week" emails. To use your own names (like `#summer-linen`), fill in **Custom link anchor** on the look.

## Settings

Everything lives in the theme editor. The main ones:

| Group | What you can change |
|---|---|
| Heading | Heading text, intro text, size, alignment |
| Layout | Page width or full width, columns on desktop and mobile, spacing |
| Look cards | Image shape (tall, portrait, square, landscape, or original), rounded corners, hover effect, look titles, "Shop the look" hover label |
| Popup | Image on left or right, width, height, arrows, colors, background dimming |
| Products in popup | Quick add or link to product page, image size and shape, vendor, price, all button labels |

The popup matches your page's background and text color by default. Set **Popup background** and **Popup text** only if you want something different.

## Quick add and your cart icon

Adding to cart works in every theme. Updating the cart icon in your header depends on the theme:

| Theme | Cart count updates? | Cart drawer |
|---|---|---|
| Horizon and other themes using Shopify's standard cart events | Yes (tested on Horizon) | Opens after the shopper closes the lookbook |
| Dawn, and themes built on Dawn (Sense, Craft, Refresh, Studio, and others) | Should update (not yet tested) | No |
| Other themes | After the next page load | No |

If you prefer shoppers go to the product page instead, set **When a shopper picks a product** to **Go to product page**.

**For developers:** after every add, the section fires `lookbook:cart:added` on `document` with `{ variantId, cart }` in `event.detail`. Listen for it to refresh your theme's cart UI.

```js
document.addEventListener('lookbook:cart:added', (event) => {
  // event.detail.cart is the full /cart.js response
});
```

## Troubleshooting

**"Lookbook gallery" isn't in the Add section list.**
Check the file is in the **Sections** folder and named exactly `lookbook-gallery.liquid`. If your theme is older than 2021, it may not support sections on pages.

**The `lookbook` template isn't in the page's Theme template dropdown.**
The dropdown only shows templates from your **published** theme. If you built the template on a theme copy, publish that copy first, or add the section to your live theme too.

**My cart icon doesn't update after adding.**
See [Quick add and your cart icon](#quick-add-and-your-cart-icon). The item is in the cart, and the icon catches up on the next page load.

**A look shows a product photo instead of my look photo.**
The look has no photo set, so it falls back to its first product's image. Pick a **Look photo** for that look.

## Try the demo

The `demo` folder has everything used to build the demo store: 27 clothing products and 9 filled-in looks. It's handy for testing on a development store.

1. **Products:** in **Products > Import**, upload [`demo/products.csv`](demo/products.csv). The product photos load from Shopify's free [Burst](https://burst.shopify.com) library.
2. **Look photos:** in **Content > Files**, upload the 9 images from [`demo/look-images`](demo/look-images). Keep the filenames.
3. **Template:** in **Edit code**, create a page template named `lookbook` (choose JSON) and paste in [`demo/page.lookbook.json`](demo/page.lookbook.json). Then create a page that uses it, as in step 2 above.

To change the demo catalog, edit `demo/build_products_csv.py` and run `python3 demo/build_products_csv.py`.

Demo photos are from [Burst](https://burst.shopify.com), free for commercial use.

## Install with Shopify CLI

If you use the CLI, copy `sections/lookbook-gallery.liquid` into your theme's `sections` folder and push:

```bash
shopify theme push --only sections/lookbook-gallery.liquid
```

## License

MIT. Use it, change it, sell stores with it. See [LICENSE](LICENSE).

## AGENTS.md

# Agent guide: Lookbook Gallery for Shopify

Instructions for AI coding agents (Claude Code, Cursor, Codex, etc.) installing or customizing this section. Humans should start with [README.md](README.md).

## What this is

A single Shopify theme section, `sections/lookbook-gallery.liquid`. It renders a grid of "looks". Clicking a look opens a `<dialog>` with the look photo and its products, with inline quick add to cart. It is built to drop into **any** Online Store 2.0 theme without changes.

```
sections/lookbook-gallery.liquid   The product. Markup, CSS, JS and schema in one file.
demo/page.lookbook.json            Example page template (demo store handles and image filenames)
demo/products.csv                  27-product demo catalog for Products > Import
demo/build_products_csv.py         Generates products.csv
demo/look-images/                  9 look photos (Burst, free commercial use)
```

## Installing into a theme

With Shopify CLI, from the user's theme directory:

1. Copy `sections/lookbook-gallery.liquid` into the theme's `sections/` folder.
2. Create a page template. Minimal `templates/page.lookbook.json`:
   ```json
   {
     "sections": {
       "main": {
         "type": "lookbook-gallery",
         "blocks": {
           "look_1": { "type": "look", "settings": { "title": "Look 1", "products": ["product-handle-a", "product-handle-b"] } }
         },
         "block_order": ["look_1"],
         "settings": { "heading": "Lookbook" }
       }
     },
     "order": ["main"]
   }
   ```
   `products` takes product **handles**. `image` takes `shopify://shop_images/<filename>` and only works for files already uploaded to the store's **Content > Files**. You cannot upload Files with the CLI. Leave `image` out and the look falls back to its first product's image.
3. Push to an **unpublished** theme first: `shopify theme push --unpublished --theme "With lookbook"`, or `--only sections/lookbook-gallery.liquid --only templates/page.lookbook.json` against an existing theme ID.
4. Ask the human before pushing to the live theme (`--allow-live`).
5. The human creates the page: **Online Store > Pages > Add page**, Theme template `lookbook`.

The page template dropdown only lists templates from the **published** theme. If the user can't find `lookbook` there, the template is only in an unpublished theme.

## Hard rules when changing the section

These keep it portable. Breaking one usually works in the theme you're testing and fails in every other theme.

1. **Stay one file.** CSS goes in `{% stylesheet %}`, JS in `{% javascript %}`. No new files in `assets/` or `snippets/`. Note that `{% stylesheet %}` and `{% javascript %}` can't contain Liquid; pass values through CSS variables or `data-` attributes instead.
2. **No theme dependencies.** Don't use a theme's classes (`page-width`, `color-scheme-1`, `grid__item`), CSS variables (`--color-background`, `--font-body-family`) or JS (`publish()`, theme components) for core behavior. Theme-specific hooks are allowed only as optional extras, feature-detected, like the ones in `notifyTheme()`.
3. **Prefix everything.** Classes are `lbg__*` (BEM style) and modifiers `lbg--*`. Data attributes are `data-lbg-*`. CSS variables are `--lbg-*`. The custom element is `<lookbook-gallery>`. Many themes ship their own "lookbook" classes, so don't use bare `.lookbook`.
4. **Size text in `em`.** Themes set different root sizes (Dawn uses 62.5% so 1rem = 10px, Horizon uses 16px). `rem` breaks in one or the other. Use `px` only for fixed UI like icons, hit targets and borders.
5. **Colors come from the page.** Inside the popup use `var(--lbg-fg)` and `var(--lbg-bg)`. They resolve to the merchant's setting, otherwise the colors `detectColors()` reads from the page at runtime. Don't hard-code colors other than neutral overlays.
6. **Every visual choice a merchant might want to change is a setting.** Every shopper-facing string is a setting too (so merchants can translate it), passed to JS through a `data-label-*` attribute on the root element. The aria-labels (`Close`, `Previous look`, `Next look`) are the one exception so far.
7. **Guard the element definition**: `if (!customElements.get('lookbook-gallery'))`. The section can appear more than once on a page.

## How the file is laid out

Top to bottom:

1. **Liquid setup** (`{%- liquid -%}` block): turns settings into values, such as the aspect ratio strings, thumbnail width, max width and anchor prefix.
2. **Root element** `<lookbook-gallery>`: carries every layout setting as an inline CSS variable (`--lbg-cols-d`, `--lbg-ratio`, `--lbg-popup-w`, ...), and the cart URLs and labels as `data-*` attributes for JS. Behavior toggles are modifier classes (`lbg--hover-zoom`, `lbg--natural`, `lbg--cta-button`, `lbg--popup-image-right`).
3. **Grid**: one `<button data-lbg-open="{index}">` per block.
4. **Dialog**: **one** `<dialog class="lbg__dialog">` for the whole section, containing one `<article data-lbg-panel>` per look. Only one panel is visible at a time (`hidden` attribute). Each panel holds the image, arrows, text, product list and the bag bar.
5. **Product rows**: two variants, switched by the `product_action` setting.
   - `quick_add`: image and title link to the PDP. Below them are option chips (`fieldset[data-lbg-option]` > `button[data-lbg-chip]`), an add button (`[data-lbg-add]`), a status line and a `<script type="application/json" data-lbg-variants>` with `{id, available, options[], image?}` per variant.
   - `link`: the whole row is an `<a>` to the PDP.
6. **`{% stylesheet %}`**: mobile first. The dialog is a bottom sheet under 750px and a centered two-column modal at 750px and up. The grid switches columns at 750px and 990px.
7. **`{% javascript %}`**: the `LookbookGallery` class, described below.
8. **`{% schema %}`**: section settings, grouped under headers, plus one block type `look`.

### JavaScript (`LookbookGallery`)

| Method | Job |
|---|---|
| `connectedCallback` / `disconnectedCallback` | Wire and unwire listeners. Opening a look from the URL hash happens here too |
| `detectColors` | Walks up from the element to find the first non-transparent background, sets `--lbg-auto-bg` and `--lbg-auto-fg` |
| `onClick` | One delegated handler for open, chip, add, close, prev and next, plus backdrop clicks |
| `open(index)` / `step(delta)` / `close()` / `onClosed()` | Show a panel, sync the URL hash with `history.replaceState`, lock page scroll, restore focus on close |
| `openFromHash` | Opens the panel whose `data-anchor` matches `location.hash` (deep links like `#look-3`) |
| `selectBlock` | Theme editor: opens the look the merchant selected |
| `variantsFor` / `selectionFor` / `selectChip` / `syncProduct` | Variant picking. `syncProduct` crosses out values with no in-stock variant given the other chosen options, and sets the add button label, `disabled` and `data-variant-id` |
| `addToCart` | See below |
| `fetchCart` / `toStandardCart` | Read `/cart.js` and convert it to the Shopify standard-events cart shape |
| `notifyTheme` | Tells the theme the cart changed. **Add support for more themes here** |
| `refreshBag` / `showBag` | The "N in your bag · View bag" bar |

### Cart flow (`addToCart`)

1. Create a promise and dispatch `shopify:cart:lines-update` (`action: 'add'`, `context: 'dialog'`, `lines` with a `gid://shopify/ProductVariant/{id}` merchandise ID, `promise`) **from the add button**, not from `document`. Themes on Shopify's standard events (Horizon) update their cart icon and cart drawer from that promise. Because the event starts inside an open modal dialog, Horizon's cart drawer waits for the lookbook to close before auto-opening. Dispatching from `document` would open the drawer on top of the popup.
2. `POST {routes.cart_add_url}.js` with `{ items: [{ id, quantity: 1 }], sections: 'cart-icon-bubble' }`.
3. `GET /cart.js`, resolve the promise with `{ cart: toStandardCart(cart), detail: { itemCount } }`. On failure, reject it and show the error in `[data-lbg-status]`.
4. `notifyTheme()`: swaps in the re-rendered `#cart-icon-bubble` (Dawn family), calls `window.publish('cart-update', ...)` if the theme defines it (Dawn pub/sub), then dispatches `lookbook:cart:added` on `document` with `{ variantId, cart }`.

To support another theme's cart drawer or icon, add a feature-detected branch to `notifyTheme()`. Find what the theme's own product form does after adding to cart (search its assets for `cart/add` or its add-to-cart handler) and repeat that. Don't remove the existing branches.

## Common changes

- **New setting:** add it to `{% schema %}` under the right header. Read it through `s.<id>` (`assign s = section.settings`). For layout values, add a `--lbg-*` variable on the root element and use it in the CSS. For JS, add a `data-*` attribute on the root element.
- **New shopper-facing text:** schema `text` setting with a default. Render it in Liquid, or pass it as `data-label-*` and read it with `this.dataset.label*`.
- **Popup layout:** desktop rules are in the `@media screen and (min-width: 750px)` block (`.lbg__panel:not([hidden])` is the two-column grid). Mobile is everything outside the media queries.
- **Product row content:** edit the `quick_add` branch and the `link` branch in the product loop. Both exist, so change both if the change applies to both.
- **Quantity picker, "add whole look", hotspots on the photo:** not built yet. Keep new controls inside the panel, use the `lbg__` prefix, route adds through `addToCart` (or a sibling that reuses its event dispatch and `notifyTheme`) so every theme keeps syncing.

## Gotchas

- The sticky bag bar (`.lbg__bag`) uses negative margins and a negative `bottom` that exactly cancel the panel body's padding. If you change `.lbg__panel-body` padding, change `.lbg__bag` to match, or the bar floats above the popup's bottom edge with content showing underneath.
- `image_picker` values must be files in the store's Files. `product_list` is capped at `limit: 25` here (Shopify allows up to 50).
- Section JS and CSS are bundled by Shopify. After adding the section in the theme editor, a merchant may need to save and refresh before the popup works in the preview.
- `{% javascript %}` runs once per page, not once per section. Per-instance state lives on the element.
- Test hash deep links by loading `/pages/<handle>#look-2` directly, not only by clicking.

## Before you hand back

1. **Schema is valid JSON:**
   ```bash
   python3 -c "import re,json;s=open('sections/lookbook-gallery.liquid').read();json.loads(re.search(r'{% schema %}(.*?){% endschema %}',s,re.S).group(1));print('ok')"
   ```
2. **JS parses:**
   ```bash
   python3 -c "import re;s=open('sections/lookbook-gallery.liquid').read();open('/tmp/lbg.js','w').write(re.search(r'{% javascript %}(.*?){% endjavascript %}',s,re.S).group(1))" && node --check /tmp/lbg.js
   ```
3. **Theme check passes**, run inside a full theme (it needs `locales/` and `config/`): copy the section into a pulled theme and run `shopify theme check`. Only look at offenses for `lookbook-gallery.liquid`, because themes ship with their own.
4. **Manual test on a dev store:** grid renders, popup opens and closes (button, Esc, backdrop), arrows cycle, `#look-2` opens on load, chips cross out sold-out values, add to cart updates the header count, bag bar sits flush at the bottom, mobile bottom sheet scrolls. If it's a Dawn-family theme, check the cart bubble too.
5. **Keep the docs in sync:** new settings or behavior go in README.md (for merchants) and this file (for agents).
