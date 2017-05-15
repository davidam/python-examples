#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division

#----------------------------------------------------------------------
# Nombre:       ejemplo_scipy_integrales.py
# PropÃ³sito:    Aprender como integrar con python.
#
# Origen:        Propio .
# Autor:         JosÃ© MarÃ­a Herrera-Fernandez, Luis Miguel SÃ¡nchez-Brea
#
# CreaciÃ³n:        18 de Septiembre de 2013
# Historia:
#
# Dependencias:    scipy
# Licencia:        GPL
#----------------------------------------------------------------------


"""
DescripciÃ³n: Ejemplo de cÃ³mo usar la funciÃ³n integrate para realizar integrales 
numÃ©ricas en python.
"""

import scipy as sp      # Importamos scipy como el alias sp
from scipy import integrate         # Importamos integrate de scipy

# Ejemplo 1: DefiniciÃ³n de la integral para la funciÃ³n y = e^(-x).

def integral_1(limite_inferior, limite_superior, mostrar_resultados):
    """
    (float,float, bool) -->(float, float)
    * DescripciÃ³n: Calculo de la integral de limite_inferior a limite_superior de 
    la funciÃ³n y = e^(-x)
    * Entradas:
    - limite_inferior = inicio del intervalo de integraciÃ³n.
    - limite_superior = fin del intervalo de integraciÃ³n.
    * Salidas:
    - tupla con las soluciones de la integral
    * Test:
    >>> integral_1(limite_inferior = 0, limite_superior = 5)
    La integral entre 0.00 y  5.00 es 
    (0.9932620530009145, 1.102742400728068e-14)
    """
    # Defino la funciÃ³n e^(-x)
    exponencial_decreciente = lambda x: sp.exp(-x)
    
    # Presento en pantalla los resultados si quiero
    if mostrar_resultados == True:
        print ('La integral entre %2.2f y  %2.2f es '% (limite_inferior, limite_superior))
        print(integrate.quad(exponencial_decreciente,limite_inferior,limite_superior))
    
    # Los devuelvo
    return integrate.quad(exponencial_decreciente ,limite_inferior,limite_superior)
