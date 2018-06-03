import numpy as np
from sklearn.model_selection import KFold

X = ["a", "b", "c", "d"]
kf = KFold(n_splits=2)
for train, test in kf.split(X):
    print("train: %s, test: %s" % (train, test))

X = np.array([[0., 0.], [1., 1.], [-1., -1.], [2., 2.]])
y = np.array([0, 1, 0, 1])

X_train, X_test, y_train, y_test = X[train], X[test], y[train], y[test]    
print("X_train: %s, \nX_test: %s, \ny_train: %s, \ny_test: %s " % (X_train, X_test, y_train, y_test))
