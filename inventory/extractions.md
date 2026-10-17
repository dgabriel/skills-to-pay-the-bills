# Extraction ledger

Updated 2026-10-17. Source review decisions (keep/split/leave) and extraction dispositions are separate. The template and MysteryMixClub canonical sources declare MIT. The author-owned Cosmic JEV tester supplies the added external-oracle procedure under the owner’s explicit extraction request; no source file is copied, and no repository license declaration is inferred. Other reviewed files remain references or deferred. Exact pinned revisions are in each skill’s provenance.

| Public repository | Relative source | Review | Disposition | Library skill | What changed |
| --- | --- | --- | --- | --- | --- |
| cosmic-jev | .agents/skills/beads/SKILL.md | keep | reference | — | Corroborates repeated procedure; no source body copied. |
| cosmic-jev | .claude/agents/developer.md | split | needs-review | — | Deferred; review decision does not imply extraction. |
| cosmic-jev | .claude/agents/reviewer.md | split | reference | — | Corroborates repeated procedure; no source body copied. |
| cosmic-jev | .claude/agents/tester.md | split | merge | regression-testing | Adapt external-oracle citation/stop rule and threshold practice; exact revision and source sections in provenance. |
| cosmic-jev | AGENTS.md | split | needs-review | — | Deferred; review decision does not imply extraction. |
| cosmic-jev | CLAUDE.md | split | needs-review | — | Deferred; review decision does not imply extraction. |
| claude-code-project-template | .claude/agents/developer.md | split | needs-review | — | Deferred; review decision does not imply extraction. |
| claude-code-project-template | .claude/agents/reviewer.md | split | merge | spec-review | Read-only evidence-based review and structured verdict. |
| claude-code-project-template | .claude/agents/tester.md | split | merge | testing | Behavior coverage, existing runner, exact failure handoff. |
| claude-code-project-template | .claude/agents/ui-agent.md | split | needs-review | — | Deferred; review decision does not imply extraction. |
| claude-code-project-template | CLAUDE.md | split | needs-review | — | Deferred; review decision does not imply extraction. |
| claude-code-project-template | docs/git-hygiene.md | split | merge | git-workflow | Policy routing, preflight, published history, conflict/reconciliation. |
| MysteryMixClub | .agents/skills/beads/SKILL.md | keep | merge | beads-workflow | Durable tasks, native IDs, wrapper precedence, handoff. |
| MysteryMixClub | .agents/skills/mmc-design-system/skill.md | leave | project-only | — | Retained at source; no universal skill extracted. |
| MysteryMixClub | .agents/skills/mmc-git-hygiene/SKILL.md | split | merge | git-workflow; beads-workflow | Policy routing, preflight, published history, conflict/reconciliation. |
| MysteryMixClub | .agents/skills/mmc-issue-management/SKILL.md | split | merge | beads-workflow | Durable tasks, native IDs, wrapper precedence, handoff. |
| MysteryMixClub | .agents/skills/run-mysterymixclub/SKILL.md | split | needs-review | — | Deferred; review decision does not imply extraction. |
| MysteryMixClub | .claude/agents/developer.md | split | needs-review | — | Deferred; review decision does not imply extraction. |
| MysteryMixClub | .claude/agents/devops.md | split | needs-review | — | Deferred; review decision does not imply extraction. |
| MysteryMixClub | .claude/agents/reviewer.md | split | merge | spec-review | Read-only evidence-based review and structured verdict. |
| MysteryMixClub | .claude/agents/tester.md | split | merge | testing | Behavior coverage, existing runner, exact failure handoff. |
| MysteryMixClub | .claude/agents/ui-agent.md | split | needs-review | — | Deferred; review decision does not imply extraction. |
| MysteryMixClub | .claude/agents/uiux-designer.md | split | needs-review | — | Deferred; review decision does not imply extraction. |
| MysteryMixClub | .claude/skills/mmc-design-system/skill.md | leave | project-only | — | Retained at source; no universal skill extracted. |
| MysteryMixClub | .claude/skills/mmc-issue-management/SKILL.md | split | skip | — | Host copy retained in review table; no independent capability. |
| MysteryMixClub | .claude/skills/run-mysterymixclub/SKILL.md | split | skip | — | Host copy retained in review table; no independent capability. |
| MysteryMixClub | AGENTS.md | split | needs-review | — | Deferred; review decision does not imply extraction. |
| MysteryMixClub | CLAUDE.md | split | needs-review | — | Deferred; review decision does not imply extraction. |
| MysteryMixClub | docs/git-hygiene.md | split | merge | git-workflow | Policy routing, preflight, published history, conflict/reconciliation. |
| tktk | .agents/skills/beads/SKILL.md | keep | reference | — | Corroborates repeated procedure; no source body copied. |
| tktk | AGENTS.md | split | needs-review | — | Deferred; review decision does not imply extraction. |
| tktk | CLAUDE.md | leave | project-only | — | Retained at source; no universal skill extracted. |
| tktk | agents/developer.md | split | needs-review | — | Deferred; review decision does not imply extraction. |
| tktk | agents/product-manager.md | split | needs-review | — | Deferred; review decision does not imply extraction. |
| tktk | agents/reviewer.md | split | reference | — | Corroborates repeated procedure; no source body copied. |
| tktk | agents/tester.md | split | reference | — | Corroborates repeated procedure; no source body copied. |
| tktk | agents/ui-agent.md | split | needs-review | — | Deferred; review decision does not imply extraction. |
| tktk | docs/git-hygiene.md | split | needs-review | — | Deferred; review decision does not imply extraction. |
| tktk | prototype/AGENTS.md | split | needs-review | — | Deferred; review decision does not imply extraction. |
| tktk | prototype/CLAUDE.md | leave | project-only | — | Retained at source; no universal skill extracted. |

## Pilot sources outside the narrowed table

| Public repository | Relative source | Disposition | Library skill |
| --- | --- | --- | --- |
| claude-code-project-template | `docs/prd/prd-interview.md` | convert | product-requirements-interview |
| claude-code-project-template | `docs/technical/technical-design-interview.md` | convert | technical-design-interview |
| claude-code-project-template | `docs/design/style-guide-interview.md` | convert | design-system-workshop |
| claude-code-project-template | `.claude/agents/developer.md` | reference | technical-design-interview |

The developer reference contributes the explicit React/TypeScript default only. This is distinct from extracting a general implementation skill. Main-only local Git guidance was useful contrast, but unavailable at the public pinned revision; no body was copied. Startup/deployment and project design skills remain deferred or project-only.

Renamed library identifiers are documented in [rename notes](../RENAMES.md). Review/source repository file names remain unchanged; no source repository was edited.
