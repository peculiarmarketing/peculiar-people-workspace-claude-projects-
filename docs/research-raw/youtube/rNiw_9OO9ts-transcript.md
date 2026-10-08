# How to Build Shopify Themes Faster with Claude Code

- URL: https://www.youtube.com/watch?v=rNiw_9OO9ts
- Channel: Will Misback
- Published: 2026-01-03
- Length: 11:15
- Views at fetch: 43537
- Fetched: 2026-10-03 with yt-dlp (YouTube auto-generated captions), file rNiw_9OO9ts.en.vtt
- Coverage: FULL TRANSCRIPT from captions. NO FRAMES: video download was blocked in this session, so on-screen code, settings and commands were not seen. Auto captions can mishear technical terms.

## Chapters

- 0:00 Introduction to AI coding
- 1:02 Connecting GitHub to Shopify
- 1:55 Shopify CLI setup
- 4:19 Initializing Git repository
- 6:00 Syncing GitHub and Shopify
- 7:23 Setting up the editor
- 8:38 Configuring AI and concluding

## Description

```
In this video, I walk through how to use Claude Code to develop and edit Shopify themes, introducing an AI-driven development workflow that significantly improves productivity.

I show how to connect your Shopify theme to GitHub, set up Shopify CLI, preview themes locally, and integrate Claude Code inside Visual Studio Code so you can make changes faster while maintaining version control and free theme backups.

This workflow allows you to safely build, test, and iterate on Shopify themes locally, sync changes with GitHub, and leverage AI tools like Claude Code.

Get my CLAUDE.md shopify development template: https://willmisback.com/blog/claude-code-for-shopify-10-mistakes-that-will-break-your-store

Top 10 Mistakes with Claude Code: https://www.youtube.com/watch?v=uW39GOgc0wo

Run the free Shopify Product Catalog Health Audit here: https://ecomseocheck.com/

For business inquiries: me@willmisback.com

Connect with me on LinkedIn:
https://www.linkedin.com/in/will-misback/
```

## Transcript

[00:00:00] Hey guys. So today I wanted to record a video about how you can start to use cloud code to code your Shopify site. So this is going to introduce AIdriven development into your workflow which will boost your productivity massively when you are making edits to your Shopify theme. So the first thing that you guys want to do is if you don't already have a GitHub account set up, you want to navigate yourself to github.com and click this sign up for GitHub button here. follow their onboarding steps and then you're going to need to create an SSH key to be able

[00:00:33] to push to GitHub and whatnot. GitHub at a high level essentially tracks version history on your codebase. So it makes it so you if you make an error, you can easily go back and also it keeps a remote copy of your theme. That way if your theme for whatever reason on your machine gets deleted, you can always pull it down from GitHub. It's free and it's one of the first things that I do when I start working with clients is I download their theme, upload it to GitHub and we connect it through that way. Okay. So, the next thing I want you guys to do is you're going to go to your

[00:01:06] online stores admin and from your admin, come here to online store themes. From there, go up to this right hand corner here, import theme, connect from GitHub. this. If you don't already have your GitHub account connected, should display a prompt to install Shopify's connector for GitHub, you guys want to go ahead and do that. Make sure inside that app you have all repositories set up. That's going to make it a lot easier for the purposes of this tutorial to follow along. Okay, so you can see here that

[00:01:37] now I've downloaded and unzipped these theme files. And in the next step of this tutorial, we're going to make sure that you guys have the Shopify CLI downloaded and implemented on your machine so that you can make the necessary connection between this these theme files and Shopify. Okay. So, I want you guys to navigate to shopify.dev/doccks/shopify cli. This is going to walk you through implementing Shopify CLI. Highle overview here is we can use npm if you

[00:02:11] already have that installed. If you don't, just find a tutorial for how to install npm. There should be a bunch on YouTube or somewhere else online. Enter that command in your terminal. Let me go ahead and blow up my terminal a little bit for you guys. And it will install Shopify CLI. You can make sure that Shopify CLI is implemented properly by typing Shopify help or and you should get these types of outputs showing up or you can type uh Shopify excuse me Shopify version here and it

[00:02:46] will give you the version number that Shopify is currently on. Okay. From here, let's make sure that the connector is working completely by going into whatever directory uh our theme files are in. So, I'm going to go into that directory. And now you should see that we we're actually in this directory now. And what I want to do to preview this theme is I type Shopify theme d-store. Yeah, let me let me full screen this

[00:03:19] really quickly. you guys. Shopify theme dev- storere and then I want to enter my Shopify my Shopify title URL here. So what I want to do is you want this after the admin.shopify.com/store. There should be this URL slug here. You want to copy that, paste that in here and type domyshopify.com after that.

