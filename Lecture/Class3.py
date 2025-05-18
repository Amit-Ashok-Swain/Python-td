# Functions

"""
Syntax:

def "Function Name" ():
    Statement/block of code

"Function Name" () -> Function call

"""
import math

"""

def sports():
    print('Cricket')
    print('Football')

sports()

sports()

print()

def greeting():

    str1 = 'Hello'
    str2 = 'World'
    print(str1 + " " + str2)

greeting()

"""

# Return Statement

"""
Syntax:
def "function name" ():
    Statement/block of code
    return expression
    
function call assigned to a variable 
"""
"""
def add(a, b):
    print(a + b)

add(1, 2)

print()

def add1(a, b):
    sum = a + b
    return sum

ans = add1(10, 20) # function call only possible if assigned to a variable
print(ans)

print()

def multiply_string(a, b):
    return a * b

str1 = multiply_string('Amit ', 7)
print(str1)

print()

"""

# Passing Arguments to a function

"""
def addition(a):
    print(a + 2)

addition(10)

print()

def addition1(x,y,z):
    print (x + y + z)

addition1(10, 20, 30)

print()
"""

# Passing Function as argument

"""
2 numbers, if you add them should be equal to 7. 
Square of the number and 1 function call to be used
"""

"""
def addition2(x,y):
    return x + y

def multiplication(x):
    return pow(x,2)

result = multiplication(addition2(3,4))
print(result)

print()

"""

# Modules

"""
import math    # Method 1 
print(math.pi)

"""

"""
from math import pi    # Method 2 
print(pi)

"""

"""
from math import *   # Method 3
print(pi)

"""

# Recursion

"""
Syntax: 
def "function name" ():
    Statement/block of code
    function call in the function itself -> "function name"()

function call
"""

"""
import sys

print(sys.getrecursionlimit()) # prints limit of recursion iterations.

print()

sys.setrecursionlimit(3000) # set limit of recursion iterations.

print(sys.getrecursionlimit())


print()

counter = 0

def python():
    global counter # declares it as global variable
    counter += 1
    print('python', counter)
    python()

python()

"""

# Factorial

"""
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

result = factorial(5)
print(result)
"""

# Global and Local variable

n = 1 # Global Variable

def fn():
    n = 5 # Local Variable
    print("in",n)

fn()

print("out",n)


print()


n1 = 1 # Global Variable

def fn1():
    global n1 # declared as global variable
    n1 = 5
    print("in",n1)

fn1()

print("out",n1)
