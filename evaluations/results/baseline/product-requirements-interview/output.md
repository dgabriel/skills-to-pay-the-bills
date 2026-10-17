# BorrowBox MVP PRD — draft

## Purpose and users
Help 30 residents in one apartment building borrow tools from neighbors through a small web application. An owner lists a tool, a neighbor requests dates, the owner accepts or rejects, and the borrower records its return. Budget: $20/month. All unconfirmed decisions below are proposals.

## Recommended scope
Include resident access, tool listings, date requests, owner acceptance/rejection, request status, and return recording. Exclude payments, chat, ratings, and insurance from MVP: each adds substantial operational, trust, or implementation complexity before the basic borrowing loop is proven. These remain proposals for later evaluation, not commitments. Provide concise pickup/return instructions with a listing or acceptance instead of building messaging.

## Behaviors and acceptance criteria
- Residents can create, edit, and deactivate their own listings with title, description, condition, and pickup instructions. Another resident cannot edit them.
- A resident can request an active tool for a valid start/end range; show pending, accepted, rejected, and returned states clearly.
- Only a tool's owner can accept or reject its requests. Acceptance must prevent overlapping accepted bookings, including simultaneous attempts.
- The borrower can mark their accepted loan returned. Preserve history and prevent unauthorized state transitions. Owner confirmation or disputes are unresolved policy questions; do not silently assume them required.
- Residents can see their own requests and requests concerning their tools. Show clear feedback for failed actions, empty states, and unavailable dates.
- Core flows work with keyboard navigation and on a narrow mobile browser; no native mobile app.

## Success and release
Proposed pilot targets: at least five successful return-recorded loans in the first month, no double bookings or unauthorized decisions, and most observed users completing a request without assistance. Instrument counts and timestamps without collecting unnecessary personal data. These targets need owner agreement.

Release to a few residents first, validate the complete listing-to-return flow and concurrent acceptance prevention, then invite all 30. Keep recurring infrastructure and delivery costs under $20/month and define who monitors them. No implementation or launch is authorized by this PRD.

## Open decisions and risks
Confirm resident verification and administrator ownership; borrowing date semantics/time zone; maximum duration and advance notice; cancellation, overdue and damaged-tool policies; pickup coordination and contact visibility; notifications; retention/deletion; support responsibility; and whether budget includes domain and email. There is no established baseline or research evidence for demand. Validate with a small pilot before expanding scope. Insurance exclusion requires a clear community agreement on responsibility, without representing that agreement as insurance coverage.
