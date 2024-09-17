#2. Using input function take two number and then swap the number
# Take input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Swap the numbers
num1, num2 = num2, num1

# Print the swapped numbers
print(f"After swapping: First number = {num1}, Second number = {num2}")

#output
'''Enter the first number: 51
Enter the second number: 45
After swapping: First number = 45, Second number = 51'''
