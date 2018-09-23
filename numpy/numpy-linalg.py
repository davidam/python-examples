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
import numpy as np
a = np.array([[1.0, 2.0], [3.0, 4.0]])
print(a)

a.transpose()

np.linalg.inv(a)

u = np.eye(2) # unit 2x2 matrix; "eye" represents "I"
print(u)

j = np.array([[0.0, -1.0], [1.0, 0.0]])

print(np.dot(j, j)) # matrix product

print(np.trace(u))  # trace

y = np.array([[5.], [7.]])
print(np.linalg.solve(a, y))

print(np.linalg.eig(j))
