# 05. Shopify CLI theme commands

## Command index: https://shopify.dev/docs/api/shopify-cli/theme
Commands listed: theme check, theme console, theme delete, theme dev, theme duplicate, theme info, theme init, theme language-server, theme list, theme metafields pull, theme open, theme package, theme preview, theme profile, theme publish, theme pull, theme push, theme rename, theme share.
> "theme list Lists the themes in your store, along with their IDs and statuses."
> "theme preview Applies a JSON overrides file to a theme and creates or updates a preview."
> "theme profile Profile the Shopify Liquid on a given page."

## theme dev: https://shopify.dev/docs/api/shopify-cli/theme/theme-dev
> "Uploads the current theme as the specified theme, or a development theme, to a store so you can preview it."
> Returns "A link to your development theme at http://127.0.0.1:9292. This URL can hot reload local changes to CSS and sections, or refresh the entire page when a file changes" plus "A link to the editor for the theme in the Shopify admin" and "A preview link that you can share with other developers."
> "If you already have a development theme for your current environment, then this command replaces the development theme with your local theme. You can override this using the --theme-editor-sync flag."
> "Development themes are deleted when you run shopify auth logout."
Flags (verbatim names): --auth-alias, --error-overlay (silent|default), --host (default 127.0.0.1), --listing, --live-reload ("hot-reload Hot reloads local changes to CSS and sections (default) full-page Always refreshes the entire page off Deactivate live reload"), --no-color, --notify, --open, --store-password, --theme-editor-sync ("Synchronize Theme Editor updates in the local theme files."), --verbose, -a/--allow-live ("Allow development on a live theme."), -e/--environment, -n/--nodelete, -o/--only ("Hot reload only files that match the specified pattern."), -s/--store, -t/--theme, -x/--ignore. (--port mentioned in description.)
Syntax: `shopify theme dev [flags]`
Getting started (https://shopify.dev/docs/storefronts/themes/getting-started/create): `shopify theme dev --store my-store` ; "You need to pass the --store flag the first time ... To check which store you're connected to, run shopify theme info." ; "This preview is only available in Google Chrome."

Development themes (https://shopify.dev/docs/storefronts/themes/tools/cli):
> "Development themes are temporary, hidden themes ... Development themes don't count toward your theme limit, and are deleted from the store after seven days of inactivity."

## theme push: https://shopify.dev/docs/api/shopify-cli/theme/theme-push
> "Uploads your local theme files to Shopify, overwriting the remote version if specified. If no theme is specified, then you're prompted to select the theme to overwrite"
Flags: --auth-alias, --listing, --no-color, --password, --path, --strict ("Require theme check to pass without errors before pushing. Warnings are allowed."), --verbose, -a/--allow-live ("Allow push to a live theme. Required in non-interactive environments when targeting the live theme."), -c/--development-context ("Unique identifier for a development theme context (e.g., PR number, branch name)"), -d/--development, -e/--environment, -j/--json, -l/--live, -n/--nodelete ("Prevent deleting remote files that don't exist locally."), -o/--only ("Upload only the specified files (Multiple flags allowed). Wrap the value in double quotes if you're using wildcards."), -p/--publish ("Publish as the live theme after uploading."), -s/--store, -t/--theme ("Theme ID or name of the remote theme ... When using --unpublished without --development, use --theme to provide the new theme name."), -u/--unpublished ("Create a new unpublished theme and push to it."), -x/--ignore.
Examples: `shopify theme push` ; `shopify theme push --unpublished --json`
Tutorial (https://shopify.dev/docs/storefronts/themes/getting-started/customize): "If you don't want to update an existing theme in the store with your changes, then you can upload your theme to the theme library as a new, unpublished theme using the --unpublished flag."

## theme pull: https://shopify.dev/docs/api/shopify-cli/theme/theme-pull
Flags: --auth-alias, --no-color, --password, --path, --verbose, -d/--development, -e/--environment, -l/--live, -n/--nodelete ("Prevent deleting local files that don't exist remotely."), -o/--only ("Download only the specified files"), -s/--store, -t/--theme, -x/--ignore. Syntax `shopify theme pull [flags]`.

## theme check: https://shopify.dev/docs/api/shopify-cli/theme/theme-check
Flags: --auth-alias, --fail-level ("Minimum severity for exit with error code"), --init ("Generate a .theme-check.yml file"), --list ("List enabled checks"), --no-color, --path, --print ("Output active config to STDOUT"), --verbose, -a/--auto-correct ("Automatically fix offenses"), -C/--config ("Use the config provided, overriding .theme-check.yml if present ... theme-check:theme-app-extension, theme-check:recommended, theme-check:all"), -e/--environment, -o/--output ("The output format to use"), -v/--version. Syntax `shopify theme check [flags]`.

## theme share: https://shopify.dev/docs/api/shopify-cli/theme/theme-share
> "Uploads your theme as a new, unpublished theme in your theme library. The theme is given a randomized name. This command returns a preview link that you can share with others."
Flags: --auth-alias, --listing, --no-color, --password, --path, --verbose, -e/--environment, -s/--store.

## theme duplicate: https://shopify.dev/docs/api/shopify-cli/theme/theme-duplicate
> "If you want to duplicate your local theme, you need to run shopify theme push first. ... Prompts and confirmations are not shown when duplicate is run in a CI environment or the --force flag is used, therefore you must specify a theme ID using the --theme flag. You can optionally name the duplicated theme using the --name flag."
> Error example: "errors": ["Maximum number of themes reached"]

## theme publish: https://shopify.dev/docs/api/shopify-cli/theme/theme-publish
> "Publishes an unpublished theme from your theme library ... You can skip this confirmation using the --force flag." -f/--force "Skip confirmation. Required if non interactive." -t/--theme "Required if non interactive."

## theme open: https://shopify.dev/docs/api/shopify-cli/theme/theme-open
Flags include -d/--development, -E/--editor ("Open the theme editor for the specified theme in the browser."), -l/--live, -t/--theme.

## NOT CONFIRMED
- theme list flags (e.g. --role, --name, --json): the flag table was not returned by search. Only the description was confirmed.
