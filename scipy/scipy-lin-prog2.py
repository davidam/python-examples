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

from scipy.optimize import linprog
import numpy as np

# Objective function
z = np.array([ 7, 6])

# Constraints
C = np.array([
    [ 2, 3],          #C1
    [ 6, 5]           #C2
])

b = np.array([12, 30])

# Bounds
x1 = (0, None)
x2 = (0, None)

#Solution
sol = linprog(-z, A_ub = C, b_ub = b, bounds = (x1, x2), method='simplex', options={'maxiter':True})

print("x1 = %s, x2 = %s, z = %s" % (sol.x[0], sol.x[1], sol.fun*-1))
