# Assignment 5

"""
Task 1: Create a Dictionary of Student Marks

Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.

"""

dict_student = {"Alice":85, "Amit": 98, "Suresh": 99, "Akash": 97, "Ramesh" : 88}

input_name = input("Enter the student's name: ")

if input_name in dict_student:
    print(f"{input_name}'s marks: {dict_student[input_name]}")
else:
    print("Student not found.")

print()
print()

"""
Output:

# If the student exist in the dictionary:


/Users/amitashokswain/PycharmProjects/Python/.venv/bin/python /Users/amitashokswain/PycharmProjects/Python/Assignment/Assignment5.py 
Enter the student's name: Alice
Alice's marks: 85

Process finished with exit code 0

# If the student does not exist in the dictionary:


/Users/amitashokswain/PycharmProjects/Python/.venv/bin/python /Users/amitashokswain/PycharmProjects/Python/Assignment/Assignment5.py 
Enter the student's name: John
Student not found.

Process finished with exit code 0


"""

"""
Task 2: Demonstrate List Slicing 
Problem Statement: Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list
"""

l = [i for i in range(1,11)]
print(f"Original list: {l}")
first_five = l[:5]
print(f"Extracted first five elements: {first_five}")
first_five.reverse()
print(f"Reversed extracted elements: {first_five}")

print()
print()

"""
Output:
/Users/amitashokswain/PycharmProjects/Python/.venv/bin/python /Users/amitashokswain/PycharmProjects/Python/Assignment/Assignment5.py 
Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Extracted first five elements: [1, 2, 3, 4, 5]
Reversed extracted elements: [5, 4, 3, 2, 1]
"""



