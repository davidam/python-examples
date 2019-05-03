#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scipy as sp                  # Importamos scipy como el alias sp
#import scipy.stats
from scipy import stats

x = stats.t.rvs(10, size=1000)
print(x)
print('normal skewtest teststat = %6.3f pvalue = %6.4f' % stats.skewtest(x))

print('normal kurtosistest teststat = %6.3f pvalue = %6.4f' % stats.kurtosistest(x))

print('normaltest teststat = %6.3f pvalue = %6.4f' % stats.normaltest(x))

print('normaltest teststat = %6.3f pvalue = %6.4f' % stats.normaltest((x-x.mean())/x.std()))

print('normaltest teststat = %6.3f pvalue = %6.4f' % stats.normaltest(stats.t.rvs(10, size=100)))

print('normaltest teststat = %6.3f pvalue = %6.4f' % stats.normaltest(stats.norm.rvs(size=1000)))

