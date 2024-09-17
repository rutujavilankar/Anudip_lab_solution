#1. Write a Python program to sum all the items in a list.
def sum_list_items(lst):
    total_sum = 0
    for item in lst:
        if isinstance(item, (int, float)):
            total_sum += item
        else:
            print(f"Warning: Skipping non-numeric item: {item}")
    return total_sum

# Example list with mixed types
mixed_list = [1, 2, 'three', 4.5, [6], 7]

# Call the function and print the result
result = sum_list_items(mixed_list)
print(f"The sum of numeric items in the list is: {result}")

#output:
'''Warning: Skipping non-numeric item: three
Warning: Skipping non-numeric item: [6]
The sum of numeric items in the list is: 14.5'''
