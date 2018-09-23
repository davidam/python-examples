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
import time

def time_dec(func):
    def wrap(*arg, **kwargs):
        init_time = time.time()
        res = func(*arg, **kwargs)
        print(func.__name__, time.time()-init_time)
        return res
    return wrap

@time_dec
def foo(n):
    out = 0
    for i in range(n):
        out = out + i
    return out

@time_dec
def bar(n):
    return sum(range(n))

bar(100000000)
foo(100000000)

# """
# OUTPUT:
# bar 0.63298201561
# foo 2.44244480133
# """
