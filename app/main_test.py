# main_test.py

import unittest
from main import add

class TestAddFunction(unittest.TestCase):

    def test_add_positive_numbers(self):
        result = add(3, 5)
        self.assertEqual(result, 8)

    def test_add_negative_numbers(self):
        result = add(-3, -5)
        self.assertEqual(result, -8)

    def test_add_mixed_numbers(self):
        result = add(3, -5)
        self.assertEqual(result, -2)

    def test_add_zero(self):
        result = add(0, 5)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
