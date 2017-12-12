#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas
data = pandas.read_csv('brain_size.csv', sep=';', na_values=".")

import scipy as sp                  # Importamos scipy como el alias sp
from scipy import stats

# sample t-test: testing the value of a population mean

print stats.ttest_1samp(data['VIQ'], 0) 

# sample t-test: testing for difference across populations

female_viq = data[data['Gender'] == 'Female']['VIQ']
male_viq = data[data['Gender'] == 'Male']['VIQ']
print stats.ttest_ind(female_viq, male_viq)

# Paired tests: repeated measurements on the same indivuals

print stats.ttest_ind(data['FSIQ'], data['PIQ'])

print stats.ttest_rel(data['FSIQ'], data['PIQ'])

print stats.ttest_1samp(data['FSIQ'] - data['PIQ'], 0)

print stats.wilcoxon(data['FSIQ'], data['PIQ'])
