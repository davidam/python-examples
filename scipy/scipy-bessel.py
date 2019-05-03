#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division

#----------------------------------------------------------------------
# Nombre:       ejemplo_scipy_bessel.py
# PropÃ³sito:    Aprender el uso el paquete special de scipy.
#
# Origen:        Propio.
# Autor:         JosÃ© MarÃ­a Herrera-Fernandez, Luis Miguel SÃ¡nchez-Brea
#
# CreaciÃ³n:        18 de Septiembre de 2013
# Historia:
#
# Dependencias:    scipy, matplotlib
# Licencia:        GPL
#----------------------------------------------------------------------


"""
DescripciÃ³n: CÃ¡lculo de los coeficientes de orden cero y uno de la funciÃ³n de Bessel
contenida en el paquete special.
"""
from scipy import special                   # Importamos scipy.special
import scipy as sp                          # Importamos scipy como el alias sp
import matplotlib.pyplot as plt             # Importamos matplotlib.pyplot como el alias plt.

# Creamos el array dimensional
x = sp.arange(0,50,.1)
print(x)
x1 = sp.arange(0,1,.1)
print(x1)
# Calculamos los coeficientes de orden cero.
# j0 = special.j0(x)
j0 = special.j0(x1)
print(j0)
# # Calculamos los coeficientes de orden uno.
j1 = special.j1(x)
print(j1)
