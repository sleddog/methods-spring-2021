# The FizzBuzz Problem, as Coded by Arnold Smithson

Welcome to Arnold's implementation of the FizzBuzz problem, coded in Python!
This code is meant to print "Fizz" if the inputted number is divisible
by 3, "Buzz" if the number is divisible by 5, and FizzBuzz
if the number is divisible by both. Otherwise, the number prints. If you don't have python installed, here is a quick
step-by-step to install Python and run this program.

## Installing Python

1. Go to [the python website.](https://www.python.org)

2. Hover over Downloads, and click the quick button at the right, which is labeled at the most current Python release
   (as of this writing, that's 3.9.x).
   
3. Open the python.exe installer in your File Explorer/Finder.

4. Before clicking next or anything, make sure to click the box in the lower right (if it shows up) to
"add python to PATH."
   
5. Run through the installer, setting the options to what you'd like.

6. Download the `fizzbuzz.py` file and the `run.sh` shell file from this directory.

7. In cmd.exe in Windows or Terminal in Mac, navigate to the directory in which `fizzbuzz.py` downloaded.

8. Run `./run.sh` in your terminal, adding whatever number you'd like after it before executing.

   8a. If `./run.sh` doesn't initally work in your command line, run `chmod 755 run.sh` to make it executable. 
## The Program

The program itself is less than 15 lines and requires user input. By running the program,
you may input whichever number you like and watch the lines print, one by one. The input parameter is grabbed from
the command line, rather than reading the keyboard for user input while the
program is running.

## Potential Changes

If I had to change anything about my solution, I could take user input during the program instead
of a program argument upon execution. Otherwise, I'm not sure what else I could do to "imrpove" it. There's always more than one solution,
and I'm sure this is one of millions at this point!

## Running The Unit Tests

These tests can be run via pytest. If you don't have that installed, follow the instructions at [this link.](https://docs.pytest.org/en/stable/getting-started.html)

### How They Work

I covered all 16 test cases, found by using the power set of the numbers 3, 5, 7, and 11. I'm sure this amount of tests wasn't necessary since running 1155 would cover everything, but it's always good to have coverage. Each unit test runs the `fizz_buzz` function and compares its results to an output file using the `validate_file` helper function. `output.txt` contains the answer when 1155 is put into the function, so it included the numbers from all previous test cases. 

### The Commands

1. Change directories to `fizzbuzz/python/Arnold`.

2. run `pytest fizzbuzz_test.py`.
