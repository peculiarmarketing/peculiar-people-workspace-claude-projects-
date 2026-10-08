# Companion: WebSensePro blog post (video 0tEkfZ4vtcs)

- Source: https://websensepro.com/blog/build-shopify-themes-in-minutes-claude-code-mcp/
- Fetched: 2026-10-03 with curl, HTML stripped to text, site navigation removed
- Verification note: the MCP install command in this post (npx @shopify/mcp-cli@latest init) does NOT match the package shown on Shopify's official page https://shopify.dev/docs/apps/build/devmcp as fetched 2026-10-03, which uses @shopify/dev-mcp@latest (via npx -y) and now also points to the Shopify AI Toolkit (npx skills add Shopify/shopify-ai-toolkit).

Shopify theme development doesn’t have to be slow. By combining GitHub version control with cloud code and MCP servers, you can transform how your team builds and deploys Shopify themes

In this guide, I’ll walk you through a three-step process that will revolutionize your Shopify development workflow.

Why This Matters

Traditional Shopify Development:

- Manual code management

- No version history

- Outdated documentation

- Slow team collaboration

The New Way:

- ✅ Full version control with GitHub

- ✅ AI-powered coding assistance

- ✅ Real-time Shopify documentation

- ✅ Team collaboration in minutes

Step 1: Connect GitHub with VS Code

First, let’s establish version control for your Shopify theme:

# Initialize git in your theme folder
git init
git add .
git commit -m "Initial commit"

Create a GitHub repository:

- Go to GitHub.com

- Click “+” → New repository

- Name it (e.g., “shopify-theme”)

- Connect your local folder:

git remote add origin https://github.com/yourusername/shopify-theme.git
git push -u origin main

Connect to Shopify:

- Go to your Shopify admin → Online Store → Themes

- Click “Import theme” → “Connect from GitHub”

- Select your repository

- Click “Connect” and “Publish”

Now every code change tracks automatically with full version history!

Step 2: Add Cloud Code to VS Code

Supercharge your coding with AI assistance:

- Open VS Code

- Go to Extensions (Ctrl+Shift+X)

- Search “Claude Code”

- Click Install

Choose your plan:

- Claude AI Subscription: Fixed monthly pricing ($70-100)

- Anthropic Console: Pay-as-you-go (API usage only)

Once connected, Claude Code reads your entire project and suggests/implement changes automatically.

Step 3: Add MCP Server (The Game-Changer)

MCP = Model Context Protocol – this keeps your AI updated with the latest Shopify documentation.

Why it matters:

Shopify documentation updates frequently. MCP server pulls the latest changes automatically, so your AI always has current context.

Installation:

# In VS Code terminal, run:
npx @shopify/mcp-cli@latest init

After installation, you’ll see “Shopify Dev MCP” in your Claude Code chat. Type /mcp to manage servers.

The Result: What You Can Achieve

Before:

- Manual code updates

- Outdated documentation

- Slow team onboarding

- No version control

After:

- Hours instead of weeks for theme development

- AI-powered coding with latest Shopify context

- Full version history for your entire team

- Real-time collaboration via GitHub

- Always current Shopify documentation

Pro Tips

- Commit often – Small, descriptive commits make history useful

- Use branches – Test features without breaking main theme

- Leverage AI – Let Claude Code handle repetitive tasks

- Keep MCP updated – Run updates monthly for latest docs

Frequently Asked Questions

Q: Do I need coding experience?

A: Basic HTML/CSS knowledge helps, but this workflow works for beginners too.

Q: Is this free?

A: GitHub is free. VS Code is free. Claude Code has both free tiers and paid plans.

Q: Can my whole team use this?

A: Yes! That’s the beauty – multiple developers can work simultaneously.

Ready to Transform Your Shopify Development?

This three-step workflow turns months of development into minutes. Whether you’re a solo developer or leading a team, GitHub + cloud code + MCP server is the ultimate Shopify development stack.

Want to learn more? Drop your questions in the comments below!

Found this helpful? Share it with your developer friends!
