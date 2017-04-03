#! /usr/bin/env python
# -*- coding: utf-8 -*-

def inversa (cadena):
    invertida = ''
    cont = len(cadena)
    indice = -1
    while cont >= 1:
        invertida += cadena[indice]
        indice = indice + (-1)
        cont -= 1
    return invertida

def es_palindromo (cadena):
    palabra_invertida = inversa (cadena)
    indice = 0
    cont = 0
    for i in range(len(cadena)):
        if palabra_invertida[indice] == cadena[indice]:
            indice += 1
            cont += 1
        else:
            print('No es palindromo')
        break

es_palindromo("abacad")
