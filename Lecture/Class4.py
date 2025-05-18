# 1. Syntax Error

"""
a = 1

if a>=1:
    print("Hello")
else
    print("World")

"""
import math

"""
Output:
/Users/amitashokswain/PycharmProjects/Python/.venv/bin/python /Users/amitashokswain/PycharmProjects/Python/Lecture/Class4.py 
  File "/Users/amitashokswain/PycharmProjects/Python/Lecture/Class4.py", line 7
    else
        ^
SyntaxError: expected ':'

Process finished with exit code 1

"""

# 2. Indentation error

"""
if a>=1:
    print("Hello")
else:
print("World")

"""

"""
Output:
/Users/amitashokswain/PycharmProjects/Python/.venv/bin/python /Users/amitashokswain/PycharmProjects/Python/Lecture/Class4.py 
  File "/Users/amitashokswain/PycharmProjects/Python/Lecture/Class4.py", line 32
    print("World")
    ^^^^^
IndentationError: expected an indented block after 'else' statement on line 31

Process finished with exit code 1
"""

# 3. Zero Division Error
"""
print(8/0)
"""

"""
Output:
/Users/amitashokswain/PycharmProjects/Python/.venv/bin/python /Users/amitashokswain/PycharmProjects/Python/Lecture/Class4.py 
Traceback (most recent call last):
  File "/Users/amitashokswain/PycharmProjects/Python/Lecture/Class4.py", line 50, in <module>
    print(8/0)
          ~^~
ZeroDivisionError: division by zero

Process finished with exit code 1

"""

# 4. Module Not Found Error

"""
import mathematics
print(mathematics.pi)
"""

"""
Output:
/Users/amitashokswain/PycharmProjects/Python/.venv/bin/python /Users/amitashokswain/PycharmProjects/Python/Lecture/Class4.py 
Traceback (most recent call last):
  File "/Users/amitashokswain/PycharmProjects/Python/Lecture/Class4.py", line 67, in <module>
    import mathematics
ModuleNotFoundError: No module named 'mathematics'

Process finished with exit code 1
"""

# 5. Type Error

"""
a = 5
b = '6'

print(a + b)

"""

"""
Output:
/Users/amitashokswain/PycharmProjects/Python/.venv/bin/python /Users/amitashokswain/PycharmProjects/Python/Lecture/Class4.py 
Traceback (most recent call last):
  File "/Users/amitashokswain/PycharmProjects/Python/Lecture/Class4.py", line 88, in <module>
    print(a + b)
          ~~^~~
TypeError: unsupported operand type(s) for +: 'int' and 'str'

"""

# 6. Logic Error

# This error depends on the error in the logic within the lines of code



# ZeroDivisionError Exception

"""
try:
    a = 5
    b = 0
    print(a/b)
except ZeroDivisionError:
    print("Division by zero")
finally:
    print("Continue with the code")
    
"""

# File Handling (opening and closing)

"""
# Method 1 Syntax:

file1 = open("my_file.txt", "r")
# parameter 1: specify the file location
# Parameter 2: specify whether "read", "write", "append"
file1.close()



# Method 2 Syntax:

with open("my_file.txt", "w") as file2:
    file2.write("Hello")
    
"""

# Reading the data from file

#Method 1:

# file1 = open("my_file.txt", "r")
# reading_file1 = file1.read()
#reading_file2 = file1.read(3)
#reading_file3 = file1.readline()
#reading_file4 = file1.readlines()
#print(reading_file1)
#print(reading_file2)
#print(reading_file3)
#print(reading_file4)

# file1.close()


# Method 2:
"""
with open("my_file.txt", "r") as file2:
   reading_file5 = file2.read()
   print(reading_file5)
"""

# Adding the data to a file


"""
file3 = open("my_file.txt", "w")
writing_file = file3.write("Hello")
print(writing_file) # prints number of characters in the write
file3.close()

print()

file4 = open("my_file.txt", "r")
reading_file5 = file4.read()
print(reading_file5)
file4.close()

"""

# Appending data to the file

"""
file = open("my_file.txt", "w")
writing_file = file.write("Hello! Everyone")
print(writing_file)
file.close()


file = open("my_file.txt", "a")
writing_file = file.write("\nMy Name is Amit Swain.")
print(writing_file)
file.close()

file = open("my_file.txt", "r")
reading_file = file.read()
print(reading_file)
file.close()

"""

# Reading and adding the data
# r+ -> read and write

file = open("my_file.txt", "r+")
writing_file = file.write("Hello! Everyone")
print(writing_file)
file.close()

"""
file = open("my_file.txt", "a")
appending_file = file.write("\nMy Name is Amit Swain.")
print(appending_file)
file.close()
"""

file = open("my_file.txt", "r+")
reading_file = file.read()
print(reading_file)
file.close()























