from scipy.stats import chisquare
import numpy as np

chisquare([16, 18, 16, 14, 12, 12])

chisquare([16, 18, 16, 14, 12, 12], f_exp=[16, 16, 16, 16, 16, 8])

obs = np.array([[16, 18, 16, 14, 12, 12], [32, 24, 16, 28, 20, 24]]).T
obs.shape

chisquare(obs)

chisquare(obs, axis=None)

chisquare(obs.ravel())

# p-values
print(chisquare([16, 18, 16, 14, 12, 12], ddof=1))

print(chisquare([16, 18, 16, 14, 12, 12], ddof=[0,1,2]))

chisquare([16, 18, 16, 14, 12, 12],
          f_exp=[[16, 16, 16, 16, 16, 8], [8, 20, 20, 16, 12, 12]],
          axis=1)
