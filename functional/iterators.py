#!/usr/bin/python# -*- coding: utf-8 -*-

L = [1,2,3]
it = iter(L)
it  
print(it.__next__())  # same as next(it)
print(next(it))
print(next(it))
#print(next(it))

L = [1,2,3]
iterator = iter(L)
t = tuple(iterator)
print(t)

L = [1,2,3]
iterator = iter(L)
a,b,c = iterator
a,b,c

