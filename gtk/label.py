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

class LabelWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Label Example")
        
        hbox = Gtk.Box(spacing=10)
        hbox.set_homogeneous(False)
        vbox_left = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox_left.set_homogeneous(False)
        vbox_right = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox_right.set_homogeneous(False)
        
        hbox.pack_start(vbox_left, True, True, 0)
        hbox.pack_start(vbox_right, True, True, 0)
        
        label = Gtk.Label("This is a normal label")
        vbox_left.pack_start(label, True, True, 0)
        
        label = Gtk.Label()
        label.set_text("This is a left-justified label.\nWith multiple lines.")
        label.set_justify(Gtk.Justification.LEFT)
        vbox_left.pack_start(label, True, True, 0)
        
        label = Gtk.Label(
            "This is a right-justified label.\nWith multiple lines.")
        label.set_justify(Gtk.Justification.RIGHT)
        vbox_left.pack_start(label, True, True, 0)
        
        label = Gtk.Label("This is an example of a line-wrapped label.  It "
                          "should not be taking up the entire             "
                          "width allocated to it, but automatically "
                          "wraps the words to fit.\n"
                          "     It supports multiple paragraphs correctly, "
                          "and  correctly   adds "
                          "many          extra  spaces. ")
        label.set_line_wrap(True)
        vbox_right.pack_start(label, True, True, 0)
        
        label = Gtk.Label("This is an example of a line-wrapped, filled label. "
                          "It should be taking "
                          "up the entire              width allocated to it.  "
                          "Here is a sentence to prove "
                          "my point.  Here is another sentence. "
                          "Here comes the sun, do de do de do.\n"
                          "    This is a new paragraph.\n"
                          "    This is another newer, longer, better "
                          "paragraph.  It is coming to an end, "
                          "unfortunately.")
        label.set_line_wrap(True)
        label.set_justify(Gtk.Justification.FILL)
        vbox_right.pack_start(label, True, True, 0)

        label = Gtk.Label()
        label.set_markup("Text can be <small>small</small>, <big>big</big>, "
                         "<b>bold</b>, <i>italic</i> and even point to "
                         "somewhere in the <a href=\"http://www.gtk.org\" "
                         "title=\"Click to find out more\">internets</a>.")
        label.set_line_wrap(True)
        vbox_left.pack_start(label, True, True, 0)

        label = Gtk.Label.new_with_mnemonic(
            "_Press Alt + P to select button to the right")
        vbox_left.pack_start(label, True, True, 0)
        label.set_selectable(True)

        button = Gtk.Button(label="Click at your own risk")
        label.set_mnemonic_widget(button)
        vbox_right.pack_start(button, True, True, 0)

        self.add(hbox)

window = LabelWindow()        
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
