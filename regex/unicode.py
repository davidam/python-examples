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

japanese = "桜の花びらたち"
print(type(japanese))

string = 'öäå'

capitalize = 'Äránzazu'

match = re.search(r'\w', capitalize)
if match:
    print("Yes, it's")
else:
    print("Not, it isn't")

match = re.search(r'[a-z]', string)
if match:
    print("Yes, it's")
else:
    print("Not, it isn't")

match = re.search(r'ö', string)
if match:
    print("Yes, it's")
else:
    print("Not, it isn't")

match = re.search(r'\w', string)
if match:
    print("Yes, it's")
else:
    print("Not, it isn't")

match = re.search(r'\w', japanese)
if match:
    print("Yes, it's")
else:
    print("Not, it isn't")

match = re.search(r'ち', japanese)
if match:
    print("Yes, it's")
else:
    print("Not, it isn't")
    
