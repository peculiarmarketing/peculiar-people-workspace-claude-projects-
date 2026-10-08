# 10. Theme updates and GitHub integration

## Theme Store update mechanics (developer side): https://shopify.dev/docs/storefronts/themes/store/success/updates
> "A theme is automatically updated only if all theme files, except settings_data.json and any JSON files in the /templates directory, are in their original state. If a theme can't be automatically updated, then merchants are shown a notification on the Online store > Themes page letting them know that they can apply the update to an unpublished copy of their theme to be reviewed and published."
> Manual update triggers: "A setting ID is changed or removed / A setting type is changed or removed / The min value for a setting of type range is increased / The max value for a setting of type range is decreased / A section or block is removed"
> "The updated theme is installed as an unpublished theme in their theme library ... The parent theme is not modified."
> "If you change the class of a section or change a CSS class name, then a merchant's custom CSS might be invalidated."
Implication: adding a custom section file (sections/*.liquid) means the theme is no longer in its original state, so it will not auto update; updates land as an unpublished copy.

## Merchant side (help.shopify.com is egress blocked; text from WebSearch snippets of https://help.shopify.com/en/manual/online-store/themes/managing-themes/updating-themes, NOT directly fetched, treat as secondhand)
> "When you update your theme, customizations made using the theme editor are copied over and applied to the updated theme. If you or an installed app have made code changes and your code edits don't conflict with the update, then your code edits will be included with the update."
> "If changes that you've made to a theme's code are incompatible with a theme update, then all your code changes are removed in the updated copy."
> "you should always save a copy of any customized code before updating your theme."

## GitHub integration: https://shopify.dev/docs/storefronts/themes/tools/github
> "The GitHub theme integration updates your theme in the Shopify admin whenever the connected branch is updated. It also commits changes made through the Shopify admin to the branch to ensure that the branch and theme in the Shopify admin always match."
> "Note: Files are updated in GitHub whenever changes are made to a connected theme. This can't be disabled."
> "Connect branches to unpublished or published themes"
> "Edits saved within about 10 seconds of each other are batched into one commit"
> "You can't reconnect a branch to a theme after it has been disconnected. If you reconnect a branch, then it's added as a new theme."
> "If an unpublished theme is connected to a branch and then published, then it maintains its connection to the branch."
> Connect: "From your Shopify admin, go to Online Store > Themes. In the Theme library section, click Add theme > Connect from GitHub."
> "the branch needs to match the required repository structure"
## Version control: https://shopify.dev/docs/storefronts/themes/best-practices/version-control
> "consider connecting your main or master branch to your store and then publishing the resulting theme" ; "The Shopify GitHub integration only supports the default Shopify theme folder structure." ; "If you use a build pipeline ... create a specific deploy branch"
## settings_data.json: https://shopify.dev/docs/storefronts/themes/architecture/config/settings-data-json
> "Any time that the value of color_page_bg is changed in the theme editor, settings_data.json is updated with the new value."
