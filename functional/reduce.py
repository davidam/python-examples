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
from functools import reduce
from functools import partial

f = lambda a,b: a if (a > b) else b
print("REDUCE EXAMPLES")
print("a if (a > b) else b")
print(reduce(f, [47,11,42,102,13]))
print("x+y, range(1,101)")
print(reduce(lambda x, y: x+y, range(1,101)))
print("x*y, range(1,49)")
print(reduce(lambda x, y: x*y, range(1,49)))
print(reduce(lambda x, y: x*y, range(44,50))/reduce(lambda x, y: x*y, range(1,7)))

def foo(a, b, c):
     return a + b if c else a * b

print(reduce(partial(foo, c=True), [1,2,3,4,5], 2))
print(reduce(partial(foo, c=False), [1,2,3,4,5], 2))
