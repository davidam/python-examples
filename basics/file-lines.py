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
import re

filepath="README.org"
with open(filepath) as fp:
    for cnt, line in enumerate(fp):
        print("Line {}: {}".format(cnt, line)) # Imprime línea y número de línea
        print(line[0])         # Imprime el primer caracter
        print(line[(len(line) -2)]) # Imprime el último carácter
        match = re.search(r'flask', line)
        # If-statement after search() tests if it succeeded
        if match:
            flaskcnt = cnt
            flaskline = line

print("---------------------------------------------------------------------------")
print("Flask is in the line {}. The full text is: {}".format(flaskcnt, flaskline)) # match.group() ## 'found word:cat'
