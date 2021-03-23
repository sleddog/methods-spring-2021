import sys
import unittest

class TestFizzBuzz(unittest.TestCase):
        
    def test_3(self):
        fizzBuzz(3)

    def test_5(self):
        fizzBuzz(5)
        
    def test_7(self):
        fizzBuzz(7)

    def test_11(self):
        fizzBuzz(11)

    def test_All(self):
        fizzBuzz(1155)


def fizzBuzz(num):
    #num = int(input("Enter the number to FizzBuzz: "))

    for i in range(1, num + 1):
        if not(i%3 == 0) and not(i%5 == 0) and not (i%7 == 0) and not (i%11 == 0):
            print(i)
        else:
            if (i%3 == 0):
                print("Fizz", end = '')
            if (i%5 == 0):
                print("Buzz", end = '')
            if (i%7 == 0):
                print("Ping", end = '')
            if (i%11 == 0):
                print("Pong", end = '')
            print()    

num = int(str(sys.argv[1]))

fizzBuzz(num)
