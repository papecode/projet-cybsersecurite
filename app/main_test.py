from main import return_backwards_string, get_mode
import unittest
import os


class TestMain(unittest.TestCase):
    def test_return_backwards_string(self):
        random_string = "Hello"
        random_string_reversed = "olleH"
        self.assertNotEqual(random_string_reversed,
                        return_backwards_string(random_string))

    def test_get_mode(self):
        self.assertEqual(os.environ.get("MODE"), get_mode())


if __name__ == "__main__":
    unittest.main()