# Sample Input — Messy Client Requirement Doc (Tier 1 demo)

Fictional client, fictional company. This is what's meant to be pasted into the chat
window (or uploaded as a .txt/.docx) live during the Tier 1 demo, as the input for:

> "Read this client requirement document and produce a structured Word document with:
> an executive summary, a numbered list of functional requirements grouped by category,
> a list of open questions needing client clarification, and a rough timeline estimate table.
> Save it as a .docx file I can send to the client."

It's deliberately unstructured — a forwarded email thread + call notes, the way these
things actually arrive. Don't clean it up before the demo; the mess is the point.

---

**Copy everything below this line into the chat window as the demo input:**

---

Subject: FW: Portal rebuild - notes from Tuesday call + a few more thoughts

Hey team,

Pulling together what we discussed Tuesday plus some stuff Priya added over email
since then. Sorry this is a bit scattered, wanted to get it to you before the long
weekend.

Main thing — our distributor portal is basically held together with duct tape at
this point. Distributors log in to check order status, submit new orders, and download
invoices. Right now half of them just email our ops team instead because the portal
is so slow and confusing. We want a rebuild.

Some of what came up:

- Order status page needs to actually be real-time, not "updated every few hours"
  like it is now. This was the #1 complaint in the last survey we sent out.
- Distributors should be able to place bulk orders (CSV upload ideally, someone on
  the call mentioned this, not sure if that's realistic for phase 1)
- Need an approval step before an order actually gets confirmed - right now anyone
  with a login can just submit and it goes straight through, which has caused problems
  twice this year (once was a $40k order that shouldn't have gone through, still
  dealing with that mess with finance)
- Invoice download - keep this, works fine, don't touch it
- SSO - this came up late in the call, Marcus mentioned distributors keep forgetting
  passwords and it's a support burden. We use Okta internally if that helps. Not 100%
  sure this is in scope for this round or a "later" thing, need to check budget
- Search - once a distributor has more than a few thousand past orders the search
  basically stops working, just spins. This gets worse every quarter as more data
  piles up. Whatever the fix is needs to actually hold up past 10k+ records, we've
  been burned before by a "fix" that worked in testing and then fell over in prod
- Mobile - portal is unusable on a phone right now, several distributors mentioned
  this, but honestly not sure how many of them actually need mobile vs just annoyed
  it looks bad. Could be lower priority.

Priya's additions from her email this morning:

"Also — can we get some kind of notification when an order status changes? Distributors
are still calling in to ask 'is my order shipped yet.' Email would be fine, doesn't need
to be fancy. And a couple of the bigger distributors (Hendricks Supply, Maren Foods) have
asked about an API instead of the portal UI entirely, since they want to pull order data
into their own systems. Not sure if that's this project or a separate thing honestly."

One more thing from the call — someone (I think it was Dana?) raised that the current
system doesn't have any audit trail. If an order gets modified or cancelled there's no
record of who did it or when. Legal flagged this a while back and it never got addressed.
Might be worth folding in here since we're already touching the order flow.

Timeline-wise: leadership wants "something" live before Q4, but nobody's said whether
that means the full rebuild or a first phase. Budget approval is still pending for
anything beyond the current scope we already talked about, so treat the API and mobile
stuff as maybe-not-this-round.

Let me know what you need from us to get started. Can hop on a call this week if useful.

Thanks,
Alan

---

**End of input.**
