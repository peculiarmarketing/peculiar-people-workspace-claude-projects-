# Claude Code + Shopify: I Built a Custom Theme Section in Minutes (Free Code)

- URL: https://www.youtube.com/watch?v=tXkpsim6sfI
- Channel: Andrew Beauchamp 
- Published: 2026-09-25
- Length: 8:01
- Views at fetch: 38
- Fetched: 2026-10-03 with yt-dlp (creator captions), file tXkpsim6sfI.en.vtt
- Coverage: FULL TRANSCRIPT from captions. NO FRAMES: video download was blocked in this session, so on-screen code, settings and commands were not seen. Auto captions can mishear technical terms.

## Chapters

- 0:00 Intro
- 0:12 The idea
- 2:16 The first build
- 4:12 Quick add
- 5:11 Make it yours
- 7:13 Install it yourself

## Description

```
I used Claude Code to build a custom Shopify theme section in minutes, no coding. The example: a lookbook from Classic Six that I loved, where you click a look and every product in it pops up. I rebuilt it and made it better. Shoppers can pick a size and add to bag right in the popup, without leaving the lookbook.

It's one free file that works in any Shopify theme. Get the code here:
https://github.com/BeauchampAndrew/shopify-lookbook-gallery

Chapters
0:00 Intro
0:12 The idea
2:16 The first build
4:12 Quick add
5:11 Make it yours
7:13 Install it yourself

What it does
- Grid of looks. Click one to see every product in that look
- Quick add: choose a size and add to bag without leaving the page
- Every look has its own link, so emails can open a specific look
- Edit looks, photos and products in the theme editor. No code needed

Install
1. Copy sections/lookbook-gallery.liquid from the repo
2. In Shopify, go to Edit code - Sections - Add a new section and paste it in
3. Go to Customize - Pages - Create template and add the Lookbook gallery section

Using Claude Code or Cursor? Point it at the repo. The AGENTS.md file tells it how to install and customize the section.

Inspired by Classic Six's S/S 2026 lookbook.
```

## Transcript

[00:00:00] All right. In this video, we are going to be taking this really, really cool, unique lookbook idea that I saw from a brand. And we're going to recreate it for ourselves. What makes this lookbook so cool is when you click on it, it actually brings up all of the featured products in here. And then from here, you can click right onto it and it'll take you to the page. I think the one thing actually that could be improved, there's actually kind of two things. There's a kind of thing you should open in a new tab. On mobile, that can be a lot. Or the other thing that I would like is if a little pop -up came up, like the little

[00:00:33] preview shops that sometimes show up, and you can just view the product information right from there. Because let's say you wanted to add this blazer and these earrings. You know, you're clicking here you're coming here, and now you're doing this. You're going to get lost. And then you're going to have to go back and then come back to this and then go to this one. Right? So it's just kind of a pain if you want to add multiple products. And obviously part of what makes it so great is that somebody can add multiple products to there. But overall, I just love this. I've seen a lot of brands struggle with building good lookbooks where they have to merge a collection

[00:01:06] specifically for something that they're doing. And it's very hard to showcase multiple ones. The way that I actually saw this was it was inside of an email. So they had included the let's say it was this girl here. And the link took you directly to this pop -up page, right? Because you can actually copy and paste it. So it'll pop up with this already populated, right? And so it took the person right to this. And I think it was just so well executed. And I've never really seen anyone else do it like this. So I really want to rebuild

[00:01:37] this and then just kind of give the code away. So by the end of this, you'll either know how to do it yourself or if you just want to click the GitHub repo below you'll be able to copy the whole code in there. So what I've done is I've just gone and created a development store with just a sample clothing brand to pull in a bunch of products. I just uploaded some things in here and we're just going to start by giving Claude here our lookbook. I forgot to add the link there so go ahead

[00:02:12] and drop that in. Okay. So now we have the lookbook built super, super easy. So we're just going to test it out here by adding a page, going to lookbook and then just grabbing the template here. Okay. We're going to go ahead and make it visible. You can view it. Oh yeah, it's already working great. So this is awesome. It's already working. This took just a couple of minutes to do. Now just to check, I want to view this

