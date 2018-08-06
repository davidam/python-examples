#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd

dates = ['2015-12-25', '2015-12-26']

# 1) Use a list comprehension.
[print(d.date()) for d in pd.to_datetime(dates)]

# 2) Convert the dates to a DatetimeIndex and extract the python dates.
print(pd.DatetimeIndex(dates).date.tolist())

dates = pd.DatetimeIndex(start='2000-01-01', end='2010-01-01', freq='d').date.tolist()

[print(d.date()) for d in pd.to_datetime(dates)]
# 100 loops, best of 3: 3.11 ms per loop

pd.DatetimeIndex(dates).date.tolist()
# 100 loops, best of 3: 6.85 ms per loop
datetimes = ['Jun 1 2005  1:33PM', 'Aug 28 1999 12:00AM']

print(pd.to_datetime(datetimes).to_pydatetime().tolist())
