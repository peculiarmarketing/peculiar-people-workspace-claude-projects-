# Claude Code + Shopify AI Toolkit: Zero to Hero Tutorial | Maelify

- URL: https://www.youtube.com/watch?v=j58kLqMPPZE
- Channel: Maelify
- Published: 2026-04-14
- Length: 8:18
- Views at fetch: 821
- Fetched: 2026-10-03 with yt-dlp (creator captions), file j58kLqMPPZE.en.vtt
- Coverage: FULL TRANSCRIPT from captions. NO FRAMES: video download was blocked in this session, so on-screen code, settings and commands were not seen. Auto captions can mishear technical terms.

## Chapters

- 0:00 What this toolkit can do
- 0:35 What we cover in this tutorial
- 0:55 The one dangerous skill nobody talks about
- 1:00 TUTORIAL STARTS HERE
- 1:02 Step 1: Install the Shopify AI Toolkit plugin
- 1:53 Step 2: Auth (Shopify login flow)
- 2:32 Step 3: Confirm access (list themes)
- 3:00 Dev theme vs production (no undo!)
- 3:10 Pause, install on your machine, subscribe
- 3:35 Step 4: Build a real section with one prompt
- 4:50 Step 5: Ship a blog post with AI-generated image
- 5:55 Step 6: Embed a downloadable CLAUDE.md file
- 6:42 THE DANGEROUS PART: store execute explained
- 7:13 Three rules to protect your store
- 7:41 Tonight: your first prompt
- 7:55 What you should build (comment below)

## Description

```
One sentence into Claude Code. 90 seconds later: a new section on my Shopify store, a published blog post, and a downloadable CLAUDE.md. No API keys. No code. No Liquid.

This is the Shopify AI Toolkit. This is how you install it. Zero to hero.

I walk you through every command from a cold start. Install. Auth. Connect. Three live prompts that change my real store. And then the one skill nobody is talking about yet, because pointing it at the wrong shop will erase your Saturday.

Full blog post with downloadable CLAUDE.md: https://www.maelify.com/blogs/news/claude-code-shopify-zero-to-hero

PREREQUISITES:
Claude Code CLI installed
https://code.claude.com/docs/en/quickstart

INSTALL COMMAND (paste into Claude Code):
Install https://github.com/Shopify/Shopify-AI-Toolkit plugins

TIMESTAMPS:
0:00 What this toolkit can do
0:35 What we cover in this tutorial
0:55 The one dangerous skill nobody talks about
1:00 TUTORIAL STARTS HERE
1:02 Step 1: Install the Shopify AI Toolkit plugin
1:53 Step 2: Auth (Shopify login flow)
2:32 Step 3: Confirm access (list themes)
3:00 Dev theme vs production (no undo!)
3:10 Pause, install on your machine, subscribe
3:35 Step 4: Build a real section with one prompt
4:50 Step 5: Ship a blog post with AI-generated image
5:55 Step 6: Embed a downloadable CLAUDE.md file
6:42 THE DANGEROUS PART: store execute explained
7:13 Three rules to protect your store
7:41 Tonight: your first prompt
7:55 What you should build (comment below)

WHAT YOU GET:
- Full Shopify AI Toolkit installation walkthrough
- Three real prompts that modify a live store
- Blog post auto-published with AI-generated featured image
- CLAUDE.md file embedded as downloadable resource
- Store execute safety rules (no undo, dev store always)

DOWNLOAD MY CLAUDE.md FOR SHOPIFY:
https://www.maelify.com/blogs/news/claude-code-shopify-zero-to-hero

Toolkit:
https://shopify.dev/docs/apps/build/ai-toolkit
https://github.com/Shopify/Shopify-AI-Toolkit

---
Maelify | Senior Shopify Plus Migrations Architect
Enterprise e-commerce infrastructure, AI-powered Shopify development
maelify.com

#ShopifyAIToolkit #ClaudeCode #Shopify #ShopifyPlus #ShopifyDeveloper #AIToolkit #ShopifyTutorial #ZeroToHero
```

## Transcript

[00:00:00] Guys, I didn't even paste a single API key. Saturday afternoon, coffee, terminal, one sentence into Cloud Code, and 90 seconds later, there is a brand new section on my Shopify store. So, this is what the new Shopify AI toolkit is all about. I published blog post on my domain and given a cloud.md for you to download with the prompts that we used for this video. So, go check it out after the video. I didn't write a single line of code. I didn't even need to touch my liquid. And this is what the Shopify AI toolkit allows you to do. It's going to

[00:00:32] this tutorial from zero to hero. I'm going to walk you through every command from a cold start, okay? Install, auth, connect, three light prompts that change my real store. And then, the one skill inside this toolkit that nobody on YouTube is talking about yet, because pointing it at the wrong shop will erase your Saturday. But, we'll get to that one last. Toolkit Shopify dropped on April, and it's free, it's open source, and it's out of dating. dating, so that's great. Cold start. Open a fresh folder on your machine, and then open a

