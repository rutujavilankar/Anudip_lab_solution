# Function to calculate factorial using a while loop
def factorial(number):
    if number < 0:
        return "Factorial is not defined for negative numbers."
    elif number == 0:
        return 1
    else:
        result = 1
        while number > 0:
            result *= number
            number -= 1
        return result

# Get user input
try:
    num = int(input("Enter a number to find its factorial: "))
    
    # Calculate factorial
    fact = factorial(num)
    
    # Display the result
    print(f"The factorial of {num} is: {fact}")

except ValueError:
    print("Invalid input. Please enter a valid integer.")

#output:
    '''Enter a number to find its factorial: 5
The factorial of 5 is: 120'''
