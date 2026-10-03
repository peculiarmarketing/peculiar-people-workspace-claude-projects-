URL: https://intercom.help/kiwi-sizing-chart/en/articles/13256403-advanced-variant-app-dom-behavior-swatch-king-similar-apps
Final URL: https://intercom.help/kiwi-sizing-chart/en/articles/13256403-advanced-variant-app-dom-behavior-swatch-king-similar-apps
HTTP status: 200
Fetched: 2026-10-03 via curl
Meta: {"og:title": "Advanced: Variant App DOM Behavior (Swatch King & Similar Apps) | Kiwi Size Chart & Recommender", "og:description": "Technical guide for DOM re-render behavior and stable placement strategy with variant apps.", "twitter:description": "Technical guide for DOM re-render behavior and stable placement strategy with variant apps.", "description": "Technical guide for DOM re-render behavior and stable placement strategy with variant apps."}
Schema dates: 2026-06-23T13:45:48Z

---

Skip to main content

Search for articles...

- All Collections

- FAQs

- Display

- Advanced: Variant App DOM Behavior (Swatch King & Similar Apps)

# Advanced: Variant App DOM Behavior (Swatch King & Similar Apps)

Technical guide for DOM re-render behavior and stable placement strategy with variant apps.

June 23, 2026

Table of contents

This is an advanced guide for variant-app behavior (Swatch King and similar apps). For the standard end-to-end troubleshooting flow, start with Fix Size Chart Disappearing After Variant or Swatch Selection.

Variant apps like Swatch King, Bold Options, and custom scripts can dynamically rebuild variant sections. When this happens, elements are removed and recreated, which can affect where Kiwi is rendered.

## Why variant apps cause placement instability

- 

Variant blocks are re-rendered after selection changes.

- 

DOM nodes can be destroyed and replaced with new nodes.

- 

Previously injected content can disappear if placed inside dynamic containers.

If Kiwi is injected into one of those dynamic zones, the chart may disappear, duplicate, jump position, or trigger script conflicts.

Important: These are usually theme/app DOM lifecycle issues, not basic selector syntax mistakes.

## Known behaviors in Swatch-style variant apps

- 

Full replacement of variant HTML blocks

- 

Variant inputs generated dynamically

- 

Event-driven DOM destruction and recreation

- 

Multiple variant blocks sharing similar classes

Because of this, inline placement inside variant controls is fragile.

## Required placement rules for variant-app stores

## Do

- 

Place the size chart outside variant-rendering containers.

- 

Use Kiwi App Block when possible.

- 

Prefer placement either below the full-variant section or above Add to Cart.

- 

Use modal display fallback when inline placement is unstable.

## Do not

- 

Inject inside swatch/radio markup that reloads on variant change.

- 

Inject directly into app-generated variant nodes.

- 

Rely on highly dynamic IDs/classes as primary anchors.

## Selector strategy (advanced)

- 

Target a static parent container that exists on initial load.

- 

Avoid nodes created only after variant events fire.

- 

Use stable classes first, then positional pseudo-classes only when needed.

- 

Re-test after variant switching to confirm persistence.

If the chart disappears after variant changes, the placement still targets a dynamic container.

​

​Also worth knowing: if you're looking for a swatch solution and don't already have one, we have a free option built by our own team - Kiwi Product Variants & Swatches. Since it's made by the same team as Kiwi Sizing, the two work together out of the box with no extra setup needed. It supports visual swatches for color, image, button styles, and more - plus automatic variant image updates, sold-out variant handling, and fully customizable swatch styling. 

​

You can install it for free here: Kiwi Product Variants & Swatches – Shopify App Store

## Use this article for

- 

DOM and architecture-level debugging

- 

Variant-app compatibility edge cases

- 

Advanced selector placement decisions

​

​

Related Articles

- 
Swatch King-Specific Compatibility Notes for Kiwi Size Chart

- 
Supported vs Unsupported Size Chart Behaviors (What Kiwi Can & Can’t Do)

- 
Common Kiwi Errors & What They Mean (Known Errors Playbook)

- 
Fix Size Chart Disappearing After Variant or Swatch Selection

- 
How to position the Kiwi size chart when using Swatch King

Did this answer your question?
Disappointed Reaction😞Neutral Reaction😐Smiley Reaction😃

Table of contents

Kiwi Size Chart & Recommender

by Staytuned Digital

Resources

- Community Hub

- More Apps

- Refer & Earn

- Blog
