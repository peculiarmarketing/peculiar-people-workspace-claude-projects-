# Claude Code for Shopify: 10 Mistakes That Will Break Your Store

- URL: https://www.youtube.com/watch?v=uW39GOgc0wo
- Channel: Will Misback
- Published: 2026-04-15
- Length: 8:00
- Views at fetch: 2048
- Fetched: 2026-10-03 with yt-dlp (YouTube auto-generated captions), file uW39GOgc0wo.en.vtt
- Coverage: FULL TRANSCRIPT from captions. NO FRAMES: video download was blocked in this session, so on-screen code, settings and commands were not seen. Auto captions can mishear technical terms.

## Chapters

- 0:00 Intro
- 0:15 1 Editing core template files
- 0:51 2 No version control
- 1:25 3 Giving Claude all API scopes
- 2:14 4 Trusting Liquid syntax blindly
- 2:53 5 Vague prompts
- 3:33 6 Inline styles
- 4:06 7 Not using git branches for experiments
- 4:58 8 Not reviewing schema settings
- 5:45 9 Saying "improve this"
- 6:41 10 Not using a CLAUDE.md file
- 7:41 Hooking up Claude Code for Shopify Development

## Description

```
I've been using Claude Code on live Shopify stores for months. Here are 10 mistakes I made that broke things, and how to avoid them.

Whether you're using Claude Code for theme development, app building, or store automation, these tips will save you hours of debugging and protect your client's stores.

Download my Shopify CLAUDE.md starter template: https://willmisback.com/blog/claude-code-for-shopify-10-mistakes-that-will-break-your-store

Related videos:
- How to Build Shopify Themes Faster with Claude Code: https://www.youtube.com/watch?v=rNiw_9OO9ts
- I Gave Claude Full Control of My Shopify Store: https://www.youtube.com/watch?v=SOY9ekUOn64
- Code Your Shopify Site With Cursor AI: https://www.youtube.com/watch?v=88YuNy42Vmc

Timestamps:
0:00 Intro
0:15 #1 Editing core template files
0:51 #2 No version control
1:25 #3 Giving Claude all API scopes
2:14 #4 Trusting Liquid syntax blindly
2:53 #5 Vague prompts
3:33 #6 Inline styles
4:06 #7 Not using git branches for experiments
4:58 #8 Not reviewing schema settings
5:45 #9 Saying "improve this"
6:41 #10 Not using a CLAUDE.md file
7:41 Hooking up Claude Code for Shopify Development

Custom Builds / Consulting:
me@willmisback.com
https://www.linkedin.com/in/will-misback/

#ClaudeCode #Shopify #ShopifyDev #AICoding #ShopifyThemes #WebDevelopment
```

## Transcript

[00:00:00] I've been using Claude Code on Shopify stores for months. Client stores, my own stores, everything. And while it has helped me 10x my productivity, it's also broken a lot of things in the process. So, here's 10 mistakes that I made using Claude Code on Shopify so you don't have to make them for yourself. The first time I pointed Claude Code at a Shopify theme, I said, "Add a promotional banner to the homepage." And Claude went straight into the theme.liquid and rewrote the entire layout file. The theme.liquid file controls every single page on your store. So, if Claude makes a mistake here, your entire site breaks, not just one section. Now, I always tell

[00:00:33] Claude up front, "Do not edit theme.liquid and do not touch the layout files. Don't touch the base templates, either. Create a new section file or a new snippet instead." You want to throw this rule in your Claude.md file so you never have to repeat it. And later in the video, I'm going to tell you what else you should be putting in your Claude.md file. Mistake number two, no version control. So, Claude makes big, sweeping changes across multiple files. And if you're editing this theme directly in a code editor with no Git repo, one bad prompt and you've got no way to undo it. I always have my theme

[00:01:05] connected to GitHub. Before I let Claude make any major change, I commit what I have. In that way, if Claude goes sideways, I run git checkout dot and I'm back exactly where I started. If you don't have your Shopify theme connected to GitHub yet, I have a full [snorts] walk-through with a link in the description to that. It takes 10 minutes to set up and it'll save you hours of pain. Okay, mistake number three, giving Claude all API scopes. So, when you connect Claude to your H Shopify admin through MCP, which allows it to create products, manage collections, edit your

[00:01:38] theme, all from your terminal, you have to choose which API scopes to enable. I see people enabling everything, every single scope. That means [snorts] Claude can delete products, modify checkout settings, access customer payment data, things it should never, ever be touching. Only enable the scopes you actually need for the task at hand. For theme development, you really need just read themes and write themes. For product management, read products and write products. So on and so forth. That's it. I covered this in detail in my video on giving Claude full control of a Shopify store. So, check that one

