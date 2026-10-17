---
name: product-requirements-interview
description: Turn a product idea into a focused PRD through staged questions. Use when defining or revising product requirements or MVP scope; not for implementing an already specified feature.
---

# Product Requirements Interview

## Use this skill

Human prompt: “Use $product-requirements-interview to help define the MVP for my neighborhood tool-sharing app.”

Inputs: an idea or existing brief, intended users, and any known constraints. No prior specification is required. Read existing discovery and requirements before asking questions; summarize what is already known and ask only about gaps or conflicts.

Output: a reviewable PRD, normally `docs/prd/prd.md` in the target project. Respect the requested location and existing document structure. In a chat-only environment, provide the draft inline. This skill works independently; architecture and visual design are optional follow-ups.

## Run the interview

Ask one short round at a time, reflect the answers, and adapt subsequent questions. Do not ask all rounds at once. If the supplied brief already answers a round, confirm only consequential ambiguities.

1. **Problem and audience:** identify a specific user, their problem in their words, their current workaround, and why this product is worth building now.
2. **Core experience:** shape a one-sentence pitch, walk through a normal user visit, and identify the first moment of value.
3. **Scope:** distinguish essential v1 features from later ideas. If roughly six or more items are called essential, ask which are truly necessary for the core journey. Record explicit non-goals and platform, budget, timeline, and service constraints without inventing them.
4. **Success and uncertainty:** choose one to three observable success signals; identify adoption, delivery, or dependency risks and unresolved decisions.

If the user asks for an initial draft without an interview, draft from supplied evidence and label assumptions and unanswered questions. Do not imply that silence confirms a decision. On pause, preserve a partial draft with answered questions and the next unresolved round; do not mark it approved.

## Produce and check the PRD

Include pitch, problem, users, core user journey, MVP scope with rationale and priority, non-goals, success signals, constraints, and risks/open questions. Link existing discovery where useful. Use the user's language for the problem; distinguish their statements from proposals.

Check that each must-have supports the core journey, success signals are observable, constraints remain consistent, and unknowns are explicit. Present the draft for review and incorporate feedback. Report whether it is a draft or explicitly accepted; unresolved critical requirements remain visible.

Work in the target project, not the installed skill directory. Preserve existing content when updating a PRD. Do not implement the product, delete interview sources, or commit, push, publish, or deploy merely because this interview ran. If architecture is next, hand off the PRD path and unresolved constraints; another installed skill is not required.

## Source

Adapted from [docs/prd/prd-interview.md](https://github.com/dgabriel/claude-code-project-template/blob/59616904f514d6351b8d8de1d6e16ae708057dc3/docs/prd/prd-interview.md). See [PROVENANCE.md](PROVENANCE.md) for revision and adaptation details.
