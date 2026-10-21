
import re
paragraph = input()
words = re.findall(r"\b[a-zA-Z']+\b", paragraph.lower())
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

sorted_words = sorted(
    word_count.items(),
    key=lambda item: item[1],
    reverse=True
)

print("\nTop 5 most frequent words:")
for word, count in sorted_words[:5]:
    print(f"{word}: {count}")

# Lists, tuples, dictionaries and sets
numbers = [10, 20, 30, 40, 50]
languages = ("Python", "Java", "SQL")
unique_numbers = {10, 20, 20, 30}
student = {"name": "Sobika", "course": "Python"}

print("List:", numbers)
print("Slicing:", numbers[:3])
print("Tuple:", languages)
print("Set:", unique_numbers)
print("Dictionary:", student)

# Comprehensions
squares = [n * n for n in range(1, 6)]
square_dict = {n: n * n for n in range(1, 6)}
even_set = {n for n in range(1, 11) if n % 2 == 0}

print("Squares:", squares)
print("Square dictionary:", square_dict)
print("Even numbers:", even_set)
