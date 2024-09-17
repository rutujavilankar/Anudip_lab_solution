#3. Write a Python program to reverse words in a string 

#String = “Deeptech Python Training”


# Given string
string = "Deeptech Python Training"

# Step 1: Split the string into words
words = string.split()

# Step 2: Reverse the list of words
reversed_words = words[::-1]

# Step 3: Join the reversed list into a single string
reversed_string = ' '.join(reversed_words)

print(f"Original string: '{string}'")
print(f"Reversed words string: '{reversed_string}'")

#output:
'''Original string: 'Deeptech Python Training'
Reversed words string: 'Training Python Deeptech'''

