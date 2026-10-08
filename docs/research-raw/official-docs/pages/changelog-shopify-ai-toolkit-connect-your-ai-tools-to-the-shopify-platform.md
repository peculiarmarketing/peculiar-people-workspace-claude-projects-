Source URL: https://shopify.dev/changelog/shopify-ai-toolkit-connect-your-ai-tools-to-the-shopify-platform
Fetched: 2026-10-03 via curl https://shopify.dev/changelog/shopify-ai-toolkit-connect-your-ai-tools-to-the-shopify-platform.md

---
title: Introducing the Shopify AI Toolkit - Shopify developer blog
description: >-
  Shopify AI Toolkit connects supported AI coding tools to Shopify
  documentation, API schemas, code validation, store-management workflows, and
  migration guidance.
source_url:
  html: >-
    https://shopify.dev/changelog/blog/shopify-ai-toolkit-connect-your-ai-tools-to-the-shopify-platform
  md: >-
    https://shopify.dev/changelog/blog/shopify-ai-toolkit-connect-your-ai-tools-to-the-shopify-platform.md
metadata:
  effectiveApiVersion: ''
  affectedApi: []
  primaryTag:
    displayName: AI Toolkit
    handle: ai-toolkit
  secondaryTag:
    displayName: New
    handle: new
  indicatesActionRequired: false
  createdAt: '2026-04-01T18:10:18-04:00'
  postedAt: '2026-04-09T15:45:00-04:00'
  updatedAt: '2026-07-10T15:14:01-04:00'
  effectiveAt: '2026-04-02T10:00:00-04:00'
---

April 9, 2026

# Introducing the Shopify AI Toolkit

Shopify AI Toolkit connects supported AI coding tools to Shopify documentation, API schemas, code validation, store-management workflows, and migration guidance.

DateApril 9, 2026

FlagsNew

SurfacesAI Toolkit

In order for AI coding agents to be useful additions to development workflows, they need to have the right context. When you're building on Shopify, a small platform detail can change the right implementation: the API surface you choose, the fields available in a schema, the extension APIs you import, or the validation steps you need before shipping.

The Shopify AI Toolkit is now available to help bridge that gap. It gives supported AI coding tools access to Shopify developer resources, API schemas, validation, and Shopify CLI workflows, so agents can spend less time rediscovering Shopify context and more time helping with the task in front of them.

## What changes with the toolkit

The Toolkit is designed for the moments where generic AI assistance usually needs extra correction. If you're designing an Admin GraphQL operation, your agent can work from Shopify's API schemas instead of guessing at fields or object relationships. If you're editing Liquid or UI extension code, it can validate the generated work against Shopify-specific expectations. If a task needs store context, your agent can use Shopify CLI’s `store execute` command when you choose to run it.

All this harness brings your agent’s work closer to the right answer, with access to the same Shopify-specific context you would otherwise need to provide manually.

## Example: extension migrations

Extension migrations are a good example of where this helps. Checkout and customer account UI extensions on API versions before `2025-10` need to adopt Polaris web components when upgrading to newer API versions. That kind of migration involves repetitive, detail-heavy work:

* Updating the extension API version in `shopify.extension.toml`.
* Converting React-based extension code to Preact where required.
* Replacing legacy components with Polaris web components.
* Updating extension APIs and target-specific imports.
* Checking the migration guide for required steps.
* Running and testing the migrated extension locally.

With the Toolkit installed, you can ask your coding agent to start that work from Shopify's migration guidance:

```
Migrate the extensions/my-checkout-extension extension to API version 2026-04.
```

The Toolkit doesn't remove the need to test the result, review the diff, or validate behavior in your app. It helps automate the repetitive parts of the migration so you can spend more time on the decisions and checks that still need your experience as a developer.

## Get started

Install the Shopify AI Toolkit with the plugin for your AI tool. The Toolkit supports Claude Code, Codex, Antigravity CLI, Cursor, Hermes through the plugin, and Visual Studio Code. For setup instructions, refer to the [Shopify AI Toolkit documentation](https://shopify.dev/docs/apps/build/ai-toolkit).

After installing, try it on a real Shopify workflow: scaffold an app, explore the right API for a use case, review an app against Shopify App Store requirements, or migrate a checkout or customer account UI extension.

## Related docs

* [Shopify AI Toolkit](https://shopify.dev/docs/apps/build/ai-toolkit)
* [Upgrade checkout UI extensions to the latest API version and Polaris web components](https://shopify.dev/docs/apps/build/checkout/migrate-to-web-components#migrate-using-ai)
* [Upgrade customer account UI extensions to the latest API version and Polaris web components](https://shopify.dev/docs/apps/build/customer-accounts/migrate-to-web-components#migrate-using-ai)
* [Use Polaris with the Shopify dev MCP server](https://shopify.dev/docs/api/polaris/using-mcp)
