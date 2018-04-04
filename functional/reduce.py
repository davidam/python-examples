#!/usr/bin/python
from functools import reduce
from functools import partial

f = lambda a,b: a if (a > b) else b
print("REDUCE EXAMPLES")
print("a if (a > b) else b")
print(reduce(f, [47,11,42,102,13]))
print("x+y, range(1,101)")
print(reduce(lambda x, y: x+y, range(1,101)))
print("x*y, range(1,49)")
print(reduce(lambda x, y: x*y, range(1,49)))
print(reduce(lambda x, y: x*y, range(44,50))/reduce(lambda x, y: x*y, range(1,7)))

def foo(a, b, c):
     return a + b if c else a * b

print(reduce(partial(foo, c=True), [1,2,3,4,5], 2))
print(reduce(partial(foo, c=False), [1,2,3,4,5], 2))
