#!/usr/bin/python
# -*- coding: utf-8 -*-

def elimDobles(l):
    if (len(l) == 0):
        return l
    else:
        rest = []
        for i in l:
            if (i != l[0]):
                rest = rest + [i]
    return [l[0]] + elimDobles(rest)

print(elimDobles([1, 2, 2, 1, 3]))
                
