# BorrowBox technical design — proposed

## Decisions and rationale
Use Python 3, Django with server-rendered templates, minimal JavaScript, and PostgreSQL. Django supplies sessions, CSRF protection, forms, migrations, and administration, keeping a 30-resident web product small. PostgreSQL supplies transactional integrity and range exclusion constraints for booking correctness. No existing stack is assumed.

Deploy one application process and PostgreSQL on a small single Linux VM, using Caddy for TLS and systemd for process management. Allocate a proposed $8/month VM ceiling, $3 backups, $2 domain amortization, $2 email, and $5 contingency. These are planning allowances, not verified vendor prices. Provider, actual prices, availability, and backup costs must be checked before commitment; if the total exceeds $20, revise hosting rather than silently exceed budget. This choice trades low cost for an operator's patching and restore responsibilities.

Use administrator-created resident accounts with Django password authentication and secure cookie sessions; restrict signup to the building's approved roster. Owner invitations and password recovery need a verified delivery channel before release. Auth and hosting choices are proposals, not supplied requirements.

## Model and invariant
Resident(id, active); Tool(id, owner_id, title, description, active); Booking(id, tool_id, borrower_id, start_date, end_date, status, created_at, returned_at). Index tool/status and borrower/status. Store audit events for acceptance/rejection/return without unnecessary personal data.

Propose building-local calendar dates with half-open ranges `[start_date,end_date)` and `start_date < end_date`; confirm this convention before implementation. Use a PostgreSQL daterange exclusion constraint keyed by tool_id for accepted bookings, with the required GiST support migration. Retain historical accepted intervals after return, either by including returned status in the constraint or preserving an immutable accepted reservation record. Never free a past accepted reservation by erasing history.

## Operations
Authenticate every operation and scope reads to building residents. Owners manage their own listings. Borrowers submit valid requests; only the tool owner can atomically change a pending request to accepted or rejected. In one database transaction, validate actor and pending state, attempt acceptance, and let the database constraint reject conflicting accepted dates. Convert a conflict into a clear availability error and leave the original pending state intact. Lock the booking row to serialize competing decisions; the database constraint protects cross-request races.

Only that booking's borrower can record return from accepted to returned. Make retries idempotent and retain original dates. Pending requests may overlap; acceptance determines reservation. Explicitly reject invalid transitions and forged IDs. No payments, chat, insurance, or realtime service.

## Web and operations
Provide listing/search, tool detail and date-request form, my requests, owner request inbox, and return action. Use standard POST/redirect/GET, server-side validation, CSRF protection, escaped templates, HTTPS-only secure cookies, and login throttling. Polling/manual refresh is sufficient. Start with text listings; file uploads and email notifications are deferred until needed and budgeted.

Run migrations during a controlled deployment, take daily encrypted off-host backups with a proposed seven-day retention, and test restore before launch. Keep secrets outside source control. Capture errors, disk usage, database health, and monthly spend; assign an operator and document rollback and resident support. A single VM is a known availability limitation.

## Verification and release
Test authorization for foreign tool/booking IDs; invalid ranges; adjacent, nested and overlapping dates; two concurrent acceptance attempts using separate database connections; rejected transaction state preservation; duplicate returns; CSRF and login flows; and restore from backup. SQLite-only tests cannot validate the PostgreSQL exclusion invariant. Pilot the full listing → request → owner decision → borrower return loop before inviting all residents.

Unknowns: date/time-zone semantics, cancellation and overdue policy, resident roster ownership, recovery channel, data retention, operator, and actual hosting quotes. No code, deployment, or tests were executed for this design.
