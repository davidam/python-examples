#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy
import matplotlib.pyplot as plt
from scipy.optimize import fmin
# Función objetivo
rsinc = lambda x: -1 * numpy.sin(x)/x
# Empezamos a partir de x = -5
x0 = -5
xmin0 = fmin(rsinc,x0)
# Empezamos a partir de x = -4
x1 = -4
xmin1 = fmin(rsinc,x1)
# Dibujamos la función
x = numpy.linspace(-15,15,100)
y = rsinc(x)
plt.plot(x,y)
# Dibujo de x0 y el mínimo encontrado empezando en x0
plt.plot(x0,rsinc(x0),'bd',xmin0,rsinc(xmin0),'bo')
# Dibujo de x1 y el mínimo encontrado empezando en x1
plt.plot(x1,rsinc(x1),'rd',xmin1,rsinc(xmin1),'ro')
plt.axis([-15,15,-1.3,0.3])
plt.show()

