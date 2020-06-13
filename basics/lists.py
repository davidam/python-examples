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
#!/usr/bin/python

mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3

li = ["a", "b", "mpilgrim", "z", "example"]
li[0]  
li.extend(["two", "elements"])
li.insert(2, "new")
li.index("example")
li.remove("example")

lista = ['a', 'b', 'mpilgrim']
lista = lista + ['example', 'new']
lista += ['two']

l = set(li).intersection(lista)

print("li: ", li)
print("lista: ", lista)

print("Intersection ", l)

a = [('when', 3), ('why', 4), ('throw', 9), ('send', 15), ('you', 1)]
b = ['the', 'when', 'send', 'we', 'us']
filtered = [i for i in a if not i[0] in b]
print(filtered)

# prints out 1,2,3
for x in li:
    print(x)

milista = ['This', 'used', 'to', 'be', 'a', 'Whopping', 'Great', 'sentence']
print(sorted(milista, key=str.lower))


# prints list except the first element
l = [[2, 3], [6, 7], [3, 34], [24, 64], [1, 43]]

for i in l[1:len(l)]:
    print(i)
