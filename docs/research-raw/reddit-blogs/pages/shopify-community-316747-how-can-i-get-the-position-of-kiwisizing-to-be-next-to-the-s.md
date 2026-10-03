URL: https://community.shopify.com/t/how-can-i-get-the-position-of-kiwisizing-to-be-next-to-the-size-selector/316747
JSON: https://community.shopify.com/t/316747.json
HTTP status: 200
Fetched: 2026-10-03 via curl (Discourse topic JSON)
Title: How can i get the position of kiwisizing to be next to the size selector
Created: 2024-04-22T21:39:42.000Z
Last posted: 2024-04-23T11:21:37.000Z
Posts: 4  Views: 133
Category id: 133  Tags: [{'id': 5078, 'name': 'product-page', 'slug': 'product-page'}]
Accepted answer: null

---

## Post 1 by Svds at 2024-04-22T21:39:42.000Z
can someone help me, i want to change the position of kiwisizing, now it is just underneath my price and it needs to be like this:

Scherm­afbeelding 2024-04-22 om 23.37.58.png678×178 4.16 KB

## Post 2 by sahilsharma9515 at 2024-04-23T07:28:39.000Z
Hi @Svds

Can you please provide your store URL and password as well if applicable, so that I can provide you solution that can work for your store.

Best regards

Sahil

## Post 3 by Svds at 2024-04-23T10:36:03.000Z
https://facce-amsterdam.nl/

## Post 4 by sahilsharma9515 at 2024-04-23T11:21:37.000Z  [ACCEPTED ANSWER]
Hi @Svds Please add the code in your theme.css/base.css/style.css file which is available in your theme.

span.ks-chart-modal-link.sizing-chart-modal-link.with-icon {
    position: absolute;
    left: 8rem;
    top: 24.7rem;
}

If you are not sure where is your theme.css/base.css/index.css/style.css file please follow the steps:

- Login in shopify admin.

- Click on the Online Store.

- Then click on the button next to Customize in live Theme.

- Click Edit Code.

- Search theme.css/base.css/index.css/style.css in the code in left hand side which ever is available in your theme.

- You can add the above code at the bottom of the file.

Result:

sahilsharma9515_0-1713871269225.png880×526 61.4 KB

If you will unable to implement the same then I’m happy to do this for you, let me know. I can implement the code changes so that this will work well for you.

Hopefully it will help you. If yes then Please don’t forget hit Like and Mark it as solution!

Best Regards

Sahil
