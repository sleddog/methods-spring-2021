using Xunit;
using FizzBuzz;
using Microsoft.VisualStudio.TestPlatform.TestHost;
using System;

namespace FizzBuzzTests
{
    public class FizzBuzzInputs
    {
        [Fact]
        public void TestFizz()
        {
            FizzBuzz.Program program = new FizzBuzz.Program();
            string output = program.RunSingleLine(Convert.ToInt32(3));
            Assert.Equal("Fizz\n", output);
        }

        [Fact]
        public void TestBuzz()
        {
            FizzBuzz.Program program = new FizzBuzz.Program();
            string output = program.RunSingleLine(Convert.ToInt32(5));
            Assert.Equal("Buzz\n", output);
        }

        [Fact]
        public void TestPing()
        {
            FizzBuzz.Program program = new FizzBuzz.Program();
            string output = program.RunSingleLine(Convert.ToInt32(7));
            Assert.Equal("Ping\n", output);
        }

        [Fact]
        public void TestPong()
        {
            FizzBuzz.Program program = new FizzBuzz.Program();
            string output = program.RunSingleLine(Convert.ToInt32(11));
            Assert.Equal("Pong\n", output);
        }
    }
}