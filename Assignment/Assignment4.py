# Assignment 4

"""
Task 1: Read a File and Handle Errors
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.

"""

try:
    file1 = open('sample.txt', 'r')
    file_content_line1 = file1.readlines()
    print("Reading file content:")

    line_count = 1;
    for line in file_content_line1:
        print("Line", line_count, ":", line.strip())
        line_count += 1
    file1.close()
except FileNotFoundError as e:
    print("Error: The file",e.filename,"was not found.")

print()
print()
"""
Output:

# If the file exists:

/Users/amitashokswain/PycharmProjects/Python/.venv/bin/python /Users/amitashokswain/PycharmProjects/Python/Assignment/Assignment4.py 
Reading file content:
Line 1 : This is a sample text file.
Line 2 : It contains multiple lines.

Process finished with exit code 0

If the file does not exist:

/Users/amitashokswain/PycharmProjects/Python/.venv/bin/python /Users/amitashokswain/PycharmProjects/Python/Assignment/Assignment4.py 
Error: The file 'sample.txt' was not found.

Process finished with exit code 0

"""

"""
Task 2: Write and Append Data to a File
 
Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.

"""

input_data1 = input('Enter text to write to the file: ')
file2 = open('output.txt', 'w')
file2.write(input_data1)
print("Data successfully written to output.txt.")
file2.close()

print()

input_data2 = input('Enter additional text to append: ')
file2 = open('output.txt', 'a')
file2.write('\n' + input_data2)
print("Data successfully appended.")
file2.close()

print()

print("Final content of output.txt:")

file2 = open('output.txt', 'r')
read_data = file2.readlines()
for line in read_data:
    print(line.strip())
file2.close()

print()
print()

"""
Output:
/Users/amitashokswain/PycharmProjects/Python/.venv/bin/python /Users/amitashokswain/PycharmProjects/Python/Assignment/Assignment4.py 
Enter text to write to the file: Hello, Python!
Data successfully written to output.txt.

Enter additional text to append: Learning file handling in Python.
Data successfully appended.

Final content of output.txt:
Hello, Python!
Learning file handling in Python.

Process finished with exit code 0
"""






