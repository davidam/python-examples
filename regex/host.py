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
#!/usr/bin/python# -*- coding: utf-8 -*-
import re

p = '(?:http.*://)?(?P<host>[^:/ ]+).?(?P<port>[0-9]*).*'
regex = 'http[s]?://(www\.)?([a-z]*\.)*(?P<host>[a-z]*)\.(?P<ext>[a-z]*)?'

m = re.search(p,'http://www.abc.com:123/test')
print(m.group('host')) # 'www.abc.com'
print(m.group('port')) # '123'

m2 = re.search(regex,'http://madrid.elpais.es')
print(m2.group('host')) # 'www.abc.com'
print(m2.group('ext')) # '123'
