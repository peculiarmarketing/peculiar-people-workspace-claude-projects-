# How to Connect Claude AI to Your Shopify Store (No More Copy-Pasting Code)

- URL: https://www.youtube.com/watch?v=qlB9JppKGQw
- Channel: WEBEXP
- Published: 2026-04-22
- Length: 6:08
- Views at fetch: 28558
- Fetched: 2026-10-03 with yt-dlp (YouTube auto-generated captions), file qlB9JppKGQw.en.vtt
- Coverage: FULL TRANSCRIPT from captions. NO FRAMES: video download was blocked in this session, so on-screen code, settings and commands were not seen. Auto captions can mishear technical terms.

## Chapters

- 0:00 Intro (the old way vs the new way)
- 0:35 Prerequisites
- 0:53 Step 1: Install Claude Desktop + GitHub Desktop
- 1:18 Step 2: Create a GitHub Repository
- 1:36 Step 3: Download Theme + Clone Repo
- 2:31 Step 4: Commit and Push to GitHub
- 2:54 Step 5: Connect Theme to GitHub in Shopify
- 3:22 Step 6: Create a GitHub API Token
- 4:16 Step 7: Create Cowork Project + Connect Token
- 5:18 Test the Connection
- 5:40 Outro + What's Next

## Description

```
Stop copy-pasting code between Claude and Shopify's code editor. In this tutorial, I'll show you how to connect Claude Cowork directly to your Shopify store through GitHub, so Claude edits your theme files and pushes changes in real time. One-time setup, then you never copy-paste code again.

Timestamps:
0:00, Intro (the old way vs the new way)
0:35, Prerequisites
0:53, Step 1: Install Claude Desktop + GitHub Desktop
1:18, Step 2: Create a GitHub Repository
1:36, Step 3: Download Theme + Clone Repo
2:31, Step 4: Commit and Push to GitHub
2:54, Step 5: Connect Theme to GitHub in Shopify
3:22, Step 6: Create a GitHub API Token
4:16, Step 7: Create Cowork Project + Connect Token
5:18, Test the Connection
5:40, Outro + What's Next

Step 7 command (swap in your own token, username, and repo name):
git remote set-url origin https://YOUR_TOKEN@github.com/YOUR_USERNAME/YOUR_REPO.git

Links:
📥 Download Claude Desktop: https://claude.com/download
📥 Download GitHub Desktop: https://desktop.github.com
🔑 GitHub Personal Access Tokens: https://github.com/settings/tokens

Built by WEBEXP, custom Shopify development and apps for brands that take their identity seriously. www.webexp.dev

-

→ Try Claude AI free for a week: https://claude.ai/referral/XQMRjxvvgw
→ Start your Shopify store (free trial): https://shopify.pxf.io/webexp
→ Add a music player to your Shopify store (free): https://apps.shopify.com/wavexp-playlist-music-player
→ Hire WEBEXP: https://webexp.dev/pages/hire-us
→ Contact: contact@webexp.dev


#Shopify #ClaudeAI #ClaudeCowork #ShopifyDev #WebDevelopment
```

## Transcript

[00:00:00] If y'all are building Shopify themes with Claude, you're probably doing what I used to do. Copy the code from the chat, paste into the Shopify's code editor, hit save, refresh, see something's off, go back to Claude, get new code, copy, paste, save, refresh again. Over and over and over. It works, but it's slow. So, in this video, I'm going to show y'all how I connected Claude Code Work to my Shopify store, so now Claude just edits my files and pushes the changes for me. I just tell it what I want to build and hit refresh. Once you set this up, you're not copying

[00:00:32] pasting code ever again. Let's get into it. Real quick. Here's what you're going to need before we start. A paid Claude plan. I'm on a max plan, but pro should work, too. A GitHub account. That's free. A Shopify store theme you want to work on, and a desktop with the Claude desktop app installed. If you got all of that, we're good to go. Step one, we got to install two apps. Go to claude.com/download, grab the Claude desktop app, install it, and sign in. Make sure you're on a paid

