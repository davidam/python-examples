import numpy as np
A = np.array([[1,-2j],[2j,5]])
print("Print Array A")
print(A)

L = np.linalg.cholesky(A)
print("Print Array L")
print(L)

print("verify that L * L.H = A")
print(np.dot(L, L.T.conj())) # verify that L * L.H = A


A = [[1,-2j],[2j,5]] # what happens if A is only array_like?
print("what happens if A is only array_like?")
print(np.linalg.cholesky(A)) # an ndarray object is returned

# But a matrix object is returned if A is a matrix object
print(np.linalg.cholesky(np.matrix(A)))
