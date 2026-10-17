"""Independent expectations from SPEC.md: integer, half-open ranges."""
import unittest
from booking import overlaps


class OverlapTests(unittest.TestCase):
    def test_disjoint_and_overlapping_ranges(self):
        # SPEC.md: [start,end) excludes end; each listed expectation is literal.
        cases = [
            ((0, 4, 1, 3), True),   # containment
            ((1, 3, 0, 4), True),
            ((0, 3, 0, 3), True),   # identical ranges
            ((0, 3, 2, 5), True),   # partial overlap
            ((2, 5, 0, 3), True),
            ((-5, -1, -3, 0), True),
            ((0, 2, 3, 5), False),  # gap
            ((3, 5, 0, 2), False),
        ]
        for args, expected in cases:
            with self.subTest(args=args):
                self.assertIs(overlaps(*args), expected)

    def test_half_open_boundary_below_on_above(self):
        # SPEC.md: relative to A's end 3, B starts at 2/3/4.
        for start, expected in [(2, True), (3, False), (4, False)]:
            for args in [(0, 3, start, 6), (start, 6, 0, 3)]:
                with self.subTest(args=args):
                    self.assertIs(overlaps(*args), expected)

    def test_invalid_ranges_raise_value_error(self):
        # SPEC.md: both ranges require start < end, including equal endpoints.
        for args in [(1, 1, 2, 3), (2, 1, 2, 3),
                     (0, 1, 3, 3), (0, 1, 4, 3),
                     (1, 1, 3, 3)]:
            with self.subTest(args=args):
                with self.assertRaises(ValueError):
                    overlaps(*args)


if __name__ == "__main__":
    unittest.main()
