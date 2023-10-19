#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


class MyList(list):
    """Implements sorted printing for the built-in list class."""
    def print_sorted(self):
        """Print a list in sorted ascending order."""
        int_items = [item for item in self if isinstance(item, int)]
        non_int_items = [item for item in self if not isinstance(item, int)]
        
        if non_int_items:
            print("Removed non-integer items:", non_int_items)
            for item in non_int_items:
                self.remove(item)
            
        sorted_list = sorted(int_items)
        print(sorted_list)