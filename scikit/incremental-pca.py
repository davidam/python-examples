#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
from sklearn.decomposition import IncrementalPCA
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
print(X)
ipca = IncrementalPCA(n_components=2, batch_size=3)
ipca.fit(X)
print(ipca.transform(X))