[00:03:52] What that will do is it will spin up a local preview of this Shopify theme. So you can see that right now it's building it. And if we hit T here, it will take us to a local copy, a local hosted copy of the Shopify theme where we can preview our changes live. And you can see that it's uploading everything here. So I'm going to quit out of that now. And the next thing that we want to do is integrate this theme with GitHub. So I'm going to type get init here. That's

[00:04:26] going to initialize an empty repository. I'm going to get add star to add everything. Get commit and type initial commit here or initial. And from there now we need to actually go into GitHub and create this repository. So once inside GitHub there should be in the lefthand corner there should be a button that prompts you to create a new repository. Uh I'm going to take you know test Shopify theme here or something. Whatever repository uh you name you want just type that

[00:05:00] here. Your visibility you want to set to private unless you want other people to be able to see this theme or the edits that you make to this theme. Hit create repository here. Now it is going to walk you through either using HTTPS or SSH to set up this git repository. If you haven't set up an SSH key, you can use you can use HTTPS here, but SSH is preferred. We have an existing repository here. So we're going to push that from the command line. So we just want to add we just want to copy paste

[00:05:34] all of these commands here from our terminal and hit enter and let's make sure that that goes through. So it's pushing our single commit up to the main branch here and you can see that it has integrated these changes. It's pushed them onto our GitHub repository. And from there, we want to connect this GitHub repository to our Shopify store. For that, we're going to hit import theme here. Connect from GitHub. And for the repository, we want

[00:06:07] to type that same uh uh URL slug here. So, mine was test Shopify theme. I'm going to go ahead hit that. Hit the main branch or whatever branch you push the changes to. And from there, hit connect. and it will upload the theme. Once you're satisfied with the changes and whatnot, you can obviously publish this. The amazing thing about having this GitHub connection is now we can use our own tools on our local machine like

[00:06:40] Cloud Code or Cursor or Visual Studio Code or whatever code editor you prefer to make changes to our Shopify theme and it will automatically sync to Shopify and changes that we make through Shopify through the customizer or the code editor here we can pull them down into our local copy of our theme so that they're always synchronized. The other nice thing, again, this provides you with free theme backups as well as version history. So, if you end up making some massive change to your store

[00:07:14] that ends up breaking your theme and you need to roll back or revert, it's as simple as a 5-minute process of going back to a previous commit. Okay. From here, what I want you guys to do is go ahead and go download Visual Studio Code if you don't already have that downloaded because we are going to use that as a sample code editor. There's a lot of different code editors that you could end up using with Cloud Code, but for the purposes of this tutorial, we're going to be using Visual Studio Code. So, just navigate to

[00:07:46] code.visisualstudio.com and go ahead hit whatever button crops up here. It's going to be specific to your machine architecture and whatnot. Walk through downloading it. And once you have that, uh, go ahead and open that up. From here, we want to open up the specific repository of the theme that we downloaded before. So, for me, that's going to be here. You can just find that in file, open, and then navigate on your machine to actually find that repository. What I want you

[00:08:19] guys to go ahead and do afterwards is go down to your settings extensions here and type in claude here. That is going to open up this uh claude code for VS Code extension here. You guys want to go ahead and install that. You can see that I already have that installed. Okay. Okay. So, once you have the Cloud Code extension installed, what you want to do is you want to hit this uh little orange icon, that will bring up the Cloud Code chat interface. And what you'll notice right now is if I go

[00:08:54] ahead and, you know, type anything uh and hit enter here, it's going to let me know that my credit balance is too low because we actually have not logged into our account yet. So you want to type /lo here and it will prompt you basically to log in one of a few different ways. And so the highle overview of these different ways is either you can use your claude.ai subscription which is going to actually be like a monthly charge. It's sort of a

[00:09:26] flat fee for using uh cloud code. Or you can use the anthropic console which is going to allow you to pay on a per credit sort of usage basis for the API or whatnot. And then finally you can use third party providers for API keys and do it that way. Choose one of these and sign up. And then from there, now when you go ahead and open this, you can go ahead and begin to start making edits and ask questions about your theme and

[00:10:00] things like that through Claude Code. Okay guys, so that is how you guys can start to use Claude Code to code your Shopify site. I also have a video on how you can use Cursor as well. Either of these tools are great to start to build in AIdriven development into your theme development for your Shopify store. I would say that, you know, if you are using these tools properly, they can easily 10x the output that you get as far as building new features for themes and whatnot. The one thing obviously to

[00:10:32] be careful with with using these tools is you don't want to have them 100% replace your critical thinking and your ability to understand how the code works behind the scenes because AI at this iteration still makes tons of mistakes and it makes mistakes in weird ways that you wouldn't necessarily expect. So being able to debug it is still a super super critical skill to possess. But let me know if you're having trouble with anything in this video in the comment

[00:11:04] section below and I will help you as soon as I can. If you got some use out of this video, you know, leave a like. It helps other people find it. and I'll see you in the next video,
