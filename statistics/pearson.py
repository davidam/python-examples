
from scipy import stats
import numpy as np
# Calculate a Pearson correlation coefficient and the p-value for testing non-correlation.
a = np.array([0, 0, 0, 1, 1, 1, 1])
b = np.arange(7)
print(stats.pearsonr(a, b))
print(stats.pearsonr([1,2,3,4,5], [5,6,7,8,7]))
