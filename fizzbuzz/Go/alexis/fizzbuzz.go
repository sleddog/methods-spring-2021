package main

import (
	"fmt"
	"os"
	"strconv"
)

func fizzbuzz(n int) string {
	finalString := ""
	for i := 1; i <= n; i++ {
		finalString = ""
		if i%3 == 0 {
			finalString += "fizz"
		}
		if i%5 == 0 {
			finalString += "buzz"
		}
		if i%7 == 0 {
			finalString += "ping"
		}
		if i%11 == 0 {
			finalString += "pong"
		}
	}
	fmt.Printf(finalString + "\n")
	return finalString
}

func main() {
	Z := os.Args[1]
	// args are initially stored as strings, so convert to int
	in, _ := strconv.Atoi(Z)
	fizzbuzz(in)
}
