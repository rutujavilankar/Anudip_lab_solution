#2. Write a Python program to remove duplicate characters of a given string.

 #Input = “String and String Function” Output: String and Function

def remove_duplicates(input_string):
    # Initialize an empty set to keep track of seen characters
    seen = set()
    # Initialize an empty list to build the output string
    result = []

    # Split the input string into words
    words = input_string.split()
    
    for word in words:
        # For each word, initialize an empty set for characters
        word_seen = set()
        new_word = []

        # Iterate through each character in the word
        for char in word:
            if char not in word_seen:
                word_seen.add(char)
                new_word.append(char)
        
        # Join the characters back into a word and append to result if it's not already in the result
        unique_word = ''.join(new_word)
        if unique_word not in seen:
            seen.add(unique_word)
            result.append(unique_word)

    # Join the result list into a single string with spaces
    return ' '.join(result)

# Input string
input_string = "String and String Function"

# Remove duplicates and get the result
output_string = remove_duplicates(input_string)

# Print the result
print(output_string)


#output:
'''String and Functio
122Chars = 8
Digits = 3
Symbols = 4'''




