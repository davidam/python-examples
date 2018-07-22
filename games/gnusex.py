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

print("¿Tienes novia?")

gnusex = input("(S | N) ")

if (gnusex == "S"):
    print("¿Usa GNU/Linux?")
    gnulinux = input("(S | N) ")

    if (gnulinux == "S"):
        print("¿Mantiene algún paquete serio de GNU?")
        gnupackage = input("(S | N) ")
        if (gnupackage == "S"):
            print("Felicidades, RMS está interesado en conoceros")
        else:
            print("Debes explicarle que el mundo lo necesita, haz que programe hasta que mantenga uno y que lo haga bastante bien. ¡El mundo está en peligro es muy importante!")
    else:
        print("Déjala o instálale Trisquel es pecadora")
