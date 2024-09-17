#3.Write a Python program that determines if a given year is a leap year or not.
# Get input from the user
year = int(input("Enter a year: "))

# Determine if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

#output
    '''Enter a year: 2021
2021 is not a leap year.'''
