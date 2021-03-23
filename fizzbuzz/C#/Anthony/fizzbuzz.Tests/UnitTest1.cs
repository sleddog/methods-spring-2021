using System;
using Xunit;
using Anthony;

namespace fizzbuzz.Tests
{
    public class UnitTest1
    {
        [Fact]
        public void Test1()
        {
            var newFizz = new fizzBuzz();
            Assert.Equal("Buzz", newFizz.FizzBuzz(5));

        }
        
        [Fact]
        public void Testfor3(){
            var newFizz = new fizzBuzz();
            Assert.Equal("Fizz", newFizz.FizzBuzz(3));
        }
        
        [Fact]
        public void Testfor7(){
            var newFizz = new fizzBuzz();
            Assert.Equal("Ping", newFizz.FizzBuzz(7));
        }
        
        [Fact]
        public void Testfor11(){
            var newFizz = new fizzBuzz();
            Assert.Equal("Pong", newFizz.FizzBuzz(11));
        }

        [Fact]
        public void Testfor15(){
            var newFizz = new fizzBuzz();
            Assert.Equal("FizzBuzz", newFizz.FizzBuzz(15));
        }

        
    }
}
