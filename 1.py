#PYTHON Syntax
print ("Hello, world")
if (5 > 2):
    print("Five is greater than two!")

#PYTHON Comments
#This is a comment
"""
This is a comment
written in 
more that just one line
"""

#PYTHON Variables
carname = "Volvo"
x = 50

x= 5
y = 10
print(x +y)

x = 5
y = 10
z= x + y
print(z)

myfirst_name = "John"

x = y = z = "Orange"

def myfunc(): 
    global x
    x = "fantastic"

#PYTHON Data Types
x = 5
print(type(x))

int

x = "Hello World"
print(type(x))

str

x = 20.5
print(type(x))

float

x = ["apple", "banana", "cherry"]
print(type(x))

list

x = ("apple", "banana", "cherry")
print(type(x))

tuple

x = {"name" : "John", "age" : 36}
print(type(x))

dict

x = True
print(type(x))

bool

#PYTHON Numbers
x = 5
x = float(x)

x = 5.5
x = int(x)

x = 5
x = complex(x)

#PYTHON Strings
x = "Hello World"
print(len(x))

txt = "Hello World"
x = txt[0]

txt = "Hello World"
x = txt[2:5]

txt = " Hello World "
x = txt.strip()

txt ="Hello World "
txt = txt.upper()

txt = "Hello World"
txt = txt.lower()

txt = "Hello World"
txt = txt.replace("H", "J")

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#PYTHON Booleans
print(10 > 9)

True

print(10 == 9)

False

print(10 < 9)

False

print(bool("abc"))

True

print(bool(0))

False

#PYTHON Operators
print(10 * 5)

print(10 / 2)

fruits = ["apple", "banana"]
if ("apple") in fruits:
    print("Yes, apple is a fruit!")

if (5 != 10):
    print("5 and 10 is not equal")

if (5 == 10) or (4 == 4):
  print("At least one of the statements is true")

#PYTHON Lists
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")

fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

#PYTHON Tuples
fruits = ("apple", "banana", "cherry")
print(fruits[0])

fruits = ("apple", "banana", "cherry")
print(len(fruits))

fruits = ("apple", "banana", "cherry")
print(fruits[-1])

fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])

#PYTHON Sets
fruits = {"apple", "banana", "cherry"}
if ("apple" in fruits):
    print("Yes, apple is a fruit!")

fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")

#PYTHON Dictionaries
car =  {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))

car =  {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020

car =  {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"

car =  {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")

car =  {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()

#PYTHON If and Else
a = 50
b = 10
if (a > b):
    print("Hello World")

a = 50
b = 10
if (a != b):
    print("Hello World")

a = 50
b = 10
if (a == b):
    print("Yes")
else:
    print("No")

a = 50
b = 10
if a == b:
  print("1")
elif a > b:
  print("2")
else:
  print("3")

if a == b and c == d:
    print("Hello")

if a == b or c == d:
    print("Hello")

if 5 > 2:
    print("Five is greater than two!")

if 5 > 2: print("Five is greater than two!")

print("Yes") if 5 > 2 else print("No")
