#!/usr/bin/python

# Abrimos el archivo fichero.txt
fo = open("/tmp/fichero.txt", "wb")
fo.write( "Gora python\n");

# Cerramos el archivo fichero.txt
fo.close()
