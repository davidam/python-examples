#!/usr/bin/python

primero = input("Primer articulo: ")
precio1 = input("Precio: ")
segundo = input("Segundo articulo: ")
precio2 = input("Precio: ")
tercero = input("Tercer articulo: ")
precio3 = input("Precio: ")

print("----------------FACTURA------------")
print(primero + "............." + precio1)
print(segundo + "............." + precio2)
print(tercero + "............." + precio3)
total = int(precio1) + int(precio2) + int(precio3)
print("Precio: " + str(total))
