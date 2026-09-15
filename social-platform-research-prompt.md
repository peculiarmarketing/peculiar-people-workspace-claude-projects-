# Prompt: which social platforms Peculiar People should actually be on

Paste everything below the line into a fresh Claude Code session in the
`Claude Projects` folder.

---

I want an in depth, readable report, not a plan and not a one line verdict.
Every platform gets its own full writeup: what it is good at, what it cannot
do, who is actually there, and why. The report should end with a
recommendation, but the recommendation is the last section, not the whole
document. I want to be able to hand this to someone and have them understand
each platform on its own terms, not just see a tier list.

Two questions the report has to answer along the way:

1. **How much does breadth actually matter?** Is a two person, pre-launch brand
   better off on two platforms done properly or on six done thinly, and what
   does each extra platform really cost per week?
2. **What is each platform genuinely good at, and what can it not do?** Every
   platform gets an honest "cannot do" list, not just a pitch.

Cover at minimum: Instagram, TikTok, Pinterest, Facebook (page, Groups, and
Marketplace treated separately), YouTube (Shorts and long form treated
separately), Snapchat, X, Threads, Reddit, and LinkedIn. Add any platform that
turns out to matter for this audience and say why you added it. If a platform
is obviously wrong for this brand, say so in two lines and move on rather than
writing a full profile.

## Read these before you research anything

- `BRAND.md`, all of it. Sections 10, 13, 17 and 19 matter most.
- The First Sale Playbook artifact:
  https://claude.ai/code/artifact/948c2205-be6f-4200-9f45-078cc42359ed
- The posting rota artifact:
  https://claude.ai/code/artifact/b02e0e11-494c-48cf-8159-b4f011efec7d

Read the artifacts with the Artifact tool's `read` action. Do not guess at their
contents.

## What is already settled, so do not re-derive it

Four earlier rounds of video research produced these. Treat them as the starting
position. You may overturn any of them, but only with evidence, and you have to
say clearly that you are doing it:

- The brand is pre-launch with zero orders and zero reviews. Distribution is the
  only constraint. Product work is done.
- Feeds are interest media, not social media, so a post about temples can reach
  people interested in temples with no followers behind it.
- Narrowing to a beachhead of a few temples was the best corroborated finding
  across all four rounds.
- Roughly 98 percent of posts carry no call to action.
- Two content shows exist: Temple Study (his research plus his own line art) and
  The Inspection (delivered samples, quality control, garment decisions,
  photographed by him). A third, a customer feature program, is designed but
  blocked until customers exist.
- Pinterest ads were ruled out. Pinterest organic was kept.
- Cadence landed at five posts a week for month one, then about nine a week,
  produced by splintering two production sessions rather than by making more.

## Hard constraints the research has to respect

These are not preferences. A recommendation that violates one of them is not a
recommendation:

- **Only material Evan owns outright.** His line art, his own photographs, his
  own writing. Never a third party photograph. No content showing how the line
  art is made and none showing reference images being gathered.
- **Print on demand.** He never sees the printing, so no factory, press, or
  making of content exists or can exist.
- **The garment blanks are undecided.** Content that requires a finished product
  he has committed to selling is blocked for now.
- Premium price, zero reviews, no photos of real people wearing anything.
- No jokes, no politics. Not affiliated with the Church, and a disclaimer
  already runs on every product page.
- Likely two operators, Evan and his wife Bailee, with the voice and attribution
  question still open. Do not assume a solo operator, and do not assume either
  of them will appear on camera.

## Open questions this round must actually answer

- Is there a TikTok Shop buyer base for Latter-day Saint temple art, or is that
  an assumption borrowed from unrelated apparel brands? Prior rounds flagged
  this as unknown. Resolve it or confirm it stays unknown.
- Snapchat has never been assessed at all. Does it do anything the others do
  not?
- Does posting the same asset to several platforms carry a real penalty, or is
  cross posting basically free? This is the crux of the breadth question.
- Is "be everywhere" a reach argument or a credibility argument? A brand a buyer
  can search for and find something about looks more real than one that returns
  nothing. Those are different reasons to open an account and they lead to
  different amounts of work. Answer them separately.

## Phase 1a: build the source list and show it to me first

Do not gather anything yet. Verify every URL resolves and is on topic. Never
invent a URL, a title, a statistic, or an account name.

Split sources into three classes and keep the labels through the whole job:

- **Class A, primary data.** Audience size, age and sex skew, United States
  versus global, time spent, and referral traffic. Pew Research Center's social
  media fact sheet, DataReportal, platform investor disclosures, Shopify and
  Similarweb style traffic data. Numbers come from here or they do not get used.
