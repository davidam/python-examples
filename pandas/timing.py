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
