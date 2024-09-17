#1. Write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen.

#I have created ABC.txt created one file

def read_and_display_file(filename):
    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            # Iterate over each line in the file
            for line in file:
                # Print the line to the screen
                print(line, end='')  # 'end' parameter avoids adding an extra newline

    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
    except IOError:
        print(f"Error: Could not read the file {filename}.")
        

# Example usage
read_and_display_file("ABC.txt")


#output
'''The next line, size = len(f1.read()) , reads the entire contents of the file 'ABC.txt', returning a string containing the file's contents. '''
