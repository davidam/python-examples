#!/usr/bin/python
# -*- coding: utf-8 -*-

l = ['-200', ' 0', ' 200', ' 400', ' green', '0', '0', '200', '400', ' yellow', '200', '0', '200', '400', ' red']

new = []
for i in range(0, len(l), 5):
    new.append(l[i : i+5])
print(new)
