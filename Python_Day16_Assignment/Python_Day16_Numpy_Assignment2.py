import numpy as np

# Input list
my_list = [1, 2, 3, 4, 5]

# Convert the list to a NumPy array
my_array = np.array(my_list)

# Display the array
print("Array:", my_array)

# Display the first and last index values
print("First element:", my_array[0])
print("Last element:", my_array[-1])

# Multiply each element by 2 and display the result
multiplied_array = my_array * 2
print("Array multiplied by 2:", multiplied_array)

#output:
'''Array: [1 2 3 4 5]
First element: 1
Last element: 5
Array multiplied by 2: [ 2  4  6  8 10]'''
