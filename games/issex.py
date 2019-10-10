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

print("Conozco el problema italiano, soy tu amiga, sígueme.")
i = input("¿Te gusto? ( S | N ): ")

if ((i == 'S') | (i == 's')):
    print("No digas nada sobre mí, trabájame en lo técnico, solo vamos a hablar a través del grupo, nunca más un mundo sin nosotros")
    print("Tu trabajarás en lo ténico que yo hago y al revés también. Tenemos muchas cosas en común. Nos amaremos de manera económicamente sostenible.")
    s = input("¿Te interesa? ( S | N ): ")
    if ((s == 'S') | (s == 's')):
        print("Pues ya sabes participa en el grupo, de manera voluntaria. Échale horas.")
        while ((s == 'S') | (s == 's')):
            print("Pues ya sabes participa en el grupo, de manera voluntaria. Échale horas.")
            s = input("¿Te interesa? ( S | N ): ")
        print("Te vemos mal, hablas de manera autoritaria, machista, cuéntanos tu dolor, unas personas que conocen bien el peligro de las drogas psiquiátricas te van a ayudar, so cansino.")
