"""
employees = {
    "emp1": {
        "name": "Ali",
        "age": 22,
        "skills": ["Python", "AI", "n8n"]
    },
    "emp2": {
        "name": "Ahmed",
        "age": 25,
        "skills": ["JavaScript", "React"]
    }
}

# Access nested data
print(employees["emp1"]["name"])        # Ali
print(employees["emp2"]["skills"][0])   # JavaScript

# Loop through nested dict
for emp_id, info in employees.items():
    print(f"\n{emp_id}:")
    print(f"  Name: {info['name']}")
    print(f"  Age: {info['age']}")
    
    
    ##########set##########
    # Raw data with duplicates
visitors = ["Ali", "Ahmed", "Ali", "Sara", "Ahmed", "Ali"]

# Instant deduplication
unique_visitors = set(visitors)
print(f"Total visits: {len(visitors)}")
print(f"Unique visitors: {len(unique_visitors)}")
print(unique_visitors)
"""

"""
####### Task 1: Create a dictionary for a person with keys like name, age, city, degree, and gpa. Then print out the person's information in a formatted string.
Person = {
    "p1": {
        "name": "Huzaifa",
        "age": 24,
        "city": "Chashma",
        "degree": "CS",
        "gpa":3.3,       
    }
}
print (Person["p1"].keys())
print (Person["p1"].values())
print (f"My name is {Person['p1']['name']} and I am {Person['p1']['age']} years old. I live in {Person['p1']['city']} and I have a degree in {Person['p1']['degree']} with a GPA of {Person['p1']['gpa']}.")
"""
######
""" Task 2: Create a dictionary for a student with keys like id, name, and marks. Then write a loop to check if the student has passed or failed based on their marks (pass mark is 50).    

Student ={
    "s1": {
        "id" : "002",
        "name" : "St 1",
        "marks" : 53, 
    },
    "s2": {
        "id" : "002",
        "name" : "St 2",
        "marks" : 48, 
    },
    "s3": {
        "id" : "003",
        "name" : "St 3",
        "marks" : 84, 
    }
}


###for student_id, info in Student.items():
   ### status = "Pass ✅" if info['marks'] >= 50 else "Fail ❌"
    ###print(f"\n{student_id}: {info['name']} | Marks: {info['marks']} | {status}")

for student_id, info in Student.items():
    print(f"\n{student_id}:")
    print(f"  Name: {info['name']}")
    if info['marks'] >= 50:
        print("  Status: Pass")
    else:
        print("  Status: Fail")
   """   
  
############### Task` 3: Create a set of unique programming languages from a list that contains duplicates. Then add a new language to the set and check if a specific language is in the set.  

"""

tags = ["python", "ai", "python", "automation", 
        "ai", "python", "n8n", "automation"]

unique_tags=set(tags)
print(unique_tags,end=" ")
print(len(unique_tags))
unique_tags.add("langchain")
print(unique_tags,end=" ")
print(len(unique_tags))
if "n8n" in unique_tags:
    print("n8n is in the set of unique tags.")
    """

################## Task 4: Create a dictionary of contacts with names as keys and phone numbers as values. Then write a loop to allow the user to search for a contact's phone number by name. If the name is not found, print a message saying so.

contacts = {
     
        "Ali": "03123456789",
        "Ahmed": "03234567890",
        "Sara": "03345678901",
        "Waqas": "03456789012"
}
while (search := input("Enter a name to search for their contact number (or 'exit' to quit): ")) != "exit":
#search= input("Enter a name to search for their contact number: ")
    if search in contacts:
        print(f"{search}'s contact number is: {contacts[search]}")
    else:    print(f"{search} is not in the contacts list.")