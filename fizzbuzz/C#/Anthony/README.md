# CSCI 494: Industry Methods
# 2/22/2021
# Assignment 3 Fizzbuzz Assignment

Here is a solution to the Fizzbuzz problem written in C#, built on the .NET Framework to allow for easily compilaltion on UNIX Systems. 
Below will be all the steps necessary in order to run the program as written, with special emphasis placed on the step by setp instructions for getting
DotNet to run. 

## Introduction to the Fizzbuzz Problem
Before I dive into the solution, I wanted to give a quick explanation about what the FizzBuzz program is for those that might be unaware. 
FizzBuzz is a simple program that prompts the user for any 32-Bit Integer Number. The program then runs through the Integer, checking all numbers on the way for if they are 
divisible by either 3 or 5. If divisible by 3, then the word "Fizz" is printed in place of the number. If divisible by 5, then the word "Buzz" is printed in place of the number.
If divisible by both 3 and 5, then the word "FizzBuzz" replaces the number. Otherwise, simply the number is printed. 

## Steps to Run the Program
In order to run my solution, a user will need to install the .NET Compiler onto their development environment. 

* Go to the .NET Framework Download [page](https://dotnet.microsoft.com/download). 
* Download the .NET SDK (Note: You can use .NET Core and the Framework, but those compilers add additional details that may complicate compilation. The Developer recommends the standard .NET SDK for this project.)
* After downloading the SDK, clone repo onto local Machine. 
* Locate the C#/Anthony file directory within the larger repository. 
* CD into the C#/Anthony directory in order to open up the project. 
* Check that the fizzbuzz.cs file successfully came through the tranfer, alongside the c#fizz.sh file. 
* If Running on a Unix system, make the file an executable by running the following command 
~~~
chmod 755 c#fizz.sh
~~~
* On Windows Powershell, run the command 
~~~
sh c#fizz.sh 
~~~
or 
~~~
sh c#fizz
~~~
in order to run the shell script.
* Follow the Onscreen Prompts in order to have the program evaluate your solution.  

## What happens if the script doesn't work? 
If the shell script fails to work, but you installed dotnet successfully. Then you can run
~~~
dotnet build
dotnet run
~~~ 
within the directory in order to achieve the results! 

