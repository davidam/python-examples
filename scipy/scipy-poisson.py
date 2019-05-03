from scipy.stats import poisson
import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)

mu = 0.6
mean, var, skew, kurt = poisson.stats(mu, moments='mvsk')
print("mean: %s, var: %s, skew: %s, kurt: %s" % (mean, var, skew, kurt))

x = np.arange(poisson.ppf(0.01, mu),
              poisson.ppf(0.99, mu))
print(x)
ax.plot(x, poisson.pmf(x, mu), 'bo', ms=8, label='poisson pmf')
ax.vlines(x, 0, poisson.pmf(x, mu), colors='b', lw=5, alpha=0.5)

rv = poisson(mu)
ax.vlines(x, 0, rv.pmf(x), colors='k', linestyles='-', lw=1,
        label='frozen pmf')
ax.legend(loc='best', frameon=False)
#plt.show()
print(np.array([0.54881164, 0.87809862, 0.97688471]))
prob = poisson.cdf(x, mu)
print(prob)
b = np.array_equal(prob, np.array([0.54881164, 0.87809862, 0.97688471]))
print("Boolean: %s" % b)
print(np.allclose(x, poisson.ppf(prob, mu)))

r = poisson.rvs(mu, size=1000)
print(r)
