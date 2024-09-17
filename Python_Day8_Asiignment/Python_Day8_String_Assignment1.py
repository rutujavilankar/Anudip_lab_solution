import string

# Given string
sentence = "To change the overall look of your document. To change the look available in the gallery"

# Convert the string to lowercase
sentence = sentence.lower()

# Remove punctuation from the string
sentence = sentence.translate(str.maketrans('', '', string.punctuation))

# Split the sentence into words
words = sentence.split()

# Create a dictionary to count occurrences of each word
word_count = {}

# Count each word's occurrences
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Print the word counts
for word, count in word_count.items():
    print(f"'{word}': {count}")

#output:
''''to': 2
'change': 2
'the': 3
'overall': 1
'look': 2
'of': 1
'your': 1
'document': 1
'available': 1
'in': 1
'gallery': 1'''
