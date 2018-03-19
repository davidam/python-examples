#!/usr/bin/python# -*- coding: utf-8 -*-

def generate_ints(N):
    for i in range(N):
        yield i

gen = generate_ints(3)
print(next(gen))
print(next(gen))
#print(next(gen))
#print(next(gen))

def counter(maximum):
    i = 0
    while i < maximum:
        val = (yield i)
        # If value provided, change counter
        if val is not None:
            i = val
        else:
            i += 1

it = counter(10)  
print(next(it))
print(next(it))
it.send(8)  
print(next(it))
#print(next(it))
