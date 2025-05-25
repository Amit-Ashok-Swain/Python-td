# Python Programming Assignments

This repository contains five foundational Python programming assignments designed to build a solid understanding of basic programming concepts. Each assignment includes two tasks covering a variety of topics such as user input, control flow, loops, functions, file handling, and data structures.

## 📁 Repository Structure

```
Assignment1.py
Assignment2.py
Assignment3.py
Assignment4.py
Assignment5.py
Assignment6.py

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

## 📚 Assignment 6: Calculator using Tkinter

Absolutely! Let’s go through the **modern Tkinter calculator code** line by line with **detailed explanations** of how everything works, including UI design and functionality:


---

### 1. **Importing Tkinter**

```python
import tkinter as tk
```

* This imports the `tkinter` library and assigns it the alias `tk`. Tkinter is Python’s standard GUI (Graphical User Interface) package.

---

### 2. **Hover Effect Functions**

```python
def on_enter(e):
    e.widget["bg"] = "#d0d0d0"

def on_leave(e):
    e.widget["bg"] = "#e0e0e0"
```

* These two functions define how a button’s background color changes when the mouse **hovers over it** (`on_enter`) and **leaves** (`on_leave`).
* `e.widget` refers to the widget (button) triggering the event.
* This creates a **hover animation effect**.

---

### 3. **Creating the Main Application Window**

```python
root = tk.Tk()
root.title("🧮 Modern Calculator")
root.configure(bg="#2c2c2c")
root.geometry("420x540")
root.resizable(False, False)
```

* `tk.Tk()` initializes the main window.
* `title()` sets the window's title text.
* `configure(bg=...)` sets the background color (dark theme).
* `geometry("420x540")` sets a fixed size (width x height in pixels).
* `resizable(False, False)` disables resizing to maintain layout integrity.

---

### 4. **Creating the Entry Field**

```python
entry = tk.Entry(root, font=("Segoe UI", 28), bd=0, relief=tk.FLAT,
                 bg="#1e1e1e", fg="white", justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=30, padx=20, ipady=10, sticky="we")
```

* `tk.Entry(...)` creates a **text input box**.
* `font`, `bg`, `fg`, etc., style the box with large text and dark theme.
* `justify="right"` makes text align to the right like in real calculators.
* `.grid(...)` places the entry box in the first row (row=0) and spans all 4 columns (`columnspan=4`) with padding.

---

### 5. **State Variables for Calculation Logic**

```python
first_number = None
operation_type = None
```

* These hold the first number typed and the operation selected (`add`, `sub`, etc.), used later when `=` is pressed.

---

### 6. **Button Functions**

#### A. Appending Numbers to Entry Field

```python
def click(num):
    entry.insert(tk.END, str(num))
```

* When a number is clicked, this function adds it to the entry field.

#### B. Clearing the Entry Field

```python
def clear():
    entry.delete(0, tk.END)
```

* Clears everything from the entry field.

#### C. Performing an Operation (Storing State)

```python
def operation(op):
    global first_number, operation_type
    try:
        first_number = float(entry.get())
        operation_type = op
        entry.delete(0, tk.END)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
```

* This stores the current number and the selected operation (`add`, `sub`, etc.).
* Clears the entry to prepare for second input.
* Uses `try/except` to prevent crashes if entry is empty or invalid.

#### D. Calculating Result When `=` Is Pressed

```python
def equal():
    global first_number, operation_type
    try:
        second = float(entry.get())
        entry.delete(0, tk.END)

        if operation_type == "add":
            result = first_number + second
        elif operation_type == "sub":
            result = first_number - second
        elif operation_type == "mul":
            result = first_number * second
        elif operation_type == "div":
            if second == 0:
                result = "Error"
            else:
                result = first_number / second
        else:
            result = "Error"
        entry.insert(0, str(result))
    except:
        entry.insert(0, "Error")
```

* Retrieves second number.
* Performs stored operation.
* Handles division by zero (`/0`) and general exceptions.
* Shows result or error in the entry field.

---

### 7. **Reusable Button Creation Function**

```python
def create_button(text, cmd, r, c, w=1, h=1):
    btn = tk.Button(root, text=text, command=cmd, font=("Segoe UI", 20), width=4*w, height=2*h,
                    bg="#e0e0e0", fg="black", bd=0, relief=tk.FLAT, activebackground="#cfcfcf")
    btn.grid(row=r, column=c, columnspan=w, padx=10, pady=10, sticky="nsew")
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
```

* Creates a styled button and places it in a grid cell.
* Adds **hover effects** using `.bind()` events.
* Uses default args (`w`, `h`) to allow wide/tall buttons like "C".

---

### 8. **All Button Definitions with Text, Command**

```python
buttons = [
    ("7", lambda: click(7)), ("8", lambda: click(8)), ("9", lambda: click(9)), ("➗", lambda: operation("div")),
    ("4", lambda: click(4)), ("5", lambda: click(5)), ("6", lambda: click(6)), ("✖️", lambda: operation("mul")),
    ("1", lambda: click(1)), ("2", lambda: click(2)), ("3", lambda: click(3)), ("➖", lambda: operation("sub")),
    ("0", lambda: click(0)), (".", lambda: click(".")), ("=", equal), ("➕", lambda: operation("add")),
    ("C", clear)
]
```

* Each tuple has button **text** and the **function to execute**.
* Emojis (`➗`, `✖️`, `➖`, `➕`) are used instead of boring symbols.

---

### 9. **Placing Buttons in Grid**

```python
row = 1
col = 0
for text, cmd in buttons:
    if text == "C":
        create_button(text, cmd, row, col, w=4)
        break
    create_button(text, cmd, row, col)
    col += 1
    if col > 3:
        col = 0
        row += 1
```

* Loops through button list and places them in a grid.
* Places "C" as a full-width button at the bottom (`w=4`).

---

### 10. **Making Layout Responsive**

```python
for i in range(4):
    root.columnconfigure(i, weight=1)
for i in range(6):
    root.rowconfigure(i, weight=1)
```

* Allows buttons to expand evenly in the grid when resizing (if resizing was enabled).
* Makes sure buttons and entry look nice and proportionate.

---

### 11. **Running the App**

```python
root.mainloop()
```

* Starts the Tkinter **event loop**, displaying the window and listening for user interaction.

---

## ✅ Summary of Features

| Feature          | How It Works                                            |
| ---------------- | ------------------------------------------------------- |
| Number Buttons   | Adds number to entry field                              |
| Operator Buttons | Stores first number and operator                        |
| Equals `=`       | Calculates and shows result                             |
| Clear `C`        | Clears the input                                        |
| Hover Effect     | Changes button color on mouse hover                     |
| Emojis as Icons  | Visual enhancement with symbols                         |
| Responsive Grid  | Even spacing and size for all elements                  |
| Error Handling   | Prevents crashes from empty input or invalid operations |


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

Happy Coding! 🚀
