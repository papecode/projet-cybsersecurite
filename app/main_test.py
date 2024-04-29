import unittest
from main import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_return_backwards_string(self):
        response = self.app.get('/Hello')
        self.assertEqual(response.data.decode('utf-8'), 'olleH')

    def test_get_mode(self):
        response = self.app.get('/get-mode')
        self.assertEqual(response.data.decode('utf-8'), 'dev')

if __name__ == '__main__':
    unittest.main()
