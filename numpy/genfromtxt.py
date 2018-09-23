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

import numpy as np
from io import BytesIO

# Splitting the lines into columns
## The delimiter argument

data = "1, 2, 3\n4, 5, 6"
print(np.genfromtxt(BytesIO(data.encode('utf-8')), delimiter=","))
data = "  1  2  3\n  4  5 67\n890123  4"
print(np.genfromtxt(BytesIO(data.encode('utf-8')), delimiter=3))
data = "123456789\n   4  7 9\n   4567 9"
print(np.genfromtxt(BytesIO(data.encode('utf-8')), delimiter=(4, 3, 2)))

## The autostrip argument

data = "1, abc , 2\n 3, xxx, 4"
# Without autostrip
print(np.genfromtxt(BytesIO(data.encode('utf-8')), delimiter=",", dtype="|U5"))
# With autostrip
print(np.genfromtxt(BytesIO(data.encode('utf-8')), delimiter=",", dtype="|U5", autostrip=True))

## The comments argument
data = """#
 # Skip me !
 # Skip me too !
 1, 2
 3, 4
 5, 6 #This is the third line of the data
 7, 8
 # And here comes the last line
 9, 0
 """

print(np.genfromtxt(BytesIO(data.encode('utf-8')), comments="#", delimiter=","))

data = "\n".join(str(i) for i in range(10))
print(np.genfromtxt(BytesIO(data.encode('utf-8')),))
print(np.genfromtxt(BytesIO(data.encode('utf-8')), skip_header=3, skip_footer=5))

# Skipping lines and choosing columns
## The skip_header and skip_footer arguments

data = "\n".join(str(i) for i in range(10))
print(np.genfromtxt(BytesIO(data.encode('utf-8')),))
print(np.genfromtxt(BytesIO(data.encode('utf-8')), skip_header=3, skip_footer=5))

# usecols

data = "1 2 3\n4 5 6"
print(np.genfromtxt(BytesIO(data.encode('utf-8')), usecols=(0, -1)))
