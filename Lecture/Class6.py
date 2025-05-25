# Functional Programming

# Normal Function

def add(x,y):
    return x+y

res = add(1,2)
print(res)


# Assign function to a variable

a = add
res1 = a(1,2)
print(res1)


# Returns function from another function

def call(x,y):
    return add(x,y)

res2 = call(1,2)
print(res2)

c = call

res7 = c(1,2)
print(res7)


# Pass function to a function

def pas(x,y,fn):
    return fn(x,y)

res3 = pas(1,2,call)
print(res3)

# Lambda Function

# Syntax:
# variable name = lambda {arguments} : expression

# With the single argument

def addition_with_one(x):
    return x+1

res4 = addition_with_one(5)
print(res4)

lamb_fn = lambda x:x+1
res5 = lamb_fn(5)
print(res5)

# With two arguments

def addition_with_two(x,y):
    return x+y

lamb_fn1 = lambda x,y:x+y
res6 = lamb_fn1(5,1)
print(res6)


# Filter

# filter (function,iterable)

def even(a):
    return a%2==0

numbers = [1,2,3,4,5]

ans = list(filter(even, numbers))
print(ans)

ans1 = list(filter(lambda x:x%2==0, numbers))
print(ans1)

ans2 = list(filter(lambda x:x%2==1, range(10)))
print(ans2)


# Map

# Syntax
# map(function, iterable)

num = [1,2,3,4,5]

def square(c):
    return c**2

squares = list(map(square, num))
print(squares)

squares_1 = list(filter(square, num))
print(squares_1)

# Here filter is not able to perform the squares of the numbers.
# This is the major difference between map and filter
# Filter basically filter outs the collections and map performs the operation with the collections without filtering.

squares_2 = list(map(lambda x:x%2==0, num))
print(squares_2)
# Here the map is not able to filter the collection with the even lambda function but returns list of true and false.

squares_3 = list(map(lambda x:x**2, range(11)))
print(squares_3)


# Iterator

list_num = [1,2,3,4,5]

iteration = iter(list_num)

print(iteration.__next__())
print(iteration.__next__())
print(next(iteration))
print(next(iteration))
print(next(iteration))


# Generator

# Syntax
def func():
    yield 1

g = func()
print(next(g))


def func2():
    yield 1
    yield 2
    yield 3
    yield 4

g1 = func2()
print(next(g1))
print(g1.__next__())
print(next(g1))
print(g1.__next__())


def square_generator():
    counter = 1
    while counter<=5:
        yield counter**2
        counter += 1

values_generator = square_generator()
print(next(values_generator))
print(next(values_generator))
print(values_generator.__next__())

for value in values_generator:
    print(value)


















