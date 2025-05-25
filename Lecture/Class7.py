 # Object Oriented Programming

 # Class - Blue-print for creating objects.
 # Objects - Instance, created as many times as you want.
 # Attributes - Characteristics associated with a type(obj.).
 # Methods - Functions associated with a type.

 # Creating a class

 # Syntax

"""
 class (name):
    statements & attributes
    ....
    
call the class 

"""

"""


class Car:
    pass # Pass - It is a null operator. It is also a placeholder.

car1 = Car()
print(car1)

class Car1:
    color = "Black"

car2 = Car1().color  # . -> dot notation
print(car2)

class Car2:
    color = "Red"
    type = "SUV"
    model = "G Wagon"

car3 = Car2()
print(car3.color.upper())
car4 = Car2()
print(car4.type.capitalize())
car5 = Car2()
print(car5.model.upper())


class Counting:
    n=0

    def count(self):
        self.n += 1
        print(self.n)

c = Counting()
c.count()
c.count()

"""

# Example 1


# Constructor & Destructor

class Const_Dest:
    x = 0

    def __init__(self):
        print("constructor 1 is created")

    def __del__(self):
        print("destructor 1 is created")


cd = Const_Dest()


class Cars:
    x = 0
    def __init__(self,color,type):
        self.color = color
        self.type = type
        print("constructor 2 is created")
    def __del__(self):
        print("destructor 2 is created")



cars1 = Cars("Black","SUV")
print(cars1.color)

cars2 = Cars("Red","Sedan")
print(cars2.color)
print(cars2.type)

"""
# Functions vs object oriented programming

def name(name):
    print("Hi!",name)

name("Amit")


class Name:

    x=0
    name = ""
    def __init__(self,y):
        self.name = y
        print("Hi!",self.name)


n = Name("Amit")
m = Name("Sedan")

"""

# Inheritance

class Name:

    x=0
    name = ""
    def __init__(self,y):
        self.name = y
        print("Hi!",self.name)


class football_fans(Name):
    pts = 0
    def points(self):
        print(self.name,"Scores")


n = Name("Amit")

f = football_fans("Ronaldo")
f.points()


# Types of inheritance

# 1. Single level inheritance
# 2. Multi-level inheritance
# 3. Multiple inheritance


# 1. Single level inheritance

class A:

    def state1(self):
        print("State 1 is present")
    def state2(self):
        print("State 2 is present")
    def state3(self):
        print("State 3 is present")

class B(A):

    def state4(self):
        print("State 4 is present")
    def state5(self):
        print("State 5 is present")


a = A()
a.state1()
a.state2()

b = B()
b.state3()
b.state4()

# Multi level inheritance

class C(B):
    def state6(self):
        print("State 6 is present")

c = C()
c.state5()
c.state6()

# Multiple inheritance

class D:
    def state7(self):
        print("State 7 is present")

    def state8(self):
        print("State 8 is present")

    def state9(self):
        print("State 9 is present")

class E:

    def state10(self):
        print("State 10 is present")

    def state11(self):
        print("State 11 is present")

class F(D,E):

    def state12(self):
        print("State 12 is present")

d = D()
d.state7()

e = E()
e.state10()

f = F()
f.state8()
f.state11()
f.state12()

# Operator Overloading

class vegetables:

    def __init__(self,carrot,beans):
        self.carrot = carrot
        self.beans = beans

    def __add__(self,other):
        carrot = self.carrot + other.carrot
        beans = self.beans + other.beans
        return vegetables(carrot,beans)

    def __sub__(self,other):
        carrot = self.carrot - other.carrot
        beans = self.beans - other.beans
        return vegetables(carrot,beans)

    def __mul__(self,other):
        carrot = self.carrot * other.carrot
        beans = self.beans * other.beans
        return vegetables(carrot,beans)

    def __truediv__(self,other):
        carrot = self.carrot / other.carrot
        beans = self.beans / other.beans
        return vegetables(carrot,beans)


v1 = vegetables(19,14)
v2 = vegetables(10,6)

v3 = v1 + v2
v4 = v1 - v2


print(v3.carrot)
print(v4.carrot)


print(v3.beans)
print(v4.beans)


# Data hiding

class Simple:

    def __init__(self):
        self._value_1 = 1
        self.__value_2 = 2 # __ - Double underscore indicates private attribute

    def _A1_(self):
        print("Apple")

    def _B1_(self):
        print("Banana")

    def __C1_(self): # __ - Double underscore indicates private attribute
        print("Cherry")

    def __D1_(self): # __ - Double underscore indicates private attribute
        print("Dark")


s1 = Simple()

print(s1._value_1)
s1._A1_()
s1._B1_()

print(dir(s1))

print(s1._Simple__value_2)
s1._Simple__C1_()
s1._Simple__D1_()

