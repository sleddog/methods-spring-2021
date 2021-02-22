using System;

namespace Anthony
{
    class fizzbuzz
    {
        static void Main(string[] args)
        {
            Boolean exit = true;
            while(exit){
                Console.WriteLine("\nWhat is the number that you want to run?");
                String value = Console.ReadLine();
                Console.WriteLine();
                int number = Int32.Parse(value);
                for(int i=1; i<number+1; i++){
                    String numberString ="";
                    if (i%3==0){
                        numberString = numberString+"Fizz";
                    }
                    if(i%5==0){
                        numberString = numberString+"Buzz";
                    }
                    if(numberString.Length==0){
                        numberString = numberString+i.ToString();
                    }
                    Console.WriteLine(numberString);
                }
                Console.WriteLine("\nIf you want to continue, press y. If not, press n.");
                String loopCheck = Console.ReadLine().ToLower();
                if(loopCheck.Equals("n")){
                    exit = false;
                }
            }
        }
    }
}
