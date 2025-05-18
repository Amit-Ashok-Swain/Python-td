# list ---> [], index values
# list = [1,2,3,4,5] , index values -> 0,1,2,3,4

# Dictionary --> {}, key
# dictionary = {key:value, key:value, key:value}, it occurs in key-value pairs

my_dict = {'Key1': 'Amit', 'Key2': [1,2,3,4,5], 'Key3': (7,7,7), 'Key4': 5.5, 'Key5': True}
print(my_dict)
print(my_dict['Key2'])

for key in my_dict:
    print(my_dict[key])

print()
print()

# Dictionary Functions

dictionary1 = {'a': 'apple', 'b': 'banana', 'c': 'cherry', 'd': 'dragon-fruit', 'e': 'egg-fruit', 'f': 'fig', 'g': 'guava'}
print(dictionary1)
print(dictionary1['g'])

dictionary1['h'] = 'hazelnut'
print(dictionary1)

del dictionary1['e']
print(dictionary1)

print('d' in dictionary1) # prints boolean whether the key is present or not in dictionary.

print(dictionary1.keys())

print(dictionary1.values())

print(dictionary1.items())

print(dictionary1.get('i','i not found'))
print(dictionary1.get('h'))


print()
print()

# LIST

number_list = [1,2,3,4,5]
print(number_list[3])

colours = ['black', 'red', 'white', 'orange', 'yellow']
print(colours[3])

mix = ["Amit",10,"Ganesh",100,"Shiva",1000,"Vishnu",1000,"Durga",1000,"Shani",1000]
print(mix[2])

blank_list = []
print(blank_list)

print()
print()

# List Operations

list1 = ['Amit',7.6,1998]
list2 = ['Vasudev Krishn', 'True']

print(list1 + list2)


list3 = ['Computer Science', 78, 0.03]
print(list3[1])
list3[2] = True
print(list3)

# Lists are mutable

n = [1,2,3,4,5]
print(n*3)

game = ['cricket','football','basketball']
print('cricket' in game) # returns true if 'cricket' is present in list game

print()
print()

# List functions

l1 = ['Amit',7.6,1998]
l1.append(7.15)
print(l1)

l2 = ['Amit',7.6,1998]
l2.extend([45,99.9,True])
print(l2)

l3 = ['Amit', 7.6, 1998, 45, 99.9, True]
l3.remove(45)
print(l3)

l4 = ['Amit', 7.6, 1998, 99.9, True]
del l4[0:3]
print(l4)

l5 = ['Amit', 7.6, 1998, 99.9, True,'text','mathematics']
del l5[1:3]
print(l5)

l6 = ['Amit', 99.9, True, 'text', 'mathematics']
l6.clear()
print(l6)

l7 = ['Amit', 99.9, True, 'text', 'mathematics']
l7.pop(2)
print(l7)

l8 = ['Amit', 99.9,'text', 'mathematics']
l8.insert(1,"Swain")
print(l8)

l9 = [89.2, 0.01, -1, -45, 99, 3, 7]
l9.sort()
print(l9)

l9.reverse()
print(l9)

print(l9.index(0.01))
print(len(l9))

print()
print()

# List Slicing

l10 = [10,20,30,40,50,60,70]

# list_name[n:n+1:interval]

print(l10[0:5])
print(l10[:])
print(l10[2:6])
print(l10[:6])
print(l10[3:])
print(l10[:7:2])
print(l10[::2])
print(l10[::-1])
print(l10[::-2])
print(l10[2:7:3])

print()
print()

# list comprehension

x = []

for i in range(11):
    z = i ** 2
    x.append(z)
print(x)

# Syntax
# [expression  for item in a list  {if (test expression)}}

y = [i**2 for i in range(11)]
print(y)


x1 = []

for i in range(11):
    if i % 2 == 0:
        z = i ** 2
        x1.append(z)
print(x1)

y1 = [i**2 for i in range(11) if (i ** 2) % 2 == 0]
print(y1)

print()
print()

# Sets

# type of collection
# unordered -> no track of indexes
# unique elements
#{}

set1 = {1,2,3,4,5}
set1.add(6)
print(set1)

set2 = {1,2,3,4,5,6,7}
set2.remove(6)
print(set2)

set3 = set1.copy()
print(set3)

set4 = set1.intersection(set2)
print(set4)
print(set1)
set5 = set3.intersection(set2)
print(set5)
set6 = set1.difference(set2)
print(set6)
set7 = set2.difference(set1)
print(set7)
set8 = set1.union(set2)
print(set8)
print(set1.issubset(set8))
set9 = set1.symmetric_difference(set2)
print(set9)

print()
print()

# String functions

name = 'AmiT'

print(name.capitalize())
print(name.upper())
print(name.lower())

num = '7'
alpha = 'K'

print(num.isnumeric())
print(alpha.isnumeric())
print(num.isalpha())
print(alpha.isalpha())

sen = 'Amit is a good boy'
print(sen.startswith('Amit'))
print(sen.endswith('boy')) # it is case-sensitive
print(sen.replace('Amit', 'Swain'))
print(sen.find('good')) # it is case-sensitive and returns the index of the first character string 'good'


sen1 = '    Amit is a good boy'
sen2 = 'Amit is a good boy  '

print(sen1.lstrip())
print(sen2.rstrip())

print(sen.split())
print(sen.splitlines())

sen3 = 'Amit is a good boy. He is devotee of Lord Jagannath'
print(sen3.splitlines())


names = 'Amit','Swain'
print(names)

name1 = ','

print(name1.join(names))


# String formatting

name2 = 'Mike'
name_len = len(name2 * 3)
print("Hello {}, Your lucky number is {}.".format(name2,name_len))

example = "format() method."
print("These are the examples of {}".format(example))

first = 'apple'
second = 'banana'
third = 'cherry'

print("{},{},{}".format(first,second,third))
print("{1},{2},{0}".format(first,second,third))

price = 500
price_tax = 500 + 500 * 0.15

print("The price of the ice-cream is {:.2f} and including gst the total cost is {:.2f}.".format(price,price_tax))

print()
print()

# Tuples

numbs = (1,2,3,4,5)

print(numbs)
print(type(numbs))
print(numbs[2])

tup1 = ('Mike',10.5,True,115)
tup2 = ('Hike',False,998,0.02)

print(tup1 + tup2)
print(len(tup1))

# tuples are immutable
"""
numbers1 = (1,2,3,4,5)
numbers1[1] = 0 # 'tuple' object does not support item assignment it is immutable.
print(numbers1)
"""

# lists are mutable
numbers2 = [1,2,3,4,5]
numbers2[1] = 0
print(numbers2)


tup3 = (889, 982, 88 ,6, 7 ,83, -1, 0.092, -99, 78, 10)
tup_sorted = sorted(tup3)
print(tup_sorted)

print(tup3.index(-1))


