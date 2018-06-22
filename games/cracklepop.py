#!/usr/bin/python

for i in range(1, 101):
    if ((i % 3) == 0) and ((i % 5) == 0): 
        print("cracklepop")
    if (i % 3) == 0: 
        print("crackle")
    elif (i % 5) == 0:
        print("pop")
    elif ((i % 3) != 0) | ((i % 5) != 0):
        print(i)
