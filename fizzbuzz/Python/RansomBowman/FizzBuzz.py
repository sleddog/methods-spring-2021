import sys
import unittest

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



if __name__ == '__main__':
    num = int(str(sys.argv[1]))



    fizzBuzz(num)
