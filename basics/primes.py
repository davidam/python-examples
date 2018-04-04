#!/usr/bin/python

def divisible(x, y):
    return (0 == (x % y))

def generaLista(x, y):
    if (x == y):
        return [y]
    else:
        return [x] + generaLista(x+1, y)

def divisores(x):
    l = generaLista(1, x)
    laux = []
    for i in l:
        if (0 == (x % i)):
            laux = laux + [i]
    return laux

def primos(x):
    l = generaLista(1, x)
    laux = []
    for i in l:
        d = divisores(i)
        if ((len(d) == 2) or (i == 1)):
            laux = laux + [i]
    return laux


x = int(input("Give me a number: "))
print("generaLista(1, 5) %s: " % generaLista(1, 5))
print("The primes list until %s is: %s" % (x, primos(x)))
