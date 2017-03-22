#!/usr/bin/python

contador = 0
print("Esta es la tabla de multiplicar del 10:")
while contador <= 10:
    print(("10 x " + str(contador) + " = " + str(10 * contador)))
    contador = contador + 1
    if contador == 7:
        break
print("Eso es todo!")
