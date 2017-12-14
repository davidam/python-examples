#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://www.scipy-lectures.org/packages/statistics/index.html#multiple-regression-including-multiple-factors

import pandas
from statsmodels.formula.api import ols

data = pandas.read_csv('iris.csv')
model = ols('sepal_width ~ name + petal_length', data).fit()
print(model.summary())

print(model.f_test([0, 1, -1, 0]))