[00:01:05] plan so you can use Code Work. Then go to desktop.github.com and download GitHub Desktop. We're going to use this to get your theme files uploaded before Code Work takes over. Once both are installed and you're signed in, we're ready to go. Step two, go to github.com and make a new repository. Name it whatever your project is. I'll call mine my-shopify-theme. Make it private. Don't check any of the boxes. No read me, none of that. Just create it empty. This is where your theme files are going to live. Step

[00:01:37] three, we need to get your theme files into that repo. Go to your Shopify admin, find the theme you want to work on, hit the three dots, and download that theme file. Shopify is going to email you a zip link. Click it and download it. Unzip it. Now open GitHub Desktop. In the top left, click the current repository drop down then hit add then clone repository. You'll see your repos listed. Pick the one you just made. At the bottom it shows the local path where the folder is going to be created. I keep mine in documents GitHub. Hit clone. Now open

[00:02:11] that folder in finder. It's going to be empty. Open another tab with your unzipped theme files. Select everything and drag it into that clone folder. When you go back to GitHub desktop, you'll see all the files show up as changes. If you see a .DS_Store file in there, uncheck it. That's just a Mac file that doesn't need to be in your repo. Step four, commit and push. Type something like initial theme upload in the summary. Hit commit to main then hit publish branch. Give it a minute. When it's done, go to github.com and

[00:02:45] refresh your repo page. You should see all your theme folders in there. Assets, config, layout, sections, snippets, templates, all of it. Step five, go back to your Shopify dashboard online store. At the top right corner, hit add theme and you'll see connect from GitHub. Click that. Authorize your GitHub if it asks. Pick the repo you just pushed to, main branch, and hit connect. Shopify is going to make a new draft theme that's linked to that repo. Anytime something gets pushed to GitHub, this theme updates automatically. Hit preview real

[00:03:18] quick just to make sure it loads right. Step six, this one's important so pay attention. Go to GitHub, click your profile pic and hit settings. Scroll all the way down on the left sidebar. At the very bottom you'll see developer settings. Click that. Then personal access tokens, fine grain tokens. Generate a new token. Give it a name. I name mine after the project like co-work my project or my Shopify theme project. Set an expiration date. Under repository access, pick only select repositories

[00:03:51] and choose a repo you just made. For permissions, set the contents to read and write and leave metadata to read. That's it. Just those two. Hit generate token. Now, copy that token immediately. Once you leave this page, you can't see it again. Quick tip, I make a separate token for every project. That way each one only has access to its own repo and nothing else. It keeps things clean, safe, and organized. Step seven, open Cloud Desktop and switch to Co-work. Hit new project. That's going to give you three options. Pick using an

[00:04:23] existing folder and point it to that theme folder GitHub Desktop created on your computer. Now, here's the important part. In your first message, tell Co-work to set the remote URL with your token. The command is get remote set {dash} URL origin. Then the URL with the token embedded in it. I'll include that full format in the description, so y'all can just copy and paste it and swap in your own token, username, and repo name. Once Co-work runs that command, it can push to your repo. Then tell Co-work to create a {dot} gitignore file, so it doesn't accidentally commit any

[00:04:55] sensitive files. Quick tip, Co-work might warn you about pasting a token. That's normal. The token gets stored in your local git config, not in any files that get pushed. That's why we make a separate token for every project, so each one only has access to its own repo. So, it's good practice to set an expiration date and once you're done, to be safe, you can also delete that token if you like. All right, let's test it. I'm going to tell Co-work to make a custom announcement bar, a black background, white text that says "Hello, world." Co-work creates a section, wires it into the header, commits, and pushes.

[00:05:28] Now, I go back to my Shopify preview, hit refresh, and there it is. Black bar, "Hello, world" right at the top. If you see that, you're fully connected and the setup is done. So, from here on out, the workflow is just open Co-work, tell it what to build, and hit refresh. No more copying code ever again. No more pasting into Shopify's editor. Cloud handles that code and pushes it for you. In future videos, I'm going to use this exact setup to build custom Shopify theme sections plus more. So, subscribe if you want to see that. I'm Cecil from

[00:06:00] Web XP. I build custom Shopify stores and apps. Link to everything is in the description. See you guys on the next video.
