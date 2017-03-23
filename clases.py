class Coordenada(object):
    def __init__(self, valorx=0, valory=0):
        self.x = valorx
        self.y = valory

coor = Coordenada(20, 35)
print("valor x:")
print(coor.x)
print("\nvalor y:")
print(coor.y)
