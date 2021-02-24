#!/bin/bash

# My Script for running the FizzBuzz Project

echo "Running C# Fizzbuzz Program...";

dotnet msbuild --restore fizzbuzz.cs;
dotnet run $1;