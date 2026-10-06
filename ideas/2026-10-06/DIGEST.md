# Idea inbox, Tuesday 6 October 2026

2 new (19 reels, read as 6 ideas): 1 useful, 0 beneficial, 2 plausible, 3 waste.

This was a test run, triggered by hand in the afternoon rather than at 2 AM. The second item is 19 links sent within a few minutes, so it was split by topic below. The 3:53 PM "web design" reel is the same sponsored Manus script as one reel in the batch, so it is judged once, under item 4.

## 1. Catch the "AI-made" look before a customer does  ·  Useful
From: iMessage note to self, saved 4:02 PM. Reels from @millee.md, @zanderwhitehurst, @lincolndevine, @adam_ha_yes.
What it is: Checklists of what makes a site look generated: centred stacked text, emoji headings, gradient text, fade-in on scroll, buzzword copy, em dashes. Plus form bugs, like double submits and raw error text.
Why this verdict: A premium store with zero reviews lives or dies on looking established, and some of this list already is house style (no em dashes, purple gradient removed). The store-cro-audit skill can absorb it as eight new checks and four form checks, plus a one-page DESIGN.md so new pages avoid the same tells.
Made: [plan](01-ai-look-checklist/plan.md)
Next step for Evan: Approve the plan in a session, or strike any rule first (the buzzword rule is the most judgement-based).

## 2. Third-party design skills for Claude Code  ·  Plausible
From: iMessage note to self, saved 4:02 PM. Reels from @nateherkai and @nick_saraev.
What it is: Install design skills (Taste Skill, impeccable, Emil Kowalski's, Vercel Web Design Guidelines) and a screenshot loop so Claude's pages stop looking generic.
Why this verdict: The store is a Shopify theme, so these React-oriented skills only touch mockups and any future custom page. The screenshot loop already exists in store-cro-audit, and neither reel shows a repo link, so nothing can be vetted from them.
Made: [test plan](02-design-skills-test/plan.md)
Next step for Evan: Do item 1 first. Then, if you want, try the Vercel audit skill on one product page after reading its source yourself.

## 3. Stop burning Claude usage  ·  Plausible
From: iMessage note to self, saved 4:02 PM. Reels from @itstundeanthony, @davidiya.co, @noevarner.ai, @thomas.lentine, @adilet.fndr.
What it is: Tricks to cut token use: the "caveman" terse-output skill, Ponytail, Graphify, file reorganisation, a Fable-plans and Opus-works setup, and a Karpathy-style CLAUDE.md.
Why this verdict: Nothing says you are hitting limits, and the workspace already does most of what these sell (short CLAUDE.md, per-project READMEs, skills that load on demand). The one measured result, caveman, cut output tokens by 30% and 51% in single runs (claimed in the video, unverified).
Made: [test plan](03-token-saving-test/plan.md)
Next step for Evan: Check the usage panel at the end of this week. If you are not near the limit, drop this.

## 4. Animated component libraries and Manus  ·  Waste
From: iMessage note to self, saved 3:53 PM ("Note for web design") and 4:02 PM. Reels from @vibecode.rob, @kaithevibecoder, @setupsai, @kevin.snippet.
What it is: Libraries of animated components (Motion, Kokonut UI, Originkit, Magic UI, SmoothUI, RetroUI) and Manus, an AI site builder with one-click publishing.
Why this verdict: These are React and Tailwind components, and the store is a Shopify Liquid theme, so they do not drop in. Heavy motion also works against "premium, reverent, understated" (BRAND.md section 5) and against audit rule H14. The Manus segment is a paid ad (#manuspartner #ad, posted word for word by two accounts), and using it would mean leaving Shopify.
Made: Nothing, see reason above.
Next step for Evan: None. Overrule if you were planning a custom page outside the theme.

## 5. Obsidian second brain and brain-response research  ·  Waste
From: iMessage note to self, saved 4:02 PM. Reels from @chase.h.ai and @jens.heitmann.
What it is: An Obsidian vault with a master index so Claude can navigate your notes. And a stack (Apify scraping, Meta's TRIBE v2 brain model, Modal GPUs) to predict which of your reels the brain responds to.
Why this verdict: The research library is already structured and verified (119 temples, BRAND.md section 12), and the workspace already gives Claude a clear path through it. The brain-model stack needs a back catalogue of your own reels to analyse, and Peculiar People has not posted yet (section 16). Its headline correlations come from 16 reels.
Made: Nothing, see reason above.
Next step for Evan: None. The brain-model idea could be worth a second look once there are 50 or more posted reels.

## 6. Giant setups, skill finders and model routers  ·  Waste
From: iMessage note to self, saved 4:02 PM. Reels from @bengusberg, @benkimball.ai, @adilet.fndr, @davidiya.co.
What it is: "Everything Claude Code" (68 agents, 292 skills, install by pasting a repo link into Claude); an unnamed skill that searches 700,000 skills and installs them; Superpowers; Claude Octopus (sends your task to 12 other AI providers); OmniRoute (routes Claude Code through 150+ free providers).
Why this verdict: Each one installs a large amount of unreviewed code or instructions into a workspace that holds your store's API tokens, or sends your files to third parties. The skill finder's name is withheld behind comment bait, so there is nothing to vet. The workspace's curated skills are the point; a 292-skill bundle would bury them.
Made: Nothing, see reason above.
Next step for Evan: None. If one specific skill from these ever looks worth having, bring the single repo to a session and vet just that.

## Couldn't see

- `instagram.com/p/DdtaUOCNmNs` is a photo post, not a reel, so no video came through and only the link was saved. Nothing about it was judged. If it mattered, text a screenshot of it.
- Every link also arrived with iMessage's link-preview card, which the collector logs as "attachment not downloaded" or "file type not processed". Those are noise, not lost content. The collector should skip them (`.pluginPayloadAttachment` files); that is a small fix for a session, not for triage.
