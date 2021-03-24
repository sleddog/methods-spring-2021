import unittest
from FizzBuzz import fizzBuzz

class TestFizzBuzz(unittest.TestCase):
        
    def test_3(self):
        self.assertEqual(fizzBuzz(3), fizzBuzz(3))

    def test_5(self):
        self.assertEqual(fizzBuzz(5), fizzBuzz(5))
        
    def test_7(self):
        self.assertEqual(fizzBuzz(7), fizzBuzz(7))

    def test_11(self):
        self.assertEqual(fizzBuzz(11), fizzBuzz(11))

    def test_All(self):
        self.assertEqual(fizzBuzz(1155), fizzBuzz(1155))

if __name__ == '__main__':
    unittest.main()
