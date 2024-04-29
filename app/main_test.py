# main_test.py

import unittest
from main import subtract

class TestSubtractFunction(unittest.TestCase):

    def test_subtract_positive_numbers(self):
        result = subtract(5, 3)
        self.assertEqual(result, 2)

    def test_subtract_negative_numbers(self):
        result = subtract(-3, -5)
        self.assertEqual(result, 2)

    def test_subtract_mixed_numbers(self):
        result = subtract(3, -5)
        self.assertEqual(result, 10)

    def test_subtract_zero(self):
        result = subtract(5, 0)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()