URL: https://community.shopify.com/t/claude-code-produced-html-beginner/631503
JSON: https://community.shopify.com/t/631503.json
HTTP status: 200
Fetched: 2026-10-03 via curl (Discourse topic JSON)
Title: Claude code produced HTML (beginner)
Created: 2026-06-07T12:59:26.412Z
Last posted: 2026-06-17T07:50:07.232Z
Posts: 10  Views: 598
Category id: 308  Tags: []
Accepted answer: null

---

## Post 1 by retrodesire at 2026-06-07T12:59:26.564Z
hi i asked claude to produce HTML code but im slightly confused where bouts im entering the code i know i have to go into theme editor>edit code but this is where i get confused, does the code go at the top of the pages or is there anything of the original code to be dleted?

many thanks

## Post 2 by Maximus3 at 2026-06-07T13:20:19.398Z
That last part… don’t delete stuff if you’re not absolutely sure it needs to be deleted.

I would seriously consider not doing anything until I have a full understanding of what the theme files do, how the theme is structured, how the files and parts are connected.

## Post 3 by tim_tairli at 2026-06-07T13:21:15.045Z
What is this code for?

Can you share it here?

What theme you’re using?

Unless you’ve instructed AI specifically, the code may be a complete HTML page, while you need a fragment.

You may want to instruct AI specifically to create a Shopify section, block, or fragment of HTML/Liquid code to paste it into “Custom Liquid” section, depending on your goal.

## Post 4 by retrodesire at 2026-06-07T13:41:37.273Z
i asked claude to design each page my current theme is premium www.retrodesire.net

## Post 5 by Maximus3 at 2026-06-07T14:13:15.920Z
A Shopify theme is structured very different from full HTML files, which have <html> <head> and <body> tags, so if that’s what you’re doing, it will not be compatible and will most definitely break things.

Shopify pages are structured as a json template file, liquid section files, and rendered liquid snippets, with the Page being the data that gets injected at read time.

So it really depends on what exactly you’re trying to do. Are you adding a new section to an existing page, replacing a full page layout, or building something from scratch?

## Post 6 by retrodesire at 2026-06-07T14:15:48.802Z
replacing a full page layout

## Post 7 by retrodesire at 2026-06-07T14:20:52.512Z
claude is building the liquid files

## Post 8 by Maximus3 at 2026-06-07T14:45:37.868Z
Ok but you need to understand that even though you want it to be a full page layout, it still needs to be saved as a Section file.

Still not advisable but if everything is correctly formatted:

So if it’s truly a Liquid file, go to the code editor, right click on Sections and create a new file. Name it, and put “.liquid” at the end. The new file will open. Make sure it’s blank. Then paste your Liquid code and save. It must have a {% schema %} block at the bottom.

Once that is done, you can go back to the theme editor, create a new Template, and add the section and remove any old ones you don’t want.

Then you can assign the Page to the new template in Admin.

## Post 10 by Choong at 2026-06-08T06:05:46.044Z
Is there any specific design or requirement that couldn’t be fulfilled by any Shopify theme?

If you are just looking for a specific feature, potentially you can get Claude to code it as an embeddable static html and just embed that specific part (using content editor in your page / blog).

Highly not recommend coding the whole page, or the whole site. Wherever / whoever gives you the idea to do this, maybe you should consult with them before going at it.

## Post 12 by bchen27 at 2026-06-17T07:50:07.232Z
the answer depends on what the code is for. if claude gave you a full HTML page (starts with ), that’s not going to work directly in shopify because themes use liquid templates, not standalone HTML files. you’d need to ask claude to convert it into a shopify section instead.

if it’s just a snippet of HTML like a banner or styled block, go to online store > themes > customize, then add a “custom liquid” section wherever you want it on the page. paste the HTML there. don’t touch the existing theme code files unless you know what you’re doing, one wrong delete and you can break the whole layout.
