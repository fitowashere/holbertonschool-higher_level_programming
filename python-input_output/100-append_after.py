#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text after each line 
    containing a specific string in a file.
    """
    # Check if the file name is empty
    if filename == "":
        return

    # Open the file for reading and writing
    with open(filename, 'r+') as file:
        lines = file.readlines()
        file.seek(0)  # Reset the file pointer to the beginning

        for line in lines:
            file.write(line)  # Write the original line
            if search_string in line:
                file.write(new_string + '\n')  # Insert the new line after matching lines

        file.truncate()  # Truncate any remaining content (if necessary)
