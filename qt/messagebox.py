#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
import sys
from PyQt4.QtGui import *
 
# Create an PyQT4 application object.
a = QApplication(sys.argv)       
 
# The QWidget widget is the base class of all user interface objects in PyQt4.
w = QWidget()
 
# Show a message box
result = QMessageBox.question(w, 'Message', "Do you like Python?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
 
if result == QMessageBox.Yes:
    print('Yes.')
    w.setWindowTitle("That's a good feeling! Python is the most popular scripting language")
else:
    print('No.')
    w.setWindowTitle("Perhaps you prefer Perl, Ruby or TCL")
 
 
# Show window
w.show() 
 
sys.exit(a.exec_())
