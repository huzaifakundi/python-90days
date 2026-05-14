name = "Huzaifa Kundi"

print(name[0])        
print(name[-1])       
print(name[0:7])      
print(name[8:13])       
print(name[:7])       
print(name[::2])      
print(name[::-1])     

sentence = "  Hello World Python is Amazing  "
print("hello123".isalpha())      # False — has numbers
print("hello".isalpha())         # True — only letters
print("123".isdigit())           # True — only numbers

# SPLIT — string → list
sentence = "Python is the best language"
words = sentence.split()          # splits by space by default
print(words)                      # ['Python', 'is', 'the', 'best', 'language']

csv_data = "Ali,Ahmed,Sara,Waqas"
names = csv_data.split(",")       # splits by comma
print(names)                      # ['Ali', 'Ahmed', 'Sara', 'Waqas']

# JOIN — list → string
words = ["Python", "is", "awesome"]
sentence = " ".join(words)        # joins with space
print(sentence)                   # Python is awesome

tags = ["ai", "python", "n8n"]
print(", ".join(tags))            # ai, python, n8n
print("-".join(tags))             # ai-python-n8n

