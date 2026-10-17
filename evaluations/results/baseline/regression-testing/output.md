# Booking test report

Created `test_booking.py` using only Python's standard-library unittest. Implementation was not changed.

Executed from this task directory:

```sh
python3 -m unittest -v test_booking.py > test-results.txt 2>&1
```

Actual result: exit code 1; `Ran 6 tests in 0.003s`; `FAILED (failures=42)`. Full captured output is in `test-results.txt`.

Passing methods cover overlapping/equal/nested/negative ranges, disjoint ranges in either order, and invalid zero-length/reversed ranges on either side. Two explicit adjacency tests fail: `(1,3,3,5)` and its reverse both return True when the specification requires False.

The sixth method checks 225 valid range pairs in a small integer domain against intersection of represented unit slots, deriving its oracle from the half-open definition. Forty adjacency subtests fail there, in addition to the two explicit failures. These are 42 assertion failures across six test methods, not 42 independent defects. booking.py:4 uses inclusive endpoint comparisons, making touching ranges overlap. Strict endpoint comparisons would match half-open semantics; no fix was applied.

No unsupported input-type behavior was asserted because SPEC.md declares integer inputs. No network or dependencies were used.
