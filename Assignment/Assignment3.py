# Assignment 3

"""
Task 1: Calculate Factorial Using a Function


Problem Statement: Write a Python program that:
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.

"""
import math


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

number = int(input("Enter a number: "))
answer = factorial(number);
print("The factorial of", number, "is:",answer)

print()
print()

"""
Output:
/Users/amitashokswain/PycharmProjects/Python/.venv/bin/python /Users/amitashokswain/PycharmProjects/Python/Assignment/Assignment3.py 
Enter a number: 5
The factorial of 5 is: 120

Process finished with exit code 0
"""

"""
Task 2: Using the Math Module for Calculations
 
Problem Statement: Write a Python program that:
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
    o   Square root of the number
    o   Natural logarithm (log base e) of the number
    o   Sine of the number (in radians)
3.   Displays the calculated results.

"""

from math import *

def square_root(n):
    return sqrt(n)

def natural_log(n):
    return log(n, e)

def sine(n):
    return sin(n)

number = int(input("Enter a number: "))
answer1 = square_root(number)
answer2 = natural_log(number)
answer3 = sine(number)

print("Square root:",answer1)
print("Logarithm:",answer2)
print("Sine:",answer3)

print()
print()


"""
Output:
/Users/amitashokswain/PycharmProjects/Python/.venv/bin/python /Users/amitashokswain/PycharmProjects/Python/Assignment/Assignment3.py 
Enter a number: 25
Square root: 5.0
Logarithm: 3.2188758248682006
Sine: -0.13235175009777303

"""





