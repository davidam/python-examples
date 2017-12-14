from pandas.tools import plotting
import pandas
import matplotlib.pyplot as plt

data = pandas.read_csv('brain_size.csv', sep=';', na_values=".")
data.shape    # 40 rows and 8 columns
data.columns  # It has columns   

mat = plotting.scatter_matrix(data[['Gender', 'Height', 'MRI_Count']]) 
