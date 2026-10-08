# Build Shopify Themes in MINUTES -[Claude Code & MCP]

- URL: https://www.youtube.com/watch?v=0tEkfZ4vtcs
- Channel: WebSensePro
- Published: 2026-03-12
- Length: 11:35
- Views at fetch: 27417
- Fetched: 2026-10-03 with yt-dlp (creator captions), file 0tEkfZ4vtcs.en.vtt
- Coverage: FULL TRANSCRIPT from captions. NO FRAMES: video download was blocked in this session, so on-screen code, settings and commands were not seen. Auto captions can mishear technical terms.

## Chapters

- 0:00 Introduction
- 0:55 Step 1: Connect GitHub with VS Code
- 3:30 Step 2: Add Claude Code to VS Code
- 6:15 Step 3: Add MCP Server for Latest Context
- 8:50 Supercharge Your Setup
- 10:50 Outro

## Description

```
Build Shopify Themes with Claude Code

Are you tired of spending days or weeks building custom Shopify themes? In this video, I reveal my "Secret Dev Stack" that allows you to build, debug, and push Shopify code in minutes instead of hours.

We are combining the power of Claude Code (Anthropic's Agentic CLI), GitHub, and the Shopify Dev MCP (Model Context Protocol). This setup doesn't just write code; it understands the latest Shopify documentation, handles version control, and automates your entire workflow directly inside VS Code.

In this tutorial, you will learn:
✅ How to connect GitHub with VS Code for seamless version control.
✅ How to install and configure Claude Code (The AI agent that actually builds).
✅ The Game Changer: How to add the Shopify MCP Server so your AI assistant always has the most updated Shopify API context.
✅ A workflow to push changes from local to live Shopify stores in seconds.

🚀 Helpful Resources & Links:
👉 Shopify MCP Server: https://shopify.dev/docs/apps/build/devmcp
👉 My Free Shopify Sections Playlist: https://www.youtube.com/playlist?list=PLvT_6E7D1NZLJrwL9-msuz1APKdmJDv6C

Command For Github

git init
git add .
git commit -m "Initial commit"

Blog: https://websensepro.com/blog/build-shopify-themes-in-minutes-claude-code-mcp/

Video Timestamps:
00:00 - Introduction
00:55 - Step 1: Connect GitHub with VS Code
03:30 - Step 2: Add Claude Code to VS Code
06:15 - Step 3: Add MCP Server for Latest Context
08:50 - Supercharge Your Setup
10:50 - Outro

Other Suggested Playlists:

Shopify Tutorials Playlist: https://www.youtube.com/playlist?list=PLvT_6E7D1NZIlHa09cgswsjD9QunUpHKy

SEO Playlist: https://www.youtube.com/playlist?list=PLvT_6E7D1NZJ1SwwbXG4mgzzTWhymTl0B

Playlist for AI Tools and News: https://www.youtube.com/playlist?list=PLvT_6E7D1NZKuPOulUyl2sWdGQBHs-wt0

If you want help with Shopify Customization, store development, or any other web development help. Contact us via https://websensepro.com/contact-us

#shopifydevelopment  #github  #claude   #shopify
```

## Transcript

[00:00:00] Really important video for all of the Shopify team developers. In this video, I'll show you guys how you can connect cloud code and use GitHub to boost your Shopify team development. So if you were building a team in months or in days, you could do that in hours and minutes using the power of new cloud code. At the end of this video, I'm also going to show you guys how to supercharge this setup. So the first step of this video will be to connect GitHub with the VS code so you can get all of the version history. In the second step, we will add the cloud code in the VS code and in the third step, which is the most important one, we will add MCP server to get the latest context.

[00:00:38] If you are not familiar with these terms, watch the complete video. I'll give you a beginner's guide on how you can set up cloud code to speed up your Shopify team development. So without further ado, let's get into the screen. So guys, this is the first step where I'll be connecting this team with the GitHub, right? I've added the latest version of Horizon team. You can see that it's the latest version as of today. Now let's create a new repository in GitHub. So that's my GitHub screen. I'm going to click on this plus sign here and click on new repository. I'm going to name it Shopify plot tutorial for the sake of this tutorial and make this

[00:01:19] repository private and then scroll down and then click on create repository. Perfect. We have our repository created. Now we will download our team and add it to our folder and open that in VS code. So I have this folder created by the name of Shopify dash team. I'm going to add all of the files of this team, which I have in my development store. For that, I'm going to click on these three small dots and then click on download team file.

[00:01:52] Once I do that, you can see that it's sending me an email with the theme files. So I'm going to click on send email and go to my email and extract all of the files on this folder here. So guys, that's the email and I have already downloaded the theme and moved it to this Shopify theme folder. Now I will extract all of the folders and move it here. So I'm going to unzip and that is the folder. That is my theme folders, which I want to have it in the Shopify theme folder.

[00:02:28] So I'm going to move these folders here and remove the zip file and this folder. So I don't need these two anymore. I'm going to remove that. Now let's open this Shopify theme folder in my VS code. So I'm going to open the Visual Studio code, click on open and in my desktop, I have this Shopify theme folder. I have all of the files downloaded locally in my laptop.

[00:03:04] Now I need to connect the GitHub repository with this folder. And how can I do that? So first I need to initialize git for this folder. And for that we have already created the GitHub repository by the name of Shopify cloud tutorial and I'm going to simply add these three commands in the terminal of VS code. So just copy this, go back to the VS code, open up the terminal and paste this command. Now we are getting this error that's an expected error because we haven't yet initialized our

