from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
"""
 input graph             minimum spanning tree

     (0)                         (0)
    /   \                       /
   3     8                     3
  /       \                   /
(3)---5---(1)               (3)---5---(1)
  \       /                           /
   6     2                           2
    \   /                           /
     (2)                         (2)
"""

X = csr_matrix([[0, 8, 0, 3],
                [0, 0, 2, 5],
                [0, 0, 0, 6],
                [0, 0, 0, 0]])
print(X)
Tcsr = minimum_spanning_tree(X)
print("-----------------------------")
print(Tcsr)
print("-----------------------------")
print(Tcsr.toarray().astype(int))
