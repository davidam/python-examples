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

ventana = Gtk.Window(title="Table")
ventana.connect("delete-event", Gtk.main_quit)

tabla = Gtk.Table(3, 3)
ventana.add(tabla)
boton1 = Gtk.Button(label="Boton 1")
boton2 = Gtk.Button(label="Boton 2")
boton3 = Gtk.Button(label="Boton 3")
boton4 = Gtk.Button(label="Boton 4")
boton5 = Gtk.Button(label="Boton 5")
boton6 = Gtk.Button(label="Boton 6")

tabla.attach(boton1, 0, 1, 0, 1)
tabla.attach(boton2, 1, 3, 0, 1)
tabla.attach(boton3, 0, 1, 1, 3)
tabla.attach(boton4, 1, 3, 1, 2)
tabla.attach(boton5, 1, 2, 2, 3)
tabla.attach(boton6, 2, 3, 2, 3)

ventana.show_all()
Gtk.main()
