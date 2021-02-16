#The FizzBuzz Problem, as Coded by Arnold Smithson

Welcome to Arnold's implementation of the FizzBuzz problem, coded in Python!
This code is meant to print "Fizz" if the inputted number is divisible
by 3, "Buzz" if the number is divisible by 5, and FizzBuzz
if the number is divisible by both. Otherwise, the number prints. If you don't have python installed, here is a quick
step-by-step to install Python and run this program.

##Installing Python

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
