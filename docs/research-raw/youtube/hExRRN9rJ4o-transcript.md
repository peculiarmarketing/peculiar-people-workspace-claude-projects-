# How to use AI as a SHOPIFY DEVELOPER in 2026 (Cursor + Shopify Dev MCP)

- URL: https://www.youtube.com/watch?v=hExRRN9rJ4o
- Channel: Bosidev | Shopify Developer
- Published: 2025-04-05  (OLDER THAN 12 MONTHS)
- Length: 22:27
- Views at fetch: 17625
- Fetched: 2026-10-03 with yt-dlp (YouTube auto-generated captions), file hExRRN9rJ4o.en.vtt
- Coverage: FULL TRANSCRIPT from captions. NO FRAMES: video download was blocked in this session, so on-screen code, settings and commands were not seen. Auto captions can mishear technical terms.

## Chapters

- 0:00 Intro
- 1:10 Setup Cursor
- 2:12 Cursor features
- 7:53 Using Cursor (real life example tasks)
- 8:46 Example task 1 (Chat/Command + K)
- 10:59 Example task 2 (Tab)
- 13:14 Example task 3 (Agent)
- 17:21 Shopify Dev MCP Server
- 19:50 5 AI/Cursor tips
- 21:42 Outro

## Description

```
👷 Create Cart Transform & Discount Functions - no Plus plan required (my Shopify app): 
https://bit.ly/nerd-functions
--------------------
🚀 Take your Shopify developer skills to the next level:
https://bosidevacademy.com/products/shopify-developer-course
--------------------
✉️ Weekly Shopify dev newsletter: 
https://bosidevacademy.com/pages/newsletter-signup
--------------------
💬 Social Links:
X: https://x.com/bosidev
LinkedIn: https://www.linkedin.com/in/bastian-fritsch-2353271a2
Discord: https://discord.gg/pR58EfYNTR
--------------------
🔗 Video Links:
Download Cursor: https://www.cursor.com
Shopify CLI Video: https://www.youtube.com/watch?v=zeZTgOiU0LI&t=145s
Shopify Dev MCP Server documentation: https://github.com/Shopify/dev-mcp?tab=readme-ov-file#setup 
--------------------
⏱️ Timestamps

00:00 Intro
01:10 Setup Cursor
02:12 Cursor features
07:53 Using Cursor (real life example tasks)
08:46 Example task 1 (Chat/Command + K)
10:59 Example task 2 (Tab)
13:14 Example task 3 (Agent)
17:21 Shopify Dev MCP Server
19:50 5 AI/Cursor tips
21:42 Outro

--------------------

Hey my Nerds!

In this video guide im going to show you how to use AI as a Shopify developer. I will present you "Cursor" which is a code editor with build in AI tools. I also show you with real life example tasks how to apply AI to get faster and more efficient with your Shopify code tasks. I will also explain what the Shopify Dev MCP Server is. In the end you will get 5 more tips on how to use AI/Cursor to get the full potential of these tools.

If you have questions let me know!
```

## Transcript

[00:00:00] If you are not using AI as a Shopify developer yet, you are falling behind. Hey my Shopify nerds, it's Boosey, your Shopify developer freelancer from Germany. I started using AI back in 2023 with Jet GBT and it was crazy on how my service as a Shopify developer improved. The only annoying thing with Jet GBT is that I always have to jump back and forth between my code editor and Jet GBT. Since also Jet GBT didn't know my code base, I always had to explain everything from scratch to it until now. Today I want to show you a tool that took my efficiency as a Shopify

[00:00:32] developer to the next level. We are looking at cursor which is basically a code editor on steroids. In this video I'm going to show you first what cursor is, how to use it, and what it's capable of. In the next step, I'm going to show you how I use cursor in real life to implement features. In the last step, I will show you what an MCP server is and how to implement the Shopify MCP server into Cursor. And of course, keep watching because in the end, I'm going to give you five tips and how to use AI to really get the full potential out of it. Quick disclaimer, in this video, for whatever reason, I'm calling the tool

