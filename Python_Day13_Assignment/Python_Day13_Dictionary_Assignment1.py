#1.1. Write a Python program and calculate the mean of the below dictionary.

 #test_dict = {"A" : 6, "B" : 9, "C" : 5, "D" : 7, "E" : 4} 

#Output: 6.2
def calculate_mean(dictionary):
    # Get all the values from the dictionary
    values = dictionary.values()
    
    # Calculate the sum of the values
    total_sum = sum(values)
    
    # Calculate the number of values
    count = len(values)
    
    # Calculate the mean
    mean = total_sum / count
    
    return mean

# Given dictionary
test_dict = {"A": 6, "B": 9, "C": 5, "D": 7, "E": 4}

# Calculate and print the mean
mean_value = calculate_mean(test_dict)
print(f"The mean of the dictionary values is: {mean_value:.1f}")

#output:
'''The mean of the dictionary values is: 6.2'''
