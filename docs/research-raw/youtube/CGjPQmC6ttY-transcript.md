# I Used A Screenshot and Claude Code to Build A New Shopify Theme

- URL: https://www.youtube.com/watch?v=CGjPQmC6ttY
- Channel: BitBranding
- Published: 2026-05-21
- Length: 20:05
- Views at fetch: 9204
- Fetched: 2026-10-03 with yt-dlp (creator captions), file CGjPQmC6ttY.en.vtt
- Coverage: FULL TRANSCRIPT from captions. NO FRAMES: video download was blocked in this session, so on-screen code, settings and commands were not seen. Auto captions can mishear technical terms.

## Chapters

- 0:00 Introduction
- 1:01 The two AI tools used in this test
- 1:51 Connecting Claude Code to Shopify
- 3:30 Testing the Shopify connection
- 4:10 Why you should not clone another brand’s website
- 4:53 First test: adding a trust badge section
- 6:54 Using a full Represent homepage screenshot
- 8:24 Reviewing the first AI-generated Shopify sections
- 9:27 Testing a more complex footer screenshot
- 10:43 Where Claude Code starts to struggle visually
- 11:52 Why Claude Design may be the better workflow
- 12:32 Creating a more detailed visual prompt in Claude Design
- 13:23 Preparing the handoff from Claude Design to Claude Code
- 14:40 Fixing the failed handoff with an uploaded file
- 15:35 Reviewing the new Horizon V2 theme
- 16:05 Comparing Claude Code vs. Claude Design
- 17:09 What this means for clothing brand owners
- 17:53 What this means for Shopify developers
- 18:08 What this means for agency operators
- 18:46 AI is replacing the boring parts, not the team

## Description

```
🔗 Schedule a FREE personalized strategy session to scale your online store. 
►https://sales.bitbranding.co/?utm_medium=social&utm_source=youtube&utm_campaign=organic

👨🏻‍🏫 If you’re a clothing boutique or apparel brand store owner who wants to know the 5 keys to successfully growing and scaling your business, we created a free 15-minute training where you can get instant access.
►https://www.optimizedstoreowner.com/ecomm-training

🚀10x Sales with Juphy ai 40% off 
►https://apps.shopify.com/juphy?ref=ztlkzmj&utm_source=ztlkzmj 


🛍️Shopify for $1 
►https://shopify.pxf.io/c/2215710/1061744/13624  


💰Vitals - The All-in-One Conversion Marketing app: Reviews, Upsells, Bundles, Replays
►  https://vitals.co/shopify/8094692 

💎 Our Website VIP Day service builds an e-commerce Shopify website in just one day, but spots fill up quickly. If you're interested in joining the waitlist, please sign up on our website and we'll notify you as soon as a spot becomes available. 
► https://www.bitbranding.co/shopifyvip 


📈Fix IOS tracking issues, predict when customers will make a second and third purchase, and finally understand the value of each customer. 
►Try TripleWhale https://triplewhale.grsm.io/BB for 15% off. Make sure to use code bitbranding (it is case sensitive)


🧵Meet and talk strategy about your brand with a USA based manufacturer, Threadbird 
►Strategy Call https://threadbird.com/brand-building-consultation-form 

Already launched your Shopify store? We created a mini-course for you to finally understand your Google analytics and what you need to do to maintain your website performance.
► Grab the mini-course https://www.websiteafterlaunch.com/website-after-launch1628021970601?utm_medium=social&utm_source=youtube&utm_campaign=organic 

🛍 Clothing Store owner? Join our free online community 
►https://www.facebook.com/groups/optimizedstoreowner  

📩Post Pilot revolutionizes marketing by combining online and offline channels to generate significant returns on investment for stores using postcards. Learn more at
►https://app.postpilot.com/signup?via=bitbranding

CommentSold is the leader in live social selling, boost your sales by 33%. Get white-glove treatment by the team at CommentSold.
►https://try.commentsold.com/partners/bitbranding/ 

🎧 Subscribe to the Optimized Store Owner Show Podcast
►https://www.bitbranding.co/podcast?utm_medium=social&utm_source=youtube&utm_campaign=organic

I tested whether Claude Design and Claude Code can turn a screenshot of Represent’s homepage into a working Shopify theme.

Represent has one of the cleanest luxury streetwear homepages: edge-to-edge hero sections, strong product/category hierarchy, polished spacing, and a premium visual system. A build like this could normally cost a clothing brand thousands of dollars and weeks of agency time, so I wanted to see how far AI could actually take it.

In this video, I connect Claude Code to Shopify, test a simple homepage section, use a full-page screenshot of Represent’s homepage, try to recreate the layout directly inside a Shopify theme, and then compare that workflow against using Claude Design first before handing the build off to Claude Code.

The goal is not to clone another brand’s site. The goal is to study structure, hierarchy, spacing, and layout principles so you can apply them to your own clothing brand store.

You’ll see what worked, what broke, where Claude Design helped, where Claude Code struggled, and why the future of Shopify theme builds is shifting from raw development time into strategy, creative direction, photography, conversion testing, and execution.

If you run a clothing brand and want our team to review your Shopify store, find where you’re losing conversions, and show you what to fix next, book a free strategy call below.

00:00 Introduction
01:01 The two AI tools used in this test
01:51 Connecting Claude Code to Shopify
03:30 Testing the Shopify connection
04:10 Why you should not clone another brand’s website
04:53 First test: adding a trust badge section
06:54 Using a full Represent homepage screenshot
08:24 Reviewing the first AI-generated Shopify sections
09:27 Testing a more complex footer screenshot
10:43 Where Claude Code starts to struggle visually
11:52 Why Claude Design may be the better workflow
12:32 Creating a more detailed visual prompt in Claude Design
13:23 Preparing the handoff from Claude Design to Claude Code
14:40 Fixing the failed handoff with an uploaded file
15:35 Reviewing the new Horizon V2 theme
16:05 Comparing Claude Code vs. Claude Design
17:09 What this means for clothing brand owners
17:53 What this means for Shopify developers
18:08 What this means for agency operators
18:46 AI is replacing the boring parts, not the team
```

