import sys

num = int(sys.argv[1])

for n in range(1, num + 1):
    if (n % 15) == 0:
        print("FizzBuzz")
    elif (n % 3) == 0:
        print("Fizz")
    elif (n % 5) == 0:
        print("Buzz")
    else:
        print(n)

