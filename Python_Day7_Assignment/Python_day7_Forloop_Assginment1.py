#1.1.Python program to check if the given string is a palindrome 
def is_palindrome(s):
    # Remove any spaces and convert the string to lowercase
    s = s.replace(" ", "").lower()
    
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Get input from the user
input_string = input("Enter a string to check if it's a palindrome: ")

# Check if the input string is a palindrome and print the result
if is_palindrome(input_string):
    print(f"'{input_string}' is a palindrome.")
else:
    print(f"'{input_string}' is not a palindrome.")

#output:
    '''Enter a string to check if it's a palindrome: Mam
'Mam' is a palindrome.'''

