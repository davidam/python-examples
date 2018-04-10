#!/usr/bin/python

def agregar():
    print("\nAGREGAR PAIS/CAPITAL")
    pais = input("Escriba el pais: ")
    capital = input("Escriba la capital: ")
    fichero.write(pais + "\n")
    fichero.write(capital + "\n")

def buscar():
    print("\nBUSCAR")
    mipais = input("Escriba el pais a buscar: ")
    mipais = mipais.title()
    fichero.seek(0)
    pais = "comenzamos"
    micapital = "Lo siento, no se encuentra ese pais"
    while (pais != ""):
        pais = fichero.readline()
        capital = fichero.readline()
        if pais == mipais + "\n":
            micapital = "La capital de " + mipais + " es " + capital
    print(micapital)
    
def listar():
    print("\nLISTADO")
    fichero.seek(0)
    contenido = fichero.readlines()
    print("Contenido exacto: ")
    print(contenido)
    print("Contenido controlado: ")
    print("PAIS".ljust(20) + "CAPITAL")
    print("-".center(30, "-"))
    pais = "comenzamos"
    fichero.seek(0)
    while(pais != ""):
        pais = fichero.readline().replace("\n", "")
        capital = fichero.readline().replace("\n", "")
        print((pais.ljust(20) + capital.ljust(20)).title())

opcion = -1
fichero = open("/tmp/ficherolineas.txt", "a+")

while(opcion != 0):
    print("\n\nMENU DE OPCIONES")
    print("1 - Agnadir pais/capital")
    print("2 - Buscar")
    print("3 - Listado")
    print("0 - Salir")
    opcion = eval(input("Indique la opcion: "))
    if (opcion == 1):
        agregar()
    if (opcion == 2):
        buscar()
    if (opcion == 3):
        listar()

print("\nFin del programa")
