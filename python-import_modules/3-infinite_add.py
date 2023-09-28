#!/usr/bin/python3
if __name__ == "__main__":
    import sys

arguments = len(sys.argv)

if arguments == 1:
    print("0")

else:
    result = 0
    for i in range(1, arguments):
        result += int(sys.argv[i])

    print(result)
