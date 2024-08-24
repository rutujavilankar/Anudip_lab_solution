#1. Calculate the multiplication and sum of two numbers
# Function to multiply and sum two numbers
def multiply_and_sum(num1, num2):
    # Multiplying the numbers
    product = num1 * num2
    
    # Adding the numbers
    sum_result = num1 + num2
    
    return product, sum_result

# Example usage
n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))

product, sum_result = multiply_and_sum(n1, n2)

print(f"The product of {n1} and {n2} is: {product}")
print(f"The sum of {n1} and {n2} is: {sum_result}")
