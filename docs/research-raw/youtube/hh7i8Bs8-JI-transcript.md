# How to Edit Shopify Theme Using Claude Code [Full Tutorial]

- URL: https://www.youtube.com/watch?v=hh7i8Bs8-JI
- Channel: CheckoutClass | Shopify Tutorials
- Published: 2026-06-03
- Length: 12:14
- Views at fetch: 1266
- Fetched: 2026-10-03 with yt-dlp (YouTube auto-generated captions), file hh7i8Bs8-JI.en.vtt
- Coverage: FULL TRANSCRIPT from captions. NO FRAMES: video download was blocked in this session, so on-screen code, settings and commands were not seen. Auto captions can mishear technical terms.

## Chapters


## Description

```
Learn how to edit your Shopify theme using Claude Code and Visual Studio Code, no coding experience required!

In this tutorial, Somath walks you through the entire process of connecting your Shopify theme to Claude Code so you can make AI-powered theme changes without ever touching the Shopify admin editor.

What you'll learn:

How to download your Shopify theme and set up a local folder
How to create a private GitHub repository and push your theme files
How to connect GitHub to your Shopify store for automatic syncing
How to install the Claude Code extension in Visual Studio Code
How to use Claude Code to make theme changes, create new sections, and improve page speed
How to push updates from Claude Code back to GitHub and Shopify
Tools you'll need:

GitHub account (free) → github.com
Visual Studio Code (free) → code.visualstudio.com
Claude account + API key → claude.ai
Your Shopify theme ZIP file
Pro tip: Always work on a copy of your live theme, never edit the live theme directly when using AI tools like Claude Code.

⚠️ Claude Code is powerful but not perfect. Use it for small changes, new sections, and minor edits. Avoid letting it rewrite complex existing code setups.

📌 Resources mentioned:

GitHub: https://github.com
Visual Studio Code: https://code.visualstudio.com
Claude: https://claude.ai
If you have questions or get stuck, drop a comment below, happy to help!

👍 Like & Subscribe for more Shopify tips
```

## Transcript

[00:00:00] Hey, so in my In this quick video, I'm going to show you how to connect your Shopify theme to CloudCode and make changes to your theme using CloudCode. You're going to need a few things for this to work. The first thing is you're going to need a GitHub account. You can go sign up to GitHub by going going to github.com. And the second thing you're going to need is you're going to need Visual Studio Code. I'm going to drop a link to all these in video description below. So, you're going to need this. And the reason we're going to use this is because it's free.

[00:00:32] And on top of that, it has a CloudCode extension that we can use. I prefer doing this over actually using the CloudCode app because it's just easier to work with code with Visual Studio Code. It doesn't matter if you don't know how to code. It's like this is quite intuitive, so you can use it. So, the second thing is you're going to need this. And then third third thing is you're going to need a Cloud Cloud account. You just You just need to You need a API key to connect CloudCode to Visual Studio Code. Let's say for a start. But, this might take a few

[00:01:05] minutes. So, let's get started. The first thing you want to do is you want to go to your online store and you want to download your theme. So, let's For me, I'm on a demo store. And if I want to make changes to this theme and my main theme using CloudCode, all I have to do is come in here and click download theme file. And it's going to send me an email. And go to I already have the theme downloaded. So, I'm not going to go to my email. But, you know, for you, once you download you need to go to your email and download the zip file. And once you have the zip file,

[00:01:39] go create a new folder anywhere on your on your PC or Mac. Create a new folder and name it anything you want. It doesn't matter. Let me name it I'm just going to name it Cloud Theme. And then, what you have to do is you need to ex- So, this is my theme file I downloaded from a email. Uh so, what you need to do is you need to extract the zip file into the new folder you just created. For me, that would be

[00:02:11] theme. Oh, right. Second, and there you go. So, there's bunch of This is your actual theme folders, and you can If you can click the things, then you can see actually like good files and stuff. And we're good here. And the next step would be you need to open up your terminal. Actually, you need to open your Visual Studio Code. If you haven't downloaded, please go ahead and download it. You need to open your Visual Studio Code and click on file and click open folder, and you need to open the theme you just

[00:02:46] extracted. So, for me, it's Klaus theme. I'm going to select the folder. And yes, I trust the authors. Perfect. And then, the next step is you need to open a terminal. Well, to do that, just click on the search bar below and click terminal. Wrong there. My bad. Sorry. So, click on the three dots and click terminal, new terminal. Right. And it will open up this terminal. If you're not If you are not familiar with coding, don't worry. I'm going to walk you through everything up to there. All

[00:03:18] right. Once you have this open, you need to go to your GitHub account. I know I'm jumping around with this. It's complicated like There's a lot of things involved. I'm sorry about that. So, you need to go to your GitHub account. And once you sign up, you're going to see something like this. Uh or if you don't have any GitHub repo, the screen might look a bit different, but all you have to do is like you need to create a new repository. So, just hit new, and you will be taken to this screen. And you need to enter your repo name.

[00:03:50] Again, this doesn't matter. The name can be anything. I'm just going to name it Claus team. And just make sure the visibility is private. If you make it public, anybody on GitHub can view it. So, just make sure it's private and no one can see it. And click create repo. And once you do that, you're going to end up on this screen. And now you need to copy a copy this code, the whole thing. I'll go back to your Visual Studio Code and paste it. It's going to say, "Are you sure you want to paste the following lines into the terminal?" Say

