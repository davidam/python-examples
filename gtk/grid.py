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

ventana = Gtk.Window(title="Grid")
ventana.connect("delete-event", Gtk.main_quit)
rejilla = Gtk.Grid()
ventana.add(rejilla)
boton1 = Gtk.Button(label="Boton 1")
boton2 = Gtk.Button(label="Boton 2")
boton3 = Gtk.Button(label="Boton 3")
boton4 = Gtk.Button(label="Boton 4")
boton5 = Gtk.Button(label="Boton 5")
boton6 = Gtk.Button(label="Boton 6")

rejilla.add(boton1)
rejilla.attach(boton2, 1, 0, 2, 1)
rejilla.attach_next_to(boton3, boton1, Gtk.PositionType.BOTTOM, 1, 2)
rejilla.attach_next_to(boton4, boton3, Gtk.PositionType.BOTTOM, 2, 1)
rejilla.attach(boton5, 1, 2, 1, 1)
rejilla.attach_next_to(boton6, boton5, Gtk.PositionType.RIGHT, 1, 1)
ventana.show_all()
Gtk.main()
