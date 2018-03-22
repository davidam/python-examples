#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

print("Introduce una moneda en los cubiletes software")
cubilete = input("Escoge estos cubiletes donde meter el dinero (gcc | emacs | bash | gimp) ")
print("Has metido tu moneda en " + cubilete)
moneda = random.sample(["gcc", "emacs", "bash", "gimp"], 1)
#print(moneda[0])
print("Hemos lanzado unos cuantos commits") 
resultado = input("Escribe dónde está ahora tu moneda (gcc | emacs | bash | gimp) ")
if (moneda[0] == resultado):
    print("Acertaste. Eres un buen gnu, RMS está orgulloso de ti. Te devolvemos la moneda.")
else:
    print("Has hecho un pecado. Nos quedamos con tu moneda.")

