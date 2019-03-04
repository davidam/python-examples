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


import random
number_list = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
print ("Original list : ",  number_list)
random.shuffle(number_list) #shuffle method
print ("List after first shuffle  : ",  number_list)
random.shuffle(number_list)
print ("List after second shuffle : ",  number_list)

#creating the list with range
x = [i for i in range(10)]
print(x)
random.shuffle(x)
print(x)
