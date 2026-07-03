# Session Outline — AI-First Adoption Workshop (90 min)

**Audience:** Cynoteck team (technical + client-facing), client-project-driven org
**Core challenge:** Not tooling — the mental model gap. Most people think "AI = chat window where I paste a paragraph and get a paragraph back." The goal is to move them from prompt-and-copy to AI that plans, acts, and touches real systems, without losing them in jargon. Anchor everything in scenarios they already recognize (RFPs, docs, code review, client comms) rather than generic demos.

---

## 0–10 min — Reframe, not features

Open with a blunt before/after:

- **Before:** paste a paragraph into a chat box, get a paragraph back.
- **After:** an AI system that reads a doc, checks three sources, drafts a deliverable, and flags what needs a human.

To make the "before" state concrete rather than just described, the slide shows an actual example exchange:

> **Pasted in:** "We need bulk invoice uploads, an approval step before finance sees it, and search that doesn't crawl once we're past 10k records. Also has to work with our SSO. Rough timeline?"
>
> **Copied out:** "Here's a summary: 1) Bulk upload 2) Approval workflow 3) Faster search 4) SSO integration. Let me know if you'd like more detail!" — then manually reformatted into whatever the client actually needs.

Don't demo yet — just set the stakes. The example above is shown as static text on the slide, not run live.

> "If you're only using AI for snippets, you're using 10% of what's available and doing 90% of the work yourself."

---

## 10–35 min — Tier 1: From snippet to deliverable

Show that even without agents, most people stop too early.

**Live demo:** take a messy client requirement doc → have Claude produce an actual structured output (a Word doc, an Excel model, a PDF) — not a chat reply they'd copy-paste.

Why this tier first: it's the easiest "aha" because it's a small mental shift but a big capability jump for people who've never seen file generation.

See [`demo-scripts/tier1-deliverables.md`](../demo-scripts/tier1-deliverables.md) for the exact prompts.

---

## 35–60 min — Tier 2: Agentic workflows (the real unlock)

This is where real war stories land — things actually built, not hypotheticals.

**Option A — RFP Assessment Agent concept:** feed in a client RFP, have the agent extract requirements, cross-check against a capability doc, and produce a scored assessment — multi-step, not one prompt.

**Option B — lighter version:** connect Gmail/Drive live in the demo, have the agent search for a thread, summarize it, draft a reply, and create a follow-up doc — all in one instruction.

This is the moment people realize "oh, it can do things, not just tell me things."

See [`demo-scripts/tier2-agentic-workflows.md`](../demo-scripts/tier2-agentic-workflows.md) for the exact prompts.

---

## 60–80 min — Tier 3: Coding agents (for the technical crowd specifically)

Since this audience is technical, don't skip this — it's the tier that lands hardest for engineers.

**Live demo:** Claude Code (or similar) on a real small task — fix a failing test, refactor a function, or generate a new module following existing project conventions. Show it reading the codebase, not just autocompleting a line.

This reframes AI from "autocomplete" to "junior engineer you can delegate to."

See [`demo-scripts/tier3-coding-agent.md`](../demo-scripts/tier3-coding-agent.md) for the exact prompts.

---

## 80–90 min — Hands-on + close

Give the room one live task to try on their own laptop with a tool they already have access to:

- "Ask it to build you an Excel model from this messy CSV," or
- "Connect it to your inbox and summarize unread mail."

**Close with 2–3 concrete next steps:**

1. Which tools to request access to.
2. One workflow to try this week.
3. Where to ask for help.

---

## Practical demo tips

- **Record backups for every live demo.** Live agent demos can be slow or flaky in front of a room — have a recorded fallback for each tier so a bad API response doesn't kill momentum.
- **Use real Cynoteck-shaped examples**, not generic "write me a poem" demos — client RFPs, procurement docs, project status reports. Relevance beats polish for this audience.
- **Don't over-tool it.** Two or three well-chosen "wow" moments beat ten shallow ones. People remember the moment it did something, not a feature list.
- **Seed a plant in the audience** for the hands-on segment if worried about a slow room — someone who tries it first and shares their result out loud gets others moving.

See [`docs/03-demo-backup-checklist.md`](03-demo-backup-checklist.md) for the full pre-session checklist.