[00:01:05] cursor.ai, but it's just cursor. So, don't get confused by me. Now, let's jump right in. First of all, we have to download cursor.ai. You have to visit the website of cursor and just download it for Windows or Mac. I have a Mac, so just click download. After downloading, you can just open cursor.ai and you will see that it's basically the same code editor as VS Code. So, don't worry if you used VS Code before. It's basically just the same. It's both developed and handled by Microsoft. The only thing is that we

[00:01:38] have extra features going with cursor.ai. In the installation process of cursor, you will also be asked if you want to get the settings and all the plugins from VS Code. So, everything you set up there, you can just like take over to the cursor.ai code editor. Since we cannot use cursor.ai, AI with our code editor in Shopify, which we don't want to use. Anyway, you also have to download the Shopify CLI to work remotely on your theme. If you don't know how to do that, check out my video on the Shopify CLI and you're ready to go. That's it. Now, you can use cursor.ai. In the next step, I'm going

[00:02:10] to show you what Cursor AI is capable [Music] of. I opened up my test theme in Cursor.AI and Cursor.AI AI mainly has three features and I'm going to show you all of these. The first feature is called command + K. It's just on the website like this. The thing is you can simply just mark code with your cursor and then hit command K. And here it opens up a little dialogue window where you can just like say instructions or ask questions. So I can say what is this

[00:02:43] block doing? You have two choices is either submit edit or quick questions. Quick questions is for questions about the code and submit edit is editing the code. I just want to ask this question and it gives me a explanation about the marked code. You can also go ahead and say add an image to this block also the settings and say submit edit. And now it changes everything in the code which is uh nice, super handy for quick fixes, quick questions, quick code changes. The next feature and personally my favorite feature is the tab function. The tab function gives you intelligent

[00:03:17] suggestions for your code. So let me show you an example. I want to create a new section called shop the look. And that's it. I didn't do anything. And now when I start typing it gives me suggestions for my code. And the cool thing is it already reads what I want to do which is crazy. Like shop the look. I didn't even say something. I just named the file like this and it gives me the suggestions. So I can just say tab yes. And it gives me even more suggestions. So obviously the container shop the look header and I just can tap my way out of it. And I can also go in here and say schema shop the look and I just can go

[00:03:51] in here and say yes I want this and text and it also always changes everything on its own just by the tab. So in 5 to 10 seconds I already built like this small layout of this shop the look section. It really can suggest intelligent features. It was kind of like it reads my mind which is yeah it's crazy. you have to try it. The use case for this if if you want to code yourself, it makes it super super fast and you can just like use it whenever you want. The last feature of cursor.ai is the real powerhouse. So the main functionality of cursor.ai. We can

[00:04:23] open this by going ahead into view appearance and say secondary sidebar. You can also open it with option commandB on Mac. And this opens up this sidebar which is the agent. And the agent is pretty much capable of doing anything you want. So you have some stuff here. Let me explain to you. So first of all you can here add context to whatever question you have. You can add files, code, docs. You can do basically give any context that you want. Then here you can select the mode, the agent, the ask or the edit mode. And here you

[00:04:56] can select the model. I use auto select. You can also do thinking and the clot 3.7 is for my experience the best. And in the last step you can also upload pictures. I have to say I didn't use this quite as much but you can also upload pictures to give some instructions to your code. First of all, this agent has a normal ask functionality which is working like check GPT. You can ask questions. For example, how to center a diff is like a common question that has nothing to do with your codebase and this gives you the answer just how to center div. The

[00:05:28] next thing you want to do is you can also ask codebase related questions. For example, you go ahead and enter add and say codebase. You can ask stuff about the code base you don't know already. Now it gives you the whole explanation once even for the code how to edit and then in the next step it also says oh it already has this and then how you can implement the quick add to cart in the theme editor. It just read the code and now it knows everything. If I remove this and open a new tab the crazy thing about the agent is basically it acts

[00:06:01] like a real I mean code body code servant. It does everything for you. To go back to the shop the look example, let's just ask the agent to do it for us. Now you can see I asked this question and now it does it step by step. It first lists, it searches, it does everything to create this section. Now it created the shop the look section and already filled everything itself in the code and it also explains all the thought steps behind of it. To show you if this is cool or not, let's open the theme. I start my development server here. Then go into the editor. And now

