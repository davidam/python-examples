from pandas.tools import plotting
import pandas

data = pandas.read_csv('brain_size.csv', sep=';', na_values=".")
data.shape    # 40 rows and 8 columns
data.columns  # It has columns   

plotting.scatter_matrix(data[['Gender', 'Height', 'MRI_Count']]) 

import matplotlib.pyplot as plt
plt.show()
