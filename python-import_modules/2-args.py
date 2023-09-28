#!/usr/bin/python3
if __name__ == "__main__":
    import sys

arguments = sys.argv[1:] #argv
num_arguments = len(arguments) #argc

#print(num_arguments, "argument(s):", end="")
if num_arguments >= 1:
    print(num_arguments, " argument:", end="")
if num_arguments == 0:
    print(num_arguments, "argument.", end="\n\n")
else:
    print("")

for i in range(0, num_arguments):
   print("{}: {}".format(i+1, arguments[i]))