[00:06:35] if we click on add section, we can look for the shop the look section which is here. I put all the settings and implemented everything. So we could select a lifestyle image. And then we can select products for blocks and also put an hotspot X hotspot Y position to move these hotspot dots here. And when we look at it in the shop, we can go ahead and just view the product. I mean, it doesn't work perfectly because when you click on these buttons, nothing happens. But for like a starting point, I created this in 10 seconds. And now I could just refine it, which is

[00:07:07] absolutely insane. So the agent is really a wonder boy, wonder girl, however you want it. But don't be fooled. This can end also the other way around. Sometimes I have cases where it doesn't work at all. Never just trust anything and put it out. Always check it first. The use case for the agent of course is complex and long features and especially if you don't know how to do it. There's also this edit mode. The edit mode is it just edits all your code. My experience is the agent makes more sense because it's just basically

[00:07:39] the same and it explains everything well. So I always use the agent or the ask if I just have a question. Now that you know how cursor.AI AI works. Let's get to some real life examples so I can show you how I use AI to fix my problems and the problems of my clients. The main thing you want to do by using AI is to get more efficient and faster. To get the most of Cursai, you have these three features I explained before, but there's like more or less fitting cases to use one or the other

[00:08:12] with different situations. I mean there's different tasks your clients can give you. We have two factors that come into play while solving problems. The first factor is the complexity of a task. So is it low complexity or like a short task or high complexity or like a longer task? The second factor is your knowledge. Do you know anything about it? Do you know nothing or just a little bit about it? Let's look at each situation by using a real life example. But before we start, I have to say you can use basically every feature of cursor.ai how you want it. But just to show you the capability of CJI, I will

[00:08:44] just use specific ones for specific cases. First of all, we have low complexity and low knowledge. The client could ask for example that he wants icons before the announcement bar messages and you don't really know how to do it or where to start. In this example, I would definitely use the agent, like a mix of agent and also command K to solve the problem because we have no knowledge about the problem or just low knowledge, but it's quick to fix. So let's go ahead and open the agent. If you have absolutely no clue, you could first ask the agent where even

[00:09:17] are the announcement bar messages to change. Add codebase and say where can I change the announcement bar messages in the code. Oh, it says in a sections announcement bar liquid. If you click on it, it instantly opens it. So we know, all right, it's here somewhere. Then you could go ahead and say add context. So now we're in the announcement bar and say can you add an icon to the announcement bar message with the settings. So now it just explained to it but you can also say apply and I applied everything and now it's also important to show you why AI is not perfect. So if you go to the base CSS it changed a lot

[00:09:50] of stuff just like for formatting you can keep this or not keep this. If you want to keep it in the base CSS or want to put it somewhere else that's up to you. And if we look at the announcement bar okay we now have icons but it's not rendered perfectly well. And here you can just mark this for example because there's something wrong still and say can you make the icon rendering the same as in the other cases in the theme because this is not the same thing. Now it changed it to be correctly and now let's have a look in the editor if it worked. We editor now and if we go to the announcement bar to a announcement bar message we can now select an icon.

[00:10:24] If we select one it gets displayed. Awesome. Now, of course, you can fine-tune the code, but we can also go back here and say accept the changes. So, we can just go in here and say accept, and it it's highlighted in your code, so you can always see what's going on. That's it. Within 5 minutes, you added the icons to the announcement bar without having any knowledge at all before by using the chat functionality. You could also ask just the agent. I just wanted to show you. And also using the command K functionality and say, "Hey, can you change this please? This was not correct perfectly." Now you can

[00:10:56] of course fine-tune it, but that's for that case. For the next task, we have a low complexity, but a high knowledge task. It's low complexity, quick, but you know already how to do it. An example task for this is the client wants you to show the shipping time on the product page. Since I already know what to do, let me show you. First of all, we can go to the main product liquid because I know there are the blocks. So, you want to add a new block with the shipping time. We could use the agent now, but I like to just code myself. So I use the tab function. We

[00:11:30] found where the blocks are rendered. We can go in here and say shipping info. And here let's create a diff class shipping info. And here we check product selected and available else span in stock. And here we give block settings in stock text out of stock text. Now we also want to add the settings of course to the block. Just enter. And here we can tab info. Yes. In stock text and the out of stock text that we want to

