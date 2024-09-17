#1.Using input() function take one number from the user and using ternary operators check whether the number is even or odd 

# Take input from the user
number = int(input("Enter a number: "))

# Use a ternary operator to check if the number is even or odd
result = "even" if number % 2 == 0 else "odd"

# Print the result
print(f"The number is {result}.")

#Output
'''Enter a number: 12
The number is even.'''
