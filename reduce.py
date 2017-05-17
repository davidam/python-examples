#!/usr/bin/python
import functools

print reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])

test = ["1", "2", "3"]
print reduce((lambda x,y: x+y), test, "testing")

def foo(a, b, c):
     return a + b if c else a * b

print reduce(functools.partial(foo, c=True), [1,2,3,4,5], 2)
print reduce(functools.partial(foo, c=False), [1,2,3,4,5], 2)
