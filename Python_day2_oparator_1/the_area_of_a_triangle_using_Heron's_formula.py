import math

# Function to calculate the area of a triangle using Heron's formula
def area_of_triangle(a, b, c):
    # Calculate the semi-perimeter
    s = (a + b + c) / 2
    
    # Calculate the area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    return area

# Get input from the user
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

# Check if the sides form a valid triangle
if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    # Calculate the area
    area = area_of_triangle(side1, side2, side3)
    
    # Print the result
    print(f"The area of the triangle is: {area:.2f}")
else:
    print("The given sides do not form a valid triangle.")
