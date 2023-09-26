#!/usr/bin/python3
# Use two loops to generate combinations of two digits
for digit1 in range(0, 9):
    for digit2 in range(digit1 + 1, 10):
        # Print the combination with a comma and space until digit1 gets to 8
         print("{:02d}".format(digit1 * 10 + digit2), end=', ' if digit1 < 8 else '\n')

# Print a newline character to end the output
print()