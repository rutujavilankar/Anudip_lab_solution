import random

# Generate 5 random numbers
numbers = [random.randint(1, 100) for _ in range(5)]

# Find the maximum and minimum values
max_value = max(numbers)
min_value = min(numbers)

# Display the results
print("Random numbers:", numbers)
print("Maximum value:", max_value)
print("Minimum value:", min_value)

#output
'''Random numbers: [64, 67, 77, 29, 17]
Maximum value: 77
Minimum value: 17'''

