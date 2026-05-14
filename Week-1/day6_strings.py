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