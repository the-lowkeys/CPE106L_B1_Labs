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
