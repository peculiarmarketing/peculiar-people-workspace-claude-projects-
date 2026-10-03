# Shopify AI Toolkit: Run Your Entire Store With Claude Code! (Setup + Use Cases)

- URL: https://www.youtube.com/watch?v=62Zc8DUVjbg
- Channel: Ryan AI SEO Tips
- Published: 2026-04-11
- Length: 15:31
- Views at fetch: 9753
- Fetched: 2026-10-03 with yt-dlp (YouTube auto-generated captions), file 62Zc8DUVjbg.en.vtt
- Coverage: FULL TRANSCRIPT from captions. NO FRAMES: video download was blocked in this session, so on-screen code, settings and commands were not seen. Auto captions can mishear technical terms.

## Chapters

- 0:00 Introduction to Shopify AI Toolkit
- 2:22 AI Assistant (Use Case 1)
- 4:46 Bulk SEO Rewrite (Use Case 2)
- 8:57 Inventory / Order Ops (Use Case 3)
- 11:20 Modifying your theme and website
- 13:44 How to WIN in the Age of Agentic Search

## Description

```
Get LinkGPT to drive traffic to your store from ChatGPT, Claude & Gemini: https://apps.shopify.com/link-gpt

Shopify just launched a MASSIVE update that changes everything for Shopify stores. The Shopify AI Toolkit lets you manage your entire store from Claude Code, Cursor, Codex, Gemini CLI, or VS Code. Bulk SEO, alt text, metafields, inventory, collections, blog posts, inventory, all of it. In this video I walk through the full setup and the exact use cases that'll save you hours every week.

⏱ Chapters
0:00 Introduction to Shopify AI Toolkit
2:22 AI Assistant (Use Case 1)
4:46 Bulk SEO Rewrite (Use Case 2)
8:57 Inventory / Order Ops (Use Case 3)
11:20 Modifying your theme and website
13:44 How to WIN in the Age of Agentic Search

🧠 What is the Shopify AI Toolkit?
Announced April 9, 2026, the Shopify AI Toolkit is an official plugin from Shopify that connects AI coding agents directly to your Shopify store. It gives the agent three things it didn't have before: live access to Shopify's documentation and API schemas, real-time code validation against those schemas, and the ability to execute operations against your actual store through the Shopify CLI. Translation: the agent can now read and write to your store, not just generate code you copy-paste.

📌 Who this is for
Shopify merchants, founders, and operators who want to manage their store with AI instead of clicking through the admin. No coding experience required, if you can type a prompt, you can use this.

💬 Follow for more
I cover Shopify, AI search, and ecommerce optimization. New video every week. Hit subscribe if you want the next one.
```

## Transcript

[00:00:00] All right, this is a big deal. Shopify AI toolkit just dropped and let me show you something. I'm just going to go into my terminal here. I've already been talking to Claude about my store and so on and I'm going to say, um, "Please generate descriptive SEO-friendly alt text for every product image in my store based on the product title and description. Update them all." And I'm just going to enter and I'm just going to let Claude go to work through the CLI. All right, it's been a couple of minutes. Claude has gone to work and it's executed the task perfectly. I see

[00:00:33] all 18 images have been updated successfully with zero errors. I can see all of the data here and if I go into my Shopify store and I go to the products, I click on any kind of products like this one, I'll see that the alt text has been correctly displayed based on the product image. So, this is the power of the Shopify AI toolkit, but it's really just the beginning because there's so many use cases that you can also implement and I'm going to go into each and every single one of them so that you can do it

[00:01:04] yourself. But before I do, what is Shopify AI toolkit? Like what is this release? Why is it such a big deal? Shopify AI toolkit is an official Shopify plugin. It works in Claude code, cursor, codex, Gemini, V VS code, basically any kind of interface and it lets the agent, in this case Claude, read docs, validate code, and execute against your real store via CLI. And CLI just stands for command line interface

[00:01:38] and that's exactly what these are, right? All of these are just interfaces that you can use to interact with the tool. All right? And you can see here that, uh, it's super super simple to set up. All you need to do is in your CLI, you need to enable the Shopify marketplace and then install the plugin. Once you do that, the Claude agent is going to have all the context that it needs about your store once you log in so that you can use it for really a plethora of different use cases. I mean, there's so much that you can do with

[00:02:09] this. We're all just kind of figuring it out, but I've already identified three major use cases that you can use this for that are pretty incredible. And of course, I'll be going into each and every single one of them. So, to start off, use case number one, you probably guessed it, is an AI assistant. And because the agent is going to have so much context about your store in real time, it can perfectly explain and audit your store or do things like apply discounts or bulk changes to products. So, for example, I'm just going to open

