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

import unittest
from app.calculator import Calculator

class TddInPythonExample(unittest.TestCase):

    def test_calculator_add_method_returns_correct_result(self):
        calc = Calculator()
        result = calc.add(2,2)
        self.assertEqual(4, result)

    def test_calculator_sub_method_returns_correct_result(self):
        calc = Calculator()
        result = calc.sub(2,2)
        self.assertEqual(0, result)


    def test_calculator_prod_method_returns_correct_result(self):
        calc = Calculator()
        result = calc.prod(2,2)
        self.assertEqual(4, result)

    def test_calculator_div_method_returns_correct_result(self):
        calc = Calculator()
        result = calc.div(2,2)
        self.assertEqual(1, result)

    def test_calculator_prodUsingAdd_method_returns_correct_result(self):
        calc = Calculator()
        result = calc.prodUsingAdd(5,4)
        self.assertEqual(20, result)

if __name__ == '__main__':
    unittest.main()
