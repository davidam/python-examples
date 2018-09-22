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

def comprobar(miboton):
    if password.get_text() == "sorpresa":
        etiqresultado.set_text("Hola " + nombre.get_text() + ", identificacion correcta")
        nombre.set_editable(False)
    else:
        etiqresultado.set_text("Identificacion erronea")

ventana = Gtk.Window(title="Entrada de texto")
ventana.connect("delete-event", Gtk.main_quit)
rejilla = Gtk.Grid()
ventana.add(rejilla)

etiqnombre = Gtk.Label("Escriba su nombre: ")
etiqpassword = Gtk.Label("Escriba el password:")
nombre = Gtk.Entry()
nombre.set_max_length(10)

password = Gtk.Entry()
password.set_visibility(False)
boton = Gtk.Button(label="Comprobar")
boton.connect("clicked", comprobar)
etiqresultado = Gtk.Label()

rejilla.attach(etiqnombre, 0, 0, 1, 2)
rejilla.attach_next_to(nombre, etiqnombre, Gtk.PositionType.RIGHT, 1, 2)
rejilla.attach_next_to(password, etiqpassword, Gtk.PositionType.BOTTOM, 1, 2)
rejilla.attach(boton, 1, 4, 1, 1)
rejilla.attach(etiqresultado, 0, 5, 2, 1)

ventana.show_all()
Gtk.main()
