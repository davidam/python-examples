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


def generaLista(x, y):
    if (x == y):
        return [y]
    else:
        return [x] + generaLista(x+1, y)

def divisores(x):
    l = generaLista(1, x)
    laux = []
    for i in l:
        if (0 == (x % i)):
            laux = laux + [i]
    return laux

def divisoresPropios(x):
    l = divisores(x)
    return l[1:len(l)-1]

def sumaLista(l):
    aux = 0
    for i in l:
        aux = aux + i
    return aux

def abundante(x):
    aux = 0
    for i in (divisoresPropios(x)):
        aux = aux + i
    return aux

x = int(input("Give me a number: "))

print("La lista de divisores de %s es: %s" % (x, divisores(x)))
print("La lista de divisores propios de %s es: %s" % (x, divisoresPropios(x)))
l = divisores(x)
l = l[0:len(l)-1]
if (x == sumaLista(l)):
    print("%s es un número perfecto" % x)
else:
    print("%s no es un número perfecto" % x)    

if (x < sumaLista(divisoresPropios(x))):
    print("%s es un número abundante" % x)
else:
    print("%s no es un número abundante" % x)    

if (x > sumaLista(divisoresPropios(x))):
    print("%s es un número defectivo" % x)
else:
    print("%s no es un número defectivo" % x)    

    
