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

print("Original list")
print(l)

print("Sorting from zero to n")

print(sorted(l, key=getKey0))
print(sorted(l, key=getKey1))

print("Sorting from n to zero")

print(sorted(l, key=getKey0, reverse=True))
print(sorted(l, key=getKey1, reverse=True))

print("Sorting with strings")

ll = [["hola", 3], ["mundo", 7], ["crue", 34], ["urjc", 64], ["uned", 43]]

print("Original list")
print(ll)

def getKey0str(item):
    return item[0]

print("Sorting from zero to n")

print(sorted(ll, key=getKey0str))
print(sorted(ll, key=getKey1))

print("Sorting from n to zero")

print(sorted(ll, key=getKey0str, reverse=True))
print(sorted(ll, key=getKey1, reverse=True))

lll = [['KRAGG', '1'], ['SULIMAN', '1'], ['CHANSOTHEA', '1'], ['TAMARA', '11'], ['ZAYED', '1'], ['MARCEL', '64'], ['SERGEI', '4']]

print("Another list, integers as strings")
print(lll)
print("Sorting from zero to n")
print(sorted(lll, key=getKey0str))
print(sorted(lll, key=getKey1))