## Transcript

[00:00:00] Representative homepage is one of the cleanest in the luxury street, where edge to Edge Hero has the category grid, the kind of polish that it would cost brand 40 50,000 plus when they paid an agency to actually build this whole thing. And in this video, I'm going to take a screenshot of the home page, drag it into cloud design and walk away and see if I can come out with a working theme based on what we're seeing on the home page. So again, the idea is from a screenshot to a live preview of a website on Shopify. The thing that you should take for

[00:00:30] six weeks, I'm going to be doing it all in this single video. For quick context, I'm Christian Pinion, one of the co-founders here at Bit Branding. We are clothing brand marketing agency. We've helped and we've worked with over 800 clothing brands through our programs and our membership building Shopify stores is basically all that we do all day, which is exactly why I want to test this, because if a couple of AI tools can compress a four week build into just a few hours, that changes the economics in every store project that we run and every project

[00:01:01] that you might be also planning. So I want to show you what works, what breaks, and where the real human time still has to go because not everything here is going to be perfect. Let's talk about the tools. There's two tools in this video, both from entropic. Both included any of the paid plans that Claude has. So Claude Design is a visual one and actually launched this in April. And you essentially describe what you want, and it builds a work in design on a canvas next to the chat. You refine it with comments sliders. I will say this is still a research preview product, and it's included when the Pro Max team

[00:01:34] and enterprise account. And then also we're going to be talking about cloud code. This is kind of like the engineering behind the actual development in the back end. So this is more of a terminal tool. So you install it. You point a project folder in your computer. You can read entire code databases, write code, run shell commands, fix its own bugs. And Shopify just recently shipped an official integration with Claude earlier, and which is what's gonna really make this whole video possible for us. So let's get to the actual setup and jump into cloud design. All right.

[00:02:05] So the first thing that we're going to do is we're going to make sure that this is all connected. At some point Shopify had released this Shopify AI tool kit. And they give you some options in here on how to install it. But we don't have to necessarily do all this right now, because now we have a better connection through an official connector. So if you go if you are on your Claude desktop app, you can make sure that you're in the code option. You can click customize in here. And then you go to connectors. And then you just basically add you can browse connectors