[00:03:41] git in the local folder. And in order to fix this bug, we will add this command here, git init, git add dot, git commit dash m initial commit. I'll add this command in the description. So don't need to worry about if you don't really understand what this command does. Let me know in the comments below if you want me to create a beginner level tutorial for GitHub, how to create a GitHub repository, how to fork a GitHub repository, how to actually contribute in open source. Let me know in the comments below if you want me to create that tutorial.

[00:04:13] For now, let's move on to this tutorial. And I'm going to hit enter and then go back to my GitHub repository. Copy this command again one more time, paste it to the terminal and hit enter. Now you can see that our code is being pushed. And now if we go back to our GitHub repository and hit refresh, you can see all of the code in our local folder has been uploaded to our GitHub repository, which we created, right? Now our local folder and our cloud GitHub repository is connected.

[00:04:51] Now whatever change we make, it will show up in the revision history in the form of comments and it will create a history of each comment which is created. Now this step is done. We will now connect our development store with this GitHub repo. And for doing that, you will go to your online store in Shopify store and click on this dropdown where it says import theme. And here you will find connect from GitHub. Click on connect from GitHub. I have already connected my GitHub account. You will see a connect button where it will take you to the GitHub login screen where

[00:05:25] you will need to connect your GitHub account. Once your GitHub account is connected, click on this repository option and we will select the repository which we have created right now. Click on that. And here it will show us the branch which we need to connect. So I'm simply going to click on this connect here. And our main branch of this GitHub repository is now connected with the theme which is being created here. Okay, you can see that it's now ready to be published. Now I'm going to hit publish and click on publish again.

[00:06:02] Now our theme is connected with this GitHub repository where if we change anything within the GitHub or our local folder, it will show up in the revision history. Let me show you how it's going to show. So first, let's try editing from the Shopify code editor. So I'm going to simply click on these three small dots and then click on edit code. Okay, let's find our base.css file. And I'm simply going to change. So let's from 99% to 99%.

[00:06:35] That's the basic change which I'm making in order to show you guys how it's going to look on GitHub repo. Click on save. And now if we go back to our GitHub repository and hit refresh, you can see that we have now Shopify bot added in Comet where it's telling us that we have made change from Shopify code editor. And if I click on Comet, you can see that it's giving us this is the Comet. If we click on that, it will give us the further details that what are the code changes which we made.

[00:07:10] So that's the code change which we made. It's going to show the same thing if we change anything locally. So if I go back to the local folder where we have our code and make any change, let's go to base.css file and make any basic change here. Again I'm going to change it to 101%, hit save. And now you can see that it's giving us this option to add a Comet, right? So I'm going to say test, change and hit Comet.

[00:07:48] Now you can see that I have these new Comets showing up in my GitHub repository. It's just a high level overview of what you can do with GitHub. If you want me to create a detailed tutorial, let me know in the comments below. I'm not going to go into more details of the GitHub. Now let's move on to the next step where we will be installing Claude and how we can do that. So simply go to GitHub, click on this extension icon here and search for Claude code. And you will find this extension on the top.

[00:08:20] Click on install button. So guys, once the Claude code extension is installed, you will have it showing up here on your VS code. Once you click on that, you can chat with Claude code. Initially what you will see is this screen. Once you install that for the first time, I've already installed and connected my Claude AI with the Anthropic Console. You can use Claude AI subscription or you can use Anthropic Console. Now the difference between these two is that Anthropic Console is only going to charge you for API usage, meaning whatever number of token you will consume, it will charge

[00:08:57] you based on that. For Claude AI subscription, there's a fixed charges of $70 or $100 if we go to Claude AI subscription. Here you can see we have these three tiers which we can use. So there's a free version where we have limited amount of contacts and the prompt and there's the pro version and this is the max version. So if you want to go with the fixed pricing, you will select the Claude AI subscription and it will take you to the browser and connect via your subscription. And if you want to do that via Anthropic Console, which I have done, you will click on Anthropic Console.

[00:09:31] Once it's connected, it is going to read all of the code which you have on your project here and it will be able to suggest the code changes automatically and it will also make the changes automatically. You won't have to do manually anything. Now the most powerful thing to do is to add an MCP server which Shopify has already provided. So if we go to that documentation, Shopify MCP Claude code, you will find this link on the top. And here, if we scroll down, you can see that we have all of these options to add MCP server.

[00:10:08] Now let's add Claude code MCP server in our VS code via this command. So I'm going to go back to my VS code, open up the terminal, and I'm going to add the this command. So simply copy this command and paste this command. And once you do that, you will have it showing up on your Claude code chat here. So if I press slash and type in MCP, you can see that we have this MCP status and manage MCP servers.

[00:10:42] You can now see that we have Shopify dev MCP connected. Now what does this MCP mean? MCP meaning model context protocol, meaning if Shopify development API documentation got updated, few days back, few hours back, it is going to pull latest and updated documentation in the context of Claude code and it will be able to assist us better in writing code as updated as per the Shopify documentation so you don't have to give it fresh context again and again to your AI assistant because developer documentation keep updating very

[00:11:18] frequently especially in case of Shopify. So Shopify dev MCP is really important to have with your Claude code in order to streamline in order to boost your Shopify theme development. And that's it for this video guys. Let me know in the comments below if you want to watch more videos with Claude code. Until next video, have a great day.
