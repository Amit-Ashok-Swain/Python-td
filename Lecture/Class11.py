# Building Database Apps with PostgreSQL & Python

# What is Data?

# 1.Collection of Information.
# 2. Datum -> Single piece of information.
# Ex. Data of a Person -> Name, Age, DOB, Gender, Nationality, etc
# Forms: Text, Numbers, Media, etc...
# Earlier it was written and stored

# What is database?

# 1. What is base?
#  In construction of the house, initially the basement is laid in an organized manner.
# Data + Base -> Database
# Organized in the form of tables by mean of rows and columns.
# Can be easily accessed, managed and updated.
# Main purpose - To operate a large amount of information by storing, retrieving and managing them.
# Many databases are available like - MySQL, Oracle, PostgreSQL, MongoDB, etc


# Types of Database:
# 1. Hierarchical Database
# 2. NoSQL Database
# 3. Object-Oriented Database
# 4. Relational Database
# 5. Network Database

# Relational Database
# 1. Categorized by a set of tables.
# 2. SQL acts as the application interface.
# 3. Easier to modify - a. Extending the database b. Joining the database.

# PostgreSQL
# 1. It is an object-relational database.
# 2. Similar to a relational database.
# 3. Object-oriented database -> objects, classes and inheritance are supported.
# It is open-source.
# Source code is available under PostgreSQL License.
# It supports the building of commercial apps.

"""
import psycopg2

def table():

    conn = psycopg2.connect(dbname="postgres",user="postgres",password="9892321787@As",host="localhost",port="5433")
    print("Connected successfully")

    cursor = conn.cursor()
    cursor.execute('''create table employees(Name Text, ID Int, Age Int, Designation Text);''')

    conn.commit()
    conn.close()

    print("Table created successfully")

def data():

    conn = psycopg2.connect(dbname="postgres",user="postgres",password="9892321787@As",host="localhost",port="5433")

    cursor = conn.cursor()
    cursor.execute('''insert into employees(Name,ID,Age,Designation) values('Amit',9876,27,'Software Engineer');''')

    conn.commit()
    conn.close()

    print("Data added successfully")

# data()


def data_from_user_input():

    name = input("Enter your name: ")
    id = int(input("Enter your ID: "))
    age = int(input("Enter your age: "))
    designation = input("Enter your designation: ")

    conn = psycopg2.connect(dbname="postgres",user="postgres",password="9892321787@As",host="localhost",port="5433")

    cursor = conn.cursor()


    query = '''insert into employees(Name,ID,Age,Designation) values(%s,%s,%s,%s);'''
    cursor.execute(query,(name,id,age,designation))

    conn.commit()
    cursor.close()
    conn.close()

    print("Data added successfully")

data_from_user_input()

def extract():

    conn = psycopg2.connect(dbname="postgres",user="postgres",password="9892321787@As",host="localhost",port="5433")

    cursor = conn.cursor()
    cursor.execute('''select * from employees;''')
    # print(cursor.fetchone())


    show = cursor.fetchone()
    print("Name-",show[0])
    print("ID-",show[1])
    print("Age-",show[2])
    print("Designation-",show[3])

    print(cursor.fetchall())

    conn.commit()
    conn.close()

extract()

"""



