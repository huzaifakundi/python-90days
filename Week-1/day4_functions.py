

"""
# =============================================
# WEEK 1 · DAY 3 — Functions & Conditionals
# =============================================

# --- BASIC FUNCTION (no input, no output) ---
def greet():
    print("Assalam o Alaikum! Welcome to Day 3.")

greet()   # calling the function

# --- FUNCTION WITH PARAMETERS (takes input) ---
def greet_person(name):
    print(f"Assalam o Alaikum, {name}!")

greet_person("Samiullah")
greet_person("Ali")

# --- FUNCTION WITH RETURN (gives back a value) ---
def add_numbers(a, b):
    result = a + b
    return result

answer = add_numbers(10, 25)
print(f"10 + 25 = {answer}")

# --- FUNCTION WITH MULTIPLE PARAMETERS ---
def student_info(name, cgpa, semester):
    return f"{name} | Semester {semester} | CGPA: {cgpa}"

info = student_info("Samiullah", 2.8, 6)
print(info)

# --- DEFAULT PARAMETERS ---
def greet_with_title(name, title="Engineer"):
    print(f"Hello, {title} {name}!")

greet_with_title("Samiullah")            # uses default "Engineer"
greet_with_title("Samiullah", "AI Dev")  # overrides default

"""
"""

def learning_message(name):
    return (f"{name} is learning python and loving it!")
learning_message("samiullah")
learning_message("alisamiullah")
def greet():
    print("Hello")
greet()
def greet_person(name):
    print(f"Hello, {name}!")
greet_person("sami")
def add_numbers(x,y):
    return x+y
result = add_numbers(5,7)
print(result)

answer= add_numbers(10,100)
print(f"sum={answer}")

def student_gpa(miss,gpa):
    print(f"{miss} has a cgpa of {gpa}")
    gpa=student_gpa("3797",2.65)
    print(gpa)
def greet_with_title(name,title="developer"):
        print(f"sir {name} is a {title}")
greet_with_title("samiullah")
greet_with_title("samiullah","python developer")

"""

x=y=z="Orange"
y=a="Apple"
print (x)
print (x)
print (y)
print (z)
print (a)