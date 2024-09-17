#1.Write a Python program to get the largest and smallest number from a list without builtin functions.

def find_largest_and_smallest(numbers):
    if not numbers:
        # Handle the case where the list is empty
        print("The list is empty.")
        return None, None

    # Initialize the first element as both largest and smallest
    largest = smallest = numbers[0]

    # Iterate through the list
    for num in numbers:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num

    return largest, smallest

# Example list of numbers
numbers = [34, 7, 23, -5, 90, 12, 0, -1]

# Call the function and get the result
largest, smallest = find_largest_and_smallest(numbers)

# Print the results
print(f"The largest number in the list is: {largest}")
print(f"The smallest number in the list is: {smallest}")

#output:
'''The largest number in the list is: 90
The smallest number in the list is: -5'''