[00:01:05] terminal inside it. And you type cloud. And then, the Cloud Code prompt blinks at you. Now, paste the install command I'm leaving you in the description of this video. It's just one line. It tells Cloud Code to fetch the Shopify AI toolkit from GitHub and install every plugin it ships with it. And inside, you'll have uh the dev MCP, the admin graph QL, the liquid validator, uh the theme check, the store execute, 16 skills in total. One install command. And then, Cloud asks for a couple of

[00:01:40] permissions on the way through. Read them. Hit allow. Let it process. When the terminal says that it's enabled or it's finished, well, then we are done with this step. Okay, authorization. In a second terminal, just a fresh pane here. Before we log in, we log out. Type Shopify off log out. I do this every recording because I want the off flow on camera to real, not a cached session. And it's also the one command nobody on

[00:02:12] the official tutorials is going to tell you run. Then we go for Shopify off log in. The browser opens. The device code in your terminal has to match the device code in the browser. If they match, you confirm. If they do not match, you close the browser and figure out why. Okay, so now it shows successfully logged in. So now we move on. And we're back in Cloud Code. And the first prompt we're going to be using here is to list all the available themes in my store. This is not a flex. It's

[00:02:45] actually a sanity check. If Cloud Code can read my themes, Cloud has full access to the shop. Two themes in my case. My main theme wire to get hops through Shopify's native theme and a dev theme I use for experiments. Everything we're about to do touches the dev theme first, never the main one. And remember this line, there's no undo on production. Quick thing here though, if this is already working for you, please please pause the video right here, run those two commands on your machine, and come back when you see the word enabled.

[00:03:17] And on the way back, please hit subscribe. Not because I'm asking, but because right now I am one of maybe three people on YouTube making real terminal content for Shopify Plus. And the algorithm is the only thing deciding whether that stays true or not. So your click is a vote. All right, back. Okay. So now we are going to actually change something in the store. The prompt I sent to Cloud on my dev theme the new section called latest videos. Show a thumbnail, link it to my most recent YouTube video. Use the scheme number five because

[00:03:51] that's how my theme's already set up, you know, with the colors and the background. One sentence, watch what Claude does with it. It opens the liquid files on my dev theme and reads how my sections are already structured, schema by schema, the way a senior dev would crack open a code base on day one. That move alone is a part most people do not know Claude can pull off. Then the thumbnail goes up straight into my Shopify CDN through the admin API. No GitHub, not a local

[00:04:23] folder. And now Claude writes the section liquid, the schema, the settings, the presets, the whole thing in one pass. Then it edits the templates/index.json, so the actual section registers on the homepage and renders. Now we have a preview here. There it is. No ID, no copy paste, no merge conflict. Everyone selling Coca-Cola and I sell fridges. And right now now I'm going to

[00:04:55] flex a bit. I tell Claude write a blog post about what we just did. Generate a featured image through the image generation skill that I already have set up on my on my Claude. Publish it on my store. Tie it to the YouTube video title that we're going to be using here, which is Claude code plus Shopify zero to hero tutorial. And this is the moment the toolkit stops feeling like a developer tool and starts feeling like a content team. Claude starts with the image. It saves it locally and then it uploads

[00:05:27] the file. It waits a bit for the CDN URL to come back. Meanwhile, it's creating the article, then calls article create with a body it wrote itself, my voice, and drops the image as the featured image, and publishes the article. Then we go to mylify.com/blog/news. And that was what? 15 seconds of my time? $400 of agency invoice that nobody is going to send. And then I thought hit me recording, which is the kind of thought you learn to trust when you have

[00:06:00] lived inside Cloud Code long enough. What if people watching this could download the exact cloud.md I use for Shopify work from inside the blog post with a button. So, we go. One sentence to Cloud. Embed a file cloud.md inside the article. Dark mode, code be aware, big download button, place it above the takeaway. 19 seconds later, done. Cloud wrote a file, uploaded it as a generic file to

[00:06:34] my Shopify stores, and then it built the HTML block. One click. And link is in the description, so you can go there and take it from from my website. So, now the part I promised you at the start. The skill this toolkit nobody on YouTube is talking about yet is called store execute. It is the one that writes to your shop. Every other skill in the bundle is read-only. Every demo you just watched run on store execute under the hood. It is also the one thing that is going to ruin somebody's Saturday this month because there is no undo. You run the prompt,

[00:07:06] the mutation fires, and whatever was there is gone. I have actually asked Shopify twice about a dry run mode, but nothing yet. So, three rules. And write them down. Use a dev store always. Save every prompt you run as a reusable file inside .cloud/skills because you're going to want to run it again, and you're not going to remember what you typed. And then reread your prompts before you even hit enter. Just the same way you would read a git commit before you push. Just remember that 3 seconds of reading is better than 3

[00:07:38] hours of cleaning up. Tonight, open a fresh folder, install your dev toolkit, off your dev store, send cloud one prompt, any prompt, then open your admin and watch what changed. Well, that feeling, my friends, is your job changing under you. So, now tell me in the comments what you built, what you did, and not just that you installed it. And if you like this kind of content, please like the video, subscribe, and share it with somebody that would find this information useful. Thank you for watching and see you in the next one. Bye.
