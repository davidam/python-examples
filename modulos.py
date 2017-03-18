import os
import sys
import random
print("Ejemplos módulo OS")
print(("Carpeta de trabajo actual: " + os.getcwd()))
if(os.path.exists(os.getcwd() + "\\soluciones")):
    print("Dispone de una carpeta de soluciones")
else:
    print("La carpeta de soluciones no se encuentra")
print()
print("EJEMPLO MODULO SYS")
print(("La ruta y nombre del intérprete Python es " + sys.executable))
print("La información sobre esta versión de Python es " + (sys.version))

print()
print("EJEMPLOS MODULO RANDOM")
contador = 1
linea = ""
while (contador <= 10):
    linea = linea + " " + str(random.randint(1, 10))
    contador = contador + 1
print("Diversos números al azar entre 1 y 10:")
print(linea)
lista = ["Barcelona", "Girona", "Lleida", "Tarragona"]
print("Una provincia al azar: " + str(random.choice(lista)))
print("Dos provincias al azar: " + str(random.sample(lista, 2)))
print("Todas las provincias mezcladas:")
random.shuffle(lista)
print(lista)
