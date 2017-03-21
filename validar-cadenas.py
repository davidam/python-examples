#!/usr/bin/python

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
