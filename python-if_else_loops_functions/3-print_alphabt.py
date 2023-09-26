#!/usr/bin/python3
for alphbt in range (97, 123):
    if alphbt == 101 or alphbt == 113:
        alphbt=+1
    print('{}'.format(chr(alphbt)), end="")