[00:04:21] yes. If you don't get an option, and make sure to hit enter after you solve this lines. And then after that, you're going to you're going to want to type in exactly what I type in. So, you're going to get add dot. And it's going to add literally all the files. Did and with comment. All right, make sure to type in like this. The The messaging side the I don't know what it calls it, but it

[00:04:52] doesn't matter, but still. The current with the anger fish. fish origin All right. this So, this is done. So, this Now, if you go go back to your GitHub and refresh your Claus team, you should see the team files here. So, beautiful. So, and the next step is Now, you need to connect your GitHub to your

[00:05:24] Shopify. So, anytime you make make changes to your team using Claus code, they get reflected in your Shopify. So, we're not going to So, one more thing I do want to mention, when you work with Claus code, Claus code is an LM and there's a very good chance that it's going to it's going to mess up things, you know? There There will be small things it will mess up here and there. So, always So, the reason we're doing it this way is because, you know, we just need to be safe. Now, we are we create a copy of the theme of the live theme, so the live

[00:05:57] theme doesn't get affected. So, yeah. So, what you need to do is you need to come back to your Shopify store, click import, and click and click on connect from GitHub. All right? If you have never connected your GitHub to your Shopify store, then you're going to get you're going to see option here saying like sign in with GitHub. So, just sign in with your GitHub and log in to your GitHub account, and you're going to end up on a screen like this. And in here, you're going to want to select the repo you just created for the theme. For me, it's Cloud Theme. Click connect. And what this will do is basically

[00:06:30] import your theme from GitHub to Shopify. And now, anytime you make changes on on your on Visual Studio Code using Cloud Code, the theme changes will reflect on your Shopify theme. So, you know, you never have to really log in to your Shopify theme, or you never have to log in to Shopify to see or make changes anymore. So, it's pretty cool. It takes a minute to set the whole thing up, but once you get it working, it's like really beautiful.

[00:07:02] And then it might take a minute for it to get uploaded and everything. During this time, I'm going to just move ahead to the next step. Don't close the screen and or anything. So, go back to Visual Studio Code, and you're going to want to go in to this icon, extensions. You're going to come in here, and you're going to search for Cloud Code. It'll probably take a second, but click on the first extension you see and install it. I already have it installed, so I'm not going to install it. Install it, and it's going to uh walk you

[00:07:34] through like how to connect Cloud Code to Visual Studio Code. It's very straightforward. All you need is a Cloud Cloud Cloud account and like the API key. So, just Well, just let let them walk you through the whole thing. And once you have done that, click on any file in your theme and click the cloud icon. Right? And now this is where how you So, if anytime you want to make changes to your theme, all you have to do is like click on a file and click on cloud and you can ask it to do anything, right? It has access to the entire

[00:08:08] project. So, it doesn't have to be like working file. I I can tell it to do something like I don't know. Can you scan my theme files? Tell me three things to improve page speed. You can it will also do the thing for you. You know, I'm just asking right now because video and I want to keep it short. But yeah, this guy is going to it's going to scan

[00:08:40] through everything without and it's going to make the changes and it's going to ask you like, you know, it's going to tell you like there's something wrong with the code. You can also create new sections. Pretty much anything you would hire a developer to do, you can ask Cloud Code to do. But please be careful because Cloud Code is not perfect. It makes mistakes all the time. So, only use it for like small things and minor things or if it's like a completely new section you're trying to create. Those things are fine. But if you already have some complicated

[00:09:12] business like section setup or like a code setup, don't don't try to mess it with mess with it too much. With Cloud, I mean, it's pretty good for the most part, but sometimes, you know. Yeah, it says it's going to ask you for like, you know, like permissions and stuff. So, another thing you could do is you can click on edit automatically. So, that way you don't have to click yes all the time. But sometimes I still have skip word permissions. But, yeah, you get the idea, right? Like, it's going to go through everything

[00:09:43] and take off the code part. But, anyway, I do want to mention one more thing. Like, I'm not going to do the cloud code part. That's the easy part. Everything else is the harder part here. But, I do want to mention one thing. For example, like, I'm going to make this watch and share the comments. Because, whenever you make an update to the theme, right? Either by yourself or with cloud code, the one step you need to make sure that you do is you need to update your GitHub as well. And the way to update your

[00:10:15] GitHub is basically the first thing is going to you're going to do is you're going to type in git add dot. You're going to be able to do is you're going to say I changed on And then, the the whatever you put in the double code doesn't matter. Just like I'm going to know what actually been what changed, you know? And the third comment third command is git push origin. This will push the entire theme.

[00:10:48] I failed to push on the branch. Oh. Okay, so my bad. This because this one is not connected to the one I just added. So, this is a different one. But, usually, the third command will go through and it will work. I made some changes to the theme before the video. So, anyway. But, if you don't want to do this, you could definitely just ask Cloud to say, "Hey, can you can you push this theme to GitHub?" And say, "I used the branch

[00:11:23] So, type in exactly this thing what whenever you're done making edits to your theme. And it will push the entire theme to GitHub. And you could also tell her to install uh Shopify CLI. I'm going to put all this information in the video description below so you have better understanding. I'm going to tell you can also ask her to install Shopify CLI so you can actually see what the theme actually looks like in your local local machine so that you don't actually have to actually push the updates to Shopify to see what the theme actually looks like live. So, yeah.

[00:11:56] Those are the things I wanted to mention. But, yeah. So, that's pretty much it for the video. I hope you guys enjoyed it. If you guys have any questions and uh if you're stuck somewhere, please leave a comment below and I'll be happy to help you out. Thank you so much for watching.
