import sys

if __name__ == "__main__":
    num = int(sys.argv[1])
    for i in range(1, num+1):
        stringbuild = ""
        if(i % 3 == 0):
            stringbuild += "Fizz"
        if(i % 5 == 0):
            stringbuild += "Buzz"
        if(len(stringbuild) == 0):
            stringbuild += str(i)
        print(stringbuild)
