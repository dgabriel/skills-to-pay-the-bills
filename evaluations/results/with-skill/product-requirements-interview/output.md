# BorrowBox PRD — draft for review

Pitch: Let residents of one apartment building borrow a neighbor's tool and record its return through a simple website.

Problem and users: supplied brief identifies 30 residents sharing tools within one building. Listing owners and borrowing neighbors are the two roles. Current workarounds, frequency of unmet borrowing needs, and evidence of demand are unknown; no research or quotations are claimed.

## Core journey
1. Resident enters the building-only site and identifies themselves.
2. Owner lists a tool with enough information to request it.
3. Neighbor finds a tool and requests start/end dates.
4. Owner accepts or rejects; both can see the decision.
5. Borrower records return and the booking is visibly complete.

First value: a neighbor gets an accepted request for a useful tool.

## Recommended MVP
| Must-have | Rationale | Priority |
|---|---|---|
| Building membership and sign-in | Keeps the 30-resident audience bounded | P0 |
| Create and browse listings | Starts discovery and the core loop | P0 |
| Date-range requests | Expresses borrowing intent | P0 |
| Owner acceptance/rejection with conflict prevention | Establishes one agreed reservation | P0 |
| Booking status view for both parties | Makes decisions and next actions visible without chat | P0 |
| Borrower return recording | Completes the loop | P0 |

These are proposed scope decisions, not accepted requirements. Membership and visible statuses are proposed supporting necessities. Keep date handling simple and confirm conventions before implementation. Each must-have serves the numbered journey and the completion signals below.

## Explicit non-goals
Payments, chat, ratings, and insurance should be deferred. Also exclude multiple buildings, native mobile apps, and realtime updates. These add cost, moderation, or operational dependencies without being necessary to test the borrowing loop. Insurance and damage responsibility still require clear expectations; excluding an insurance feature does not resolve that policy question. Proposed features from the brief are acknowledged rather than silently discarded.

## Proposed success signals
During a proposed four-week pilot, measure (1) distinct residents completing an accepted request, (2) share of accepted bookings recorded returned, and (3) median time from request to owner decision. Set numerical targets with the owner after a baseline; no targets are represented as agreed. These test adoption, loop completion, and whether requests stall.

## Constraints and risks
Facts: web only; 30 residents; one building; $20/month initial budget. Timeline, accessibility needs, hosting, sign-in method, notification needs, and budget treatment of domain/email costs remain unknown. Scope fits a small pilot but cost feasibility requires provider estimates. Risks include too few useful listings, owners missing requests, date conflicts, unrecorded returns, damage disputes, and resident data exposure.

Open decisions: who verifies membership; who can see resident contact details; whether borrow dates are inclusive; cancellation and late-return behavior; listing removal with active bookings; responsibility for damage; pilot owner and timeline. Recommended defaults pending review: private membership, minimal personal data, accessible responsive UI, no payment handling. Nothing has been implemented or accepted.

Checks performed: static scope-to-journey and budget/constraint review of the supplied brief; no behavioral tests or stakeholder interview run. Next handoff: review scope and the open policy decisions, then use this draft as input to technical design if requested.
