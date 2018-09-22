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

dicc = {"precio1": 2300, "precio2": 3450, "precio3": 2760}
print("Diccionario original:")
print(dicc)
print("Añadimos un nuevo elemento:")
dicc["precio4"] = 1000
print(dicc)
print("Eliminamos un elemento:")
del dicc["precio1"]
print(dicc)
print("Las claves son:")
print(list(dicc.keys()))
print("Los valores son:")
print(list(dicc.values()))

print("Ahora un diccionario de listas")
dicc2 = {"elem1": list(), "elem2": [1, 2, 3]}
print(dicc2)
dicc2["elem1"].append(1)
print(dicc2)
dicc2["elem1"].append(2)
print(dicc2)
