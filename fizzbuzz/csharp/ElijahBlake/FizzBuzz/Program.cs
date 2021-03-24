using System;

namespace FizzBuzz
{
    public class Program
    { 

        static void Main(string[] args)
        {
            Program program = new Program();
            string output = program.RunFizzBuzz(Convert.ToInt32(args[0]));
            Console.WriteLine(output);
        }

        public string RunSingleLine(int n)
        {
            string output = "";
            if (n % 1155 == 0)
            {
                output += "FizzBuzzPingPong\n";
            }
            else if (n % 385 == 0)
            {
                output += "BuzzPingPong\n";
            }
            else if (n % 231 == 0)
            {
                output += "FizzPingPong\n";
            }
            else if (n % 77 == 0)
            {
                output += "PingPong\n";
            }
            else if (n % 55 == 0)
            {
                output += "BuzzPong\n";
            }
            else if (n % 35 == 0)
            {
                output += "BuzzPingPong\n";
            }
            else if (n % 33 == 0)
            {
                output += "BuzzPing\n";
            }
            else if (n % 15 == 0)
            {
                output += "FizzBuzz\n";
            }
            else if (n % 11 == 0)
            {
                output += "Pong\n";
            }
            else if (n % 7 == 0)
            {
                output += "Ping\n";
            }
            else if (n % 5 == 0)
            {
                output += "Buzz\n";
            }
            else if (n % 3 == 0)
            {
                output += "Fizz\n";
            }
            else
            {
                output += n + "\n";
            }
            return output;
        }

        public string RunFizzBuzz(int n)
        {
            string output = "";
            for (int j = 1; j < n + 1; j++)
            {
                string outputAddOn = RunSingleLine(j);
                output += outputAddOn;
            }
            return output;
        }
    }

}
