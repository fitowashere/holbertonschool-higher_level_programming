#!/usr/bin/python3
for decimal in range(0, 100):
    if decimal == 99:
        print("{}".format(decimal))
        break
    print("{:02d}, ".format(decimal), end="")
