Source URL: https://shopify.dev/docs/api/shopify-cli/theme/theme-dev
Fetched: 2026-10-03 via curl https://shopify.dev/docs/api/shopify-cli/theme/theme-dev.md (HTTP 200, markdown)

---
title: theme dev
description: >-
  Uploads the current theme as the specified theme, or a development theme, to a
  store so you can preview it.
source_url:
  html: 'https://shopify.dev/docs/api/shopify-cli/theme/theme-dev'
  md: 'https://shopify.dev/docs/api/shopify-cli/theme/theme-dev.md'
api_name: shopify-cli
---

# theme dev

Uploads the current theme as the specified theme, or a [development theme](https://shopify.dev/docs/themes/tools/cli#development-themes), to a store so you can preview it.

This command returns the following information:

* A link to your development theme at <http://127.0.0.1:9292>. This URL can hot reload local changes to CSS and sections, or refresh the entire page when a file changes, enabling you to preview changes in real time using the store's data.

  You can specify a different network interface and port using `--host` and `--port`.

* A link to the [editor](https://shopify.dev/docs/themes/tools/online-editor) for the theme in the Shopify admin.

* A [preview link](https://help.shopify.com/manual/online-store/themes/adding-themes#share-a-theme-preview-with-others) that you can share with other developers.

If you already have a development theme for your current environment, then this command replaces the development theme with your local theme. You can override this using the `--theme-editor-sync` flag.

**Note:**

You can't preview checkout customizations using <http://127.0.0.1:9292>.

Development themes are deleted when you run `shopify auth logout`. If you need a preview link that can be used after you log out, then you should [share](https://shopify.dev/docs/api/shopify-cli/theme/theme-share) your theme or [push](https://shopify.dev/docs/api/shopify-cli/theme/theme-push) to an unpublished theme on your store.

You can run this command only in a directory that matches the [default Shopify theme folder structure](https://shopify.dev/docs/themes/tools/cli#directory-structure).

#### Flags

The following flags are available for the `theme dev` command:

* **--auth-alias \<value>**

  **string**

  **env: SHOPIFY\_FLAG\_AUTH\_ALIAS**

  Alias of the Shopify account to use for authentication.

* **--error-overlay \<value>**

  **string**

  **env: SHOPIFY\_FLAG\_ERROR\_OVERLAY**

  Controls the visibility of the error overlay when an theme asset upload fails:

  * silent Prevents the error overlay from appearing.
  * default Displays the error overlay.

* **--host \<value>**

  **string**

  **env: SHOPIFY\_FLAG\_HOST**

  Set which network interface the web server listens on. The default value is 127.0.0.1.

* **--listing \<value>**

  **string**

  **env: SHOPIFY\_FLAG\_LISTING**

  The listing preset to use for multi-preset themes. Applies preset files from listings/\[preset-name] directory.

* **--live-reload \<value>**

  **string**

  **env: SHOPIFY\_FLAG\_LIVE\_RELOAD**

  The live reload mode switches the server behavior when a file is modified:

  * hot-reload Hot reloads local changes to CSS and sections (default)
  * full-page Always refreshes the entire page
  * off Deactivate live reload

* **--no-color**

  **env: SHOPIFY\_FLAG\_NO\_COLOR**

  Disable color output.

* **--notify \<value>**

  **string**

  **env: SHOPIFY\_FLAG\_NOTIFY**

  The file path or URL. The file path is to a file that you want updated on idle. The URL path is where you want a webhook posted to report on file changes.

* **--open**

  **env: SHOPIFY\_FLAG\_OPEN**

  Automatically launch the theme preview in your default web browser.

* **--password \<value>**

  **string**

  **env: SHOPIFY\_CLI\_THEME\_TOKEN**

  Password generated from the Theme Access app or an Admin API token.

* **--path \<value>**

  **string**

  **env: SHOPIFY\_FLAG\_PATH**

  The path where you want to run the command. Defaults to the current working directory.

* **--port \<value>**

  **string**

  **env: SHOPIFY\_FLAG\_PORT**

  Local port to serve theme preview from. Must be between 1 and 65535.

* **--reconciliation-strategy \<value>**

  **string**

  **env: SHOPIFY\_FLAG\_RECONCILIATION\_STRATEGY**

  How to resolve JSON conflicts when --theme-editor-sync is enabled. Use keep-local to keep local files, keep-remote to keep remote files, or abort to fail instead of prompting.

* **--standard-events-inspector**

  **env: SHOPIFY\_FLAG\_STANDARD\_EVENTS\_INSPECTOR**

  Inject the standard events inspector into storefront HTML.

* **--store-password \<value>**

  **string**

  **env: SHOPIFY\_FLAG\_STORE\_PASSWORD**

  The password for storefronts with password protection.

* **--theme-editor-sync**

  **env: SHOPIFY\_FLAG\_THEME\_EDITOR\_SYNC**

  Synchronize Theme Editor updates in the local theme files.

* **--verbose**

  **env: SHOPIFY\_FLAG\_VERBOSE**

  Increase the verbosity of the output. May include sensitive data.

* **-a, --allow-live**

  **env: SHOPIFY\_FLAG\_ALLOW\_LIVE**

  Allow development on a live theme.

* **-e, --environment \<value>**

  **string**

  **env: SHOPIFY\_FLAG\_ENVIRONMENT**

  The environment to apply to the current command.

* **-n, --nodelete**

  **env: SHOPIFY\_FLAG\_NODELETE**

  Prevents files from being deleted in the remote theme when a file has been deleted locally. This applies to files that are deleted while the command is running, and files that have been deleted locally before the command is run.

* **-o, --only \<value>**

  **string**

  **env: SHOPIFY\_FLAG\_ONLY**

  Hot reload only files that match the specified pattern.

* **-s, --store \<value>**

  **string**

  **env: SHOPIFY\_FLAG\_STORE**

  Store URL. It can be the store prefix (example) or the full myshopify.com URL (example.myshopify.com, <https://example.myshopify.com>).

* **-t, --theme \<value>**

  **string**

  **env: SHOPIFY\_FLAG\_THEME\_ID**

  Theme ID or name of the remote theme.

* **-x, --ignore \<value>**

  **string**

  **env: SHOPIFY\_FLAG\_IGNORE**

  Skip hot reloading any files that match the specified pattern.

Examples

### Examples

* ####

  ##### theme dev

  ```sh
  shopify theme dev [flags]
  ```

***
