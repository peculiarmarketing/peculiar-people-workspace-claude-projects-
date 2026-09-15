#!/usr/bin/env node
/*
 * Walks a Shopify storefront in a real browser and saves PNG evidence.
 * READ ONLY. Never submits a form, never completes a checkout, never edits the store.
 *
 * Usage:
 *   node capture.js --base https://example.com --out /path/to/run \
 *     --collection /collections/all --pdp /products/a --pdp /products/b [--search tee]
 *
 * Writes <out>/shots/*.png and <out>/manifest.json
 */
const { chromium, devices } = require(process.env.PW_PATH || 'playwright');
const fs = require('fs');
const path = require('path');

const argv = process.argv.slice(2);
const arg = (n, d) => { const i = argv.indexOf('--' + n); return i > -1 ? argv[i + 1] : d; };
const argAll = (n) => argv.reduce((a, v, i) => (v === '--' + n ? [...a, argv[i + 1]] : a), []);

const BASE = (arg('base') || '').replace(/\/$/, '');
const OUT = arg('out');
const COLLECTION = arg('collection', '/collections/all');
const PDPS = argAll('pdp');
const SEARCH = arg('search', 'temple');
if (!BASE || !OUT) { console.error('need --base and --out'); process.exit(2); }

const SHOTS = path.join(OUT, 'shots');
fs.mkdirSync(SHOTS, { recursive: true });
const manifest = { base: BASE, startedAt: new Date().toISOString(), viewports: {}, failures: [] };

const VIEWPORTS = {
  desktop: { name: 'desktop', opts: { viewport: { width: 1440, height: 900 } } },
  mobile: { name: 'mobile', opts: { ...devices['iPhone 13'] } },
};

// Full-page screenshots capture blank bands unless lazy-loaded sections are scrolled into
// view first. Walk the page down and back up before shooting, or the report will contain
// "empty section" findings that are really screenshot artifacts.
async function settleLazy(page) {
  await page.evaluate(async () => {
    const step = Math.round(window.innerHeight * 0.8);
    for (let y = 0; y < document.body.scrollHeight; y += step) {
      window.scrollTo(0, y);
      await new Promise(r => setTimeout(r, 320));
    }
    window.scrollTo(0, 0);
    await new Promise(r => setTimeout(r, 600));
  });
  await page.waitForTimeout(1200);
}

async function shot(page, vp, label, full = false) {
  const file = `${vp}__${label}.png`;
  try {
    if (full) await settleLazy(page);
    await page.screenshot({ path: path.join(SHOTS, file), fullPage: full });
    (manifest.viewports[vp] ||= []).push({ label, file, url: page.url(), fullPage: full });
    console.log(`saved ${file}`);
    return file;
  } catch (e) {
    manifest.failures.push({ vp, label, stage: 'screenshot', error: String(e).slice(0, 200) });
    return null;
  }
}

async function go(page, url) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
  await page.waitForTimeout(2500);
  // settle lazy images so the grid renders honestly
  await page.evaluate(() => window.scrollTo(0, 600)).catch(() => {});
  await page.waitForTimeout(800);
  await page.evaluate(() => window.scrollTo(0, 0)).catch(() => {});
  await page.waitForTimeout(600);
}

// Dismiss nothing automatically. Popups and banners ARE findings; capture them first.
//
// Scans EVERY match of each selector, not just .first(). Shopify themes ship a hidden
// cart-drawer copy of the cart form, so `button[name="checkout"]` matches two elements and
// the first one is invisible. Testing only .first() makes a present control look absent.
async function firstVisible(page, selectors) {
  for (const s of selectors) {
    try {
      const loc = page.locator(s);
      const n = Math.min(await loc.count(), 12);
      for (let i = 0; i < n; i++) {
        const el = loc.nth(i);
        if (await el.isVisible({ timeout: 700 }).catch(() => false)) return el;
      }
    } catch (_) {}
  }
  return null;
}

