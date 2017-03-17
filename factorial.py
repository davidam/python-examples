#!/usr/bin/python

def factorial(n):
    if ((n == 0) | (n == 1)):
        return 1
    elif (n > 1):
        return n * factorial(n - 1)
    
n = input("Choose a number: ")
print factorial(n)    
