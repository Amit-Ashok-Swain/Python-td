# Calculator using Tkinter

import tkinter as tk # Imports the tkinter library using alias tk.

# Hover effect function
def on_enter(e):
    e.widget["bg"] = "#d0d0d0" # e.widget is the button widget being hovered over.
    # When mouses enters, it changes the background to light gray

def on_leave(e):
    e.widget["bg"] = "#e0e0e0" # When mouses leaves, it changes the background back to dark gray.

#  Create the Main Application Window
window = tk.Tk() # Initializes the window (the main GUI)
window.title("📟Modern Calculator") # Sets the window title
window.configure(bg="#2c2c2c") # Sets background color to dark gray
window.geometry("420x540") # sets window size to 420x540
window.resizable(False, False) # Disables the resizing

# What User Sees: A non-resizable dark-themed calculator window with a title.


# Entry field (Display Screen)
entry = tk.Entry(window, font=("Segoe UI", 28), borderwidth=0, relief=tk.FLAT, bg="#1e1e1e", fg="white", justify="right")
# Entry() - Creates a single-line text box for displaying input/output
# font = ("Segoe UI",28) - Sets the font family and size. The text will appear in Segoe, 28-point size - large and modern
# borderwidth=0 - No border around the entry box. Keeps the design clean
# relief=tk.FLAT - Sets the relief to flat. This makes the entry box look like a button.
# bg="1e1e1e" - Sets the background color to dark gray
# fg="white" - Sets the text color to white
# justify="right" - Sets the justification to right. This makes the text appear to the right of the entry box. Like most calculators do


# What User Sees: A dark-colored box with white, right-aligned large numbers.

entry.grid(row=0, column=0, columnspan=4, pady=30, padx=20, ipady=10, sticky="we") # Places the entry box in the grid
# entry.grid() -  tells Tkinter how and where to place the entry widget on the window, using the grid geometry manager.
# Row=0, column=0 - Place the entry in the first row, first column of the grid layout.
# columnspan=4 - The entry box should span across 4 columns, so it is as wide as all numbers buttons combined.
# Pady=30 - Adds vertical padding of 30 pixels above and below for spacing.
# padx=20 - Adds horizontal padding of 20 pixels left and right for spacing.
# Ipady=10 - Adds internal vertical padding. Makes the box taller inside
# sticky="we" - Sticks the entry box to the left and right edges of the window. This makes it look like a number box.

# Variables to track state
first_number = None # Stores first operand
operation_type = None # Stores operation type
# Used between pressing a number → operation → equals.

# Input Handling functions

# Click Number
def click(num):
    entry.insert(tk.END, str(num)) # Inserts the number into the entry box

# Clear Screen
def clear():
    entry.delete(0, tk.END) # Deletes all text in the entry box

# Set Operation
def operation(op):
    global first_number, operation_type
    try:
        first_number = float(entry.get()) # Converts the text in the entry box to a float
        operation_type = op # Stores the operation type
        entry.delete(0, tk.END) # Deletes all text in the entry box
    except:
        entry.delete(0, tk.END) # If the text in the entry box is not a valid number, delete it
        entry.insert(0, "Error") # Insert "Error" into the entry box

# Equal
def equal():
    global first_number, operation_type
    try:
        second = float(entry.get()) # Converts the text in the entry box to a float
        entry.delete(0, tk.END) # Deletes all text in the entry box
        if operation_type == "add":
            result = first_number + second # Adds the two numbers
        elif operation_type == "sub":
            result = first_number - second # Subtracts the two numbers
        elif operation_type == "mul":
            result = first_number * second # Multiplies the two numbers
        elif operation_type == "div":
            if second == 0: # Checks if the second number is 0
                result = "NaN" # If it is, display "NaN"
                entry.insert(0, result)
            else:
                result = first_number / second
        else:
            result = "Error" # If the operation type is invalid, display "Error"
        entry.insert(0, str(result)) # Displays the result in string
    except:
        entry.insert(0, "Error") # If the text in the entry box is not a valid number, display "Error"


#  Reusable Button Creator

def create_button(text, cmd, r, c,w=1, h=1): # create_button() is a function that simplifies button creation.
    btn = tk.Button(window, text=text, command=cmd, font=("Segoe UI", 20), width=4*w, height=2*h, 
                    bg="#e0e0e0", fg="black", bd=0, relief=tk.FLAT, activebackground="#cfcfcf")
    btn.grid(row=r, column=c, columnspan=w, padx=10, pady=10, sticky="nsew")
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
# Parameters
# text - The label/text to display on the buttons (eg. 1, 2, +, =)
# cmd - The parameter named command to execute when the button is clicked.
# r - The row number in the grid layout where the button should appear.
# c - The column number in the grid layout where the button should appear.
# w & h - width and height multipliers
# btn.grid() - Used for positioning of the button.
"""
row=r: Row number in the grid.

column=c: Column number.

columnspan=w: Span across multiple columns (used for wide buttons like "C").

padx=10, pady=10: Add spacing around the button.

sticky="nsew": Make the button expand in all directions (North, South, East, West) to fill the grid cell.

"""
# btn.bind() - Adding Hover Effect
# "<Enter>": Triggered when the mouse pointer enters the button area — changes the background color.
# "<Leave>": Triggered when the mouse leaves — resets the background.
# These are handled by the functions you defined earlier as on_enter & on_leave.

# What User Sees: Modern rounded buttons with hover effects.


# Button Labels and Functions

buttons = [
    ("7", lambda: click(7)), ("8", lambda: click(8)), ("9", lambda: click(9)), ("➗", lambda: operation("div")),
    ("4", lambda: click(4)), ("5", lambda: click(5)), ("6", lambda: click(6)), ("✖️", lambda: operation("mul")),
    ("1", lambda: click(1)), ("2", lambda: click(2)), ("3", lambda: click(3)), ("➖", lambda: operation("sub")),
    ("0", lambda: click(0)), (".", lambda: click(".")), ("=", equal), ("➕", lambda: operation("add")),
    ("C", clear)
]

# Create buttons using the buttons list
for i, (text, cmd) in enumerate(buttons):
    row = (i // 4) + 1
    col = i % 4
    create_button(text, cmd, row, col)

# Dry run of button placement:

# i=0: ("7", click(7))
# i//4 = 0//4 = 0, row = 1
# i%4 = 0%4 = 0, col = 0
# Result: "7" placed at row 1, col 0

# i=1: ("8", click(8))
# i//4 = 1//4 = 0, row = 1
# i%4 = 1%4 = 1, col = 1
# Result: "8" placed at row 1, col 1

# i=2: ("9", click(9))
# i//4 = 2//4 = 0, row = 1
# i%4 = 2%4 = 2, col = 2
# Result: "9" placed at row 1, col 2

# i=3: ("➗", operation("div"))
# i//4 = 3//4 = 0, row = 1
# i%4 = 3%4 = 3, col = 3
# Result: "➗" placed at row 1, col 3

# i=4: ("4", click(4))
# i//4 = 4//4 = 1, row = 2
# i%4 = 4%4 = 0, col = 0
# Result: "4" placed at row 2, col 0

# And so on...
"""
[7] [8] [9] [➗]  # Row 1 (i=0,1,2,3)
[4] [5] [6] [✖️]  # Row 2 (i=4,5,6,7)
[1] [2] [3] [➖]  # Row 3 (i=8,9,10,11)
[0] [.] [=] [➕]  # Row 4 (i=12,13,14,15)
[C]  # Row 5 (i=16)
"""

window.mainloop()