def count_characters(input_string):
    # Initialize counts
    char_count = 0
    digit_count = 0
    symbol_count = 0

    # Iterate over each character in the string
    for char in input_string:
        if char.isalpha():
            char_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            symbol_count += 1

    return char_count, digit_count, symbol_count

# Input string
input_string = "P@#yn26at^&i5ve"

# Get counts
chars, digits, symbols = count_characters(input_string)

# Print the results
print(f"Chars = {chars}")
print(f"Digits = {digits}")
print(f"Symbols = {symbols}")

#output:
'''Chars = 8
Digits = 3
Symbols = 4'''
