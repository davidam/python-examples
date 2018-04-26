#!/usr/bin/python
# -*- coding: utf-8 -*-

from pandas import read_csv
import numpy
dataset = read_csv('pima-indians-diabetes.data.csv', header=None)
# mark zero values as missing or NaN
print("Before remove")
print(dataset.shape)
dataset[[1,2,3,4,5]] = dataset[[1,2,3,4,5]].replace(0, numpy.NaN)
# drop rows with missing values
dataset.dropna(inplace=True)
# summarize the number of rows and columns in the dataset
print("After remove")
print(dataset.shape)
