#!/usr/bin/python3
if __name__ == "__main__":
    import sys

arguments = sys.argv[1:]#argv
num_arguments = len(arguments)#argc

if num_arguments >= 1:
    print(num_arguments, "arguments:", end="")
if num_arguments == 0:
    print(num_arguments, "argument.", end="\n")
else:
    print("")

for i in range(0, num_arguments):
    print("{}: {}".format(i+1, arguments[i]))
