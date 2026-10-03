URL: https://community.shopify.com/t/liquid-text-appearing-in-brand-grid-sections/590610
JSON: https://community.shopify.com/t/590610.json
HTTP status: 200
Fetched: 2026-10-03 via curl (Discourse topic JSON)
Title: "liquid" text appearing in "Brand Grid" sections
Created: 2026-03-02T17:04:40.559Z
Last posted: 2026-03-03T14:30:50.379Z
Posts: 8  Views: 91
Category id: 95  Tags: [{'id': 4021, 'name': 'troubleshooting', 'slug': 'troubleshooting'}]
Accepted answer: null

---

## Post 1 by JRSTupelo at 2026-03-02T17:04:40.694Z
I have added several sections with “Brand Grids” in them. In the space where the header would be, I get the text “liquid” that appears when nothing is supposed to be there. I had this same issue before with a text appearing that said “‘ ‘‘liquid “, but I was able to find the issue in the code and get rid of it. I’m not having the same luck with this new issue. Any help would be appreciated.

Screenshot 2026-03-02 102806138×128 954 Bytes

## Post 2 by Mustafa_Ali at 2026-03-02T17:08:59.467Z
Hey @JRSTupelo Welcome to Shopify Community if you feel comfortable plz share the URL of your website so i can help you out

## Post 3 by devcoders at 2026-03-02T17:43:00.211Z
Hi @JRSTupelo

Welcome to the Shopify Community! Please share your store URL and password (if it’s password-protected), so I can check and provide you with the exact solution.

Best regards,

Devcoder

## Post 4 by JRSTupelo at 2026-03-02T19:10:38.994Z
Jackson Restaurant Supply
  

  
    

Jackson Restaurant Supply

  Restaurant and Kitchen Supply store with locations in Tupelo, MS and Jackson, TN. We are open to the public and would love to help with all your restaurant and home kitchen needs! Come shop with us today!

  

  
    
    
  

  

shaemp

## Post 5 by Dan-From-Ryviu at 2026-03-03T02:29:18.162Z  [ACCEPTED ANSWER]
JRSTupelo:

shaemp

Right-click on that section > Edit code, check, and remove liquid text from the file that AI generates to solve the issue.

## Post 6 by devcoders at 2026-03-03T03:32:34.072Z
Hi @JRSTupelo

Please send me the file code for the AI-brand section that you created.

Best regards,

Devcoder

## Post 7 by tim_tairli at 2026-03-03T05:28:16.908Z
That looks like an AI-generated block.

So, look at the code of this “Brand grid” block and see if there is a stray “liquid” somewhere near the top.

You may share the code as well here, just do not forget to use the </> button when doing this or it will be broken by the forum.

## Post 8 by JRSTupelo at 2026-03-03T14:30:50.379Z
I found the issue. For some reason, it had inserted the word into the code at the very beginning, and I had glossed over it. Thank you to everyone for your help
