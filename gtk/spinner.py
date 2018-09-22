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
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class SpinnerAnimation(Gtk.Window):

    def __init__(self):

        Gtk.Window.__init__(self, title="Spinner")
        self.set_border_width(3)
        self.connect("destroy", Gtk.main_quit)

        self.button = Gtk.ToggleButton("Start Spinning")
        self.button.connect("toggled", self.on_button_toggled)
        self.button.set_active(False)

        self.spinner = Gtk.Spinner()

        self.table = Gtk.Table(3, 2, True)
        self.table.attach(self.button, 0, 2, 0, 1)
        self.table.attach(self.spinner, 0, 2, 2, 3)

        self.add(self.table)
        self.show_all()

    def on_button_toggled(self, button):

        if button.get_active():
            self.spinner.start()
            self.button.set_label("Stop Spinning")

        else:
            self.spinner.stop()
            self.button.set_label("Start Spinning")


myspinner = SpinnerAnimation()

Gtk.main()
