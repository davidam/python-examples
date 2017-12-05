import numpy as np
a = np.array([[1.0, 2.0], [3.0, 4.0]])
print(a)

a.transpose()

np.linalg.inv(a)

u = np.eye(2) # unit 2x2 matrix; "eye" represents "I"
print u

j = np.array([[0.0, -1.0], [1.0, 0.0]])

np.dot (j, j) # matrix product

np.trace(u)  # trace

y = np.array([[5.], [7.]])
np.linalg.solve(a, y)

np.linalg.eig(j)
