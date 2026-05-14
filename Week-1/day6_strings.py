# =============================================
# DAY 6 — Strings Deep Dive
# =============================================


name = "Huzaifa Kundi"

# Slicing
print(name[0:7])        # Huzaifa
print(name[-5:])        # Kundi
print(name[::-1])       # reversed

# String methods
print(name.upper())
print(name.lower())
print(name.replace("Kundi", "Ahmed"))
print(len(name))
print(name.find("Kundi"))

# Split and Join
sentence = "Python is the best language"
words = sentence.split()
print(words)
print(" ".join(words))

csv = "Ali,Ahmed,Sara,Waqas"
names = csv.split(",")
print(names)
print(" - ".join(names))

# Word Counter
sentence = input("Enter a sentence: ").lower().strip()
words = sentence.split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(f"\nTotal words: {sum(word_count.values())}")
print(f"Unique words: {len(word_count)}")

top_word = max(word_count, key=word_count.get)
print(f"Most used: '{top_word}' ({word_count[top_word]} times)")

for word, count in sorted(word_count.items(), 
                          key=lambda x: x[1], reverse=True):
    print(f"  {word:<15} : {'⭐' * count} ({count})")
    
    
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

#                       Word Frequency Counter

def count_words(sentence):
    sentence = sentence.lower().strip()
    words = sentence.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

def most_frequent(word_count):
    top_word = max(word_count, key=word_count.get)
    return top_word, word_count[top_word]

sentence = input("Enter a sentence: ")
result = count_words(sentence)

print(f"\nTotal words: {sum(result.values())}")
print(f"Unique words: {len(result)}")

top, count = most_frequent(result)
print(f"Most used word: '{top}' ({count} times)")

print("\nAll frequencies:")
for word, count in sorted(result.items(), key=lambda x: x[1], reverse=True):
    print(f"  {word:<15} : {'⭐' * count} ({count})")