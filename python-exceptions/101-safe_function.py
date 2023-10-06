#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        # Call the given function with the provided arguments
        result = fct(*args)
        return result
    except Exception as e:
        # Print the exception message to stderr
        print("Exception: {}".format(e), file=sys.stderr)
        return None
    