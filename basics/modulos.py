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
import os
import sys
import random
print("Ejemplos módulo OS")
print(("Carpeta de trabajo actual: " + os.getcwd()))
if(os.path.exists(os.getcwd() + "\\soluciones")):
    print("Dispone de una carpeta de soluciones")
else:
    print("La carpeta de soluciones no se encuentra")
print()
print("EJEMPLO MODULO SYS")
print(("La ruta y nombre del intérprete Python es " + sys.executable))
print("La información sobre esta versión de Python es " + (sys.version))

print()
print("EJEMPLOS MODULO RANDOM")
contador = 1
linea = ""
while (contador <= 10):
    linea = linea + " " + str(random.randint(1, 10))
    contador = contador + 1
print("Diversos números al azar entre 1 y 10:")
print(linea)
lista = ["Barcelona", "Girona", "Lleida", "Tarragona"]
print("Una provincia al azar: " + str(random.choice(lista)))
print("Dos provincias al azar: " + str(random.sample(lista, 2)))
print("Todas las provincias mezcladas:")
random.shuffle(lista)
print(lista)
