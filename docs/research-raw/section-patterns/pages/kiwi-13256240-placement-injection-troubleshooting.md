URL: https://intercom.help/kiwi-sizing-chart/en/articles/13256240-kiwi-size-chart-placement-injection-troubleshooting
Final URL: https://intercom.help/kiwi-sizing-chart/en/articles/13256240-kiwi-size-chart-placement-injection-troubleshooting
HTTP status: 200
Fetched: 2026-10-03 via curl
Meta: {"og:title": "Kiwi Size Chart Placement & Injection Troubleshooting | Kiwi Size Chart & Recommender", "og:description": "Step-by-step guide to placing your Kiwi size chart using app blocks or CSS selectors, including common placement issues, selector examples, and troubleshooting tips.", "twitter:description": "Step-by-step guide to placing your Kiwi size chart using app blocks or CSS selectors, including common placement issues, selector examples, and troubleshooting tips.", "description": "Step-by-step guide to placing your Kiwi size chart using app blocks or CSS selectors, including common placement issues, selector examples, and troubleshooting tips."}
Schema dates: 2026-05-07T04:28:09Z

---

Skip to main content

Search for articles...

- All Collections

- Size Chart

- Size Chart Display

- Kiwi Size Chart Placement & Injection Troubleshooting

# Kiwi Size Chart Placement & Injection Troubleshooting

Step-by-step guide to placing your Kiwi size chart using app blocks or CSS selectors, including common placement issues, selector examples, and troubleshooting tips.

May 7, 2026

Table of contents

Kiwi Size Chart & Recommender gives you full control over where your size chart appears on the product page, whether that’s next to the size label, below the variant options, or just above the Add to Cart button.

This guide walks you through how Kiwi places the size chart using CSS selectors, how to build a reliable selector, and how to avoid the most common placement mistakes that cause repeat issues.

​

## When to Use This Guide

Use this article if:

- 

Your size chart appears in the wrong place

- 

The size chart only shows on one product

- 

You’re using custom placement instead of the app block

- 

Your size chart disappears after a customer selects a variant

## How Kiwi Places the Size Chart

In Kiwi → Settings → Display, you’ll see an option to inject the size chart using a CSS selector.

A CSS selector is simply a rule that tells Kiwi exactly where on the page the size chart should appear.

​

Think of it as a delivery address:

- 

Your product page = the building

- 

Variant blocks (Color, Size, Material) = rooms

- 

The selector = the exact room number

The more precise the address, the more reliable the placement.

## The 3 Selector Types Kiwi Uses

Kiwi works with a combination of these selector types:

## 1. ID Selectors (#id)

⚠️ Not recommended for Shopify themes

Although IDs are supposed to be unique, Shopify dynamically generates them per product.

That means:

- 

The selector may work on one product

- 

Then fail on all other products

Avoid selectors like this:

#ProductForm-20669957144825

## 2. Class Selectors (.class)

✅ Recommended as the foundation

Classes are reused across products and templates, which makes them stable.

Example:

.product-form__input

However, class selectors alone are often too broad because:

- 

Every variant block (color, size, material) uses the same class

So we need one more layer of precision.

## 3. Pseudo-Class Selectors (:last-of-type, :nth-of-type)

✅ Critical for targeting the correct variant

Pseudo-classes help Kiwi choose which matching element to use, based on position.

Common examples:

:last-of-type :nth-of-type(2)

Most stores use :last-of-type because:

- 

Size is usually the last variant

- 

It adapts automatically if products have different variant counts

## Why IDs Break (and Classes Don’t)

In Shopify:

- 

IDs change per product

- 

Classes stay consistent

That’s why Kiwi relies on:

Class selectors + pseudo-classes

This combination ensures:

- 

The size chart appears on all products

- 

Placement stays stable across templates

## Step-by-Step: Building a Reliable Selector

## Step 1: Inspect the Product Page

- 

Open your product page in Chrome

- 

Right-click near the size label

- 

Click Inspect

This opens Chrome DevTools.

## Step 2: Find the Variant Container

Hover through the HTML until the size label highlights on the page.

You’re looking for the parent container that wraps the size options.

​

You’ll usually see classes like:

- 

.product-form__input ✅ (best starting point)

- 

.product-form__input--pill (more specific, optional)

- 

.js ❌ (too generic, ignore)

## Step 3: Identify the Label Element

Expand the container and find where the size text actually lives.

Common child classes:

legend.form__label

Now you have:

- 

A parent class

- 

A child class

## Step 4: Combine Parent + Child

Basic structure:

.parent-class > child-class

Example:

.product-form__input > legend.form__label

If your product only has one variant, this may already be enough.

## Step 5: Handle Multiple Variants (Most Stores)

If you have multiple variants (e.g. Color + Size), add a pseudo-class:

.product-form__input:last-of-type > legend.form__label

This tells Kiwi:

- 

“Use the last variant block”

- 

Which is usually Size

## Placement Validation Checklist

After each selector or placement change, verify immediately:

- 

Placement check: The chart appears in the intended location on one product.

- 

Variant check: The chart remains visible when changing variants.

- 

Device check: The chart is visible on both desktop and mobile.

If one check fails:

- 

Return to the previous stable selector.

- 

Move the chart to a more stable parent container.

## Common Placement Options

## Place the Size Chart Next to the Size Label

This creates a small “Size Guide” style link.

​

Use a selector that injects inside the label, then add light CSS for spacing and alignment.

Best for:

- 

Clean layouts

- 

Inline size links

## Place the Size Chart Above Add to Cart Button

Inject after a stable container like:

- 

Price block

- 

Quantity selector

- 

Variant wrapper

This places the chart where shoppers check sizing right before purchase.

## Common Mistakes to Avoid

❌ Using IDs

❌ Targeting .js or overly generic classes

❌ Injecting inside containers that reload on variant change

❌ Not using pseudo-classes when multiple variants exist

## Quick Recap

Kiwi placement works best when you:

- 

Avoid IDs

- 

Start with a stable parent class

- 

Target the correct child element

- 

Use pseudo-classes to select the right variant

- 

Inject outside variant-reloading containers

Once you’ve done this a few times, building selectors becomes second nature.

If you’re still running into issues after following this guide, we recommend watching the full walkthrough video above for a visual step-by-step example.

​

If things still don't look right after following this guide, contact our support team. To help us fix it quickly, please include:

• A link to the product page where the issue is happening
• The injection selector you're currently using
• A description of what you see (wrong position, disappears on variant change, not showing at all)

Without these details, we'll need to ask before we can investigate, sharing them upfront gets you to a fix faster.

Related Articles

- 
How to Move the Size Chart with an Injection Selector (Advanced)

- 
Using the Hijack Method to Inject the Kiwi Size Chart & Recommender

- 
How to Move the Size Chart on Your Product Page (Beginner-Friendly: App Block Method)

- 
How Kiwi Works on the Product Page (Understanding What’s Happening Behind the Scenes)

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
