class Hanoi(object):

  def hanoi(self, discos):
    if (discos == 1):
        return 1
    else:
        return 1 + (2 * (self.hanoi(discos - 1)))

h = Hanoi()
print h.hanoi(4)
