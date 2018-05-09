#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
from io import BytesIO

# Splitting the lines into columns
## The delimiter argument

data = "1, 2, 3\n4, 5, 6"
print(np.genfromtxt(BytesIO(data.encode('utf-8')), delimiter=","))
data = "  1  2  3\n  4  5 67\n890123  4"
print(np.genfromtxt(BytesIO(data.encode('utf-8')), delimiter=3))
data = "123456789\n   4  7 9\n   4567 9"
print(np.genfromtxt(BytesIO(data.encode('utf-8')), delimiter=(4, 3, 2)))

## The autostrip argument

data = "1, abc , 2\n 3, xxx, 4"
# Without autostrip
print(np.genfromtxt(BytesIO(data.encode('utf-8')), delimiter=",", dtype="|U5"))
# With autostrip
print(np.genfromtxt(BytesIO(data.encode('utf-8')), delimiter=",", dtype="|U5", autostrip=True))

## The comments argument
data = """#
 # Skip me !
 # Skip me too !
 1, 2
 3, 4
 5, 6 #This is the third line of the data
 7, 8
 # And here comes the last line
 9, 0
 """

print(np.genfromtxt(BytesIO(data.encode('utf-8')), comments="#", delimiter=","))

data = "\n".join(str(i) for i in range(10))
print(np.genfromtxt(BytesIO(data.encode('utf-8')),))
print(np.genfromtxt(BytesIO(data.encode('utf-8')), skip_header=3, skip_footer=5))

# Skipping lines and choosing columns
## The skip_header and skip_footer arguments

data = "\n".join(str(i) for i in range(10))
print(np.genfromtxt(BytesIO(data.encode('utf-8')),))
print(np.genfromtxt(BytesIO(data.encode('utf-8')), skip_header=3, skip_footer=5))

# usecols

data = "1 2 3\n4 5 6"
print(np.genfromtxt(BytesIO(data.encode('utf-8')), usecols=(0, -1)))

