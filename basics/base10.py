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
# Obtenemos datos.
nbinario = input('Número binario: ')

# Obtenemos los dígitos.
nbinario = nbinario.split(',')
if len(nbinario) == 1: nbinario = list(nbinario[0])

# Inicializamos algunos contadores.
decimal = 0
potencia = 0

# Le damos la vuelta al número binario.
nbinario.reverse()

# Calculamos el número decimal, a partir del número binario.
for i in nbinario:
    decimal += pow(2,potencia) if i == '1' else 0
    potencia += 1

# Visualizamos resultado.
cadena = u'Su representación decimal es %d' % (decimal)
print(cadena)
