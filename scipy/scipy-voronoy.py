from scipy.spatial import KDTree
import numpy as np

# A Voronoi diagram is a subdivision of the space into the nearest neighborhoods of a given set of points.

points = np.array([[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2],
                   [2, 0], [2, 1], [2, 2]])
tree = KDTree(points)
tree.query([0.1, 0.1])

x = np.linspace(-0.5, 2.5, 31)
y = np.linspace(-0.5, 2.5, 33)
xx, yy = np.meshgrid(x, y)
xy = np.c_[xx.ravel(), yy.ravel()]
import matplotlib.pyplot as plt
plt.pcolor(x, y, tree.query(xy)[1].reshape(33, 31))
plt.plot(points[:,0], points[:,1], 'ko')
plt.show()

