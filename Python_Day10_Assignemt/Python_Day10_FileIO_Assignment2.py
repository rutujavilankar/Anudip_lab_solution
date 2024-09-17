#1. Write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen.
#created on ABC.txt file

def count_words_in_file(filename):
    total_words = 0
    
    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            # Iterate over each line in the file
            for line in file:
                # Split the line into words and count them
                words = line.split()
                total_words += len(words)
        
        # Display the total number of words
        print(f"Total number of words in the file '{filename}': {total_words}")

    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
    except IOError:
        print(f"Error: Could not read the file {filename}.")

# Example usage
count_words_in_file("ABC.txt")

#output
'''Total number of words in the file 'ABC.txt': 22'''

