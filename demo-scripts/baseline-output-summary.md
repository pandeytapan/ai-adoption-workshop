# Baseline Output — Tier 1 Demo

**Prompt used:**

> "Summarize the key requirements in this document."

**Input:** `sample-input-messy-requirements.md` (the forwarded email thread, unedited)

---

## Output

The client wants to rebuild their distributor portal, which is currently unreliable and pushing distributors to email the ops team directly instead of using it. The main requirements raised are: making the order status page real-time instead of updating every few hours; allowing bulk orders via CSV upload, though it's unclear if that's realistic for phase one; adding an approval step before an order is confirmed, since orders currently go through automatically and this has already caused a $40k mistaken order; keeping the existing invoice download feature as-is; possibly adding SSO through Okta since distributors keep forgetting passwords, though it's not confirmed to be in scope for this round; fixing search performance, which breaks down once a distributor has more than a few thousand past orders and needs to reliably handle 10,000+ records; and improving mobile usability, though the priority of this is unclear. Additional requests include email notifications when an order status changes, API access for two larger distributors (Hendricks Supply and Maren Foods) who want to pull order data into their own systems, and an audit trail for order modifications and cancellations, which Legal has flagged as missing. Leadership wants something live before Q4, but it hasn't been decided whether that means the full rebuild or just a first phase, and budget approval is still pending for anything beyond the currently agreed scope — so the API and mobile work may end up out of this round.

---

*This is what you get by default: a reasonably accurate summary, but still just prose. Everything — the audit trail, the budget caveat, the open questions about SSO scope — is compressed into one paragraph. Nothing here is client-ready, nothing is categorized, and nothing distinguishes a firm requirement from an open question. That's the gap Tier 1's structured prompt closes.*
