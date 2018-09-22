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
# -*- coding: utf-8 -*-

conjunto = "Italia", "Grecia", "Italia", "China", "Grecia", "Brasil"
paises = set(conjunto)
europa = set({"Francia", "Italia", "España", "Grecia", "Alemania", "Portugal"})

paises.remove("China")
paises.add("Turquia")
paises.add("Alemania")
print("contenido actual del conjunto de paises:")
for pais in paises:
    print(pais.ljust(15))

print("\n\ncontenido actual del conjunto de Europa:")
for pais in europa:
    print(pais.ljust(15))

print("\n\nUnion de los dos conjuntos:")
for pais in paises | europa:
    print(pais.ljust(15))

print("\n\nIntersección de los dos conjuntos (elementos en común):")
for pais in paises.intersection(europa):
    print(pais.ljust(15))

print("\n\ndiferencia simétrica de los dos conjuntos (elementos que no están en ambos conjuntos):")
for pais in paises.symmetric_difference(europa):
    print(pais.ljust(15))
