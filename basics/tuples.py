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
# along with tuples; see the file LICENSE.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

a = (1, 1, 2, 2, 3, 3)
print(tuple(set(a)))

b = ["CPython", "IronPython", "Stackless", "Stackless", "CPython"]
print(list(set(b)))


# ZIP

a = ("URL", "Titulo", "Tema")
b = ("recursospython.com", "Recursos Python", "Lenguaje de programacion Python")
c = zip(a, b)
for nombre, valor in c:
    print("%s: %s" % (nombre, valor))

nombres = "Jorge", "Ricardo", "Carlos"
apellidos = "Gonzalez", "Medina", "Pedro"
edades = 30, 25, 41

for nombre, apellido, edad in zip(nombres, apellidos, edades):
    print("%s %s: %d." % (nombre, apellido, edad))
