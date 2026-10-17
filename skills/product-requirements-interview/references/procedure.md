# PRD interview procedure

## Four rounds

1. Problem/users: who narrowly needs this, what hurts in their words, current workaround, and why build now?
2. Solution: one-sentence pitch, normal visit from start to finish, and the first moment of value.
3. Scope: what must ship for that journey to work? Push back when the must-have list grows past roughly six. Separate later features, record at least three useful explicit non-goals when possible, and identify platform, budget, service, and timeline constraints.
4. Success/risks: one to three observable signals, the strongest adoption/dependency/delivery risks, and unresolved decisions.

Ask one short round at a time. Confirm only consequential ambiguity in an existing brief. Recommended defaults are scope-shaping prompts, not permission to discard explicit requirements. Explain tradeoffs and get decisions where needed. Never invent user quotes, research, budgets, or approval.

## Output

Use the requested location and existing structure. Otherwise write `docs/prd/prd.md` with pitch, problem, users, numbered core journey, MVP scope (feature/rationale/priority), non-goals, success signals, constraints, risks/open questions. Link existing discovery. Check every must-have against the core journey and success signals; flag assumptions distinctly from facts. In chat-only use, draft inline.

Review the draft with the user and revise; do not demand approval before producing a useful draft. Mark draft versus explicitly accepted status. A paused interview retains completed rounds, partial draft, and next question. An unattended draft records unknowns rather than simulating answers. Hand off the artifact path, constraints, status, and unresolved questions to architecture or visual design if requested.
