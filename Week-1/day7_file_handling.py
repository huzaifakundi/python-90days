# =============================================
# WEEK 1 DAY 7 — File I/O
# =============================================

# WRITE to a file


with open('G:\\AI Engineer Course\\Week-2\\myfile.txt', 'w') as file:
    file.write("Huzaifa\n")
    file.write("Sami\n")
    file.write("Ali\n")

print("File written successfully.")

# READ entire file

with open('G:\\AI Engineer Course\\Week-2\\myfile.txt', 'r') as file:
    content = file.read()
print("File content:")
print(content)

# APPEND — add without deleting existing content
with open("G:\\AI Engineer Course\\Week-2\\myfile.txt", "a") as file:
    file.write("Sara\n")
    file.write("Waqas\n")

print("New students added!")

# Verify
with open("G:\\AI Engineer Course\\Week-2\\myfile.txt", "r") as file:
    print(file.read())
    
# Write student names then read them back
students = ["Huzaifa", "Sami", "Ali", "Ahmed", "Sara"]

# Write all at once
with open("G:\\AI Engineer Course\\Week-2\\class_list.txt", "w") as file:
    for student in students:
        file.write(student + "\n")

print("Class list saved!")

# Read back
print("\n--- Class List ---")
with open("G:\\AI Engineer Course\\Week-2\\class_list.txt", "r") as file:
    for i, line in enumerate(file, 1):
        print(f"{i}. {line.strip()}")
        
        
#Challenge:

with open("G:\\AI Engineer Course\\Week-2\\myskills.txt", "w") as file:
    file.write("Python\n")
    file.write("AI\n")
    file.write("Automation\n")
    file.write("Cloud Computing\n")
    file.write("Cybersecurity\n")
    
print("Skills saved!")

with open("G:\\AI Engineer Course\\Week-2\\myskills.txt", "r") as file:
    print("My Skills:")
    for i, line in enumerate(file, 1):
        print(f"{i}. {line.strip()}") 
print("Skills read successfully!")

with open("G:\\AI Engineer Course\\Week-2\\myskills.txt", "a") as file:
    file.write("Data Science\n")
    file.write("Machine Learning\n")
print("New skills added!")

with open("G:\\AI Engineer Course\\Week-2\\myskills.txt", "r") as file:
    print("\nUpdated Skills:")
    for i, line in enumerate(file, 1):
        print(f"{i}. {line.strip()}")
    #print number of skills
    file.seek(0)  # Move back to the beginning of the file
    print(f"\nTotal skills: {len(file.readlines())}")
print("Skills read successfully!")