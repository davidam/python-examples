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

# Python 3 Program to find first
# n terms of Golomb sequence.

# Return the nth element of
# Golomb sequence
def findGolomb(n):

    # base case
    if (n == 1):
        return 1

    # Recursive Step
    return 1 + findGolomb(n -
    findGolomb(findGolomb(n - 1)))


# Print the first n term
# of Golomb Sequence
def printGolomb(n):

    # Finding first n terms of
    # Golomb Sequence.
    for i in range(1, n + 1):
        print(findGolomb(i), end=" ")

# Driver Code
n = 9

printGolomb(n)
print("\n")
