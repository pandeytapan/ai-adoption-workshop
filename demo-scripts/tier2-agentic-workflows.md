# Tier 2 Demo Script — Agentic Workflows (the real unlock)

**Window:** 35–60 min
**Goal:** Show multi-step, cross-system work — the moment people realize "oh, it can do things, not just tell me things."

Pick **one** of the two options below based on what's reliably available on the demo machine. Rehearse whichever you pick at least twice before the session.

---

## Option A — RFP Assessment Agent

**Setup beforehand:** have a real (anonymized) client RFP and your team's capability/services doc ready.
A ready-to-run fictional example is included, continuing the same client story as Tier 1:
[`sample-rfp-distributor-portal.md`](./sample-rfp-distributor-portal.md) (Meridian's formal RFP,
built directly from the Tier 1 requirements) and
[`vendor-capability-doc.md`](./vendor-capability-doc.md) (our fictional capability doc — deliberately
not a perfect match, so the agent has real gaps to catch). A pre-generated real output from running
the prompt below against both files is included as
[`rfp-fit-assessment.docx`](./rfp-fit-assessment.docx) — 79% overall fit, with a SOC 2 Type II gap,
an untested Okta integration, and a kickoff-logistics mismatch flagged as the top 3 items to address.
All three files are also linked as downloads directly on the Tier 2 slides in the live deck.

**Live prompt sequence:**

**Step 1 — name the steps out loud before running it** (this matters — the room should be able to follow along):

> "Watch what this does: it's going to read the RFP, pull out every requirement, check each one against our capability doc, and score how well we match — that's four steps most people would do by hand over an afternoon."

**Step 2 — the actual prompt:**

> "Read this client RFP and extract every distinct requirement into a list. Then cross-check each requirement against our capability document and mark it as: Strong Fit, Partial Fit, or Gap. Produce a scored assessment summary — overall fit percentage, a table of every requirement with its fit rating and a one-line justification, and a short list of the top 3 gaps we'd need to address before responding."

**Step 3 — narrate the cross-checking as it happens**, not just the final output — this is the "multi-step, not one prompt" moment the audience needs to see, not just hear about.

**Step 4 — open the output and point at one specific gap it flagged** — this builds trust ("it's not just saying yes to everything") more than pointing at the strong fits.

---

## Option B — Inbox-to-draft workflow (lighter, needs live Gmail/Drive access)

**Setup beforehand:** confirm connector auth is live and pick a real (or realistic seeded) thread in advance so the demo doesn't stall searching for one.

**Live prompt sequence:**

**Step 1 — be transparent about scope before running anything:**

> "To be clear — I'm giving it read, summarize, and draft access only. Nothing sends without me reviewing it first."

**Step 2 — the actual prompt:**

> "Find the most recent email thread about [project/client name], summarize where things stand, draft a reply that addresses the open question in the thread, and create a short follow-up doc listing the action items with owners."

**Step 3 — review the draft reply out loud before "sending"** (or explicitly not sending, if using a real inbox) — this is the human-in-the-loop moment, and it should be visible, not assumed.

---

## Talking point to land (either option)

"It can do things, not just tell me things." Say this explicitly once the output appears — don't assume the room draws the conclusion themselves.

## If it fails live

Switch to the recorded backup (see [`../docs/03-demo-backup-checklist.md`](../docs/03-demo-backup-checklist.md)).
