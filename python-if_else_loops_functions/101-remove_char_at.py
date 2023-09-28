#!/usr/bin/python3
def remove_char_at(str, n):
    # prototype that was given
    if n < 0 or n >= len(str):
        # checks if n is less than 0 or more than the amount of letters
        return str
    # Return the original text if n is more than the amount of letters
    result = ""
    # initialize the an empty string
    for i in range(len(str)):
        if i != n:
            # checks if the possition is not equil to n
            result += str[i]
            # adds the letter to the empty string
    return result
# return the results
