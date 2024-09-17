#1. Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.


def divide_numbers():
    try:
        # Prompt the user for two numbers
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))
        
        # Perform the division
        result = numerator / denominator
        
    except ZeroDivisionError:
        # Handle the case where the denominator is zero
        print("Error: You cannot divide by zero.")
        
    except ValueError:
        # Handle the case where the input is not a valid number
        print("Error: Invalid input. Please enter numeric values.")
        
    else:
        # If no exception occurs, print the result
        print(f"The result of {numerator} divided by {denominator} is {result:.2f}")
        
# Call the function to execute the division
divide_numbers()

#output:
'''Enter the numerator: 21
Enter the denominator: 22
The result of 21.0 divided by 22.0 is 0.95'''


