# Tkinter

"""
🧱 What is Tkinter?
Tkinter is Python’s standard library for building Graphical User Interfaces (GUIs).
It's a wrapper around the Tcl/Tk GUI toolkit.
"""

"""
# Step 1: Import tkinter

from tkinter import * # This imports all classes and functions from the tkinter module.
# You can now use Label, Tk, Button, etc., without prefixing them with tkinter.

# Step 2: GUI Interaction

window = Tk() # This creates the main application window.
# Think of it as the blank canvas where you'll place all your GUI components like buttons, text fields, etc.

# Step 3: Adding Inputs

# input = Label(window, text="Hello World!") # This creates a label widget. It will display the text "Hello World!" inside the window.
# input.pack() # This adds the label to the window and uses geometry management to place it automatically (centered by default).
window.title("Jai Shree Ram")
window.geometry("500x700")
window.configure(bg="orange")

frame1 = Frame(window,bg="red",width=300,height=300,cursor="heart")
frame2 = Frame(window,bg="yellow",width=300,height=300,cursor="dot")

btn1 = Button(frame1,text="Start",bg="green",cursor="dot")
btn2 = Button(frame2,text="Quit",bg="purple",cursor="dot")
btn3 = Button(frame1,text="Mini Project",bg="blue",cursor="dot")

frame1.pack(side=TOP)
frame2.pack(side=BOTTOM)
btn1.pack()
btn2.pack()
btn3.pack()
# Step 4: Main loop

window.mainloop() # This tells Python to run the GUI application.
# The app stays open and listens for events (like mouse clicks) until the window is closed.
# It’s a blocking call, meaning it keeps running until you exit.

"""

"""
# Login Window

from tkinter import *

window = Tk()

window.title("Login In")

label1 = Label(window,text="E-mail:")
label2 = Label(window,text="Password:")

entry1 = Entry(window,width=40,borderwidth=5,relief="ridge")
entry2 = Entry(window,width=40,borderwidth=5,relief="ridge")

btn = Button(window,text="Login",bg="green",cursor="dot")

label1.grid(row=0,column=0)
entry1.grid(row=0,column=1)
label2.grid(row=1,column=0)
entry2.grid(row=1,column=1)
btn.grid(row=2,column=1)

window.mainloop()

"""

"""

# pack()

from tkinter import *
window = Tk()
title = Label(window,text="Pack")
window.geometry("500x700")

label1 = Label(window,text="Label_1",bg="red",fg="white")
label2 = Label(window,text="Label_2",bg="green",fg="white")
label3 = Label(window,text="Label_3",bg="blue",fg="white")

label1.pack(side=TOP,fill=X,expand=False)
label2.pack(side=LEFT,fill=Y,expand=False)
label3.pack(side=RIGHT,fill=Y,expand=False)

window.mainloop()

"""
# Handling buttons

"""

from tkinter import *
window = Tk()

def log_status():
    print("Logged In")

btn = Button(window, text="Login", bg="green", fg="white",
             activebackground="black", activeforeground="white",
             highlightbackground="green", font=("Bold", 12), cursor="dot", width=12,
             command=log_status)

btn.pack()

window.mainloop()

"""

# Menu

"""

from tkinter import *
window = Tk()

menu = Menu(window)

file = Menu(menu, tearoff=False)

file.add_command(label="New")
file.add_command(label="Open")
file.add_command(label="Save")
file.add_command(label="Save As")
file.add_separator()
file.add_command(label="Exit",command=window.quit)

menu.add_cascade(label="File", menu=file)
window.config(menu=menu)
window.mainloop()

"""

# Message box

"""

from tkinter import *
import tkinter.messagebox as messagebox

window = Tk()

messagebox.showinfo("Info","The download is in progress")
messagebox.showerror("Error","Something went wrong")
message = messagebox.askyesno("Delete file","Do you really want to delete it?")

if message:
    print("Deleted")
else:
    print("Cancelled")

window.mainloop()


"""

# Canvas(Drawing)

"""

from tkinter import *
window = Tk()
c = Canvas(window,width=500,height=500)
c.pack()

c.create_line(0,0,500,500, width=5, fill="blue", dash=(5,5))
c.create_line(0,500,500,0, width=5, fill="purple", dash=(5,5))
c.create_rectangle(150,125,450,375, fill="red", outline="pink", width=5)

mainloop()

"""

# Message box 2

from tkinter import *
window = Tk()

window.title("Message box with button interaction")
window.geometry("500x700")

"""

var = StringVar()

message = Message(window, textvariable=var, relief="ridge", padx=75, pady=75)
var.set("Welcome to Lecture")
message.pack()
window.mainloop()

"""

"""

def insert():
    text = entry_var.get()
    message_var.set(text)


message_var = StringVar()
entry_var = StringVar()

message = Message(window,textvariable=message_var, relief="ridge", padx=75, pady=75)
entry = Entry(window,textvariable=entry_var)
button = Button(window,text="OK",command=insert)

message.pack()
entry.pack()
button.pack()
window.mainloop()

"""

"""

# Checkbox

from tkinter import *
window = Tk()
window.geometry("500x500")

check_box1 = IntVar()
check_box2 = IntVar()
check_box3 = IntVar()

check_btn1 = Checkbutton(window,text="Apple",onvalue=1, offvalue=0, height=2, width=10, variable=check_box1)
check_btn2 = Checkbutton(window, text="Banana", onvalue=1, offvalue=0, height=2, width=10, variable=check_box2)
check_btn3 = Checkbutton(window, text= "Mango", onvalue=1, offvalue=0, height=2, width=10, variable=check_box3)

check_btn1.pack()
check_btn2.pack()
check_btn3.pack()

window.mainloop()

"""

# Place

from tkinter import *
window = Tk()
window.geometry("500x500")

button = Button(window,text="Button",width=10)
button.place(x=200,y=200)
window.mainloop()



