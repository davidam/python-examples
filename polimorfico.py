class Clase1(object):
    def __init__(self, mivalor):
        self.valor = mivalor

    def __str__(self):
        return "###" + self.valor + "###"

class Clase2(object):
    def __init__(self, mivalor):
        self.valor = mivalor

    def __str__(self):
        return "@@@" + self.valor + "@@@"

c1 = Clase1("Hola")
c2 = Clase2("Adios")
print(str(c1))
print(str(c2))
