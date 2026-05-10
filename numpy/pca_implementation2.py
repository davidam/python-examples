import numpy as np
import matplotlib.pyplot as plt


### Representing the Data
# data has shape (n, d)
# data = np.array([
#     [   1,   2,  -1,   4,  10],
#     [   3,  -3,  -3,  12, -15],
#     [   2,   1,  -2,   4,   5],
#     [   5,   1,  -5,  10,   5],
#     [   2,   3,  -3,   5,  12],
#     [   4,   0,  -3,  16,   2],
# ])



data = np.loadtxt("features_list.csv",
		  delimiter=",", dtype=str)
data = np.genfromtxt("features_list.csv",delimiter=",", dtype="int")


### Step 1: Standardize the Data along the Features
standardized_data = (data - data.mean(axis = 0)) / data.std(axis = 0)


### Step 2: Calculate the Covariance Matrix
# use `ddof = 1` if using sample data (default assumption) and use `ddof = 0` if using population data
covariance_matrix = np.cov(standardized_data, ddof = 1, rowvar = False)


### Step 3: Eigendecomposition on the Covariance Matrix
eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)


### Step 4: Sort the Principal Components
# np.argsort can only provide lowest to highest; use [::-1] to reverse the list
order_of_importance = np.argsort(eigenvalues)[::-1] 

# utilize the sort order to sort eigenvalues and eigenvectors
sorted_eigenvalues = eigenvalues[order_of_importance]
sorted_eigenvectors = eigenvectors[:,order_of_importance] # sort the columns


### Step 5: Calculate the Explained Variance
# use sorted_eigenvalues to ensure the explained variances correspond to the eigenvectors
explained_variance = sorted_eigenvalues / np.sum(sorted_eigenvalues)

### Iterate on the Number of Principal Components
plt.plot(np.cumsum(explained_variance))
plt.show()

### Step 6: Reduce the Data via the Principal Components
k = 2 # select the number of principal components
reduced_data = np.matmul(standardized_data, sorted_eigenvectors[:,:k]) # transform the original data


### Step 7: Determine the Explained Variance
total_explained_variance = sum(explained_variance[:k])


