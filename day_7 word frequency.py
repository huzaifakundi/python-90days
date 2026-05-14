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