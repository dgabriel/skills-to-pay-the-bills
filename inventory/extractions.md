# Extraction ledger

Updated 2026-10-17. Source review decisions (keep/split/leave) and extraction dispositions are separate. The template and MysteryMixClub canonical sources declare MIT. The author-owned Cosmic JEV tester supplies the added external-oracle procedure under the owner’s explicit extraction request; no source file is copied, and no repository license declaration is inferred. Other reviewed files remain references or deferred. Exact pinned revisions are in each skill’s provenance.

| Public repository | Relative source | Review | Disposition | Library skill | What changed |
| --- | --- | --- | --- | --- | --- |
| cosmic-jev | .agents/skills/beads/SKILL.md | keep | reference | — | Corroborates repeated procedure; no source body copied. |
| cosmic-jev | .claude/agents/developer.md | split | needs-review | — | Deferred; review decision does not imply extraction. |
| cosmic-jev | .claude/agents/reviewer.md | split | reference | — | Corroborates repeated procedure; no source body copied. |
| cosmic-jev | .claude/agents/tester.md | split | merge | regression-testing | Adapt external-oracle citation/stop rule and threshold practice; exact revision and source sections in provenance. |
| cosmic-jev | AGENTS.md | split | skip | — | No verified repository license; no session instructions extracted in this pass. |
| cosmic-jev | CLAUDE.md | split | skip | — | No verified repository license; no session instructions extracted in this pass. |
| claude-code-project-template | .claude/agents/developer.md | split | needs-review | — | Deferred; review decision does not imply extraction. |
| claude-code-project-template | .claude/agents/reviewer.md | split | merge | spec-review | Read-only evidence-based review and structured verdict. |
| claude-code-project-template | .claude/agents/tester.md | split | merge | regression-testing | Behavior coverage, existing runner, exact failure handoff. |
| claude-code-project-template | .claude/agents/ui-agent.md | split | needs-review | — | Deferred; review decision does not imply extraction. |
| claude-code-project-template | CLAUDE.md | split | merge | session-start-and-close | Extract orientation/task loading and durable close handoff; leave generated blocks, stack commands and fixed branch/service policy. |
| claude-code-project-template | docs/git-hygiene.md | split | merge | git-workflow | Policy routing, preflight, published history, conflict/reconciliation. |
| MysteryMixClub | .agents/skills/beads/SKILL.md | keep | merge | beads-workflow | Durable tasks, native IDs, wrapper precedence, handoff. |
| MysteryMixClub | .agents/skills/mmc-design-system/skill.md | leave | project-only | — | Retained at source; no universal skill extracted. |
| MysteryMixClub | .agents/skills/mmc-git-hygiene/SKILL.md | split | merge | git-workflow; beads-workflow | Policy routing, preflight, published history, conflict/reconciliation. |
| MysteryMixClub | .agents/skills/mmc-issue-management/SKILL.md | split | merge | beads-workflow | Durable tasks, native IDs, wrapper precedence, handoff. |
| MysteryMixClub | .agents/skills/run-mysterymixclub/SKILL.md | split | merge | local-test-handoff | Extract branch preservation, readiness, persistent-data troubleshooting; device/account handoff comes from pattern evidence. |
| MysteryMixClub | .claude/agents/developer.md | split | needs-review | — | Deferred; review decision does not imply extraction. |
| MysteryMixClub | .claude/agents/devops.md | split | needs-review | — | Deferred; review decision does not imply extraction. |
| MysteryMixClub | .claude/agents/reviewer.md | split | merge | spec-review | Read-only evidence-based review and structured verdict. |
| MysteryMixClub | .claude/agents/tester.md | split | merge | regression-testing | Behavior coverage, existing runner, exact failure handoff. |
| MysteryMixClub | .claude/agents/ui-agent.md | split | needs-review | — | Deferred; review decision does not imply extraction. |
| MysteryMixClub | .claude/agents/uiux-designer.md | split | needs-review | — | Deferred; review decision does not imply extraction. |
| MysteryMixClub | .claude/skills/mmc-design-system/skill.md | leave | project-only | — | Retained at source; no universal skill extracted. |
| MysteryMixClub | .claude/skills/mmc-issue-management/SKILL.md | split | skip | — | Host copy retained in review table; no independent capability. |
| MysteryMixClub | .claude/skills/run-mysterymixclub/SKILL.md | split | skip | — | Host copy retained in review table; no independent capability. |
| MysteryMixClub | AGENTS.md | split | merge | session-start-and-close | Extract orientation/task loading and durable close handoff; leave generated blocks, stack commands and fixed branch/service policy. |
| MysteryMixClub | CLAUDE.md | split | merge | session-start-and-close | Extract orientation/task loading and durable close handoff; leave generated blocks, stack commands and fixed branch/service policy. |
| MysteryMixClub | docs/git-hygiene.md | split | merge | git-workflow | Policy routing, preflight, published history, conflict/reconciliation. |
| tktk | .agents/skills/beads/SKILL.md | keep | reference | — | Corroborates repeated procedure; no source body copied. |
| tktk | AGENTS.md | split | skip | — | No verified repository license; no session instructions extracted in this pass. |
| tktk | CLAUDE.md | leave | project-only | — | Retained at source; no universal skill extracted. |
| tktk | agents/developer.md | split | needs-review | — | Deferred; review decision does not imply extraction. |
| tktk | agents/product-manager.md | split | needs-review | — | Deferred; review decision does not imply extraction. |
| tktk | agents/reviewer.md | split | reference | — | Corroborates repeated procedure; no source body copied. |
| tktk | agents/tester.md | split | reference | — | Corroborates repeated procedure; no source body copied. |
| tktk | agents/ui-agent.md | split | needs-review | — | Deferred; review decision does not imply extraction. |
| tktk | docs/git-hygiene.md | split | needs-review | — | Deferred; review decision does not imply extraction. |
| tktk | prototype/AGENTS.md | split | skip | — | No verified repository license; no session instructions extracted in this pass. |
| tktk | prototype/CLAUDE.md | leave | project-only | — | Retained at source; no universal skill extracted. |

