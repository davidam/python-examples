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
#!/usr/bin/python# -*- coding: utf-8 -*-
import re, unicodedata

def elimina_tildes(s):
    aux = ""
    for c in unicodedata.normalize('NFD', s):
        if (unicodedata.category(c) != 'Mn'):
            aux = aux + c
    return aux

print(elimina_tildes("córcholis"))

def elimina_tildes(s):
    aux = ""
    for c in unicodedata.normalize('NFD', s):
        if (unicodedata.category(c) != 'Mn'):
            aux = aux + c
    return aux

def elimina_espacios(s):
    result = ""
    if re.search(r' ', s):
        result = re.sub(r' ', '-', s)
    return result

def elimina_tildes_espacios(m):
    aux = ""
    aux = elimina_tildes(m)
    aux = elimina_espacios(aux)
    return aux

cadena = "Hola Mundo"
print(elimina_espacios(cadena))

cadena2 = "Jamón"
print(elimina_espacios(cadena2))

cadena3 = "Era un hombre diligente, la policía entró en su casa rápidamente"
print(cadena3)
print(elimina_tildes_espacios(cadena3))
