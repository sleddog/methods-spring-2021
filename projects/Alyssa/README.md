# Riječi Solution in Kotlin
## Introduction
This is a solution to the [Riječi](https://open.kattis.com/problems/rijeci)  problem on Kattis using Kotlin. 
I chose to use Kotlin to solve this problem because I am unfamiliar with the language and thought that solving the problem in Kotlin would be a fun way to familiarize myself with Kotlin's syntax.

### The Problem
One day, little Mirko came across a funny looking machine! When he found the machine, the screen displayed only the letter A. After he pressed the button, the letter changed to B. The next few times he pressed the button, the word transformed from B to BA, then to BAB, then to BABBA... When he saw this, Mirko realized that the machine alters the word in a way that all the letters B get transformed to BA and all the letters A get transformed to B.

After 𝐾 times of pressing the button, how many letters A and how much letters B will be displayed on the screen?

### The Solution
Since the machine initially displays one A and zero B's we can initialize variables that represent these two totals. When the button is pressed, A's are transformed to B's and B's are transformed to BA's. This can be respresented by a simple function. Upon each press of the button, the count of A's becomes the count of B's and the count of B's becomes the count of the current B's and A's.

#### Sample Input/Output
Input represents the number of button presses 𝐾 (1 ≤ 𝐾 ≤ 45). Output represents the number of A's followed by the number of B's.
```
input: 1      output: 0 1
input: 4      output: 2 3
input: 10     output: 34 55
```
