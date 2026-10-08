# Reddit fetch attempts (2026-10-03, curl, Chrome UA)

Result: NOT ACCESSIBLE. No Reddit content was read. Nothing below is inferred about thread content.

- www.reddit.com/r/{shopify,ShopifyeCommerce,ClaudeAI,ClaudeCode,vibecoding,webdev}/search.json?q=...&restrict_sr=1
  -> HTTP 403. Body: "You've been blocked by network security. If you think you've been blocked by mistake, file a ticket below and we'll look into it."
- old.reddit.com/r/{same subreddits}/search.json?q=...&restrict_sr=1 and old.reddit.com/r/shopify/search?q=claude+code+theme&restrict_sr=on
  -> redirected to https://old.reddit.com/login/?reason=lor2&dest=... (HTTP 200, page title "Welcome to Reddit"). Login wall.
- Queries tried: "claude code theme", "shopify theme liquid section", "shopify theme" (r/ClaudeAI).
- Not retried with cookies, proxies or mirrors, per instructions.
