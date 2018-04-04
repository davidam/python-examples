#!/usr/bin/python
import profile

def factorial(n):
    if ((n == 0) | (n == 1)):
        return 1
    elif (n > 1):
        return n * factorial(n - 1)

print("RAW")
profile.run('factorial(4)')
    
