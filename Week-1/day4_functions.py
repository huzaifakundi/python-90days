# =============================================
# DAY 4 — Functions & Conditionals
# =============================================

# Basic function
def greet():
    print("Assalam o Alaikum! Welcome to Day 4.")
greet()

# Function with parameters
def greet_person(name):
    print(f"Assalam o Alaikum, {name}!")
greet_person("Huzaifa")

# Function with return
def add_numbers(a, b):
    return a + b
print(f"10 + 25 = {add_numbers(10, 25)}")

# Multiple parameters
def student_info(name, cgpa, semester):
    return f"{name} | Semester {semester} | CGPA: {cgpa}"
print(student_info("Huzaifa", 3.3, 7))

# Default parameters
def greet_with_title(name, title="Engineer"):
    print(f"Hello, {title} {name}!")
greet_with_title("Huzaifa")
greet_with_title("Huzaifa", "AI Developer")

# Grade checker
def check_grade(marks):
    if marks >= 90:
        return "A — Excellent!"
    elif marks >= 80:
        return "B — Good"
    elif marks >= 70:
        return "C — Average"
    elif marks >= 60:
        return "D — Below Average"
    else:
        return "F — Failed"

score = int(input("Enter marks: "))
print(check_grade(score))

# BMI Calculator
def calculate_bmi(weight, height):
    return weight / (height ** 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

weight = float(input("Weight (kg): "))
height = float(input("Height (meters): "))
bmi = calculate_bmi(weight, height)
print(f"BMI: {bmi:.2f} — {bmi_category(bmi)}")

#Build a CLI calculator using functions + conditionals
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y    
def multiply(x, y):
    return x * y        
def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y
def calculator():
    print("Welcome to the CLI Calculator!")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    while (choice := input("Enter choice (1/2/3/4/5): ")) != '5':
        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
            pass
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
            pass
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
            pass
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
            pass
        else:
            print("Invalid input. Please select a valid operation.")
            pass
        if choice != '5':
            print("\nSelect another operation or exit:")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Exit")    
    print("Thank you for using the CLI Calculator. Goodbye!")
calculator()