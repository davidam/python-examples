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

import hyphen
h = hyphen.Hyphenator('en_US')
print(h.syllables(u"Hammond's"))
#It's just included in one syllable
# [u'Ham', u"mond's"]
# But if I do the same using the German dictionary

h = hyphen.Hyphenator('de_CH')
print(h.syllables(u"Hammond's"))
print(h.syllables(u"Bismarck'sche"))


h2 = hyphen.Hyphenator('es_ES')
print(h2.syllables(u"David"))
print(h2.syllables(u"María"))
print(h2.syllables(u"Diego"))
print(h2.syllables(u"Laura"))
print("Bug found:")
print(h2.syllables(u"Irene"))
