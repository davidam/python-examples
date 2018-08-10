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

edad = int(input("¿Qué edad tienes? "))

if (edad < 16):
    lombrices = input("¿Te salieron lombrices en el culete? ( S | N ) ")
    if (lombrices == "S"):
        print("Te vamos a dar supositorios")
    else:
        print("Muy bien")
else:
    python = input("¿Escribiste código Python con una licencia libre? ( S | N ) ")
    if (python == "S" ):
        print("Súbelo al repositorio, así más gente puede ver lo que pasa")
    else:
        print("Si estás viendo al doctor puede ser que te haga falta escribirlo")
