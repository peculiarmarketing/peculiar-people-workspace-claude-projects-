URL: https://community.shopify.com/t/urgent-need-help-removing-malicious-code-injections-jsdeliver-cloud-brandagents-js-from-shrine-theme/600137
JSON: https://community.shopify.com/t/600137.json
HTTP status: 200
Fetched: 2026-10-03 via curl (Discourse topic JSON)
Title: Urgent: Need help removing malicious code injections (jsdeliver.cloud & brandAgents_js) from Shrine Theme
Created: 2026-04-01T04:37:16.061Z
Last posted: 2026-09-22T11:22:34.471Z
Posts: 10  Views: 738
Category id: 211  Tags: [{'id': 4021, 'name': 'troubleshooting', 'slug': 'troubleshooting'}, {'id': 5030, 'name': 'shopify-theme', 'slug': 'shopify-theme'}, {'id': 2135, 'name': 'third-party-apps', 'slug': 'third-party-apps'}, {'id': 1775, 'name': 'liquid', 'slug': 'liquid'}, {'id': 5317, 'name': 'cyber-security', 'slug': 'cyber-security'}]
Accepted answer: null

---

## Post 1 by dandychen at 2026-04-01T04:37:16.221Z
Hi everyone,

My store (BuroLipo, using Shrine Theme) was recently compromised by an unauthorized app called “Product Network.” While I have uninstalled the app, my site is still showing malicious script injections and phantom products from other stores.

The specific snippets I need to locate and safely remove are:

- 
References to shopify.jsdeliver.cloud (fake Shopify CDN).

- 
A block or script named brandAgents_js or frontendInjection.js.

- 
Unauthorized scripts originating from azurefd.net.

I am seeing these in my page source, but I am struggling to find the exact Liquid file or Snippet where these are being injected.

Technical Details:

- 
Theme: Shrine

- 
Issue: Cross-store product hijacking / Malicious JS injection.

Can someone guide me on where these scripts usually hide? Is it typically in theme.liquid, or should I be looking for specific .js assets or hidden snippets?

Any help would be greatly appreciated as this is affecting my checkout and store reputation. Thank you!

## Post 2 by tim_tairli at 2026-04-01T04:46:17.963Z
Share a preview password so we can see for ourselves.

Do you see these when do “View code” (then it’s rendered on the server) or when “Inspect elements” (then it can be added by another script).

If it’s in theme code, then you should be able to use global search in theme code editor to find these references:

Screenshot 2026-03-31 at 3.06.21 PM534×311 15.6 KB

## Post 4 by dandychen at 2026-04-01T05:16:07.128Z
Thank you for your insight. I want to clarify the situation:

I managed to capture the malicious behavior on my mobile device earlier. Although the issue is intermittent and hard to replicate now, I have saved the full page source from that session.

Here is what I found in the code during the hijacking:

- 
Cross-Store Injection: The source code contained numerous product links with -remote suffixes (e.g., /products/...-remote). These products belong to other stores like “Bisoulovely,” not mine.

- 
Malicious Domain: Shopify Support confirmed that the script loading from shopify.jsdeliver.cloud is a major Red Flag and is not a legitimate Shopify domain.

- 
Method of Injection: These scripts and products appeared in the “Inspect Elements” view during the incident. Since I have now uninstalled the “Product Network” app, I need to ensure there are no lingering Script Tags or hidden Liquid snippets that could trigger this again.

My preview password is zhenu2025. Even if the phantom products aren’t visible right now, could you please help me check if there are any suspicious ScriptTags or Web Pixels still registered in the background that might be calling that jsdeliver domain?

I want to make sure my store is 100% clean. Thank you!

## Post 5 by tim_tairli at 2026-04-01T06:34:24.589Z
frontendInjections seem to be a part of clarity (or masquerades as clarity?)

At the moment I do not see anything suspicious.

If you still see unexpected elements, can you share screenshots?

<!-- BEGIN app block: shopify://apps/microsoft-clarity/blocks/brandAgents_js/31c3d126-8116-4b4a-8ba1-baeda7c4aeea -->

<script type="text/javascript">
  (function(d){
      var s = d.createElement('script');
      s.async = true;
      s.src = "https://adsagentclientafd-b7hqhjdrf3fpeqh2.b01.azurefd.net/frontendInjection.js";
      var firstScript = d.getElementsByTagName('script')[0];
      firstScript.parentNode.insertBefore(s, firstScript);
  })(document);
</script>
<!-- END app block -->

## Post 6 by PaulNewton at 2026-04-01T11:51:56.792Z
Just restore files before that time, or restore an external backup if you have proper procedures in place.

