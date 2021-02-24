package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {
	Z := os.Args[1]
	// args are initially stored as strings, so convert to int
	in, _ := strconv.Atoi(Z)
	for i := 1; i <= in; i++ {
		if i%3 == 0 {
			fmt.Printf("fizz")
		}
		if i%5 == 0 {
			fmt.Printf("buzz")
		}
		if i%3 != 0 && i%5 != 0 {
			fmt.Printf("%d", i)
		}
		fmt.Printf("\n")
	}
}
