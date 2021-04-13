Question 1:

void main() {
  double total = 0;
  for (double i = 0; i < 1000; i++) {
    if((i % 3) == 0){

      total += i;
      
    }else if((i % 5) == 0){
      
      total += i;
      
    }
  }
  print("Sum of numbers: ${total}");
}