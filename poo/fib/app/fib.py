#!/usr/bin/python

class Fib(object):
    def fib(self, x):
        if x == 1:
            return[1]
        if x == 2:
            return [1, 1]
        a = 1
        b = 1
        series = [a, b]
        for i in range(x):
            c = a + b
            series.append(c)
            a = b
            b = c
        return series
        
