if __name__ == "__main__":
    num = 0
    while(num != -1):
        num = int(input("Please input a number for the FizzBuzz Problem (press -1 to quit): "))
        for i in range(num):
            stringbuild = ""
            if(i % 3 == 0):
                stringbuild += "Fizz"
            if(i % 5 == 0):
                stringbuild += "Buzz"
            if(len(stringbuild) == 0):
                stringbuild += str(i)
            print(stringbuild)
    print("Goodbye!")