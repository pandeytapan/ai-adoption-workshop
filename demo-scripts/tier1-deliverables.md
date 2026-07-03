# Tier 1 Demo Script — From Snippet to Deliverable

**Window:** 10–35 min
**Goal:** Show that AI can produce an actual structured file (Word/Excel/PDF), not just a chat reply to copy-paste.

## Setup beforehand

- Have one real (anonymized) messy client requirement doc ready to paste or upload — the messier and more realistic, the better. Avoid clean, obviously-staged inputs.
- Decide in advance which output format best fits your audience's daily work: a Word doc (client-facing summary), an Excel model (scoping/estimation), or a PDF (formal deliverable).

## Live prompt sequence

**Step 1 — establish the baseline (what most people already do):**

> "Summarize the key requirements in this document."

Run this first and point out: this is where most people stop — a chat reply they'd then manually reformat.

**Step 2 — the actual demo prompt (structured deliverable):**

> "Read this client requirement document and produce a structured Word document with: an executive summary, a numbered list of functional requirements grouped by category, a list of open questions that need client clarification, and a rough timeline estimate table. Save it as a proper .docx file I can send to the client."

**Step 3 (optional, if time and audience skew toward estimation/finance) — Excel variant:**

> "Take the requirements from this document and build an Excel scoping model — one row per requirement, with columns for category, estimated effort (S/M/L), owner (blank for now), and a status column. Add a summary tab totaling effort by category."

**Step 4 — open and narrate the output:**

- Open the actual file, don't just describe it.
- Point at one specific structural choice it made well (e.g., how it grouped requirements, or how it flagged an ambiguous requirement as an open question).
- Say explicitly: "I didn't copy or reformat anything — this is the file I'd attach to an email right now."

## Talking point to land

"Notice what didn't happen — I didn't copy anything. That's the whole mental shift for this tier: stop treating the chat window as the finish line."

## If it fails live

Switch to the recorded backup (see [`../docs/03-demo-backup-checklist.md`](../docs/03-demo-backup-checklist.md)) — say "let me show you the version I captured earlier" and move on without dwelling on the failure.
