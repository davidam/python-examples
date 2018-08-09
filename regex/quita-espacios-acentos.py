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