- **Class B, mechanics.** How distribution works on each platform, what formats
  win, how links are treated, whether posts are searchable later, watermark and
  repost handling. Practitioner videos through the /watch skill and written
  sources. Good for how it works, not for numbers.
- **Class C, first hand reconnaissance.** Go look. Search each platform for
  Latter-day Saint temple art, temple photography, and faith apparel accounts.
  Note what exists, roughly how big, what formats get engagement, and whether
  anyone is already doing this well. Use the in app browser tools where the
  platform shows content logged out, and say plainly which platforms are gated
  and therefore unverified. Do not log in to anything.

For each candidate give me: source, class, URL, date of the data, and one line
on why it earns a slot. Flag anything over 25 minutes and tell me which section
you would watch. **Show me the list and stop. This is a real gate.**

## Phase 1b: gather

Use /watch with `--no-whisper` on any video. Transcription stays local, never a
paid API. Use `--start` and `--end` to watch only what matters.

Write one file per platform at `research/social-platforms/<platform>.md`, and
answer the same questions in the same order every time so the platforms are
comparable:

1. Who is actually there. Reach, age skew, sex skew, US versus global, with
   source and date on every number.
2. How a post reaches someone who does not follow the account. Interest media
   or follower media. This decides whether a brand with no audience can start
   there at all.
3. Shelf life of a post. Hours, days, or years.
4. Searchability. Can someone find this later by typing a temple name, and does
   Google index it?
5. Link behavior. Can a post send a person to a product page without being
   throttled, and is that traffic known to buy?
6. Native commerce. Shops, in app checkout, creator commission programs, and
   whether this category is allowed. TikTok Shop specifically.
7. What the platform demands in return: format, length, cadence, face on camera
   or not. Then say whether that can be met using owned material only, given the
   constraints above.
8. **What it is bad at.** Required section. No platform profile ships without
   it.
9. Real cost to run per week in hours for someone who is not a full time
   creator, and what happens if the account goes quiet for a month.
10. Rules and account risk. Anything about religious content, religious imagery
    in ads, or posting identical assets across platforms.
11. Is there a Latter-day Saint audience on this platform today? Name what you
    actually saw with rough sizes, or write "none found." Do not estimate.

Then write `research/social-platforms/_cross-cutting.md` covering:

- Cross posting penalties, with evidence rather than folklore.
- The marginal cost and marginal return of platform number three, four, five.
  Is there a documented pattern of small brands winning by concentrating?
- The credibility versus reach split described above.
- The owned audience alternative, email and a blog, taken seriously. Seth
  Godin's position is already on record in the prior research and reaches a
  million people without these platforms. Weigh it, do not wave at it.
- What changes when there are two operators instead of one.

## Phase 1c: synthesize

Write `research/SOCIAL-PLATFORM-FINDINGS.md`. This is the deliverable, so write
it as a report someone actually reads, not a table with notes attached. Open
with a short summary of the question and how you approached it, then give each
platform its own section in full prose covering the eleven points from 1b, not
just a restated checklist. The comparison table and the tiering
recommendation belong near the end, as the payoff after the reader has seen the
reasoning, not as the whole document.

Label every claim:

- **CONFIRMED**: two or more independent sources agree, and any number is backed
  by at least one Class A source.
- **SINGLE SOURCE**: keep it, mark it.
- **CONFLICT**: sources disagree. Say so, then give your read and your reasoning.
- **UNKNOWN**: you could not verify it. Write this often rather than filling
  gaps with plausible sentences.

Throw out any statistic that does not have a primary source or two independent
matches. A number a marketer said on camera is not evidence.

The file needs:

- A comparison table, one row per platform, columns for reach to non followers,
  shelf life, searchable, sends traffic, native commerce, fit with owned
  material only, hours per week, and whether an audience is already there.
- A tiering recommendation: primary, secondary, presence only meaning claim the
  handle and post rarely or never, and skip. Tie every placement to this brand's
  constraints, not to general best practice.
- For each platform not in the primary tier, one line on what is lost by not
  being there.
- A section called "The case against this recommendation," written as strongly
  as you can make it. Then say whether it survives.
- A section flagging anything that contradicts the settled findings above or
  collides with BRAND.md.

## Rules

- No em dashes anywhere.
- Date every number. A 2019 demographic split says nothing about 2026.
- Keep United States and global figures separate.
- Do not write a content calendar, do not draft posts, do not build a skill, and
  do not touch the store. This round ends at a recommendation.
- Show me the findings and stop.

If I approve it, the next job is updating the posting rota artifact and
BRAND.md. Do not start that on your own.
