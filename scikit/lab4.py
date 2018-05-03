#!/usr/bin/python
# -*- coding: utf-8 -*-

#read data using pandas
import pandas as pd
import numpy as np

boston_df  = pd.read_csv('boston.csv')

#verify whether ther exisits NaN 
print(np.sum(boston_df.isnull()))

print(boston_df)
print(boston_df.describe())

#get names
x_var_names = list(boston_df)[:-1]
print(x_var_names)
y_var_names = list(boston_df)[-1]
print(y_var_names)

#get matrix X and vector y

X = boston_df[x_var_names]
y = boston_df[y_var_names]

#some easy checks

print(X.shape)
print(y.shape)

#split
import numpy as np
import sklearn
print(sklearn.__version__)
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

print(sum(y))
print(len(y))
print(X_train.shape)
print(X_test.shape)

from sklearn import linear_model

#build the model
rl_model = linear_model.LinearRegression()

#fit the model

rl_model.fit(X_train,y_train)

#Before we test, let's explore the model

coefs = [rl_model.intercept_]
coefs.extend(list(rl_model.coef_))

labels = ['bias']
labels.extend(x_var_names)

"----"
for n,c in zip(labels,coefs):
    print(n,str(round(c,3))) 
    print("---------------")
