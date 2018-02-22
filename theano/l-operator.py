#!/usr/bin/python
# -*- coding: utf-8 -*-

import theano
import theano.tensor as T

W = T.dmatrix('W')
v = T.dvector('v')
x = T.dvector('x')
y = T.dot(x, W)
VJ = T.Lop(y, W, v)
f = theano.function([v,x], VJ)
print(f([2, 2], [0, 1]))
