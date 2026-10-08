# New Shopify AI Toolkit: Claude Code Setup + Demo (April 2026)

- URL: https://www.youtube.com/watch?v=ptnWksC9TXY
- Channel: UNKNOWN (presenter's store is "lifetropics.com", account "Jons Nutrition", per the video)
- Length: about 7:45 (last scene timestamp). Upload approx 2026-04-12 (from search result "days ago" math, not verified).
- Tool: Higgsfield video_analysis (job dae1c3fd-3c15-4df0-a2e7-8c9735e507cd), completed 2026-10-03. Output is a scene list with an "audio" field (machine transcription, may be condensed) and a "visual" field (machine description of the frames). This is NOT a verbatim transcript and there are no image frames saved. Treat quotes as close paraphrase.

## Scenes (audio field verbatim from the analysis; visual field summarized)

0:00-0:09. Audio: "Shopify have just released the AI Toolkit, which is really cool and allows you to manage your store using Claude. I've tried it, it works really well, so let's do it together now." Visual: social post about the Shopify AI Toolkit; presenter in picture-in-picture.

0:09-0:23. Audio: "So, first we're going to go to the Shopify AI Toolkit page on the developer documentation. And then there's these two sets of instructions here of how to install it. So I'm going to be installing it with Claude Code and it gives you the code to copy." Visual: shopify.dev AI Toolkit page, "Install with a plugin" section, Copy button.

0:23-0:47. Audio: "So first I'm going to open the terminal, I'm going to launch Claude, dangerously skip permissions. I launch Claude this way so that it doesn't keep asking me about permissions and things like this. So I've initiated Claude and now I'm going to paste in that command: plugin marketplace add shopify-ai-toolkit. So it's successfully done that." Visual: terminal; pasted marketplace-add command; success message.

0:47-1:05. Audio: "And now there's the next command, so install the plugin. ... install for you, install for all collaborators ... So I'm going to install it for you, so user scope." Visual: plugin install command pasted; scope options.

1:05-1:59. Audio: "... Now if I click on reload plugins ... List out all of my active products on Shopify. ... It's asked me if I want to run the query directly against the store ... what is my store URL". Visual: browser opens for authentication.

1:59-2:31. Audio: store handle pasted, "it's now authenticated ... listing out all of my active products." Visual: "Authentication succeeded" page; product table in terminal.

2:31-4:00. Analytics questions (revenue, AOV, conversion rate). Visual: second authentication step for analytics access; results table.

4:00-5:35. Customer lifetime value computed from ShopifyQL component metrics.

5:35-6:27. Audio: "... can it also start actually editing the website design itself? ... edit the homepage title 'Science-Backed Supplements for True Results' and change it to ... 'Science-Backed Supplements for Real Results' ... normally I'd have to do that within the theme editor."

6:27-7:24. Audio: "... It's going to find the main theme ID, it's going to read the template, find the correct section and it's going to update the section. I've just skipped ahead but you can see now it's actually done this ... and it's applied the update to my live theme. ... I'm going to refresh it and you see it's now edited the actual copy on my theme." Visual: terminal shows theme update; browser refresh shows new headline.

7:24-7:45. Call to action.

## Notes for the briefing
- Shows: AI Toolkit plugin install in Claude Code; Claude launched with permission prompts skipped ("dangerously skip permissions"); a text edit written straight to the LIVE (main) theme, with no duplicate theme, no git, no preview, and the edit step skipped over on camera.
- This is a working example of the "editing the live theme directly" failure mode, presented as a success.
