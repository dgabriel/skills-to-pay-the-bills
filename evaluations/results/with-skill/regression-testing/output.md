# Test result: FAIL

Oracle: SPEC.md defines valid half-open integer ranges [start,end), adjacent intervals do not overlap, and either start >= end raises ValueError. Test expectations use explicit examples from that definition, independent of booking.overlaps.

Executed `python3 -m unittest -v test_booking.py` in this fixture, exit code 1. Exact stdout/stderr retained in test-results.txt. Ran 12 tests in 0.001s: 9 passed, 3 failed; no collection/environment errors.

Failures:
- test_booking.py:14, OverlapTests.test_adjacent_forward: (1,3) and (3,6), expected False, actual True.
- test_booking.py:16, OverlapTests.test_adjacent_reverse: (3,6) and (1,3), expected False, actual True.
- test_booking.py:20, OverlapTests.test_negative_adjacent: (-5,-2) and (-2,0), expected False, actual True.

Each failure emitted `AssertionError: True is not false`. booking.py:4 uses inclusive <= comparisons and incorrectly counts shared endpoints. This violates half-open interval semantics. Implementation was not changed and assertions were not weakened.

Passing coverage: separated intervals; partial overlap; containment; identical ranges; one-unit overlap; empty and reversed first/second ranges raising ValueError. The forward adjacency, one-unit overlap, and separated cases bracket the endpoint threshold. One-unit overlap duplicates the partial example; counts above reflect actual runner output, not unique semantic cases.

Only the requested focused standard-library suite ran; no broader suite/config was supplied, no network or installs used. Handoff: implementation owner should use strict endpoint intersection comparisons and rerun these regressions. No open spec decision blocks that fix.
