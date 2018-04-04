
nombres = []
nuevo = ""
while nuevo.upper() != "FIN":
    nuevo = input("Escribe un nombre (FIN para acabar): ")
    if nuevo.upper() != "FIN":
        veces = nombres.count(nuevo)
        if veces == 0:
            nombres.append(nuevo)
nombres.sort()
print("La lista ordenada es: ")
for nombre in nombres:
    print(nombre.ljust(15))
