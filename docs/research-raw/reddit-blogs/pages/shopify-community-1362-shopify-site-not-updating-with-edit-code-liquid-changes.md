URL: https://community.shopify.com/t/shopify-site-not-updating-with-edit-code-liquid-changes/1362
JSON: https://community.shopify.com/t/1362.json
HTTP status: 200
Fetched: 2026-10-03 via curl (Discourse topic JSON)
Title: Shopify site not updating with Edit Code liquid changes
Created: 2018-05-05T02:50:44.000Z
Last posted: 2023-12-18T13:43:27.000Z
Posts: 15  Views: 535
Category id: 133  Tags: []
Accepted answer: null

---

## Post 1 by Try431 at 2018-05-05T02:50:44.000Z
I’m trying to make a simple change to my site in my list-collections.liquid page. However, no matter what I change and Save, I’m not seeing the changes reflect on the site. At first I thought maybe there was a built-in delay, but changes made with the higher level template editor are instantenous, so what’s the deal?

For clarity, I’m just trying to change the following collection.title output to be an href tag that a customer can click on to navigate to the respective collection page

<div class="col-md-12">
			   		<h3 class="custom-font">
						{{ collection.title }}
					</h3>

I’ve messed around with duplicating the output, so there’d be two or three collection.titles, changing the header tags, etc. but nothing is reflected on the site 

Thanks so much for any help!

(Also, does anyone know what the purple dots next to certain .liquid files signify?)

## Post 2 by Jason at 2018-05-05T17:03:38.000Z
The dots indicate a changed file.

I would assume that you’re not changing the right seciton of code. A bit more context would help - a link to the page and name of the theme in use would be good starting places.

Also knowing what file you’re making those changes to would also help.

(moving this to the design section as this post doesn’t related to the Script Editor)

## Post 3 by Try431 at 2018-05-06T00:51:12.000Z
Hey Jason, thanks so much for the reply!

The website is soltribecollective.com and we’re using the Envy theme.

You were right - I was looking at the wrong code. Turns out I needed to be looking at the collection.liquid section, not list-collections.liquid. However, I’m running into a strange issue that perhaps is arising out of my ignorance about how things work together.

I’ve managed to change the section header on the main page to a link:

      <div class="title-bar custom-font">
        <h2><a href="{{ section.settings.link }}" title="{{ section.settings.link | escape }}">{{ section.settings.title | escape }}</a> </h2>
      	<div class="clear"></div>
      </div>

However, the url that populates is blank, which means the section.settings.link isn’t being grabbed from my settings_data.json file (I’ve added a ‘link’ attribute for each of the collections):

​
      "collection": {
        "type": "collection",
        "settings": {
          "title": "Sunnies",
          "show-vendor": false,
          "hover-effect": "second-image",
          "collection": "sunnies",
          "grid": "4",
          "rows": 3,
          "link": "[https://soltribecollective.com/collections/sunnies](https://soltribecollective.com/collections/sunnies)"
        }

​

The page source reveals that the href which is populating is just an empty string for some reason. Any suggestions as to what’s going on? I’ve tested it by directly putting in the string for the desired site, and that works fine, but of course I want each section link to be different.

Thanks!

## Post 4 by klatchdesign at 2019-09-13T20:47:18.000Z
I’m also experiencing it not updating. I’m editing the code for ‘page.about.liquid’ and the code hasn’t updated. Could you help me with this?

Site is klatch roasting.com using an edited version of ‘minimal’ theme.

## Post 5 by DymaxionGroove at 2020-03-23T17:23:13.000Z
I’m experiencing the same problem. This issue seems to have been around a while.

## Post 6 by Ciodensky at 2020-04-07T09:38:29.000Z
I am experiencing the same problem.. Shopify is not updating no matter what I do. I already deleted and the file and it still not updating my site despite the .css file is deleted already.

## Post 7 by DavidSousa at 2020-04-20T02:43:44.000Z
I’m too having the same problem, one way around i found was simply add an 
 tag to the html just so it knows something changed besided css and save/refresh. Then just delete the h1 u just created. It fixed for me!

## Post 8 by Canna at 2020-05-19T11:41:01.000Z
Hi

I use Prestige theme.

I have edited code and even taken it out from theme.js and cart-template.liquid without seeing any changes on the homepage. This is the first time that I have tried where code changes were not reflected.

Is it because of the theme, Shopify or me:)?

## Post 9 by TincyTincy at 2021-01-03T14:18:12.000Z
Judging from the replies in this thread, this seems to be a somewhat common issue. Anyone found a solution?

I’m operating two shops. In one, I can make changes to all the .liquid files in the code editor, and they take immediate effect, in the other one, I can change anything… no effect at all to the front-end. No plugins, default Shopify themes…

Anyone have an idea what might be the issue?

## Post 10 by NATURALZING at 2021-01-28T01:43:21.000Z
Same issue. Trying to update customer.login.liquid register link

## Post 11 by gb2world at 2021-02-02T04:58:51.000Z
Just in case anyone else is making the same mistake I made: Make sure you are viewing the same theme that you are updating. I had been previewing another theme in the morning, then came back later in the day and neglected to turn that preview off. It was perplexing that I could not observe the changes I was making to the liquid files. Then I noticed that I was previewing a different theme!

## Post 12 by ahsanrao at 2021-05-06T06:59:50.000Z
Thank u soo much gb2world.

I made the same mistake but didn’t notice what’s the issue.

You just save my day.

## Post 13 by Boneoh at 2023-05-11T22:37:09.000Z
Same issue here. This is horribly frustrating.

## Post 14 by andrea76 at 2023-12-18T13:42:32.000Z
Same. I’ve tried making multiple different development stores, trying different themes, and making basic changes in each and I do not see them live on my site…there seems to be no Shopify support for this and it’s very concerning.

## Post 15 by andrea76 at 2023-12-18T13:43:27.000Z
I’ve been updating the correct theme’s liquid files but am still not seeing the changes.
