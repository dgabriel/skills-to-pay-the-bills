Status: done (38ffa07)

# Work order: four skills drawn from session history

A reviewing agent analyzed the owner's agent session history (about 160 sessions, September to October 2026) and found repeated workflows the library didn't cover. That agent reviews the output and acts as gatekeeper. Push back in writing on anything you disagree with; don't silently skip it.

## Setup

- Branch `codex/history-skills` from `main` (the first library PR is merged).
- Don't push, open a PR, or touch remote history. Local commits only.
- Follow AGENTS.md, the shared execution contract, and the existing package format (SKILL.md of 28 lines or fewer, references/procedure.md, PROVENANCE.md, LICENSE, agents/openai.yaml, synced contract copy).

## Evidence rules

- The evidence below is the reviewer's **paraphrase** of patterns. Do not search for, quote, or copy session transcripts, and don't read local agent session directories.
- Provenance for each skill lists (a) any public source files used, pinned to a commit, and (b) a "Pattern evidence" section using the paraphrases below, labeled "author session history, paraphrased by reviewer, 2026-10-17". No session IDs, credentials, server names, people's names, or private repo names.
- Before using any source file, confirm its repository is public and check its license. If a source (including the Flaught core repository) is private, local-only, or unlicensed, don't extract from it; write the procedure from the pattern evidence and say so.

## Skill 1: `review-findings-triage`

Purpose: triage automated or adversarial PR review findings (Flaught by default, any reviewer works) into fix, dismiss with rationale, or upstream bug, until the gate is clean.

Pattern evidence (about 20 sessions, 4+ projects):
- Before acting, the owner asks for a table of every finding: ID, severity/confidence, description, proposed action.
- She often triages one finding at a time and makes the fix/dismiss call herself. Dismissal rationale: "code owner understands the risk"; harmless findings get dismissed; valid findings are never ignored or merged past.
- Merging with unresolved findings is a hard no. The gate is blocking, and dismissals must be tracked properly.
- After triage, regenerate the review dashboard or report.
- Recurring false positives, a dismissed finding resurfacing under new wording or fingerprint, and noisy categories (docs-only diffs, tests that pass on base and head) become a concise **upstream bug report** for the review tool's maintainers, filed as an issue on request.
- She regularly asks for a "how well did the reviewer work, and where are the holes" report after a session.
- She asks for plain explanations of confusing findings.

Public sources to check: Flaught quick-start and prompt docs, `.advreview.yml` patterns in public repos that use Flaught, and the adversarial-review entries in `inventory/extractions.md`.

## Skill 2: `session-start-and-close`

Purpose: get oriented at session start and leave a clean handoff at the end, in any repo, using Beads when present.

Pattern evidence (about 22 start and 8 close sessions, 6 projects):
- Start: "situate yourself / get your bearings, then look at the new bead issues / outstanding tasks." After an interruption: "my work got cut off, see where we are and continue." Reply briefly with location, branch/PR state, open and ready issues, and blockers.
- Read the project's AGENTS.md/CLAUDE.md, git hygiene doc, and issue tracker before proposing work.
- Close: leave a note for the next developer, file follow-ups as tracker issues instead of loose notes, make sure work is committed (pushed only if authorized), and report what's left.
- When the owner is confused mid-session: a short, concrete bulleted status, not a long narrative.

Public sources: the session/handoff portions of AGENTS.md/CLAUDE.md marked `split / needs-review` in `inventory/extractions.md`. Resolve those ledger rows as part of this work.

## Skill 3: `local-test-handoff`

Purpose: after a feature is done, make it testable by the owner on her own devices and hand over what she needs.

Pattern evidence (about 12 sessions, 3 projects):
- Standing rule: when a feature is complete, spin up a local instance from the feature branch so she can test before merge.
- Make it reachable from a phone or tablet on the LAN (bind to the LAN address or use `--host`), and give the exact URL.
- Seed and keep a persistent dev test account so she doesn't recreate one after every change. Dev-only credentials on a local server may be shared in chat; **never share staging or production credentials**.
- Prefer a stable runtime (such as Docker) when the dev server keeps crashing; update in place without tearing everything down.
- End with a short device test checklist; she reports pass/fail per item.

Public sources: `run-mysterymixclub` (split / needs-review in the ledger). Keep ports, services, and hostnames as project overlay, not library defaults.

## Skill 4: `prose-edit`

Purpose: edit or tighten prose (READMEs, sites, talks, descriptions) in the owner's voice.

Rules (author-stated, not from a source file; provenance must say so):
- No em dashes. Limit colons and stacked clauses.
- Remove AI-isms; especially avoid "not X, but Y" / "not that, this" constructions and decorative metaphors.
- Tighter by default while keeping clarity. "Warmer" when asked means friendlier, not longer.
- Show the edited text and leave committing to the owner unless asked.

Include 2 or 3 before/after examples you write yourself.

## Also update

- `inventory/extractions.md`: resolve the rows these skills draw on.
- README skill table, catalog routing, evaluations (2 positive and 2 negative routing cases per new skill, written after descriptions are frozen, scored by a fresh evaluator), and validation.md (state exactly what ran).
- One paired baseline-vs-skill run for `review-findings-triage` and `prose-edit` on fictional fixtures. Report honestly if there's no difference.

## Out of scope

- Personal preferences beyond skill 3 don't go into this library's AGENTS.md; the owner handles personal config separately.
- No TestFlight/iOS runbook, what's-new modal, or LLM release gate. Those stay project-specific.

## Commits

1. `feat: add review-findings-triage skill`
2. `feat: add session-start-and-close skill`
3. `feat: add local-test-handoff skill`
4. `feat: add prose-edit skill`
5. `test: add routing and paired evidence for history-derived skills`
6. `docs: update catalog, README, and extraction ledger` (also include `work-orders/` and the AGENTS.md work-order rule added by the reviewer)

## Acceptance criteria

- [ ] `python3 scripts/check_library.py` and `python3 scripts/replay_evaluations.py` pass at HEAD and at each commit. Paste the output.
- [ ] Every new PROVENANCE has a "Pattern evidence" section and pinned public sources, or an explicit "no public source used".
- [ ] Privacy grep is clean: no session IDs, IP addresses, hostnames, credentials, people's names, or private repo names in tracked files, including `work-orders/`. Paste the command and output.
- [ ] `prose-edit` contains no em dashes anywhere in its package.
- [ ] Each new SKILL.md description says when NOT to use it, and its routing negatives test that.
- [ ] validation.md separates fresh routing scores from historical ones and states what was static review versus execution.
- [ ] `git log --oneline main..HEAD` shows exactly the six commits; `git status -sb` shows nothing pushed.

## Hand back

Reply with: the acceptance checklist with evidence for each item, `git log --oneline main..HEAD`, any source you couldn't use and why, and any finding you disagree with. Don't open a PR. When the reviewer approves, update this file's status line to `done (<commit>)`.
