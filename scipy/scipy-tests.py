#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scipy as sp                  # Importamos scipy como el alias sp
#import scipy.stats
from scipy import stats
# We can use the t-test to test whether the mean of our sample differs in a statistically significant way from the theoretical expectation.
m, v, s, k = stats.t.stats(10, moments='mvsk')
x = stats.t.rvs(10, size=1000)
print('t-statistic = %6.6f pvalue = %6.4f' %  sp.stats.ttest_1samp(x, m))
# The pvalue is 0.7, this means that with an alpha error of, for example, 10%, we cannot reject the hypothesis that the sample mean is equal to zero, the expectation of the standard t-distribution.

# The Kolmogorov-Smirnov test can be used to test the hypothesis that the sample comes from the standard t-distribution


print('KS-statistic D = %6.3f pvalue = %6.4f' % stats.kstest(x, 't', (10,)))

# Again the p-value is high enough that we cannot reject the hypothesis that the random sample really is distributed according to the t-distribution.
