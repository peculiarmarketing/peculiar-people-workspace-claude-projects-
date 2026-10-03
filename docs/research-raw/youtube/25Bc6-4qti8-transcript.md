# Build with AI with full dev MCP support

- URL: https://www.youtube.com/watch?v=25Bc6-4qti8
- Channel: Shopify
- Published: 2025-12-10
- Length: 2:49
- Views at fetch: 8704
- Fetched: 2026-10-03 with yt-dlp (creator captions), file 25Bc6-4qti8.en.vtt
- Coverage: FULL TRANSCRIPT from captions. NO FRAMES: video download was blocked in this session, so on-screen code, settings and commands were not seen. Auto captions can mishear technical terms.

## Chapters

- 0:00 Introduction to DevMCP
- 0:22 Building a checkout extension
- 1:06 Implementing dynamic content
- 1:55 Expanding to POS and wrap-up

## Description

```
Shopify's Dev MCP validates APIs in real-time, detects errors instantly, and generates production-ready code so you can ship faster. Building commerce experiences just got exponentially quicker. 
Part of Shopify Winter '26: The Renaissance Edition. Explore all 150+ updates: shopify.com/editions/winter2026
```

## Transcript

[00:00:00] I'm Darius and I work on developer experience at Shopify. Years ago, it took ages to build an app, but today, well, let me show you. Let's start by opening up a cursor and enabling the dev MCP server. The Dev MCP server brings all our Shopify dev platform, our docs, our APIs, and our best practices directly into your IDE. How about we take it for a spin. Build me a checkout UI extension. It should include three promises in an unordered list. Fast shipping,

[00:00:30] ten year guarantee, and 24 hour service. When paired with the Dev MCP cursor doesn't just generate code, it learns about the specific APIs, it pulls in the relevant docs, and then it validates the output to ensure your code runs smoothly. All right. That's not so bad, but I think we can tighten this up a little bit. Let's add an image to the left side of this block of text. Here is the link to the image. Also, let's update the heading to be more punchy. That looks much, much nicer.

[00:01:06] But an extension with just static text is kind of boring. I really want this extension to be configurable in the merchant admin. Let's start by moving this data into a meta object. Help me create a metaobject declaratively. Store the image URL, the heading, and the list items. The extension should read these values from the metaobject. Great. The Dev MCP server added the metaobject definition into the Shopify app toml. and updated the extension to read from it. Now let's make it configurable in the admin. Can you make the metaobject values

[00:01:36] configurable via a new route in the admin app home. And there you have it. In one command, the Shopify Dev MCP server generated a new route, scaffolded out a form, and integrated the meta object definition. Well, let's take this one step further. I want to recreate this exact same experience on POS. Let's ask the Dev MCP server to help us out. Can you create a POS extension that highlights the exact same information from checkout. Read from the metaobject

[00:02:06] and use the post-purchase render target. The Dev MCP server understands our goals from our previous work on the checkout extension. However, it's smart enough to understand the differences between checkout and POS to bring in the relevant APIs. Okay, there you have it. We went from a simple idea to a fully fleshed out application in minutes. The checkout extension. app home UI and POS all working together. Shopify Dev MCP server brings all of the power of the Shopify

[00:02:36] dev platform into your IDE. It reduces the time required to get started so you can start building today. So what are you going to build?
