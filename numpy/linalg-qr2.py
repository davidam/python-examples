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
# along with linalg-qr2; see the file LICENSE.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

import numpy as np
import numpy.linalg as LA
#If A = qr such that q is orthonormal (which is always possible via Gram-Schmidt), then x = inv(r) * (q.T) * b. (In numpy practice, however, we simply use lstsq.)

A = np.array([[0, 1], [1, 1], [1, 1], [2, 1]])
print(A)
b = np.array([1, 0, 2, 1])
q, r = LA.qr(A)
p = np.dot(q.T, b)
print(np.dot(LA.inv(r), p))
