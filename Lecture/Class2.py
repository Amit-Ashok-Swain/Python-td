# if statement
"""
if(expression):
   print(statement1)
print(statement2)
"""
"""
a = 6
if a>=5:
    print("The number is greater than 5")
print("Thank you")

b = int(input("Enter a number: "))


if b>=5:
    print("The number is greater than 5")
print("Thank you")

"""

# if else statement

"""
if(expression):
   print(statement1)
else:
   print(statement2)
   
"""

"""
x = 55

if x>=40:
    print("Congratulations! You're Passed")
else:
    print("Sorry, you are not Passed")
print("Thank you")

y = int(input("Enter your marks: "))
if y>=40:
    print("Congratulations! You're Passed")
else:
    print("Sorry, you are not Passed")
print("Thank you")

age = int(input("Enter your age: "))

if age>=18:
    print("You are eligible")
else:
    print("You are not eligible")
print("Thank you")

"""

# elif statement

"""
if(expression1):
  print(statement1)
elif(expression2):
  print(statement2)
elif(expression3):
  print(statement3)
....
else:
  print(statement4)
  
"""

"""
operand1 = int(input("Enter first operand: "))
operand2 = int(input("Enter second operand: "))

operation = input("Enter operation(+,-,*,/): ")

if operation == "+":
    print(operand1 + operand2)
elif operation == "-":
    print(operand1 - operand2)
elif operation == "*":
    print(operand1 * operand2)
elif operation == "/":
    print(operand1 / operand2)
else:
    print("Invalid operation! Try Again")

print("Thank You!")

"""


# range function

"""
range(arg1,arg2,arg3)

where arg1 -> start of range
arg2 -> end of range but will not be included
arg -> number of steps
"""

"""
range1 = list(range(1,10))
print(range1)

range2 = list(range(0,10,2))
print(range2)

range3 = list(range(1,101,3))
print(range3)

"""


# for loop

"""

list1 = ['Chocolate', 45, 5.88]

for item in list1:
    print(item)

print()

fruit = 'banana'

for letter in fruit:
    print(letter)

print()

for i in range(0,10):
    print(i)

print()

for i in range(0,10):
    print(fruit)

print()

for i in range(0,10):
    print('A')

"""

# while loop

"""

counter_variable 

while(condition):
    print(statement1)
    increment/decrement counter_variable

print(statement2)

"""

counter_variable = 0

while(counter_variable < 10):
    print('a' * (counter_variable+1))
    counter_variable += 1

