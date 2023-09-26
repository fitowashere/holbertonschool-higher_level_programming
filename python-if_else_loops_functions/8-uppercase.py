#!/usr/bin/python3
def uppercase(input_str):
    for i in input_str:
        if ord(i) >= 97 and ord(i) <= 122:
            i = chr(ord(i) - 32)
        print("{}".format(i), end="")
    print("")