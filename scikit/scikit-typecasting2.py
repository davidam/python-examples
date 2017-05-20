from sklearn import datasets
from sklearn.svm import SVC
iris = datasets.load_iris()
clf = SVC()
print clf.fit(iris.data, iris.target)

list(clf.predict(iris.data[:3]))
print clf.fit(iris.data, iris.target_names[iris.target])

list(clf.predict(iris.data[:3])) 
