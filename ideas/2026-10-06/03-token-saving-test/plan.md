# Test plan: are you actually running out of Claude usage?

Verdict: **Plausible.** Six reels in the 4:02 PM batch make the same pitch: stop burning through usage limits.

| Reel | Trick | What the reel actually showed |
|---|---|---|
| @itstundeanthony | "caveman" skill: Claude answers in compressed shorthand | His own test: output tokens fell from about 4,000 to 2,800 on one task and from 4,900 to 2,400 on another. Single runs, output tokens only. A clip in the reel claimed 65%; his own numbers were 30% and about 51%. |
| @davidiya.co | Ponytail (shortest working code), Graphify (codebase as a knowledge graph), Addy Osmani's Agent Skills | Ponytail's README claims 54% less code and 22% fewer tokens on one benchmark (n=4). Claimed, unverified. |
| @noevarner.ai | "ICM architecture": reorganise files so Claude reads only what it needs | No repo, paper or full name shown. Claims a cost drop to "a fifth or a sixth". Unverifiable as given. |
| @thomas.lentine | Fable writes specs and reviews; cheaper Opus subagents do the work | Concept only; the setup is withheld behind "comment TOKEN". Claude Code already supports subagents with a chosen model. |
| @adilet.fndr | Karpathy-inspired CLAUDE.md (4 rules) and "I Have ADHD" (answer first, no preamble) | Repo cards shown, but owners disagree between the card and the install command. |

## Why only Plausible

Nothing in BRAND.md or the workspace says usage limits are a problem, and BRAND.md section 16 says building more is not the bottleneck anyway. A fix for a problem you may not have is not worth a change to a working setup.

Some of this is already true here. CLAUDE.md is short and specific, every project has a README and HANDOFF, and skills load only when used. That is most of what "ICM" and the Karpathy file are selling.

## Cheapest test (5 minutes)

1. **Open the usage panel** in the Claude desktop app (or run `/usage` in Claude Code) at the end of a normal week.
2. **If you are not near the limit,** close this idea. Nothing to do.
3. **If you are,** look at the "What's using your limits?" breakdown, which @itstundeanthony's reel shows exists. Fix the biggest line first. A skill or MCP server eating a large share is a more direct fix than any of these tricks.
4. **Only then** consider "caveman" for a week, on chat-style work only and never for customer copy. Compare the usage panel before and after. Read its SKILL.md before installing it; it is a single text file.

## Do not do

**OmniRoute** (the fourth item in @davidiya.co's reel) routes Claude Code traffic through other providers to dodge limits. Your code and files would go to unknown third parties, and it likely breaks the terms of your Claude plan. This is covered under item 6 in the digest.
