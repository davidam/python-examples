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
z = np.array([300,500,200])
expense = 75000

# Constraints
C = np.array([
    [ 10, 7.5,   4],        #C1
    [  0,  10,   0],        #C2
    [0.5, 0.4, 0.5],        #C3
    [  0, 0.4,   0],        #C4
    [0.5, 0.1, 0.5],        #C5
    [0.4, 0.2, 0.4],        #C6
    [  1, 1.5, 0.5],        #C7
    [  1,   0,   0],        #C8
    [  0,   1,   0],        #C9
    [  0,   0,   1]         #C10
])

b = np.array([4350, 2500, 280, 140, 280, 140, 700, 300, 180, 400])

# Bounds
x1 = (0, None)
x2 = (0, None)
x3 = (0, None)

#Solution
sol = linprog(-z, A_ub = C, b_ub = b, bounds = (x1, x2, x3), method='simplex')

#Profit Monthly.
profit = (sol.fun*-1) - expense

print("x1 = %s, x2 = %s, x3 = %s, z = %s" % (sol.x[0], sol.x[1], sol.x[2], profit))
