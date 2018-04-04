# -*- coding: utf-8 -*-

dicc = {"precio1": 2300, "precio2": 3450, "precio3": 2760}
print("Diccionario original:")
print(dicc)
print("Añadimos un nuevo elemento:")
dicc["precio4"] = 1000
print(dicc)
print("Eliminamos un elemento:")
del dicc["precio1"]
print(dicc)
print("Las claves son:")
print(dicc.keys())
print("Los valores son:")
print(dicc.values())
