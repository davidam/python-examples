def hanoi():
    discos = input("Dime tus discos y te digo los pasos: ")
    print(hanoiAux(int(discos)))

def hanoiAux(discos):
    if (discos == 1):
        return 1
    else:
        return 1 + (2 * (hanoiAux(discos - 1)))

hanoi()
