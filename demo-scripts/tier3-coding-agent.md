# Tier 3 Demo Script — Coding Agents (for the technical crowd)

**Window:** 60–80 min
**Goal:** Reframe AI from "autocomplete" to "junior engineer you can delegate to" — show it reading the codebase before it touches anything.

## Setup beforehand

- Pick a real, small task in a real repo — one of:
  - a genuinely failing test with a non-trivial fix
  - a function that needs refactoring for clarity or an obvious code smell
  - a new small module/endpoint that needs to follow existing project conventions
- Confirm the repo/branch is in a clean, expected starting state on the demo machine — check this the morning of, not the night before.
- Show the failing test or the function to refactor first, plainly, before running anything, so the room can judge the before/after themselves.

## Live prompt sequence

**Option A — fix a failing test:**

> "This test is failing. Find out why, fix the underlying issue (not just the test), and show me what you changed and why before you commit anything."

**Option B — refactor a function:**

> "This function has grown hard to follow. Refactor it for clarity following the conventions already used elsewhere in this codebase — check how similar functions are structured first. Don't change its behavior."

**Option C — new module following conventions:**

> "Add a new [module/endpoint/CLI command] for [X]. First look at how existing [modules/endpoints/commands] in this project are structured, named, and tested, then follow the same pattern."

## Narration cues while it runs

- Call out explicitly when it reads other files before writing: "Notice it's not autocompleting a line — it went and looked at three other files to understand our conventions before touching anything."
- If it runs tests or lints as it goes, narrate that too — this is the "junior engineer checking their own work" beat.
- Resist narrating every line of code — narrate the *decisions*, not the syntax.

## Talking point to land

"That's not autocomplete. That's delegation." Say this once the diff is on screen, not before.

## Anticipated question — code review concerns

If someone raises code quality or review concerns, welcome it — it's a genuine and reasonable question. Honest answer: agent output still goes through the same PR review process as anyone's code — nothing merges without a human review.

## If it fails live

Switch to the recorded backup (see [`../docs/03-demo-backup-checklist.md`](../docs/03-demo-backup-checklist.md)).
