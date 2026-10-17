# Public instruction-source review

Reviewed 2026-10-17. This replaces the broad machine-specific inventory with a narrowly scoped candidate table. Only public repository names and repository-relative paths are included; no source bodies are copied.

## Scope and decision vocabulary

The table covers skill entry points (case-insensitive filename), agent definitions, project instruction files including nested entry points, and Git hygiene documents found in the initial local scan for public, non-fork repositories. It is a local-snapshot review, not a fresh remote-content audit. Local revisions may be ahead of published files; verify exact remote revisions and licenses before extraction. The library itself is excluded as an output, rather than counted as a source. Private and local-only sources are excluded.

- **keep**: already reusable within its stated tool/domain boundary; consolidate and validate.
- **split**: extract the general procedure and retain project details at the source.
- **leave**: project-specific content or a host shim; do not turn it into a library skill.

These describe source decisions. The extraction ledger can separately use **convert / merge / reference / project-only / skip / needs-review**. A keep or split decision is a candidate, not evidence that a conversion has been completed.

## Proposed source decisions

| Repository | Relative path | Decision | Rationale |
| --- | --- | --- | --- |
| cosmic-jev | `.agents/skills/beads/SKILL.md` | keep | Canonical Beads procedure; consolidate identical public copies and verify CLI assumptions. |
| cosmic-jev | `.claude/agents/developer.md` | split | Keep scoped implementation and explicit handoff; leave framework details, domain constraints, and mandatory role delegation. |
| cosmic-jev | `.claude/agents/reviewer.md` | split | Keep evidence-based findings and spec/security checks; leave domain invariants and project-specific approval rules. |
| cosmic-jev | `.claude/agents/tester.md` | split | Keep happy/edge/error coverage, independent expected values, and exact failure reports; leave commands, fixtures, and domain cases. |
| cosmic-jev | `AGENTS.md` | split | Extract repeated session/handoff and policy-discovery procedures; leave stack, milestone, services, and generated integration blocks. |
| cosmic-jev | `CLAUDE.md` | split | Extract repeated session/handoff and policy-discovery procedures; leave stack, milestone, services, and generated integration blocks. |
| claude-code-project-template | `.claude/agents/developer.md` | split | Keep scoped implementation and explicit handoff; leave framework details, domain constraints, and mandatory role delegation. |
| claude-code-project-template | `.claude/agents/reviewer.md` | split | Keep evidence-based findings and spec/security checks; leave domain invariants and project-specific approval rules. |
| claude-code-project-template | `.claude/agents/tester.md` | split | Keep happy/edge/error coverage, independent expected values, and exact failure reports; leave commands, fixtures, and domain cases. |
| claude-code-project-template | `.claude/agents/ui-agent.md` | split | Keep design-token discovery and UI verification procedure; leave brand, framework, and project-specific role wiring. |
| claude-code-project-template | `CLAUDE.md` | split | Extract repeated session/handoff and policy-discovery procedures; leave stack, milestone, services, and generated integration blocks. |
| claude-code-project-template | `docs/git-hygiene.md` | split | Extract repository-policy discovery, preflight, conflict handling, and reconciliation; keep branch/release rules as project policy. |
| MysteryMixClub | `.agents/skills/beads/SKILL.md` | keep | Canonical Beads procedure; consolidate identical public copies and verify CLI assumptions. |
| MysteryMixClub | `.agents/skills/mmc-design-system/skill.md` | leave | Project palette, typography, motifs, and signal policy; retain in the project rather than universalize. |
| MysteryMixClub | `.agents/skills/mmc-git-hygiene/SKILL.md` | split | Keep policy-discovery and operation routing; leave project paths and issue-start wrapper in the project. |
| MysteryMixClub | `.agents/skills/mmc-issue-management/SKILL.md` | split | Keep claim/close, durable tasks, and legacy-ID lookup; leave migration history, branch policy, and local memory wiring. |
| MysteryMixClub | `.agents/skills/run-mysterymixclub/SKILL.md` | split | Keep branch-preserving startup, readiness checks, and smoke-test procedure; leave ports, services, driver paths, and environment details. |
| MysteryMixClub | `.claude/agents/developer.md` | split | Keep scoped implementation and explicit handoff; leave framework details, domain constraints, and mandatory role delegation. |
| MysteryMixClub | `.claude/agents/devops.md` | split | Keep deployment preflight, verification, and rollback procedure; leave infrastructure identities and release policy. |
| MysteryMixClub | `.claude/agents/reviewer.md` | split | Keep evidence-based findings and spec/security checks; leave domain invariants and project-specific approval rules. |
| MysteryMixClub | `.claude/agents/tester.md` | split | Keep happy/edge/error coverage, independent expected values, and exact failure reports; leave commands, fixtures, and domain cases. |
| MysteryMixClub | `.claude/agents/ui-agent.md` | split | Keep design-token discovery and UI verification procedure; leave brand, framework, and project-specific role wiring. |
| MysteryMixClub | `.claude/agents/uiux-designer.md` | split | Keep design-token discovery and UI verification procedure; leave brand, framework, and project-specific role wiring. |
| MysteryMixClub | `.claude/skills/mmc-design-system/skill.md` | leave | Project palette, typography, motifs, and signal policy; retain in the project rather than universalize. |
| MysteryMixClub | `.claude/skills/mmc-issue-management/SKILL.md` | split | Keep claim/close, durable tasks, and legacy-ID lookup; leave migration history, branch policy, and local memory wiring. |
| MysteryMixClub | `.claude/skills/run-mysterymixclub/SKILL.md` | split | Keep branch-preserving startup, readiness checks, and smoke-test procedure; leave ports, services, driver paths, and environment details. |
| MysteryMixClub | `AGENTS.md` | split | Extract repeated session/handoff and policy-discovery procedures; leave stack, milestone, services, and generated integration blocks. |
| MysteryMixClub | `CLAUDE.md` | split | Extract repeated session/handoff and policy-discovery procedures; leave stack, milestone, services, and generated integration blocks. |
| MysteryMixClub | `docs/git-hygiene.md` | split | Extract repository-policy discovery, preflight, conflict handling, and reconciliation; keep branch/release rules as project policy. |
| tktk | `.agents/skills/beads/SKILL.md` | keep | Canonical Beads procedure; consolidate identical public copies and verify CLI assumptions. |
| tktk | `AGENTS.md` | split | Extract repeated session/handoff and policy-discovery procedures; leave stack, milestone, services, and generated integration blocks. |
| tktk | `CLAUDE.md` | leave | Host import shim; no independent workflow to extract. |
| tktk | `agents/developer.md` | split | Keep scoped implementation and explicit handoff; leave framework details, domain constraints, and mandatory role delegation. |
| tktk | `agents/product-manager.md` | split | Keep scope checks and acceptance criteria; leave milestone exclusions and domain entities. |
| tktk | `agents/reviewer.md` | split | Keep evidence-based findings and spec/security checks; leave domain invariants and project-specific approval rules. |
| tktk | `agents/tester.md` | split | Keep happy/edge/error coverage, independent expected values, and exact failure reports; leave commands, fixtures, and domain cases. |
| tktk | `agents/ui-agent.md` | split | Keep design-token discovery and UI verification procedure; leave brand, framework, and project-specific role wiring. |
| tktk | `docs/git-hygiene.md` | split | Extract repository-policy discovery, preflight, conflict handling, and reconciliation; keep branch/release rules as project policy. |
| tktk | `prototype/AGENTS.md` | split | Extract repeated session/handoff and policy-discovery procedures; leave stack, milestone, services, and generated integration blocks. |
| tktk | `prototype/CLAUDE.md` | leave | Host import shim; no independent workflow to extract. |

