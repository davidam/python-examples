#!/usr/bin/python# -*- coding: utf-8 -*-

# Copyright (C) 2018  Leticia Martin Fuertes

# Author: Leticia Martin Fuertes

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

import re

saludos = ["hola", "adios", "hasta luego", "nos vemos"]

def detectar_locuciones(lista):
    for elemento in lista:
        if re.search(r' ', elemento):
            print(elemento)

detectar_locuciones(saludos)

infinitivos = ["comprometer", "abrir", "manejar", "absorver", "congelar", "estudiar", "descubrir", "correr"]

def crear_participios(verbos):
    for verbo in verbos:
        if re.search(r'er$', verbo):
            participio = re.sub(r'er$', 'ido', verbo)
            print(participio)
        elif re.search(r'ar$', verbo):
            participio = re.sub(r'ar$', 'ado', verbo)
            print(participio)
        elif re.search(r'ir$', verbo):
            participio = re.sub(r'rir$', 'ierto', verbo)
            print(participio)

crear_participios(infinitivos)
