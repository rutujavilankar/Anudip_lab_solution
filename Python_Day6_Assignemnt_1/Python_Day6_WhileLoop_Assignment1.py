#1.Write a python program to check whether a number is palindrome or not? 
# Function to check if a number is a palindrome
def is_palindrome(number):
    # Convert the number to a string
    num_str = str(number)
    # Check if the string is the same forwards and backwards
    return num_str == num_str[::-1]

# Get user input
try:
    number = int(input("Enter a number: "))

    # Check if the number is a palindrome
    if is_palindrome(number):
        print(f"{number} is a palindrome.")
    else:
        print(f"{number} is not a palindrome.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")

#Output:
    '''Enter a number: 121
121 is a palindrome.'''
