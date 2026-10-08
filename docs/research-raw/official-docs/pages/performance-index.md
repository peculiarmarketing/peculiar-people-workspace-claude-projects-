Source URL: https://shopify.dev/docs/storefronts/themes/best-practices/performance
Fetched: 2026-10-03 via curl https://shopify.dev/docs/storefronts/themes/best-practices/performance.md (HTTP 200, markdown)

---
title: Performance best practices for Shopify themes
description: >-
  A complete reference of actionable performance recommendations and guides for
  Shopify theme developers, covering Liquid, JavaScript, images, CSS, resource
  hints, and Core Web Vitals.
source_url:
  html: 'https://shopify.dev/docs/storefronts/themes/best-practices/performance'
  md: 'https://shopify.dev/docs/storefronts/themes/best-practices/performance.md'
api_name: liquid
---

# Performance best practices for Shopify themes

Performance is an important factor for merchants when they choose a theme for their online store. When you build or customize a theme, build with performance in mind. Optimizing your theme for performance is key to the success of the merchants you support and to the experiences of their customers. Performance directly influences [conversion rates](https://www.shopify.com/enterprise/site-performance-page-speed-ecommerce), repeat business, and search engine rankings.

When you submit a theme to the [Shopify Theme Store](https://shopify.dev/docs/storefronts/themes/store), Shopify tests it on a benchmark store to determine its performance score. To be accepted into the Shopify Theme Store, a theme must have a minimum average Lighthouse performance score of 60 across the home page, product page, and collection page. You can run a similar test on your theme using a [development store](https://shopify.dev/docs/storefronts/themes/best-practices/performance/testing-for-performance).

[Learn more about performance testing for themes in the Shopify Theme Store](https://shopify.dev/docs/storefronts/themes/store/requirements#6-lighthouse-performance-and-accessibility).

Each best practice page answers three questions: Why does this matter technically? How do you implement it? And how do you test that it worked?

***

## In this section

### Best practices

Specific, single-subject, actionable recommendations:

* [Essential practices](#essential-practices)
* [Liquid](#liquid)
* [Images](#images)
* [JavaScript](#javascript)
* [CSS and fonts](#css-and-fonts)
* [Resource hints and CDN](#resource-hints-and-cdn)

### Guides and strategy

Methodology, measurement, and broader strategy:

* [Guides](#guides)
* [Mobile experience](#mobile-experience)
* [Platform](#platform)

***

## Performance metrics

Each recommendation table below has a Metric column naming the metric that the recommendation moves. Those metrics are abbreviated throughout this section, in roughly the order a page load produces them:

* **[Time to First Byte (TTFB)](https://web.dev/ttfb/)**: How long the browser waits for the first byte of the HTML response. On a Shopify storefront, most of that time is Liquid rendering. The Liquid recommendations below list TTFB as their metric for that reason. Shopify can [stream the response](https://shopify.dev/docs/storefronts/themes/best-practices/performance/platform#streamed-html-responses), and on most pages it does. A streamed response starts with the top of your `<head>`, before the sections have rendered. The sections follow in the same response. In that case, a tool's TTFB figure covers only the head. The rest of your Liquid time appears in the document's download time. See [Measuring Liquid rendering time](https://shopify.dev/docs/storefronts/themes/best-practices/performance/testing-for-performance#measuring-liquid-rendering-time).
* **[First Contentful Paint (FCP)](https://web.dev/fcp/)**: When the browser paints the first text or image. Render-blocking stylesheets and scripts in the `<head>` are the usual reason it's late.
* **[Largest Contentful Paint (LCP)](https://web.dev/lcp/)**: When the largest element in the initial viewport finishes rendering, usually a hero or product image. It tracks perceived load speed more closely than any other single metric.
* **[Cumulative Layout Shift (CLS)](https://web.dev/cls/)**: How much visible content moves unexpectedly while the page loads. Images without dimensions, fonts that swap in late, and app-injected content are the common causes.
* **[Interaction to Next Paint (INP)](https://web.dev/inp/)**: How long the page takes to respond visibly after someone taps or clicks. Main-thread work, usually JavaScript, is what makes it slow.

LCP, CLS, and INP are the [Core Web Vitals (CWV)](https://web.dev/vitals/), which Google uses as a ranking signal. TTFB and FCP aren't scored, but they help you find the cause of a slow LCP. If the server response is slow too, look at your Liquid. If the server response is fast, look at the browser-side work that follows. See [Debugging with metric gaps](https://shopify.dev/docs/storefronts/themes/best-practices/performance/performance-gaps) for how to read those gaps.

***

## Essential practices

These best practices have the largest impact on Core Web Vitals across the broadest range of themes. Check these before anything else.

| Recommendation | Summary | Metric | Impact |
| - | - | - | - |
| [Never lazy-load the LCP image](https://shopify.dev/docs/storefronts/themes/best-practices/performance/never-lazy-load-lcp-image) | `loading="lazy"` on the LCP image delays it until after layout completes. Always load images visible in the initial viewport eagerly. | LCP | High |
| [Mark the LCP image with `fetchpriority="high"`](https://shopify.dev/docs/storefronts/themes/best-practices/performance/set-fetchpriority-high-on-lcp-image) | Tells the browser to fetch the LCP image before other resources. A one-line change with measurable LCP improvement. | LCP | High |
| [Don't hide the LCP image behind animations](https://shopify.dev/docs/storefronts/themes/best-practices/performance/dont-hide-lcp-image-behind-animations) | Fade-in and reveal animations delay the LCP event even after the image finishes downloading. | LCP | High |
| [Render essential content in Liquid and HTML, not JavaScript](https://shopify.dev/docs/storefronts/themes/best-practices/performance/render-essential-content-server-side) | Moving product info, hero content, or nav into client-side JavaScript delays LCP and harms SEO. Liquid renders server-side before the browser does anything. | LCP | High |
| [Avoid deeply nested Liquid loops](https://shopify.dev/docs/storefronts/themes/best-practices/performance/avoid-deeply-nested-liquid-loops) | Loops nested across products, variants, or options grow quadratically with catalog size. A theme that's fast on 10 products can be slow on 100. The most common cause of high TTFB. | TTFB | High |
| [Load first-paint resources before `content_for_header`](https://shopify.dev/docs/storefronts/themes/best-practices/performance/load-critical-resources-before-content-for-header) | When Shopify streams the response, everything above `{{ content_for_header }}` reaches the browser before your sections render. Stylesheets, fonts, and scripts placed above it download while Liquid runs. | FCP | High |
| [Use `preload` resource hints sparingly](https://shopify.dev/docs/storefronts/themes/best-practices/performance/use-preload-resource-hints-sparingly) | Overusing `preload` competes with the browser's own prioritization and can make pages slower. Reserve it for only 1 or 2 resources the browser discovers late. | LCP | Medium |

***

## Liquid

Shopify renders Liquid templates server-side on every page request. The time Shopify spends executing your Liquid code directly determines [Time to First Byte (TTFB)](https://web.dev/ttfb/), the foundation on which all other performance metrics are built. Slow server rendering delays every subsequent phase: the browser can't paint content, discover images in sections, or run the scripts that depend on them until the sections arrive. When Shopify [streams the response](https://shopify.dev/docs/storefronts/themes/best-practices/performance/platform#streamed-html-responses), the browser can fetch the stylesheets, fonts, and scripts in your `<head>` while the sections render, but the wait for content is the same. Client-side optimizations don't shorten it. Reducing Liquid rendering time does.

Common sources of Liquid slowness include loops that grow in cost as catalog size increases, especially nested loops and metafield access inside loops, unnecessary database queries caused by iterating variants or products beyond what's displayed, and expensive operations that repeat work on every iteration. Run the [Shopify Theme Inspector for Chrome](https://shopify.dev/docs/storefronts/themes/tools/theme-inspector) to identify which Liquid lines are slowest in your theme before optimizing.

| Recommendation | Summary | Metric | Impact |
| - | - | - | - |
| [Avoid deeply nested Liquid loops](https://shopify.dev/docs/storefronts/themes/best-practices/performance/avoid-deeply-nested-liquid-loops) | Eliminate O(n²) patterns, including nested loops and metafield access inside loops, that make rendering time grow quadratically with catalog size. | TTFB | High |
| [Move metafield access outside loops](https://shopify.dev/docs/storefronts/themes/best-practices/performance/move-metafield-access-outside-loops) | Move metafield access outside loops, avoid variant-level metafield checks in loops, and prefer theme settings over metafields for static data. | TTFB | High |
| [Avoid over-fetching product variants](https://shopify.dev/docs/storefronts/themes/best-practices/performance/avoid-variant-overfetching) | Load only the variant data needed for the initial render. Iterating all variants forces expensive database queries. | TTFB | High |
| [Limit pagination depth](https://shopify.dev/docs/storefronts/themes/best-practices/performance/limit-pagination-depth) | Keep pagination under 25,000 objects. Deeper pagination is resource-intensive and slows all requests on the server. | TTFB | Medium |
| [Flatten nested `render` calls, especially inside loops](https://shopify.dev/docs/storefronts/themes/best-practices/performance/avoid-nested-renders) | Minimize `render` and `include` nesting, especially inside loops. Each nested snippet adds rendering overhead. | TTFB | Medium |
| [Defer dialog content loading](https://shopify.dev/docs/storefronts/themes/best-practices/performance/defer-modal-content-loading) | Guard expensive Liquid in dialogs and drawers with conditional parameters so content only loads when the component opens. | TTFB | Medium |
| [Defer child product loading in combined listings](https://shopify.dev/docs/storefronts/themes/best-practices/performance/defer-combined-listing-products) | Use `product.options_with_values` for combined listing UI, and defer child product data through the Section Rendering API. | TTFB | Medium |
| [Filter collections before entering loops](https://shopify.dev/docs/storefronts/themes/best-practices/performance/avoid-conditionals-in-loops) | Pre-filter collections before entering loops. Conditional logic inside loops multiplies overhead across every iteration. | TTFB | Medium |
| [Move repeated `assign` and filter calls outside loops](https://shopify.dev/docs/storefronts/themes/best-practices/performance/move-operations-outside-loops) | Assign calculations and filter operations to variables before loops so they run once, not once per iteration. | TTFB | Medium |
| [Load above-the-fold and below-the-fold sections differently with `section.index`](https://shopify.dev/docs/storefronts/themes/best-practices/performance/use-section-index) | Use `section.index` and `section.location` to apply different loading strategies based on whether a section is in or outside the initial viewport. | LCP | Medium |
| [Use the Section Rendering API for dynamic updates](https://shopify.dev/docs/storefronts/themes/best-practices/performance/use-section-rendering-api) | Fetch and update individual theme sections through Ajax using the Section Rendering API instead of full page reloads. | TTFB | Medium |
| [Cache repeated Liquid filter results with `assign`](https://shopify.dev/docs/storefronts/themes/best-practices/performance/avoid-repetitive-filter-calls) | Cache filter results with `assign` instead of calling the same filter multiple times with the same arguments. | TTFB | Low |
| [Assign `block.settings` to a variable](https://shopify.dev/docs/storefronts/themes/best-practices/performance/assign-block-settings-to-variable) | Assign `block.settings` to a variable instead of accessing it repeatedly to eliminate redundant object lookups. | TTFB | Low |
| [Output strings with `echo` instead of `append` and `prepend`](https://shopify.dev/docs/storefronts/themes/best-practices/performance/use-echo-for-concatenation) | Use `echo` or `{{ }}` output tags instead of string manipulation filters like `append` or `prepend`. | TTFB | Low |
| [Limit how many items a Liquid array fetches](https://shopify.dev/docs/storefronts/themes/best-practices/performance/limit-product-queries-with-pagination) | A `for` loop's `limit` reduces the fetch for `collection.products` and `collections`. Other arrays need `paginate`. | TTFB | High |

***

## Images

Images are typically the [Largest Contentful Paint (LCP)](https://web.dev/lcp/) element, the metric that measures when the largest visible content finishes loading, and that directly tracks perceived page speed. Correct image loading strategy, including eager or lazy loading, `fetchpriority`, and responsive sizing, has a direct effect on LCP for most storefronts.

Shopify's `image_tag` and `image_url` Liquid filters handle the most complex parts automatically: generating `srcset` attributes, adding `width` and `height` to prevent layout shift, and serving images from the CDN. Using these filters consistently is the baseline. The recommendations below cover the decisions and patterns that go beyond the filters themselves.

| Recommendation | Summary | Metric | Impact |
| - | - | - | - |
| [Mark the LCP image with `fetchpriority="high"`](https://shopify.dev/docs/storefronts/themes/best-practices/performance/set-fetchpriority-high-on-lcp-image) | Apply `fetchpriority="high"` to the LCP image to signal its importance before the browser completes layout. | LCP | High |
| [Never lazy-load the LCP image](https://shopify.dev/docs/storefronts/themes/best-practices/performance/never-lazy-load-lcp-image) | Apply `loading="lazy"` only to images outside the initial viewport. Always eagerly load images visible in the initial viewport, especially the LCP candidate. | LCP | High |
| [Don't hide the LCP image behind animations](https://shopify.dev/docs/storefronts/themes/best-practices/performance/dont-hide-lcp-image-behind-animations) | Remove or async-load CSS transitions on LCP images. Animations delay the LCP event even when the image has loaded. | LCP | High |
| [Don't use CSS `background-image` for LCP content](https://shopify.dev/docs/storefronts/themes/best-practices/performance/avoid-background-images-hero) | Use `<img>` instead of CSS background images for hero and LCP content so the browser's preload scanner can discover them early. | LCP | High |
| [Serve correctly sized images with `srcset` and `sizes`](https://shopify.dev/docs/storefronts/themes/best-practices/performance/use-responsive-images) | Use `srcset` and `sizes` with `image_tag` to serve the smallest image that still looks good at each viewport size. | LCP | Medium |
| [Prevent image layout shift](https://shopify.dev/docs/storefronts/themes/best-practices/performance/prevent-image-layout-shift) | Always include `width` and `height` attributes on `<img>` tags, or use `image_tag`, which adds them automatically. | CLS | Medium |
| [Use `image_url` and `image_tag` instead of manual CDN URLs](https://shopify.dev/docs/storefronts/themes/best-practices/performance/use-shopify-image-filters-efficiently) | Use `image_url` and `image_tag` instead of constructing CDN URLs manually to get automatic optimization and correct attributes. | LCP | Medium |
| [Prevent dialogs from hijacking LCP](https://shopify.dev/docs/storefronts/themes/best-practices/performance/prevent-popups-hijacking-lcp) | Keep dialogs smaller than main content or delay them until after interaction so they don't become the LCP element. | LCP | Medium |
| [Use Liquid filter chains for images](https://shopify.dev/docs/storefronts/themes/best-practices/performance/use-filter-chains) | Generate image markup through Shopify's filter system (`image_url` and `image_tag`) instead of constructing URLs manually. | LCP | Medium |
| [Use the picture element when you have separate mobile and desktop images](https://shopify.dev/docs/storefronts/themes/best-practices/performance/use-picture-for-art-directed-heroes) | Replace CSS-toggled mobile/desktop hero image pairs with a `<picture>` element so the browser downloads only the matching image. | LCP | Medium |

***

## Java​Script

JavaScript, whether your own theme code or scripts from installed apps, runs on the main thread and directly competes with the browser's ability to render content and respond to user input. Too much JavaScript, loaded at the wrong time or written inefficiently, is one of the primary causes of poor [Interaction to Next Paint (INP)](https://web.dev/inp/) and delayed [Largest Contentful Paint (LCP)](https://web.dev/lcp/).

The goal is to load only what's needed, only when it's needed: defer non-critical scripts, import modules on interaction instead of at page load, and avoid heavyweight frameworks when Liquid and CSS can do the same job. When JavaScript problems do appear, profiling the specific cause matters. Badly written first-party code is just as damaging as a poorly implemented third-party script.

| Recommendation | Summary | Metric | Impact |
| - | - | - | - |
| [Remove render-blocking apps](https://shopify.dev/docs/storefronts/themes/best-practices/performance/remove-render-blocking-apps) | Identify and remove or defer app scripts that block HTML parsing before any content is rendered. | LCP | High |
| [Render essential content in Liquid and HTML, not JavaScript](https://shopify.dev/docs/storefronts/themes/best-practices/performance/render-essential-content-server-side) | Render initial content with Liquid and HTML. Use Hydrogen for server-side rendering if a framework is truly required. | LCP | High |
| [Send data requests for critical content before the DOM is ready](https://shopify.dev/docs/storefronts/themes/best-practices/performance/request-critical-data-before-dom-ready) | When JavaScript must render above-the-fold content from an external API, send the request as soon as the script executes and wait for the DOM only to render. Load the bundle `async` from the `<head>`, above `{{ content_for_header }}` if it doesn't read `Shopify.*`. | LCP | High |
| [Audit and remove unused scripts](https://shopify.dev/docs/storefronts/themes/best-practices/performance/audit-remove-third-party-scripts) | Audit all scripts, including apps, tracking pixels, and theme code, and remove anything that isn't earning its performance cost. | INP | High |
| [Use `defer` and `async` on non-critical scripts](https://shopify.dev/docs/storefronts/themes/best-practices/performance/defer-scripts) | Use the `defer` attribute on non-critical scripts. Use `async` only for independent third-party scripts where execution order doesn't matter. | LCP | High |
| [Load JavaScript on user interaction](https://shopify.dev/docs/storefronts/themes/best-practices/performance/load-javascript-on-user-interaction) | Use dynamic `import()` inside event listeners to load JavaScript modules only when a user actually interacts with a component. | INP | High |
| [Remove A/B test anti-flicker snippets when no tests are running](https://shopify.dev/docs/storefronts/themes/best-practices/performance/disable-ab-testing-when-inactive) | Disable anti-flicker snippets when no tests are running, and end completed tests immediately to remove their performance cost. | LCP | High |
| [Defer render-blocking CSS and JavaScript](https://shopify.dev/docs/storefronts/themes/best-practices/performance/defer-non-critical-resources) | Use `async`/`defer` for JavaScript and the async CSS pattern for stylesheets that aren't needed for initial render. | LCP | Medium |
| [Debounce, throttle, and yield in event handlers](https://shopify.dev/docs/storefronts/themes/best-practices/performance/debounce-throttle-event-handlers) | Use debouncing, throttling, passive listeners, and `requestAnimationFrame` to reduce main-thread blocking from event handlers. | INP | Medium |
| [Cancel in-progress view transitions on user interaction](https://shopify.dev/docs/storefronts/themes/best-practices/performance/cancel-view-transitions-on-interaction) | Cancel in-progress view transitions when users interact to prevent transitions from blocking INP. | INP | Medium |
| [Load JavaScript modules with import maps instead of bundlers](https://shopify.dev/docs/storefronts/themes/best-practices/performance/use-import-maps-for-modules) | Use import maps with bare module specifiers. Shopify automatically includes `es-module-shims`, so don't load your own copy. | FCP | Low |
| [Build DOM for hidden components only when opened](https://shopify.dev/docs/storefronts/themes/best-practices/performance/lazy-dom-rendering) | Filter panels, cart drawers, and dialogs add thousands of DOM nodes even when closed. Build their DOM only when the user first opens them. | INP | Medium |

***

## CSS and fonts

CSS affects three Core Web Vitals: [First Contentful Paint (FCP)](https://web.dev/fcp/) through render-blocking stylesheets, [Cumulative Layout Shift (CLS)](https://web.dev/cls/) through font swapping and late-loading content, and [INP](https://web.dev/inp/) through expensive style recalculations triggered by too many stylesheets or layout-affecting animations. Web fonts introduce additional complexity because they're a render-blocking resource by default and cause visible layout shift when they swap in.

Key CSS decisions that affect Core Web Vitals: load only critical styles synchronously, use `size-adjust` and font metric overrides to reduce layout shift during font swap, and prefer `transform`/`opacity` animations over layout-property animations.

| Recommendation | Summary | Metric | Impact |
| - | - | - | - |
| [Reduce stylesheet count](https://shopify.dev/docs/storefronts/themes/best-practices/performance/reduce-stylesheet-count) | Minimize separate `<link>` tags for stylesheets. Each additional stylesheet triggers an expensive style recalculation that blocks INP. | INP | High |
| [Reduce CLS from font swapping](https://shopify.dev/docs/storefronts/themes/best-practices/performance/reduce-cls-font-swapping) | Use `size-adjust` and override descriptors on fallback fonts to match web font metrics and reduce layout shift during font swap. | CLS | High |
| [Load critical CSS synchronously](https://shopify.dev/docs/storefronts/themes/best-practices/performance/load-critical-css-synchronously) | Load critical CSS for content visible in the initial viewport synchronously. Use the async CSS pattern only for sections outside the initial viewport where it's proven beneficial. | FCP | High |
| [Load first-paint resources before `content_for_header`](https://shopify.dev/docs/storefronts/themes/best-practices/performance/load-critical-resources-before-content-for-header) | Place base stylesheets, font preloads, and the import map above `{{ content_for_header }}` so the browser can fetch them while Shopify renders your sections. Check inline `Shopify.*` scripts and cascade order before moving anything. | FCP | High |
| [Self-host web fonts on Shopify CDN](https://shopify.dev/docs/storefronts/themes/best-practices/performance/self-host-web-fonts) | Upload web fonts to the Shopify CDN instead of loading from Google Fonts or other external services to eliminate DNS and connection overhead. | FCP | Medium |
| [Eliminate font loading delays with system fonts](https://shopify.dev/docs/storefronts/themes/best-practices/performance/use-system-fonts) | Use [system fonts](https://shopify.dev/docs/storefronts/themes/architecture/settings/fonts#system-fonts) to avoid downloading web font files before text can render. | FCP | Medium |
| [Reserve space for app-injected content](https://shopify.dev/docs/storefronts/themes/best-practices/performance/reserve-space-app-injected) | Use App Blocks with `min-height` CSS to reserve space for app-injected content and prevent CLS when it loads. | CLS | Medium |
| [Animate with `transform` and `opacity` instead of layout properties](https://shopify.dev/docs/storefronts/themes/best-practices/performance/use-transform-for-animations) | Animate with `transform` and `opacity` rather than layout properties like `top` or `left` to avoid triggering relayout on every frame. | INP | Medium |
| [Merge duplicate mobile and desktop menus into one](https://shopify.dev/docs/storefronts/themes/best-practices/performance/reduce-mega-menu-dom-overhead) | Use a single responsive menu with CSS media queries rather than separate desktop/mobile menus that double the DOM size. | INP | Medium |
| [Ensure compatibility with stylesheet subsetting](https://shopify.dev/docs/storefronts/themes/best-practices/performance/stylesheet-subsetting) | Shopify automatically subsets CSS from `{% stylesheet %}` tags so each page loads only the styles from its render tree. Ensure each file's classes are used only within that file or files it directly renders. | FCP | Medium |

***

## Resource hints and CDN

Resource hints instruct the browser to take action on resources before it would discover them naturally: establishing connections early, fetching critical assets ahead of time, or prerendering likely next pages. Shopify handles many of these automatically. Assets served from the Shopify CDN benefit from HTTP/3, Brotli compression, and global edge caching without any configuration. Shopify [preloads render-blocking scripts and stylesheets through Early Hints](https://shopify.dev/docs/storefronts/themes/best-practices/performance/platform#early-hints) before the HTML arrives.

The recommendations here cover the decisions that remain in your hands: which third-party origins to `preconnect` to, when (and when not) to use `preload`, and how to configure the Speculation Rules API for faster navigations. A key caution applies to all resource hints: overuse is as harmful as underuse, because hints that compete with the browser's own prioritization can make pages slower.

| Recommendation | Summary | Metric | Impact |
| - | - | - | - |
| [Avoid request proxies](https://shopify.dev/docs/storefronts/themes/best-practices/performance/avoid-request-proxies) | Don't serve your Shopify storefront through a reverse proxy. Proxies mask real problems, distort metrics, and add latency. | TTFB | High |
| [Serve assets from Shopify CDN](https://shopify.dev/docs/storefronts/themes/best-practices/performance/use-shopify-cdn) | Serve all theme assets through the Shopify CDN by placing them in the `/assets` folder to avoid extra DNS connections per external domain. | TTFB | Medium |
| [Use `preload` sparingly](https://shopify.dev/docs/storefronts/themes/best-practices/performance/use-preload-resource-hints-sparingly) | Use `<link rel="preload">` for only 1 or 2 critical resources the browser discovers late. Overuse competes with browser prioritization. | LCP | Medium |
| [Speed up navigations with the Speculation Rules API](https://shopify.dev/docs/storefronts/themes/best-practices/performance/use-speculation-rules) | Declare prefetch and prerender rules for likely next-page navigations to make them near-instant for users. | TTFB | Medium |
| [Warm up third-party connections early with `preconnect`](https://shopify.dev/docs/storefronts/themes/best-practices/performance/use-preconnect) | Establish DNS, TCP, and TLS connections to critical third-party domains earlier with `preconnect` resource hints. | LCP | Medium |

***

## Guides

Guides cover the methodology, tooling, and strategy that support all of the best practices above. They answer broader questions: How do you measure performance correctly? How do you find which JavaScript is causing the most damage? How do you prevent performance from regressing as the site grows?

Start with [Testing for performance](https://shopify.dev/docs/storefronts/themes/best-practices/performance/testing-for-performance) and [Lab and field data](https://shopify.dev/docs/storefronts/themes/best-practices/performance/lab-vs-field) before making any optimizations. Understanding your baseline and measurement tools prevents wasted effort.

| Guide | Summary |
| - | - |
| [Testing for performance](https://shopify.dev/docs/storefronts/themes/best-practices/performance/testing-for-performance) | Run the same Lighthouse benchmark Shopify uses for Theme Store evaluation, set up Lighthouse CI, and interpret Web Performance Dashboard data. |
| [Lab and field data](https://shopify.dev/docs/storefronts/themes/best-practices/performance/lab-vs-field) | Understand when to use Real User Monitoring (RUM) and when to use synthetic lab tests, and how to use both together for debugging. |
| [Debugging with metric gaps](https://shopify.dev/docs/storefronts/themes/best-practices/performance/performance-gaps) | Analyze the gaps between TTFB, FCP, and LCP in RUM data to narrow down root causes before running lab tests. |
| [Understanding INP](https://shopify.dev/docs/storefronts/themes/best-practices/performance/understanding-inp) | A detailed look at Interaction to Next Paint: the three phases of input delay, processing time, and presentation delay, and how to reduce each. |
| [Finding your worst JavaScript offenders](https://shopify.dev/docs/storefronts/themes/best-practices/performance/finding-worst-offenders) | Use Lighthouse Treemap, DevTools Coverage, and network analysis to identify the 20 percent of scripts causing 80 percent of problems. |
| [Avoiding fake performance apps](https://shopify.dev/docs/storefronts/themes/best-practices/performance/fake-performance-apps) | Recognize apps that cheat Lighthouse and PageSpeed tests, such as apps that inject transparent elements or serve different pages to crawlers, and avoid them. |
| [Theme Check linting tool](https://shopify.dev/docs/storefronts/themes/best-practices/performance/theme-check-tool) | Use Shopify's official linter to catch performance violations, such as oversized bundles, parser-blocking scripts, and remote assets, before deployment. |
| [Liquid performance patterns](https://shopify.dev/docs/storefronts/themes/best-practices/performance/liquid-performance-patterns) | A reference of compounding Liquid micro-optimizations that together can save 25 to 50 ms of TTFB on complex themes. |
| [Build a sustainable performance practice](https://shopify.dev/docs/storefronts/themes/best-practices/performance/sustainable-performance) | Why one-time performance projects fail, how to build a repeatable improvement cycle, and how to get organizational alignment to keep a storefront fast over time. |
| [Performance in Hydrogen](https://shopify.dev/docs/storefronts/themes/best-practices/performance/hydrogen-performance) | React optimization patterns such as code splitting and memoization, image prioritization, and third-party script management for Hydrogen storefronts. |

***

## Mobile experience

Mobile devices account for the majority of Shopify storefront traffic and are subject to the most challenging performance conditions: slower CPUs, constrained memory, and variable network connections. Core Web Vitals scores are measured on mobile by default, so mobile performance is theme performance.

The recommendations below address the mobile-specific usability issues that directly affect CWV scores and search rankings. A dedicated mobile experience section is planned, so these recommendations are grouped here in the interim.

| Recommendation | Summary | Metric | Impact |
| - | - | - | - |
| [Test with real mobile CPU and network throttling](https://shopify.dev/docs/storefronts/themes/best-practices/performance/improve-mobile-page-load-speed) | Address the CPU, memory, and network constraints that make mobile performance harder than desktop. Test with realistic throttling and representative devices. | LCP | High |
| [Remove intrusive interstitials](https://shopify.dev/docs/storefronts/themes/best-practices/performance/remove-intrusive-interstitials) | Avoid full-screen dialogs and overlays that cover main content on page load. They trigger Google ranking penalties and harm Core Web Vitals. | LCP | High |
| [Build responsive layouts that perform well](https://shopify.dev/docs/storefronts/themes/best-practices/performance/implement-responsive-design) | Use Shopify's responsive image tools, conditional Liquid rendering, and targeted CSS to serve fast pages across all screen sizes. | LCP | Medium |
| [Increase tap target size](https://shopify.dev/docs/storefronts/themes/best-practices/performance/increase-tap-target-size) | Make interactive elements at least 48 × 48 px on mobile to reduce mis-taps and the interaction delays that hurt INP. | INP | Medium |
| [Fix content wider than the viewport](https://shopify.dev/docs/storefronts/themes/best-practices/performance/fix-content-wider-than-mobile-screen) | Eliminate horizontal scrolling by making sure all content, images, and embeds fit within the device viewport width. | CLS | Medium |
| [Ensure content parity between mobile and desktop](https://shopify.dev/docs/storefronts/themes/best-practices/performance/ensure-content-parity-mobile-desktop) | Verify that content hidden on mobile with CSS isn't deprioritized by Google's mobile-first indexer. | LCP | Medium |

***

## Platform

Shopify's infrastructure provides a foundation of automatic optimizations that apply to every storefront: a global CDN backed by Cloudflare, Brotli and gzip compression, HTTP/3 and TLS 1.3, automatic image versioning, Early Hints for render-blocking resources, and streamed HTML responses that can deliver the top of your `<head>` before your sections render. Understanding what the platform handles automatically helps you avoid duplicating effort and shows which optimizations are already in place before you write any code.

| Guide | Summary |
| - | - |
| [The Shopify platform](https://shopify.dev/docs/storefronts/themes/best-practices/performance/platform) | An overview of the CDN, HTTP/3, Brotli compression, Early Hints, streamed HTML responses, and the automatic optimizations Shopify provides to every storefront. |
| [Audit and optimize checkout extensions](https://shopify.dev/docs/storefronts/themes/best-practices/performance/optimize-checkout-extensions) | Identify slow checkout UI extensions, remove unused ones, and work with extension developers to reduce checkout LCP and INP (Shopify Plus). |

***

## Next steps

* [Learn about theme accessibility best practices](https://shopify.dev/docs/storefronts/themes/best-practices/accessibility)
* [Submit your theme to the Shopify Theme Store](https://shopify.dev/docs/storefronts/themes/store)

***
