URL: https://community.shopify.com/t/looking-for-a-good-size-chart-app-that-does-what-i-need/653757
JSON: https://community.shopify.com/t/653757.json
HTTP status: 200
Fetched: 2026-10-03 via curl (Discourse topic JSON)
Title: Looking for a good size chart app that does what I need
Created: 2026-07-22T08:18:47.054Z
Last posted: 2026-09-21T06:20:57.508Z
Posts: 14  Views: 230
Category id: 186  Tags: [{'id': 4775, 'name': 'shopify-apps', 'slug': 'shopify-apps'}]
Accepted answer: null

---

## Post 1 by Rubidium at 2026-07-22T08:18:47.249Z
I’m looking for a size chart app for my clothing store with these requirements:

- Have a clean frontend design

- Support multiple size charts for different products

- Auto-translate between English and French

- Auto-apply the correct chart to new products (I have new arrivals coming in constantly and really don’t want to assign charts manually every time)

I’ve already tried some size chart apps from the app store, but none of them tick all these boxes.

 Also, please don’t reply with AI-generated suggestions as I went that route already and ended up installing apps that didn’t actually meet my requirements, and one of them broke my store.

I’d really appreciate hearing from someone who genuinely know an app that handles all of this.

Thank you in advance!

## Post 2 by Ellie-BOGOS at 2026-07-22T08:22:20.976Z  [ACCEPTED ANSWER]
Hi @Rubidium,

Since you’ve installed many different apps already, have you tried Kiwi Size Chart & Recommender? I think it covers all four of your requirements and runs quite stably.

My tip is to tidy up your product tags and collections first. That way the auto-assignment rules have a clean structure to key off of, and new arrivals will get the right chart applied automatically without any manual work.

Hope it helps!

Ellie from BOGOS: Free Gift Bundle Upsell team

## Post 3 by Ellie-BOGOS at 2026-07-22T08:30:14.612Z
Their support team is responsive if you hit any theme compatibility quirks during install, which should help avoid the store-breaking situation you had before.

## Post 4 by Maximus3 at 2026-07-22T08:42:17.908Z
I wouldn’t use an app for a size chart. You can add a section with Sidekick, or go with one of the many free sections available on the internet.

## Post 5 by Moeed at 2026-07-22T09:10:27.346Z
Hey @Rubidium

Honestly though, given you’ve already hit the exact wall where no app does everything and one of them broke your store, I’d lean toward getting this custom coded instead, and that’s genuinely what I’d prefer for your case. A custom size chart is your own code, so no app conflicts or breakage, no monthly fee, and it can hit all four requirements precisely: chart data held in metafields with rule based logic in the theme that auto-applies the right chart to new products by type or tag (so your constant new arrivals just work), the French version rendered automatically based on the visitor’s language rather than a bolted-on translation, and a frontend styled cleanly to match your store instead of an app’s look. It’s a one-time build that removes the exact frustrations you listed. If you’d like to go that way, happy to sort it for you.

Best,

Moeed

## Post 6 by Rubidium at 2026-07-22T09:11:33.411Z
With new arrivals coming in constantly, I don’t want to manually add or update the right chart on every new product (we have a huge number of SKUs). Also, a size recommender that suggests the right size based on the customer’s body info is something I really need. Can the section you recommend do that? Thank you!!

## Post 7 by Maximus3 at 2026-07-22T09:27:06.610Z
That one specifically, I believe it automatically shows the chart based on product tag. You would implement and upload a chart for each kind of product, then in your import you would assign tags to the products accordingly. If a product has tag1, the tag1 size chart is shown. But you are the one who uploads the chart image with the dimensions. No it does not have a “recommender” as you described I don’t think.

Honestly, I think you are wanting too much out of something. For me, I think a size chart should be somewhat accurate for the product I’m uploading, and I don’t think there is an app (or custom code) that can automatically determine what the size of a shirt or hoodie or whatever should be without some kind of manual work or verification. At best, you’d be looking at sets and kinds. A large adult shirt has wildly different sizing based on manufacturer. So I think you will, at least at some level, need to do some work figuring out what the different sizes will need to be, and base your decision on that.

## Post 8 by oscprofessional at 2026-07-22T11:29:07.365Z
Hi @Rubidium

Based on your requirements, I’d look at ESC Size Charts & Size Guide or Kiwi Size Chart & Recommender.

From my experience:

- Both support multiple size charts for different products.

