#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division

#----------------------------------------------------------------------
# Nombre:       scipy-interpolacion.py
# PropÃ³sito:    Aprender como interpolar con python.
#
# Origen:        Propio a partir de la documentaciÃ³n oficial.
# Autor:         JosÃ© MarÃ­a Herrera-Fernandez, Luis Miguel SÃ¡nchez-Brea
#
# CreaciÃ³n:        18 de Septiembre de 2013
# Historia:
#
# Dependencias:    scipy
# Licencia:        GPL
#----------------------------------------------------------------------

"""
DescripciÃ³n: Ejemplo de cÃ³mo hacer una interpolaciÃ³n en python.
"""
import scipy as sp                  # Importamos scipy como el alias sp
from scipy import interpolate       # Importamos interpolate de scipy
import matplotlib.pyplot as plt     # Importamos matplotlib.pyplot como el alias plt

# Creamos el array dimensional
x = sp.linspace(0,3,10)

# Evaluamos x en la funciÃ³n y = e^(-x/3) (generando nuestros "datos experimentales")
y = sp.exp(-x/3.0)

# Interpolamos
interpolacion = interpolate.interp1d(x, y)
print("interpolacion: %s" % interpolacion)
# Creamos un nuevo array dimensional con mÃ¡s puntos en el mismo intervalo
x2 = sp.linspace(0,3,100)

# Evaluamos x2 en la interpolaciÃ³n
y2 = interpolacion(x2)

# Creamos la figura
plt.figure

# Dibujamos las dos grÃ¡ficas juntas
plt.plot(x, y, 'o', x2, y2, '-')

# AÃ±adimos la leyenda
plt.legend(('Datos conocidos', 'Datos experimentales'))

# aÃ±adimos las etiquetas
plt.xlabel('Eje x')
plt.ylabel('Eje y')

# Mostramos en pantalla
plt.show()
