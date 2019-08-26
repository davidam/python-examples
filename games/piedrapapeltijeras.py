#!/usr/bin/python

print("Escoja piedra, papel o tijeras para cada jugador")

jugador1 = input("jugador 1: ")
jugador2 = input("jugador 2: ")

if (jugador1 == jugador2):
    print("Empate")
elif ((jugador1 == "piedra") & (jugador2 == "tijeras")):
    print("Gana jugador1")
elif ((jugador1 == "tijeras") & (jugador2 == "papel")):
    print("Gana jugador1")
elif ((jugador1 == "papel") & (jugador2 == "piedra")):
    print("Gana jugador1")
elif ((jugador1 == "tijeras") & (jugador2 == "piedra")):
    print("Gana jugador2")
elif ((jugador1 == "papel") & (jugador2 == "tijeras")):
    print("Gana jugador2")
elif ((jugador1 == "piedra") & (jugador2 == "papel")):
    print("Gana jugador2")
