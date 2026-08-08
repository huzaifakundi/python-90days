# =============================================
# WEEK 2 DAY 8 — File I/O
# =============================================

# WRITE to a file
with open("students.txt", "w") as file:
    file.write("Huzaifa\n")
    file.write("Sami\n")
    file.write("Ali\n")
    file.write("Ahmed\n")

print("✅ File written successfully!")

# READ whole file at once
with open("students.txt", "r") as file:
    content = file.read()
    print(content)

# READ line by line — numbered
with open("students.txt", "r") as file:
    lines = file.readlines()
    print(f"Total students: {len(lines)}")
    for i, line in enumerate(lines, 1):
        print(f"{i}. {line.strip()}")
        
# APPEND — adds without deleting existing content
with open("students.txt", "a") as file:
    file.write("Sara\n")
    file.write("Waqas\n")

print("✅ New students added!")

# Verify — read the full updated file
with open("students.txt", "r") as file:
    lines = file.readlines()
    print(f"\nUpdated list ({len(lines)} students):")
    for i, line in enumerate(lines, 1):
        print(f"{i}. {line.strip()}")
        
# Write from a list — real world pattern
skills = ["Python", "AI", "Automation", "n8n", "LangChain"]

with open("skills.txt", "w") as file:
    for skill in skills:
        file.write(skill + "\n")

print("✅ Skills saved!")

# Read back
with open("skills.txt", "r") as file:
    lines = file.readlines()
    print("\n📋 My Skills:")
    for i, line in enumerate(lines, 1):
        print(f"{i}. {line.strip()}")
    print(f"\nTotal: {len(lines)} skills")

#challenge: 1. Create a file called "my_goals.txt"
#2. Write these 5 goals to it:
#  - Learn Python
#  - Build AI projects
#  - Get freelance clients
#  - Earn in dollars
#  - Be an AI Engineer
#3. Read it back and print like:
#   🎯 My 90-Day Goals:
#   1. Learn Python
#   2. Build AI projects
#   3. Get freelance clients
#4. Append 2 more goals of your choice
#5. Read the final file and print:

#   🎯 My 90-Day Goals:
#write the goals to a file
with open("my_goals.txt", "w") as file:
    file.write("Learn Python\n")
    file.write("Build AI projects\n")
    file.write("Get freelance clients\n")
    file.write("Earn in dollars\n")
    file.write("Be an AI Engineer\n")
print("✅ Goals written successfully!")

#read the goals back and print
with open("my_goals.txt", "r") as file:
    lines = file.readlines()
    print("\n🎯 My 90-Day Goals:")
    for i, line in enumerate(lines, 1):
        print(f"{i}. {line.strip()}")

#append 2 more goals
with open("my_goals.txt", "a") as file:
    file.write("Contribute to open source\n")
    file.write("Build a personal brand\n") 

#read the final file and print
with open("my_goals.txt", "r") as file:
    lines = file.readlines()
    print("\n🎯 My 90-Day Goals:")
    for i, line in enumerate(lines, 1):
        print(f"{i}. {line.strip()}")
    print(f"\nTotal goals: {len(lines)}")