import unittest
from FizzBuzz import fizzBuzz

class TestFizzBuzz(unittest.TestCase):
        
    def test_3(self):
        self.assertEqual(fizzBuzz(3), 'Fizz')

    def test_5(self):
        self.assertEqual(fizzBuzz(5), 'Buzz')
        
    def test_7(self):
        self.assertEqual(fizzBuzz(7), 'Ping')

    def test_11(self):
        self.assertEqual(fizzBuzz(11), 'Pong')

    def test_All(self):
        self.assertEqual(fizzBuzz(1155), 'FizzBuzzPingPong')

if __name__ == '__main__':
    unittest.main()
