#!/usr/bin/python
# -*- coding: utf-8 -*-

conjunto = "Italia", "Grecia", "Italia", "China", "Grecia", "Brasil"
paises = set(conjunto)
europa = set({"Francia", "Italia", "España", "Grecia", "Alemania", "Portugal"})

paises.remove("China")
paises.add("Turquia")
paises.add("Alemania")
print("contenido actual del conjunto de paises:")
for pais in paises:
    print(pais.ljust(15))

print("\n\ncontenido actual del conjunto de Europa:")
for pais in europa:
    print(pais.ljust(15))

print("\n\nUnion de los dos conjuntos:")
for pais in paises | europa:
    print(pais.ljust(15))

print("\n\nIntersección de los dos conjuntos (elementos en común):")
for pais in paises.intersection(europa):
    print(pais.ljust(15))

print("\n\ndiferencia simétrica de los dos conjuntos (elementos que no están en ambos conjuntos):")
for pais in paises.symmetric_difference(europa):
    print(pais.ljust(15))
