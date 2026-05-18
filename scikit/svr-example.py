#!/usr/bin/python
# -*- coding: utf-8 -*-

from sklearn.svm import SVR
import numpy as np
# n_samples, n_features = 10, 5
# np.random.seed(0)
X = np.array([[0., 0.], [1., 1.]])
y = np.array([0, 1])
clf = SVR(C=1.0, epsilon=0.2)
print(clf.fit(X, y))
print(clf.predict([[1., 1.]]))
print(type(clf))
print(type(clf.predict([[1., 1.]])))
