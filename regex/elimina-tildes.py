#!/usr/bin/python
# -*- coding: utf-8 -*-

import unicodedata
def elimina_tildes(s):
   return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))

print("córcholis")
print(elimina_tildes("córcholis"))

def elimina_tildes2(s):
    aux = ""
    for c in unicodedata.normalize('NFD', s):
        if (unicodedata.category(c) != 'Mn'):
            aux = aux + c
    return aux

print(elimina_tildes2("córcholis"))
