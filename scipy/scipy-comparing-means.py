#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scipy as sp                  # Importamos scipy como el alias sp
#import scipy.stats
from scipy import stats

rvs1 = stats.norm.rvs(loc=5, scale=10, size=500)
print(rvs1)
rvs2 = stats.norm.rvs(loc=5, scale=10, size=500)

txt1 = stats.ttest_ind(rvs1, rvs2) # estadístico y p-valor
print(txt1)
#print stats.ttest_ind(rvs1, rvs2) # estadístico y p-valor

rvs3 = stats.norm.rvs(loc=8, scale=10, size=500)
print(stats.ttest_ind(rvs1, rvs3)) # estadístico y p-valor

# For the example where both samples are drawn from the same distribution, we cannot reject the null hypothesis since the pvalue is high
print(stats.ks_2samp(rvs1, rvs2))

# In the second example, with different location, i.e. means, we can reject the null hypothesis since the pvalue is below 1%
print(stats.ks_2samp(rvs1, rvs3))
