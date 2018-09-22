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
from app.primes import Primes

class TddInPythonExample(unittest.TestCase):

    def test_primes_divisible_method_returns_correct_result(self):
        p = Primes()
        result = p.divisible(4, 2)
        self.assertEqual(result, True)

    def test_primes_generateList_method_returns_correct_result(self):
        p = Primes()
        result = p.generateList(2, 11)
        self.assertEqual([2, 3, 4, 5, 6, 7, 8, 9, 10, 11], result)

    def test_primes_dividers_method_returns_correct_result(self):
        p = Primes()
        result = p.dividers(4)
        self.assertEqual([1, 2, 4], result)

    def test_primes_primes_method_returns_correct_result(self):
        p = Primes()
        result = p.primes(4)
        self.assertEqual([1, 2, 3], result)


if __name__ == '__main__':
    unittest.main()
