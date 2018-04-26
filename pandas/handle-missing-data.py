#!/usr/bin/python
# -*- coding: utf-8 -*-

from pandas import read_csv
import numpy
dataset = read_csv('pima-indians-diabetes.data.csv', header=None)
print(dataset.describe())
print(dataset.head(20))
print((dataset[[1,2,3,4,5]] == 0).sum())
dataset[[1,2,3,4,5]] = dataset[[1,2,3,4,5]].replace(0, numpy.NaN)
# count the number of NaN values in each column
print(dataset.isnull().sum())

dataset[[1,2,3,4,5]] = dataset[[1,2,3,4,5]].replace(0, numpy.NaN)
# print the first 20 rows of data
print(dataset.head(20))

