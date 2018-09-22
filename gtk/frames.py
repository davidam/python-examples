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
ventana.minsize(200, 200)
ventana.maxsize(300, 300)

zona1 = Frame(ventana, background='green', width=50, height=50)
zona1.pack(side=TOP, expand=True, fill=BOTH)
eti = Label(zona1, text="arriba", bg="yellow")
eti.pack()
Label(zona1, text="abajo", bg="yellow").pack(side=BOTTOM)

zona2 = Frame(ventana, background="blue", width=30, height=30)
zona2.pack(side=BOTTOM, expand=True, fill=BOTH)
Label(zona2, text="izquierda", bg='red').pack(side=LEFT)
Label(zona2, text="derecha", bg='red').pack(side=RIGHT)

ventana.mainloop()
