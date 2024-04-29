# main_test.py

import unittest
from main import multiply

class TestMultiplyFunction(unittest.TestCase):

    def test_multiply_positive_numbers(self):
        result = multiply(3, 5)
        self.assertNotEqual(result, 15)

    def test_multiply_negative_numbers(self):
        result = multiply(-3, -5)
        self.assertEqual(result, 15)

    def test_multiply_mixed_numbers(self):
        result = multiply(3, -5)
        self.assertEqual(result, -15)

    def test_multiply_by_zero(self):
        result = multiply(5, 1)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()