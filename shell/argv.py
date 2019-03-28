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
#!/usr/bin/env python
import sys

if __name__ == "__main__":
    # The first argument of sys.argv is always the filename,
    # meaning that the length of system arguments will be
    # more than one, when command-line arguments exist.
    if len(sys.argv) > 2:
            num1 = float(sys.argv[1])
            num2 = float(sys.argv[2])
    else:
            print("This command takes two arguments and adds them")
            print("Less than two arguments given.")
            sys.exit(1)
    print("%s" % str(num1 + num2))
