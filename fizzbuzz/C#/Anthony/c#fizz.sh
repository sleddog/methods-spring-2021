#!/bin/bash

# My Script for running the FizzBuzz Project

echo "Running C# Fizzbuzz Program...";

dotnet restore;
dotnet build;
dotnet run $1;
