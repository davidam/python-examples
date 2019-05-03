#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division

#----------------------------------------------------------------------
# Nombre:       ejemplo_scipy_raicesPolinomio.py
# PropÃ³sito:    Aprender como calcular las raices de un polinomio con python.
#
# Origen:        Propio a partir de la documentaciÃ³n oficial.
# Autor:         JosÃ© MarÃ­a Herrera-Fernandez, Luis Miguel SÃ¡nchez-Brea
#
# CreaciÃ³n:        20 de Septiembre de 2013
# Historia:
#
# Dependencias:    scipy, matplotlib
# Licencia:        GPL
#----------------------------------------------------------------------


"""
DescripciÃ³n: Ejemplo de cÃ³mo calcular las raices de un polinomio mediante scipy.
"""


import scipy as sp                  # Importamos scipy como el alias sp
import matplotlib.pyplot as plt     # Importamos matplotlib.pyplot como el alias plt

# Creamos un polinomio
polinomio = [1.3,4,.6,-1]   # polinomio = 1.3 x^3 + 4 x^2 + 0.6 x - 1
print("Creamos un polinomio")
print(polinomio)

# Creamos un array dimensional
x = sp.arange(-4,1,.05)
print("Creamos un array dimensional")
print(x)
#  Evaluamos el polinomio en x mediante polyval.
y = sp.polyval(polinomio,x)
print("Evaluamos el polinomio en x mediante polyval.")
print(y)
# Calculamos las raices del polinomio
raices = sp.roots(polinomio)
print("Calculamos las raices del polinomio")
print(raices)
# Evaluamos el polinomio en las raices
s = sp.polyval(polinomio,raices)

# Las presentamos en pantalla
print ("Las raices son %2.2f, %2.2f, %2.2f. " % (raices[0], raices[1], raices[2]))
