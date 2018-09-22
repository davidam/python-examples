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

primero = input("Primer articulo: ")
precio1 = input("Precio: ")
segundo = input("Segundo articulo: ")
precio2 = input("Precio: ")
tercero = input("Tercer articulo: ")
precio3 = input("Precio: ")

print("----------------FACTURA------------")
print(primero + "............." + precio1)
print(segundo + "............." + precio2)
print(tercero + "............." + precio3)
total = int(precio1) + int(precio2) + int(precio3)
print("Precio: " + str(total))
