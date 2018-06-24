#Representar gráficas inline
#%matplotlib inline
import matplotlib.pyplot as plt
#Importe el módulo de pandas
import pandas as pd

pd_diabetes = pd.read_csv('diabetes.csv',delimiter = ';')
print(pd_diabetes)
#Lea el documento diabetes.csv. Recuerde que el fichero debe estar en el mismo directorio en el que esté creando el 
#notebook o bien debe indicar el path completo.

print("¿Cuál es el valor de la presión arterial?")
print(pd_diabetes['BP'][415])
print("¿Cuál es el valor de la variable respuesta para el paciente número 415?")
print(pd_diabetes['Y'][415])

print("¿Cuál es el resumen de datos?")
print(pd_diabetes.describe())

# import matplotlib.pyplot as plt
# plt.show()
#plt.plot(pd_diabetes['AGE'].plot.hist(x = 'Age',alpha=0.5))
plt.hist(pd_diabetes['AGE'])
plt.show()

plt.scatter(x=pd_diabetes['AGE'], y=pd_diabetes['Y'])
plt.show()

#representar la scatter matrix
from pandas.tools.plotting import scatter_matrix
scatter_matrix(pd_diabetes, alpha = 0.2, figsize = (12,12), diagonal = 'kde')

pd_diabetes.corr()


# # #Y vs SEX, scatter plot
# plt.boxplot(by='SEX',column = 'Y')

# fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(6, 6), sharey=True)
# axes[0, 0].boxplot(pd_diabetes, labels=labels)
# axes[0, 0].set_title('Default', fontsize=fs)

# plt.show()
