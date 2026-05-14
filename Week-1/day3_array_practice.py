# Day 3 - List/Array Practice

fruits = ["apple", "banana", "cherry", "mango"]

# Indexing
print(fruits[0])      # first
print(fruits[-1])     # last

# Slicing
print(fruits[1:3])    # banana, cherry

# Methods
fruits.append("grape")
fruits.remove("apple")
print(fruits)
print(len(fruits))

# Looping through list
for fruit in fruits:
    print(fruit.upper())

# List with numbers
numbers = [5, 2, 8, 1, 9, 3]
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(sorted(numbers))

