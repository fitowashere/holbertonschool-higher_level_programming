#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

def handle_operation(a, operator, b):
    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = sub(a, b)
    elif operator == '*':
        result = mul(a, b)
    elif operator == '/':
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print("{} {} {} = {}".format(a, operator, b, result))

# Get the command-line arguments
arguments = sys.argv[1:]

# Check if the number of arguments is 3
if len(arguments) != 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)

# Extract the arguments
a = int(arguments[0])
operator = arguments[1]
b = int(arguments[2])

# Handle the operation
handle_operation(a, operator, b)