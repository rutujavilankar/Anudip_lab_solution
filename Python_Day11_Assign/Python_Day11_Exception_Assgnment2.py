#2. Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.

def get_integer_from_user():
    while True:
        try:
            # Prompt the user for input
            user_input = input("Please enter an integer: ")
            
            # Attempt to convert the input to an integer
            integer_value = int(user_input)
            
            # If conversion is successful, break out of the loop
            print(f"You entered a valid integer: {integer_value}")
            break
        
        except ValueError:
            # Handle the case where conversion fails
            print("Error: The input is not a valid integer. Please try again.")

# Call the function to prompt the user and handle errors
get_integer_from_user()

#output:
'''Please enter an integer: 23
You entered a valid integer: 23'''

'''Please enter an integer: 2.555
Error: The input is not a valid integer. Please try again.'''


