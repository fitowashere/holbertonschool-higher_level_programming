#!/usr/bin/python3
if __name__ == "__main__":
    import sys

arguments = sys.argv[1:]
num_arguments = len(arguments)

if num_arguments == 1:
    print(num_arguments, "argument:", end="")
if num_arguments > 1:
    print(num_arguments, "arguments:", end="")
if num_arguments == 0:
    print(num_arguments, "arguments.", end="\n")
else:
    print("")

for i in range(num_arguments):
    print("{}: {}".format(i+1, arguments[i]))
