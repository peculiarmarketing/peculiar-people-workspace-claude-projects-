Source URL: https://shopify.dev/docs/storefronts/themes/tools/github
Fetched: 2026-10-03 via curl https://shopify.dev/docs/storefronts/themes/tools/github.md (HTTP 200, markdown)

---
title: Shopify GitHub integration for themes
description: >-
  Learn about the Shopify GitHub integration, a tool that lets you make and
  track changes to theme code using Git.
source_url:
  html: 'https://shopify.dev/docs/storefronts/themes/tools/github'
  md: 'https://shopify.dev/docs/storefronts/themes/tools/github.md'
api_name: liquid
---

# Shopify Git​Hub integration for themes

The [Shopify GitHub app](https://shopify.dev/docs/api/github-app) lets you connect your GitHub and Shopify accounts. This lets you sync theme code to and from GitHub repositories and collaborate with other developers on your themes.

***

## Features

* Automatically pull and push theme code from any organization or repository associated with your GitHub account
* Connect one or more branches from a repository to easily develop and test new theme features or campaigns
* Keep a theme up to date with commits to a branch, and track edits made in the Shopify admin, including the [code editor](https://shopify.dev/docs/storefronts/themes/tools/code-editor) and [theme editor](https://shopify.dev/docs/storefronts/themes/tools/online-editor)
* Connect branches to unpublished or published themes

***

## How it works

The GitHub theme integration updates your theme in the Shopify admin whenever the connected branch is updated. It also commits changes made through the Shopify admin to the branch to ensure that the branch and theme in the Shopify admin always match.

**Note:**

Files are updated in GitHub whenever changes are made to a connected theme. This can't be disabled. If you want to separate the code that Shopify has access to from the rest of your code, then consider using multiple repositories or subtrees. For more information, refer to [Version control best practices for Shopify themes](https://shopify.dev/docs/storefronts/themes/best-practices/version-control).

### Commits by Shopify

When your theme is edited through the Shopify admin, any changes are automatically committed to your repository by Shopify. A commit is created when any owner, staff member, or collaborator makes changes. Changes are added as a commit to the connected branch when they are saved.

The commit body names the person who last edited the theme:

```text
Update from Shopify for theme Dawn


Committed from shop: Snowdevil
Theme last edited by: Bob Bobsen
```

Edits saved within about 10 seconds of each other are batched into one commit, so the name is the person who saved last, not a per-file record. If the theme has no recorded editor, the commit body lists only the shop name.

You can edit your theme in the following areas of the Shopify admin:

* The [theme editor](https://shopify.dev/docs/storefronts/themes/tools/online-editor). When you customize a theme using the theme editor, these customizations are stored in [setting files](https://shopify.dev/docs/storefronts/themes/architecture/settings), which are part of the theme code.
* The [code editor](https://shopify.dev/docs/storefronts/themes/tools/code-editor).
* [Theme apps](https://shopify.dev/docs/apps/build/online-store) installed in the Online Store.

#### Organization access

If you grant the Shopify GitHub app access to repositories in a GitHub organization, then any user that has a GitHub account that is part of the organization, and has the **Manage themes** permission or **Themes** permission, can view any repository that the app has access to in the list of available repositories. However, these users can only connect branches for which they have write permissions, and the branch needs to match the required [repository structure](#repository-structure).

If you want to prevent users from viewing certain repositories, then you should grant Shopify’s GitHub app access to only the repositories that you want to connect to the Shopify store. If you grant access to only specific repositories and you create a new repository that you want to use with Shopify, then you need to [grant the app access to the repository through GitHub](https://docs.github.com/en/organizations/keeping-your-organization-secure/reviewing-your-organizations-installed-integrations).

### Conflicts and error handling

If a user is editing an open file in the theme editor while the same file is being edited in GitHub or the code editor, then the user is warned that they're overriding the new changes when they save.

There are currently no conflict alerts in the code editor. The version of the file in the code editor overwrites the GitHub version of the file.

In case of a conflict in commits or pushes made outside Shopify, the developer has a chance to resolve it in GitHub or force push the change to overwrite the file in Shopify.

In limited cases, conflicts might occur if a file is saved in the theme editor or code editor and a change is pushed to the GitHub branch simultaneously. In this case, the commit coming from Shopify might be viewed as outdated and rejected by GitHub.

If you suspect that an error has occurred when pushing or pulling changes, then you can view the logs for the last few version control events by clicking **View logs** beside the **Last saved** timestamp on the theme card.

If you believe that the theme has fallen out of date with the branch, then you can pull the latest version of the branch manually by going to the theme card and selecting **Actions** > **Reset to last commit**.

***

## Limitations

* Only repositories to which you have write access can be used to create a new theme.
* GitHub outside collaborators can't connect branches. Only members of the GitHub organization with write access can.
* Personal repositories where you're a GitHub collaborator, but not the owner, aren't visible in the list of available repositories.

These limitations describe GitHub permissions. They're unrelated to Shopify [collaborator accounts](https://shopify.dev/docs/storefronts/themes/tools/collaborator-accounts), which can use the integration.

***

## Repository structure

You can connect only branches that match the default Shopify theme [folder structure](https://shopify.dev/docs/storefronts/themes/architecture#directory-structure-and-component-types). This structure represents a buildless theme, or a theme that has already gone through any necessary [file transformations](https://shopify.dev/docs/storefronts/themes/best-practices/file-transformation).

Folders in the repository that don't match the default theme structure are ignored.

***

## Branch management strategies

Consider the following when managing themes connected to GitHub repositories in Shopify:

* You can't reconnect a branch to a theme after it has been disconnected. If you reconnect a branch, then it's added as a new theme.

* If an unpublished theme is connected to a branch and then published, then it maintains its connection to the branch.

  To understand the relationship between branches and themes, and how to optimize your workflow to use branches effectively, refer to our [version control best practices](https://shopify.dev/docs/storefronts/themes/best-practices/version-control).

***

## Step 1: Connect a theme repo

Make sure you've installed the [Shopify GitHub app](https://shopify.dev/docs/api/github-app) first.

You can connect a repo as the store owner, from a staff account, or from a [collaborator account](https://shopify.dev/docs/storefronts/themes/tools/collaborator-accounts), as long as the account has the **Manage themes** permission or **Themes** permission.

1. From your Shopify admin, go to **Online Store** > **Themes**.
2. In the **Theme library** section, click **Add theme** > **Connect from GitHub**.
3. In the **Connect theme** pane, select your organization or account.
4. Under **Repository**, select your repo.
5. Under **Branch**, search for the branch you want to connect.

The theme appears in your theme library. Themes that are connected to GitHub list the repository, branch name, and last commit time on the theme card.

***

## Step 2: Test the connection

Try making a small change to the theme and then verify that a commit was made in the branch.

1. From your Shopify admin, go to **Online Store** > **Themes**.
2. On the theme that's connected to GitHub, click **Customize**.
3. Change any setting in your theme. For example, in Dawn, you might change the text on the announcement bar.
4. Click **Save**, and then exit the theme editor.
5. In the theme library, on the card for the theme, click the name of the branch to navigate to GitHub.
6. Note the most recent commit. It should list the `shopify` bot as the author, and the commit body should name the shop and the person who last edited the theme.

![A commit from Shopify in the GitHub repo](https://shopify.dev/assets/assets/images/themes/github/github-update-CZXTUcSD.png)

If desired, you can also push a change to the branch from your local machine. After you push a commit to your branch, the **Last saved** date on the theme updates and the change is visible in the theme.

![The card for a theme that's connected to GitHub](https://shopify.dev/assets/assets/images/themes/github/github-card-C62fPPvl.png)

***

## Step 3: Publish the theme

To track changes to your published theme, you need to publish a theme from your theme library that's connected to a GitHub branch. You might add your main branch as a theme so you can keep your [published theme up to date](https://shopify.dev/docs/storefronts/themes/best-practices/version-control) using Git.

***
