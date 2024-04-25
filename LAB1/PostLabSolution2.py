""" Write a program that allows the user to navigate through the lines of text in a file. 
The program prompts the user for a filename and inputs the lines of text into a list. 
The program then enters a loop in which it prints the number of lines in the file and prompts the user for a line number. 
Actual line numbers range from 1 to the number of lines in the file. 
If the input is 0, the program quits. Otherwise, 
the program prints the line associated with that number.  """

def navigate_file_lines():
    # Prompt the user for a filename
    filename = input("Enter a filename: ")

    # Open the file and read the lines into a list
    with open(filename, 'r') as file:
        lines = file.readlines()

    while True:
        # Print the number of lines in the file
        print(f"The file has {len(lines)} lines.")

        # Prompt the user for a line number
        line_number = int(input("Enter a line number (or 0 to quit): "))

        # If the input is 0, quit the program
        if line_number == 0:
            break

        # Otherwise, print the line associated with that number
        else:
            print(lines[line_number - 1])

# Call the function
navigate_file_lines()