https://help.shopify.com/en/manual/online-store/themes/theme-structure/extend/edit-theme-code#roll-back

 dandychen:

-remote suffixes (e.g., /products/...-remote).

Without burning the time to untangle this those seem like [remote products, a shopify feature] which(Remote products and multiple merchant in checkout changes - Announcements - Shopify Developer Community Forums) which is supposed to optional; meaning you the merchant enabled it especially if there was a full blown app installed it literally , third party apps have to be authorized by someone with access to your store so they aren’t “unauthorized” someone gave it permissions.

In which case if it is remote producents then nothing to see here but unneeded hysteria from not taking the time to understanding the platform your business relies on.

contact shopify support DIRECTLY to discuss it:

 → https://help.shopify.com

## Post 7 by tim_tairli at 2026-04-01T12:00:07.956Z
Ah, Paul I’ve seen several time an app go rogue and all of a sudden redirect people to other sites.

Nothing prevents an app from doing stuff on your storefront which is different from what you’ve authorized  it to do.

## Post 8 by Maximus3 at 2026-04-01T13:55:28.117Z
None of this sounds suspicious to me. You haven’t said any malicious action was done, at all. Just because you say it’s malicious doesn’t mean it is. So, what is the problem here? Shopify Product Network, though I never heard of it before, is an app built by Shopify that puts or injects product blocks into your store (how safe could that be?). You Uninstalled the app, which means at some point you or someone who had access went into the app store and installed it. It didn’t magically sneak into your store. I can only imagine the kinds of crap people are installing. But you still haven’t said any bad happened… I see words hijacked and malicious but nothing that was actually done to make anyone think that’s what this is.

Azurefd.net is from Microsoft Azure, another app… and @tim_tairli pointed out the frontendInjection is from Clarity so that makes a lot of sense.

So it all just sounds like stuff you installed. If you wnt someone to come in and remove stuff, that’s one thing. But I see nothing malicious here.

## Post 9 by tim_tairli at 2026-04-01T14:11:56.437Z
Could also be a case like the old ones …

  
    
    
    
      Issue with developer downloading charging apps wihtout asking has anyone had this issue Shopify Discussion
    
  
  
    So today I noticed that a developer that’s well known in this community has snuck onto my account and downloaded a app that he must get money from without asking me. I went into my log and see he has downloaded it and authorized monthly payment has anyone else had this issue. This is a shopify partner quite disgusted.
  

or this:

  
    
    
    
      Localization position mobile version Horizon theme Ask & Offer
    
  
  
    I saw that you added the language switcher where I wanted to be it, but…. you also installed an app that I pay $99 dollars for today which I cannot find anywhere. The app is called order porter and is installed at the same time you were active. Have you any comment please?

## Post 10 by GhostAstra at 2026-09-19T09:29:33.137Z
@tim_tairli Fair pushback on a few points, but “it’s Azure/Clarity, so it’s legitimate” doesn’t actually clear it, that’s the reasoning attackers count on. Hosting malicious payloads on Azure, AWS, or other major cloud infra specifically because it’s trusted and rarely gets blocklisted is a well-known technique, precisely so a domain check comes back looking “normal.” The infrastructure being legitimate says nothing about what’s being served from it.

Same logic applies to “you installed it yourself so it’s not malicious”. Installed by someone with access isn’t the same as sanctioned by the store owner. That’s literally the pattern in the collaborator-account thread posted elsewhere on this board this month: access was legitimate, the action taken with it wasn’t.

None of that means this specific case is malicious, it might genuinely just be normal app residue, which happens constantly and looks alarming to anyone not used to reading it. But the way to settle it isn’t “the domain sounds legit” or “you must have clicked install”, it’s diffing the current live theme against a known-clean baseline (a backup from before any of this, or a fresh copy of the Shrine theme) and checking exactly what changed and what it does at runtime. Has anyone actually done that diff, or is this still going on domain names alone?

## Post 11 by josedrobles at 2026-09-22T11:22:34.471Z
Uninstalling the app usually does not remove what it injected. Two places to check first: theme.liquid (Online Store > Themes > Edit code) and any remaining App embeds, search the theme for ‘jsdeliver.cloud’ and ‘brandAgents’. If the snippet lives in theme.liquid, removing the app changes nothing.

Then check Settings > Custom data for the phantom products. Apps like this often create them as metafield-driven or unpublished entries rather than real products, so they do not disappear when the app is uninstalled.

Also worth generating a fresh API key/secret afterwards and checking Settings > Users for any collaborator the app added, since that is how the script normally gets re-injected.

If you want, I can look at the theme and tell you exactly which lines to remove before you touch anything. No charge for the first look.
