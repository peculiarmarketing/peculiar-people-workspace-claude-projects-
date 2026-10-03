# New Shopify AI Toolkit: Claude Code Setup + Demo (April 2026)

- URL: https://www.youtube.com/watch?v=ptnWksC9TXY
- Channel: Jonathan Lewell
- Published: 2026-04-11
- Length: 7:45
- Views at fetch: 9794
- Fetched: 2026-10-03 with yt-dlp (YouTube auto-generated captions), file ptnWksC9TXY.en.vtt
- Coverage: FULL TRANSCRIPT from captions. NO FRAMES: video download was blocked in this session, so on-screen code, settings and commands were not seen. Auto captions can mishear technical terms.

## Chapters

- 0:00 Intro
- 0:10 Installation
- 1:15 Listing available products
- 2:36 Getting store analytics
- 3:50 Customer lifetime value
- 5:35 Theme edits

## Description

```
You can now control your Shopify store with Claude Code. Pull revenue data, calculate LTV, edit your theme - all with prompts.  

Note: This assumes you have already installed Claude Code. If you haven't, I'll create a video on that soon.

The toolkit documentation: https://shopify.dev/docs/apps/build/ai-toolkit

Chapters
0:00 Intro
0:10 Installation
1:15 Listing available products
2:36 Getting store analytics
3:50 Customer lifetime value
5:35 Theme edits
```

## Transcript

[00:00:00] Shopify have just released the AI toolkit, which is really cool and it allows you to manage your store using Claude. I've tried it, it works really well, so let's do it together now. So, first we're going to go to the Shopify AI toolkit page on the developer documentation. And then there's these two sets of instructions here of how to install it. So, I'm going to be installing with Claude code and it gives you the code to copy. So, first I'm going to open the terminal. I'm going to launch Claude. dangerously skip permissions I launched Claude this way so that it

[00:00:32] doesn't keep asking me about permissions and things like this. Um so, I've initiated Claude and now I'm going to paste in that command. So, plug-in marketplace add Shopify Shopify AI toolkit. So, it's successfully done that and now there's the next command. So, install the plug-in. Going to copy that in. And you see it's giving me these options at the bottom here. So, install for you, install for all collaborators, or you know, all these other options. So, I'm going to install it for you, so user

[00:01:04] scope. That is done now as well. Now, if I click on reload plug-ins. So, that looks all good. And now, what is the next step? List out all of my active products on Shopify. It's probably going to ask me then for a link to my Shopify store to help me like, you know, finish the setup. So, let's see. It's asking me if I want to run the

[00:01:44] query directly against the store to fetch the results. I would say yes. So, now it's asked me, yeah, for what is my store URL basically. So, my Shopify store URL. So, I'm going to paste that in now. So, if I look at my actual website, the actual short hand account name is actually John's Nutrition. So, I'm just going to paste this in instead. So, John's Nutrition. Now, it's going to load up my website. It's now authenticated.

[00:02:18] It's going to proceed. It's loading the store info. And it's listing out all of my active products. Super cool stuff, right? Um and now, let's show you some extra stuff. So, um let's first look at analytics and then it's let's look at editing actual store like uh themes and stuff like this. So, first thing is like um what was my revenue for the past 30 days? What is my average order value and

[00:02:52] website conversion rate? Isn't this insane? Like, it's literally querying my store. I mean, I'm just thinking of all of the different possibilities you can do now that we have a direct connection to you know, my Shopify store. I can ask it for analytics, you know, I can ask it for like, you know, monthly reporting. I can ask it for customer lifetime value, all this kind of stuff, man. It's so cool. Okay, so it's now asked access to my store analytics. Of course, I'm going to

[00:03:24] say yes. Have everything you need. &gt;&gt; [laughter] &gt;&gt; Okay, let's go. I don't know about you guys about what other software you've added into your Claude stack, but you know, I've added like pretty much my entire work stack at this point. Okay, cool. So, here's your store summary for the past 30 days, total revenue, average order value, sessions, and conversion rate. Awesome. Okay, now what was my customer lifetime value

[00:03:57] over the last 6 months? So, this is more of a tricky question, right? Because Shopify might not necessarily have this in the reports that easily. So, maybe it's going to have to do some calculations and things like this. And normally like before, I had to get an app called Lifetimely and that told me all of my customer lifetime value statistics and all of these kinds of things. But, let's see if this can also find this out. You see, so Shopify doesn't have a built-in customer lifetime value metric in the Shopify QL, but I can calculate it from component metrics. So, it's

[00:04:30] actually going to calculate these metrics from uh the data that it can get. So, it's got the revenue, it's got the orders. Let me fix the customer queries. And here you can see it's calculated customer lifetime value. So, it's calculated the average order value, purchase frequency on average, and the customer value over 6 months. So, the average order value times purchase frequency is about a $45.21.

[00:05:04] And then estimated annual customer lifetime value is uh 6 months times 2, 12 months. It's about a $90 customer lifetime value. Right. So, then it's justified all of this and it's 6 months customer lifetime value suggests that more customers are single purchase buyers right now. Given that supplements are consumable, there's a significant opportunity to increase purchase frequency through subscription offers. Yeah, it's true. It's true. Thank you, Claude. Um it's provided me the insight and suggestions. Insanely powerful. So, now that we've seen that it can look at the

[00:05:36] data that I have, can it also start actually editing the website design itself? So, if I look at my website, let me just load it up. livetropics.com You see, this is kind of the design that I have. Um so, I've got all my supplements, my reviews, etc. But, can I like, for example, like edit maybe this part? And to do this normally, I would have to go in and I'd have to edit the uh website theme. But, let's see if it can edit the actual theme for me. So, edit the uh home page

[00:06:09] uh title. Change it to, let's say, Science-Backed Supplements for real results. Um so, I'm changing the word true results to now real results. And obviously, I'd have to normally do that um within the theme editor. So, let me click go. And now it's looking for where it is in the theme.

[00:06:48] And it's figured it out. It's figured out the steps. It's going to find the main theme ID. It's going to read the template. Find the correct section and it's going to update the uh the section. I've just skipped ahead, but you can see now it's actually done this. So, it's changed the Science-Backed Supplements for True Results to Science-Backed Supplements for Real Results and it's applied the update to my live theme. So, let's check this out. I'm going to now open my website. Going to refresh it. And you see, it's now edited the actual copy on my theme. Insane stuff.

[00:07:23] So, I mean, I'm going to play around with maybe some more of the different uh commands and everything. Maybe I'll build some skills. Um but, it's looking super promising, really exciting. If you haven't tried it yet with your Shopify store, definitely do so. And I'm going to be doing more Claude tutorials for operators and professionals alike. So, feel free to subscribe if you liked this video.
