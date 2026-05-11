import numpy as np
from sklearn.decomposition import PCA
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
# n_components = min(n_samples, n_features)
# https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html
num_components = min(X.shape)

pca = PCA(n_components=num_components)
pca.fit(X)
print(pca.explained_variance_ratio_)
print(pca.singular_values_)
