URL: https://dev.to/iamrobindhiman/the-liquid-you-lint-isnt-the-liquid-shopify-runs-5bhp
Final URL: https://dev.to/iamrobindhiman/the-liquid-you-lint-isnt-the-liquid-shopify-runs-5bhp
HTTP status: 200
Fetched: 2026-10-03 via curl
Meta: {"description": "shopify theme check passed clean. The validator I run before every commit passed too. Then I opened... Tagged with shopify, liquid, frontend.", "og:title": "The Liquid you lint isn't the Liquid Shopify runs", "og:description": "shopify theme check passed clean. The validator I run before every commit passed too. Then I opened...", "twitter:description": "shopify theme check passed clean. The validator I run before every commit passed too. Then I opened..."}
Schema dates: 2026-07-16T09:03:12Z

---

Skip to content

Powered by Algolia

Log in

Create account

## DEV Community

Add reaction

Like

Unicorn

Exploding Head

Raised Hands

Fire

Jump to Comments

Save

Boost

Pick as gem

Copy link

Copied to Clipboard

Share to X

Share to LinkedIn

Share to Facebook

Share to Mastodon

Report Abuse

Robin Dhiman

Posted on Jul 16

•
 Originally published at devrob.in 

# 
 The Liquid you lint isn't the Liquid Shopify runs

#shopify
 #liquid
 #frontend

shopify theme check passed clean. The validator I run before every commit passed too. Then I opened the page on the dev store, and a size chart that builds its rows from a metafield rendered as one long, mangled line.

The Liquid was correct. The tool that checked it wasn't running the same Liquid that Shopify runs.

## 

Two engines, one language

Shopify's storefront renders Liquid with a Ruby engine, Shopify's own implementation, the one that has run the platform for years. Almost nothing you run locally uses it. shopify theme check, the Shopify MCP validator, and nearly every Node-based Liquid simulator run LiquidJS, a separate JavaScript reimplementation of the language.

So you have two implementations of one templating language. They agree on the overwhelming majority of what you write. They do not agree on all of it.

## 

Where they split

The gap I keep hitting is whitespace control. The trimming markers {%- and -%} strip surrounding whitespace, and the two engines don't always strip it identically. A few other rendering semantics differ too.

For what a linter is actually for, LiquidJS is faithful: syntax, undefined objects, unknown filters and tags, schema shape. A green run tells you the template parses and references things that exist. It does not promise byte-for-byte identical output.

## 

Why a few bytes of whitespace become a real bug

Most of the time you never notice, because HTML collapses runs of whitespace and the page looks fine either way. The exception is any code that treats rendered whitespace as data.

{%- assign rows = product.metafields.custom.size_chart.value | split: row_delimiter -%}
{%- for row in rows -%}
 <tr><td>{{ row }}</td></tr>
{%- endfor -%}

Split a rendered string on a delimiter and the exact whitespace decides where each field begins and ends. The same holds for a <pre> block, an inline SVG path you assemble in Liquid, or a JSON blob you build and hand to JavaScript. In all of those, an extra or missing newline isn't cosmetic. It changes the parse. That's how a table that's correct in my local preview shreds on the live storefront, or the reverse.

## 

Use the linter for what it catches

I still run theme check on every change, and you should. It catches the things it's built to catch: malformed syntax, undefined objects, unknown filters, schema errors. And, increasingly useful, it flags filters an AI assistant hallucinated into a template that don't exist. That's real value, and it's fast.

What it can't vouch for is whitespace-exact output. So the rule I follow is simple. Lint locally. When whitespace is load-bearing, render it on live Shopify, a dev store or a theme preview, before you trust it. Not the Node simulator. The engine that actually serves customers.

## 

The pattern underneath

This isn't really about Liquid. LiquidJS standing in for Ruby Liquid is one instance of a trap every engineer meets: the local stand-in that isn't the runtime. A mock that isn't the live API. SQLite in dev and Postgres in production. A cloud emulator on your laptop. Each one is close enough to be useful and different enough to lie to you at exactly the wrong moment.

The move isn't to distrust the tool. It's to know precisely which class of bug it can catch and which it can't, then send the rest to the real thing. For Liquid: lint in Node, render on Shopify.

## 
 Top comments (0)

Subscribe

Personal
 Trusted User

Create template

Templates let you quickly answer FAQs or store snippets for re-use.

Submit
 Preview
 Dismiss

Code of Conduct
 •
 Report abuse

Are you sure you want to hide this comment? It will become hidden in your post, but will still be visible via the comment's permalink.

Hide child comments as well

Confirm

For further actions, you may consider blocking this person and/or reporting abuse

Robin Dhiman

Follow

Magento 2 engineer focused on performance & security, working across the e-commerce stack, Shopify, WooCommerce, headless. I write about making catalogs fast, safe, and legible to AI assistants. Open

- 

Location

Chandigarh, India

- 

Work

Senior Magento 2 / E-commerce Engineer, 14+ years shipping production storefronts

- 

Joined

Jun 14, 2026

### 
 More from Robin Dhiman

What a minimal JS framework hands back to you

#hyv
 #javascript
 #magento2
 #frontend

DEV Community, A space to discuss and keep up software development and manage your software career

- 
 
 Home

- 
 
 DEV Challenges

- 
 
 DEV++

- 
 
 Videos

- 
 
 DEV Education Tracks

- 
 
 DEV Help

- 
 
 Advertise on DEV

- 
 
 Organization Accounts

- 
 
 DEV Showcase

- 
 
 About

- 
 
 Contact

- 
 
 Free Postgres Database

- 
 
 DEV Shop

- 
 
 MLH

- 
 
 Code of Conduct

- 
 
 Privacy Policy

- 
 
 Terms of Use

Built on Forem, the open source software that powers DEV and other inclusive communities.

Made with love and Ruby on Rails. DEV Community © 2016 - 2026.

We're a place where coders share, stay up-to-date and grow their careers.

Log in

Create account
