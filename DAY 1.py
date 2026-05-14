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