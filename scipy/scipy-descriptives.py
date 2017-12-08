#!/usr/bin/python

import numpy as np
from scipy import stats

np.random.seed(282629734)
x = stats.t.rvs(10, size=1000)

print(x.min())   # equivalent to np.min(x)
print(x.max())   # equivalent to np.max(x)
print(x.mean())  # equivalent to np.mean(x)
print(x.var())   # equivalent to np.var(x))

m, v, s, k = stats.t.stats(10, moments='mvsk')
n, (smin, smax), sm, sv, ss, sk = stats.describe(x)

sstr = '%-14s mean = %6.4f, variance = %6.4f, skew = %6.4f, kurtosis = %6.4f'
print(sstr % ('distribution:', m, v, s ,k))
print(sstr % ('sample:', sm, sv, ss, sk))


