# encoding: utf-8

print("resultado del clásico".upper())
cadena = input("Indique el resultado en formato Barcelona Goles Madrid Goles: ")
espacios = cadena.count(" ")
if espacios != 3:
    print("El formato escrito erróneo!")
else:
    posBarc = cadena.find("Barcelona")
    posMadr = cadena.find("Madrid")
    if posBarc == -1 or posMadr == -1:
        print("Los equipos no son correctos")
    else:
        if posBarc < posMadr:
            print("El partido se jugó en el Camp Nou")
        else:
            print("El partido se jugó en el Santiago Bernabeu")
            
