#!/usr/bin/python
# -*- coding: utf-8 -*-

import theano as th
import theano.tensor as T
import numpy as np
from pprint import pprint

ninputs = 1000
nfeatures = 100
noutputs = 10
nhiddens = 50

rng = np.random.RandomState(0)
x = T.dmatrix('x')
wh = th.shared(rng.normal(0, 1, (nfeatures, nhiddens)), borrow=True)
bh = th.shared(np.zeros(nhiddens), borrow=True)
h = T.nnet.sigmoid(T.dot(x, wh) + bh)

wy = th.shared(rng.normal(0, 1, (nhiddens, noutputs)))
by = th.shared(np.zeros(noutputs), borrow=True)
y = T.nnet.softmax(T.dot(h, wy) + by)

predict = th.function([x], y)
pprint(predict)

from theano.printing import pydotprint
import os

if not os.path.exists('examples'):
    os.makedirs('examples')
pydotprint(predict, 'examples/mlp.png')

import theano.d3viz as d3v
d3v.d3viz(predict, 'examples/mlp.html')