- Both let you automatically assign charts using product tags, collections, or product types, so new products can inherit the correct chart without manual work.

- They offer a clean, customizable storefront design.

The one requirement I’d verify before installing is automatic English/French translation. Some apps integrate with Shopify’s multilingual setup (Translate & Adapt), while others require you to create translations within the app itself.

If multilingual support is a hard requirement, I’d recommend confirming that feature with the app developer before committing, as it’s one area where implementations differ.

## Post 9 by Custom-Cursor at 2026-07-22T14:01:04.422Z
Rubidium:

I’m looking for a size chart app for my clothing store with these requirements:

- Have a clean frontend design

- Support multiple size charts for different products

- Auto-translate between English and French

- Auto-apply the correct chart to new products (I have new arrivals coming in constantly and really don’t want to assign charts manually every time)

I’ve already tried some size chart apps from the app store, but none of them tick all these boxes.

 Also, please don’t reply with AI-generated suggestions as I went that route already and ended up installing apps that didn’t actually meet my requirements, and one of them broke my store.

I’d really appreciate hearing from someone who genuinely know an app that handles all of this.

Thank you in advance!

Hello, @Rubidium

Hope you are doing great!

You should have a look at MP Size Chart & Size Guide. t has a clean UI, supports multiple size charts, and rule based auto assignment for products. The only feature I’d verify with their team is the automatic EN/FR translation, since that’s a key requirement for your store.

Go and check here : MP Size Chart & Size Guide - Reduce returns with customizable size chart & AI recommender | Shopify App Store

## Post 10 by Ploqo at 2026-07-22T15:27:46.153Z
I built it and tested it on Dawn theme. It works. Result:

Two products, nothing assigned to either, two different charts1400×990 178 KB

A chart exists once per product type, not once per product.

If you import 500 new t-shirts tomorrow and every one of them shows the t-shirt chart, because they are all Type “T-Shirt”. That is your auto-apply.

The recommender is in there too.

- It reads the table you already typed, so you do not enter your numbers twice.

- It works out which columns are measurable on its own. In my test it offered Chest and Waist but not Length, because Length holds single numbers rather than ranges.

- Enter 96 and it says M and highlights that row. Enter something past the end of the chart and it says Closest size instead.

Chest 96 returns M and highlights that row1400×783 134 KB

How to implement:

Step 1, create the chart type. Settings, > Custom data, > Metaobjects, > Add definition. Name it Size chart and add four fields:

- Heading, single line text

- Table, multi-line text

- Note, single line text

- Recommender, multi-line text

Leave the Translations toggle on.

Step 1: the Size chart metaobject definition1400×1292 142 KB

Step 2, add one entry per product type. In Table, the first line is your column headers and every line after it is a row, with | between the cells:

Size | Chest (cm) | Waist (cm) | Length (cm)
XS | 82-87 | 66-71 | 66
S | 88-93 | 72-77 | 68
M | 94-99 | 78-83 | 70
L | 100-105 | 84-89 | 72
XL | 106-113 | 90-97 | 74
XXL | 114-121 | 98-105 | 76

Recommender is optional and holds three lines, the button and the two result labels:

Find my size
Your size:
Closest size:

Set the entry’s Handle to the product type, lowercased with dashes. Type “T-Shirt” means handle t-shirt. Type “Shirt” means handle shirt. That handle is the whole auto-assignment mechanism.

Step 2: the table format and the handle that drives it1400×873 127 KB

Step 3, paste the code. Online Store, > Themes, > the ... next to your theme, > Edit code.

In the snippets folder click Add a new snippet, name it size-chart, paste this, Save.

{%- comment -%}
  Auto size chart + size recommender.  snippets/size-chart.liquid

  Use:  {% render 'size-chart' %}   (Custom Liquid block on the product template)

  Which chart shows is worked out at render time. Nothing is set per product.
  First match wins:
    1. product.metafields.custom.size_chart   (optional manual override)
    2. a Size chart entry whose handle = the product TYPE, handleized
    3. a Size chart entry whose handle = any product TAG, handleized
    4. a Size chart entry with the handle "default"
  No match, no button. Nothing to clean up.

  Every visible string comes from the metaobject or from Liquid's own
  translation files, so Translate & Adapt handles English/French for free.
{%- endcomment -%}

