URL: https://community.shopify.com/t/how-to-hide-sticky-header-on-scroll-down-and-show-it-again-on-scroll-up-shrine-pro-theme/667049
JSON: https://community.shopify.com/t/667049.json
HTTP status: 200
Fetched: 2026-10-03 via curl (Discourse topic JSON)
Title: How to hide sticky header on scroll down and show it again on scroll up, Shrine Pro theme
Created: 2026-08-16T10:25:23.365Z
Last posted: 2026-08-16T16:45:59.596Z
Posts: 5  Views: 138
Category id: 294  Tags: []
Accepted answer: null

---

## Post 1 by ayubbaloch at 2026-08-16T10:25:23.526Z
Hi everyone,

I’m using the Shrine Pro theme on my store and I have the sticky header enabled. Right now it stays fixed on screen at all times while scrolling.

I’d like to customize this behavior so that:

- The sticky header hides when scrolling down

- The sticky header reappears when scrolling up

Has anyone done this on Shrine Pro before, or know which file/section controls the sticky header behavior (e.g. header.liquid, global.js, or theme settings)? I’m comfortable adding custom CSS/JS via the theme editor’s custom code sections if someone can point me to the right approach.

Any code snippets or theme setting suggestions would be really appreciated. Thanks in advance!

## Post 2 by NKCreativeSoulutions at 2026-08-16T11:25:46.887Z
That’s a pretty neat idea!

There are probably hundreds of ways to do it. Right off the top of my head, I’d create a boolean variable for scrolling down and when this value is true, you add the css value of hidden to the class names of the header. Remove it when the value is false.

Now, you need to determine how to identify if the user is scrolling in the appropriate direction, this stackexchange post should get you sorted for that:

detecting scroll direction on StackExchange

Hope it helps!

Nathan

## Post 3 by New_Dev at 2026-08-16T11:44:50.489Z
Nathan’s approach makes sense. One thing I’d add is to hide the header with transform: translateY(-100%) rather than display: none, so the transition stays smooth and doesn’t cause a layout jump.

## Post 4 by anna_backlip_hq at 2026-08-16T14:50:57.243Z
I’m not sure what the exact header selector is in Shrine Pro, but it should be the same general idea. Find the header element, then use a small script to check whether the user is scrolling up or down. The script adds a class when scrolling down and removes it when scrolling up:

const header = document.querySelector(‘YOUR_HEADER_SELECTOR’);

let lastScrollY = window.scrollY;

if (header) {

window.addEventListener(‘scroll’, () => {

const currentScrollY = window.scrollY;

if (currentScrollY > lastScrollY && currentScrollY > 80) {
  header.classList.add('header-hidden');
} else if (currentScrollY < lastScrollY) {
  header.classList.remove('header-hidden');
}

lastScrollY = currentScrollY;

});

}

Then add CSS for the hidden state:

YOUR_HEADER_SELECTOR {

transition: transform 0.2s ease;

}

YOUR_HEADER_SELECTOR.header-hidden {

transform: translateY(-100%);

}

## Post 6 by Ploqo at 2026-08-16T16:45:59.596Z
I tested on the Shrine Pro demo store (by injecting js and css in the client side).

Before: on Shrine Pro the header stays fixed when scrolling down3400×1752 732 KB

After: scrolling down hides the header3400×1752 755 KB

Scrolling back up brings the header in3400×1752 741 KB

Shrine Pro is built on Dawn.

Building on Nathan (translateY is the right call, it keeps the motion smooth with no layout jump)

- Header hides when you scroll down.

- Header slides back in when you scroll up.

- Smooth slide, no jump, works on every page.

- 

steps

- Online Store > Themes > … > Edit code.

- open layout/theme.liquid, scroll to the bottom, and paste this on a new line just above the closing </body> tag.

- Save.

Paste before the closing body tag in theme.liquid3424×1180 439 KB

{%- comment -%} Hide sticky header on scroll down, show on scroll up {%- endcomment -%}
<style>
  [data-hs-header]{transition:transform .35s ease !important;will-change:transform;}
  [data-hs-header].hs-header--hidden{transform:translateY(-100%) !important;}
</style>
<script>
(function(){
  function init(){
    var header =
      document.querySelector('.section-header') ||
      document.querySelector('sticky-header') ||
      document.querySelector('.header-wrapper') ||
      (document.querySelector('header') && document.querySelector('header').closest('.shopify-section'));
    if(!header) return;
    header.setAttribute('data-hs-header','');
    var lastY = window.pageYOffset || document.documentElement.scrollTop;
    var ticking = false;
    function update(){
      var y = window.pageYOffset || document.documentElement.scrollTop;
      var threshold = header.offsetHeight || 80;
      if(y > lastY && y > threshold){ header.classList.add('hs-header--hidden'); }
      else if(y < lastY){ header.classList.remove('hs-header--hidden'); }
      lastY = y <= 0 ? 0 : y;
      ticking = false;
    }
    window.addEventListener('scroll', function(){
      if(!ticking){ window.requestAnimationFrame(update); ticking = true; }
    }, {passive:true});
  }
  if(document.readyState === 'loading'){ document.addEventListener('DOMContentLoaded', init); }
  else { init(); }
})();
</script>

Notes

- Slide speed: change .35s (lower is faster).

- Hide sooner or later: header.offsetHeight is the point where hiding starts. Replace it with a number like 150 to hide only after scrolling further down.

Alternatives: sticky header apps lile qikify Sticky Header or Sticky Header Effects

Regards,

Ploqo
