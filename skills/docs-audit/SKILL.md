---
name: docs-audit
description: Audit project documentation for factual accuracy and missing coverage against code and configuration, including help, privacy, terms, about, and architecture diagrams when requested. Not prose-only polishing, patch review against a spec, or legal approval.
---

# Docs Audit

**Inputs:** Documentation scope, repository/configuration, known runtime evidence, audience, and any requested diagram or documentation deliverable.
**Output:** Evidence-linked mismatches, missing documentation inventory, verification limits, and requested drafts or diagrams.
**Try:** “Audit our help and privacy pages against the implementation and list missing docs.” (use the skill name in your host's invocation syntax).

Honor task scope and project policy; preserve unrelated work. Read the [procedure](references/procedure.md) for details and the [shared contract](references/execution-contract.md) for authority boundaries.

1. Inventory the requested documentation and relevant code/configuration. Identify intended readers and missing topics before rewriting.
2. Trace factual claims to implementation, tests, or runtime evidence; distinguish confirmed mismatches from deployment-dependent unknowns.
3. Report findings with document location, claim, evidence, impact, and correction or verification needed. Privacy/terms checks never claim legal approval.
4. When requested, write missing documentation and readable architecture diagrams from verified facts. Label proposals and unknowns; report actual checks separately.

Report actual checks, unresolved decisions, and the next handoff. See [provenance and pattern evidence](PROVENANCE.md).
