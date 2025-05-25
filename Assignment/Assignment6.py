import tkinter as tk

# Hover effect function
def on_enter(e):
    e.widget["bg"] = "#d0d0d0"

def on_leave(e):
    e.widget["bg"] = "#e0e0e0"

# Main app window
root = tk.Tk()
root.title("🧮 Modern Calculator")
root.configure(bg="#2c2c2c")
root.geometry("420x540")
root.resizable(False, False)

# Entry field
entry = tk.Entry(root, font=("Segoe UI", 28), bd=0, relief=tk.FLAT,
                 bg="#1e1e1e", fg="white", justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=30, padx=20, ipady=10, sticky="we")

# Calculator logic
first_number = None
operation_type = None

def click(num):
    entry.insert(tk.END, str(num))

def clear():
    entry.delete(0, tk.END)

def operation(op):
    global first_number, operation_type
    try:
        first_number = float(entry.get())
        operation_type = op
        entry.delete(0, tk.END)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

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

# Button builder
def create_button(text, cmd, r, c, w=1, h=1):
    btn = tk.Button(root, text=text, command=cmd, font=("Segoe UI", 20), width=4*w, height=2*h,
                    bg="#e0e0e0", fg="black", bd=0, relief=tk.FLAT, activebackground="#cfcfcf")
    btn.grid(row=r, column=c, columnspan=w, padx=10, pady=10, sticky="nsew")
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

# Button layout
buttons = [
    ("7", lambda: click(7)), ("8", lambda: click(8)), ("9", lambda: click(9)), ("➗", lambda: operation("div")),
    ("4", lambda: click(4)), ("5", lambda: click(5)), ("6", lambda: click(6)), ("✖️", lambda: operation("mul")),
    ("1", lambda: click(1)), ("2", lambda: click(2)), ("3", lambda: click(3)), ("➖", lambda: operation("sub")),
    ("0", lambda: click(0)), (".", lambda: click(".")), ("=", equal), ("➕", lambda: operation("add")),
    ("C", clear)
]

# Place buttons in grid
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

# Grid config for responsiveness
for i in range(4):
    root.columnconfigure(i, weight=1)
for i in range(6):
    root.rowconfigure(i, weight=1)

# Start app
root.mainloop()
