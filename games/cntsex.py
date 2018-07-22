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

print("Soy An. Soy una chica. ¿Te gusto?")

love = input("(S | N) ")

if (love == "N"):
    print("Aún así, puedes estar afiliado.")

if (love == "S"):
    pi = input("¿Vas a piquetes?. Demuéstralo quiero verte, al menos durante tres meses, quizás tres años. (S | N) ")

    if (pi == "S"):
        re = input("¿Eres reformista?. Demuéstralo quiero verte, al menos durante tres meses, quizás tres años. (S | N) ")

        if (re == "N"):
            per = input("¿Te interesa estar en una permanencia?. Demuéstralo quiero verte, al menos un año, quizás tres (S | N) ")

            if (per == "S"):
                sec = input("¿Te interesa una secretaría?. Demuéstralo quiero verte, debes cumplir cuatro años (S | N) ")

                if (sec == "S"):
                    print("Felicidades, ya podemos ir a tomar algo a tu casa")