[00:02:36] and you find Shopify. So we already had it installed. But I have to disconnect it and reconnect just to see how this works. If you have multiple stores you may have to disconnect and reconnect. So for example, we have a bunch of different stores for testing and different purposes. So I'm going to do this brand new store that we created so that it only targets that particular store for you. You may have to just connect this once and you're good to go. But if you if you do run multiple stores, you may have to do this for those particular stores. Okay.

[00:03:09] Now this is going to essentially have a sort of like a custom app that you need to install to make sure that you create that connection. And if we go to our Shopify, you'll see now we have all of these tools that we can use. For me, I'm going to all just hit always allow for all of these, just to make it a little bit easier for me when I'm creating or changing or making things happen in the back end. All right, let's hit back. Let's do a new session. Okay. Let's hope we're connected. Let's just run a quick test. Let's see. Get list of themes. And my shop.

[00:03:42] The first few times that you run this, you may have to still have it for a lot of these permissions and a lot of these things. And then once you done all these, a lot of times you won't have to necessarily do them again. Okay. There we go. And then we have our test data horizon and then debut vintage theme. And then we have our test data which is our main live theme. Let me go ahead and double check that. So if you go to here and we go to our online store, there we go. We have our test data as our main theme. And then we have the debut vintage and the horizon theme priority. All right.

[00:04:14] So now that we have everything here connected, we've confirmed that our cloud code can read and is connected to our Shopify store because it's able to pull all the information. Now let's go into the next step. Quick disclaimer to that. I want to just be up front about I never tell you to literally clone another brand's website and ship it. I think that's a fast track to one just looking generic, getting sued or actually both. What we're doing here is really studying the structure, the hierarchy, the spacing, the type system, so you can apply those principles to your own brand. All right.

[00:04:47] So I've actually published the horizon theme. Just so that's the one that we want to make the changes to. And I want to run just a quick test. Right. And on the horizon theme on the homepage at a three column section with shipping returns and secure payment options with an icon for each column. And let's see how it actually does with just a simple command here. Interesting. Okay, so it looks like it blocks it from being on a live theme. So what we're going to do is let's see if we can ask it to change horizon to non polished.

[00:05:21] Let's say bring back the was the name of it test data. And I guess that would probably be best practice. If you have this website live, you probably want to create a copy of your theme so that there are any errors or anything like that. You can always catch them and fix them before it actually goes back. Got it? So it looks like we have to go ahead and do that automatically. So or manually. So let me go in here and let's publish this one. Now that we have the horizon done here. Amazing. So it looks like it's created

[00:05:51] that section. And by the way I also want to clarify we are using Sonic 4.6. Hi. We're probably three fourths of the way there. So let's go and check out the yeah the horizon theme was going to go ahead and refresh this and see how it created that section. So it looks like yeah we have trust badges in here. We click on that. We can manipulate color schemes. The with each of the badges. Now we cannot necessarily manipulate the actual icons that it picks. I kind of pick

[00:06:21] those automatically. But again I just wanted to do just yeah, just a quick test just to see how it would it would do. And again it's it pretty good I would say if you wanted to and we could always, you know, reproduce it and give it more instructions on. We want the ability to change the icon images, for example, or we want the ability for mobile to be a completely different view, which it did actually really good job of making sure that I was mobile, mobile friendly, and it actually stacks up on top of each other on, on the mobile side. So yeah, that

[00:06:51] that test was great. So let's go ahead. I want to do a couple of tests in here. I want to take a full screenshot of the represent home page and see if, if we could just paste it in here and say make this happen and see what happens. So let's go ahead and do that. So let's go and check for represent. And then in here I've taken a screenshot of this whole this whole home page which again at the end of the day it's somewhat straightforward. I would say this section here

[00:07:22] it's a little bit different. So we'll see. I don't think we'll be able to just run a screenshot, be able to to get that. But I do want to see if we can just one shot majority of this and see how how it does. Now let's go ahead and do the prompt in here. So let's do files and folders. We have our image here. All right. So it's actually asking which collections do we want entered on the home page. Let's do. Yeah. Number one

[00:07:52] which is I'll list them. And then how many product hero product sections pairs do you want representation for. File turn. Yeah. Let's go. Yeah. Full represent style. And then keep section. Know that one section that we just created. Let's go ahead and remove that okay. Where the collection is in here. Awesome. So I recognize that it doesn't have any collections created yet in the back end. But I'm going to go ahead and create all four of those collections so you can actually connect them on the front. Okay. This took about eight minutes