{%- liquid
  assign chart = product.metafields.custom.size_chart.value

  if chart == blank
    assign type_handle = product.type | handleize
    if type_handle != blank
      assign chart = metaobjects.size_chart[type_handle]
    endif
  endif

  if chart == blank
    for tag in product.tags
      assign tag_handle = tag | handleize
      assign candidate = metaobjects.size_chart[tag_handle]
      if candidate != blank
        assign chart = candidate
        break
      endif
    endfor
  endif

  if chart == blank
    assign chart = metaobjects.size_chart.default
  endif
-%}

{%- if chart != blank and chart.table != blank -%}
  {%- assign rows = chart.table.value | strip | split: '
' -%}
  {%- assign head = rows | first | split: '|' -%}
  {%- assign uid = 'sc-' | append: product.id -%}

  {%- comment -%}
    The recommender's own wording. Optional: leave the field empty and the
    English defaults below are used. Filling it in keeps every visible string
    inside the metaobject, so Translate & Adapt covers the whole widget
    rather than just the table.
  {%- endcomment -%}
  {%- assign labels = chart.recommender.value | strip | split: '
' -%}
  {%- assign lbl_go = labels[0] | default: 'Find my size' -%}
  {%- assign lbl_hit = labels[1] | default: 'Your size:' -%}
  {%- assign lbl_near = labels[2] | default: 'Closest size:' -%}

  <style>
    #{{ uid }}-modal { position: fixed; inset: 0; z-index: 9999; display: none; }
    #{{ uid }}-modal[open] { display: block; }
    #{{ uid }}-modal .sc-veil { position: absolute; inset: 0; background: rgba(0,0,0,.5); }
    #{{ uid }}-modal .sc-box {
      position: relative; margin: 5vh auto 0; max-width: 640px; width: calc(100% - 2rem);
      max-height: 90vh; overflow: auto; background: #fff; color: #1a1a1a;
      border-radius: 10px; padding: 2rem;
      font-family: inherit; box-shadow: 0 10px 40px rgba(0,0,0,.25);
    }
    #{{ uid }}-modal .sc-close {
      position: absolute; top: .6rem; right: .6rem; width: 2.2rem; height: 2.2rem;
      border: 0; background: transparent; font-size: 1.6rem; line-height: 1; cursor: pointer; color: inherit;
    }
    #{{ uid }}-modal h2 { margin: 0 0 1rem; font-size: 1.25rem; line-height: 1.3; }
    #{{ uid }}-modal table { width: 100%; border-collapse: collapse; font-size: .9rem; }
    #{{ uid }}-modal th, #{{ uid }}-modal td { padding: .55rem .5rem; text-align: left; border-bottom: 1px solid #e3e3e3; }
    #{{ uid }}-modal th { font-weight: 600; white-space: nowrap; }
    #{{ uid }}-modal tr.sc-hit td { background: #e8f4ec; font-weight: 600; }
    #{{ uid }}-modal .sc-note { margin: .9rem 0 0; font-size: .82rem; opacity: .75; }
    #{{ uid }}-modal .sc-rec { margin-top: 1.4rem; padding-top: 1.2rem; border-top: 1px solid #e3e3e3; }
    #{{ uid }}-modal .sc-rec-row { display: flex; gap: .5rem; flex-wrap: wrap; align-items: center; }
    #{{ uid }}-modal .sc-rec select,
    #{{ uid }}-modal .sc-rec input { padding: .5rem; border: 1px solid #c9c9c9; border-radius: 6px; font-size: .9rem; color: inherit; background: #fff; }
    #{{ uid }}-modal .sc-rec input { width: 6.5rem; }
    #{{ uid }}-modal .sc-rec button { padding: .55rem 1rem; border: 0; border-radius: 6px; background: #1a1a1a; color: #fff; cursor: pointer; font-size: .9rem; }
    #{{ uid }}-modal .sc-out { margin: .9rem 0 0; font-size: .95rem; min-height: 1.3em; }
    #{{ uid }}-open { background: none; border: 0; padding: 0; font: inherit; color: inherit; text-decoration: underline; cursor: pointer; }
    @media screen and (max-width: 749px) {
      #{{ uid }}-modal .sc-box { margin-top: 0; height: 100%; max-height: 100%; border-radius: 0; }
    }
  </style>

  <button type="button" id="{{ uid }}-open" aria-haspopup="dialog">
    {{ chart.heading | default: 'Size chart' }}
  </button>

  <div id="{{ uid }}-modal" role="dialog" aria-modal="true" aria-label="{{ chart.heading | escape }}">
    <div class="sc-veil" data-sc-close></div>
    <div class="sc-box">
      <button type="button" class="sc-close" data-sc-close aria-label="Close">&times;</button>

      <h2>{{ chart.heading }}</h2>

      <table>
        <thead>
          <tr>
            {%- for cell in head -%}
              <th>{{ cell | strip }}</th>
            {%- endfor -%}
          </tr>
        </thead>
        <tbody>
          {%- for row in rows offset: 1 -%}
            {%- assign cells = row | split: '|' -%}
            {%- if cells.size > 0 -%}
              <tr>
                {%- for cell in cells -%}
                  <td>{{ cell | strip }}</td>
                {%- endfor -%}
              </tr>
            {%- endif -%}
          {%- endfor -%}
        </tbody>
      </table>

      {%- if chart.note != blank -%}
        <p class="sc-note">{{ chart.note }}</p>
      {%- endif -%}

      <div
        class="sc-rec"
        hidden
        data-hit="{{ lbl_hit | escape }}"
        data-near="{{ lbl_near | escape }}"
      >
        <div class="sc-rec-row">
          <select aria-label="{{ lbl_go | escape }}"></select>
          <input type="number" inputmode="decimal" step="0.1" min="0" placeholder="0">
          <button type="button">{{ lbl_go }}</button>
        </div>
        <p class="sc-out" role="status" aria-live="polite"></p>
      </div>
    </div>
  </div>

  <script>
    (function () {
      var uid = {{ uid | json }};
      var modal = document.getElementById(uid + '-modal');
      var open = document.getElementById(uid + '-open');
      if (!modal || !open) return;

      // Move the dialog to <body>. Many themes put a transform on the product
      // info column (Dawn does), and any transformed ancestor becomes the
      // containing block for position:fixed, which shrinks the overlay to that
      // column instead of the viewport. Reparenting sidesteps it everywhere.
      // The CSS above is keyed on the element id, so it follows the move.
      if (modal.parentElement !== document.body) document.body.appendChild(modal);

      var last = null;
      function show() { last = document.activeElement; modal.setAttribute('open', ''); document.body.style.overflow = 'hidden'; }
      function hide() { modal.removeAttribute('open'); document.body.style.overflow = ''; if (last) last.focus(); }

      open.addEventListener('click', show);
      modal.addEventListener('click', function (e) { if (e.target.closest('[data-sc-close]')) hide(); });
      document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && modal.hasAttribute('open')) hide(); });

      // ---- recommender -------------------------------------------------
      // Reads the table that is already on the page, so the merchant never
      // enters the numbers twice. A column is offered only when most of its
      // cells look like a range ("88-93").
      var rows = [].slice.call(modal.querySelectorAll('tbody tr'));
      var heads = [].slice.call(modal.querySelectorAll('thead th'));
      var range = /^\s*(\d+(?:\.\d+)?)\s*[-–]\s*(\d+(?:\.\d+)?)\s*$/;

      function parse(i) {
        var out = [];
        for (var r = 0; r < rows.length; r++) {
          var cell = rows[r].cells[i];
          var m = cell && range.exec(cell.textContent);
          out.push(m ? { lo: parseFloat(m[1]), hi: parseFloat(m[2]) } : null);
        }
        return out;
      }

      var usable = [];
      for (var i = 1; i < heads.length; i++) {
        var vals = parse(i);
        var hits = vals.filter(Boolean).length;
        if (hits >= Math.ceil(rows.length / 2)) usable.push({ i: i, label: heads[i].textContent.trim(), vals: vals });
      }
      if (!usable.length) return;

      var box = modal.querySelector('.sc-rec');
      var sel = box.querySelector('select');
      var num = box.querySelector('input');
      var go = box.querySelector('button');
      var out = box.querySelector('.sc-out');
      box.hidden = false;

      usable.forEach(function (c, n) {
        var o = document.createElement('option');
        o.value = String(n);
        o.textContent = c.label;
        sel.appendChild(o);
      });

      go.addEventListener('click', function () {
        rows.forEach(function (r) { r.classList.remove('sc-hit'); });
        var v = parseFloat(num.value);
        if (isNaN(v)) { out.textContent = ''; return; }

        var col = usable[parseInt(sel.value, 10)];
        var best = -1, bestGap = Infinity, exact = false;

        col.vals.forEach(function (rg, r) {
          if (!rg) return;
          if (v >= rg.lo && v <= rg.hi) { if (!exact) { exact = true; best = r; bestGap = 0; } return; }
          if (exact) return;
          var gap = v < rg.lo ? rg.lo - v : v - rg.hi;
          if (gap < bestGap) { bestGap = gap; best = r; }
        });

        if (best < 0) { out.textContent = ''; return; }
        rows[best].classList.add('sc-hit');
        var size = rows[best].cells[0].textContent.trim();
        // The label carries its own punctuation, so French can use "Votre
        // taille :" with the space its typography wants and English can use
        // "Your size:" without one.
        out.textContent = (exact ? box.dataset.hit : box.dataset.near) + ' ' + size;
      });

      num.addEventListener('keydown', function (e) { if (e.key === 'Enter') { e.preventDefault(); go.click(); } });
    })();
  </script>
{%- endif -%}

