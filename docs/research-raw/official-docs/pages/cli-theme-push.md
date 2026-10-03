Source URL: https://shopify.dev/docs/api/shopify-cli/theme/theme-push
Fetched: 2026-10-03 via curl https://shopify.dev/docs/api/shopify-cli/theme/theme-push.md (HTTP 200, markdown)

---
title: theme push
description: >-
  Uploads your local theme files to Shopify, overwriting the remote version if
  specified.
source_url:
  html: 'https://shopify.dev/docs/api/shopify-cli/theme/theme-push'
  md: 'https://shopify.dev/docs/api/shopify-cli/theme/theme-push.md'
api_name: shopify-cli
---

# theme push

Uploads your local theme files to Shopify, overwriting the remote version if specified.

If no theme is specified, then you're prompted to select the theme to overwrite from the list of the themes in your store.

You can run this command only in a directory that matches the [default Shopify theme folder structure](https://shopify.dev/docs/themes/tools/cli#directory-structure).

This command returns the following information:

* A link to the [editor](https://shopify.dev/docs/themes/tools/online-editor) for the theme in the Shopify admin.
* A [preview link](https://help.shopify.com/manual/online-store/themes/adding-themes#share-a-theme-preview-with-others) that you can share with others.

If you use the `--json` flag, then theme information is returned in JSON format, which can be used as a machine-readable input for scripts or continuous integration.

Sample output:

```json
{
  "theme": {
    "id": 108267175958,
    "name": "MyTheme",
    "role": "unpublished",
    "shop": "mystore.myshopify.com",
    "editor_url": "https://mystore.myshopify.com/admin/themes/108267175958/editor",
    "preview_url": "https://mystore.myshopify.com/?preview_theme_id=108267175958"
  }
}
```

#### Flags

The following flags are available for the `theme push` command:

* **--auth-alias \<value>**

  **string**

  **env: SHOPIFY\_FLAG\_AUTH\_ALIAS**

  Alias of the Shopify account to use for authentication.

* **--listing \<value>**

  **string**

  **env: SHOPIFY\_FLAG\_LISTING**

  The listing preset to use for multi-preset themes. Applies preset files from listings/\[preset-name] directory.

* **--no-color**

  **env: SHOPIFY\_FLAG\_NO\_COLOR**

  Disable color output.

* **--password \<value>**

  **string**

  **env: SHOPIFY\_CLI\_THEME\_TOKEN**

  Password generated from the Theme Access app or an Admin API token.

* **--path \<value>**

  **string**

  **env: SHOPIFY\_FLAG\_PATH**

  The path where you want to run the command. Defaults to the current working directory.

* **--strict**

  **env: SHOPIFY\_FLAG\_STRICT\_PUSH**

  Require theme check to pass without errors before pushing. Warnings are allowed.

* **--verbose**

  **env: SHOPIFY\_FLAG\_VERBOSE**

  Increase the verbosity of the output. May include sensitive data.

* **-a, --allow-live**

  **env: SHOPIFY\_FLAG\_ALLOW\_LIVE**

  Allow push to a live theme. Required in non-interactive environments when targeting the live theme.

* **-c, --development-context \<value>**

  **string**

  **env: SHOPIFY\_FLAG\_DEVELOPMENT\_CONTEXT**

  Unique identifier for a development theme context (e.g., PR number, branch name). Reuses an existing development theme with this context name, or creates one if none exists.

* **-d, --development**

  **env: SHOPIFY\_FLAG\_DEVELOPMENT**

  Push theme files from your remote development theme. Use --development, --live, --theme, or --unpublished in non-interactive environments.

* **-e, --environment \<value>**

  **string**

  **env: SHOPIFY\_FLAG\_ENVIRONMENT**

  The environment to apply to the current command.

* **-j, --json**

  **env: SHOPIFY\_FLAG\_JSON**

  Output the result as JSON. Automatically disables color output.

* **-l, --live**

  **env: SHOPIFY\_FLAG\_LIVE**

  Push theme files from your remote live theme. Use --development, --live, --theme, or --unpublished in non-interactive environments.

* **-n, --nodelete**

  **env: SHOPIFY\_FLAG\_NODELETE**

  Prevent deleting remote files that don't exist locally.

* **-o, --only \<value>**

  **string**

  **env: SHOPIFY\_FLAG\_ONLY**

  Upload only the specified files (Multiple flags allowed). Wrap the value in double quotes if you're using wildcards.

* **-p, --publish**

  **env: SHOPIFY\_FLAG\_PUBLISH**

  Publish as the live theme after uploading.

* **-s, --store \<value>**

  **string**

  **env: SHOPIFY\_FLAG\_STORE**

  Store URL. It can be the store prefix (example) or the full myshopify.com URL (example.myshopify.com, <https://example.myshopify.com>).

* **-t, --theme \<value>**

  **string**

  **env: SHOPIFY\_FLAG\_THEME\_ID**

  Theme ID or name of the remote theme. Use --development, --live, --theme, or --unpublished in non-interactive environments. When using --unpublished without --development, use --theme to provide the new theme name.

* **-u, --unpublished**

  **env: SHOPIFY\_FLAG\_UNPUBLISHED**

  Create a new unpublished theme and push to it. Use --development, --live, --theme, or --unpublished in non-interactive environments. When using --unpublished without --development, use --theme to provide the new theme name.

* **-x, --ignore \<value>**

  **string**

  **env: SHOPIFY\_FLAG\_IGNORE**

  Skip uploading the specified files (Multiple flags allowed). Wrap the value in double quotes if you're using wildcards.

Examples

### Examples

* ####

  ##### theme push

  ```sh
  shopify theme push

  shopify theme push --unpublished --json
  ```

***
