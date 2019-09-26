#!/usr/bin/python
# -*- coding: utf-8 -*-

from sklearn.svm import SVR
import numpy as np
# n_samples, n_features = 10, 5
# np.random.seed(0)
X = [[0., 0.], [1., 1.]]
y = [0, 1]
clf = SVR(C=1.0, epsilon=0.2)
print(clf.fit(X, y))
print(clf.predict([[1., 1.]]))
