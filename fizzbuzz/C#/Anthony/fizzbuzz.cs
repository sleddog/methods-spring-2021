using System;

namespace Anthony
{
    class fizzBuzz
    {
        static void Main(string[] args)
        {
            int number;
            bool test = int.TryParse(args[0], out number);
            var fizz = new fizzBuzz();
            fizz.FizzBuzz(number);
        }

        public String FizzBuzz(int testNumber){
            String numberString ="";
            for(int i=1; i<testNumber+1; i++){
                numberString ="";
                if (i%3==0){
                    numberString = numberString+"Fizz";
                }
                if(i%5==0){
                    numberString = numberString+"Buzz";
                }
                if(i%7==0){
                    numberString = numberString+"Ping";
                }
                if(i%11==0){
                    numberString = numberString+"Pong";
                }
                if(numberString.Length==0){
                    numberString = numberString+i.ToString();
                }
                Console.WriteLine(numberString);
            }
            return numberString;
        }
    }
}