Step 4, put it on the product page. Theme editor > open a product template, > Add block, > Custom Liquid, > and paste one line:

{% render 'size-chart' %}

Drag it under the variant picker..

Step 5, French.

- Install the free app Translate & Adapt > open the entry and use More actions, Localize.

You get your English in one column and an empty French column next to it.

Translate the heading, the column headers, the note and the three recommender lines. The size letters and the numbers stay as they are.

Step 5: English and French side by side in Translate and Adapt1400×500 105 KB

That is the whole French job, once per chart.

Notes:

- If a product’s type has no matching chart, no button appears at all. This is what is expected.

- If you organise by tag rather than type, it falls back to tags automatically, then to an entry handled default if you make one.

- You can still override a single product by pointing a custom.size_chart metafield at a different entry.

## Post 11 by OptiAdvancedTech at 2026-07-22T19:47:46.464Z
Like @Moeed said, with the customizations necessary for a size chart, I’d recommend strongly looking into creating your own. Our clients have tried others but have always felt like they were compromising and didn’t get it exactly how they wanted. With Shopify’s AI dev blocks, I think you could probably get it looking pretty close to how you wanted. Could be worth testing out anyway.

## Post 13 by JimFromTshirtgang at 2026-07-27T22:04:52.928Z
App recommendations aside, there is an upstream decision that will cut your returns more than any app will, so it is worth settling first.

