# Build Shopify Themes in MINUTES -[Claude Code & MCP]

- URL: https://www.youtube.com/watch?v=0tEkfZ4vtcs
- Channel: UNVERIFIED (likely WebSensePro, per a same-titled blog post). Length about 11:35. Upload approx 2026-03-13 (search-result estimate).
- Tool: Higgsfield video_analysis (job 599ac55f-6b2f-463a-ac49-a4c17f7cd719), completed 2026-10-03. Machine scene list (audio + visual description). Not a verbatim transcript; no frames saved.

## Scenes (audio verbatim from the analysis; visuals summarized)

0:00-0:50. Intro. Audio: "...how you can connect Claude Code and use GitHub to boost your Shopify theme development." "So if you were building a theme in months or in days, you could do that in hours and minutes using the power of new Claude Code." "The first step will be to connect GitHub with the VS Code. In the second step, we will add the Claude Code. And in the third step, we will add MCP server."

0:51-1:02. Audio: "... I've added the latest version of Horizon theme." Visual: Shopify admin Themes page, Horizon active.

1:03-1:35. Creates a private GitHub repo named "shopify-claude-tutorial".

1:36-2:34. Downloads the theme from admin (theme files arrive by email as a zip), unzips into a local folder "shopify-theme".

2:35-4:32. Opens the folder in VS Code. Audio: "First I need to initialize Git for this folder ... Now we are getting this error, because we haven't yet initialized our Git." "In order to fix this bug, we will add this command here: 'git init', 'git add .', 'git commit'." Visual: commands typed into the VS Code terminal.

4:33-5:00. Files appear on GitHub as "Initial commit".

5:01-6:13. Audio: "We will now connect our development store with this GitHub repo. Click on 'Connect from GitHub'." "Our main branch is now connected with the theme. Now whatever change we make, it will show up in the revision history in the form of commits." Visual: Shopify admin, Import theme, Connect from GitHub, repo and main branch chosen.

6:14-7:15. Edits base.css in the Shopify code editor (100% to 99%), saves; GitHub shows a commit from the Shopify bot.

7:16-8:04. Edits locally (101%), commits "test-change".

8:05-9:51. Installs the Claude Code VS Code extension (published by Anthropic); explains Claude subscription vs Anthropic Console API billing.

9:52-10:45. Audio: "The most powerful thing to do is to add an MCP server. Go to the documentation 'Shopify MCP Claude Code'. Simply copy this command and paste this command in the terminal." "Type in '/mcp' and you can see that we have shopify-dev-mcp connected." The exact command text is not in the analysis output.

10:46-11:35. Audio: "MCP meaning Model Context Protocol. It is going to pull the latest and updated documentation in the context of Claude Code." Wrap-up.

## Notes for the briefing
- Shows: GitHub integration for themes (two-way sync, admin edits become commits), Claude Code VS Code extension, Dev MCP verified with /mcp.
- Does not show: building a section, theme check, a preview step, or what happens when the agent is wrong. The title promises themes "in minutes"; the video only sets up tooling.
- Uses a development store per the audio ("connect our development store").