40 files: 3 keep, 4 leave, 33 split.

## Repetition and recommended next skills

1. **git-workflow** — compare all three Git hygiene documents plus the existing Git router. Discover the target repository’s policy; preserve its mainline or staging model.
2. **beads / issue-workflow** — consolidate the three byte-identical public Beads entry points. Split the richer project issue procedure into reusable tracking and project overlays. Do not import outdated branch instructions from issue guidance over canonical Git policy.
3. **code-review** — merge repeated reviewer procedures; preserve concrete evidence, spec compliance, and domain-specific checklists as references.
4. **testing** — merge repeated tester procedures, including independent expected values and exact failure reports; discover actual commands and shared-resource constraints.

Repeated host copies are recorded separately so they remain visible rather than inflated into distinct capabilities. Matching procedures across different projects are stronger evidence than a duplicated host installation alone.

## Existing pilot and corrections still pending

The three current pilot skills derive from the public template repository’s interview documents, which are outside this narrowed candidate table. The design workshop did not incorporate the project design skill; its appearance in the previous candidate proposal was not provenance. Per-skill provenance, concise entry points with detailed references, explicit overridable defaults, dual-host usage, and behavioral evaluations remain scheduled after review of this table.

## Inventory handling

The original full inventory is held outside the checkout. It must not be reintroduced into tracked files or distributed skills. The approved history cleanup replaces the initial branch commit; earlier copies or cached commit pages may remain outside the current branch history. No private source names or machine paths are needed to maintain this public review.
