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

int fizzprint(int k) {
	char str[50];
	strcpy(str, fizztest(3));
	int n = k;
	for (int i =1; i < (n+1); i++){
		if((n% 3 != 0) && (n%5 != 0) && (n%7 != 0) && (n%11 != 0)) {
			printf("%d", i);
		}
		printf("\n");
		printf("%s", fizztest(i));
	}
	printf("\n");
}
