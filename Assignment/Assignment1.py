# Assignment 1

"""
Task 1: Perform Basic Mathematical Operations
Problem Statement: Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
   o	Addition
   o	Subtraction
   o	Multiplication
   o	Division
3.  Displays the results of each operation on the screen.
"""

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

add = a + b
sub = a - b
mul = a * b
div = a / b

print()

print("Addition:",add)
print("Subtraction:",sub)
print("Multiplication:",mul)
print("Division:",div)

"""
Output:
/Users/amitashokswain/PycharmProjects/Python/.venv/bin/python /Users/amitashokswain/PycharmProjects/Python/Assignment/Assignment1.py 
Enter the first number: 5
Enter the second number: 10

Addition: 15
Subtraction: -5
Multiplication: 50
Division: 0.5
"""
print()
print()
"""
Task 2: Create a Personalized Greeting
Problem Statement: Write a Python program that:
1.  Takes a user's first name and last name as input.
2.  Concatenates the first name and last name into a full name.
3.  Prints a personalized greeting message using the full name.
"""

fname = str(input("Enter your first name: "))
lname = str(input("Enter your last name: "))

print()

lname = lname +"!"

print("Hello,",fname,lname,"Welcome to the Python program.")

print()
print()

"""
Output:
Enter your first name: Amit
Enter your last name: Swain
Hello, Amit Swain! Welcome to the Python program.

Process finished with exit code 0
"""


