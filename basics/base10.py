#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Obtenemos datos.
nbinario = input('Número binario: ')

# Obtenemos los dígitos.
nbinario = nbinario.split(',')
if len(nbinario) == 1: nbinario = list(nbinario[0])

# Inicializamos algunos contadores.
decimal = 0
potencia = 0

# Le damos la vuelta al número binario.
nbinario.reverse()

# Calculamos el número decimal, a partir del número binario.
for i in nbinario:
    decimal += pow(2,potencia) if i == '1' else 0
    potencia += 1

# Visualizamos resultado.
cadena = u'Su representación decimal es %d' % (decimal)
print(cadena)
