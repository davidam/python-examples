#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2018  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gnu.org>
# Maintainer: David Arroyo Menéndez <davidam@gnu.org>

# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with GNU Emacs; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, 
# Boston, MA 02110-1301 USA,

# A confusion matrix C is such that Ci,j. Being Ci,j is the number of predictions known to be in group ii but predicted to be in group j
# See accuracy.py to understand the concept of prediction.

from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Binary Classification
X, y = make_classification(n_samples=1000, n_features=4, n_classes=2)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)

from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier()
model.fit(X_train, y_train)

y_predict = model.predict(X_test)

from sklearn.metrics import confusion_matrix

print("y_test: %s. \n\nThe size of the vector is %s.\n" % (y_test, len(y_test)))
print("y_predict: %s. \n\nThe size of the vector is %s.\n" % (y_predict, len(y_predict)))
print("The accuracy between vectors is %s.\n" % accuracy_score(y_test, y_predict))
print("The confusion matrix is \n%s" % confusion_matrix(y_test, y_predict))
print("The diagonal is high because the accuracy is high.")
print("0 is predicted as 0 many times")
print("1 is predicted as 1 many times\n")

print("By definition a confusion matrix :math:C is such that :math:C_{i, j} is equal to the number of observations known to be in group :math:i but predicted to be in group :math:j. Thus in binary classification, the count of true negatives is :math:C_{0,0}, false negatives is :math:C_{1,0}, true positives is :math:C_{1,1} and false positives is :math:C_{0,1}.")

