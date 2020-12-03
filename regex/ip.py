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
# along with python-examples; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

import re

string = input("Write an ip: ")

n = re.match(r"(\d+)(\.)(\d+)(\.)(\d+)(\.)(\d+)", string)

if not(n): 
    print("It is not an ip")
else:

    if ((int(n.group(1)) >= 0) and (int(n.group(1)) <= 255)):
        ip1 = True
    else:
        ip1 = False

    if ((int(n.group(3)) >= 0) and (int(n.group(3)) <= 255)):
        ip2 = True
    else:
        ip2 = False

    if ((int(n.group(5)) >= 0) and (int(n.group(5)) <= 255)):
        ip3 = True
    else:
        ip3 = False

    if ((int(n.group(7)) >= 0) and (int(n.group(7)) <= 255)):
        ip4 = True
    else:
        ip4 = False
    
    if (ip1 and ip2 and ip3 and ip4):
        print("It's an ip")
