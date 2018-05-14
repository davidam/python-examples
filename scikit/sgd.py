#!/usr/bin/python
# -*- coding: utf-8 -*-

from sklearn.linear_model import SGDClassifier
X = [[0., 0.], [1., 1.]]
y = [0, 1]
clf = SGDClassifier(loss="hinge", penalty="l2")
print(clf.fit(X, y))
# After being fitted, the model can then be used to predict new values:

# print(clf.predict([[2., 2.]]))

clf = SGDClassifier(loss="log").fit(X, y)

print(clf.predict_proba([[1., 1.]]))