[00:08:22] total. Obviously we sped up and paused. So you don't have to just sit here and wait, but it essentially just kind of created all these little sections just like her represent has on their home page. I do want to I'm very curious to see how this actually looks. So let's go ahead and go to travel five to see what this looks like. So let's go to our represent theme here. Let's refresh this and see the sections that are generated and some of the options that we have for each of these. So just at a glance right. This is a very

[00:08:53] very basic sections. So it's still used the actual horizon section. So it didn't necessarily create anything new. Looks like in here. Let me see this. New arrivals. We have a header collection title. We have you all button. And then it lets me yeah let's me select different collections which actually created those collections for me which is great. Now let's let's try to push it a little bit further and see if we can tweak things and make things happen just like they are here.

[00:09:27] So I do want to say, for example, this here at the bottom, the way that they have all these links and all these pages, I want to see if it can truly do this footer for example. So let's take just a screenshot of that footer area and see what we can do. Let's go ahead and copy that. And so we can just paste it in here I want to mimic this footer as close as possible I'm going to say because it does

[00:09:58] have that floating chat button. And I also want to say if the pages are not non-existing, it's interesting how yeah, I was able to I think just get the gist right of that screenshot of it's just yeah, hero Prada hero product. So it's a very somewhat straightforward basic basic sections. But there are some, some things inside of those that I think make it truly unique for representing. So I do want to see how it does the footer. And then we may go into the actual sections, get just a deeper screenshot of it

[00:10:28] and see how well it can actually recreate some of those things. All right. This one took a little bit longer I would say a total probably good 15 minutes a bunch of different allows to go through. But actually I'm going to create 18 plus pages because we didn't have any of those pages created in the back end. So let's see how this looks. My main concern here really with using strictly cloud cloud code is the the inability to visually see what's happening. Right.

[00:11:02] Like you're kind of I'm kind of giving it a screenshot and then saying like, here we go, you know, make it happen. And there's going to be certain things where you're going to have to kind of go back and forth quite a lot, you know, to, to make it exactly what we need to make it. So as you can see here, not the best not the best setup. It kind of I mean, it got all the things from the screenshot, which is great. Again, it created all the pages, which is amazing. They created all the menus automatically, which is amazing. So all of that, it's it's really good. But when it comes to getting it

[00:11:32] to look exactly how we need it to look, I think pasting it directly through cloud code may not be the best idea. Now, I do want to test one more thing, which is going to be using Claude design and seeing how maybe we can use cloud design in order to generate something a little bit more visual. And then we can send that to cloud code to make these changes live on the website. So let's go ahead and check that out I real quick. If you are running a Shopify clothing brand and you want our team to look at your store and tell you where you're

[00:12:03] losing conversions, there's a link in the description down below. It's a free strategy call. We do real audit. Just generally useful information for your frame. Now we have the ability to do Claude design. So I'm here on the actual browser because the cloud closes on doesn't show up on the on the application itself. And so if we go in here to cloud design, you'll see that I've done essentially the same thing that we tried to do with cloud code. But I give it a little bit

[00:12:34] more sophisticated prompt in here to try to match everything along with the actual sync screenshot that we had before. And part of the the actual, the actual prompt is the ability to hand it off to cloud code for Shopify theme implementation, to see if we can actually get this to be exactly what what we needed to be. Right? So at a glance, this actually gives us a visual representation of what the prompt right. Everything that it worked on.

[00:13:07] So we can now technically make tweaks and changes to to this which is which is great. So as you can see we have we can do tweaks, comments, we can edit, we can mark up things. It's really get it to be exactly what we needed to be before we technically shipped this directly with with cloud code. Now, because we have this in here, let's see, without having to do any editor anything like that, I do want to see if we have the ability to essentially move this over into Claude code, essentially. Okay.

[00:13:40] So let's look if we click here on the component tree, we'll see everything that cloud code may need. Okay. Now for the handoff. There are two two ways we can do this. If you want you just prompt it and it will give you sort of like the package for the handoff that you need. You could also go here to the very top, click share and then do the handoff to cloud code. So let's try this. Let's copy this command and see if this works. Let's open up our cloud code.

