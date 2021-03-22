using System;

namespace Anthony
{
    class fizzbuzz
    {
        static void Main(string[] args)
        {
            int number;
            bool test = int.TryParse(args[0], out number);
            for(int i=1; i<number+1; i++){
                String numberString ="";
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
        }
    }
}
