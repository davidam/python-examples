import scipy.stats as stats

oddsratio, pvalue = stats.fisher_exact([[8, 2], [1, 5]])
print(pvalue)
print(oddsratio)
