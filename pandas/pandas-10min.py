#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2018  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gnu.org>
# Maintainer: David Arroyo Menéndez <davidam@gnu.org>

# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with GNU Emacs; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt

# Series
s = pd.Series([1,3,5,np.nan,6,8])
print(s)

# Data Frames
dates = pd.date_range('20130101', periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(df)

# Creating a DataFrame by passing a dict of objects that can be converted to series-like.

df2 = pd.DataFrame({ 'A' : 1.,
                     'B' : pd.Timestamp('20130102'),
                     'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                     'D' : np.array([3] * 4,dtype='int32'),
                     'E' : pd.Categorical(["test","train","test","train"]),
                     'F' : 'foo' })

print(df2)

print(df2.dtypes)

# Viewing Data

print("VIEWING DATA")

print("df.head()")

print(df.head())

print("df.tail(3)")

print(df.tail(3))

print("df.index")

print(df.index)

print("df.columns")

print(df.columns)

print("df.values")

print(df.values)

print("df.describe")

print(df.describe)

print("Transposing your data: df.T")

print(df.T)

print("Sorting by an axis")

print(df.sort_index(axis=1, ascending=False))


# GETTING

print(df['A'])

print(df[0:3])

print(df['20130102':'20130104'])

print(df.loc[dates[0]])

print(df.loc[:,['A','B']])

print(df.loc['20130102':'20130104',['A','B']])

print(df.loc['20130102',['A','B']])

print(df.loc[dates[0],'A'])

print(df.at[dates[0],'A'])

print(df.iloc[3])

print(df.iloc[3:5,0:2])

print(df.iloc[[1,2,4],[0,2]])

print(df.iloc[1:3,:])

print(df.iloc[:,1:3])

print(df.iloc[1,1])

print(df.iat[1,1])

# BOOLEAN INDEXING

print(df[df.A > 0])

print(df[df > 0])

df2 = df.copy()

df2[df2 > 0] = -df2

print(df2)

# Missing Data

df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])

df1.loc[dates[0]:dates[1],'E'] = 1

print(df1)

df1.dropna(how='any')

print(df1.fillna(value=5))

# pd.isna(df1)

# OPERATIONS

print(df.mean())

print(df.mean(1))

s = pd.Series([1,3,5,np.nan,6,8], index=dates).shift(2)

print(s)

print(df.sub(s, axis='index'))

print(df.apply(np.cumsum))

print(df.apply(lambda x: x.max() - x.min()))

s = pd.Series(np.random.randint(0, 7, size=10))

print(s)

print(s.value_counts())

s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])

print(s.str.lower())

# MERGE

df = pd.DataFrame(np.random.randn(10, 4))

print(df)

pieces = [df[:3], df[3:7], df[7:]]

print(pd.concat(pieces))

left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})

right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})

print(left)

print(right)

print(pd.merge(left, right, on='key'))

left = pd.DataFrame({'key': ['foo', 'bar'], 'lval': [1, 2]})

right = pd.DataFrame({'key': ['foo', 'bar'], 'rval': [4, 5]})

print(left)

print(right)

print(pd.merge(left, right, on='key'))

df = pd.DataFrame(np.random.randn(8, 4), columns=['A','B','C','D'])

print(df)

s = df.iloc[3]

print(s)

print(df.append(s, ignore_index=True))


df = pd.DataFrame({'A' : ['bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
                   'B' : ['one', 'two', 'three', 'two', 'two', 'one', 'three'],
                   'C' : np.random.randn(7),
                   'D' : np.random.randn(7)})

print(df)

print(df.groupby('A').sum())

print(df.groupby(['A','B']).sum())

tuples = list(zip(*[['bar', 'bar', 'baz', 'baz',
                     'foo', 'foo', 'qux', 'qux'],
                    ['one', 'two', 'one', 'two',
                     'one', 'two', 'one', 'two']]))

index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])

df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])

df2 = df[:4]

print(df2)

stacked = df2.stack()

print(stacked)

print(stacked.unstack())

print(stacked.unstack(1))

print(stacked.unstack(0))


# PIVOT TABLES

df = pd.DataFrame({'A' : ['one', 'one', 'two', 'three'] * 3,
                   'B' : ['A', 'B', 'C'] * 4,
                   'C' : ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
                   'D' : np.random.randn(12),
                   'E' : np.random.randn(12)})

print(df)

print(pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C']))

rng = pd.date_range('1/1/2012', periods=100, freq='S')

print(rng)

ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)

print(ts)

print(ts.resample('5Min').sum())

rng = pd.date_range('3/6/2012 00:00', periods=5, freq='D')

ts = pd.Series(np.random.randn(len(rng)), rng)

print(ts)

ts_utc = ts.tz_localize('UTC')

print(ts_utc)

print(ts_utc.tz_convert('US/Eastern'))

# TIME SERIES

rng = pd.date_range('1/1/2012', periods=5, freq='M')

ts = pd.Series(np.random.randn(len(rng)), index=rng)

print(ts)

ps = ts.to_period()

print(ps)

print(ps.to_timestamp())

prng = pd.period_range('1990Q1', '2000Q4', freq='Q-NOV')

ts = pd.Series(np.random.randn(len(prng)), prng)

ts.index = (prng.asfreq('M', 'e') + 1).asfreq('H', 's') + 9

print(ts.head())

# CATEGORICALS

# df = pd.DataFrame({"id":[1,2,3,4,5,6], "raw_grade":['a', 'b', 'b', 'a', 'a', 'e']})

# df["grade"] = df["raw_grade"].astype('category')

# print df["grade"]

# df["grade"].cat.categories = ["very good", "good", "very bad"]

# df["grade"] = df["grade"].cat.set_categories(["very bad", "bad", "medium", "good", "very good"])

# print df["grade"]

# print df.sort_values(by="grade")

# print df.groupby("grade").size()

# PLOTTING

# ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))

# ts = ts.cumsum()

# ts.plot()

# df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=['A', 'B', 'C', 'D'])

# df = df.cumsum()

# plt.figure(); df.plot(); plt.legend(loc='best')

# Getting Data In/Out

# csv

df.to_csv('foo.csv')

print(pd.read_csv('foo.csv'))

# hdf5

# df.to_hdf('foo.h5','df')

# pd.read_hdf('foo.h5','df')

# excel

# df.to_excel('foo.xlsx', sheet_name='Sheet1')

# pd.read_excel('foo.xlsx', 'Sheet1', index_col=None, na_values=['NA'])
