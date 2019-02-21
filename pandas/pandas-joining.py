#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2019  David Arroyo Menéndez

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

s1 = pd.Series(['a', 'b'])
s2 = pd.Series(['c', 'd'])
pd.concat([s1, s2])

print(pd.concat([s1, s2], ignore_index=True))

print(pd.concat([s1, s2], keys=['s1', 's2',]))

print(pd.concat([s1, s2], keys=['s1', 's2'], names=['Series name', 'Row ID']))

df1 = pd.DataFrame([['a', 1], ['b', 2]],
                    columns=['letter', 'number'])
print(df1)

df2 = pd.DataFrame([['c', 3], ['d', 4]],
                    columns=['letter', 'number'])
print(df2)

print(pd.concat([df1, df2]))

df3 = pd.DataFrame([['c', 3, 'cat'], ['d', 4, 'dog']],
                    columns=['letter', 'number', 'animal'])
print(df3)

print(pd.concat([df1, df3]))

print(pd.concat([df1, df3], join="inner"))

df4 = pd.DataFrame([['bird', 'polly'], ['monkey', 'george']],
                    columns=['animal', 'name'])

print(pd.concat([df1, df4], axis=1))

df5 = pd.DataFrame([1], index=['a'])
print(df5)
df6 = pd.DataFrame([2], index=['a'])
print(df6)
print(pd.concat([df5, df6]))
