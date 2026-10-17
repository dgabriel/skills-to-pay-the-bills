# FAIL

High — `after.py:4`: authorization happens after state mutation. For an existing booking owned by Alice, calling `cancel(booking, "Bob")` first sets `booking.status = "cancelled"`, then returns `"forbidden"` at lines 5–6. Requirements require both owner-only cancellation and unchanged state after rejection. This permits unauthorized cancellation despite an error response. Move the owner check before mutation; this is a correction direction only, no code edited.

Medium — `test_cancel.py:2`: the assertion checks only the returned status, which the defective patch still satisfies. Add an assertion that a non-owner's rejection leaves the original status unchanged. Also cover the owner success and missing-booking paths.

Checks: statically compared before.py, after.py, requirements.md, and test_cancel.py and traced each return path. Missing booking remains `not_found`; owner cancellation remains `ok`. No tests executed: the supplied snippet lacks imports and fixture definitions and this request is read-only. No unresolved requirement blocks diagnosis. Handoff: fix authorization ordering and add side-effect regression coverage before reconsidering approval.