## Pilot sources outside the narrowed table

| Public repository | Relative source | Disposition | Library skill |
| --- | --- | --- | --- |
| claude-code-project-template | `docs/prd/prd-interview.md` | convert | product-requirements-interview |
| claude-code-project-template | `docs/technical/technical-design-interview.md` | convert | technical-design-interview |
| claude-code-project-template | `docs/design/style-guide-interview.md` | convert | design-system-workshop |
| claude-code-project-template | `.claude/agents/developer.md` | reference | technical-design-interview |

The developer reference contributes the explicit React/TypeScript default only. This is distinct from extracting a general implementation skill. Main-only local Git guidance was useful contrast, but unavailable at the public pinned revision; no body was copied. Branch-safe local startup now contributes to local-test-handoff; deployment and project design overlays remain deferred or project-only.

Renamed library identifiers are documented in [rename notes](../RENAMES.md). Review/source repository file names remain unchanged; no source repository was edited.

## History-derived sources and pattern evidence

The four new packages use the work order’s reviewer paraphrases, labeled in each Pattern evidence section. No session transcript was searched or read. Visibility and license metadata were checked before eligible source retrieval; exact revisions are in package provenance and the source-check record. The review-tool repository is currently public and MIT-licensed, so it is eligible here even though it was absent from the earlier account-scoped inventory.

| Public repository | Relative source | Disposition | Library skill | Contribution |
| --- | --- | --- | --- | --- |
| flaught/core | `docs/dismissals.md` | merge | review-findings-triage | Stable fingerprint versus run-local ID, tracked dismissal, expiry and recurrence |
| flaught/core | `docs/dashboard.md` | merge | review-findings-triage | Artifact-backed dashboard refresh and missing-input distinction |
| flaught/core | `docs/findings-schema.md` | reference | review-findings-triage | Source type, confidence, and analysis completeness |
| MysteryMixClub | `.advreview.yml` | reference | review-findings-triage | Explicit gate/dismissal configuration and docs-only inversion controls |
| Author-stated work-order rules | No public source file used | convert | prose-edit | Direct voice/length/punctuation rules with original examples |

The session rows above are resolved: eligible public MIT instructions were split into the session workflow; new extraction from candidates without a verified license was skipped. Earlier historical extractions under a prior work order are preserved, not claimed as new licensed-source use. Host-copy run instructions remain a duplicate skip. No source repository was edited, and no fixed address, credential, account, port, or service identity was copied.

## Follow-up candidates from reviewer paraphrases

No public source used for these additions. No session transcripts were accessed. Each package attributes the supplied reviewer paraphrases and explicit owner decisions in its provenance.

| Supplied pattern | Disposition | Destination | Decision |
| --- | --- | --- | --- |
| Confirm reported problems before repair | convert | diagnose-first | New troubleshooting workflow; rollback comparison needs owner approval and isolated worktree or branch |
| Compare documentation with behavior and missing coverage | convert | docs-audit | Factual audit; no claim of legal approval |
| Write agent briefs and assess another agent's output | convert | agent-handoff-prompt | Independently selectable; excludes session close and direct patch-versus-spec review |
| Prepare a new repository for agent development | merge | New-project starter prompt | Extend the prompt using existing skills, not a new bootstrap skill |
