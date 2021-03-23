#include <stdio.h>
#include <assert.h>
#include <string.h>
#include <stdlib.h>

char* fizztest(int n){

	char str[50] = "";

	if((n% 3 == 0) || (n%5 == 0) || (n%7 == 0) || (n%11 == 0)) {
		if(n%3 == 0){
			strcat(str, "Fizz");			
		}
		if(n%5 == 0){
			strcat(str, "Buzz");
		}
		if(n %7 == 0){
			strcat(str, "Ping");
		}
		if(n%11 == 0){
			strcat(str, "Pong");
		}
	}
	if((n% 3 != 0) && (n%5 != 0) && (n%7 != 0) && (n%11 != 0)) 
	{
		//copy n into str
		char string[50] = "";
		char buffer[10];
		sprintf(buffer, "%d", n);
		strcat(str, buffer);
	}
	char *strP = (char *) malloc(strlen (str) + 1);
	strncpy(strP, str, sizeof(str));
	return strP;
}

int main() {
	char str[50];
	strcpy(str, fizztest(3));
	
//if divisible by none
	assert(strcmp("1", fizztest(1)) == 0);
	assert(strcmp("2", fizztest(2)) == 0);
	assert(strcmp("4", fizztest(4)) == 0);
	assert(strcmp("13", fizztest(13)) == 0);

//if divisible by only 3
	assert(strcmp("Fizz", fizztest(3)) == 0);
	assert(strcmp("Fizz", fizztest(9)) == 0);
	assert(strcmp("Fizz", fizztest(12)) == 0);
	assert(strcmp("Fizz", fizztest(24)) == 0);

//if divisible by only 5
	assert(strcmp("Buzz", fizztest(5)) == 0);
	assert(strcmp("Buzz", fizztest(10)) == 0);
	assert(strcmp("Buzz", fizztest(20)) == 0);
	assert(strcmp("Buzz", fizztest(25)) == 0);

//if divisible by only 7
	assert(strcmp("Ping", fizztest(7)) == 0);
	assert(strcmp("Ping", fizztest(14)) == 0);
	assert(strcmp("Ping", fizztest(28)) == 0);

//if divisible by only 11
	assert(strcmp("Pong", fizztest(11)) == 0);
	assert(strcmp("Pong", fizztest(22)) == 0);
	assert(strcmp("Pong", fizztest(44)) == 0);
	assert(strcmp("Pong", fizztest(88)) == 0);

//if divisible by 3 and 5 
	assert(strcmp("FizzBuzz", fizztest(15)) == 0);
	assert(strcmp("FizzBuzz", fizztest(45)) == 0);
	assert(strcmp("FizzBuzz", fizztest(30)) == 0);
	assert(strcmp("FizzBuzz", fizztest(90)) == 0);

//if divisible by 3 and 7 
	assert(strcmp("FizzPing", fizztest(21)) == 0);

//if divisible by 3 and 11 
	assert(strcmp("FizzPong", fizztest(33)) == 0);

//if divisible by 3, 5 and 7 
	assert(strcmp("FizzBuzzPing", fizztest(105)) == 0);

//if divisible by 3, 5, and 11 
	assert(strcmp("FizzBuzzPong", fizztest(165)) == 0);

//if divisible by 5 and 7
	assert(strcmp("BuzzPing", fizztest(35)) == 0);

//if divisible by 5 and 11
	assert(strcmp("BuzzPong", fizztest(55)) == 0);

//if divisible by 5, 7, and 11
	assert(strcmp("BuzzPingPong", fizztest(385)) == 0);

//if divisible by 3, 7, and 11
	assert(strcmp("FizzPingPong", fizztest(231)) == 0);

//if divisible by 7 and 11
	assert(strcmp("PingPong", fizztest(77)) == 0);

//if divisible by 3, 5, 7, and 11 
	assert(strcmp("FizzBuzzPingPong", fizztest(1155)) == 0);

	printf("Tests Passed\n");
}