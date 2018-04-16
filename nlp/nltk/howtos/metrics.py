#!/usr/bin/python
# -*- coding: utf-8 -*-

# metrics package provides a variety of evaluation measures

from __future__ import print_function
from nltk.metrics import *

reference = 'DET NN VB DET JJ NN NN IN DET NN'.split()
test    = 'DET VB VB DET NN NN NN IN DET NN'.split()
print(accuracy(reference, test))

reference_set = set(reference)
test_set = set(test)
precision(reference_set, test_set)
print(recall(reference_set, test_set))
print(f_measure(reference_set, test_set))

from nltk import FreqDist, MLEProbDist
pdist1 = MLEProbDist(FreqDist("aldjfalskfjaldsf"))
pdist2 = MLEProbDist(FreqDist("aldjfalssjjlldss"))
print(log_likelihood(['a', 'd'], [pdist1, pdist2]))

edit_distance("rain", "shine")

s1 = set([1,2,3,4])
s2 = set([3,4,5])
binary_distance(s1, s2)
print(jaccard_distance(s1, s2))
print(masi_distance(s1, s2))

spearman_correlation({'e':1, 't':2, 'a':3}, {'e':1, 'a':2, 't':3})

s1 = "000100000010"
s2 = "000010000100"
s3 = "100000010000"
s4 = "000000000000"
s5 = "111111111111"
windowdiff(s1, s1, 3)

abs(windowdiff(s1, s2, 3) - 0.3)  < 1e-6  # windowdiff(s1, s2, 3) == 0.3
abs(windowdiff(s2, s3, 3) - 0.8)  < 1e-6  # windowdiff(s2, s3, 3) == 0.8
windowdiff(s1, s4, 3)
windowdiff(s1, s5, 3)

# Confusion Matrix

reference = 'This is the reference data.  Testing 123.  aoaeoeoe'
test =      'Thos iz_the rifirenci data.  Testeng 123.  aoaeoeoe'
print(ConfusionMatrix(reference, test))

cm = ConfusionMatrix(reference, test)
print(cm.pretty_format(sort_by_count=True))

print(cm.pretty_format(sort_by_count=True, truncate=10))

print(cm.pretty_format(sort_by_count=True, truncate=10, values_in_chart=False))

# Association Measures

n_new_companies, n_new, n_companies, N = 8, 15828, 4675, 14307668
bam = BigramAssocMeasures
bam.raw_freq(20, (42, 20), N) == 20. / N
bam.student_t(n_new_companies, (n_new, n_companies), N)
bam.chi_sq(n_new_companies, (n_new, n_companies), N)
bam.likelihood_ratio(150, (12593, 932), N)

bam.mi_like(20, (42, 20), N) > bam.mi_like(20, (41, 27), N)
bam.pmi(20, (42, 20), N) > bam.pmi(20, (41, 27), N)
bam.phi_sq(20, (42, 20), N) > bam.phi_sq(20, (41, 27), N)
bam.poisson_stirling(20, (42, 20), N) > bam.poisson_stirling(20, (41, 27), N)
bam.jaccard(20, (42, 20), N) > bam.jaccard(20, (41, 27), N)
bam.dice(20, (42, 20), N) > bam.dice(20, (41, 27), N)
bam.fisher(20, (42, 20), N) > bam.fisher(20, (41, 27), N)

n_w1_w2_w3 = 20
n_w1_w2, n_w1_w3, n_w2_w3 = 35, 60, 40
pair_counts = (n_w1_w2, n_w1_w3, n_w2_w3)
n_w1, n_w2, n_w3 = 100, 200, 300
uni_counts = (n_w1, n_w2, n_w3)
N = 14307668
tam = TrigramAssocMeasures
tam.raw_freq(n_w1_w2_w3, pair_counts, uni_counts, N) == 1. * n_w1_w2_w3 / N
uni_counts2 = (n_w1, n_w2, 100)
tam.student_t(n_w1_w2_w3, pair_counts, uni_counts2, N) > tam.student_t(n_w1_w2_w3, pair_counts, uni_counts, N)
tam.chi_sq(n_w1_w2_w3, pair_counts, uni_counts2, N) > tam.chi_sq(n_w1_w2_w3, pair_counts, uni_counts, N)
tam.mi_like(n_w1_w2_w3, pair_counts, uni_counts2, N) > tam.mi_like(n_w1_w2_w3, pair_counts, uni_counts, N)
tam.pmi(n_w1_w2_w3, pair_counts, uni_counts2, N) > tam.pmi(n_w1_w2_w3, pair_counts, uni_counts, N)
tam.likelihood_ratio(n_w1_w2_w3, pair_counts, uni_counts2, N) > tam.likelihood_ratio(n_w1_w2_w3, pair_counts, uni_counts, N)
tam.poisson_stirling(n_w1_w2_w3, pair_counts, uni_counts2, N) > tam.poisson_stirling(n_w1_w2_w3, pair_counts, uni_counts, N)
tam.jaccard(n_w1_w2_w3, pair_counts, uni_counts2, N) > tam.jaccard(n_w1_w2_w3, pair_counts, uni_counts, N)
