#!/usr/bin/python
# -*- coding: utf-8 -*-

from chempy import Substance
ferricyanide = Substance.from_formula('Fe(CN)6-3')
ferricyanide.composition == {0: -3, 26: 1, 6: 6, 7: 6}  # 0 for charge
print(ferricyanide.unicode_name)
print(ferricyanide.latex_name + ", " + ferricyanide.html_name)
print('%.3f' % ferricyanide.mass)
