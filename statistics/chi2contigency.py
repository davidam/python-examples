from scipy.stats import chi2_contingency
import numpy as np

obs = np.array([[10, 10, 20], [20, 20, 20]])
chi2_contingency(obs)

g, p, dof, expctd = chi2_contingency(obs, lambda_="log-likelihood")
g, p

obs = np.array(
    [[[[12, 17],
       [11, 16]],
      [[11, 12],
       [15, 16]]],
     [[[23, 15],
       [30, 22]],
      [[14, 17],
       [15, 16]]]])
print(chi2_contingency(obs))
