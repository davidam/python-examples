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

v1 = [1, 1, 0, 1, 0, 1]
v2 = [1, 2, 0, 1, 0, 1]
print(v1)
print(v2)

success = 0
fails = 0
for i in range(0, len(v1)):
    if (v1[i] == v2[i]):
        success = success + 1
    else:
        fails = fails + 1
print("success: " + str(success))
print("fails: " + str(fails))

accuracy = success / len(v1)
print(accuracy)
# print(len(v1))
# print(len(v2))
