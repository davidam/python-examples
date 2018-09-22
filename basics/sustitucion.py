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
nombre = "Señora Alfredo Villar"
print("Nombre original: " + nombre)
nombre = nombre.replace("Señora", "Señor")
print("Género cambiado: " + nombre)
nombre = nombre.lstrip("Señor ")
print("Sin formalismos: " + nombre)
print("\nCambio de texto dinámico:")
cadena = "bienvenido a mi programa {0}"
print("original: " + cadena)
print(("Formateado: " + cadena.format("en Python")))
cadena = "Importe bruto: {0}€ + IVA: {1}€ = Importe neto: {2}€"
print("\noriginal: " + cadena)
print(("Formateado: " + cadena.format(100, 21, 121)))
cadena = "Importe bruto: {bruto}€ + IVA: {iva}€ = Importe neto: {neto}€"
print("\noriginal: " + cadena)
print(("Formateado: " + cadena.format(iva=21, neto=121, bruto=100)))
