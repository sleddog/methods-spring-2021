import unittest
import fizzbuzz

class FizzBuzzTestCases(unittest.TestCase):

    def test_none(self):
        result = fizzbuzz.fizzbuzz(0)
        self.assertEqual(result, "Error input must be greater than zero.")

    def test_fizz(self):
        result = fizzbuzz.fizzbuzz(3)
        self.assertEqual(result[2], "Fizz")

    def test_buzz(self):
        result = fizzbuzz.fizzbuzz(5)
        self.assertEqual(result[4], "Buzz")

    def test_ping(self):
        result = fizzbuzz.fizzbuzz(7)
        self.assertEqual(result[6], "Ping")

    def test_pong(self):
        result = fizzbuzz.fizzbuzz(11)
        self.assertEqual(result[10], "Pong")

    def test_fizz_buzz(self):
        result = fizzbuzz.fizzbuzz(15)
        self.assertEqual(result[14], "FizzBuzz")

    def test_fizz_ping(self):
        result = fizzbuzz.fizzbuzz(21)
        self.assertEqual(result[20], "FizzPing")

    def test_fizz_pong(self):
        result = fizzbuzz.fizzbuzz(33)
        self.assertEqual(result[32], "FizzPong")

    def test_buzz_ping(self):
        result = fizzbuzz.fizzbuzz(35)
        self.assertEqual(result[34], "BuzzPing")

    def test_buzz_pong(self):
        result = fizzbuzz.fizzbuzz(55)
        self.assertEqual(result[54], "BuzzPong")

    def test_ping_pong(self):
        result = fizzbuzz.fizzbuzz(77)
        self.assertEqual(result[76], "PingPong")

    def test_fizz_buzz_ping(self):
        result = fizzbuzz.fizzbuzz(105)
        self.assertEqual(result[104], "FizzBuzzPing")

    def test_fizz_buzz_pong(self):
        result = fizzbuzz.fizzbuzz(165)
        self.assertEqual(result[164], "FizzBuzzPong")

    def test_fizz_ping_pong(self):
        result = fizzbuzz.fizzbuzz(231)
        self.assertEqual(result[230], "FizzPingPong")

    def test_buzz_ping_pong(self):
        result = fizzbuzz.fizzbuzz(385)
        self.assertEqual(result[384], "BuzzPingPong")

    def test_fizz_buzz_ping_pong(self):
       result = fizzbuzz.fizzbuzz(1155)
       self.assertEqual(result[1154], "FizzBuzzPingPong")

unittest.main()
