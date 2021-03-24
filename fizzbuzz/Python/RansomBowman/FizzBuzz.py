import sys
import unittest

def fizzBuzz(num):
    #num = int(input("Enter the number to FizzBuzz: "))
    ret_str = ""
    if not(num%3 == 0) and not(num%5 == 0) and not (num%7 == 0) and not (num%11 == 0):
        return num
    else:
        if (num%3 == 0):
            ret_str += "Fizz"
        if (num%5 == 0):
            ret_str += "Buzz"
        if (num%7 == 0):
            ret_str += "Ping"
        if (num%11 == 0):
            ret_str += "Pong"
        return ret_str



if __name__ == '__main__':
    num = int(str(sys.argv[1]))
    
    for i in range(1, num + 1):
        print(fizzBuzz(i), end = '')
        print()

