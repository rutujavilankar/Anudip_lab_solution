#2. Write a Python program to remove a newline in Python

 #String = "\nBest \nDeeptech \nPython \nTraining\n"

# Given string with newlines
string = "\nBest \nDeeptech \nPython \nTraining\n"

# Remove newline characters
cleaned_string = string.replace('\n', '')

# Optionally, strip any leading or trailing whitespace
cleaned_string = cleaned_string.strip()

print(f"Original string:\n{string}")
print(f"Cleaned string:\n{cleaned_string}")

#output:
'''Original string:

Best 
Deeptech 
Python 
Training

Cleaned string:
Best Deeptech Python Training'''

