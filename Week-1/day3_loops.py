# Multiplication Table Generator

def Table(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
print("Welcome to the Multiplication Table Generator!")
number = int(input("Enter a number to see its multiplication table: "))
Table(number)



###########Timer###############
import time
for i in range (10,0,-1):
    print(f"{i} seconds remaining")
    time.sleep(1)
print("Time's up!")