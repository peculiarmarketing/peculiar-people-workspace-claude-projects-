Source URL: https://shopify.dev/docs/api/shopify-cli
Fetched: 2026-10-03 via curl https://shopify.dev/docs/api/shopify-cli.md (HTTP 200, markdown)

---
title: Shopify CLI
description: >-
  Shopify CLI is a command-line interface tool that helps you generate and work
  with Shopify apps, themes and custom storefronts.
source_url:
  html: 'https://shopify.dev/docs/api/shopify-cli'
  md: 'https://shopify.dev/docs/api/shopify-cli.md'
api_name: shopify-cli
---

# Shopify CLI

Shopify CLI is a command-line interface tool that helps you generate and work with Shopify apps, themes and custom storefronts. You can also use it to automate many common development tasks.

## Requirements

* [Node.js](https://nodejs.org/en/download/): 22.12 or higher
* A Node.js package manager: [npm](https://www.npmjs.com/get-npm), [Yarn 1.x](https://classic.yarnpkg.com/lang/en/docs/install), or [pnpm](https://pnpm.io/installation).
* [Git](https://git-scm.com/downloads): 2.28.0 or higher

***

## Installation

This installs Shopify CLI globally on your system, so you can run `shopify` commands from any directory. Find out more about the available commands by running `shopify` in your terminal.

## Code

##### npm

```sh
npm install -g @shopify/cli@latest
```

##### yarn

```sh
yarn global add @shopify/cli@latest
```

##### pnpm

```sh
pnpm install -g @shopify/cli@latest
```

##### homebrew

```sh
# Only for macOS
brew tap shopify/shopify
brew install shopify-cli
```

***

## Commands

Shopify CLI groups commands into topics. The command syntax is: `shopify [topic] [command]`. Refer to each topic section in the sidebar for a list of available commands.

Or, run the `help` command to get this information right in your terminal.

## terminal

```sh
shopify help
```

***

## Upgrade Shopify CLI

Starting with Shopify CLI 4.0, Shopify CLI upgrades itself automatically using the package manager you installed it with. Auto-upgrade is skipped in CI environments, project-local installs, and major version bumps. To upgrade immediately, run `shopify upgrade`.

### Turn off auto-upgrades

* To disable auto-upgrades, run `shopify config autoupgrade off`.
* To re-enable, run `shopify config autoupgrade on`.

When auto-upgrade is off, Shopify CLI shows a daily reminder when a new version is available, but won't upgrade itself.

## terminal

```sh
> shopify version
4.0.0


> shopify config autoupgrade status
╭─ info ──────────────────────────────────────────────────────╮
│                                                             │
│  Auto-upgrade on. Shopify CLI will update automatically     │
│  after each command.                                        │
│                                                             │
╰─────────────────────────────────────────────────────────────╯
```

***

## Network proxy configuration

When working behind a network proxy, you can configure Shopify CLI (version 3.78+) to route connections through it:

1. Set the proxy for HTTP traffic:

   ```bash
   export SHOPIFY_HTTP_PROXY=http://proxy.com:8080
   ```

2. Optionally, set a different proxy for HTTPS traffic:

   ```bash
   export SHOPIFY_HTTPS_PROXY=https://secure-proxy.com:8443
   ```

   If not specified, the HTTP proxy will be used for all traffic.

3. For authenticated proxies, include credentials in the URL:

   ```bash
   export SHOPIFY_HTTP_PROXY=http://username:password@proxy.com:8080
   ```

***

## Usage reporting

Anonymous usage statistics are collected by default. To opt out, you can use either `SHOPIFY_CLI_NO_ANALYTICS=1` or `OPT_OUT_INSTRUMENTATION=true`.

***

## Contribute to Shopify CLI

Shopify CLI is open source. [Learn how to contribute](https://github.com/Shopify/cli/wiki/Contributors:-Introduction) to our GitHub repository.

***

## Where to get help

* [Shopify CLI and Libraries](https://community.shopify.dev/c/shopify-cli-libraries/14) - Report any issues with the CLI.
* [Dev Platform](https://community.shopify.dev/c/dev-platform/32) - Ask any questions and learn more about the Dev Platform powering the CLI.

***

## Resources

[Start building a theme\
\
](https://shopify.dev/docs/themes/getting-started/create)

[Learn how to set up your theme development environment and create a new theme](https://shopify.dev/docs/themes/getting-started/create)

[Start building an app\
\
](https://shopify.dev/docs/apps/getting-started/create)

[Learn how to set up your app development environment and start building](https://shopify.dev/docs/apps/getting-started/create)

***
