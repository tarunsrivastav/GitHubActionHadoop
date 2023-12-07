# test_example.py
#Add 1 more comment
import unittest
from example import add_numbers

class TestExample(unittest.TestCase):

    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, 1), 0)

if __name__ == '__main__':
    unittest.main()
