
class Calculator(object):
    def add(self, x, y):
        return x+y
    def sub(self, x, y):
        return x-y
    def prod(self, x, y):
        return x*y
    def div(self, x, y):
        return x/y
    def prodUsingAdd(self, x, y):
        r = 0
        for i in range(0, x):
            r = self.add(r, y)
        return r