[00:02:45] real quick on mobile. Oh, nice. That's pretty good, actually. I like how that comes up from the bottom. This is great. I'm actually really impressed with how this turned out. I know we're missing images here. Oh, this is so good. I'm really impressed at how quick this came together. Okay, so really quickly, we found some of our – just some images for the lookbook. So this is one thing that Claude can't do. So we just need to go into content, files

[00:03:18] and then we can pull in these Lookbook files. Great. So now that's how we can just pull those in once you have them. And it should be able to figure out how to apply those in. And then we can start to see how this build looks here we go. Okay. So obviously not perfect, right? You because it's just pulling these images. But this is still pretty awesome. The fact that you can just scroll through these as well. And let's just look on

[00:03:50] mobile here, how it looks. They're a little small, but it still looks pretty dang good. And then you can just click through. Okay. So there's actually still a couple of changes that I want to make because I would really rather have it open up the modal that would allow, like the quick select modal. So I'm going to see if I can change this around and get it to do that for me instead. Okay. So we went ahead and added it in. I honestly think it looks even better. Like this is perfect. Right. So you can do medium add to bag. And then

[00:04:20] like if you wanted this one, you can add it to bag and it's, it's giving us this little update here. The reason that we couldn't do like a quick pop where it shows all of the product information, because I'm trying to build this for multiple stores to kind of fit that can break, but this should work across. So we've even got our view bag here. It looks a little funny with this overlay here, but this is pretty dang good Let's just check on Mobile and see how this displays It's a little small But I don't know this still looks pretty dang good Let's see if we can fix this kind of funky

[00:04:53] overlay that's happening But overall, this is looking really really good and really easy. So next, I'm going to run through how you could just set this up yourself and how you can edit it like on an in an ongoing way All right. So coming back to this, we can see now that we've fixed that overlay. So everything looks really really clean now. So the other thing that I wanted to run through is how you would actually edit this. So there's a couple of different ways. Now, if you're comfortable, you can

[00:05:24] just do it inside of Claude Code. The other way that you can do it is coming into your online store and then coming into the editing. Theme itself and then finding this page which would be here pages and then you go to your lookbook here and then you would actually be able to just edit everything right here so you can just change the look photo you can change the products right so change products or just you know click on one and and reorder whatever you need to do here so you can kind of reorder the order of Or yeah, you can change the products right here.

[00:05:55] So super super easy You can change the name of them The look any other things that you want to do I can all just be done right inside of the actual theme editor So if you feel a little less technical This is all doable so you can add looks and continue to add additional looks if you wanted more and or less Delete them or do any of the things in here with this overall section So if you wanted it to be the let's just say winter 2026, boom, you can go ahead and do that. You can bump this up if you wanted it to

[00:06:27] be bigger. So there's a whole bunch of things that you can just do inside of here without really being super technical So it makes it really easy. If you are more technical, then you can just connect your theme to Claude Code and just have it go ahead and do all of that for you. So, yeah, we basically took the whole idea from this lookbook right here and went ahead and turned it into our own really, really pretty awesome lookbook page that I'm pretty stoked about. We even made some improvements, so I think it looks really good. Again, I just really love the fact that

[00:06:58] you can just quick select and add these. Such a cool feature and I really think makes a big difference in just the functionality and the usability So this is looking great. If you want this code it'll be in the GitHub repo below If you are less technical, I'll quickly actually just run through that as well If you want this but don't really feel comfortable doing something like this go into edit code And then in here you can create a new template

[00:07:29] if you want to create this yourself and maybe you feel a little less comfortable, you can go ahead and copy this JSON in you just by going to new page and then just page.lookbook.json. That will bring in the template. And then from there, you will have to copy in like the different sections because these These are actually how this whole thing gets built So this was kind of our lookbook copy and build. So thanks for the time. Bye.
