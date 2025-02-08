text = "She was happy to see her happy family"

words = text.split()

word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print("Word count dictionary:", word_count)
