import sys

def fizzbuzz(num):
    result = []

    if (num < 1):
        return "Error input must be greater than zero."

    for n in range(1, num + 1):
        temp = ""
        if (n % 3) == 0:
            temp += "Fizz"
        if (n % 5) == 0:
            temp += "Buzz"
        if (n % 7) == 0:
            temp += "Ping"
        if (n % 11) == 0:
            temp += "Pong"
        if temp == "":
            temp += str(n)
        result.append(temp)
    return result

if __name__ == "__main__":
    num = int(sys.argv[1])
    if (num > 0):
        for n in fizzbuzz(num):
            print(n)
    else:
        print("Error input must be greater than zero.")
