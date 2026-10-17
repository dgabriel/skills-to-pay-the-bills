import unittest
from booking import overlaps

class OverlapTests(unittest.TestCase):
    def test_partial_overlap(self):
        self.assertTrue(overlaps(1, 4, 3, 6))
    def test_containment(self):
        self.assertTrue(overlaps(-3, 8, 0, 2))
    def test_identical(self):
        self.assertTrue(overlaps(1, 3, 1, 3))
    def test_separated(self):
        self.assertFalse(overlaps(1, 3, 4, 6))
    def test_adjacent_forward(self):
        self.assertFalse(overlaps(1, 3, 3, 6))
    def test_adjacent_reverse(self):
        self.assertFalse(overlaps(3, 6, 1, 3))
    def test_one_unit_overlap(self):
        self.assertTrue(overlaps(1, 4, 3, 6))
    def test_negative_adjacent(self):
        self.assertFalse(overlaps(-5, -2, -2, 0))
    def test_empty_first(self):
        with self.assertRaises(ValueError): overlaps(2, 2, 3, 5)
    def test_reversed_first(self):
        with self.assertRaises(ValueError): overlaps(4, 2, 3, 5)
    def test_empty_second(self):
        with self.assertRaises(ValueError): overlaps(1, 2, 3, 3)
    def test_reversed_second(self):
        with self.assertRaises(ValueError): overlaps(1, 2, 5, 3)

if __name__ == '__main__':
    unittest.main()
