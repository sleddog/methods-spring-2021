import sys


def fizz_buzz(number):
    return_string = ""
    if number < 1:
        return "Invalid number. Please input number greater than 0."

    for i in range(1, number + 1):
        string_build = ""
        if i % 3 == 0:
            string_build += "Fizz"
        if i % 5 == 0:
            string_build += "Buzz"
        if i % 7 == 0:
            string_build += "Ping"
        if i % 11 == 0:
            string_build += "Pong"
        if len(string_build) == 0:
            string_build += str(i)
        return_string += string_build + "\n"
    return return_string


if __name__ == "__main__":
    num = int(sys.argv[1])
    print(fizz_buzz(num))

# Test cases: 0, 3, 5, 15, 7, 21, 35, 105, 11, 33, 55, 165, 77, 231, 385, 1155
