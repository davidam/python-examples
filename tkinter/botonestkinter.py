#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2018  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gnu.org>
# Maintainer: David Arroyo Menéndez <davidam@gnu.org>

# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with GNU Emacs; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,
try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter 
except ImportError:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here

ventana = Tk()
ventana.title("mi primera ventana en Python")
etiqueta1 = Label(ventana, text="Nombre: ")
etiqueta1.grid(row=0, column=0)
etiqueta2 = Label(ventana, text="Apellidos: ")
etiqueta2.grid(row=1, column=0)
boton1 = Button(ventana, text="Aceptar", bg='red')
boton1.grid(row=2, column=0)
boton2 = Button(ventana, text="Boton Normal")
boton2.grid(row=3, column=1)
boton3 = Button(ventana, text="Boton FLAT", relief=FLAT)
boton3.grid(row=3, column=2)
boton4 = Button(ventana, text="Boton SUNKEN", relief=SUNKEN)
boton3.grid(row=3, column=3)
boton3 = Button(ventana, text="Boton RIDGE", relief=RIDGE)
boton3.grid(row=3, column=4)
boton4 = Button(ventana, text="Boton SOLID", relief=SOLID)
boton4.grid(row=3, column=5)
boton5 = Button(ventana, text="Boton GROOVE", relief=GROOVE)
boton5.grid(row=3, column=6)
boton6 = Button(ventana, text="Boton RAISED", relief=RAISED)
boton6.grid(row=3, column=7)

ventana.mainloop()
