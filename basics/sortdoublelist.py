# Copyright (C) 2020  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@libresoft>
# Maintainer: David Arroyo Menéndez <davidam@libresoft>

# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with python-examples; see the file LICENSE.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, 
# Boston, MA 02110-1301 USA,

results = []

def getKey0(item):
    return int(item[0])

def getKey1(item):
    return int(item[1])

l = [[2, 3], [6, 7], [3, 34], [24, 64], [1, 43]]

#print(mysort(l))

print(sorted(l, key=getKey0))
print(sorted(l, key=getKey1))