I run apparel production, so I see the returns that come back from bad size charts.

Publish garment measurements, not body measurements. Most charts list what body a size is meant to fit. What a customer can actually verify is a shirt they already own and a tape measure. Give chest width laid flat, body length from high point shoulder, and sleeve length, per size, and “will this fit me” becomes answerable in thirty seconds. Body-measurement charts generate the most “it was too small” returns by a wide margin.

Take the numbers from the mill’s spec sheet for the exact style you sell, not a generic chart. Gildan, Bella+Canvas, Next Level, AS Colour and the rest all publish per-style measurements with tolerances. If you carry three brands you genuinely need three charts, which is exactly why you are hunting for multi-chart support.

State the tolerance on the chart. “Measurements are plus or minus half an inch” pre-empts a whole category of complaint, and it is the honest truth of how garments are cut.

On your auto-apply requirement specifically: whichever app you pick, the assignment is only as good as your product organisation. Tag or collection your products by blank style rather than by category, so a rule can map “BC3001” to one chart. Do that once and new arrivals get the correct chart automatically forever. If your products are only organised as “tees” and “hoodies”, no app can auto-assign correctly, because the information it needs is not in your data.

One note for the French side: auto-translate will usually leave your numbers in inches. Canadian and French customers want centimetres, so build both columns into the chart itself rather than relying on the translation layer to handle it.

## Post 14 by info_17099 at 2026-09-18T12:43:00.350Z
Hi @Rubidium, I know this is late; but you might not have a solution that fully fits your needs yet. We saw the gap in size charts and other tables that they where not fully customisable, ugly, translatable etc. when we worked with our clients, so we decided to build a really good tables app ourselves.

I think our app will be a great fit, as it has all the requirements you mentioned. If not we would love to hear your feedback. Please see: OO ‑ Advanced Table Builder - AI table builder for size charts, specs, comparisons and more | Shopify App Store

## Post 15 by gaige.ji at 2026-09-21T06:20:57.508Z
@Rubidium Not sure whether you’ve already settled on a size-chart setup since your earlier post.

Is sizing across the constantly changing catalog still an active problem for you?
