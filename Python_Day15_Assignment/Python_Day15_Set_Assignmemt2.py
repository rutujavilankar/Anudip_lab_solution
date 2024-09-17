#2. Write a Python program to Return a set of elements present in Set A or B, but not both.

#Input: set1 = {10, 20, 30, 40, 50} set2 = {30, 40, 50, 60, 70} 

#Output: {20, 70, 10, 60}

# Define the sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Find the symmetric difference of both sets
unique_elements = set1 ^ set2

# Print the result
print(unique_elements)

#output:
'''{20, 70, 10, 60}'''
