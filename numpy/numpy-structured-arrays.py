#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2018  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gnu.org>
# Maintainer: David Arroyo Menéndez <davidam@gnu.org>

# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with GNU Emacs; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,
#!/usr/bin/python# -*- coding: utf-8 -*-

import numpy as np

x = np.array([('Rex', 9, 81.0), ('Fido', 3, 27.0)],
             dtype=[('name', 'U10'), ('age', 'i4'), ('weight', 'f4')])

print(x)
print(x[1])
print(x['age'])
x['age'] = 5
print(x)

# Structured Datatype Creation

print(np.dtype([('x', 'f4'), ('y', np.float32), ('z', 'f4', (2,2))]))
print(np.dtype([('x', 'f4'),('', 'i4'),('z', 'i8')]))
print(np.dtype('i8,f4,S3'))
print(np.dtype('3int8, float32, (2,3)float64'))
#print(np.dtype=({'col1': ('i1',0), 'col2': ('f4',1)}))

# Manipulating and Displaying Structured Datatypes

d = np.dtype([('x', 'i8'), ('y', 'f4')])
print(d.names)
print(d.fields)

def print_offsets(d):
     print("offsets:", [d.fields[name][1] for name in d.names])
     print("itemsize:", d.itemsize)
     
print_offsets(np.dtype('u1,u1,i4,u1,i8,u2'))
print_offsets(np.dtype('u1,u1,i4,u1,i8,u2', align=True))

# Field Titles

print(np.dtype([(('my title', 'name'), 'f4')]))
print(np.dtype({'name': ('i4', 0, 'my title')}))

for name in d.names:
    print(d.fields[name][:2])

# Indexing and Assignment to Structured arrays

## Assigning data to a Structured Array

x = np.array([(1,2,3),(4,5,6)], dtype='i8,f4,f8')
x[1] = (7,8,9)
print(x)

## Assignment from Scalars

x = np.zeros(2, dtype='i8,f4,?,S1')
x[:] = 3
print(x)

x[:] = np.arange(2)
print(x)

twofield = np.zeros(2, dtype=[('A', 'i4'), ('B', 'i4')])
onefield = np.zeros(2, dtype=[('A', 'i4')])
nostruct = np.zeros(2, dtype='i4')
# nostruct[:] = twofield
nostruct[:] = onefield
print(nostruct)

## Assignment from other Structured Arrays

a = np.zeros(3, dtype=[('a', 'i8'), ('b', 'f4'), ('c', 'S3')])
b = np.ones(3, dtype=[('x', 'f4'), ('y', 'S3'), ('z', 'O')])
b[:] = a
print(b)

# Indexing Structured Arrays

## Accessing Individual Fields

x = np.array([(1,2),(3,4)], dtype=[('foo', 'i8'), ('bar', 'f4')])
x['foo']
x['foo'] = 10
print(x)

y = x['bar']
y[:] = 10
print(x)

print(y.dtype, y.shape, y.strides)

a = np.zeros(3, dtype=[('a', 'i4'), ('b', 'i4'), ('c', 'f4')])
print(a[['a', 'c']])

# Indexing with an Integer to get a Structured Scalar

x = np.array([(1, 2., 3.)], dtype='i,f,f')
scalar = x[0]
print(scalar)
print(type(scalar))

x = np.array([(1,2),(3,4)], dtype=[('foo', 'i8'), ('bar', 'f4')])
s = x[0]
s['bar'] = 100
print(x)

scalar = np.array([(1, 2., 3.)], dtype='i,f,f')[0]
scalar[0]
scalar[1] = 4

# Record Arrays

recordarr = np.rec.array([(1,2.,'Hello'),(2,3.,"World")],
                    dtype=[('foo', 'i4'),('bar', 'f4'), ('baz', 'S10')])

print(recordarr.bar)
print(recordarr[1:2])
print(recordarr[1:2].foo)
print(recordarr.foo[1:2])
print(recordarr[1].baz)