[00:02:43] up my terminal once again and I'm going to say, "Apply a 15% discount to all of my products." And it's really that simple. The AI assistant is going to be able to go in. It's going to be able to apply that change. That's it. It can also do things like obviously explain about your store and if you have any kind of customer queries, if you want any kind of specific analytics data like, you know, for example, which products are underperforming, of course, it will be able to do that too and run

[00:03:16] that analysis. But in this case, let's just check how our discount is going. And there you go. I just wanted to skip over you waiting for it to finish, but it logged in, executed the GraphQL operation, and automatically applied the 15% off everything discount to all products. And it even gave me all the information so I can check the discount ID and so on. So, you can see just how powerful this is. And you know, if you ever want to ask it like any kind of questions like, for example,

[00:03:48] um, "What is my best performing product?" Right? Previously, you need to go in or do some analysis or anything like that. Now you can literally just ask Claude code, right? So, let's see what it comes back with. All right. So, since my store is actually a test store, it doesn't have any kind of orders, but if you did have orders coming in, if you actually have a real store, which I'm guessing that you do, you can literally just ask it and it'll be able to query all of the analytics and the financial info. And you can get

[00:04:20] as intricate as you want with this. You can literally ask it, you know, about specific financial data or specific days or what's your best performing product on X amount of time or, you know, what is the best time of day that people buy? There's really, like I said, so many use cases for this AI assistant. So, just kind of putting some ideas into your head already about how powerful this tool is. All right? Now, number two is going to be the bulk SEO rewrite. So, basically all of the SEO functionality that comes with this. So, we already did

[00:04:53] one of it, right? Alt text for every single product image. But there's so much more that you can do. There's stuff like meta fields clean up so you can audit all of your product meta fields and fill in any missing values for X field. You can also just say something like, "Optimize my products for SEO." But I don't really recommend this because what will happen is you're going to use a bunch of tokens. It's going to go in. It's going to do a bunch of things that you don't have maybe 100% visibility on. So, I'd only say if you do do something like this and the only reason why I mention it is cuz

[00:05:26] it's actually what Shopify used in their example, which is literally like, "Optimize all of my products for SEO." Um, if you do do that, just be like, um, be verbose and, you know, um, "Confirm with me before making any specific change." Just so you have a little bit more control, right? But if you wanted like some specific commands, uh, meta fields clean up is one that I came up with. You can literally audit all of your product

[00:05:58] meta fields and fill in any kind of missing data. So, for example, I'll say, "Audit my product meta fields and fill in any missing data or missing values for SEO. dot description." And it can really be anything, right? So, in my case, it's going to be description, but in your case, it could be something like the materials. It could be the care guide. So, if it's materials, for example, it'll literally go in, read the description, read the title, understand, okay, is this shirt made of cotton? Is it made, you know, is it a leather jacket or something and

[00:06:31] fill in that data, right? So, again, all kinds of product meta fields can be auto-filled using this. But I'm just going to go for SEO description. Coming back to our store here, our test, uh, store, uh, you can see here that a lot of these, uh, don't have descriptions. So, I expect that to get published. And by the way, while we're here, we can actually check if the discount that we created earlier was applied and you can literally see here that it is. So, 15% off everything is applied to all of our products.

[00:07:04] Incredible, right? All right, let's go back to our terminal here and see what happens when we ask it to fill in all of our SEO descriptions. And just a heads up, while you're running this tool, it's very likely that it's going to prompt you every now and then to accept or not accept something or authenticate. In In this case, you know, generally just say yes and it'll continue to be able to work. So, you can see it's been working for a little bit. It's, uh, created a whole kind of script and it's now writing it to our store.

[00:07:38] So, let's just wait for those results. All right, and it looks like it succeeded. So, uh, all 17 products now have SEO descriptions set. It's providing me the audit summary. So, two of them actually did have the description, but now the 15 that didn't have been set up. So, let's just go ahead and validate that. We'll go in products. We can click on any single one like this one and we expect to see the description filled out and also the SEO description here. And you can, by the way, you can see all your

[00:08:10] different meta fields. But I'm just going to go into the search engine listing and I can see that it's been updated as well. So, that's perfect. Uh, on top of that, let's just double-check by clicking any single one here. Multilock, okay, so that's filled out and also the search engine listing is filled out. Perfect. Just, you know, incredible. Uh, so it's working exactly how we wanted to. All right, so very very powerful for SEO. You can use this for any kind of meta field,

[00:08:43] anything with SEO related. You can do bulk edits and have AI generate those fields for you and make sure that you have nothing empty so you appear more often or higher on search engine results. So, that's use case number two. The final one, use case number three, is going to be inventory and order operations, okay? And this is where you can get a little bit creative with it. So, for example, you can create an automation. So, for every X number of orders, plant a tree, right? That's really kind of something popular, uh, where, um, stores like to show they're

