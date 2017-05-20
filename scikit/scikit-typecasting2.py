from sklearn import datasets
from sklearn.svm import SVC
iris = datasets.load_iris()
clf = SVC()
print clf.fit(iris.data, iris.target)

list(clf.predict(iris.data[:3]))
print clf.fit(iris.data, iris.target_names[iris.target])

list(clf.predict(iris.data[:3])) 

# Here, the first predict() returns an integer array, since iris.target (an integer array) was used in fit. The second predict() returns a string array, since iris.target_names was for fitting.