[00:02:10] out. I'll leave another link to that one as well in the description. Mistake number four, trusting Claude's liquid blindly. So, Claude writes liquid that looks correct and it uses the right object names, the right filters, the right structure, but sometimes it uses deprecated syntax or it references properties that don't actually exist on the objects you're working with. So, the fix here is simple. You should run Shopify theme check after Claude Code changes before you push them. Theme check will catch deprecated filters, missing translations, invalid schema,

[00:02:43] all the stuff that looks fine visually, but will cause problems down the line. The other thing is you want to hook up the Claude Code MCP with Shopify. I'll cover that in a future video. So, mistake number five here, vague prompts. This one applies to all AI coding, not just Shopify, but it's especially bad with Shopify because the theme architecture is so specific. If you see this example here, the bad prompt gives Claude zero constraints. It'll generate something that technically works, but doesn't really match your theme, uses random class names, and probably will add inline styles. And the good prompt

[00:03:17] tells Claude exactly where to put the file, what to include, and what patterns to follow. Claude will read those reference files and match the style exactly. Specificity is the difference between Claude generating production code and generating a prototype you have to rewrite manually. Mistake number six, letting Claude add inline styles. So, when Claude isn't sure where your CSS files live, a lot of the time, it'll take the easy route and just inject inline styles into your liquid files. This is a maintenance nightmare. You can't update styles from

[00:03:50] the theme editor, it overrides your CSS cascade. Tell Claude which CSS file to use. If your theme uses component level CSS files, tell Claude that. If there's a global stylesheet, point to it. Once I put this rule in my Claude.md file, I never had that problem again. So, mistake number seven is not using Git branches for experiments. This one would have saved me more time than anything else if I'd started doing it sooner. When Claude makes a big change, a new section, a layout overhaul, anything experimental, you should be doing that on a separate Git branch, not

[00:04:23] on main. Here's what happens when you don't. You ask Claude to try something, it makes changes across six files, you realize the approach isn't right down the line, and now you're trying to untangle which changes to keep and which to throw away. It's a complete mess. Now, with branches, Claude can go wild. If the experiment works, you merge it back into main, and if it doesn't, you just delete the branch and nothing is touched. I do this for every major change now. Small tweaks, fine, you can do this on main, but if Claude is building something new or you're not sure whether you'll keep it, branch it

[00:04:55] first. Takes 5 seconds and it gives you a clean undo. Mistake number eight, not reviewing schema settings. Claude generates Shopify section schemas that technically work. A lot of the time, the section loads, the settings appear in the customizer, but the merchant experience is terrible. Look at this one, for instance. The label is just the ID repeated. So, your client is going to see heading text content main in the customizer and have no idea what that means. The default is lorem ipsum and there's no info text explaining what

[00:05:27] this setting does. Always review the schema Claude generates. Check that labels are human-readable, defaults make sense, and there's info text where a non-technical person might need guidance. Remember, you might understand code, but your client lives in the Shopify customizer. That's their interface, so make it clean for them. Mistake number nine, saying just "General improve this." Never, and I mean never, tell Claude to just, quote, like improve something. I've done this before, you just say like improve this product section, and Claude just will refactor the entire file. It'll rename

[00:06:01] CSS classes, restructure the liquid, change the schema IDs, and rewrite the JavaScript like from scratch. Technically, the code is like better, but it breaks every reference to CSS classes across the theme, and it breaks the customizer settings because the schema IDs changed. So, half the section's functionality stops working, and yeah, it's just it's just a nightmare. So, be surgical and tell Claude exactly what to change. One specific change per prompt. If you want multiple changes, make multiple prompts

[00:06:34] or have Claude generate a plan that you can sign off on. Let Claude commit after each one so you can roll back individually. Final mistake, not using a Claude.md file. So, this is the most important thing to do with Claude when you're using it with your Shopify store. It'll fix about half of the other mistakes on this list, to be honest with you. And so, that's using this Claude.md file. Claude.md file sits in the root of your project. Claude Code reads it automatically at the start of every conversation. It's basically your rulebook for the specific conversation.

[00:07:08] Without this file, you're repeating the same instructions to Claude every single conversation. With it, Claude starts every session already knowing your rules. I'm going to put a link to a Shopify Claude.md starter template in the description for you guys to be able to copy, customize to your theme, and drop into your project root. If you take one thing from this video, please set up a Claude.md file. Takes 5 minutes and it prevents most of the problems I just talked about. If you haven't set up Claude Code with Shopify yet, I have a full walk-through that covers the entire

[00:07:39] setup from theme connection to GitHub to Shopify CLI, everything, that I'll link right here. And if you want to see me build a Shopify app with Claude Code, that video is coming next. Drop a comment if you've made any of these mistakes or if you have a Claude Code horror story that I didn't cover, and I'll see you guys in the next video.