[00:12:05] do. We also want to add some colors for the in stock and the out of stock text. Let's type this color. Into stock color out of stock color. Let's go back in here. and also style color in stock and out of stock color. That was like 2 minutes. I just tapped my way through it because I know what to do. Let's check if it worked. Go to our product page. And now we can add the shipping info block. Let's put it above the buy buttons. Now we have in stock. We can also change the in stock color. Perfect. So we have the

[00:12:39] in stock out of stock text. And it also checks if the variant is available. If not, then the out of stock text is shown. Now, I did this by myself just using AI and the tab functionality. This was also really quick because I already knew what to do. And the good thing is while going I could also check if this was still the thing I wanted to do and had full control over it. That's why I like it the most in this cursor.ai editor. You can use this whenever you're just coding yourself. You're in the flow and it gives you like really smart suggestions. Like mentioned before, as you could see, I was just tabbing around

[00:13:12] and it did everything for myself. Perfect. The next two segments we can combine. We have the high complexity low knowledge or high complexity high knowledge of it. It's like a big task or a big feature you have to do and one time you don't know what to do and the other time you know what to do. But in both cases I would advise to use the agent because it's just a lot of code you have to write and even if you know or don't know how to do it it just saves you a lot a lot of time. for the task the client could give you. It would be to build an upsell in the cart drawer. Even if you know how to do it or don't

[00:13:45] know how to do it, you can open the agent and just let him do everything for yourself and just lay back and in the end we can adjust the things. First of all, we can advise the agent to build this. So really basic. Can you please add a UPS functionality in the card draw? He is done now and the crazy thing is you can watch every step that he's doing. So this took round about 5 minutes for the AI to fully complete the first run through. It's thinking, it's doing, it's explaining, it's iterating. And here it even does like the same way

[00:14:19] the theme already does. So it creates custom components. It implements everything in custom JS files. It also says, oh, here's an error. We run into some errors. He had to fix this. So he did everything himself. Run about 5 minutes. Big question is now what did the do actually? So let us check this. We have CSSJS card draw upsell liquid which is a snippet. All right. And the card draw of course. So let's go into the editor and see what he did. All right. We are in the editor and if we go

[00:14:51] to the cart settings, we can see there is no settings for the upsell. All right, we have this product in the cart. You might also like it. I mean there is something but we have to first figure out what the AI did. That's what I always said never trust 100% AI. So it uses the product recommendations but we don't want this. We want to say use a setting where you can put a collection of products. Now the did all the adjustments. So let's see what was happening now. Let's open the editor again. Go to the cart settings because now it should appear. Yes, we have the

[00:15:23] upsell products collection. Let's go ahead and say we have the homepage collection and click save. And if we go to our theme now, we have an upsell product. Now in the card drawer, we have the product image, a product title, price, and add to cart button. Let's see what happens here. We have added, but nothing changed, but it was added. So it missed the card rerender, which as you can see, the eye is not perfect, but we have a starting point. Now, from here, we could give AI more hints to complete the task. Let's also try to fix this. Card drawer does not rerender. We have

[00:15:55] to reload. Can you fix that? He's done now. Let's see if it worked. So, if we refresh our browser and now if we click add to cart, the cart refresh and the item is in the cart which is awesome. Now everything works. I gave the AI three prompts. So it was can you please add this? Can you please change this and can you please fix it? And it did everything perfectly. Even if you have knowledge or not, this already helped immensely. So, in 15 minutes, I have a full functioning upsell section in the

[00:16:27] cart raw. I mean, there's like still stuff to do. For example, like now we can still add it to the cart, although it is already in the cart or here like the image is a little bit cut off and stuff. So, it's not 100% working fine, but it is working and we have a nice starting point to work on this upsell section even more. But again, I have to say always check what you're doing because in the next step, you have to really verify that everything works properly fine. For example, here this is hardcoded. We don't want this. This is also hardcoded. We don't want this and other stuff. So you have to always check what is happening and make improvements.

