# Calculator

from tkinter import *

window = Tk()

window.geometry("500x500")

def click(num):
    result = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(result)+str(num))

entry = Entry(window,width=54,borderwidth=3,relief=SUNKEN)
entry.place(x=0,y=0)

b = Button(window,text="1",width=12,command=lambda:click(1))
b.place(x=10,y=60)

b = Button(window,text="2",width=12,command=lambda:click(2))
b.place(x=150,y=60)

b = Button(window,text="3",width=12,command=lambda:click(3))
b.place(x=290,y=60)

b = Button(window,text="4",width=12,command=lambda:click(4))
b.place(x=10,y=120)

b = Button(window,text="5",width=12,command=lambda:click(5))
b.place(x=150,y=120)

b = Button(window,text="6",width=12,command=lambda:click(6))
b.place(x=290,y=120)

b = Button(window,text="7",width=12,command=lambda:click(7))
b.place(x=10,y=180)

b = Button(window,text="8",width=12,command=lambda:click(8))
b.place(x=150,y=180)

b = Button(window,text="9",width=12,command=lambda:click(9))
b.place(x=290,y=180)

b = Button(window,text="0",width=12,command=lambda:click(0))
b.place(x=10,y=240)

def add():
    n1 = entry.get()
    global i
    global math
    math = "add"
    i  = int(n1)
    entry.delete(0, END)

b = Button(window,text="+",width=12, command=add)
b.place(x=150,y=240)

def sub():
    n1 = entry.get()
    global i
    global math
    math = "sub"
    i  = int(n1)
    entry.delete(0, END)

b = Button(window,text="-",width=12, command=sub)
b.place(x=290,y=240)

def mul():
    n1 = entry.get()
    global i
    global math
    math = "mul"
    i  = int(n1)
    entry.delete(0, END)

b = Button(window,text="x",width=12,command=mul)
b.place(x=10,y=300)

def div():
    n1 = entry.get()
    global i
    global math
    math = "div"
    i  = int(n1)
    entry.delete(0, END)

b = Button(window,text="÷",width=12,command=div)
b.place(x=150,y=300)

def equal():
    n2 = entry.get()
    entry.delete(0, END)

    if math == "add":
        entry.insert(0,i+int(n2))
    elif math == "sub":
        entry.insert(0,i-int(n2))
    elif math == "mul":
        entry.insert(0,i*int(n2))
    elif math == "div":
        entry.insert(0,i/int(n2))


b = Button(window,text="=",width=12,command=equal)
b.place(x=290,y=300)

def clear():
    entry.delete(0, END)

b = Button(window,text="A/C",width=12,command=clear)
b.place(x=10,y=350)

window.mainloop()

