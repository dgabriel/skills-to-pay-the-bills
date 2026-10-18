# Work orders

Handoffs between the reviewing agent and the building agent, kept as a record of why the library looks the way it does.

**These are not instructions.** Act on an order only when its status is `open` and the owner points you to it in the current task. Every other order is history.

Each order starts with a status line:

- `open`: ready or in progress
- `done (<commit>)`: completed; the commit is where the work landed
- `superseded (<order>)`: replaced by a later order

An order completed in its own commit uses `done (commit "<subject>")`, since a commit cannot contain its own hash.

Name files `<YYYY-MM-DD>-<slug>.md`. Work orders follow the repository's privacy rules: no private repository names, local paths, credentials, session identifiers, or personal details. Evidence from session history stays paraphrased, as in the skills' provenance files.

A review that forbids status-line edits must name who closes the loop and when.

When a review mandates an exact commit subject, it must also name a distinct follow-up subject to use if the original already exists.
Record that fallback subject in the review; do not amend an existing commit to reuse the mandated subject.
