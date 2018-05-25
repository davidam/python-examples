#!/usr/bin/python
# -*- coding: utf-8 -*-

from chempy import Equilibrium
from sympy import symbols
K1, K2, Kw = symbols('K1 K2 Kw')
e1 = Equilibrium({'MnO4-': 1, 'H+': 8, 'e-': 5}, {'Mn+2': 1, 'H2O': 4}, K1)
e2 = Equilibrium({'O2': 1, 'H2O': 2, 'e-': 4}, {'OH-': 4}, K2)
coeff = Equilibrium.eliminate([e1, e2], 'e-')
coeff
redox = e1*coeff[0] + e2*coeff[1]
print(redox)
autoprot = Equilibrium({'H2O': 1}, {'H+': 1, 'OH-': 1}, Kw)
n = redox.cancel(autoprot)
print(n)
redox2 = redox + n*autoprot
print(redox2)
