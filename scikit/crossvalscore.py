#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
from sklearn import metrics
from sklearn.model_selection import ShuffleSplit
from sklearn import datasets
from sklearn.model_selection import cross_val_score
from sklearn import svm
clf = svm.SVC(kernel='linear', C=1)
iris = datasets.load_iris()

scores = cross_val_score(clf, iris.data, iris.target, cv=5)
n_samples = iris.data.shape[0]
cv = ShuffleSplit(n_splits=5, test_size=0.3, random_state=0)
cross_val_score(clf, iris.data, iris.target, cv=cv)

def custom_cv_2folds(X):
    n = X.shape[0]
    i = 1
    while i <= 2:
        idx = np.arange(n * (i - 1) / 2, n * i / 2, dtype=int)
        yield idx, idx
        i += 1



custom_cv = custom_cv_2folds(iris.data)
print(cross_val_score(clf, iris.data, iris.target, cv=custom_cv))
