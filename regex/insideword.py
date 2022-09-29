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
import re

string0 = input('You must write here: ')
m = re.match(r"(.*)([a-z]|[A-Z])+(.*)", string0)
if m:
    print("There are characters of the alphabet in the input")
else:
    print("There are not characters of the alphabet in the input")
# m = re.match(r"(\w+) (\w+) (\w+)", "Isaac Newton physicist")
# print(m.group(0))
# print(m.group(1))
# print(m.group(2))
# print(m.group(1, 2, 3))
