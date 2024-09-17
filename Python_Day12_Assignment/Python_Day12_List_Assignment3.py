#3. Write a Python program to find duplicate values from a list and display those
def find_duplicates(lst):
    seen = set()
    duplicates = set()

    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)

    return list(duplicates)

# Example list with duplicates
numbers = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 1]

# Find and display duplicates
duplicates = find_duplicates(numbers)

print("Duplicate values in the list are:", duplicates)

#output:
'''Duplicate values in the list are: [1, 2, 3]'''

