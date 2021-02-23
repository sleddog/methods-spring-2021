#!/bin/bash

# My Script for running the FizzBuzz Project

echo "Running C# Fizzbuzz Program...";

dotnet build fizzbuzz.cs;
dotnet run $1;