[00:14:13] Let's do do new session and let's paste that in here. And then let's give it a little bit more instruction. Implement the page. 002 or horizon v2 which I created just a brand new version of the theme, just so we can compare and see what this version can look like. All right. So we have to try something a little bit different. The first route didn't work, so I just made sure to include within this prompt

[00:14:46] the fact that we want to make these changes on my actual Shopify store. Now, it gave me an error here. So we're going to try to use and upload the file. So we're going to go back to downloading this as a zip and then uploading it that way and seeing if that gets us a better result. So let's do we're going to upload the file. Then we open up the let me go ahead and do all of the files. Our guest the helm for HTML,

[00:15:16] do those components. All right. So after hitting this allow like 20 times. And about 20 minutes later it looks like we have everything near constructed. So let's double check how this looks on the live theme. Exit out of here and see our horizon V2. All right. So I will say definitely slightly different. It does look like

[00:15:47] maybe everything got sort of dumped into one single section called the Represent Home page. It still gives us the ability to edit a lot of these things. And technically, yeah, everything in here is essentially what we would need in order to. So let's just see, for example, let's just do home page say there we go. So yeah, technically, yeah, it made all the changes that we needed to in here super interesting. And it did capture all of the elements from what we were able to design

[00:16:23] right within the cloud design. So I will say, I think I've ever to compare the two routes that we took today using claw design would definitely be my go to. Obviously, there's still some tweaks that we need to make to throughout this whole process, so there's definitely going to be a part to of this video in order to make this the best version of this available, there's still a lot that's missing. I will say that, but I do think out of the two things that we did today using the Claw design

[00:16:54] and then from this actually finalizing images, finalizing products, adding the tweaks written here will be the way to go in order for you to see something ahead of time before hitting polish. Now, what does this all mean for you? I think there's going to be three audiences that are going to be watching this, and let me tell you what to do, depending on which one you are, if you're a brand owner, you have a clothing brand. The math just changed right? On whether you can afford a real custom theme. Six months ago,

[00:17:25] a custom Shopify build was 15 to $50,000 or even more. Today, the structural cost of that build just dropped significantly, and the work shifts to brand strategy, to the photography, to conversion testing, which is a lot more exciting. I think the parts that actually move revenue in my eyes. So if you've been on a stretched Dawn theme or a $200 theme template, because a custom built, which is kind of out of the reach, I think that calculation is different now. And I would I would implore you to kind of get some get some quotes again.

[00:17:57] Now, if you're a Shopify developer, I would say don't panic. The agencies that figure out how to use this the fastest are going to eat the agencies that really don't. So your job just then disappeared. It just kind of moved up the stack. There's less time writing boilerplate sections, more time on actual architecture, performance, custom logic, and the things that actually require judgment. The developers who pair this with a strong conversion rate optimization and brand thinking are about to become extremely valuable. Extremely bad.

[00:18:28] Now, if you're an agency operator, you're probably already running this internally using cloud design for first pass mock ups before going into potentially Figma piping out designs into code for the structural liquid build, and then developers actually doing a little bit of customization performance, a little bit of custom logic, right on top of everything that's already been built. And it's not about doing fewer projects, it's about doing better projects. Right with with more passes, with faster turnaround, in more room for actual strategy work. I think at the end of the day, the tools are not going to replace the team.

[00:19:00] They're replacing the boring parts of the team's job. Now, the reason I'm putting out videos like this isn't because AI is going to replace anyone. I don't think it is. I think our designers or developers are still the reason themes in general just ship clean, right? There's got to be taste, judgment and craft, I think. I think those are going to be some of the things that are going to sort of like writes to the top. The tools, I think, just got things to move faster. And if you are a brand owner who has been maybe priced out of good design or good development, or you're an operator trying to move faster, or you're just here

[00:19:30] because you like seeing how the sausage gets made, like you've got more leverage today than you had six months ago. Use it. This is this is useful for you. Then I want you to subscribe. We do builds. We do teardowns. We're always looking for new ideas for videos, for Shopify, for AI. So if you took something out of this video, I implore you to subscribe. Leave a comment down below. Let me know what you're going to do next with with this whole setup, I would love to hear and see what you do. And if you are new here, you haven't seen any of our other videos.

[00:20:02] I would definitely implore you to check out this next one here.
