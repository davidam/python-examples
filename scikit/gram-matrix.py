import numpy as np
from sklearn import svm
X = np.array([[0, 0], [1, 1]])
y = [0, 1]
clf = svm.SVC(kernel='precomputed')
# linear kernel computation
gram = np.dot(X, X.T)
print(clf.fit(gram, y))

# predict on training examples
print(clf.predict(gram))
