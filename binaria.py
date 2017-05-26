#!/usr/bin/python
# -*- coding: utf-8 -*-

def binaria(x, l):
    maxi = len(l)
    if (maxi > 2):
        pos = maxi / 2
    else:
        pos = 0
    elem = l[pos]
    if (x == elem):
        return True
    elif ((maxi == 1) & (x != elem)):
        return False
    elif (x > elem):
        return binaria(x, l[pos+1:maxi])
    elif (x < elem):
        return binaria(x, l[0:pos])

num = int(raw_input("Escribe un número: "))
l1 = [1, 6, 7, 20, 40, 50]
l2 = [1, 6, 7]
boolean = binaria(num, l1)
if (boolean):
    print "%s está en la lista" % (num)
else:
    print "%s no está en la lista" % (num)
