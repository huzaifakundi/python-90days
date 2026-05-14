print("Hello, World!")
if 5 > 3:
    print("5 is greater than 3")
x=5
y="Hello, World!"
print(x,end=" ")
print(y)
print("I am",24,"years old.")
###################
print(type(x))
print(type(y))
###################
fruits = ["apple", "banana", "cherry"]
x,y,z = fruits
print(x)
print(y)   
print(z)
#################
x="Awesome"
def myfunc():
    print("Python is " + x)
myfunc()
##################
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()
print("Python is " + x)
#####################
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#
# Day 1 - Python Basics
# Name: Huzaifa Kundi
# Date: Day 1 of 90

# Variables
name = "Huzaifa"
age = 24
city = "Chashma"
gpa = 3.3
is_student = True

# Print
print("Hello World!")
print(f"My name is {name} and I am {age} years old")
print(f"I live in {city} with a GPA of {gpa}")
print(f"Am I a student? {is_student}")

# Data types
print(type(name))    # str
print(type(age))     # int
print(type(gpa))     # float
print(type(is_student))  # bool

# Basic math
print(5 + 3)
print(10 - 4)
print(3 * 4)
print(10 / 2)