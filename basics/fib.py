#!/usr/bin/python

def fibo(n):
    if n == 1:
        return[1]
    if n == 2:
        return [1, 1]
    a = 1
    b = 1
    series = [a, b]
    for i in range(n):
        c = a + b
        series.append(c)
        a = b
        b = c

    return series

print(fibo(3))
