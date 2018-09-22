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
from gi.repository.GdkPixbuf import Pixbuf

icons = ["edit-cut", "edit-paste", "edit-copy"]

class IconViewWindow(Gtk.Window):

  def __init__(self):
    Gtk.Window.__init__(self)
    self.set_default_size(200, 200)

    liststore = Gtk.ListStore(Pixbuf, str)
    iconview = Gtk.IconView.new()
    iconview.set_model(liststore)
    iconview.set_pixbuf_column(0)
    iconview.set_text_column(1)

    for icon in icons:
        pixbuf = Gtk.IconTheme.get_default().load_icon(icon, 64, 0)
        liststore.append([pixbuf, "Label"])

    self.add(iconview)

win = IconViewWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
