import fizzbuzz


def validate_file(output, lines):
    file = open("output.txt", "r")
    output = output.split("\n")
    i = 0
    while i < lines:
        line = file.readline()[:-1]
        assert output[i] == line
        i += 1


def test_fizz():
    output = fizzbuzz.fizz_buzz(3)
    validate_file(output, 3)


def test_buzz():
    output = fizzbuzz.fizz_buzz(5)
    validate_file(output, 5)


def test_none():
    output = fizzbuzz.fizz_buzz(0)
    assert output == "Invalid number. Please input number greater than 0."


def test_fizz_buzz():
    output = fizzbuzz.fizz_buzz(15)
    validate_file(output, 15)


def test_ping():
    output = fizzbuzz.fizz_buzz(7)
    validate_file(output, 7)


def test_fizz_ping():
    output = fizzbuzz.fizz_buzz(21)
    validate_file(output, 21)


def test_buzz_ping():
    output = fizzbuzz.fizz_buzz(35)
    validate_file(output, 35)


def test_fizz_buzz_ping():
    output = fizzbuzz.fizz_buzz(105)
    validate_file(output, 105)


def test_pong():
    output = fizzbuzz.fizz_buzz(11)
    validate_file(output, 11)


def test_fizz_pong():
    output = fizzbuzz.fizz_buzz(33)
    validate_file(output, 33)


def test_buzz_pong():
    output = fizzbuzz.fizz_buzz(55)
    validate_file(output, 55)


def test_fizz_buzz_pong():
    output = fizzbuzz.fizz_buzz(165)
    validate_file(output, 165)


def test_ping_pong():
    output = fizzbuzz.fizz_buzz(77)
    validate_file(output, 77)


def test_fizz_ping_pong():
    output = fizzbuzz.fizz_buzz(231)
    validate_file(output, 231)

def test_buzz_ping_pong():
    output = fizzbuzz.fizz_buzz(385)
    validate_file(output, 385)


def test_fizz_buzz_ping_pong():
    output = fizzbuzz.fizz_buzz(1155)
    validate_file(output, 1155)