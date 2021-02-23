#!/bin/bash

javac FizzBuzz.java

read -p "Enter number: " number

java FizzBuzz $number
