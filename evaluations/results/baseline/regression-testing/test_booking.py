import unittest
from booking import overlaps


class OverlapTests(unittest.TestCase):
    def test_overlapping_ranges(self):
        for ranges in [(1, 4, 3, 6), (1, 6, 2, 3), (2, 3, 1, 6),
                       (1, 4, 1, 4), (-4, 0, -2, 2), (0, 1, 0, 2)]:
            with self.subTest(ranges=ranges):
                self.assertIs(overlaps(*ranges), True)

    def test_disjoint_ranges(self):
        for ranges in [(1, 2, 3, 4), (3, 4, 1, 2), (-4, -2, 0, 1)]:
            with self.subTest(ranges=ranges):
                self.assertIs(overlaps(*ranges), False)

    def test_adjacent_forward(self):
        self.assertIs(overlaps(1, 3, 3, 5), False)

    def test_adjacent_reverse(self):
        self.assertIs(overlaps(3, 5, 1, 3), False)

    def test_invalid_ranges(self):
        for ranges in [(1, 1, 2, 3), (2, 1, 2, 3), (1, 2, 3, 3),
                       (1, 2, 4, 3), (2, 1, 4, 3)]:
            with self.subTest(ranges=ranges):
                with self.assertRaises(ValueError):
                    overlaps(*ranges)

    def test_small_integer_domain_against_set_definition(self):
        # Integer half-open ranges represent unit slots; a shared slot is overlap.
        valid = [(s, e) for s in range(-2, 3) for e in range(s + 1, 4)]
        for a_start, a_end in valid:
            for b_start, b_end in valid:
                with self.subTest(a=(a_start, a_end), b=(b_start, b_end)):
                    expected = bool(set(range(a_start, a_end)) & set(range(b_start, b_end)))
                    self.assertIs(overlaps(a_start, a_end, b_start, b_end), expected)


if __name__ == '__main__':
    unittest.main()