[00:17:00] In the same essence, I have to say the agent is a real real powerhouse and it will just skyrocket your efficiency. This task could take me like 2 hours and I did it in 15 minutes from now. Now you saw how I use cursor in real life basically with the examples to fulfill the requests my clients give me. Now I'm going to show you how to install the Shopify MCP server. Let's [Music] go. MCP or model context protocol is a fairly new technology. Cursor on the website have a documentation for it. We

[00:17:33] can simply connect cursor to external systems and data sources that's super handy to give cursor additional context regarding your subject. Here are also some examples. You can hook a database or notion so it can read data out of notion or guide you wrote or GitHub that lets you create PRs, create branches, find code, etc., etc. Shopify also released an MCP server fairly recently and if we visit the GitHub repository, there's also a usage with cursor. There's two tools currently available. It's one the search Shopify dev documentation and also access and search

[00:18:07] Shopify admin GraphQL schema. With this MCP server, you basically give cursor extra information about the whole Shopify dev documentation. And also if you want to write CraftQL calls to implement this into cursor, we can just simply copy this. Then go back to cursor and here in the top left corner, we can go to preferences and here it says cursor settings. Here we can find the MCP section of the settings. And currently I have no MCP service added. So we can add one. And now it opens up this MCP JSON. And here we can simply copy this. And that's it. If we go back

[00:18:39] now to the preferences, cursor settings, we can see that we have the Shopify def MCP here. Now it's enabled but CL closed. You have to quickly reopen cursor. Let me do that. Now I reload cursor and as you can see there's this green dot and the Shopify def MCP is ready to go. Now if we open up the agent again, we can go ahead and ask something related to the Shopify docs. For example, how to implement settings for sections and hit enter. And now whenever there's a fitting case for an MCP tool to use the agent will suggest it. So in our case it's the search dev docs and we

[00:19:13] can say okay run tool. And now it gives you the information based on the real Shopify dev docs. All the explanation about creating these settings for the sections. The Shopify MCP server tools ensure that the information is pretty pretty accurate that the agent gets. definitely install this into cursor to minimize the risk of getting false information. As I mentioned in the beginning, it's currently two tools, but I think that Shopify will improve this even further in the future. Now that we set up everything and also understand

[00:19:45] everything about cursor, I can give you five more tips on how to use it to improve even [Music] further. First, know how to code. Yes, you heard that right. You will not be using AI proficiently if you don't know what to ask or what to do. If you use AI and don't know what's going on, this can lead to a lot of frustration. Second tip, ask simple questions. Don't over complicate prompting and coding. You want to move fast and get results fast. AI will not understand you 100% anyway.

[00:20:19] Keep it clean and short. As you could see in my examples, I just put one sentence and that was it. Third tip. If you can't find a solution after some dialogue with AI, just start over again. I made the experience that the more I talk to AI about a problem or try to redefine code, the worse it got. I think that's because AI also gets confused the more commands you give to it. I don't know why, but I just made the experience. Just take the knowledge you got from this dialogue and start over with a new prompt. You will see that you get better results this time. Fourth

[00:20:51] tip, always check what AI is doing. I am preaching this vibe coding gets a trend where people just recklessly use AI and implement everything that AI is telling them to do. Maybe this works for certain people industries, but in the Shopify space, this is not a good idea because I had the experience that AI, especially in the Shopify space, Shopify Liquid app and theme development is not fully developed. This can lead to a lot of problems and errors in your and your client's code. Tip five, still read documentation and educate yourself.

[00:21:25] Don't get lazy with AI and learn yourself. AI is just as good as the information out there. And especially in the Shopify space, when stuff gets released, there is a pretty likely chance that AI doesn't know already about it. Jump into the Shopify docs from time to time and maybe you can teach AI something. And that was it. As you can see, AI or especially cursor.AI in our case is a powerful tool if you know how to use it and what you're doing. Blindly copying AI generated code will just make your life and your client's life much worse. But that's also pretty good news because look at it

[00:21:58] like this. AI won't take your jobs anytime soon. Definitely play around with our new tool cursor.ai and let me know in the comments how it changed your efficiency in the Shopify developer game. As always, I would be really happy if you would subscribe to my channel because I will post a lot of this stuff in the future. Also, don't forget to join my Discord community. I try to build a community solely for Shopify developers. If you're a beginner, if you're advanced, come join us. We help each other out and have a good time there. See you next time.
