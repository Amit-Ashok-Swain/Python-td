# Assignment 2

"""
Task 1: Check if a Number is Even or Odd
Problem Statement:  Write a Python program that:
1. 	Takes an integer input from the user.
2. 	Checks whether the number is even or odd using an if-else statement.
3. 	Displays the result accordingly.
"""

number = int(input('Enter a number: '))

if number % 2 == 0:
    print(number,'is an even number.')
else:
    print(number,'is an odd number.')

"""
Output:
/Users/amitashokswain/PycharmProjects/Python/.venv/bin/python /Users/amitashokswain/PycharmProjects/Python/Assignment/Assignment2.py 
Enter a number: 4
4 is an even number.

Process finished with exit code 0

"""

print()

"""
Task 2: Sum of Integers from 1 to 50 Using a Loop
 
Problem Statement: Write a Python program that:
1.   Uses a for loop to iterate over numbers from 1 to 50.
2.   Calculates the sum of all integers in this range.
3.   Displays the final sum.

"""
sum = 0

for i in range(1,50):
    sum+=i
print("The sum of numbers from 1 to 50 is:",sum)

print()
print()

"""
Output:
/Users/amitashokswain/PycharmProjects/Python/.venv/bin/python /Users/amitashokswain/PycharmProjects/Python/Assignment/Assignment2.py 

The sum of numbers from 1 to 50 is: 1225

Process finished with exit code 0

"""
