Welcome to my Fortran FizzBuzz program!
Make sure you have gfortran installed on your system before beginning
To run, using the shell script 'run' as follows:
./run.sh 17
The first argument is read and used for the FizzBuzz program(the example above will go up to 17).
Enjoy!

Setting up Fortran testing environment:
1.) Run:
     sudo gem install funit
    followed by:
     export FC="gfortran"
 
2.) Run:
     funit fizzbuzz
    run any commands funit requests if necessary