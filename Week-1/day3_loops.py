# Multiplication Table Generator
"""
def Table(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
print("Welcome to the Multiplication Table Generator!")
number = int(input("Enter a number to see its multiplication table: "))
Table(number)
"""
"""

#BMI Calculator
def calculate_bmi(weight, height):
    bmi = (weight*703) / (height ** 2)
    return bmi
def prt(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"
print("Welcome to the BMI Calculator!")
weight = float(input("Enter your weight in kilograms: "))     
height = float(input("Enter your height in feets: "))
bmi = calculate_bmi(weight, height)
print(f"Your BMI is: {bmi:.2f}")
print(f"Your weight category is: {prt(bmi)}")
"""
"""
class Person:
    def __init__(self,Name,Age):
        self.name =  Name
        self.age = Age
    def greet(self):
        print(f"Hello, my name is {self.name}")
p1 = Person("John", 30)
p1.greet()
"""