async function run(vpKey) {
  const vp = VIEWPORTS[vpKey];
  const browser = await chromium.launch();
  const ctx = await browser.newContext({ ...vp.opts, locale: 'en-US' });
  const page = await ctx.newPage();
  const step = async (label, fn) => {
    try { await fn(); } catch (e) {
      manifest.failures.push({ vp: vp.name, label, stage: 'interact', error: String(e).slice(0, 250) });
      console.log(`FAILED ${vp.name} ${label}: ${String(e).slice(0, 120)}`);
    }
  };

  // ---------- HOME ----------
  await step('home', async () => {
    await go(page, BASE + '/');
    await shot(page, vp.name, '01-home-fold');            // first impression, popups included
    await shot(page, vp.name, '02-home-full', true);
  });

  // ---------- NAV ----------
  await step('nav', async () => {
    await go(page, BASE + '/');
    const burger = await firstVisible(page, [
      'button[aria-label*="menu" i]', 'summary[aria-label*="menu" i]',
      '.header__icon--menu', 'button.header__icon--menu', '[data-testid="menu"]',
    ]);
    if (burger) { await burger.click(); await page.waitForTimeout(1200); }
    await shot(page, vp.name, '03-nav-open');
  });

  // ---------- SEARCH ----------
  await step('search', async () => {
    await go(page, `${BASE}/search?q=${encodeURIComponent(SEARCH)}`);
    await shot(page, vp.name, '04-search-results', true);
  });

  // ---------- COLLECTION ----------
  await step('collection', async () => {
    await go(page, BASE + COLLECTION);
    await shot(page, vp.name, '05-collection-fold');
    await shot(page, vp.name, '06-collection-full', true);
    if (vp.name === 'desktop') {
      const card = await firstVisible(page, [
        '.card-wrapper', '.card__inner', 'product-card', '.grid__item',
        '.collection product-card', '[class*="product-card"]', '.grid__item a',
      ]);
      if (card) {
        await card.scrollIntoViewIfNeeded().catch(() => {});
        await card.hover({ timeout: 8000 });
        await page.waitForTimeout(1200);
        await shot(page, vp.name, '07-collection-hover');
      } else {
        manifest.failures.push({ vp: vp.name, label: 'collection-hover', stage: 'note',
          error: 'no product card matched the known selectors; check the grid markup by hand' });
      }
    }
  });

  // ---------- PRODUCT PAGES ----------
  for (let i = 0; i < PDPS.length; i++) {
    const n = String(i + 1);
    const url = BASE + PDPS[i];
    await step(`pdp${n}`, async () => {
      await go(page, url);
      await shot(page, vp.name, `10-pdp${n}-fold`);
      await shot(page, vp.name, `11-pdp${n}-full`, true);
    });

    await step(`pdp${n}-variants`, async () => {
      await go(page, url);
      // colour: swatch-style inputs first, then any variant select
      const swatch = page.locator('input[type="radio"] + label, .swatch label, [class*="swatch"] label').nth(2);
      if (await swatch.count() && await swatch.isVisible().catch(() => false)) {
        await swatch.click({ timeout: 5000 });
        await page.waitForTimeout(2200);
        await shot(page, vp.name, `12-pdp${n}-colour-changed`);
      } else {
        const sel = page.locator('select').first();
        if (await sel.count()) {
          const opts = await sel.locator('option').allTextContents();
          if (opts.length > 1) { await sel.selectOption({ index: 1 }); await page.waitForTimeout(2000); }
          await shot(page, vp.name, `12-pdp${n}-colour-changed`);
          manifest.failures.push({ vp: vp.name, label: `pdp${n}-colour`, stage: 'note',
            error: 'colour presented as a <select> dropdown, not swatches (rule P3/P4 evidence)' });
        }
      }
      // size
      const sizeBtn = page.locator('fieldset:has-text("Size") label, [class*="size"] label, legend:has-text("Size") ~ * label').nth(1);
      if (await sizeBtn.count() && await sizeBtn.isVisible().catch(() => false)) {
        await sizeBtn.click({ timeout: 5000 }); await page.waitForTimeout(1500);
        await shot(page, vp.name, `13-pdp${n}-size-changed`);
      } else {
        const sels = page.locator('select');
        if (await sels.count() > 1) {
          await sels.nth(1).selectOption({ index: 1 }).catch(() => {});
          await page.waitForTimeout(1500);
          await shot(page, vp.name, `13-pdp${n}-size-changed`);
        }
      }
      // scroll to test sticky add-to-cart
      await page.evaluate(() => window.scrollBy(0, 1600));
      await page.waitForTimeout(1200);
      await shot(page, vp.name, `14-pdp${n}-scrolled-sticky`);
    });
  }

  // ---------- ADD TO CART + DRAWER ----------
  await step('cart', async () => {
    if (!PDPS.length) return;
    await go(page, BASE + PDPS[0]);
    const atc = await firstVisible(page, [
      'button[name="add"]', 'button.product-form__submit', '[type="submit"][name="add"]',
      'button:has-text("Add to cart")', 'button:has-text("Add to Cart")',
    ]);
    if (!atc) throw new Error('no add-to-cart button found');
    await atc.click({ timeout: 12000 });
    await page.waitForTimeout(4000);
    await shot(page, vp.name, '20-cart-drawer');
    // cart page too, in case the drawer is not the real cart
    await go(page, BASE + '/cart');
    await shot(page, vp.name, '21-cart-page', true);
  });

  // ---------- CHECKOUT ENTRY (never complete) ----------
  await step('checkout', async () => {
    await go(page, BASE + '/cart');
    const co = await firstVisible(page, [
      'button[name="checkout"]', 'input[name="checkout"]', '[href="/checkout"]',
      'button:has-text("Check out")', 'button:has-text("Checkout")',
    ]);
    if (!co) throw new Error('no checkout button found on cart page');
    await co.click({ timeout: 15000 });
    await page.waitForTimeout(7000);
    await shot(page, vp.name, '30-checkout-entry');
    await shot(page, vp.name, '31-checkout-entry-full', true);
    // HARD STOP. Nothing is typed and nothing is submitted beyond this point.
  });

  // ---------- FOOTER ----------
  await step('footer', async () => {
    await go(page, BASE + '/');
    await page.evaluate(() => window.scrollTo(0, document.body.scrollHeight));
    await page.waitForTimeout(2000);
    await shot(page, vp.name, '40-footer');
  });

  await ctx.close();
  await browser.close();
}

(async () => {
  for (const k of Object.keys(VIEWPORTS)) {
    console.log(`\n=== ${k} ===`);
    await run(k);
  }
  manifest.finishedAt = new Date().toISOString();
  fs.writeFileSync(path.join(OUT, 'manifest.json'), JSON.stringify(manifest, null, 2));
  console.log(`\nmanifest: ${path.join(OUT, 'manifest.json')}`);
  console.log(`failures: ${manifest.failures.length}`);
})();
