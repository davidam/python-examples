#!/usr/bin/python
# -*- coding: utf-8 -*-

nombre = str(input("Indica el nombre del archivo: "))

try:
    fichero = open(nombre, "r+")
except FileNotFoundError:
    fichero = open(nombre, "w")
    
print("El programa continua hasta finalizar")
