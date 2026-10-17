# Documentation audit procedure

## Scope and coverage

Read project instructions and establish the requested scope and audience. Inventory relevant README/setup material, help, privacy, terms, about pages, operational guidance, and architecture documents. Compare that inventory with actual user journeys, developer tasks, configuration, and system boundaries. List documentation that is missing, stale, contradictory, or difficult to find, with a concrete reader/task it should support. An audit does not imply rewriting every document.

## Trace claims to behavior

For each consequential claim, record the document location and exact claim or a faithful short paraphrase. Inspect the implementing code, configuration defaults, migrations, tests, and available runtime evidence. Trace collection, storage, retention/deletion, sharing, account actions, and external integrations where privacy or terms make factual assertions. A dependency's presence does not prove it is enabled or deployed. Distinguish repository defaults from actual deployment settings and identify the evidence needed to settle uncertainty. Do not access production data or credentials to complete an audit.

Report confirmed factual mismatches separately from missing evidence and possible omissions. Privacy and terms review is a factual consistency check, never a statement of legal approval, enforceability, or regulatory compliance. Refer legal decisions to the owner; do not invent retention periods, guarantees, or contractual promises. Avoid quoting private data in examples.

## Findings and requested writing

Return an evidence table: document/location, claim or missing topic, implementation/configuration reference, observed mismatch or uncertainty, impact, and proposed correction or next verification. Prioritize inaccurate consequential claims over wording preferences. Report inspected scope and excluded or inaccessible areas, even when no mismatch is found.

If asked to write or update documents, preserve established structure and confirmed facts. For architecture, show real components, ownership, interfaces, data flow, and external boundaries using a readable diagram such as Mermaid. Distinguish current behavior from proposed design. Use project-relative paths and placeholders, not machine paths or secrets. Check document links and diagram syntax when tooling is available; say if rendering was not verified. Do not represent a drafted correction as implemented behavior or an unexecuted runtime check as evidence.
