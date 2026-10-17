import unittest
from booking import overlaps


class BookingOverlapTests(unittest.TestCase):
    def test_valid_ranges(self):
        cases = [
            ('partial', (1, 5, 3, 7), True),
            ('contained', (1, 8, 3, 5), True),
            ('identical', (1, 5, 1, 5), True),
            ('same_start', (1, 3, 1, 6), True),
            ('same_end', (1, 6, 3, 6), True),
            ('disjoint', (1, 3, 5, 7), False),
            ('adjacent', (1, 3, 3, 7), False),
            ('negative', (-8, -2, -4, 1), True),
            ('negative_adjacent', (-8, -2, -2, 1), False),
            ('unit_overlap', (0, 1, 0, 1), True),
            ('unit_adjacent', (0, 1, 1, 2), False),
            ('large', (10**30, 10**30 + 5, 10**30 + 2, 10**30 + 8), True),
        ]
        for name, args, expected in cases:
            for ordered in (args, args[2:] + args[:2]):
                with self.subTest(case=name, args=ordered):
                    self.assertEqual(overlaps(*ordered), expected)

    def test_invalid_ranges(self):
        for args in [(1, 1, 2, 3), (2, 1, 2, 3),
                     (1, 2, 3, 3), (1, 2, 4, 3),
                     (1, 1, 3, 3), (2, 1, 4, 3)]:
            with self.subTest(args=args):
                with self.assertRaises(ValueError):
                    overlaps(*args)


if __name__ == '__main__':
    unittest.main()
