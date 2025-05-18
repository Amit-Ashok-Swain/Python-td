# Python Programming Assignments

This repository contains five foundational Python programming assignments designed to build a solid understanding of basic programming concepts. Each assignment includes two tasks covering a variety of topics such as user input, control flow, loops, functions, file handling, and data structures.

## 📁 Repository Structure

```
Assignment1.py
Assignment2.py
Assignment3.py
Assignment4.py
Assignment5.py
README.md
```

---

## 🧮 Assignment 1: Basic Operations and Greetings

### ✅ Task 1: Basic Mathematical Operations

* **Objective:** Perform addition, subtraction, multiplication, and division.
* **Steps:**

  1. Accept two integer inputs from the user.
  2. Perform all four arithmetic operations.
  3. Display the results.
* **Approach & Code Explanation:**

  * The code uses `input()` to accept two numbers from the user, converting them to integers.
  * Arithmetic operations (`+`, `-`, `*`, `/`) are performed and stored in variables.
  * Results are printed with labels for clarity.

### ✅ Task 2: Personalized Greeting

* **Objective:** Create a greeting using the user's full name.
* **Steps:**

  1. Take first and last name input.
  2. Concatenate to form full name.
  3. Print a personalized message.
* **Approach & Code Explanation:**

  * Inputs are taken using `input()`.
  * Concatenation is done using `+` and a space character.
  * `print()` is used to show the final greeting.

---

## 🔢 Assignment 2: Conditionals and Looping

### ✅ Task 1: Even or Odd Checker

* **Objective:** Determine if a number is even or odd.
* **Steps:**

  1. Accept an integer input.
  2. Use modulo operator and `if-else`.
  3. Print the result accordingly.
* **Approach & Code Explanation:**

  * `number % 2 == 0` is used to check evenness.
  * `if-else` block prints "Even" or "Odd" accordingly.

### ✅ Task 2: Sum of Integers (1–50)

* **Objective:** Calculate the sum using a `for` loop.
* **Steps:**

  1. Use a loop to iterate from 1 to 49.
  2. Accumulate the sum.
  3. Display the final total.
* **Approach & Code Explanation:**

  * `range(1, 51)` creates the number series.
  * A variable `total` accumulates the sum using `+=`.
  * Result is printed after the loop ends.

---

## 🔁 Assignment 3: Functions and Math Module

### ✅ Task 1: Factorial Using Recursion

* **Objective:** Compute the factorial of a number.
* **Steps:**

  1. Define a recursive function `factorial()`.
  2. Take input and call the function.
  3. Print the result.
* **Approach & Code Explanation:**

  * Base case: `if n == 0: return 1`.
  * Recursive call: `return n * factorial(n - 1)`.
  * User input is validated and passed to the function.

### ✅ Task 2: Math Calculations

* **Objective:** Use Python's `math` module.
* **Steps:**

  1. Accept a number from the user.
  2. Calculate square root, natural log, and sine (in radians).
  3. Print each result.
* **Approach & Code Explanation:**

  * `import math` is used to access built-in functions.
  * `math.sqrt()`, `math.log()`, and `math.sin()` are applied.
  * Results are clearly labeled.

---

## 📄 Assignment 4: File Handling

### ✅ Task 1: Read from File with Error Handling

* **Objective:** Read and display content from `sample.txt`.
* **Steps:**

  1. Try to open the file in read mode.
  2. Handle `FileNotFoundError` gracefully.
  3. Print each line with line number.
* **Approach & Code Explanation:**

  * `try-except` block is used.
  * File is read using `with open()` for safe handling.
  * `enumerate()` helps print line numbers.

### ✅ Task 2: Write and Append to File

* **Objective:** Demonstrate writing and appending to a file.
* **Steps:**

  1. Get input and write to `output.txt`.
  2. Accept more input and append it.
  3. Read and display the final file content.
* **Approach & Code Explanation:**

  * `open(file, 'w')` for writing and `'a'` for appending.
  * User input is captured using `input()`.
  * Final content is read and printed line by line.

---

## 📚 Assignment 5: Dictionaries and Lists

### ✅ Task 1: Student Marks Dictionary

* **Objective:** Use a dictionary to store and retrieve student marks.
* **Steps:**

  1. Define a dictionary with name-mark pairs.
  2. Ask user to input a student name.
  3. Display the mark or show a not-found message.
* **Approach & Code Explanation:**

  * Dictionary is defined statically.
  * Input name is matched using `get()` method with default message.

### ✅ Task 2: List Slicing and Reversing

* **Objective:** Perform slicing and manipulation on a list.
* **Steps:**

  1. Create a list from 1 to 10.
  2. Extract the first five elements.
  3. Reverse the sliced list and print both.
* **Approach & Code Explanation:**

  * `list(range(1, 11))` creates the list.
  * Slicing: `list[:5]` and reverse: `[::-1]`.
  * Results are printed to show transformations.

---

## 🚀 How to Run the Programs

1. Clone the repository:

   ```bash
   git clone https://github.com/Amit-Ashok-Swain/Python-td.git
   cd python-assignments
   ```
2. Run each assignment individually using Python:

   ```bash
   python Assignment1.py
   ```

## ✅ Prerequisites

* Python 3.x installed
* Basic command-line interface knowledge

---

## 🧪 Testing & Validation

Each script includes user-friendly prompts and basic error handling to ensure smooth user interaction. Make sure to test with various inputs for validation.

---

## 📞 Support

If you face any issues or have queries, feel free to contact the mentor or use the chat support option.


---

Happy Coding! 🚀
