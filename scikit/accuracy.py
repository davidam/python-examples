#!/usr/bin/python
# -*- coding: utf-8 -*-

# To evaluate a prediction, you must know the true class and the class predicted. More success, more accuracy.

from sklearn.metrics import accuracy_score

# True class
y = [0, 0, 1, 1, 0]
# Predicted class
y_hat = [0, 1, 1, 0, 0]

# 60% accuracy
print(accuracy_score(y, y_hat))

# True class
y = [0, 1, 2, 1, 0]
# Predicted class
y_hat = [0, 2, 2, 1, 0]

# 80% accuracy
print(accuracy_score(y, y_hat))
