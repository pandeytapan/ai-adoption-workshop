# Sample Input — Vendor RFP (Tier 2 demo)

Fictional client, fictional company, fictional vendor — same client as the Tier 1 demo,
one step further down the road. This is what's meant to be pasted into the chat window
(or uploaded as a .pdf/.docx) live during the Tier 2 demo, as the input for:

> "Read this client RFP and extract every distinct requirement into a list. Then
> cross-check each requirement against our capability document and mark it as: Strong
> Fit, Partial Fit, or Gap. Produce a scored assessment summary — overall fit
> percentage, a table of every requirement with its fit rating and a one-line
> justification, and a short list of the top 3 gaps we'd need to address before
> responding."

**The story so far:** In Tier 1, Alan's scattered call notes about the distributor
portal became a clean structured requirements doc. A few weeks later, Meridian's
procurement team turned that into a formal RFP and sent it to a shortlist of vendors —
including us. This is that RFP.

The companion file for this demo is
[`vendor-capability-doc.md`](./vendor-capability-doc.md) — our (fictional) capability
doc, deliberately not a perfect match, so the agent has something real to catch.

---

**Copy everything below this line into the chat window as the demo input:**

---

# Request for Proposal — Distributor Portal Rebuild
**Meridian Industrial Supply**
**RFP reference:** MIS-2026-014
**Issued:** June 15, 2026
**Proposals due:** July 24, 2026
**Point of contact:** Priya Sharma, Head of Procurement — psharma@meridian-industrial.example

## 1. Background

Meridian Industrial Supply operates a distributor-facing web portal used by roughly
80 distributor accounts to check order status, place orders, and download invoices.
The current portal was built in 2018 and no longer meets our operational or security
requirements. We are seeking a vendor to design, build, and support a full rebuild.

This RFP reflects requirements gathered from internal stakeholders (operations,
finance, legal, and IT) over the past quarter.

## 2. Scope of work

Vendors should propose an approach covering all items in Section 3, with a phased
delivery plan if a full rebuild cannot reasonably be delivered as a single release
before our Q4 target (see Section 6).

## 3. Functional and technical requirements

1. **Real-time order status.** Distributors must see order status updates in
   real time, not on a batch/polling delay. This is our #1 distributor complaint
   today.
2. **Bulk order upload.** Distributors must be able to submit bulk orders via CSV
   upload, with validation and error reporting before submission is finalized.
3. **Order approval workflow.** No order should be auto-confirmed. All orders must
   pass through a configurable internal approval step before confirmation, with a
   full record of who approved or rejected each order.
4. **Invoice download.** Retain existing invoice download functionality; no material
   changes required here.
5. **Single sign-on.** The portal must support SSO for distributor users. Meridian's
   internal identity provider is **Okta**; distributor-side SSO should integrate
   cleanly with Okta as the source of truth for our internal users, and support
   standard SAML/OIDC federation for distributor-side identity providers.
6. **Search performance at scale.** Order history search must remain performant
   (sub-2-second response) for accounts with 10,000+ historical orders, and must
   be load-tested to demonstrate this before go-live, not just in a staging
   environment with sample data.
7. **Mobile-responsive design.** The portal must be fully usable on mobile browsers.
   A native mobile app is not required for this phase.
8. **Order status notifications.** Distributors must receive a notification
   (email at minimum) when an order's status changes.
9. **API access.** The portal must expose a documented REST API for order data,
   for distributor accounts (initially Hendricks Supply and Maren Foods) who want
   to integrate order data into their own systems rather than use the UI.
10. **Audit trail.** Every modification or cancellation of an order must be logged
    with a timestamp and the identity of the user who made the change. This is a
    hard requirement flagged by our legal team.
11. **Data residency & security.** All distributor and order data must be hosted in
    a data center located in the United States or Canada. Vendor must provide
    evidence of a current **SOC 2 Type II** report covering the systems that will
    host or process Meridian data. A SOC 2 Type I report alone is not sufficient
    for this engagement given the financial and order data involved.
12. **Support SLA.** Vendor must provide a minimum of business-hours support
    (8am–6pm Eastern, Mon–Fri) with a documented critical-issue response time of
    under 4 hours. 24/7 support is preferred but not required.
13. **Kickoff.** Vendor's proposed delivery team must be available for an
    in-person kickoff workshop at Meridian's headquarters (Columbus, Ohio) within
    the first two weeks of contract signature. This is a strong preference from
    our VP of Operations, not a hard disqualifier, but should be addressed in
    proposals.
14. **References.** Vendor must provide at least two references from prior clients
    of comparable size (mid-market B2B portal or e-commerce rebuild).

## 4. Evaluation criteria

Proposals will be scored on: technical fit against Section 3 (40%), team
qualifications and references (20%), proposed timeline (20%), and cost (20%).

## 5. Submission requirements

Proposals should include a proposed team structure, relevant past project summaries,
a phased delivery plan with rough timeline, and a not-to-exceed cost estimate.
Formal pricing will be requested from shortlisted vendors in a follow-up round.

## 6. Timeline

Meridian's leadership has asked for a Phase 1 release live before the end of Q4 2026.
Budget for Phase 2 scope (API access, mobile optimization beyond responsive basics)
is approved contingent on Phase 1 delivery; anything beyond that is not yet approved.

---

**End of input.**
