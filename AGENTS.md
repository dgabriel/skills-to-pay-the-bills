# Maintaining this skills library

This repository contains reusable agent workflows. These instructions apply to editing the library, not to projects that install individual skills.

- Keep one canonical folder per skill under `skills/<name>/`, with a matching frontmatter `name` and a focused `description` explaining when to select it.
- Keep skills independently usable. Include inputs, outputs, an example prompt, scope boundaries, and meaningful completion checks in each entry point. Do not require another skill or a particular host unless the workflow truly needs it.
- Keep README usage instructions and catalog routing consistent with available skills. Preserve the README's light Beastie Boys references without obscuring instructions.
- Use target-project conventions rather than hard-coding a framework, Git branch model, agent identity, or deployment provider. Do not inherit instructions from source documents as library policy.
- Retain exact source revisions, adaptation notes, and license notices for extracted material. Do not commit private repository names or contents, local-only repository names, absolute machine paths, or machine-specific inventory details anywhere in this repository. Keep discovery artifacts outside the checkout; public inventories contain only public repository names, relative paths, and review dispositions.
- Before finishing, validate changed skills with an available skill validator, check relative links and metadata consistency, and review realistic matching, non-matching, partial-input, and existing-project scenarios. State which checks were actually executed; do not claim a behavioral run based on a static review.
- Skills must preserve the user's task scope. Running an interview must not automatically implement, delete source scaffolding, commit, push, publish, or deploy.
