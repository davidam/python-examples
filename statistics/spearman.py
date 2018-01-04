from scipy import stats
stats.spearmanr([1,2,3,4,5], [5,6,7,8,7])
import numpy as np

np.random.seed(1234321)
x2n = np.random.randn(100, 2)
y2n = np.random.randn(100, 2)
stats.spearmanr(x2n)

stats.spearmanr(x2n[:,0], x2n[:,1])

rho, pval = stats.spearmanr(x2n, y2n)
print(rho)
print(pval)
rho, pval = stats.spearmanr(x2n.T, y2n.T, axis=1)
print(rho)
stats.spearmanr(x2n, y2n, axis=None)
stats.spearmanr(x2n.ravel(), y2n.ravel())

xint = np.random.randint(10, size=(100, 2))
stats.spearmanr(xint)
