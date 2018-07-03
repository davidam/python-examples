#!/usr/bin/python
# -*- coding: utf-8 -*-

# To evaluate a prediction, you must know the true class and the class predicted. More success, more accuracy.

from sklearn.metrics import accuracy_score

# True class
y = [0, 0, 1, 1, 0]
print("True class: %s" % y)

# Predicted class
y_hat = [0, 1, 1, 0, 0]
print("Predicted class: %s" % y_hat)
# 60% accuracy
print("Accuracy: %s" % accuracy_score(y, y_hat))

# True class
y = [0, 1, 2, 1, 0]
print("True class: %s" % y)
# Predicted class
y_hat = [0, 2, 2, 1, 0]
print("Predicted class: %s" % y_hat)

# 80% accuracy
print("Accuracy: %s" % accuracy_score(y, y_hat))

