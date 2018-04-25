#!/usr/bin/python
# -*- coding: utf-8 -*-

# EJERCICIO 2

import pandas as pd
import numpy as np

fhr = pd.read_csv('FHR-Apgar.csv',sep = ';')

fhr['y'] = np.where(fhr['Apgar 1'] > 7, 1, 0)

fhr_not_nan = fhr.dropna()

print(fhr_not_nan)

#El siguiente ejercicio consistirá en obtener la matrix de datos  XX  y el vector de etiquetas  yy . Cabe recordar en este punto que sería conveniente realizar un análisis exploratorio de los datos, tal y como se describió en el Lab 1.

x_var_name = list(fhr_not_nan)[4:-1]
print("El siguiente ejercicio consistirá en obtener la matrix de datos  XX  y el vector de etiquetas  yy . Cabe recordar en este punto que sería conveniente realizar un análisis exploratorio de los datos, tal y como se describió en el Lab 1.")
print(x_var_name)
y_var_name = list(fhr_not_nan)[-1]
X = fhr_not_nan[x_var_name]
y = fhr_not_nan[y_var_name]


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3, random_state=0)
print("X_train es ")    
print(X_train.shape)
print("X_test es ")    
print(X_test.shape)

from sklearn.linear_model import LogisticRegression

#crea model
log_reg = LogisticRegression()

#ajustar el modelo

log_reg.fit(X_train,y_train)

y_pred = log_reg.predict(X_test)

from sklearn.metrics import accuracy_score

acc = accuracy_score(y_test,y_pred)

print("Mi model es tan bueno como: ",acc)


from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV

tuned_parameters = {'gamma': np.logspace(-4,1,25),'C':np.logspace(1,4,25)}

svm = SVC(kernel = 'rbf')
grid =  GridSearchCV(svm,param_grid = tuned_parameters,cv = 10,n_jobs = -1)
grid.fit(X_train,y_train)

y_pred_svm = grid.predict(X_test)
acc = accuracy_score(y_test,y_pred_svm)

print('Mi Super SVM tiene un acc de: ',acc)
