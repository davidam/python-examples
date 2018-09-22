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
from gi.repository import Gtk

def saludo(miboton):
    if miboton.get_label() == "Hola":
        print("Hola, buenos dias")
    else:
        print("Ciao, buenas noches")

ventana = Gtk.Window(title="Box")
ventana.connect("delete-event", Gtk.main_quit)
caja = Gtk.Box(spacing=10)
ventana.add(caja)
boton1 = Gtk.Button(label="Hola")
boton1.connect("clicked", saludo)
caja.pack_start(boton1, True, True, 0)

boton2 = Gtk.Button(label="Ciao")
boton2.connect("clicked", saludo)
caja.pack_start(boton2, True, True, 0)
ventana.show_all()
Gtk.main()
