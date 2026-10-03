# Instagram reel fetch attempts (2026-10-03)

Result: no reel content was retrieved by any automated method. Nothing below is inferred about reel content.

| Reel | WebFetch | curl (page) | curl (/embed/captioned/) |
|---|---|---|---|
| https://www.instagram.com/reel/DdJ5ynbDxqS/ | Error: `{"error_type":"EGRESS_BLOCKED","domain":"www.instagram.com","message":"Access to www.instagram.com is blocked by the network egress proxy."}` | HTTP 000, `curl: (56) CONNECT tunnel failed, response 403` | HTTP 000 |
| https://www.instagram.com/reel/DdiYr7wOmsE/ | Same EGRESS_BLOCKED error | HTTP 000 | HTTP 000 |
| https://www.instagram.com/reel/DcwkX6OyduT/ | Same EGRESS_BLOCKED error | HTTP 000 | HTTP 000 |

Notes:
- The proxy blocks instagram.com at the CONNECT stage, so login walls were never reached.
- A separate file in this folder, `reel-transcripts-from-owner.md`, holds transcripts the owner pasted. Those were not fetched by Claude. Tool names checked in web research (Emil Kowalski skills, Impeccable, Taste Skill, Figma MCP, Playwright MCP, Motion.dev, Bklit UI, Kokonut UI, Manus, UX laws md) came from the task brief and that owner file, not from a fetch.
- Web search for "adam_ha_yes UX laws Claude md file" found no page for that creator or file.
