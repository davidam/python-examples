import pandas as pd
import numpy as np

dates = pd.date_range('20130101', periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(df)

# GETTING
print("###################################")
print("############ GETTING ##############")
print("###################################")
# print(df['A'])

# print(df[0:3])

# print(df['20130102':'20130104'])

# print(df.loc[dates[0]])

print(df.loc[:,['A','B']])

# print(df.loc['20130102':'20130104',['A','B']])

print(df.loc['20130102',['A','B']])

# print(df.loc[dates[0],'A'])

# print(df.at[dates[0],'A'])

# print(df.iloc[3])

# print(df.iloc[3:5,0:2])

# print(df.iloc[[1,2,4],[0,2]])

# print(df.iloc[1:3,:])

# print(df.iloc[:,1:3])

# print(df.iloc[1,1])

# print(df.iat[1,1])
