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

# Python code to generate first
# 'n' terms of the Moser-de
# Bruijn Sequence

# Function to generate nth term
# of Moser-de Bruijn Sequence
def gen(n):

    # S(0) = 0
    if n == 0:
        return 0

    # S(1) = 1
    elif n ==1:
        return 1

    # S(2 * n) = 4 * S(n)
    elif n % 2 ==0:
        return 4 * gen(n // 2)

    # S(2 * n + 1) = 4 * S(n) + 1
    elif n % 2 == 1:
        return 4 * gen(n // 2) +1

# Generating the first 'n' terms
# of Moser-de Bruijn Sequence
def moserDeBruijn(n):
    for i in range(n):
        print(gen(i), end = " ")

# Driver Program
n = 15
print("First", n, "terms of ",
       "Moser-de Brujn Sequence:")
moserDeBruijn(n)
print("\n")
