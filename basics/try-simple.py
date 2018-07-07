#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import signal

nombre = str(input("Indica el nombre del archivo: "))

try:
    fichero = open(nombre, "r+")
except FileNotFoundError:
    print("The program has not found the file, it stops.")
    os.kill(os.getpid(), signal.SIGUSR1)

print("The program has found the file, it continues.")

a = [1, 2, 3]
# a[0] = str(input("Give me an element for my array: "))
# a[1] = str(input("Give me another element for my array: "))
# a[2] = str(input("Give me the last element for my array: "))

try:
    print("Second element = %d" %(a[1]))
    # Throws error since there are only 3 elements in array
    print("Third element = %d" %(a[2]))
except IndexError:
    print("Your array has not the index")
    os.kill(os.getpid(), signal.SIGUSR1)


print("The program don't have a trouble with the array indexes")

# Program to handle multiple errors with one except statement
try :
    a = int(input("Give me an integer: "))
    b = int(input("Give me another integer: "))
    # throws ZeroDivisionError for a = 3
    c = a/b
    # throws NameError if a >= 4
    print("Value of c = %s" % c)
# note that braces () are necessary here for multiple exceptions
except(ZeroDivisionError, NameError):
    print("\nDividing % by %s has troubles with the zero division" % (a, b))
    os.kill(os.getpid(), signal.SIGUSR1)

print("The program has not troubles with the zero division")
