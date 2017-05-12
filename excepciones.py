
nombre = raw_input("Indica el nombre del archivo: ")
try:
    fichero = open(nombre + ".txt", "r")
    line2 = fichero.readline(2)
    line3 = fichero.readline(3)
    print(("Second line: " + line2))
    print(("Third line: " + line3))
    fichero.close()
except FileNotFoundError:
    print("\nEl archivo indicado no existe")
print("\nEl programa ha finalizado correctamente.")
