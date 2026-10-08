Source URL: https://shopify.dev/docs/storefronts/themes/tools/cli
Fetched: 2026-10-03 via curl https://shopify.dev/docs/storefronts/themes/tools/cli.md (HTTP 200, markdown)

---
title: Shopify CLI for themes
description: >-
  Learn about Shopify CLI, a command line tool that helps you to build Shopify
  themes faster.
source_url:
  html: 'https://shopify.dev/docs/storefronts/themes/tools/cli'
  md: 'https://shopify.dev/docs/storefronts/themes/tools/cli.md'
api_name: liquid
---

# Shopify CLI for themes

Shopify CLI is a command-line interface tool that helps you build Shopify apps and themes. It quickly generates Shopify apps, themes, and custom storefronts. You can also use it to automate many common development tasks.

This documentation explains how to use Shopify CLI for theme development. To learn how to use Shopify CLI for other tasks, refer to the following documentation:

* [Shopify CLI for apps](https://shopify.dev/docs/apps/build/cli-for-apps)
* [Shopify CLI for Hydrogen storefronts](https://shopify.dev/docs/api/shopify-cli/hydrogen)

**Tip:**

You can use Shopify CLI together with the [Shopify GitHub integration](https://shopify.dev/docs/storefronts/themes/tools/github) to add version control to themes that you're developing.

***

## Features

Shopify CLI accelerates your theme development process with the following features:

* Safely preview, test, and share changes to themes using [development themes](https://shopify.dev/docs/storefronts/themes/tools/cli#development-themes)
* Hot reload CSS and section changes, or automatically refresh a page on file change, when previewing a theme
* Initialize a new theme
* Push and publish themes from the command line
* Work on multiple themes using [environments](#environments)
* Run [Theme Check](https://shopify.dev/docs/storefronts/themes/tools/theme-check/configuration) on your theme

### Development themes

Development themes are temporary, hidden themes that are connected to the Shopify store that you're using for development. When you connect your theme to a store as a development theme, you can use that store's data for local testing.

You can create a development theme using the [`shopify theme dev`](https://shopify.dev/docs/api/shopify-cli/theme/theme-dev) command.

You can use development themes on a Shopify store or a [development store](https://shopify.dev/docs/storefronts/themes/tools/development-stores). Development themes don't count toward your theme limit, and are deleted from the store after seven days of inactivity.

Your development theme is deleted when you run `shopify auth logout`. If you want a preview link for the theme that can be accessed after you log out, then you should [push](https://shopify.dev/docs/api/shopify-cli/theme/theme-push) your development theme to an unpublished theme on your store.

Your development theme can be used to perform the following tasks:

* View changes in real time to a theme that you're developing locally
* Customize and interact with the theme using the Shopify admin [theme editor](https://shopify.dev/docs/storefronts/themes/tools/online-editor)
* Share a password-protected [preview](https://help.shopify.com/manual/online-store/themes/adding-themes#share-a-theme-preview-with-others) of the theme with other developers

### Environments

Many command configurations, such as the theme and store to be used with the command, are passed using flags. To avoid passing multiple flags with each command, and to easily switch projects or contexts, you can use environments. Environments are sets of command configurations that can be referenced by name using a single `--environment` flag.

You might want to use environments in the following cases:

* You need to switch between development stores frequently.
* You access multiple stores using [Theme Access](https://shopify.dev/docs/storefronts/themes/tools/theme-access) passwords.
* You want to deploy your project to development, staging, and production instances of your theme.

[Learn how to configure and use environments](https://shopify.dev/docs/storefronts/themes/tools/cli/environments).

***

## Installation

To learn how to install Shopify CLI on Windows, macOS, or Linux, refer to [Install Shopify CLI](https://shopify.dev/docs/api/shopify-cli).

***

## Getting started

Refer to the following tutorials for details about creating or working on a Shopify theme using Shopify CLI:

[Start building a theme\
\
](https://shopify.dev/docs/storefronts/themes/getting-started/create)

[Learn how to set up your theme development environment and create a new theme.](https://shopify.dev/docs/storefronts/themes/getting-started/create)

[Customize an existing theme\
\
](https://shopify.dev/docs/storefronts/themes/getting-started/customize)

[Learn how to set up your development environment to work on a theme in a Shopify store.](https://shopify.dev/docs/storefronts/themes/getting-started/customize)

***

## Command reference

Refer to the [Shopify CLI theme command reference](https://shopify.dev/docs/api/shopify-cli/theme) to explore the commands available to build themes with Shopify CLI.

***

## Authenticating and accessing stores

As a theme developer, you might want to use a Shopify store to test your theme, or to share your theme with stakeholders. You also might need to work on multiple stores, or use a different set of credentials to authenticate with a particular store. Learn about the authentication methods that you can use to work on stores using Shopify CLI, and how to switch between accounts and stores.

### Authentication

You can use the following authentication methods to work on a theme in a Shopify store using Shopify CLI:

* [Log in with a Shopify account](#log-in-with-a-shopify-account)
* [Provide a Theme Access password](#theme-access-password)
* [Provide a custom app access token](#custom-app-access-token)

#### Log in with a Shopify account

You can use the following types of Shopify accounts to access the store you want to work on:

* A [collaborator account](https://shopify.dev/docs/storefronts/themes/tools/collaborator-accounts) with the **Manage themes** permission
* A [staff account](https://help.shopify.com/manual/your-account/staff-accounts) with the **Themes** permission
* The store owner account

To authenticate with a Shopify account, run a command that requires store access. You'll be prompted to log in.

**Caution:**

To use a dev store with [Shopify CLI](https://shopify.dev/docs/apps/build/cli-for-apps), you need to be the store owner, or have a [staff account](https://help.shopify.com/manual/your-account/staff-accounts) on the store. If you create a dev store, then you're assigned as the store owner. Other staff members must be added to the store.

##### Switching between accounts

If you need to switch between accounts, then log out of the current account using the following command:

```terminal
shopify auth logout
```

The next time you enter a command that requires authentication, you'll be prompted to log in, and can enter a new set of credentials.

#### Theme Access password

You can use a Theme Access password to authenticate with the store that you want to work on. Theme Access passwords are generated for a store using the [Theme Access app](https://shopify.dev/docs/storefronts/themes/tools/theme-access).

To use a Theme Access password, pass the `--password` flag with each command that you want to run against the store. If you run a command without the `--password` flag, then Shopify CLI attempts to use your Shopify account credentials to run the command.

#### Custom app access token

You can use a [custom app access token](https://shopify.dev/docs/apps/build/authentication-authorization/legacy/admin-custom-apps) to authenticate with the store that you want to work on.

To authenticate using an access token, pass the `--password` flag with each command that you want to run against the store. If you run a command without the `--password` flag, then Shopify CLI attempts to use your Shopify account credentials to run the command.

Your custom app needs to have the `read_themes` and `write_themes` [API access scopes](https://shopify.dev/docs/api/usage/access-scopes). To enable hot reloading, you also need to add the `unauthenticated_read_content` access scope for Storefront API integration, and pass the tokens as [environment variables](https://shopify.dev/docs/storefronts/themes/tools/cli/environments) instead of using the `--password` flag.

### Connecting to a store

The first time you enter a command that requires you to interact with a Shopify store, pass the `--store` flag with the command and specify the store that you want to interact with:

```terminal
shopify theme dev --store my-store
```

The store that you specify is used for future commands until a new store is specified.

If you want to change the store that you're interacting with, pass the `--store` flag with your command, specifying the new store that you want to interact with.

To check which store you're using, run `shopify theme info`:

## Terminal

```terminal
shopify theme info
```

## Output

```terminal
THEME CONFIGURATION
-----------------------
Store   my-store.myshopify.com
...
```

***

## Directory structure

You can run certain theme commands, such as `shopify theme dev`, only if the directory you're using matches the default Shopify theme [directory structure](https://shopify.dev/docs/storefronts/themes/architecture#directory-structure-and-component-types). This structure represents a buildless theme, or a theme that has already gone through any necessary [file transformations](https://shopify.dev/docs/storefronts/themes/best-practices/file-transformation). If you use build tools to generate theme files, then you might need to run commands from the directory where the generated files are stored.

The default Shopify theme directory structure is as follows:

## Shopify theme directory structure

```text
└── project
    ├── assets
    ├── blocks
    ├── config
    ├── layout
    ├── locales
    ├── sections
    ├── snippets
    └── templates
        └── customers
```

***

## Excluding files from Shopify CLI

If you have files in the same repository as your theme that you don't want to interact with using Shopify CLI, then you can add them to a `.shopifyignore` at the root of the theme.

`.shopifyignore` accepts references to files in the following formats:

* Simple file names: `templates/product.temp.json`
* Wildcards: `config/*_secret.json`, `*.jpg`
* Regular expressions: `/\.(txt|gif|bat)$/`

You can also exclude specific files or patterns during a `push` or `pull` using the `--ignore` flag. If files are excluded using `.shopifyignore`, then both the contents of `.shopifyignore` and the `--ignore` flag are respected.

***

## Using Shopify CLI for continuous integration

If you have a theme that you want to work with programmatically, then you can integrate Shopify CLI into your CI/CD pipeline to perform actions like pushing, pulling, and publishing a theme.

[Learn more about running Shopify CLI in a CI/CD pipeline](https://shopify.dev/docs/storefronts/themes/tools/cli/ci-cd).

***

## Upgrade Shopify CLI

To upgrade Shopify CLI to the latest version, run the [`upgrade`](https://shopify.dev/docs/api/shopify-cli#upgrade) command from your theme directory:

```terminal
shopify upgrade
```



To check your CLI version, run the [`version`](https://shopify.dev/docs/api/shopify-cli/common-commands/version) command from your theme directory:

```terminal
shopify version
```

***

## Migrate to Shopify CLI 3.​0+

In October 2022, support for themes was added to Shopify CLI 3.0. Shopify CLI 3.0+ provides a streamlined authentication and store management experience.

To learn about the differences between Shopify CLI 2.x and 3.0+, how to upgrade to Shopify CLI 3.0+, or how to use both Shopify CLI 2.x and 3.0+ on the same machine, refer to [Migrate to Shopify CLI 3.0+](https://shopify.dev/docs/storefronts/themes/tools/cli/migrate).

***

## Usage reporting

Anonymous usage statistics are collected by default. To opt out, you can use the environment variable `SHOPIFY_CLI_NO_ANALYTICS=1`.

***

## Contributing to Shopify CLI

Shopify CLI is open source. [Learn how to contribute](https://github.com/Shopify/cli/wiki/Contributors:-Introduction) to our GitHub repository.

***

## Where to get help

* **[Open a GitHub issue](https://github.com/shopify/cli/issues)** - To report bugs or request new features, open an issue in the Shopify CLI repository.
* **[.dev Community](https://community.shopify.dev/)** - Visit our forums to connect with the community and learn more about Shopify CLI development.

***
