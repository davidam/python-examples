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

cadena = input("Escriba un texto: ")
if cadena.isalnum():
    print("Consta de letras y/o números, sin espacios")
if cadena.isalpha():
    print("Consta de letras, sin números y sin espacios")
if cadena.isdigit():
    print("Consta sólo de números, sin espacios")
if cadena.islower():
    print("La cadena está en minúsculas")
if cadena.isupper():
    print("La cadena está en mayúsculas")
if cadena.isspace():
    print("La cadena tiene un espacio en blanco")
if cadena.istitle():
    print("La cadena tiene un formato de título")
if cadena.startswith("Barcelona"):
    print("La cadena comienza con Barcelona")
if cadena.endswith("Barcelona"):
    print("La cadena finaliza con Barcelona")
