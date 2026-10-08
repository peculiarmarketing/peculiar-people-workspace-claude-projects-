Source URL: https://shopify.dev/changelog/ai-toolkit-skills-have-been-consolidated
Fetched: 2026-10-03 via curl https://shopify.dev/changelog/ai-toolkit-skills-have-been-consolidated.md

---
title: >-
  AI Toolkit skills have been consolidated to shopify - Shopify developer
  changelog
description: >-
  Shopify’s developer changelog documents all changes to Shopify’s platform.
  Find the latest news and learn about new platform opportunities.
source_url:
  html: 'https://shopify.dev/changelog/posts/ai-toolkit-skills-have-been-consolidated'
  md: >-
    https://shopify.dev/changelog/posts/ai-toolkit-skills-have-been-consolidated.md
metadata:
  effectiveApiVersion: ''
  affectedApi: []
  primaryTag:
    displayName: AI Toolkit
    handle: ai-toolkit
  secondaryTag:
    displayName: Update
    handle: update
  indicatesActionRequired: true
  createdAt: '2026-09-25T15:31:29-04:00'
  postedAt: '2026-09-25T12:00:00-04:00'
  updatedAt: '2026-09-25T16:08:38-04:00'
  effectiveAt: '2026-09-25T12:00:00-04:00'
---

September 25, 2026

# AI Toolkit skills have been consolidated to `shopify`

DateSeptember 25, 2026

FlagsUpdate[Action required](https://shopify.dev/changelog?action_required=true)

SurfacesAI Toolkit

With today's release of [AI Toolkit](https://shopify.dev/docs/apps/build/ai-toolkit), all existing `shopify-` skills are consolidated into a single `shopify` skill. If you use AI Toolkit skills with agents or `npx skills`, you might need to update your environment.

## What changed

Shopify skills content in AI Toolkit was previously distributed across many skills, such as `shopify-dev-onboarding`, `shopify-admin`, and `shopify-functions`. The agent plugins and the [AI Toolkit skills repository](https://github.com/Shopify/shopify-ai-toolkit) now expose a consolidated `shopify` skill that covers these use cases and supports development and merchant workflows.

## Who's affected

You're affected if you install or run AI Toolkit skills through:

* Agent environments that support plugins
* `npx skills`
* Similar tools that install individual `shopify-` skills

Users of the `ucp` skill and Dev MCP are unaffected.

## Why this matters

The previous skill architecture sometimes led to agent confusion and caused truncation of skill descriptions when they took up too much of the context window. Consolidating content into a single `shopify` skill reduces this ambiguity and the number of skill descriptions in agent context.

## What to do

Many agent environments that support plugins update skills automatically. If yours doesn't, or if you want to update immediately, use the agent's plugin management tools to update the plugin.

If you use `npx skills`, run the following commands:

```bash
# remove deprecated skills, add -g for global install
npx skills remove -y shopify-admin shopify-app-pricing shopify-app-store-review shopify-custom-data shopify-customer shopify-dev shopify-functions shopify-hydrogen shopify-liquid shopify-onboarding-dev shopify-onboarding-merchant shopify-partner shopify-payments-apps shopify-polaris-admin-extensions shopify-polaris-app-home shopify-polaris-checkout-extensions shopify-polaris-customer-account-extensions shopify-pos-ui shopify-shopifyql shopify-storefront-graphql shopify-use-shopify-cli

# reinstall the new skill
npx skills add Shopify/shopify-ai-toolkit --skill shopify
```

These commands remove the deprecated `shopify-` skills from your environment and install the unified `shopify` skill from the AI Toolkit repository. Use `-g` if you installed skills globally, and run these commands in each environment where you previously installed the old skills.

## Related docs

* [Learn about Shopify AI Toolkit](https://shopify.dev/docs/apps/build/ai-toolkit)
