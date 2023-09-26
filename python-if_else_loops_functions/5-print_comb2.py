#!/usr/bin/python3
for num in range(100):
    if num < 99:
     print(f"{num:02d}, ", end='') #prints 2 digit numbers 
else:
    print(f"{num:02d}")