#!/usr/bin/python3
""" triangle """


def pascal_triangle(n):
    """Generate Pascal's Triangle of height 'n'."""

    # Check if n is less than or equal to 0
    if n <= 0:
        return []

    # Initialize the Pascal's Triangle with the first row
    triangle = [[1]]

    # Generate the subsequent rows of the triangle
    for i in range(1, n):
        prev_row = triangle[-1]  # Get the previous row
        new_row = [1]  # Initialize the new row with the first element (1)

        # Calculate the values for the new row based on the previous row
        for j in range(1, i):
            new_value = prev_row[j - 1] + prev_row[j]
            new_row.append(new_value)

        new_row.append(1)  # Add the last element (1) to the new row
        triangle.append(new_row)  # Append the new row to the triangle

    return triangle