[00:09:16] environmentally conscious. You can do something like, "Show me every product with less than five units and draft a reorder list." So, we're actually just going to use that as an example and, uh, we'll go ahead and, um, we can, I think, do we have anything with less than five units? Let's check. Let's go into products here. Oh, okay. So, we have one that's 10 in stock and we have another one that's zero in stock. So, we expect both to get pinged and for reorder list to get drafted. So, let's go back into terminal here. Show me every product with less than, let's

[00:09:49] say, 11 units and draft a reorder list. All right, so that was quick. So, it's already gotten back to us and it's created a reorder draft. It's checked all of the audit of all of our uh products and it's actually said that we should definitely reorder some of these. And it's been smart enough to figure out the gift card is actually not a product that requires a reorder. All right, that's how that's how good it is. So, it's telling us priority number one, priority number two, and it's drafting all this. So, this looks

[00:10:23] much better than I even expected. So, it's giving us priority number one, this snowboard is out of stock. And it's telling us that these are critical. All right, so let's go ahead and create this reorder list. So, now it's just creating an MD, which is just a markdown text file, that's going to allow us to see all of that information, uh which is exactly what we want. All right, perfect. So, it's drafted up that file, and now we can literally just go ahead and copy this, or you can ask it to actually export it into a file that you can then send to your team, right?

[00:10:56] So, super useful, exactly what we needed. I'm sure it's getting kind of old at this point, but as you can see, this tool works exactly as advertised. It really is just allowing AI a transparent window into your store, and of course, the ability to modify your store and uh edit or input anything that needs to happen, right? So, extremely powerful. Um I'm going to get into some limitations, because I think it's important to understand what and what it can't do. So, you can think

[00:11:28] of every Shopify store as having two layers. The first is going to be the data layer, and this is your products, your prices, your inventory, your descriptions, all text, meta fields, you get the idea, all of the data. And then there's the theme layer, which is like the front end, which is the colors, the fonts, the layout, your homepage and product pages, your header, your footer. And this is kind of a visualization of that. So, the way that this CLI works, this CLI is really only built for this. It's only built for all of these fields

[00:12:01] of kind of data. So, it's built for admin, right? What it is not built for, at least not yet, is to actually make changes directly to the theme layer. So, you could go ahead and you can talk to Claude, and you can ask it, um on the hero page, can you generate like a a, you know, badge or something, like 100% uh money-back guarantee or something. And Claude will actually generate you the exact, you know, code of whatever that badge looks like and and how it fits

[00:12:33] into your store. But that code, you're going to need to So, this is going to be code, right? It's going to be JavaScript. You're going to need to manually input that, copy that code, and input it into your theme, okay? So, the CLI does not yet have the ability to just input elements directly into your front end, or change the color, or change the fonts, or anything like that. But the reason why I kind of wanted to show you um this uh kind of uh example of of the back end, or kind of a visualization of

[00:13:05] the back end, is to show you that it is still very, very powerful. Like, for example, all of your blog posts, I'll just go for like a different color here, all of your blog posts here, it's all just metadata. It's all just, you know, markdown. So, it's very, very easy to imagine using the CLI to just add, you know, new blog posts, it's all just data. But it's So, it's still extremely powerful. It just doesn't have that ability to actually input elements, or change your theme uh liquid uh directly,

[00:13:39] okay? So, just be knowledgeable of that uh single limitation. Now, in case it's not clear at this point, and I talk about it all the time, AI is changing everything about how e-commerce operates and how users find out about your store. And Shopify AI toolkit is incredible. It's incredible at doing things, but it doesn't have an opinion yet on what to do for AI search specifically. So, the toolkit has no view on which schema fields are actually important for ChatGPT, Grok, or

[00:14:13] Perplexity, and the ones that they actually read versus the ones that are just legacy SEO. And here's why I'm bringing it up. LinkGPT, which is my own Shopify app, uses this exact toolkit and MCP, model context protocol, to help stores get cited more often in AI search. And it handles all of the structured data LLMs actually parse, like LLMs.text, JSON-LD, and the AI context metadata that LLMs actually are going to read. But it also does LLM

[00:14:49] outreach and index now. So, it makes sure that all of that information actually gets to LLM providers like ChatGPT and Perplexity, so that they actually index your store instead of guessing at it. So, if you're thinking about setting up toolkit, uh or interested just in ranking higher in ChatGPT, it is worth a look. The link is going to be in the description, or you can just find it in the Shopify marketplace by searching for LinkGPT. All right.

[00:15:20] Now, that's going to be it for this video. If Shopify keeps shipping at this pace, I'll keep covering it. Uh definitely subscribe if you haven't already, and I'll see you in the next one.
