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
#!/usr/bin/env python 
# -*- coding: utf-8 -*-

 

cadena = "¿A dónde voy?" 

desplazamiento = 3 

 

def encriptar(cadena, desplazamiento): 

    letras_mayusculas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", 

                         "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", 

                         "U", "V", "W", "X", "Y", "Z"] 

    letras_minusculas = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", 

                         "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", 

                         "u", "v", "w", "x", "y", "z"] 
    
    letras_mayusculas_desplazadas = letras_mayusculas[desplazamiento:] + letras_mayusculas[:desplazamiento] 

    letras_minusculas_desplazadas = letras_minusculas[desplazamiento:] + letras_minusculas[:desplazamiento] 

    lista_caracteres = [] 

 

    for caracter in cadena: 

        if caracter in letras_mayusculas: 

            lista_caracteres.append(letras_mayusculas_desplazadas [letras_mayusculas.index(caracter)]) 

        elif caracter in letras_minusculas: 

            lista_caracteres.append(letras_minusculas_desplazadas [letras_minusculas.index(caracter)]) 

        else: 

            lista_caracteres.append(caracter) 

 

    nueva_cadena = "".join(lista_caracteres) 

 

    return nueva_cadena 

 

def desencriptar(cadena, desplazamiento): 

    letras_mayusculas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", 

                         "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", 

                         "U", "V", "W", "X", "Y", "Z"] 

    letras_minusculas = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", 

                         "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", 

                         "u", "v", "w", "x", "y", "z"] 

    letras_mayusculas_desplazadas = letras_mayusculas[-desplazamiento:] + letras_mayusculas[:-desplazamiento] 

    letras_minusculas_desplazadas = letras_minusculas[-desplazamiento:] + letras_minusculas[:-desplazamiento] 

    lista_caracteres = [] 

 

    for caracter in cadena: 

        if caracter in letras_mayusculas: 

            lista_caracteres.append(letras_mayusculas_desplazadas [letras_mayusculas.index(caracter)]) 

        elif caracter in letras_minusculas: 

            lista_caracteres.append(letras_minusculas_desplazadas [letras_minusculas.index(caracter)]) 

        else: 

            lista_caracteres.append(caracter) 

 

    nueva_cadena = "".join(lista_caracteres) 

 

    return nueva_cadena

print("Encriptando cadena:"+ cadena + " con desplazamiento " + str(desplazamiento))
print(encriptar(cadena, desplazamiento))

print("Desencriptando cadena:"+ cadena + " con desplazamiento " + str(desplazamiento))
print(desencriptar(cadena, desplazamiento))
