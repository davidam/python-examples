import pandas as pd
import numpy as np

boston_df  = pd.read_csv('boston.csv')

#verify whether ther exisits NaN 
print(np.sum(boston_df.isnull()))

print(boston_df)

from pandas.tools.plotting import scatter_matrix

scatter_matrix(boston_df, alpha = 0.2, figsize = (12,12), diagonal = 'kde')
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

#"----"
for n,c in zip(labels,coefs):
    print() 
    print(n,str(round(c,3)) )
    print("---------------")


#r2 metric
from sklearn.metrics import r2_score

#Evaluate the first model
y_pred = rl_model.predict(X_test)

#select the metric
r2_model1 = r2_score(y_test,y_pred)


print("R2 model 1:",r2_model1)

# from sklearn.svm import SVR
# from sklearn.model_selection import GridSearchCV
# tuned_parameters = {'gamma': np.logspace(-4,1,25),'C': np.logspace(1,4,25)}
# svm = SVR(kernel = 'rbf')
# grid = GridSearchCV(svm, param_grid=tuned_parameters, cv=10,n_jobs = -1) #10-fold cross-validatio
# grid.fit(X_train, y_train)
# #the result contains the cross-validation results and the best
# y_pred_svm = grid.predict(X_test)

# r2_svm = r2_score(y_test,y_pred_svm)


# #fitting random forest
# from sklearn.ensemble import RandomForestRegressor
# tuned_parameters_2 = {'n_estimators':[500,1000,2000]}
# rand_forest = RandomForestRegressor()
# grid_RF = GridSearchCV(rand_forest,param_grid = tuned_parameters_2,cv = 10,n_jobs = -1)
# grid_RF.fit(X_train,y_train
#            )
# y_pred_rf = grid_RF.predict(X_test)

# r2_rf = r2_score(y_test,y_pred_rf)

# print("-------------")
# print("R2 linear model:",r2_model1)
# print("-------------")
# print("R2 svm:",r2_svm)
# print("-------------")
# print("R2 Random Forest:",r2_rf)
