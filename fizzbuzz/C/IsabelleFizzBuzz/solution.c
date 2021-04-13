#include <stdio.h>
int main() {
   

   int n;
  scanf("%d", &n);


for(int i = 1; i < (n+1); i++){
if (i%15 == 0){
printf("FizzBuzz\n");
}
	else  if (i%3 == 0){
   	printf("Fizz");
    if(i%7 == 0){
      printf("Ping");
    }
    if(i%11 == 0){
      printf("Pong");
    }
   }
   	else if(i%5 == 0){
   		printf("Buzz\n");
   	}
    else if(i%7 == 0){
      printf("Ping\n");
    }
     else if(i%11 == 0){
      printf("Pong\n");
    }
else{
	printf("%d\n", i);
}
}
   return 0;
}  
