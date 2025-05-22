import unittest
from main import get_hello_world

class TestMain(unittest.TestCase):
    def test_get_hello_world(self):
        self.assertEqual(get_hello_world(), "Hello, World!")

if __name__ == '__main__':
    unittest.main()
