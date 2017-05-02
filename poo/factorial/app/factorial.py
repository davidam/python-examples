#!/usr/bin/python

class Factorial(object):
    def fac(self, n):
        if ((n == 0) | (n == 1)):
            return 1
        elif (n > 1):
            return n * fac(n - 1)

x = input("Choose a number: ")
f = Factorial()

print f.fac(x)     
